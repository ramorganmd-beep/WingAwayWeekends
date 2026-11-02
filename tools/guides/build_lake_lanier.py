"""Generate docs/lake-lanier/index.html (Lake Lanier and Gainesville, Georgia)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['lake-lanier']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='lake-lanier', name='Lake Lanier', state='Georgia', number=21,
    description='A curated two-night Lake Lanier getaway for GA pilots and their partners, from KMYR to KGVL Gainesville. A lake resort, a day on the water, downtown Gainesville dinners and an easy wine-country side trip.',
    lede='A day on the water, a dinner downtown.',
    intro='Lake Lanier spreads across the North Georgia foothills with hundreds of miles of shoreline. Land in Gainesville beside the lake, spend a day on a pontoon, have dinner on Gainesville’s historic square, and, if you like, add a wine afternoon in Dahlonega, half an hour away.',
    pills=['Lake resort', 'Boating', 'Wine nearby'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KGVL', nm=247, flight_time='~1 hr 54 <small>min</small>',
    style='Rental car + boat', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land beside the lake.',
    'KGVL, Lee Gilmer Memorial in Gainesville, sits near the lake’s north end, minutes from downtown Gainesville and about 30 minutes from Lanier Islands.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Champion Aviation Services', '1137 Aviation Way, Gainesville, GA 30501', '770-532-4136') +
    '<p class="note">Recent pilot reports say there is no courtesy car, so reserve a rental car and confirm pickup at the airport. A second operator on the field, Lanier Flight Center, also sells fuel. Ask about two-night parking and fees. No live fuel price is shown.</p>'
    '<p class="note">Atlanta’s Class B airspace lies to the southwest. Review the sectional and current NOTAMs, and expect afternoon storms in summer.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Car on land, pontoon on the lake.</h3><p>Rent a car for the weekend. For the lake, rent a pontoon by the hour or day; several companies deliver to docks or rent from Lanier Islands.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'A lake resort, or a lake house of your own. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Lake resort · Lanier Islands', 'Lanier Islands Legacy Lodge',
         'A lodge on the islands at the south end of the lake, with lake views, a pool, golf, a spa and Sidney’s restaurant. The easy, all-in-one choice.') +
    card('Private · Lakefront', 'Lake Lanier vacation rentals',
         'A lake house with a private dock, closer to Gainesville. Book early for summer weekends, and ask about the dock and boat rules.') +
    card('In the hills · Wine country', 'Dahlonega, 30 minutes north',
         'Combine the lake with wine country: stay on Dahlonega’s square and drive down for a day on the water. See our Dahlonega guide.',
         '../dahlonega/', 'Dahlonega guide') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Downtown dinners, lake-view lunch.',
    'Downtown Gainesville has the best restaurants; the resort has the views. Reserve weekend dinners.') +
    '<div class="grid three">' +
    card('Friday dinner · Downtown', 'Luna’s Restaurant',
         'A special-occasion favorite on Gainesville’s square, with a piano lounge for a drink and live music before dinner.') +
    card('Saturday dinner · Steakhouse', 'CHR Steak',
         'An upscale, modern steakhouse downtown, led by its chef-owner. The dressed-up night.') +
    card('Lunch · Lake views', 'Sidney’s at Legacy Lodge',
         'Seasonal cooking with a view over the lake at Lanier Islands. For Italian downtown instead, try Cotto Modern Italian.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Mostly, the water.',
    'Spend one day on the lake and one exploring.') +
    '<div class="explore-list">' +
    explore(1, 'A day on a pontoon',
            'Rent a pontoon and find a quiet cove for a swim and a picnic. Hundreds of miles of wooded shoreline make it easy to escape the crowds.') +
    explore(2, 'Lanier Islands',
            'The resort islands at the lake’s south end have a beach, golf, a spa and boat rentals. Easy for an afternoon even if you stay elsewhere.') +
    explore(3, 'Lake Lanier Olympic Park',
            'The rowing and canoe venue from the 1996 Atlanta Olympic Games, on the lake in Gainesville. A pretty spot to walk and watch the rowers.') +
    explore(4, 'Downtown Gainesville',
            'A historic square with restaurants, shops and the Atlanta Botanical Garden’s Gainesville garden nearby.') +
    explore(5, 'Dahlonega wineries',
            'Half an hour north: a gold-rush square and mountain wineries. Taste on the non-flying day.',
            '../dahlonega/', 'Dahlonega guide') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the lake visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('May–September', 'Lake season',
         'Warm water and long days on the lake. Summer weekends are very busy; go early or choose a weekday.') +
    card('November–January', 'Magical Nights of Lights',
         'Lanier Islands’ drive-through holiday light show, a long-running North Georgia tradition. Check dates and tickets.') +
    card('Spring & fall', 'Best seasons',
         'Mild weather and a quieter lake. Fall color peaks in late October.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the lake visitor site when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://discoverlakelanier.com/" target="_blank" rel="noopener">Discover Lake Lanier</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: a dinner downtown, a day on the lake and an easy Sunday. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & downtown', [
        ('Late-morning arrival', 'Land at KGVL, subject to weather and your actual flight plan, and pick up the rental car.'),
        ('Afternoon', 'Check in and walk Gainesville’s square.'),
        ('Evening', 'A drink in the piano lounge, then dinner at Luna’s.')]) +
    day('SAT', 'On the water', [
        ('Morning', 'Pick up a pontoon and find a quiet cove.'),
        ('Afternoon', 'Lunch by the lake at Lanier Islands, then more time on the water.'),
        ('Evening', 'Dinner at CHR Steak.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Lake Lanier Olympic Park, or a short drive to Dahlonega for a look around the square.'),
        ('Before leaving', 'Return the car and allow time at the FBO; afternoon storms build in summer.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Rental car and lodging first, then a boat and dinners.'),
          ('No courtesy car', 'Recent reports say KGVL has none. Reserve a rental car ahead.'),
          ('Busy summer weekends', 'The lake is crowded on summer weekends and holidays. Start early.'),
          ('Boating safety', 'Wear life jackets and keep a sober skipper; the lake is busy and storms build quickly.')]) +
    '</section>')

P.append(page_end(number=21, place='Lake Lanier, Georgia', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
