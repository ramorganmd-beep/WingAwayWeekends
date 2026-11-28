"""Check Fly to Lunch spots against Google Places business status.
Usage: python3 tools/checks/places_status.py OUT.json
Needs network access to places.googleapis.com with the API key added by the environment (X-Goog-Api-Key).
For each spot: text search for its name, biased to 15 km around its airport; records Google's top match,
its businessStatus (OPERATIONAL, CLOSED_TEMPORARILY, CLOSED_PERMANENTLY) and its Maps link. Planning aid only:
a person reviews every flag before anything is removed.
"""
import json, re, sys, time, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
s = (ROOT / 'docs/fly-to-lunch/index.html').read_text()
blk = s[s.index('SPOTS'):]; blk = blk[:blk.index('];')]
ap = {}
for m in re.finditer(r'\["([^"]+)","([^"]*)","[^"]*","([^"]*)","([^"]*)",(-?[\d.]+),(-?[\d.]+)\]', (ROOT / 'docs/airports-us.js').read_text()):
    v = (float(m.group(5)), float(m.group(6)), m.group(3), m.group(4)); ap[m.group(1)] = v; ap.setdefault(m.group(2), v)
spots = []
for m in re.finditer(r"\{code:'([^']+)'(.*?)checked:'(?:[^'\\]|\\.)*'\}", blk, re.S):
    code, body = m.groups()
    g = lambda k: (re.search(k + r":'((?:[^'\\]|\\.)*)'", body) or [None, ''])[1].replace("\\'", "'")
    lat = re.search(r'lat:(-?[\d.]+), lon:(-?[\d.]+)', body)
    a = ap.get(code)
    ll = (float(lat.group(1)), float(lat.group(2))) if lat else (a[:2] if a else None)
    city = g('city') or (a[2].title() + ', ' + a[3] if a else '')
    spots.append(dict(code=code, name=g('name'), city=city, ll=ll))
out = []
for sp in spots:
    body = {'textQuery': sp['name'] + (' ' + sp['city'] if sp['city'] else ''), 'maxResultCount': 1}
    if sp['ll']: body['locationBias'] = {'circle': {'center': {'latitude': sp['ll'][0], 'longitude': sp['ll'][1]}, 'radius': 15000}}
    req = urllib.request.Request('https://places.googleapis.com/v1/places:searchText', data=json.dumps(body).encode(),
        headers={'Content-Type': 'application/json', 'X-Goog-FieldMask': 'places.displayName,places.businessStatus,places.formattedAddress,places.googleMapsUri'})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=30)).get('places', [])
    except Exception as e:
        r = []; sp['error'] = str(e)[:80]
    p = r[0] if r else {}
    out.append(dict(code=sp['code'], name=sp['name'], city=sp['city'], match=p.get('displayName', {}).get('text'),
                    status=p.get('businessStatus', 'NOT_FOUND' if not r else 'UNKNOWN'), address=p.get('formattedAddress'), maps=p.get('googleMapsUri')))
    time.sleep(0.15)
json.dump(out, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(Counter(o['status'] for o in out))
