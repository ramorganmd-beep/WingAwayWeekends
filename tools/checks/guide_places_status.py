"""Check the hotels and restaurants named in every guide (Stay and Eat cards) against Google Places business status.
Usage: python3 tools/checks/guide_places_status.py OUT.json [slug ...]
Needs network access to places.googleapis.com with the API key added by the environment (X-Goog-Api-Key).
Each card name is searched near the guide's destination (40 km bias). Results are for a person to review:
"NOT_FOUND" or a different name is a prompt to look, not proof of closure.
"""
import html, json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
s = (ROOT / 'docs/destinations.js').read_text(); D = {d['guide'].strip('/'): d for d in json.loads(s[s.index('['):s.rindex(']') + 1]) if d.get('guide')}
only = set(sys.argv[2:])
items = []
for slug, d in D.items():
    if only and slug not in only: continue
    p = ROOT / 'docs' / slug / 'index.html'
    if not p.exists(): continue
    t = p.read_text()
    for sec in ('stay', 'eat'):
        m = re.search(r'<section id="%s".*?</section>' % sec, t, re.S)
        if not m: continue
        for card in re.findall(r'<article class="card">(.*?)</article>', m.group(0), re.S):
            h = re.search(r'<h3>(.*?)</h3>', card, re.S)
            if not h: continue
            name = html.unescape(re.sub(r'<[^>]+>', '', h.group(1))).strip()
            if not name or name.lower().startswith('our ') or ' guide' in name.lower(): continue
            items.append(dict(slug=slug, section=sec, name=name, town=f"{d['name'].split(' & ')[0]}, {d.get('stateCode') or d['state']}", lat=d['lat'], lon=d['lon']))
def check(it):
    body = {'textQuery': it['name'] + ' ' + it['town'], 'maxResultCount': 1,
            'locationBias': {'circle': {'center': {'latitude': it['lat'], 'longitude': it['lon']}, 'radius': 40000}}}
    req = urllib.request.Request('https://places.googleapis.com/v1/places:searchText', data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json', 'X-Goog-FieldMask': 'places.displayName,places.businessStatus,places.formattedAddress,places.googleMapsUri'})
    for attempt in range(3):
        try:
            r = json.load(urllib.request.urlopen(req, timeout=30)).get('places', []); break
        except Exception as e:
            r = None; err = str(e)[:80]; time.sleep(2 * (attempt + 1))
    if r is None: return dict(it, status='ERROR', error=err)
    p = r[0] if r else {}
    return dict(it, match=p.get('displayName', {}).get('text'), status=p.get('businessStatus', 'NOT_FOUND' if not r else 'UNKNOWN'),
                address=p.get('formattedAddress'), maps=p.get('googleMapsUri'))
with ThreadPoolExecutor(6) as ex: out = list(ex.map(check, items))
json.dump(out, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(len(out), 'places;', Counter(o['status'] for o in out))
