"""Move the $100 Hamburger link out of page headers (one-off; run on docs/**/*.html and templates)."""
import re, sys
from pathlib import Path
LINK = re.compile(r'<a class="header-link" href="((?:\.\./)*)fly-to-lunch/"[^>]*>\$100 Hamburger</a>')
for p in map(Path, sys.argv[1:]):
    s = p.read_text()
    m = LINK.search(s)
    if not m:
        continue
    hdr_end = s.find('</header>', m.end())
    has_map = re.search(r'class="header-link" href="(?:\.\./)*map/"', s[m.end():hdr_end]) or re.search(r'class="header-link" href="(?:\.\./)*map/"', s[max(0, m.start()-800):m.start()])
    rep = '' if has_map else f'<a class="header-link" href="{m.group(1)}map/">Map</a>'
    p.write_text(s[:m.start()] + rep + s[m.end():])
    print(p, 'removed' if has_map else '-> Map')
