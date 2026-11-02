"""Generate docs/greenville/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('wine', 'Drinks'),
       ('events', 'Sports & events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='greenville', name='Greenville', state='South Carolina', number=7,
    description='A curated two-night Greenville getaway for GA pilots and their partners, from KMYR to KGMU. Falls Park, a walkable Main Street, Michelin-recognized dining and the Swamp Rabbit Trail.',
    lede='Land downtown. Leave the car behind.',
    intro='A waterfall in the middle of the city, a tree-lined Main Street full of restaurants and the Blue Ridge on the horizon. Greenville Downtown Airport is minutes from it all.',
    pills=['Falls Park', 'Dining', 'Walkable downtown'],
    photo='greenville-falls-bridge', widths=[480, 960, 1600], alt='Reedy River waterfall beneath Liberty Bridge at Falls Park in Greenville', img_w=960, img_h=638,
    caption='Liberty Bridge over Reedy River Falls', airport='KGMU', nm=184, flight_time='~1 hr 29 <small>min</small>',
    style='Rideshare + walks', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then walk to dinner.',
    'KGMU, Greenville Downtown Airport, is a towered field just a few miles from Main Street. It is one of the closest-in airports in this collection.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The main FBO</h3>' +
    fbo('Vantage Aviation', '100 Tower Drive, Greenville, SC 29607', '864-232-7100') +
    '<p class="note">Full-service and self-serve 100LL are listed. Ask about handling fees, two-night parking, waivers with fuel and after-hours access. Directory prices vary, so call ahead; no live price is shown.</p>'
    '<p class="note">GMU is busy with business jets and training traffic. Review the airport diagram, tower procedures and the Greenville-Spartanburg (GSP) Class C airspace nearby.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Rideshare in. Walk everywhere.</h3><p>Main Street is about 10 minutes from the airport by rideshare. Downtown, Falls Park and most restaurants are walkable, and the Swamp Rabbit Trail starts in town.</p><p>A car is only needed for side trips into the mountains.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Three different stays. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('On Falls Park · Lodge style', 'Grand Bohemian Lodge',
         'A lodge-style hotel right beside Falls Park and the Reedy River, ranked among South Carolina’s best hotels for 2026. Wake up to the sound of the falls.') +
    card('Historic Main Street', 'The Westin Poinsett',
         'A grand 1925 hotel on Main Street with soaring ceilings and marble details, restored with Old World glamour. The classic downtown choice.') +
    card('Estate hotel · Splurge', 'Hotel Hartness',
         'A newer luxury hotel set on a large green estate a short drive from downtown, also ranked among the state’s best for 2026. Choose it for quiet and space.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long brunch.',
    'Greenville’s restaurant scene now has Michelin recognition. Reserve the special dinner well ahead.') +
    '<div class="grid three">' +
    card('Friday dinner · Italian', 'Jianna',
         'Handmade pasta and an oyster bar overlooking Main Street, recognized by Michelin. Lively and polished; ask for a window or balcony table.') +
    card('Saturday dinner · Michelin star', 'Scoundrel',
         'Chef Joe Cash’s restaurant, awarded a Michelin star. The special-occasion dinner of the weekend. Book as early as reservations open.') +
    card('Sunday brunch · Southern', 'Soby’s',
         'A downtown institution since 1997 for Southern cooking, with a wine list that won a Wine Spectator Grand Award in 2025. Confirm brunch hours.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'A waterfall downtown.',
    'Most of Greenville’s best experiences are free and within walking distance of Main Street.') +
    '<div class="explore-list">' +
    explore(1, 'Falls Park & Liberty Bridge',
            'Reedy River Falls in the middle of the city, with gardens and a curved pedestrian suspension bridge. Early morning and evening are the quietest and most beautiful times.') +
    explore(2, 'Swamp Rabbit Trail',
            'A paved greenway of more than 20 miles along the Reedy River, from downtown toward Travelers Rest. Rent bikes in town and ride to lunch.') +
    explore(3, 'Unity Park & The Commons',
            'A large riverside park on the trail, with a food hall nearby for a casual lunch.') +
    explore(4, 'Main Street',
            'Tree-lined, walkable and full of patios, galleries and shops. Look for the small bronze mice hidden along the street.') +
    explore(5, 'Blue Ridge day trip',
            'With a car, the mountains are under an hour away: waterfalls, overlooks and small towns. Save it for a longer stay.') +
    '</div></section>')

P.append('<section id="wine">' + head('05', 'Drinks', 'A glass, and no hurry.',
    'Downtown is the bar crawl; pick one or two stops.') +
    '<div class="grid three">' +
    card('Award-winning list', 'Soby’s wine program',
         'Make a glass at Soby’s part of the weekend, even if brunch is your meal there.') +
    card('Riverside', 'Grand Bohemian Lodge',
         'A drink by the fire or overlooking Falls Park, if you are staying there or passing through.') +
    card('Craft beer', 'Downtown breweries',
         'Greenville has a lively brewery scene in and around downtown. Ask locally which taprooms are closest to your hotel.') +
    '</div></section>')

P.append('<section id="events">' + head('06', 'Sports & what’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to current calendars. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Minor league baseball · Spring–summer', 'Greenville Drive',
         'Games at Fluor Field, a ballpark modeled on Fenway, walkable from downtown. Check the home schedule.',
         'https://www.milb.com/greenville', 'Schedule & tickets') +
    card('Performing arts', 'Peace Center',
         'Broadway tours, concerts and shows by the river, steps from Main Street. Check what is on for your dates.') +
    card('Fall festival', 'Fall for Greenville',
         'A large food and music festival on Main Street each fall. Fun and crowded; book lodging early.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.visitgreenvillesc.com/" target="_blank" rel="noopener">Browse Greenville events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend with no car needed: the falls, the trail and two standout dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KGMU, subject to the actual flight plan, and ride downtown.'),
        ('Afternoon', 'Lunch on Main Street, then Falls Park and Liberty Bridge. Check in when your room is ready.'),
        ('Evening', 'Dinner at Jianna.')]) +
    day('SAT', 'Trail & table', [
        ('Morning', 'Rent bikes and ride the Swamp Rabbit Trail, stopping at Unity Park.'),
        ('Afternoon', 'Back downtown to browse Main Street, or catch an afternoon Greenville Drive game in season.'),
        ('Evening', 'Dinner at Scoundrel, then a nightcap by the falls.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Brunch at Soby’s and a last walk by the river.'),
        ('Before leaving', 'Ride back to the FBO with ample time for aircraft preparation.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.').replace('07 /', '08 /') +
    know([('Book in this order', 'Scoundrel first if it is the reason for the trip, then lodging, the Friday dinner and bikes.'),
          ('Allow for the season', 'Summers are hot; fall is the busiest and most beautiful season.'),
          ('Busy airport', 'GMU sees plenty of jet traffic. Allow time for taxi and tower instructions.'),
          ('Dates come next', 'Hotel rates, tickets and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=7, place='Greenville, South Carolina', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html='Greenville - Liberty Bridge at Falls Park by P. Hughes, <a href="https://commons.wikimedia.org/wiki/File:Greenville_-_Liberty_Bridge_at_Falls_Park.jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>. Resized for display; adaptations shared under the same license.'))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
