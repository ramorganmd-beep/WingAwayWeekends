"""Add a "Luxury alternatives" row under Where to stay in destination guides.

Usage: python3 tools/guides/luxury.py docs/*/index.html

Idempotent: removes a previously inserted row and re-adds it. Entries are
(tag, name, description[, URL[, link text]]). Charleston's
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
         'A lodge-style luxury hotel at the entrance to Biltmore Village, steps from the estate gates. Ideal for a Biltmore-centered weekend.',
         'https://www.grandbohemianasheville.com/'),
        ('Downtown · Curio Collection', 'The Foundry Hotel',
         'A boutique hotel in a restored steel foundry downtown, with polished rooms and a short walk to dinner.',
         'https://www.foundryasheville.com/'),
        ('Downtown · Small & stylish', 'The Windsor Boutique Hotel',
         'A small, highly rated boutique hotel downtown with apartment-style suites.',
         'https://windsorasheville.com/')],
    'pinehurst': [
        ('Upgrade · Suites', 'The Carolina Hotel',
         'The Carolina is already the area’s luxury standard. For a step up, ask about its suites, or a resort villa or cottage for more space.',
         'https://www.pinehurst.com/accommodations/the-carolina-hotel/'),
        ('Nearby · Classic', 'Pine Needles Lodge',
         'A long-running golf lodge on a Donald Ross course in Southern Pines. Not grand luxury, but warm, polished and golf-first.',
         'https://pineneedleslodge.com/')],
    'beaufort': [
        ('Ultra-luxury · About 45 minutes', 'Montage Palmetto Bluff',
         'A destination resort on the May River near Bluffton, with a spa, golf and riverside cottages. A splurge worth the drive; plan a car.',
         'https://www.montage.com/palmettobluff/')],
    'st-augustine': [
        ('Oceanfront · About 30 minutes north', 'Ponte Vedra Inn & Club',
         'A classic oceanfront resort in Ponte Vedra Beach with a spa, golf and beach club. Choose it for beach time; drive into the old city for the sights.',
         'https://www.pontevedra.com/'),
        ('Oceanfront · Quieter', 'The Lodge & Club at Ponte Vedra Beach',
         'The smaller sister property, with oceanfront rooms and a relaxed feel.',
         'https://www.pontevedra.com/stay/lodge')],
    'greenville': [
        ('Travelers Rest · Countryside', 'Hotel Domestique',
         'A small, European-style luxury hotel in the foothills near Travelers Rest, about 30 minutes from downtown, with mountain views and a quiet setting. Pair it with a ride on the Swamp Rabbit Trail.',
         'https://hoteldomestique.com/')],
    'charlottesville': [
        ('Manor house · 100 acres', 'The Clifton',
         'A romantic historic manor on about 100 acres outside town, with fine dining and a quiet country setting.',
         'https://www.the-clifton.com/'),
        ('Near UVA · Kimpton', 'Kimpton The Forum Hotel',
         'A polished, newer boutique hotel beside the University of Virginia, with a restaurant and bar. Choose it to stay in town, close to dinner.',
         'https://www.forumhotelcharlottesville.com/')],
    'nashville': [
        ('Riverfront · Five-star', 'Four Seasons Hotel Nashville',
         'A tower on the Cumberland River downtown with skyline views, a spa and polished service.',
         'https://www.fourseasons.com/nashville/'),
        ('Historic · Train station', 'Union Station Hotel',
         'A grand 1900 railway station turned hotel, with a vaulted lobby and stained glass. Walkable to The Gulch and downtown.',
         'https://www.unionstationhotelnashville.com/'),
        ('The Gulch · Rooftop', 'Thompson Nashville',
         'A stylish hotel in The Gulch with a rooftop bar and strong restaurants downstairs.',
         'https://www.hyatt.com/hotel/tennessee/thompson-nashville/bnath')],
    'key-west': [
        ('Private island', 'Sunset Key Cottages',
         'Cottages on a private island a short launch ride from Old Town, home to Latitudes. The ultimate Key West splurge.'),
        ('Old Town · On the water', 'Pier House Resort & Spa',
         'A waterfront resort at the end of Duval Street with a private beach and spa, steps from Mallory Square.'),
        ('Old Town · Garden oasis', 'The Gardens Hotel',
         'A small luxury hotel set in lush tropical gardens in Old Town, often rated among the island’s best.')],
    'outer-banks': [
        ('Oceanfront · Rent a house', 'Luxury beach homes',
         'The Outer Banks’ real luxury is a private oceanfront house in Duck, Corolla or Nags Head, often with a pool and hot tub. Book through a local rental agency; many require week-long stays in summer, with shorter stays off-season.'),
        ('Upgrade · Duck', 'Sanderling soundfront suites',
         'The Sanderling is already the area’s top resort. For a step up, ask about its soundfront suites and spa packages.',
         'https://www.thesanderling.com/')],
    'amelia-island': [
        ('Upgrade · Oceanfront', 'Club level at The Ritz-Carlton',
         'The Ritz-Carlton’s club level adds a private lounge with food and drinks throughout the day, on top of the oceanfront setting and spa.',
         'https://www.ritzcarlton.com/en/about-the-ritz-carlton/experience/club-level/'),
        ('More space · Resort villas', 'Omni oceanfront villas',
         'Omni Amelia Island’s villas and suites give you room to spread out, with the resort’s spa, golf and restaurants close by.',
         'https://www.omnihotels.com/hotels/villas-amelia-island')],
    'yadkin-valley': [
        ('Winery cabins · Historic', 'Grassy Creek Klondike Cabins',
         'Restored historic cabins at Grassy Creek Vineyard & Winery near Elkin, with the tasting room a short walk away.',
         'https://www.theklondikecabins.com/'),
        ('More space · Rental', 'Vineyard cottage rentals',
         'The valley’s most indulgent stays are private cottages and farmhouses near the wineries. Look for one with a porch and a view of the vines.',
         'https://www.airbnb.com/rooms/872256673641256276', 'See an example rental')],
    'hunt-country': [
        ('Three Michelin stars · About 45 minutes', 'The Inn at Little Washington',
         'Opulent rooms above one of America’s great restaurants. Pair dinner and a night here for the ultimate splurge.'),
        ('Upgrade · Salamander', 'Salamander suites',
         'Salamander is already the area’s luxury standard. For a step up, ask about its suites, with more space and views over the estate.')],
    'dahlonega': [
        ('Bed & breakfast · Spa', 'Mountain Laurel Creek Inn & Spa',
         'A small, highly rated inn in the woods outside town with its own spa and multi-course breakfasts. Quiet and romantic.')],
    'gulf-shores': [
        ('Upgrade · Gulf-front suites', 'Turquoise Place suites',
         'Turquoise Place’s largest suites add wraparound Gulf views and private balcony hot tubs. Ideal for a slow, indulgent weekend.'),
        ('Private · Beach house', 'Gulf-front beach homes',
         'A private beach house in Orange Beach or Fort Morgan, often with a pool. Book through a local rental agency; summer stays may require a week.')],
    'chattanooga': [
        ('Upgrade · River views', 'The Edwin suites',
         'The Edwin is already the city’s romantic choice. For a step up, ask for a river-view suite overlooking the Walnut Street Bridge.'),
        ('Historic inn · Fort Wood', 'Mayor’s Mansion Inn',
         'A restored Victorian mansion turned bed and breakfast in a quiet historic neighborhood near downtown. Intimate and romantic.')],
    'smoky-mountains': [
        ('Ultra-luxury · Walland', 'Blackberry Farm',
         'One of America’s most celebrated country hotels, in the foothills near Townsend, known for its food, wine and service. About 25 minutes from KTYS. A once-in-a-lifetime splurge.'),
        ('Mountaintop · Walland', 'Blackberry Mountain',
         'Blackberry Farm’s sister resort on a mountain preserve, with stone cottages, hiking and wellness at its heart.')],
}

ROW_RE = re.compile(r'<h3 class="subhead" data-lux>Luxury alternatives</h3><div class="grid three">.*?</div>(?=</section>)', re.S)


def card(tag, name, body, href=None, link_text='Official details'):
    link = (f'<a class="textlink" href="{href}" target="_blank" rel="noopener">{link_text}'
            f'<span class="sr"> for {name}</span></a>') if href else ''
    return f'<article class="card"><div class="tag">{tag}</div><h3>{name}</h3><p>{body}</p>{link}</article>'


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
