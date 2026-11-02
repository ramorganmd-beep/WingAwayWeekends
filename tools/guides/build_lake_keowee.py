"""Generate docs/lake-keowee/index.html (Lake Keowee and Lake Jocassee, South Carolina)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['lake-keowee']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='lake-keowee', name='Lake Keowee & Jocassee', state='South Carolina', number=20,
    description='A curated two-night Lake Keowee and Lake Jocassee getaway for GA pilots and their partners, from KMYR to KCEU Clemson. Clear mountain lakes, waterfalls you reach by boat and Blue Ridge hiking.',
    lede='Clear water and waterfalls you reach by boat.',
    intro='In South Carolina’s Upstate, two linked lakes sit at the foot of the Blue Ridge. Lake Keowee is broad and sunny, with lakeside restaurants. Lake Jocassee, above it, is deep, clear and blue-green, ringed by protected forest, with waterfalls tumbling straight into the lake. Rent a boat, find a waterfall and slow right down.',
    pills=['Mountain lakes', 'Waterfalls by boat', 'Hiking'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KCEU', nm=205, flight_time='~1 hr 37 <small>min</small>',
    style='Rental car + boat', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Two good airports.',
    'KCEU, Oconee County Regional near Clemson, is about 20 minutes from Lake Keowee and 40 from Lake Jocassee. KLQK, Pickens County, is the alternative, about 25 minutes from Keowee’s east shore and 35–40 from Jocassee.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBOs</h3>' +
    fbo('Oconee County Regional Airport · KCEU', '365 Airport Road, Seneca, SC 29678', '864-882-2959') +
    fbo('Pickens County Airport · KLQK', '240 Airport Road, Liberty, SC 29657', '864-843-5803') +
    '<p class="note">The county FBO lists a crew car, and Hertz and Enterprise rent cars at the airport six days a week; reserve ahead. Ask about two-night parking and fees. On Clemson football weekends the area fills up.</p>'
    '<p class="note"><strong>Pickens County (KLQK):</strong> the county FBO lists Titan 100LL and Jet A, self-serve and full-serve, and a courtesy car, with staff on site about 8–5 daily; after-hours service costs extra. Ask about two-night parking and a rental car. No live fuel price is shown.</p>'
    '<p class="note">The Blue Ridge escarpment rises to the north. Review terrain, the sectional and current NOTAMs, and watch for afternoon mountain storms in summer.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>A car, then a boat.</h3><p>Rent a car for the weekend. For the lakes, rent a pontoon, or join a guided boat tour from Devils Fork State Park, the only public access to Lake Jocassee.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Stay on the water if you can.',
    'This is lake-house country rather than resort country. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Private · Lakefront', 'Lake Keowee vacation rentals',
         'The best stay here is a lake house with its own dock, many with hot tubs and screened porches. Book early for summer and fall weekends.') +
    card('State park · Jocassee', 'Devils Fork State Park villas',
         'Lakeside villas and cabins in the state park on Lake Jocassee, steps from the boat ramp. Simple, and very popular; reserve far ahead.') +
    card('Hotel · On Lake Keowee', 'Fairfield Inn & Suites Seneca Clemson',
         'A dependable hotel with a deck and pool overlooking Lake Keowee. Easy if you want a hotel close to the airport and restaurants.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Lakeside and relaxed.',
    'Dining is casual. Reserve on weekends, especially during Clemson football season.') +
    '<div class="grid three">' +
    card('Friday dinner · Lake views', 'The Lighthouse Restaurant',
         'Lake Keowee’s best-known restaurant, with a second-floor dining room and panoramic lake and mountain views. Go for sunset.') +
    card('Lunch · By the marina', 'Tiki Hut Lakeside Grill',
         'An island-style bar and grill beside Keowee Marina. Arrive by car or by boat.') +
    card('Saturday dinner · Steaks & seafood', 'Copper River Grill',
         'Steaks, seafood and classic American dishes in a relaxed setting. An easy second night.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Waterfalls, boats and big views.',
    'Lake Jocassee is the highlight. Plan one full day on the water.') +
    '<div class="explore-list">' +
    explore(1, 'A waterfall boat tour on Lake Jocassee',
            'Guided pontoon tours from Devils Fork State Park visit waterfalls that drop straight into the lake, with stops to swim in summer. Book ahead; tours fill on weekends.') +
    explore(2, 'Rent a pontoon or kayaks',
            'Rental companies deliver pontoons, canoes and kayaks to the Devils Fork dock. The water is famously clear and cold.') +
    explore(3, 'Whitewater Falls',
            'Among the highest waterfalls in the eastern United States, just over the North Carolina line, about 45 minutes away. A short paved walk to the overlook.') +
    explore(4, 'Table Rock State Park',
            'A granite mountain with a demanding trail to the top and wide views of the lakes and the Upstate. Allow most of a day for the summit.') +
    explore(5, 'Clemson',
            'The South Carolina Botanical Garden and the university campus make an easy morning near the airport.') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the county visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Late spring–summer', 'Lake season',
         'Warm days and swimming at the waterfalls. Weekends at Devils Fork are busy; arrive early.') +
    card('Fall', 'Clemson football',
         'Home game weekends fill every hotel and restaurant for miles. Great fun, or a reason to choose another weekend.') +
    card('October–early November', 'Fall color',
         'The forests around Jocassee turn gold. Cool, clear and beautiful from the water.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the county calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://visitoconeesc.com/" target="_blank" rel="noopener">Browse Oconee County events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: a sunset dinner, a day on Jocassee and a waterfall. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KCEU or KLQK, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Check in on Lake Keowee and get down to the dock.'),
        ('Evening', 'Sunset dinner at The Lighthouse.')]) +
    day('SAT', 'Lake Jocassee', [
        ('Morning', 'A waterfall boat tour, or your own pontoon from Devils Fork.'),
        ('Afternoon', 'A swim and a picnic by the falls, then a slow cruise back.'),
        ('Evening', 'Dinner at Copper River Grill.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'A short drive to Whitewater Falls.'),
        ('Before leaving', 'Return the car and allow time at the FBO.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and the rental car first, then a boat tour or rental.'),
          ('Football weekends', 'Clemson home games fill the area. Check the schedule before booking.'),
          ('Cold water', 'Jocassee stays cold and deep even in summer. Swim with care.'),
          ('Dates come next', 'Rates, tours and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=20, place='Lake Keowee & Jocassee, South Carolina', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
