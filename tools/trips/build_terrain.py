"""Build docs/trips/terrain.js from the FAA NASR APT_BASE.csv.
Usage: python3 tools/trips/build_terrain.py /path/to/nasr
WINGAWAY_HIGH: open airports (public or private) at 3,000 ft or higher, [id, lat, lon, elev ft], a rough proxy for
high terrain near a route. WINGAWAY_ELEV: field elevation for every guide airport. Planning use only.
"""
import csv, json, re, sys
from pathlib import Path
nasr = Path(sys.argv[1]); docs = Path(__file__).resolve().parents[2] / 'docs'
s = (docs / 'destinations.js').read_text(); D = json.loads(s[s.index('['):s.rindex(']') + 1])
want = {d['airport'] for d in D}
high, elev = [], {}
for b in csv.DictReader(open(nasr / 'APT_BASE.csv', encoding='latin-1')):
    if b['ARPT_STATUS'] != 'O' or not b['ELEV']: continue
    e = round(float(b['ELEV'])); ids = {b['ARPT_ID'], b['ICAO_ID']}
    for i in ids & want: elev[i] = e
    if b['SITE_TYPE_CODE'] == 'A' and e >= 3000:
        high.append([b['ICAO_ID'] or b['ARPT_ID'], round(float(b['LAT_DECIMAL']), 3), round(float(b['LONG_DECIMAL']), 3), e])
(docs / 'trips' / 'terrain.js').write_text('// Airport elevations from FAA NASR (APT_BASE.csv). Built by tools/trips/build_terrain.py. Planning use only.\n'
    'window.WINGAWAY_HIGH=' + json.dumps(high, separators=(',', ':')) + ';\nwindow.WINGAWAY_ELEV=' + json.dumps(elev, separators=(',', ':')) + ';\n')
print(len(high), 'high airports;', len(elev), 'of', len(want), 'guide airports')
