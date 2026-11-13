"""Add a "Getting into town" box under each guide's route box.

Usage: python3 tools/guides/ground.py docs/<guide>/index.html [...]

One short, scannable block per guide: crew car, rental car, rideshare, how far
town is, and whether a downtown weekend works without a rental car. Pilot perks
(fly-in discounts, pilot rates) appear only where confirmed. Every entry carries
the month it was checked and a reminder to call the FBO, because crew cars and
perks change often. Idempotent: the block sits between <!--wa-ground--> markers.
"""
import re
import sys
from pathlib import Path

# guide folder -> facts. Keep each value short; the guide body has the detail.
GROUND = {
    'knoxville': {
        'fbo': 'Signature Knoxville',
        'crew': 'Listed by Signature; ask when you call ahead',
        'rental': 'At the FBO (Go Rentals) and in the terminal',
        'ride': 'Uber and Lyft; about 25 minutes downtown',
        'norental': 'Yes, for a downtown weekend: ride in, then walk Market Square and the Old City',
        'checked': 'Nov 2026',
    },
    'smoky-mountains': {
        'fbo': 'Gatlinburg-Pigeon Forge Airport',
        'crew': 'Recent pilot reports (2025–26) mention one for short trips; call ahead',
        'rental': 'Enterprise, picked up at the FBO; reserve by phone, as online booking isn’t offered',
        'ride': 'Limited; arrange a ride before you land',
        'town': 'About 30 minutes to Gatlinburg and the park entrance',
        'norental': 'No: plan on a rental car for the park and Gatlinburg',
        'checked': 'Nov 2026',
    },
    'asheville': {
        'fbo': 'Signature Asheville',
        'crew': 'Listed by Signature; ask when you call ahead',
        'rental': 'On site at the FBO; a car service can be booked through the FBO',
        'ride': 'Uber and Lyft; about 20 minutes downtown',
        'norental': 'Yes, for a downtown weekend; you’ll want a car for the Blue Ridge Parkway or Biltmore',
        'checked': 'Nov 2026',
    },
    'chattanooga': {
        'fbo': 'Wilson Air Center',
        'crew': 'Listed, run through Go Rentals; one pilot reports a minimum age of 25',
        'rental': 'Through the FBO; arrange ahead',
        'ride': 'No rideshare pickup on the GA ramp; arrange a car or taxi ahead',
        'town': 'About 15 minutes downtown',
        'norental': 'Yes, for a downtown weekend: downtown is walkable and a free electric shuttle runs through it; you’ll want a car for Lookout Mountain',
        'checked': 'Nov 2026',
    },
}

ROWS = [('crew', 'Crew car'), ('rental', 'Rental car'), ('ride', 'Rideshare'), ('town', 'Into town'),
        ('norental', 'No rental car needed?'), ('perks', 'Pilot perks')]
MARK = re.compile(r'<!--wa-ground-->.*?<!--/wa-ground-->', re.S)
STYLE = ('<style>.wa-ground{margin:14px 0 4px;padding:14px 18px;background:#fff;border:1px solid #dbe3e9;'
         'border-left:4px solid #efbd70;border-radius:3px;font-size:.95rem}.wa-ground h3{margin:0 0 8px;font-size:1rem;'
         'color:#102d40}.wa-ground dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 14px;margin:0}'
         '.wa-ground dt{font-weight:700;color:#102d40}.wa-ground dd{margin:0;color:#33475a}.wa-ground p{margin:8px 0 0;'
         'font-size:.85rem;color:#647784}@media(max-width:560px){.wa-ground dl{grid-template-columns:1fr}'
         '.wa-ground dd{margin-bottom:6px}}</style>')


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def block(g):
    rows = ''.join(f'<dt>{label}</dt><dd>{esc(g[k])}</dd>' for k, label in ROWS if g.get(k))
    return ('<!--wa-ground-->' + STYLE + '<div class="wa-ground" aria-label="Getting into town"><h3>Getting into town</h3>'
            f'<dl><dt>FBO</dt><dd>{esc(g["fbo"])}</dd>{rows}</dl>'
            f'<p>Checked {esc(g["checked"])}. Crew cars and pilot perks change often: call the FBO before you go. '
            'Know something we missed? <a href="mailto:hello@wingawayweekends.com?subject=Getting%20into%20town">Tell us</a>.</p>'
            '</div><!--/wa-ground-->')


def main(paths):
    for p in map(Path, paths):
        key = p.parent.name
        if key not in GROUND:
            continue
        s = MARK.sub('', p.read_text())
        anchor = '<!--/wa-wx-->'
        assert s.count(anchor) == 1, p
        s = s.replace(anchor, anchor + block(GROUND[key]))
        p.write_text(s)
        print('ground:', p)


if __name__ == '__main__':
    main(sys.argv[1:])
