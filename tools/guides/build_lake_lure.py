"""Generate docs/lake-lure/index.html (Lake Lure and Chimney Rock, North Carolina)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 2, 2026'  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['lake-lure']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='lake-lure', name='Lake Lure', state='North Carolina', number=19, reviewed=REVIEWED,
    description='A curated two-night Lake Lure and Chimney Rock getaway for GA pilots and their partners, from KMYR to KFQD. A mountain lake in Hickory Nut Gorge, Chimney Rock State Park and a historic 1927 inn.',
    lede='A mountain lake, back after the storm.',
    intro='Lake Lure fills a steep, forested gorge below Chimney Rock, the setting for Dirty Dancing and The Last of the Mohicans. Hurricane Helene hit the gorge hard in 2024; the lake reopened in May 2026 and Chimney Rock State Park in 2025. Visiting now is a lovely weekend and real support for a community still rebuilding.',
    pills=['Mountain lake', 'Chimney Rock', 'Historic inn'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KFQD', nm=182, flight_time='~1 hr 28 <small>min</small>',
    style='Courtesy or rental car', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land in the foothills, drive up the gorge.',
    'KFQD, Rutherford County Airport (Marchman Field), is about 25–30 minutes from Lake Lure by car.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Rutherford County Airport', '110 Marchman Field Drive, Rutherfordton, NC 28139', '828-287-0800') +
    '<p class="note">The county lists full-service fuel and a courtesy car during regular hours (about 9–6 daily); directories also list 828-755-7261 for the FBO. The courtesy car suits a short trip; for a two-night stay, arrange a rental car ahead. Ask about parking and fees. No live fuel price is shown.</p>'
    '<p class="note">The Blue Ridge escarpment rises sharply to the west. Review terrain, the sectional and current NOTAMs, and watch for mountain weather and low clouds in the gorge.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>You’ll want a car.</h3><p>The airport, the lake and Chimney Rock are spread along US 64 and 74A. Some roads and businesses in the gorge are still being repaired; check current conditions before you drive.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your view of the lake.',
    'A historic inn on the water, a resort with mountain trails, or a lake house of your own. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Historic · 1927', 'Lake Lure Inn & Spa',
         'The grand old hotel of the gorge, across the road from the lake. New owners plan renovations through 2026–27 while it stays open; confirm which rooms and services are available.',
         'https://lakelurenc.com/') +
    card('Resort · Lake & golf', 'Rumbling Bald on Lake Lure',
         'A large resort on the lake’s north shore with a lakeside restaurant, golf, a wellness center and rental homes and condos.',
         'https://rumblingbald.com/stay/') +
    card('Private · Lake house', 'Lake Lure vacation rentals',
         'A lakefront house with a dock and hot tub is the classic way to stay. Ask whether boats and the dock are usable under current lake rules.',
         'https://www.hometogo.com/f/lake-lure/cabin/', 'Browse lake cabins') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Lakeside and unhurried.',
    'Dining here is casual. Hours are still settling after the storm; call ahead and reserve where you can.') +
    '<div class="grid three">' +
    card('Friday dinner · On the lake', 'Legends on the Lake',
         'Rumbling Bald’s lakeside restaurant, with pizza, burgers, salads and steaks and a view of the water.',
         'https://rumblingbald.com/amenities/#section-dining-at-rumbling-bald') +
    card('Saturday dinner · Historic inn', 'The Veranda at Lake Lure Inn',
         'Dinner at the 1927 inn, with a drink first in the Moose & Goose Lounge. Confirm hours during renovations.',
         'https://lakelurenc.com/dining/') +
    card('Alternative · Italian', 'La Strada at Lake Lure',
         'A relaxed Italian restaurant near the lake. A good second-night option.',
         'https://lastradaatlakelure.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Up the rock, out on the water.',
    'Check what is open before you go; recovery is still under way in places.') +
    '<div class="explore-list">' +
    explore(1, 'Chimney Rock State Park',
            'Climb to the top of Chimney Rock for the view straight down Hickory Nut Gorge to the lake, and walk to Hickory Nut Falls, seen in The Last of the Mohicans. Some trails may still be closed; check before you go.',
            'https://www.ncparks.gov/state-parks/chimney-rock-state-park', 'Park information') +
    explore(2, 'A boat on Lake Lure',
            'A lake tour or a rented boat is the best way to see the gorge from the water. The lake reopened in 2026 with some temporary rules, including no-wake areas; ask what is running. Lake Lure Adventure Company offers rentals and guided outings on the water; check what is running for your dates.',
            'https://lakelureadventurecompany.com/', 'Lake Lure Adventure Company') +
    explore(3, 'Lake Lure Beach',
            'The town beach reopened for Memorial Day 2026. Pack a picnic and spend an afternoon by the water in summer.') +
    explore(4, 'Rumbling Bald and Bat Cave hikes',
            'Granite cliffs and boulder fields on the lake’s north shore, popular with hikers and climbers.') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the town. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Summer', 'Lake season',
         'Boating, the beach and long evenings on the water. Book lodging early.') +
    card('Mid–late October', 'Fall color',
         'The gorge turns gold and red. Beautiful, and the busiest weekends of the year.') +
    card('Year-round', 'A community rebuilding',
         'Some businesses are still reopening after Helene. Your visit helps; be patient with closures and check ahead.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the town’s site for lake rules and events, and confirm dates with the organizer.</p></div>'
    '<a class="button" href="https://www.townoflakelure.com/" target="_blank" rel="noopener">Town of Lake Lure</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the lake, Chimney Rock and two relaxed dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & the lake', [
        ('Late-morning arrival', 'Land at KFQD, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Drive up the gorge, check in and get out on the water.'),
        ('Evening', 'Dinner at Legends on the Lake.')]) +
    day('SAT', 'Chimney Rock', [
        ('Morning', 'Chimney Rock State Park, early, before the crowds.'),
        ('Afternoon', 'A lazy afternoon at the beach or a lake tour.'),
        ('Evening', 'A drink in the Moose & Goose Lounge, then dinner at the Lake Lure Inn.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast by the lake and a short hike at Rumbling Bald.'),
        ('Before leaving', 'Return the car and allow time at the FBO during its hours.'),
        ('Fly home', 'Mountain clouds can linger in the morning; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and a car first, then dinners and any boat rental.'),
          ('Still recovering', 'Some roads, trails and businesses are still being repaired after Helene. Check current status before you go.'),
          ('Lake rules', 'The lake reopened with temporary rules on boats and speed. Ask your lodging or the town.'),
          ('FBO hours', 'The airport keeps daytime hours. Plan arrivals and departures accordingly.')]) +
    '</section>')

P.append(page_end(number=19, place='Lake Lure, North Carolina', reviewed=REVIEWED, note='Researched while the gorge is still recovering from Hurricane Helene. Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
