"""Generate docs/highlands-cashiers/index.html (Highlands and Cashiers, North Carolina)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 3, 2026'  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['highlands-cashiers']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='highlands-cashiers', name='Highlands–Cashiers', state='North Carolina', number=24, reviewed=REVIEWED,
    description='A curated two-night Highlands and Cashiers getaway for GA pilots and their partners, from KMYR to K1A5 Franklin. Mountain inns, waterfalls, Whiteside Mountain and fine dining on the Blue Ridge plateau.',
    lede='Waterfalls, cool air and a great inn.',
    intro='High on a plateau in the Blue Ridge, the twin villages of Highlands and Cashiers are cooler than the valleys below and surrounded by waterfalls and granite cliffs. Stay at a polished mountain inn, walk behind a waterfall, hike to the cliffs of Whiteside Mountain, and end with dinner on a village main street.',
    pills=['Mountain inns', 'Waterfalls', 'Fine dining'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='K1A5', nm=241, flight_time='~1 hr 51 <small>min</small>',
    style='Courtesy or rental car', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land in the valley, drive up the mountain.',
    'K1A5, Macon County Airport in Franklin, is about 35–40 minutes from Highlands by a winding mountain road; Cashiers is about 20 minutes farther. Jackson County Airport (24A) near Sylva is an alternative for Cashiers.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Macon Air · Macon County Airport', '1241 Airport Road, Franklin, NC 28734', '828-524-5529') +
    '<p class="note">The FBO lists a courtesy car and rental cars; for two nights, reserve a rental car ahead. CTAF 123.05. Ask about parking, fees and hours. No live fuel price is shown.</p>'
    '<p class="note">This is mountain flying: high terrain surrounds the valley, and clouds and fog can linger on the ridges. Review terrain, density altitude, the sectional and current NOTAMs, and plan morning flights in summer.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>You’ll want a car.</h3><p>The road up to Highlands passes waterfalls and steep curves; allow extra time and drive it in daylight. Both villages are walkable once you arrive.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'A celebrated inn, a small romantic one, or a boutique hotel in Cashiers. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Highlands · Relais & Châteaux', 'Old Edwards Inn & Spa',
         'The area’s landmark inn in the middle of Highlands, with a renowned spa, Madison’s restaurant and beautifully kept rooms. The romantic splurge.',
         'https://www.oldedwardshospitality.com/') +
    card('Highlands · Small & romantic', 'The White Birch Inn',
         'A cozy, highly rated small inn favored by couples, close to the village.',
         'https://www.whitebirchinn.com/') +
    card('Cashiers · Boutique', 'Hotel Cashiers',
         'A boutique inn in the center of Cashiers with dining and a spa, and an easy drive to Highlands.',
         'https://www.hotelcashiers.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long lunch.',
    'Mountain-town dining is excellent here. Reserve weekend dinners well ahead, especially in summer and fall.') +
    '<div class="grid three">' +
    card('Friday dinner · Old Edwards', 'Madison’s',
         'Seasonal fine dining at Old Edwards Inn on Highlands’ main street. Polished and romantic.',
         'https://www.oldedwardshospitality.com/') +
    card('Saturday dinner · Cashiers', 'The Orchard',
         'A much-praised restaurant in a restored farmhouse near Cashiers. Diners call it one of the best meals in the mountains; reserve ahead.',
         'https://theorchardcashiers.com/') +
    card('Lunch · Highlands', 'Wolfgang’s Restaurant & Wine Bistro',
         'A long-running Highlands favorite with a wine list and a garden patio. Good for a long lunch between waterfalls.',
         'https://www.wolfgangs.net/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Waterfalls and granite cliffs.',
    'Most of the best sights are short walks from the road.') +
    '<div class="explore-list">' +
    explore(1, 'Dry Falls & Bridal Veil Falls',
            'On the road between Franklin and Highlands: walk behind the curtain of Dry Falls, then pass Bridal Veil Falls, which spills right beside the highway.') +
    explore(2, 'Whiteside Mountain',
            'A two-mile loop to sheer granite cliffs with long views over the Blue Ridge. Moderate, and one of the area’s classic hikes.') +
    explore(3, 'Sunset Rock',
            'A short walk from downtown Highlands to a rock ledge with a view over the town and mountains. Go for sunset.') +
    explore(4, 'Whitewater Falls',
            'Among the highest waterfalls in the eastern United States, about 30 minutes south of Cashiers, with a short paved walk to the overlook.') +
    explore(5, 'Main Street Highlands & Cashiers',
            'Galleries, boutiques and wine shops in two small villages. An easy afternoon.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The spa at Old Edwards · Time for two</h3>'
    '<p>Old Edwards Inn’s spa is one of the best known in the Southeast, with couples treatments, a heated mineral pool and quiet lounges.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-inn guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the area visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Summer', 'Cool mountain season',
         'Highlands sits near 4,000 feet, so summer days are pleasantly cool. The busiest season; book well ahead.') +
    card('October', 'Fall color',
         'The plateau turns gold and red, usually in mid-October. Spectacular, and very busy.') +
    card('November', 'Culinary Weekend',
         'Highlands’ well-known food-and-wine weekend in the fall. Check dates and tickets.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the area visitor site when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.highlandschamber.org/" target="_blank" rel="noopener">Browse Highlands events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: waterfalls on the way up, a cliff-top hike and two mountain dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & the waterfall road', [
        ('Late-morning arrival', 'Land at K1A5, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Drive up past Bridal Veil Falls and walk behind Dry Falls, then check in.'),
        ('Evening', 'Dinner at Madison’s.')]) +
    day('SAT', 'Cliffs & villages', [
        ('Morning', 'Hike the Whiteside Mountain loop.'),
        ('Afternoon', 'A long lunch, then the spa at Old Edwards or a wander through Cashiers.'),
        ('Evening', 'Dinner at The Orchard.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Sunset Rock in the morning light, or a last coffee on Main Street.'),
        ('Before leaving', 'Allow extra time for the mountain road and the FBO.'),
        ('Fly home', 'Mountain clouds can linger in the morning; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and a car first, then dinners and the spa.'),
          ('Mountain flying', 'High terrain, valley fog and quick-building storms. Fly in the morning and keep a backup day.'),
          ('Mountain roads', 'The road from Franklin is steep and winding. Drive it in daylight.'),
          ('Peak seasons', 'Summer weekends and October fill early. Book well ahead.')]) +
    '</section>')

P.append(page_end(number=24, place='Highlands–Cashiers, North Carolina', reviewed=REVIEWED, note='Confirm hours, prices and availability directly with each place before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
