"""Add a "Getting into town" block to each guide's aviation section, under the FBO panel.

Usage: python3 tools/guides/ground.py docs/<guide>/index.html [...]

One short, scannable block per guide: crew car, rental car, rideshare, how far
town is, and whether a downtown weekend works without a rental car. Pilot perks
(fly-in discounts, pilot rates) appear only where confirmed. Every entry carries
the month it was checked and a reminder to call the FBO, because crew cars and
perks change often. Idempotent: the block sits between <!--wa-ground--> markers.
"""
import json
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
    'san-luis-obispo': {
        'fbo': 'ACI Jet San Luis Obispo · 805-548-1330',
        'crew': 'Not confirmed; ask when you call ahead',
        'rental': 'Avis, Budget, Enterprise, Hertz and National at the airline terminal; the airport advises reserving ahead for evenings',
        'ride': 'Uber and Lyft serve the airport, but the airport warns drivers can be scarce in the evening',
        'town': 'About 10 minutes to downtown San Luis Obispo, 15 to Pismo Beach',
        'norental': 'Possible for a downtown weekend by rideshare; you’ll want a car for Pismo and wine country',
        'checked': 'Nov 2026',
    },
    'harris-ranch': {
        'fbo': 'Harris Ranch Airport · 559-935-0717, ext. 6444',
        'crew': 'None needed: the hotel and restaurants are a short walk from the tie-downs',
        'rental': 'None on the field',
        'town': 'Everything for an overnight stop is on the resort property',
        'norental': 'Yes: walk from the airplane to your room and dinner',
        'checked': 'Nov 2026',
    },
    'halter-ranch': {
        'fbo': 'Halter Ranch fly-in requests · 805-226-9455',
        'crew': 'None needed for a visit: the tasting room and restaurant are on the estate',
        'rental': 'None on the field; Paso Robles (KPRB) is 11 nm east',
        'town': 'Paso Robles is about 11 nm east; arrange a car or taxi ahead',
        'norental': 'Yes, for a fly-in lunch and tasting on the estate',
        'checked': 'Nov 2026',
    },
    'block-island': {
        'fbo': 'No FBO. Airport parking and safety brief on 122.85, or call 401-466-5511',
        'crew': 'None on the field (pilot report)',
        'rental': 'Not at the airport; rental cars, scooters and bikes are in town',
        'ride': 'Taxis are plentiful and meet the planes',
        'town': 'A pleasant 20-minute walk into town',
        'norental': 'Yes: walk or take a taxi into town, then rent bikes or a scooter',
        'checked': 'Nov 2026; pilot report from a Cirrus SR20 owner',
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
    'charleston': {
        'fbo': 'Atlantic Aviation Charleston · 843-746-7600',
        'crew': 'Listed by Atlantic Aviation; ask when you call ahead',
        'rental': 'Go Rentals at the FBO; airline-terminal rental counters are a short ride away',
        'ride': 'Uber and Lyft; confirm the pickup point at the FBO entrance',
        'town': 'About 12 miles to the historic district, 20–30 minutes',
        'norental': 'Yes: ride in, then walk the peninsula',
        'checked': 'Nov 2026',
    },
    'savannah': {
        'fbo': 'Sheltair Savannah · 912-965-0095',
        'crew': 'Listed as complimentary; ask when you call ahead',
        'rental': 'Hertz at the FBO; pilots report cars brought planeside',
        'ride': 'Uber and Lyft serve the airport; confirm pickup at the FBO; taxi or car service as a fallback',
        'town': 'About 10 miles to the Historic District, 15–20 minutes',
        'norental': 'Yes: ride in, then walk the squares',
        'checked': 'Nov 2026',
    },
    'key-west': {
        'fbo': 'Signature Key West · 305-296-5439',
        'crew': 'Listed by Signature; ask when you call ahead',
        'rental': 'National and other providers through the FBO',
        'ride': 'Taxis; Signature lists local taxi and limo partners',
        'town': 'Old Town is about 10 minutes by taxi',
        'norental': 'Yes: walk or bike Old Town; parking is scarce',
        'checked': 'Nov 2026',
    },
    'nantucket': {
        'fbo': 'Nantucket Memorial Airport (town-run FBO, next to the terminal)',
        'crew': 'Not confirmed; ask when you call ahead',
        'rental': 'Available at the airport; book well ahead in summer',
        'ride': 'Taxis, plus Uber and Lyft; seasonal shuttle buses run from the airport',
        'town': 'About 3 miles to town',
        'norental': 'Yes: taxis and shuttles in, then bikes and walking',
        'checked': 'Nov 2026',
    },
    'bar-harbor': {
        'fbo': 'Modern Aviation · Bar Harbor · 207-667-5534',
        'crew': 'Not confirmed; ask when you call ahead',
        'rental': 'Hertz year-round and Enterprise (May–October) at counters in the terminal',
        'ride': 'The free Island Explorer bus runs from the airport to Mount Desert Island in summer (late June to mid-October); taxis otherwise',
        'town': 'About 20 minutes to downtown Bar Harbor',
        'norental': 'Possible in summer: the Island Explorer links the airport, town and park; otherwise rent a car',
        'checked': 'Nov 2026',
    },
    'jackson-hole': {
        'fbo': 'Jackson Hole Flight Services · 307-733-4767',
        'crew': 'Not confirmed; ask when you call ahead',
        'rental': 'Avis, Budget, Enterprise, Hertz and National on site at the airport',
        'ride': 'Uber and Lyft run but can be scarce in peak season; taxis and shuttles too',
        'town': 'About 9–10 miles to the town of Jackson, roughly 20 minutes',
        'norental': 'No: plan on a rental car for the park',
        'checked': 'Nov 2026',
    },
    'sedona': {
        'fbo': 'Red Rock Aviation · 928-282-1046',
        'crew': 'None, according to the airport',
        'rental': 'Sedona Car Rentals on the field rents by the hour when cars are available; call ahead. Hertz and Enterprise may deliver',
        'ride': 'Taxi or shuttle; arrange before you land',
        'town': 'The airport sits on a mesa above town, a few minutes’ drive to West Sedona and Uptown',
        'norental': 'No: plan on a car for the trailheads',
        'checked': 'Nov 2026',
    },
    'santa-barbara': {
        'fbo': 'Signature Santa Barbara · 805-967-5608',
        'crew': 'Not confirmed; ask when you call ahead',
        'rental': 'Enterprise and National through Signature; most major companies at the terminal. Atlantic Aviation is the other FBO',
        'ride': 'Uber and Lyft; about 15 minutes to downtown',
        'town': 'About 8 miles to downtown and State Street',
        'norental': 'Yes, for a downtown weekend: ride in, then walk State Street and the waterfront; you’ll want a car for wine country',
        'checked': 'Nov 2026',
    },
}

GROUND['mackinac'] = {
    'crew': 'None: there is no FBO, and cars are not allowed on the island',
    'rental': 'None: no cars on Mackinac Island',
    'town': 'Horse-drawn taxi from the airport into town; arrange it ahead of time',
    'norental': 'Yes: horses, bikes and walking',
    'checked': 'Nov 2026', 'nocars': True,
}

ROWS = [('crew', 'Crew car'), ('rental', 'Rental car'), ('ride', 'Rideshare'), ('town', 'Into town'),
        ('norental', 'No rental car needed?'), ('perks', 'Pilot perks')]
MARK = re.compile(r'<!--wa-ground-->.*?<!--/wa-ground-->', re.S)
STYLE = ('<style>.wa-ground{margin:16px 0 12px;padding:14px 18px;background:#fff;border:1px solid #dbe3e9;'
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
            f'<dl>{rows}</dl>'
            + (f'<p>Checked {esc(g["checked"])}. No cars on the island: plan on the taxi, bikes and your own two feet. '
               if g.get('nocars') else
               f'<p>Checked {esc(g["checked"])}. Crew cars and pilot perks change often: call the FBO before you go. '
               '<a href="../rental-cars/">How to have a rental car waiting at the FBO</a> · ')
            + 'Know something we missed? <a href="mailto:hello@wingawayweekends.com?subject=Getting%20into%20town">Tell us</a>.</p>'
            '</div><!--/wa-ground-->')


NEEDS_CAR = re.compile(r'rental|\bcar\b', re.I)
NO_CAR = re.compile(r'walk|shuttle|rideshare|\bride\b|pickup|transfer|uber|lyft|taxi|trolley|bike|golf cart|boat|ferry|van|tram|resort', re.I)


RIDES = json.load(open(Path(__file__).with_name('rideshare.json')))['guides']


def rideshare(slug):
    r = RIDES.get(slug)
    if not r:
        return ''
    who = 'Uber and Lyft both list' if r['uber'] and r['lyft'] else ('Uber lists' if r['uber'] else 'Lyft lists')
    return f"{who} service in {r['town']}; drivers can be few near a small airport, so ask the FBO"


def auto_block(s, slug=''):
    """A plainer box for guides without hand-checked details, built from what the guide already says."""
    m = re.search(r'<div class="fbo"><div><strong>([^<]+)</strong>.*?</div>(?:<a href="(tel:[^"]+)">([^<]+)</a>)?', s, re.S)
    t = re.search(r'data-transport="([^"]+)"', s) or re.search(r'WEEKEND STYLE</span><strong[^>]*>[^<]*<small>· ([^<]+)</small>', s)
    if not m or not t:
        return ''
    fbo = m.group(1) + (f' · <a href="{m.group(2)}">{m.group(3)}</a>' if m.group(2) else '')
    way = t.group(1)
    plain = re.sub(r'crew car|courtesy car', '', way, flags=re.I)
    if NEEDS_CAR.search(plain) and (not NO_CAR.search(plain) or re.match(r'(rental )?car( and| \+)', plain, re.I)):
        norental = 'No: plan on a rental car'
    elif not NEEDS_CAR.search(plain):
        norental = 'Likely: ' + way[0].lower() + way[1:]
    else:
        norental = ''
    rows = [('Crew car', 'Ask when you call the FBO ahead'),
            ('Rental car', 'Ask the FBO which companies deliver there, and about any delivery fee'),
            ('Rideshare', rideshare(slug))]
    dl = ''.join(f'<dt>{k}</dt><dd>{esc(v)}</dd>' for k, v in rows if v)
    return ('<!--wa-ground-->' + STYLE + '<div class="wa-ground" aria-label="Getting into town"><h3>Getting into town</h3>'
            f'<dl>{dl}</dl>'
            '<p>Crew cars change often: call the FBO before you go. '
            '<a href="../rental-cars/">How to have a rental car waiting at the FBO</a> · Know something we missed? '
            '<a href="mailto:hello@wingawayweekends.com?subject=Getting%20into%20town">Tell us</a>.</p>'
            '</div><!--/wa-ground-->')


def main(paths):
    n = 0
    for p in map(Path, paths):
        key = p.parent.name
        s = MARK.sub('', p.read_text())
        i = s.find('<section id="flight"')
        if i < 0 or 'data-dest=' not in s:
            continue
        j = s.index('</section>', i)
        k = s.find('<div class="arrival-main">', i, j)
        if k < 0:
            print('ground: skipped (no aviation section):', p)
            continue
        b = block(GROUND[key]) if key in GROUND else auto_block(s, key)
        if not b:
            print('ground: skipped (no FBO or transport found):', p)
            continue
        # after the last FBO card in the aviation section (before its notes)
        nt = s.find('<p class="note">', k, j)
        end = s.find('</div><aside>', k, j)
        at = nt if nt >= 0 else (end if end >= 0 else j)
        s = s[:at] + b + s[at:]
        p.write_text(s)
        n += 1
    print(f'ground: {n} guides')


if __name__ == '__main__':
    main(sys.argv[1:])
