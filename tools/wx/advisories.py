"""Fetch current aviation weather advisories and recent pilot reports for the weather outlook's route check.

Usage: python3 tools/wx/advisories.py OUT_DIR      (writes OUT_DIR/adv.json)

Source: Aviation Weather Center data API (https://aviationweather.gov/data/api/), public, NOAA/NWS:
  G-AIRMETs (icing, turbulence, IFR, mountain obscuration, low-level wind shear, strong surface wind), forecast
  hours 0-12; SIGMETs and convective SIGMETs; Center Weather Advisories; PIREPs of icing or turbulence, last 2 hours.
Only areas are kept (not freezing-level contour lines). Times are epoch milliseconds.
"""
import json, os, ssl, sys, time, urllib.request
from datetime import datetime
from pathlib import Path

API = 'https://aviationweather.gov/api/data/'
UA = 'WingAwayWeekends-wx/0.1 (https://wingawayweekends.com; hello@wingawayweekends.com)'
CA = os.environ.get('REQUESTS_CA_BUNDLE') or ('/root/.ccr/ca-bundle.crt' if os.path.exists('/root/.ccr/ca-bundle.crt') else None)
CTX = ssl.create_default_context(cafile=CA) if CA else None


def get(q):
    req = urllib.request.Request(API + q, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        d = json.loads(r.read().decode('utf-8') or '[]')
    return d if isinstance(d, list) else []


def ms_iso(s):
    return int(datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp() * 1000)


def poly(coords):
    return [[round(float(c['lat']), 3), round(float(c['lon']), 3)] for c in coords or []]


def alt(v):
    """G-AIRMET levels: '080' = 8,000 ft, 'SFC', 'FZL' (freezing level) kept as words."""
    if v in (None, ''):
        return None
    return int(v) * 100 if str(v).isdigit() else str(v)


def main():
    out = []
    seen = set()
    for fore in (0, 3, 6, 9, 12):
        for g in get(f'gairmet?format=json&fore={fore}'):
            if g.get('geom') != 'AREA' or g.get('hazard') in ('FZLVL', 'M_FZLVL'):
                continue
            t = ms_iso(g['validTime'])
            key = (g['tag'], g['hazard'], t)
            if key in seen:
                continue
            seen.add(key)
            base = alt(g.get('base'))
            out.append({'k': 'gairmet', 'hz': g['hazard'], 'sev': g.get('severity'), 'due': g.get('due_to'),
                        'base': base, 'top': alt(g.get('top')), 'fzl': [alt(g.get('fzlbase')), alt(g.get('fzltop'))] if base == 'FZL' else None,
                        't0': t - 90 * 60000, 't1': t + 90 * 60000, 'p': poly(g.get('coords'))})
        time.sleep(1)
    for s in get('airsigmet?format=json'):
        if not s.get('coords'):
            continue
        out.append({'k': s.get('airSigmetType', 'SIGMET').lower(), 'hz': s.get('hazard'), 'sev': s.get('severity'),
                    'base': s.get('altitudeLow1'), 'top': s.get('altitudeHi1'),
                    't0': s['validTimeFrom'] * 1000, 't1': s['validTimeTo'] * 1000, 'p': poly(s['coords'])})
    for c in get('cwa?format=json'):
        if not c.get('coords'):
            continue
        out.append({'k': 'cwa', 'hz': c.get('hazard'), 'base': c.get('base'), 'top': c.get('top'), 'by': c.get('name'),
                    't0': c['validTimeFrom'] * 1000, 't1': c['validTimeTo'] * 1000, 'p': poly(c['coords'])})
    pireps = []
    for r in get('pirep?format=json&age=2&bbox=17,-170,72,-50'):
        ice, turb = (r.get('icgInt1') or '').strip(), (r.get('tbInt1') or '').strip()
        if (not ice or ice == 'NEG') and (not turb or turb == 'NEG'):
            continue
        pireps.append({'t': r['obsTime'] * 1000, 'lat': r['lat'], 'lon': r['lon'], 'fl': r.get('fltLvl'), 'ac': r.get('acType'),
                       'ice': ice if ice != 'NEG' else '', 'turb': turb if turb != 'NEG' else '', 'raw': r.get('rawOb', '')[:200]})
    o = Path(sys.argv[1]); o.mkdir(parents=True, exist_ok=True)
    (o / 'adv.json').write_text(json.dumps({'made': int(time.time() * 1000), 'adv': out, 'pireps': pireps}, separators=(',', ':')))
    print(f'{len(out)} advisories, {len(pireps)} icing/turbulence PIREPs', file=sys.stderr)


if __name__ == '__main__':
    main()
