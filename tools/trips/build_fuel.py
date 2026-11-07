"""Build docs/trips/fuel-airports.js from FAA NASR CSVs (APT_BASE.csv, APT_RWY.csv).
Usage: python3 tools/trips/build_fuel.py /path/to/nasr
Keeps open, public-use land airports that list 100LL and/or Jet A and have a paved runway of 3,000 feet or more.
Fields: [code, name, city, state, lat, lon, fuel (1=100LL, 2=Jet A, 3=both), longest paved runway ft]
"""
import csv, json, sys
from pathlib import Path
nasr = Path(sys.argv[1])
rw = {}
for r in csv.DictReader(open(nasr / 'APT_RWY.csv', encoding='latin-1')):
    if any(s in r['SURFACE_TYPE_CODE'] for s in ('ASPH', 'CONC')):
        try: rw[r['ARPT_ID']] = max(rw.get(r['ARPT_ID'], 0), int(float(r['RWY_LEN'] or 0)))
        except ValueError: pass
out = []
for b in csv.DictReader(open(nasr / 'APT_BASE.csv', encoding='latin-1')):
    if b['SITE_TYPE_CODE'] != 'A' or b['FACILITY_USE_CODE'] != 'PU' or b['ARPT_STATUS'] != 'O': continue
    f = b['FUEL_TYPES'].replace(' ', '').split(',')
    av = any(x.startswith('100') for x in f); jet = any(x.startswith('A') for x in f)
    L = rw.get(b['ARPT_ID'], 0)
    if not (av or jet) or L < 3000: continue
    code = b['ICAO_ID'] or b['ARPT_ID']
    out.append([code, b['ARPT_NAME'].title()[:40], b['CITY'].title(), b['STATE_CODE'], round(float(b['LAT_DECIMAL']), 4), round(float(b['LONG_DECIMAL']), 4), (1 if av else 0) + (2 if jet else 0), L])
Path('docs/trips/fuel-airports.js').write_text('// Public airports with fuel and a paved runway of 3,000 ft or more, from FAA NASR data. Built by tools/trips/build_fuel.py. Planning use only: confirm fuel before you go.\nwindow.WINGAWAY_FUEL=' + json.dumps(out, separators=(',', ':')) + ';\n')
print(len(out), 'airports')
