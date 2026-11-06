"""Build docs/airports-us.js from the OurAirports airports.csv (public domain).

Usage: python3 tools/airports/build_airports.py path/to/airports.csv docs/airports-us.js

Keeps open U.S. land airports (small, medium and large) that have a K-prefixed
ICAO/GPS code or a three-character FAA ID, which approximates public-use fields.
Fields per airport: [code, alternate FAA ID, name, city, state, lat, lon].
"""
import csv, json, re, sys, datetime
src, out = sys.argv[1], sys.argv[2]
rows = []
for r in csv.DictReader(open(src, encoding='utf-8')):
    if r['iso_country'] != 'US' or r['type'] not in ('small_airport', 'medium_airport', 'large_airport'):
        continue
    state = r['iso_region'].split('-')[-1]
    gps, local, ident = r['gps_code'].strip(), r['local_code'].strip(), r['ident'].strip()
    icao = gps if re.fullmatch(r'K[A-Z][A-Z0-9]{2}', gps) else ''
    faa = local if re.fullmatch(r'[A-Z0-9]{3}', local) else ''
    if not (icao or faa):
        continue
    code = icao or faa
    alt = faa if icao and faa and 'K' + faa != icao else ''
    pic = (r.get('icao_code') or gps).strip()
    if not alt and state in ('AK', 'HI') and re.fullmatch(r'P[A-Z]{3}', pic):
        alt = pic  # Alaska/Hawaii ICAO codes (e.g. PATK) as the alternate ID
    full = r['name'].strip()
    name = re.sub(r'\s*\bAirport\b\s*(?=-|$)', ' ', full).replace('  ', ' ').strip()
    if ' ' not in name.split(' - ')[0]:
        name = full  # keep 'Airport' when the name is a single word, e.g. 'Lee Airport'
    name = re.sub(r'\s+-\s*', ' - ', name)
    rows.append([code, alt, name, r['municipality'].strip(), state, round(float(r['latitude_deg']), 4), round(float(r['longitude_deg']), 4)])
rows.sort(key=lambda x: x[0])
seen, uniq = set(), []
for x in rows:
    if x[0] in seen: continue
    seen.add(x[0]); uniq.append(x)
hdr = ('// U.S. public airports for WingAway flight-time estimates.\n'
       '// Fields: [code, alternate FAA ID, name, city, state, lat, lon]\n'
       f'// Source: OurAirports (https://ourairports.com/data/), public domain. Generated {datetime.date.today():%B %-d, %Y}.\n'
       '// Filter: all 50 states and DC; open land airports with a K-prefixed ICAO code or a 3-character FAA ID.\n')
open(out, 'w').write(hdr + 'window.WINGAWAY_AIRPORTS=' + json.dumps(uniq, ensure_ascii=False, separators=(',', ':')) + ';\n')
print(len(uniq), 'airports')
