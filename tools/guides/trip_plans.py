"""Add trip-length plans (Day trip / Longer stay) to destination guides.

Usage: python3 tools/guides/trip_plans.py docs/*/index.html

Idempotent: removes any previously inserted plans and re-adds them. Marks the
route box's "Weekend style" value so docs/guide-route.js can relabel it, and
inserts two hidden plans into the itinerary section. guide-route.js shows the
one matching the visitor's trip length (?trip=... from the homepage cards, or
the last choice saved on the homepage). Run after building/personalizing a guide.
"""
import re
import sys
from pathlib import Path

PLANS = {
    'savannah': {
        'day': [('Arrive', 'Land at KSAV mid-morning and ride downtown.'),
                ('Midday', 'Walk Forsyth Park and a few squares, then lunch at The Collins Quarter or on River Street.'),
                ('Afternoon', 'Browse Broughton Street, then head back to the FBO for a late-afternoon departure.')],
        'extra': [('Morning', 'A private dolphin tour from Whitemarsh Island, or a sunrise walk along the river.'),
                  ('Afternoon', 'Starland District and a brewery stop at Two Tides or Hop Atomica.'),
                  ('Evening', 'Dinner at Vic’s on the River, or a sunset riverboat dinner cruise.')]},
    'charleston': {
        'day': [('Arrive', 'Land at KCHS mid-morning and ride to Patriots Point.'),
                ('Midday', 'Explore the USS Yorktown and its aircraft, then lunch downtown.'),
                ('Afternoon', 'A walk past Rainbow Row to the Battery, then back to the FBO.')],
        'extra': [('Morning', 'A slow morning on Lower King for antiques and galleries.'),
                  ('Afternoon', 'Fort Sumter by ferry from Liberty Square, then a brewery stop at Edmund’s Oast.'),
                  ('Evening', 'Dinner at Halls Chophouse.')]},
    'asheville': {
        'day': [('Arrive', 'Land at KAVL early and pick up a car.'),
                ('Midday', 'Biltmore House and gardens with a timed entry, plus lunch on the estate.'),
                ('Afternoon', 'Winery tasting for the non-pilot, then back to the airport before mountain afternoon weather builds.')],
        'extra': [('Morning', 'Drive the Blue Ridge Parkway for overlooks and a short walk, if open.'),
                  ('Afternoon', 'The Western North Carolina Air Museum in Hendersonville (open select days), or the River Arts District.'),
                  ('Evening', 'Sunset on the Grove Park Inn terrace and a relaxed dinner downtown.')]},
    'pinehurst': {
        'day': [('Arrive', 'Land at KSOP mid-morning and head to the village.'),
                ('Midday', 'Nine holes at The Cradle or a putting match at Thistle Dhu, then lunch at Pinehurst Brewing Co.'),
                ('Afternoon', 'A drink at The Deuce overlooking No. 2’s 18th green, then fly home.')],
        'extra': [('Morning', 'A second round at Mid Pines or Pine Needles, or a long spa morning.'),
                  ('Afternoon', 'Browse downtown Southern Pines and walk the Reservoir Park loop.'),
                  ('Evening', 'A brewery stop in Southern Pines or Aberdeen, then a quiet dinner in the village.')]},
    'beaufort': {
        'day': [('Arrive', 'Land at KARW mid-morning; borrow the courtesy car or arrange a ride across the river.'),
                ('Midday', 'Lunch on Bay Street, then a horse-drawn carriage tour of the historic district.'),
                ('Afternoon', 'The waterfront park swings, then back to the FBO well before it closes.')],
        'extra': [('Morning', 'The Spanish Moss Trail by bike or on foot.'),
                  ('Afternoon', 'The Parris Island Museum (check base access) or more beach time at Hunting Island.'),
                  ('Evening', 'A sunset boat outing from the downtown marina.')]},
    'st-augustine': {
        'day': [('Arrive', 'Land at KSGJ early and ride into the old city.'),
                ('Midday', 'Castillo de San Marcos, then lunch at The Columbia on St. George Street.'),
                ('Afternoon', 'A San Sebastian Winery tasting or a Flagler College tour, then fly home ahead of afternoon storms.')],
        'extra': [('Morning', 'Beach time on Anastasia Island or a quiet walk at Crescent Beach.'),
                  ('Afternoon', 'The St. Augustine Distillery tour and a wander through Lincolnville.'),
                  ('Evening', 'A sunset cruise on Matanzas Bay, then dinner at the Casa Monica.')]},
    'greenville': {
        'day': [('Arrive', 'Land at KGMU and ride ten minutes to Main Street.'),
                ('Midday', 'Falls Park and Liberty Bridge, then lunch on Main Street.'),
                ('Afternoon', 'A short bike ride on the Swamp Rabbit Trail, then back to the airport.')],
        'extra': [('Morning', 'Rent a car for a Blue Ridge drive: waterfalls, overlooks and small towns under an hour away.'),
                  ('Afternoon', 'Unity Park and The Commons food hall, or a Greenville Drive game in season.'),
                  ('Evening', 'A show at the Peace Center.')]},
    'charlottesville': {
        'day': [('Arrive', 'Land at KCHO early and pick up a car.'),
                ('Midday', 'Monticello with a timed entry, then lunch at a nearby winery.'),
                ('Afternoon', 'A stroll on the Downtown Mall, then back to the airport. Leave tastings to the passenger.')],
        'extra': [('Morning', 'Drive to Skyline Drive or the Blue Ridge Parkway for overlooks.'),
                  ('Afternoon', 'Barboursville Vineyards and its Jefferson-designed ruins, with lunch at the winery.'),
                  ('Evening', 'A relaxed dinner at your estate hotel.')]},
    'nashville': {
        'day': [('A long day', 'At about three hours each way from KMYR, Nashville is a stretch for a day trip; it works better from closer airports.'),
                ('Midday', 'Ryman Auditorium tour and lunch downtown.'),
                ('Afternoon', 'Country Music Hall of Fame, then back to KJWN with daylight to spare.')],
        'extra': [('Morning', 'Brunch and a wander through The Gulch or 12 South.'),
                  ('Afternoon', 'A tour of a historic home or a distillery outside town (you’ll want a car).'),
                  ('Evening', 'A quieter listening room for songwriters, then dinner at The Optimist.')]},
    'key-west': {
        'day': [('Not a day trip', 'At about four hours each way from KMYR, Key West is not a day trip from most of the Southeast.'),
                ('If you are closer', 'From south Florida airports: lunch at First Flight, then a bike loop through Old Town.'),
                ('Afternoon', 'Hemingway Home, then back to the FBO well before it closes.')],
        'extra': [('Morning', 'A snorkel or sail trip on the reef, or a lazy beach morning at Casa Marina.'),
                  ('Afternoon', 'Bike to the Southernmost Point and Fort Zachary Taylor’s beach.'),
                  ('Evening', 'A sunset sail, then a casual dinner in Old Town.')]},
    'outer-banks': {
        'day': [('Arrive', 'Land at KMQI mid-morning and take the courtesy car or a rental.'),
                ('Midday', 'Wright Brothers National Memorial, then lunch on the Manteo waterfront.'),
                ('Afternoon', 'A short climb at Jockey’s Ridge, then fly home before the afternoon winds build.')],
        'extra': [('Morning', 'Drive south through Cape Hatteras National Seashore toward the Cape Hatteras Lighthouse.'),
                  ('Afternoon', 'Beach time, or the North Carolina Aquarium on Roanoke Island.'),
                  ('Evening', 'In summer, The Lost Colony outdoor drama; otherwise a quiet dinner in Duck.')]},
    'amelia-island': {
        'day': [('Arrive', 'Land at KFHB mid-morning and borrow the crew car.'),
                ('Midday', 'Lunch downtown and a stroll up Centre Street to the harbor.'),
                ('Afternoon', 'Fort Clinch and a walk on the beach, then back to the FBO.')],
        'extra': [('Morning', 'A guided horseback ride on the beach.'),
                  ('Afternoon', 'A long spa afternoon at one of the oceanfront resorts.'),
                  ('Evening', 'A sunset river cruise, then dinner at Burlingame.')]},
    'yadkin-valley': {
        'day': [('Arrive', 'Land at KZEF mid-morning and pick up the courtesy car or a rental.'),
                ('Midday', 'Lunch and a tasting for the non-pilot at Shelton Vineyards.'),
                ('Afternoon', 'A glass on the terrace at Raffaldini for the non-pilot, then back to the FBO before it closes.')],
        'extra': [('Morning', 'Hike to the overlooks at Pilot Mountain or Stone Mountain State Park.'),
                  ('Afternoon', 'Downtown Elkin, or a side trip to Mount Airy.'),
                  ('Evening', 'Live music at the Reeves Theater.')]},
    'hunt-country': {
        'day': [('Arrive', 'Land at KJYO (SFRA procedures) or KHWY mid-morning and pick up a car.'),
                ('Midday', 'The Udvar-Hazy Center: the Space Shuttle, the SR-71 and more.'),
                ('Afternoon', 'Lunch and a stroll in Middleburg, with a tasting for the non-pilot, then fly home.')],
        'extra': [('Morning', 'Historic Leesburg and Morven Park.'),
                  ('Afternoon', 'A couples spa afternoon at Salamander.'),
                  ('Evening', 'A splurge dinner at The Inn at Little Washington, with a driver.')]},
    'dahlonega': {
        'day': [('Arrive', 'Land at KGVL mid-morning and pick up the rental car.'),
                ('Midday', 'Lunch on the square and the Gold Museum.'),
                ('Afternoon', 'A tasting-room stop on the square for the non-pilot, then the drive back to the FBO.')],
        'extra': [('Morning', 'Amicalola Falls and its staircase trail.'),
                  ('Afternoon', 'A gold-mine tour and a little panning.'),
                  ('Evening', 'Sunset with a glass at Wolf Mountain, then dinner on the square.')]},
}
STYLE_RE = re.compile(r'<span>WEEKEND STYLE</span><strong(?: data-style data-transport="[^"]*")?>Two nights <small>· ([^<]+)</small></strong>')


def block(kind, title, eyebrow, items):
    lis = ''.join(f'<li><strong>{t}</strong><p>{p}</p></li>' for t, p in items)
    return (f'<div class="trip-plan" data-trip="{kind}" hidden><span class="eyebrow">{eyebrow}</span>'
            f'<h3>{title}</h3><ol>{lis}</ol></div>')


for path in map(Path, sys.argv[1:]):
    slug = path.parent.name
    if slug not in PLANS:
        print('skip (no plans):', path)
        continue
    s = path.read_text()
    s = re.sub(r'<div class="trip-plan".*?</ol></div>', '', s)
    m = STYLE_RE.search(s)
    if not m:
        sys.exit(f'weekend style not found in {path}')
    s = s.replace(m.group(0), f'<span>WEEKEND STYLE</span><strong data-style data-transport="{m.group(1)}">Two nights <small>· {m.group(1)}</small></strong>', 1)
    p = PLANS[slug]
    day = block('Day trip', 'Just for the day', 'Day trip version', p['day'])
    extra = block('Longer stay', 'With an extra day', 'Longer stay · Add a day', p['extra'])
    i = s.index('<section id="itinerary">')
    j = s.index('<div class="days">', i)
    s = s[:j] + day + s[j:]
    k = s.index('</section>', j)
    s = s[:k] + extra + s[k:]
    path.write_text(s)
    print('trip plans added:', path)
