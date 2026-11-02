"""Generate docs/yadkin-valley/index.html."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know, wine_and_flying  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['yadkin-valley']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('wine', 'Wine'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='yadkin-valley', name='Yadkin Valley', state='North Carolina', number=13,
    description='A curated two-night Yadkin Valley wine weekend for GA pilots and their partners, from KMYR to KZEF Elkin. Estate wineries, vineyard dinners and the Blue Ridge foothills.',
    lede='North Carolina wine country, one runway away.',
    intro='Elkin sits in the middle of the Yadkin Valley, the state’s first wine region, with dozens of wineries scattered across the foothills below the Blue Ridge. Land a few minutes from town, taste at estate vineyards with mountain views, and end the day with dinner among the vines.',
    pills=['Estate wineries', 'Vineyard dining', 'Foothills views'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KZEF', nm=181, flight_time='~1 hr 27 <small>min</small>',
    style='Car + wine shuttle', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land just outside town.',
    'KZEF, Elkin Municipal, is a non-towered field beside the Yadkin River, a few minutes from downtown Elkin.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Yadkin Valley Aviation', '1598 C.C. Camp Road, Elkin, NC 28621', '336-366-3433') +
    '<p class="note">Yadkin Valley Aviation lists self-serve 100LL and Jet A and a courtesy car, with staff on site during the day (about 8–5). Pilots report a small tie-down fee and an after-hours call-out fee. A rental car can be arranged with notice; call ahead. CTAF 123.05. No live fuel price is shown.</p>'
    '<p class="note">Pilot Mountain and the Blue Ridge rise to the north and west. Review terrain, the sectional and current NOTAMs, and watch for afternoon mountain weather in summer.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Let someone else drive the wine roads.</h3><p>Wineries are spread out, 10–30 minutes apart. Use a car for town and dinner, and book the Elkin Vine Line wine shuttle (Friday–Sunday from the downtown visitor center) or a private driver for the tasting day.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Sleep among the vines.',
    'Small inns and winery cabins rather than big resorts. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Winery cabins · Creekside', 'Elkin Creek Vineyard cabins',
         'A handful of cabins beside Elkin Creek at a small family winery minutes from town. The most romantic choice: wake up at the vineyard.',
         'https://www.elkincreekvineyard.com/cabins') +
    card('Historic inn · Dobson', 'The Rockford Inn',
         'An 1848 farmhouse with heart-pine floors near the Dobson wineries. Recent listings describe it as a guest house rather than a full bed and breakfast; confirm what is included.',
         'https://rockfordinn.com/') +
    card('Practical · Dobson', 'Hampton Inn & Suites Dobson',
         'A dependable hotel in Dobson, central to the wineries, with its own wine bar. Easy if you simply want a comfortable hotel.',
         'https://www.hilton.com/en/hotels/hvnobhx-hampton-shelton/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Dinner at the vineyard.',
    'Some of the best tables are at the wineries. Reserve weekend dinners well ahead.') +
    '<div class="grid three">' +
    card('Saturday dinner · Fine dining', 'JOLO Winery & Vineyards',
         'An intimate dining room with vineyard views and Pilot Mountain beyond. Dinner Thursday–Sunday; reservations required.',
         'https://www.jolovineyards.com/dine/dining-spaces/') +
    card('Friday dinner · Wine bar & kitchen', 'Wisdom Table',
         'An intimate downtown Elkin restaurant with a wine tasting menu that changes weekly, a good introduction to the valley’s wines. Dinner Wednesday–Saturday; reserve ahead.') +
    card('Lunch · Casual', 'Elkin Creek Vineyard',
         'Wood-fired pizza and a glass by the creek. For a beer instead, Angry Troll Brewing in downtown Elkin has good food too.',
         'https://www.elkincreekvineyard.com/') +
    '</div></section>')

P.append('<section id="wine">' + head('04', 'Wineries', 'Pick three, not six.',
    'More than 20 wineries lie within a short drive of Elkin. Three tastings, with lunch between them, is a full and pleasant day.') +
    '<div class="grid three">' +
    card('Ronda · Italian varietals', 'Raffaldini Vineyards',
         'A Tuscan-style villa on a hilltop with Blue Ridge views and Italian-style wines, including appassimento reds. The prettiest terrace in the valley.',
         'https://www.raffaldini.com/') +
    card('Pilot Mountain · Small estate', 'JOLO Winery & Vineyards',
         'Small-lot wines and a polished tasting room in the shadow of Pilot Mountain. Pair a tasting with dinner.',
         'https://www.jolovineyards.com/') +
    card('Elkin area · Big reds', 'Jones von Drehle Vineyards',
         'A hillside estate known for structured reds such as Cabernet Sauvignon, with sweeping views from the deck.',
         'https://www.jonesvondrehle.com/') +
    card('Elkin · Creekside', 'Elkin Creek Vineyard',
         'A small family winery with a creekside setting, pizza and cabins. Easy and unhurried.',
         'https://www.elkincreekvineyard.com/') +
    card('Elkin · Organic', 'Carolina Heritage Vineyard & Winery',
         'One of the region’s certified-organic vineyards, close to town and a little different from the rest.',
         'https://www.yadkinvalleync.com/attractions/carolina-heritage-vineyards/') +
    '</div>' + wine_and_flying('The Elkin Vine Line shuttle runs Friday–Sunday; check its current schedule and book seats.') +
    '<p class="note" style="margin-top:14px">Tasting hours and reservation rules change by season; many wineries require reservations for groups or on weekends. Confirm before you go.</p></section>')

P.append('<section id="explore">' + head('05', 'Things to do', 'Between the tastings.',
    'Small-town evenings and big foothills views.') +
    '<div class="explore-list">' +
    explore(1, 'Downtown Elkin',
            'A walkable main street with shops, cafés and the restored Reeves Theater, which hosts live music most weekends.') +
    explore(2, 'Pilot Mountain State Park',
            'The famous quartzite knob is a landmark from the air; from the ground, short trails lead to wide overlooks. About 30 minutes east.') +
    explore(3, 'Stone Mountain State Park',
            'A granite dome, waterfalls and hiking trails about 30 minutes northwest. A good Sunday-morning walk before the flight home.') +
    explore(4, 'Elkin & Alleghany Rail Trail',
            'An easy walk or bike ride from town along an old rail bed, part of North Carolina’s Mountains-to-Sea Trail route.') +
    explore(5, 'Mount Airy',
            'Andy Griffith’s hometown, the model for Mayberry, about 30 minutes north. Nostalgic and fun for an hour or two.') +
    '</div></section>')

P.append('<section id="events">' + head('06', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the regional calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('May', 'Yadkin Valley Wine Festival',
         'A one-day festival in Elkin Municipal Park with wineries from across the valley. Fun and busy; book lodging early.',
         'https://yadkinvalleywinefestival.com/') +
    card('August–October', 'Harvest season',
         'Grapes come in and the wineries are at their liveliest. Fall color follows in October.') +
    card('Year-round', 'Live music',
         'The Reeves Theater in Elkin and many wineries host weekend music. Check schedules for your dates.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the regional calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.yadkinvalleync.com/" target="_blank" rel="noopener">Browse Yadkin Valley events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend with the tasting day in the middle. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KZEF, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Lunch at Elkin Creek Vineyard and check in. The non-pilot can enjoy a glass.'),
        ('Evening', 'Dinner at Wisdom Table in downtown Elkin.')]) +
    day('SAT', 'Wine country day', [
        ('Late morning', 'Ride the Vine Line or a private driver to Raffaldini for a tasting on the terrace.'),
        ('Afternoon', 'Jones von Drehle, then one more stop. Water and lunch between tastings.'),
        ('Evening', 'Dinner at JOLO. Keep the night early if you fly tomorrow.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast in Elkin and a walk at Stone Mountain or Pilot Mountain.'),
        ('Before leaving', 'Return the car and allow time at the FBO, which keeps daytime hours.'),
        ('Fly home', 'Only when the pilot is well clear of the 8-hour rule and feels fully fit to fly.')]) +
    '</div></section>')

P.append('<section id="know">' + head('08', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and the wine shuttle or driver first, then dinners. Winery dinners fill early.'),
          ('Wine & flying', 'Taste on the non-flying day and keep the evening before departure dry.'),
          ('FBO hours', 'Staff are on site during the day; after-hours service costs extra. Plan arrivals and departures accordingly.'),
          ('Dates come next', 'Tasting hours and restaurant days change by season. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=13, place='Yadkin Valley, North Carolina', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
