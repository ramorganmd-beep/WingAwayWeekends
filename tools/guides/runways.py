"""Add the longest land runway to each destination in docs/destinations.js.

Usage: python3 tools/guides/runways.py /path/to/nasr   (folder with FAA NASR APT_BASE.csv and APT_RWY.csv)

Sets "rwy" (feet) on every destination whose airport is in the NASR data, and
"rwySurf" ("turf", "gravel", "dirt" ...) when that runway is not paved.
Water lanes are ignored. Re-run after adding destinations or a new NASR cycle.
"""
import csv, json, re, sys
from pathlib import Path

nasr = Path(sys.argv[1])
dest = Path(__file__).resolve().parents[2] / 'docs' / 'destinations.js'

icao = {}
for b in csv.DictReader(open(nasr / 'APT_BASE.csv', encoding='latin-1')):
    if b.get('ICAO_ID'):
        icao[b['ICAO_ID']] = b['ARPT_ID']

rw = {}
for r in csv.DictReader(open(nasr / 'APT_RWY.csv', encoding='latin-1')):
    surf = r['SURFACE_TYPE_CODE']
    if not surf or surf.startswith('WATER'):
        continue
    try:
        ln = int(float(r['RWY_LEN'] or 0))
    except ValueError:
        continue
    if ln > rw.get(r['ARPT_ID'], (0, ''))[0]:
        rw[r['ARPT_ID']] = (ln, surf)

def lookup(code):
    for k in (icao.get(code), code, code[1:] if len(code) == 4 and code[0] == 'K' else None):
        if k and k in rw:
            return rw[k]
    return None

def surface(code):
    if code.startswith(('ASPH', 'CONC', 'PEM')):
        return None
    for word, label in (('TURF', 'turf'), ('GRAV', 'gravel'), ('GRVL', 'gravel'), ('DIRT', 'dirt'), ('SAND', 'sand')):
        if word in code:
            return label
    return code.lower()

src = dest.read_text()
# Edit in place next to each "airport" field so the file's existing formatting is kept.
src = re.sub(r', "rwy": \d+(, "rwySurf": "[a-z ]+")?', '', src)
missing = []
def add(m):
    code = m.group(1)
    found = lookup(code)
    if not found:
        missing.append(code)
        return m.group(0)
    extra = f', "rwy": {found[0]}'
    s = surface(found[1])
    if s:
        extra += f', "rwySurf": "{s}"'
    return f'"airport": "{code}"{extra}'
src = re.sub(r'"airport": "([A-Z0-9]+)"', add, src)
dest.write_text(src)
n = len(re.findall(r'"airport": "', src))
print(f'{n - len(missing)} of {n} destinations with runway lengths; missing: {missing or "none"}')
