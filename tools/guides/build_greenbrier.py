"""Generate docs/greenbrier/index.html (The Greenbrier and Lewisburg, West Virginia)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = None  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['greenbrier']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='greenbrier', name='The Greenbrier', state='West Virginia', number=29, reviewed=REVIEWED,
    description='A curated two-night getaway to The Greenbrier and Lewisburg, West Virginia, for GA pilots and their partners, from KMYR to KLWB. A legendary resort, a Cold War bunker, mineral baths, golf and a charming small town.',
    lede='A legendary resort with a secret underneath.',
    intro='The Greenbrier in White Sulphur Springs has hosted presidents since the 1700s, and for 30 years it hid a secret: an emergency bunker for Congress, built under the hotel during the Cold War. Fly into the valley, tour the bunker, soak in the mineral baths, play golf, and spend an afternoon in nearby Lewisburg.',
    pills=['Grand resort', 'Cold War bunker', 'Golf & spa'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KLWB', nm=261, flight_time='~2 hr',
    style='Resort transfer', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land in the valley, 15 minutes from the resort.',
    'KLWB, Greenbrier Valley Airport, sits just north of Lewisburg, about 15 minutes from The Greenbrier in White Sulphur Springs.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Greenbrier Valley Airport FBO', '584 Airport Road, Suite 1, Lewisburg, WV 24901', '304-645-3961') +
    '<p class="note">The airport has airline service and a full-service FBO. Sources disagree on hours, so confirm them. Ask the resort about a transfer when you book, and ask the FBO about parking and fees. No live fuel price is shown.</p>'
    '<p class="note">The field is near 2,300 feet in a valley among the Allegheny ridges. Expect valley fog on fall mornings and turbulence on windy days. Review terrain, the sectional and current NOTAMs.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>The resort covers most of it.</h3><p>The Greenbrier’s grounds are walkable. Rent a car, or arrange a ride, for an afternoon in Lewisburg.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'The resort, or a small-town inn.',
    'Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('White Sulphur Springs · Grand resort', 'The Greenbrier',
         'A landmark resort with Dorothy Draper’s bold interiors, a mineral spa, golf and dozens of activities. The reason to come.',
         'https://www.greenbrier.com/') +
    card('The Greenbrier · More space', 'Greenbrier cottages & estate homes',
         'Cottages and estate homes on the resort grounds, some with porches and fireplaces. Ask the resort when you book.') +
    card('Lewisburg · Historic inn', 'The General Lewis Inn',
         'A historic inn in downtown Lewisburg, filled with antiques and a short walk to shops and restaurants.',
         'https://www.generallewisinn.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One very grand.',
    'Reserve resort dinners ahead, and check dress codes.') +
    '<div class="grid three">' +
    card('Friday dinner · Steakhouse', 'Prime 44 West',
         'The Greenbrier’s steakhouse, named for basketball great Jerry West, with the 44-ounce porterhouse and Cathy Justice’s cornbread.',
         'https://www.greenbrier.com/dining/prime-44-west/') +
    card('Saturday dinner · Grand', 'The Main Dining Room',
         'The Greenbrier’s grand dining room, with live music and more than a century of tradition. Dress for dinner.',
         'https://www.greenbrier.com/dining/main-dining-room/') +
    card('Lunch or dinner · Lewisburg', 'The General Lewis Inn restaurant',
         'Classic dining in the historic inn on Lewisburg’s main street. A good break from the resort.',
         'https://www.generallewisinn.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'A bunker, the baths and a small town.',
    'Choose one big outing a day and leave room for the resort.') +
    '<div class="explore-list">' +
    explore(1, 'The Bunker tour',
            'A guided tour of the once top-secret Cold War emergency relocation center for Congress, built under the hotel and revealed in 1992. Book ahead; cameras and phones aren’t allowed.',
            'https://www.greenbrier.com/activities/bunker-tours/', 'Bunker tours') +
    explore(2, 'Golf',
            'Several courses on the grounds, led by The Old White TPC, a classic 1914 design.') +
    explore(3, 'Resort activities',
            'Falconry, fly-fishing, carriage rides, sporting clays, tennis and off-road driving. Book a few the week before.') +
    explore(4, 'Downtown Lewisburg',
            'A lively small town with galleries, shops, Carnegie Hall and good restaurants. Easy for an afternoon.') +
    explore(5, 'The Greenbrier River Trail',
            'A 78-mile rail trail along the Greenbrier River. Rent bikes and ride a short stretch.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>The Greenbrier spa · Time for two</h3>'
    '<p>The resort was built around its sulphur springs, and its spa still offers mineral baths, couples treatments and an indoor pool. <a href="https://www.greenbrier.com/spa/" target="_blank" rel="noopener">Spa details</a>.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the county visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('August', 'State Fair of West Virginia',
         'The state fair, held just outside Lewisburg. Fun, and it fills local lodging.') +
    card('October', 'Fall color',
         'The valley and ridges turn in mid-October. Beautiful, and busy.') +
    card('December', 'Holidays at The Greenbrier',
         'Lights, decorations and holiday events at the resort.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the county visitor site when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://greenbrierwv.com/" target="_blank" rel="noopener">Browse Greenbrier County events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the bunker, the baths, golf and two resort dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & settle in', [
        ('Late-morning arrival', 'Land at KLWB, subject to weather and your actual flight plan, and transfer to the resort.'),
        ('Afternoon', 'The Bunker tour.'),
        ('Evening', 'Dinner at Prime 44 West.')]) +
    day('SAT', 'Resort day', [
        ('Morning', 'Golf on The Old White, or falconry and a carriage ride.'),
        ('Afternoon', 'The mineral baths and the spa.'),
        ('Evening', 'Dinner in the Main Dining Room.')]) +
    day('SUN', 'Lewisburg & home', [
        ('Morning', 'Brunch and a walk in downtown Lewisburg.'),
        ('Before leaving', 'Allow time at the FBO.'),
        ('Fly home', 'Valley fog often lifts by mid-morning; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'The resort and transfer first, then the bunker tour, dinners, tee times and the spa.'),
          ('Dress codes', 'Some dining rooms ask for jackets in the evening. Check before you pack.'),
          ('Mountain valley', 'Fog, ridges and gusty winds. Fly in the morning and keep a backup day.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=29, place='The Greenbrier, West Virginia', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
