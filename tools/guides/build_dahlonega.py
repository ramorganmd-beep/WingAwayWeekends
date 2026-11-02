"""Generate docs/dahlonega/index.html."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know, wine_and_flying  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['dahlonega']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('wine', 'Wine'), ('explore', 'Explore'),
       ('spa', 'Spa'), ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='dahlonega', name='Dahlonega', state='Georgia', number=15,
    description='A curated two-night Dahlonega wine weekend for GA pilots and their partners, from KMYR to KGVL Gainesville. North Georgia mountain wineries, a gold-rush town square and waterfalls.',
    lede='Gold-rush town. Mountain wineries.',
    intro='America’s first major gold rush began here in 1828. Today Dahlonega’s historic square is lined with tasting rooms, shops and restaurants, and the surrounding mountains hold some of Georgia’s best wineries. Add a waterfall hike and it is an easy, romantic weekend.',
    pills=['Mountain wineries', 'Historic square', 'Waterfalls'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KGVL', nm=247, flight_time='~1 hr 54 <small>min</small>',
    style='Rental car + wine driver', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land by the lake, drive into the hills.',
    'KGVL, Lee Gilmer Memorial in Gainesville, is about 30–35 minutes from Dahlonega by car, near Lake Lanier.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Champion Aviation Services', 'Lee Gilmer Memorial · Phillips 66', '770-532-4136') +
    '<p class="note">Recent pilot reports say there is no courtesy car, so arrange a rental car before you go and confirm pickup at the airport. A second operator on the field, Lanier Flight Center, also sells fuel. Ask about two-night parking and fees. No live fuel price is shown.</p>'
    '<p class="note">The North Georgia mountains rise to the north. Review terrain, the sectional and current NOTAMs, and expect afternoon storms in summer.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Walk the square; ride to the wineries.</h3><p>The square is walkable, with several tasting rooms on it. The vineyards are 10–20 minutes out on winding mountain roads, so book a wine-tour driver for the tasting day.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Stay on the square to walk to dinner, or at a vineyard resort in the hills. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('On the square · Boutique', 'Hall House Hotel',
         'A small boutique hotel right on Dahlonega’s historic square. Walk to tasting rooms, shops and dinner.') +
    card('Downtown · Hotel & villas', 'The Dahlonega Square Hotel',
         'Rooms and villas a short walk from the square, with a porch-and-garden feel.') +
    card('Vineyard resort · In the hills', 'Dahlonega Resort and Vineyard',
         'A resort with its own vineyard, restaurant and bar a few minutes outside town. Choose it to wake up to mountain views.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long lunch.',
    'The square has no chain restaurants. Reserve weekend dinners, and eat a little early; the square quiets down late.') +
    '<div class="grid three">' +
    card('Saturday dinner · Winery fine dining', 'Montaluce Winery & Restaurant',
         'A Tuscan-style winery estate in the hills with a polished restaurant and vineyard views. The special-occasion dinner.') +
    card('Friday dinner · On the square', 'Bourbon Street Grille',
         'New Orleans-style Cajun and Creole cooking, with a porch overlooking the square. Ask for a porch table.') +
    card('Lunch · Southern', 'Crimson Moon',
         'Southern cooking in one of the oldest commercial buildings on the square, with live music some evenings.') +
    '</div></section>')

P.append('<section id="wine">' + head('04', 'Wineries', 'Georgia wine country.',
    'More than a dozen wineries surround Dahlonega, with more tasting rooms right on the square.') +
    '<div class="grid three">' +
    card('Mountain views · Sunday brunch', 'Wolf Mountain Vineyards',
         'A hilltop winery with sweeping views, sparkling and still wines, and a popular weekend brunch. Book ahead.') +
    card('Tuscan estate · Dining', 'Montaluce Winery',
         'Tasting with dinner, or on its own, at the estate’s piazza-style terrace.') +
    card('Award-winning · Relaxed', 'Frogtown Cellars',
         'One of North Georgia’s most awarded wineries, with a big deck over the vines.') +
    card('Small estate · Views', 'Kaya Vineyards',
         'A winery and vineyard with a hilltop tasting room and wide mountain views.') +
    card('Family farm · Rustic', 'Cavender Creek Vineyards',
         'A small family winery in an old barn-style tasting room, relaxed and friendly.') +
    card('On the square · Walk-in', 'Downtown tasting rooms',
         'Several wineries pour on the square, including Accent Cellars. An easy tasting with no driving at all.') +
    '</div>' + wine_and_flying('Many wineries take reservations on weekends; check before you go.') + '</section>')

P.append('<section id="explore">' + head('05', 'Things to do', 'Gold, waterfalls and mountain air.',
    'Balance the tasting day with something outdoors.') +
    '<div class="explore-list">' +
    explore(1, 'The historic square',
            'Boutiques, galleries, candy shops and tasting rooms around the 1836 courthouse. Lovely in the evening.') +
    explore(2, 'Dahlonega Gold Museum',
            'Inside the old courthouse on the square, telling the story of the 1828 gold rush and the federal mint that once stood in town.') +
    explore(3, 'A gold-mine tour',
            'Go underground at a historic mine outside town, and try panning for gold. Fun and a little corny.') +
    explore(4, 'Amicalola Falls State Park',
            'One of the tallest waterfalls in the Southeast, about 30 minutes west, with a staircase trail and a lodge. A great Sunday-morning walk.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>A mountain-inn spa · Time for two</h3>'
    '<p>Mountain Laurel Creek Inn & Spa, a small bed and breakfast just outside town, offers spa treatments. A quiet afternoon for the pilot while others taste.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-inn guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('06', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the town calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('October', 'Gold Rush Days',
         'One of Georgia’s biggest festivals, with crafts and food on the square. Huge crowds; book far ahead or choose another weekend.') +
    card('Late September–October', 'Harvest and fall color',
         'Harvest at the wineries and color in the mountains. Beautiful and busy.') +
    card('November–December', 'Old-Fashioned Christmas',
         'The square lights up for the holidays, with weekend events through December.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the town calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.dahlonega.org/" target="_blank" rel="noopener">Browse Dahlonega events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend with the tasting day in the middle. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & the square', [
        ('Late-morning arrival', 'Land at KGVL, subject to weather and your actual flight plan, and pick up the rental car.'),
        ('Afternoon', 'Drive up to Dahlonega, check in and wander the square. The Gold Museum is a good first stop.'),
        ('Evening', 'Dinner on the porch at Bourbon Street Grille.')]) +
    day('SAT', 'Wine country day', [
        ('Late morning', 'A driver to Wolf Mountain for brunch and a tasting.'),
        ('Afternoon', 'Frogtown or Kaya, or a spa afternoon at Mountain Laurel Creek.'),
        ('Evening', 'Dinner at Montaluce. Keep the night early if you fly tomorrow.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast and a walk at Amicalola Falls.'),
        ('Before leaving', 'Return the car and allow time at the FBO; afternoon storms build in summer.'),
        ('Fly home', 'Only when the pilot is well clear of the 8-hour rule and feels fully fit to fly.')]) +
    '</div></section>')

P.append('<section id="know">' + head('08', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Rental car and lodging first, then a wine driver and dinners.'),
          ('No courtesy car', 'Recent reports say KGVL has none. Reserve a rental car ahead.'),
          ('Festival weekends', 'Gold Rush Days in October fills the town. Check dates before booking.'),
          ('Wine & flying', 'Taste on the non-flying day and keep the evening before departure dry.')]) +
    '</section>')

P.append(page_end(number=15, place='Dahlonega, Georgia', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
