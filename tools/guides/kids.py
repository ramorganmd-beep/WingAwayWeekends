"""Add a "Best for kids" box to family guides, just before the flight section.

Usage: python3 tools/guides/kids.py docs/<slug>/index.html [...]
Idempotent (replaces the block between wa-kids markers). Guides not in KIDS are left without a box.
Facts in KIDS are checked by hand; airport notes come from the airport listing, not from memory.
"""
import re, sys
from pathlib import Path
START, END = '<!--wa-kids-->', '<!--/wa-kids-->'
BLOCK = re.compile(r'\n?' + re.escape(START) + '.*?' + re.escape(END), re.S)
KIDS = {
    'mackinac': dict(
        ages='3 to 12',
        why='No cars on the island: kids can bike, ride in a horse-drawn carriage and walk everywhere.',
        top=['Bike the flat eight-mile road around the island; rent bikes, trailers and tag-alongs in town.',
             'Fort Mackinac, with soldiers in period uniform and cannon and rifle firings through the day in season.',
             'A horse-drawn carriage tour, and watching the fudge being made on the marble slabs in the shops.'],
        airport='KMCD has a 3,501 ft runway, no fuel and no FBO, and a landing fee. Arrive with fuel for the return, and arrange the horse-drawn taxi into town ahead of time.'),
}
def block(k):
    d = KIDS[k]
    tops = ''.join(f'<li>{t}</li>' for t in d['top'])
    return (START + '<section id="kids" style="padding-top:0"><div style="background:#eef5f9;border:1px solid #c9dde8;border-radius:3px;padding:20px 22px">'
            '<span class="eyebrow">Flying with children</span><h2 style="margin:6px 0 8px">Best for kids</h2>'
            f'<p style="margin:0 0 10px"><b>Best ages: {d["ages"]}.</b> {d["why"]}</p>'
            f'<p style="margin:0 0 4px;font-weight:700">Top three for kids</p><ol style="line-height:1.6;margin:0 0 10px;padding-left:22px;list-style:decimal">{tops}</ol>'
            f'<p style="margin:0;font-size:15px"><b>At the airport:</b> {d["airport"]}</p></div></section>' + END)
for path in map(Path, sys.argv[1:]):
    k = path.parent.name; s = BLOCK.sub('', path.read_text())
    if k in KIDS:
        i = s.find('<section id="flight"')
        s = s[:i] + block(k) + '\n' + s[i:]
    path.write_text(s)
