"""Generate docs/hunt-country/index.html (Middleburg and Loudoun wine country, Virginia)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know, wine_and_flying  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 2, 2026'  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['hunt-country']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('wine', 'Wine'), ('explore', 'Explore'),
       ('spa', 'Spa'), ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='hunt-country', name='Virginia Hunt Country', state='Virginia', number=14, reviewed=REVIEWED,
    description='A curated two-night Virginia Hunt Country wine weekend for GA pilots and their partners, from KMYR to KJYO Leesburg. Middleburg, Loudoun wineries, horse country inns and the Udvar-Hazy Center.',
    lede='Stone walls, horse farms and serious wine.',
    intro='West of Washington, the rolling Piedmont around Middleburg is fox-hunting and steeplechase country, with more than 50 wineries in Loudoun County alone. Stay at a historic inn or a horse-country resort, taste some of Virginia’s best wines, and save an hour for the Space Shuttle at the Udvar-Hazy Center.',
    pills=['Loudoun wineries', 'Horse-country inns', 'Udvar-Hazy Center'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KJYO', nm=331, flight_time='~2 hr 27 <small>min</small>',
    style='Courtesy or rental car + driver', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Two good doors to horse country.',
    'KJYO, Leesburg Executive, is about 25 minutes from Middleburg. It sits inside the Washington, DC SFRA, so many pilots will prefer KHWY, Warrenton-Fauquier, just outside it.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBOs</h3>' +
    fbo('Kuhn Jet Center · KJYO', '1001 Sycolin Road, Leesburg, VA 20175', '703-665-3000') +
    fbo('Warrenton-Fauquier Airport FBO · KHWY', '1533 Iris Trail, Midland, VA 22728', '540-422-8285') +
    '<p class="note"><strong>Washington, DC SFRA:</strong> KJYO lies inside the Special Flight Rules Area. You need the FAA’s SFRA training, a filed SFRA flight plan, a discrete transponder code and two-way radio contact, and you must follow the published Leesburg procedures. If that is not for you, fly to KHWY (about 300 NM, ~2 hr 15 min at 150 kt), outside the SFRA and about 25 minutes from Middleburg.</p>'
    '<p class="note">Kuhn Jet Center lists free courtesy cars for local use and fueling from early morning into the evening. Warrenton-Fauquier lists a courtesy car and daytime hours (about 8–5), with a fee for after-hours service. Ask both about two-night parking and fees. No live fuel price is shown.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Book a driver for tasting day.</h3><p>Wineries are spread across back roads, 15–30 minutes apart. Rent a car for the weekend (courtesy cars are for short local trips), and hire a private wine-tour driver for the tasting day.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'A resort with a spa, a historic tavern inn in town, or a country estate. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Resort · Spa & equestrian', 'Salamander Middleburg',
         'A polished resort on 340 acres at the edge of Middleburg, with a full spa, an equestrian center, a cooking studio and several restaurants. The indulgent choice.',
         'https://www.salamanderresort.com/') +
    card('Historic inn · In town', 'The Red Fox Inn & Tavern',
         'One of America’s oldest inns, dating to the 1700s, on Middleburg’s main street. Walk to the shops and to dinner downstairs.',
         'https://redfox.com/') +
    card('Country estate · Romantic', 'Goodstone Inn & Restaurant',
         'An estate inn on a large property of rolling fields and woods just outside Middleburg, with cottages, walking trails and its own restaurants.',
         'https://www.goodstone.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long lunch.',
    'Hunt country dining is small and special. Reserve weekend dinners well ahead.') +
    '<div class="grid three">' +
    card('Friday dinner · Historic tavern', 'The Red Fox Inn & Tavern',
         'Candlelit rooms with low beams and a fireplace, and a seasonal menu that diners rate highly. Book ahead.',
         'https://redfox.com/tavern/') +
    card('Saturday dinner · Fine dining', 'The Conservatory at Goodstone',
         'Contemporary American cooking with seasonal ingredients in a glass conservatory overlooking the estate. Check current dinner days.',
         'https://www.goodstone.com/dining') +
    card('Splurge · About 45 minutes', 'The Inn at Little Washington',
         'One of America’s most celebrated restaurants, with three Michelin stars, in the village of Washington, Virginia. A once-in-a-lifetime dinner; book months ahead and plan a driver.',
         'https://www.theinnatlittlewashington.com/dine') +
    '</div></section>')

P.append('<section id="wine">' + head('04', 'Wineries', 'Virginia’s best, close together.',
    'The Middleburg AVA and the Loudoun wine clusters hold dozens of wineries. Choose three for a relaxed day.') +
    '<div class="grid three">' +
    card('Middleburg · Bordeaux style', 'Boxwood Estate Winery',
         'Elegant Bordeaux-style blends in a modern tasting room set among horse farms. A polished, grown-up first stop.',
         'https://boxwoodestate.com/') +
    card('Middleburg · Award-winning', 'Cana Vineyards & Winery',
         'One of the most decorated wineries in the Middleburg AVA, with a hilltop tasting room and wide views.',
         'https://canavineyards.com/') +
    card('Middleburg · Boutique', 'Greenhill Winery & Vineyards',
         'A boutique estate making 100% Virginia wines, with a refined tasting room and a pond-side lawn.',
         'https://experiencegreenhill.com/') +
    card('Aldie · Views', '50 West Vineyards',
         'Sweeping Blue Ridge views and a lively terrace on the Route 50 corridor. Good for an afternoon glass.',
         'https://www.50westvineyards.com/') +
    card('Middleburg · Virginia’s own grape', 'Chrysalis Vineyards',
         'Home to one of the largest plantings of Norton, the native American grape, plus Albariño and other Spanish varieties.',
         'https://www.chrysaliswine.com/') +
    card('Rectortown · Small farm winery', 'Slater Run Vineyards',
         'A small family farm winery with a relaxed tasting room and pastoral views, a few miles from Middleburg.',
         'https://www.slaterrun.com/') +
    '</div>' + wine_and_flying('Many Loudoun wineries limit group sizes, require reservations on weekends or are adults-only; check before you go.') + '</section>')

P.append('<section id="explore">' + head('05', 'Things to do', 'Horse country, history and one great hangar.',
    'Mix a slow village morning with a big aviation afternoon.') +
    '<div class="explore-list">' +
    explore(1, 'Steven F. Udvar-Hazy Center',
            'The Smithsonian’s huge companion museum beside Dulles: the Space Shuttle Discovery, an SR-71 Blackbird, the Enola Gay and hundreds more aircraft. About 30 minutes from KJYO. Admission is free; parking is paid.',
            'https://airandspace.si.edu/visit/udvar-hazy-center', 'Museum information') +
    explore(2, 'Middleburg’s main street',
            'Stone buildings, boutiques, tack shops, galleries and cafés in one of Virginia’s prettiest small towns.') +
    explore(3, 'National Sporting Library & Museum',
            'Art and books on horses, hunting and the sporting life, in Middleburg. Small, beautiful and very hunt country.',
            'https://nationalsporting.org/', 'Visit the museum') +
    explore(4, 'Historic Leesburg',
            'Brick sidewalks, restaurants and shops in a colonial-era town center, near KJYO. Morven Park’s mansion and gardens are on the edge of town.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The spa at Salamander · Time for two</h3>'
    '<p>Salamander Middleburg’s full-service spa has couples treatments, pools and relaxation rooms. A good way to spend the afternoon while the pilot stays off the wine.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-resort guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p>'
    '<a href="https://www.salamanderresort.com/spa/overview" target="_blank" rel="noopener">Spa details</a></div></section>')

P.append('<section id="events">' + head('06', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the regional calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('May & October', 'Virginia Gold Cup races',
         'Steeplechase racing at Great Meadow in The Plains: the Virginia Gold Cup in spring and the International Gold Cup in fall. Tailgates, hats and big crowds; book far ahead.') +
    card('September–October', 'Harvest and fall color',
         'Harvest at the wineries and color in the hills. The most beautiful and busiest season.') +
    card('December', 'Middleburg Christmas parade',
         'Horses and hounds lead the town’s holiday parade. Charming, and the inns fill early.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the regional calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.visitloudoun.org/" target="_blank" rel="noopener">Browse Loudoun events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: aviation on arrival day, wine in the middle and an easy Sunday. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & a big hangar', [
        ('Late-morning arrival', 'Land at KJYO or KHWY, subject to weather, the SFRA and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'The Udvar-Hazy Center, then on to Middleburg to check in.'),
        ('Evening', 'Dinner at The Red Fox Inn & Tavern.')]) +
    day('SAT', 'Wine country day', [
        ('Late morning', 'A private driver to Boxwood and Greenhill, with lunch between tastings.'),
        ('Afternoon', 'A glass at Cana or 50 West, or a spa afternoon at Salamander.'),
        ('Evening', 'Dinner at The Conservatory at Goodstone. Keep the night early if you fly tomorrow.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast and a walk along Middleburg’s main street, or the National Sporting Library.'),
        ('Before leaving', 'Return the car, file the SFRA plan if departing KJYO, and allow time at the FBO.'),
        ('Fly home', 'Only when the pilot is well clear of the 8-hour rule and feels fully fit to fly.')]) +
    '</div></section>')

P.append('<section id="know">' + head('08', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and a wine-tour driver first, then dinners and any spa time.'),
          ('The SFRA', 'KJYO requires SFRA procedures. KHWY, outside it, is the simpler choice for many pilots.'),
          ('Race weekends', 'The Gold Cup weekends in May and October fill every inn for miles. Check dates before booking.'),
          ('Wine & flying', 'Taste on the non-flying day and keep the evening before departure dry.')]) +
    '</section>')

P.append(page_end(number=14, place='Virginia Hunt Country', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
