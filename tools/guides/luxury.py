"""Add a "Luxury alternatives" row under Where to stay in destination guides.

Usage: python3 tools/guides/luxury.py docs/*/index.html

Idempotent: removes a previously inserted row and re-adds it. Charleston's
row lives in build_charleston.py instead, so it is skipped here. Run after
building a guide (with personalize.py and trip_plans.py).
"""
import re
import sys
from pathlib import Path

LUXURY = {
    'savannah': [
        ('Luxury Collection · Historic district', 'Perry Lane Hotel',
         'Savannah’s Luxury Collection hotel on East Perry Street, with art-filled rooms, a rooftop bar and a short walk to the squares.'),
        ('Grand inn · Victorian', 'The Gastonian',
         'A pair of 1868 mansions turned luxury inn, with fireplaces in the rooms and a quiet setting near Forsyth Park.'),
        ('Riverfront · Design-forward', 'The Alida',
         'A modern riverfront hotel with a rooftop bar, an easy walk to River Street and the historic district.')],
    'asheville': [
        ('Biltmore Village · Lodge style', 'Grand Bohemian Hotel Asheville',
         'A lodge-style luxury hotel at the entrance to Biltmore Village, steps from the estate gates. Ideal for a Biltmore-centered weekend.'),
        ('Downtown · Curio Collection', 'The Foundry Hotel',
         'A boutique hotel in a restored steel foundry downtown, with polished rooms and a short walk to dinner.'),
        ('Downtown · Small & stylish', 'The Windsor Boutique Hotel',
         'A small, highly rated boutique hotel downtown with apartment-style suites.')],
    'pinehurst': [
        ('Upgrade · The Carolina', 'Carolina suites',
         'The Carolina is already the area’s luxury standard. For a step up, ask about its suites, or a resort villa or cottage for more space.'),
        ('Nearby · Classic', 'Pine Needles Lodge',
         'A long-running golf lodge on a Donald Ross course in Southern Pines. Not grand luxury, but warm, polished and golf-first.')],
    'beaufort': [
        ('Ultra-luxury · About 45 minutes', 'Montage Palmetto Bluff',
         'A destination resort on the May River near Bluffton, with a spa, golf and riverside cottages. A splurge worth the drive; plan a car.'),
        ('Hilton Head · About an hour', 'The Inn & Club at Harbour Town',
         'An intimate luxury inn at Sea Pines on Hilton Head Island, next to the famous Harbour Town golf course and lighthouse.')],
    'st-augustine': [
        ('Oceanfront · About 30 minutes north', 'Ponte Vedra Inn & Club',
         'A classic oceanfront resort in Ponte Vedra Beach with a spa, golf and beach club. Choose it for beach time; drive into the old city for the sights.'),
        ('Oceanfront · Quieter', 'The Lodge & Club at Ponte Vedra Beach',
         'The smaller sister property, with oceanfront rooms and a relaxed feel.')],
    'greenville': [
        ('Travelers Rest · Countryside', 'Hotel Domestique',
         'A small, European-style luxury hotel in the foothills near Travelers Rest, about 30 minutes from downtown, with mountain views and a quiet setting. Pair it with a ride on the Swamp Rabbit Trail.')],
    'charlottesville': [
        ('Manor house · 100 acres', 'The Clifton',
         'A romantic historic manor on about 100 acres outside town, with fine dining and a quiet country setting.'),
        ('Downtown · Art hotel', 'Quirk Hotel',
         'A boutique art hotel near the Downtown Mall, with a gallery and rooftop bar. Choose it to be in town for dinner.')],
    'nashville': [
        ('Riverfront · Five-star', 'Four Seasons Hotel Nashville',
         'A tower on the Cumberland River downtown with skyline views, a spa and polished service.'),
        ('Historic · Train station', 'Union Station Hotel',
         'A grand 1900 railway station turned hotel, with a vaulted lobby and stained glass. Walkable to The Gulch and downtown.'),
        ('The Gulch · Rooftop', 'Thompson Nashville',
         'A stylish hotel in The Gulch with a rooftop bar and strong restaurants downstairs.')],
    'key-west': [
        ('Private island', 'Sunset Key Cottages',
         'Cottages on a private island a short launch ride from Old Town, home to Latitudes. The ultimate Key West splurge.'),
        ('Old Town · On the water', 'Pier House Resort & Spa',
         'A waterfront resort at the end of Duval Street with a private beach and spa, steps from Mallory Square.'),
        ('Old Town · Garden oasis', 'The Gardens Hotel',
         'A small luxury hotel set in lush tropical gardens in Old Town, often rated among the island’s best.')],
}

ROW_RE = re.compile(r'<h3 class="subhead" data-lux>Luxury alternatives</h3><div class="grid three">.*?</div>(?=</section>)', re.S)


def card(tag, name, body):
    return f'<article class="card"><div class="tag">{tag}</div><h3>{name}</h3><p>{body}</p></article>'


for path in map(Path, sys.argv[1:]):
    slug = path.parent.name
    if slug not in LUXURY:
        print('skip:', path)
        continue
    s = path.read_text()
    s = ROW_RE.sub('', s)
    row = ('<h3 class="subhead" data-lux>Luxury alternatives</h3><div class="grid three">'
           + ''.join(card(*c) for c in LUXURY[slug]) + '</div>')
    i = s.index('<section id="stay">')
    j = s.index('</section>', i)
    s = s[:j] + row + s[j:]
    path.write_text(s)
    print('luxury added:', path)
