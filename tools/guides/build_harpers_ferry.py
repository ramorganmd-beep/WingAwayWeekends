"""Generate docs/harpers-ferry/index.html (Harpers Ferry and Shepherdstown, West Virginia)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 2, 2026'  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['harpers-ferry']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='harpers-ferry', name='Harpers Ferry', state='West Virginia', number=22, reviewed=REVIEWED,
    description='A curated two-night Harpers Ferry getaway for GA pilots and their partners, from KMYR to KMRB Martinsburg. A historic river town, Maryland Heights, the C&O Canal towpath and Shepherdstown dinners.',
    lede='Where two rivers meet below the mountains.',
    intro='Harpers Ferry sits where the Potomac and the Shenandoah join, its 19th-century lower town climbing a steep hillside below the Blue Ridge. Walk the national historical park, hike to the overlook on Maryland Heights, bike the C&O Canal towpath, and spend the evenings in Shepherdstown, a lively little college town nearby.',
    pills=['Civil War history', 'River views', 'Hiking'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KMRB', nm=347, flight_time='~2 hr 34 <small>min</small>',
    style='Crew car or rental car', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land in Martinsburg.',
    'KMRB, Eastern West Virginia Regional (Shepherd Field), is a towered airport about 30 minutes from Harpers Ferry and 20 minutes from Shepherdstown.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('MRB Aviation', '170 Aviation Way, Martinsburg, WV 25405', '304-262-2507') +
    '<p class="note">The airport-owned FBO lists fuel, a crew car and Enterprise rentals, which pilots report can be delivered to the FBO. Call ahead to confirm the crew car, two-night parking and fees. No live fuel price is shown.</p>'
    '<p class="note">The Washington, DC SFRA and the Camp David prohibited area (P-40) lie to the east. Review the sectional and current NOTAMs carefully, and watch for temporary flight restrictions. Ridges run along the Blue Ridge to the south and east.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>You’ll want a car.</h3><p>Harpers Ferry, Shepherdstown and the trails are 15–30 minutes apart. Parking in Harpers Ferry’s lower town is very limited; park at the national park visitor center and ride the shuttle down.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'A historic inn in the lower town, or a riverside inn in Shepherdstown. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Lower town · Historic', 'The Town’s Inn',
         'Rooms in a pair of buildings about 200 years old in Harpers Ferry’s historic lower town. Everything is walkable, including the trails and the rivers.',
         'https://thetownsinn.com/') +
    card('Shepherdstown · On the river', 'The Bavarian Inn',
         'A long-running inn on the bluffs above the Potomac in Shepherdstown, with river-view rooms and its own restaurant. A comfortable, romantic base.',
         'https://www.bavarianinnwv.com/') +
    card('Bed & breakfast · Intimate', 'Lily Garden Bed & Breakfast',
         'A small bed and breakfast often recommended for couples. Confirm rooms, breakfast and how far it is from the lower town.',
         'https://lilygardenbnb.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One river-town lunch.',
    'The best special-occasion dinner is in the countryside nearby. Reserve weekend dinners ahead.') +
    '<div class="grid three">' +
    card('Friday dinner · Gastropub', 'The Rabbit Hole',
         'A cozy, rustic gastropub in Harpers Ferry with a locally inspired menu. An easy first night after the flight.',
         'https://rabbitholewv.com/') +
    card('Saturday dinner · Fine dining', 'Redbook at Hillbrook Inn',
         'A romantic fine-dining room at the Hillbrook Inn near Charles Town, about 20 minutes away. Business casual attire is expected; reserve well ahead.',
         'https://www.hillbrookinn.com/charles-town-wv-restaurant.html') +
    card('Lunch · Wine bar', 'Snallygasters Cafe & Wine Bar',
         'A relaxed café and wine bar, good for lunch or a glass after a hike. For farm-to-table cooking instead, try Kelley Farm Kitchen in Bolivar.',
         'https://www.snallygasterscafe.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'History, rivers and big views.',
    'Most of the best experiences here are outdoors. Wear good walking shoes.') +
    '<div class="explore-list">' +
    explore(1, 'Harpers Ferry National Historical Park',
            'The restored lower town, John Brown’s Fort and the museums tell the story of the armory, the 1859 raid and the Civil War. The rivers meet just beyond the main street.',
            'https://www.nps.gov/hafe/', 'Park information') +
    explore(2, 'Maryland Heights overlook',
            'A steep climb across the Potomac to the classic view down onto the town and the meeting of the rivers. Allow three to four hours round trip. For an easier walk, climb the stone steps to Jefferson Rock.') +
    explore(3, 'C&O Canal towpath',
            'A flat, shaded path along the Potomac on the Maryland side, reached by the footbridge from town. Walk a few miles or rent bikes and ride.') +
    explore(4, 'Tubing and paddling',
            'In summer, River & Trail Outfitters runs tubing, rafting and canoe trips on the Shenandoah and Potomac, and rents bikes for the C&O Canal towpath. Book ahead and check river levels.',
            'https://www.rivertrail.com/', 'River & Trail Outfitters') +
    explore(5, 'Shepherdstown & Antietam',
            'Shepherdstown has shops, restaurants and an easy small-town evening. Antietam National Battlefield, site of the bloodiest single day of the Civil War, is about 15 minutes beyond it.') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the county visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('June–August', 'River season',
         'Tubing, paddling and long evenings by the water. Weekends are busy; arrive early to park.') +
    card('Mid–late October', 'Fall color',
         'The ridges around the rivers turn red and gold. The most beautiful and busiest season.') +
    card('December', 'Old Tyme Christmas',
         'Harpers Ferry’s lower town celebrates the holidays with candlelit streets and seasonal events. Check dates.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the county visitor site when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.discoverthepanhandle.com/" target="_blank" rel="noopener">Browse Jefferson County events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the lower town, a mountain overlook and a countryside dinner. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & the lower town', [
        ('Late-morning arrival', 'Land at KMRB, subject to weather, nearby restricted airspace and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Park at the visitor center, ride the shuttle down and wander the lower town and the rivers.'),
        ('Evening', 'Dinner at The Rabbit Hole.')]) +
    day('SAT', 'The overlook', [
        ('Morning', 'Hike Maryland Heights for the view, or walk the C&O Canal towpath.'),
        ('Afternoon', 'Lunch and a glass of wine at Snallygasters, then a slow afternoon in Shepherdstown.'),
        ('Evening', 'Dinner at Redbook at Hillbrook Inn.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Antietam National Battlefield, or Jefferson Rock and a last look at the rivers.'),
        ('Before leaving', 'Return the car and allow time at the FBO.'),
        ('Fly home', 'Check the latest TFRs and NOTAMs before departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Car and lodging first, then dinners and any river trip.'),
          ('Airspace', 'The DC SFRA and P-40 are nearby, and TFRs are common. Brief them carefully.'),
          ('Parking', 'Lower-town parking is scarce. Use the national park visitor center and shuttle.'),
          ('Dates come next', 'Rates, river trips and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=22, place='Harpers Ferry, West Virginia', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
