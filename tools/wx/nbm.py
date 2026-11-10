"""Fetch the National Blend of Models (NBM) station text guidance and write compact JSON for the weather outlook.

Usage: python3 tools/wx/nbm.py OUT_DIR [--cycle YYYYMMDDHH] [--src DIR]

Reads two NOAA bulletins for one model run:
  NBS (short range): every 3 hours to 72 hours, with ceiling, visibility, wind, gusts, sky, rain, thunder.
  NBE (extended): every 12 hours to about 8 days, with wind, gusts, sky, rain, thunder (no ceiling or visibility).
Writes OUT_DIR/run.json (run time) and OUT_DIR/st/<bucket>.json, stations grouped by the first two characters
of their ID so a page loads only the small file it needs.
Source: https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/ (public, NOAA/NWS).
"""
import argparse, datetime as dt, json, os, re, sys, urllib.request
from collections import defaultdict
from pathlib import Path

BASE = 'https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod'
UA = 'WingAwayWeekends-wx/0.1 (https://wingawayweekends.com; hello@wingawayweekends.com)'
CA = os.environ.get('REQUESTS_CA_BUNDLE') or ('/root/.ccr/ca-bundle.crt' if os.path.exists('/root/.ccr/ca-bundle.crt') else None)
NBS_ROWS = ['CIG', 'VIS', 'LCB', 'IFC', 'IFV', 'SKY', 'WDR', 'WSP', 'GST', 'P06', 'T03', 'TMP']
NBE_ROWS = ['SKY', 'WDR', 'WSP', 'GST', 'P12', 'T12', 'TMP']

def get(url):
    import ssl
    ctx = ssl.create_default_context(cafile=CA) if CA else None
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
        return r.read().decode('latin-1')

def latest_cycle():
    now = dt.datetime.now(dt.timezone.utc)
    for back in range(0, 30):
        c = now - dt.timedelta(hours=back)
        d, h = c.strftime('%Y%m%d'), c.strftime('%H')
        try:
            idx = get(f'{BASE}/blend.{d}/{h}/text/')
        except Exception:
            continue
        if 'blend_nbstx' in idx and 'blend_nbetx' in idx:
            return d + h
    raise SystemExit('no recent NBM run with both bulletins')

def parse(text, rows):
    """Return {station: {'fhr': [...], ROW: [...]}} from an NBM text bulletin."""
    out = {}
    for block in re.split(r'\n(?= *[A-Z0-9]{3,5} +NBM )', text):
        m = re.match(r' *([A-Z0-9]{3,5}) +NBM', block)
        if not m:
            continue
        lines = block.split('\n')
        fhr_line = next((l for l in lines if l[1:4] == 'FHR'), None)
        if not fhr_line:
            continue
        ends = [mm.end() for mm in re.finditer(r'\d+', fhr_line[4:])]
        ends = [e + 4 for e in ends]
        st = {'fhr': [int(fhr_line[e - 3:e]) for e in ends]}
        for l in lines:
            key = l[1:4]
            if key in rows:
                vals = []
                for e in ends:
                    s = l[e - 3:e].strip() if len(l) >= e - 3 else ''
                    vals.append(int(s) if re.fullmatch(r'-?\d+', s or 'x') else None)
                st[key] = vals
        out[m.group(1)] = st
    return out

ROOT = Path(__file__).resolve().parents[2]

def bucket(sid):
    """File a station lives in: KMY for KMYR, CY for CYYZ, 0W for 0W3. The page computes the same name."""
    return sid[:3] if sid.startswith('K') and len(sid) == 4 else sid[:2]

def wanted():
    """Stations worth keeping: U.S. public airports (docs/airports-us.js) and every destination airport."""
    ids = set()
    a = (ROOT / 'docs/airports-us.js').read_text()
    for code, alt in re.findall(r'\["([A-Z0-9]+)","([A-Z0-9]*)"', a):
        ids.update({code, alt, 'K' + code if len(code) == 3 else code} - {''})
    ids.update(re.findall(r'"airport": "([A-Z0-9]+)"', (ROOT / 'docs/destinations.js').read_text()))
    return ids

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('out'); ap.add_argument('--cycle'); ap.add_argument('--src')
    a = ap.parse_args()
    cyc = a.cycle or latest_cycle()
    d, h = cyc[:8], cyc[8:]
    def bulletin(kind):
        if a.src:
            return Path(a.src, f'{kind}.txt').read_text(errors='ignore')
        return get(f'{BASE}/blend.{d}/{h}/text/blend_{kind}.t{h}z')
    nbs, nbe = parse(bulletin('nbstx'), NBS_ROWS), parse(bulletin('nbetx'), NBE_ROWS)
    out = Path(a.out); (out / 'st').mkdir(parents=True, exist_ok=True)
    keep = wanted()
    fs = max((v['fhr'] for v in nbs.values()), key=len); fe = max((v['fhr'] for v in nbe.values()), key=len)
    buckets = defaultdict(dict)
    for sid in sorted((set(nbs) | set(nbe)) & keep):
        rec = {}
        for k, src, f in (('s', nbs, fs), ('e', nbe, fe)):
            if sid in src and src[sid]['fhr'] == f:
                rec[k] = {r: v for r, v in src[sid].items() if r != 'fhr'}
        if rec:
            buckets[bucket(sid)][sid] = rec
    for b, recs in buckets.items():
        (out / 'st' / f'{b}.json').write_text(json.dumps(recs, separators=(',', ':')))
    run = dt.datetime.strptime(cyc, '%Y%m%d%H').replace(tzinfo=dt.timezone.utc)
    n = sum(len(v) for v in buckets.values())
    (out / 'run.json').write_text(json.dumps({'run': run.strftime('%Y-%m-%dT%H:00Z'), 'fhrS': fs, 'fhrE': fe, 'stations': n,
                                             'source': 'NOAA/NWS National Blend of Models'}, separators=(',', ':')))
    print(f'run {cyc}: {len(nbs)} NBS, {len(nbe)} NBE stations, {len(buckets)} files', file=sys.stderr)

if __name__ == '__main__':
    main()
