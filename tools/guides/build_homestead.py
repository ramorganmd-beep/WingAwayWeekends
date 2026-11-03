"""Generate docs/homestead/index.html (The Omni Homestead and Bath County, Virginia)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = None  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['homestead']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='homestead', name='The Homestead', state='Virginia', number=28, reviewed=REVIEWED,
    description='A curated two-night getaway to The Omni Homestead and Bath County, Virginia, for GA pilots and their partners, from KMYR to KHSP. Hot springs, a historic grand resort, mountain golf and chamber music.',
    lede='A grand resort and the warm springs.',
    intro='Deep in the Allegheny Mountains, Hot Springs has welcomed travelers to its mineral waters since the 1700s. Land on a mountaintop runway, stay at the grand Homestead, soak in the historic Warm Springs Pools, play one of the great mountain golf courses, and dress for dinner.',
    pills=['Grand resort', 'Hot springs', 'Mountain golf'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KHSP', nm=260, flight_time='~2 hr',
    style='Resort transfer', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land on a mountaintop.',
    'KHSP, Ingalls Field, sits on a ridge near 3,800 feet, one of the highest airports in the East, about 15–20 minutes from The Homestead.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Ingalls Field · Bath County Airport Authority', '6240 Airport Road, Hot Springs, VA 24445', '540-839-5326') +
    '<p class="note">Listed hours are about 9 a.m. to 5 p.m., with a callout fee after hours. Ask the resort about a transfer when you book, and ask the FBO about overnight parking, tie-downs and fees. No live fuel price is shown.</p>'
    '<p class="note">This is serious mountain flying: a ridge-top runway with drop-offs, high density altitude in summer, gusty winds and clouds that can sit on the field. Review the airport diagram, performance, terrain and current NOTAMs, and have an alternate in the valley.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>The resort does the driving.</h3><p>Once you’re at The Homestead, most of the weekend is on foot. A car helps for the Warm Springs Pools, Garth Newel and Falling Spring Falls, all within about 15 minutes.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Grand resort or a quiet inn.',
    'Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Hot Springs · Historic grand resort', 'The Omni Homestead Resort & Spa',
         'A grand resort dating to 1766, with a famous spa, mountain golf, a long list of outdoor activities and afternoon tea in the Great Hall. The reason to come.',
         'https://www.omnihotels.com/hotels/homestead-virginia') +
    card('Warm Springs · Small inn', 'The Inn at Gristmill Square',
         'A small inn in restored 19th-century buildings around an old mill in Warm Springs, with its own restaurant, a few minutes from the pools. Quiet and personal.',
         'https://gristmillsquare.com/') +
    card('Hot Springs · Bed & breakfast', 'Vine Cottage Inn',
         'A small, relaxed inn in the village, within walking distance of The Homestead.',
         'https://www.vinecottageinn.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One very grand.',
    'Most dining is at the resort. Reserve, and check dress codes.') +
    '<div class="grid three">' +
    card('Friday dinner · Casual', 'Jefferson’s Restaurant & Taproom',
         'The Homestead’s relaxed restaurant, with Virginia wines, craft beer and regional dishes.',
         'https://www.omnihotels.com/hotels/homestead-virginia/dining/jeffersons-restaurant-and-taproom') +
    card('Saturday dinner · Fine dining', 'American Audubon Dining Room',
         'The Homestead’s grand dining room, with refined multi-course dinners. Dress for the occasion.',
         'https://www.omnihotels.com/hotels/homestead-virginia/dining') +
    card('Lunch · At the golf course', 'Sam Snead’s Tavern',
         'A casual tavern named for the golf legend, who grew up nearby. Walk-in only.',
         'https://www.omnihotels.com/hotels/homestead-virginia/dining/sam-sneads-tavern') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Warm water and cool mountains.',
    'Slow down. This is a place for long soaks and long walks.') +
    '<div class="explore-list">' +
    explore(1, 'The Warm Springs Pools',
            'Two historic bathhouses over natural warm springs, restored and reopened in 2022. Book a 50-minute soak ahead; you don’t need to stay at the resort.',
            'https://www.omnihotels.com/hotels/homestead-virginia/things-to-do/resort-activities/pools', 'Pools and reservations') +
    explore(2, 'Golf on the Cascades course',
            'A classic mountain course, long ranked among the best in Virginia, plus The Old Course at the resort, home to one of the oldest first tees in continuous use in the country.') +
    explore(3, 'Resort activities',
            'Falconry, fly-fishing, sporting clays, horseback riding, hiking and a zip line. Book a few the week before.') +
    explore(4, 'Garth Newel Music Center',
            'Chamber music on a farm between Hot Springs and Warm Springs, sometimes with dinner after the concert. Check the season’s schedule.',
            'https://www.garthnewel.org/', 'Concert schedule') +
    explore(5, 'Falling Spring Falls',
            'A tall roadside waterfall a short drive south of Hot Springs, with an overlook just off the highway.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The Spa at The Homestead · Time for two</h3>'
    '<p>The resort’s spa uses the area’s mineral springs, with pools, couples treatments and quiet lounges.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the county visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Summer', 'Chamber music',
         'Garth Newel’s summer festival, and cool mountain air for golf.') +
    card('October', 'Fall color',
         'The Alleghenies turn in mid-October. Beautiful, and busy at the resort.') +
    card('December', 'Holidays at The Homestead',
         'Lights, decorated halls and holiday events at the resort.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the county visitor site when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://visitbathva.com/" target="_blank" rel="noopener">Browse Bath County events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the springs, golf or the spa, and two resort dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & settle in', [
        ('Late-morning arrival', 'Land at KHSP, subject to weather and your actual flight plan, and transfer to the resort.'),
        ('Afternoon', 'Afternoon tea in the Great Hall, and a walk around the grounds.'),
        ('Evening', 'Dinner at Jefferson’s.')]) +
    day('SAT', 'Springs & mountains', [
        ('Morning', 'A round on the Cascades course, or falconry and a hike.'),
        ('Afternoon', 'A soak at the Warm Springs Pools, then the spa.'),
        ('Evening', 'Dinner in the American Audubon Dining Room.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'A slow breakfast, or the drive to Falling Spring Falls.'),
        ('Before leaving', 'Transfer to the airport during FBO hours.'),
        ('Fly home', 'Clouds can sit on the ridge; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'The resort and transfer first, then dinners, tee times, the pools and the spa.'),
          ('Mountain airport', 'A ridge-top field near 3,800 feet. Check performance, winds and ceilings, and plan an alternate.'),
          ('FBO hours', 'Arrive and depart during staffed hours, or arrange a callout ahead.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=28, place='The Homestead, Hot Springs, Virginia', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
