"""Add a "Make it a longer trip" box to guides that appear in a multi-stop trip route.

Usage: python3 tools/guides/trips_link.py docs/<slug>/index.html [...]
Idempotent (replaces the block between wa-trips markers). Routes come from tools/trips/build_trips.py.
A guide that is a default stop links to the route; a guide that is an alternative links to the route
with itself swapped in.
"""
import re, runpy, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ROUTES = runpy.run_path(str(ROOT / 'tools/trips/build_trips.py'))['ROUTES']
START, END = '<!--wa-trips-->', '<!--/wa-trips-->'
BLOCK = re.compile(re.escape(START) + '.*?' + re.escape(END), re.S)


def links(slug):
    out = []
    for r in ROUTES:
        stops = [[s, n] for s, n, _ in r['route']]
        if any(s == slug for s, _ in stops):
            out.append((r, f'../trips/{r["id"]}/', True))
            continue
        for i, (s, n, alts) in enumerate(r['route']):
            if slug in alts:
                st = [x[:] for x in stops]; st[i][0] = slug
                q = ','.join(f'{a}:{b}' for a, b in st).replace(':', '%3A').replace(',', '%2C')
                out.append((r, f'../trips/{r["id"]}/?stops={q}', False))
                break
    return out


def block(slug):
    L = links(slug)
    if not L:
        return ''
    items = ''.join(f'<li><a href="{u}">{r["h1"]}</a> <span style="color:#647784">· {sum(x[1] for x in r["route"])} nights{"" if main else ", with this stop swapped in"}</span></li>' for r, u, main in L)
    return (START + '<div class="wa-trips" style="margin:28px 0 0;padding:16px 20px;border:1px solid #eadcc0;border-radius:3px;background:#fbf6ec">'
            '<strong style="display:block;margin-bottom:6px">Make it a longer trip</strong>'
            '<p style="margin:0 0 6px;font-size:15px">This guide is part of a multi-stop flying trip. Set your dates and aircraft, then swap stops to make it your own.</p>'
            f'<ul style="margin:0;padding-left:18px;line-height:1.7">{items}</ul></div>' + END)


for path in map(Path, sys.argv[1:]):
    s = BLOCK.sub('', path.read_text())
    b = block(path.parent.name)
    if b:
        i = s.find('<section id="itinerary"')
        j = s.find('</section>', i) if i >= 0 else -1
        if j < 0:
            print('no itinerary section', path); continue
        s = s[:j] + b + s[j:]
    path.write_text(s)
