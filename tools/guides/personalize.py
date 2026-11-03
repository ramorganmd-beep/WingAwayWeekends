"""Add home-airport personalization to destination guide pages.

Usage: python3 tools/guides/personalize.py docs/<guide>/index.html [...]

Idempotent. Marks the route box with the destination airport and coordinates
(taken from docs/destinations.js), adds a note line and
loads airports-us.js and guide-route.js. Run after (re)building a guide.
"""
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[2] / 'docs'
import json
_src = (DOCS / 'destinations.js').read_text()
COORDS = {d['airport']: (d['lat'], d['lon']) for d in json.loads(_src[_src.index('=[') + 1:_src.rindex(';')])}

for path in map(Path, sys.argv[1:]):
    s = path.read_text()
    m = re.search(r'<div class="snapshot" aria-label="Trip snapshot"><div><span>YOUR ROUTE</span><strong>KMYR <span class="route-line">to</span> ([A-Z0-9]+)</strong>', s)
    if not m:
        if 'data-dest=' in s:
            print('already personalized:', path)
            continue
        sys.exit(f'route box not found in {path}')
    dest = m.group(1)
    lat, lon = COORDS[dest]
    s = s.replace('<div class="snapshot" aria-label="Trip snapshot">',
                  f'<div class="snapshot" aria-label="Trip snapshot" data-dest="{dest}" data-lat="{lat}" data-lon="{lon}">', 1)
    s = s.replace('<span>YOUR ROUTE</span><strong>', '<span>YOUR ROUTE</span><strong data-route>', 1)
    s = s.replace('<span>STRAIGHT-LINE DISTANCE</span><strong>', '<span>STRAIGHT-LINE DISTANCE</span><strong data-dist>', 1)
    s = s.replace('<span>ILLUSTRATIVE FLIGHT TIME</span><strong>', '<span>ILLUSTRATIVE FLIGHT TIME</span><strong data-time>', 1)
    i = s.index('<p class="estimate">')
    s = s[:i] + '<p class="estimate" id="route-note" hidden></p>' + s[i:]
    s = s.replace('</body>', '<script src="../airports-us.js"></script><script src="../aircraft.js"></script><script src="../guide-route.js"></script></body>', 1)
    path.write_text(s)
    print('personalized:', path, dest)
