"""Generate docs/chattanooga/index.html."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 2, 2026'  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['chattanooga']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='chattanooga', name='Chattanooga', state='Tennessee', number=17, reviewed=REVIEWED,
    description='A curated two-night Chattanooga getaway for GA pilots and their partners, from KMYR to KCHA. A walkable riverfront, Lookout Mountain, the Tennessee Aquarium and excellent dining.',
    lede='A river city with a mountain view.',
    intro='Chattanooga wraps around a bend of the Tennessee River below Lookout Mountain. Walk the riverfront and the pedestrian Walnut Street Bridge, ride the steep Incline Railway to the top of the mountain, and finish with dinner at some of the best restaurants in the state.',
    pills=['Riverfront', 'Lookout Mountain', 'Dining'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KCHA', nm=321, flight_time='~2 hr 24 <small>min</small>',
    style='Courtesy van + walks', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land about 15 minutes from downtown.',
    'KCHA, Chattanooga Metropolitan (Lovell Field), is a towered airport east of downtown with one full-service FBO.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Wilson Air Center', '932 Jubilee Drive, Chattanooga, TN 37421', '423-855-2299') +
    '<p class="note">Directories list a courtesy car or shuttle van and rental cars at Wilson Air Center. Arrange ground transport ahead; there is no rideshare pickup on the general aviation ramp. Ask about two-night parking and fees. No live fuel price is shown.</p>'
    '<p class="note">KCHA sits in Class C airspace among ridges, with Lookout Mountain and Signal Mountain nearby. Review terrain, the sectional and current NOTAMs.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Walk the riverfront.</h3><p>Downtown, the North Shore and the Southside are walkable, and a free electric shuttle runs through downtown. Rent a car, or use a taxi, for Lookout Mountain.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'A riverfront hotel, a grand historic one, or a stylish small one. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Riverfront · Autograph Collection', 'The Edwin Hotel',
         'A boutique hotel on the river between the Aquarium and the Hunter Museum, with a rooftop bar and views of the Walnut Street Bridge. The romantic choice.',
         'https://www.theedwinhotel.com/') +
    card('Historic · Downtown', 'The Read House',
         'A grand downtown hotel with roots in the 1870s, restored with Jazz Age glamour and an excellent bar. Walk to dinner.',
         'https://www.thereadhousehotel.com/') +
    card('Design hotel · Intimate', 'The Dwell Hotel',
         'A small, colorful boutique hotel in a restored historic building, with a cocktail bar and a retro-modern feel.',
         'https://thedwellhotel.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long lunch.',
    'Chattanooga punches well above its size for food. Reserve weekend dinners.') +
    '<div class="grid three">' +
    card('Friday dinner · Seafood', 'Easy Bistro & Bar',
         'A polished downtown bistro known for seafood, oysters and a lively bar. An easy, festive first night.',
         'https://www.easybistro.com/') +
    card('Saturday dinner · Southern fine dining', 'St. John’s Restaurant',
         'Seasonal Southern fine dining in a formal downtown room, with an award-winning wine list. The special-occasion dinner.',
         'https://www.stjohnsrestaurant.com/') +
    card('Alternative · Tasting menu', 'Calliope',
         'An inventive Levantine-inspired tasting menu, one of the city’s most talked-about tables. Book well ahead.',
         'https://www.callioperestaurant.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'River, mountain and a little nostalgia.',
    'Choose one outing a day and leave time for the riverfront.') +
    '<div class="explore-list">' +
    explore(1, 'Lookout Mountain',
            'Ride the Incline Railway, one of the steepest passenger railways in the world, to the top. Nearby, Rock City’s gardens and lookouts and the underground waterfall at Ruby Falls make a full morning.') +
    explore(2, 'Walnut Street Bridge & the North Shore',
            'A long pedestrian bridge across the Tennessee River to Coolidge Park, shops and cafés. Best at sunset.') +
    explore(3, 'Tennessee Aquarium',
            'Two buildings on the riverfront, following the water from the Appalachian mountains to the sea. Allow two to three hours.',
            'https://tnaqua.org/', 'Aquarium tickets') +
    explore(4, 'Bluff View Art District & Hunter Museum',
            'American art in a museum on a bluff over the river, with a sculpture garden, cafés and a walking path nearby.') +
    explore(5, 'The Chattanooga Choo Choo',
            'The restored 1909 Terminal Station on the Southside, with gardens, restaurants and the classic train. Fun for a stroll and a drink.',
            'https://choochoo.com/', 'Chattanooga Choo Choo') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the city calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('June', 'Riverbend Festival',
         'Chattanooga’s big riverfront music festival. Fun and crowded; book lodging early.',
         'https://www.riverbendfestival.com/') +
    card('October', 'Fall color',
         'The ridges around the city turn in mid-to-late October. The views from Lookout Mountain are at their best.') +
    card('November–January', 'Rock City lights',
         'Rock City’s holiday light show on top of Lookout Mountain. Timed tickets often sell out.',
         'https://www.seerockcity.com/enchanted-garden-of-lights/') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the city calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.chattanoogafun.com/" target="_blank" rel="noopener">Browse Chattanooga events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the riverfront, the mountain and two excellent dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & the river', [
        ('Late-morning arrival', 'Land at KCHA, subject to weather and your actual flight plan, and head downtown.'),
        ('Afternoon', 'Check in, then walk the Walnut Street Bridge to the North Shore.'),
        ('Evening', 'Dinner at Easy Bistro & Bar.')]) +
    day('SAT', 'Up the mountain', [
        ('Morning', 'The Incline Railway to Lookout Mountain, then Rock City or Ruby Falls.'),
        ('Afternoon', 'Lunch on the Southside and the Hunter Museum or the Aquarium.'),
        ('Evening', 'Dinner at St. John’s, then a nightcap at your hotel’s bar.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Brunch and a walk through the Bluff View Art District.'),
        ('Before leaving', 'Return the car or ride to the FBO, and allow time for departure.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and ground transport first, then dinners and attraction tickets.'),
          ('Timed tickets', 'Rock City, Ruby Falls and the Incline often use timed entry on busy weekends. Book ahead.'),
          ('Terrain', 'Ridges surround the city. Brief the departure and arrival with terrain in mind.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=17, place='Chattanooga, Tennessee', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
