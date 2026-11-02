"""Generate docs/smoky-mountains/index.html (Great Smoky Mountains: Gatlinburg and Townsend, Tennessee)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['smoky-mountains']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='smoky-mountains', name='Great Smoky Mountains', state='Tennessee', number=18,
    description='A curated two-night Great Smoky Mountains getaway for GA pilots and their partners, from KMYR to KGKT. Mountain inns, Cades Cove, waterfall hikes and Blackberry Farm.',
    lede='Blue ridges, mountain inns and quiet trails.',
    intro='America’s most visited national park is a short drive from the runway in Sevierville. Stay at a quiet inn near Gatlinburg or on the peaceful Townsend side, hike to a waterfall, drive the Cades Cove loop at dawn, and splurge, if you like, on one of the country’s most celebrated country hotels.',
    pills=['National park', 'Mountain inns', 'Hiking'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KGKT', nm=262, flight_time='~2 hr 0 <small>min</small>',
    style='Rental car', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land in the foothills.',
    'KGKT, Gatlinburg-Pigeon Forge Airport, is in Sevierville, about 30 minutes from Gatlinburg and the park entrance. For Blackberry Farm and Townsend, Knoxville’s McGhee Tyson (KTYS) is closer.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Gatlinburg-Pigeon Forge Airport', '134 Air Museum Way, Sevierville, TN 37862', '865-453-8393') +
    '<p class="note">Pilots report no courtesy car, but an Enterprise rental desk serves the airport; call the local office ahead and the car can be waiting at the airplane. Recent reviews mention a new runway and FBO building. Ask about two-night parking and fees. No live fuel price is shown.</p>'
    '<p class="note">The Great Smoky Mountains rise above 6,000 feet just south of the field. Review terrain, density altitude in summer, the sectional and current NOTAMs, and plan around mountain weather and low clouds.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>A car is essential.</h3><p>The park, the towns and the inns are spread out. Rent a car for the weekend, and buy a park parking tag, required to park anywhere in the national park for more than 15 minutes.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your side of the park.',
    'Gatlinburg is lively and close to the main park road; Townsend, the “peaceful side,” is quieter and near Cades Cove. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Near Gatlinburg · Quiet inn', 'Buckhorn Inn',
         'A long-established country inn on a hillside outside Gatlinburg, close to the park but away from the crowds. Breakfast and mountain views.',
         'https://www.buckhorninn.com/') +
    card('Gatlinburg · Creekside', 'Old Creek Lodge',
         'Rooms with private balconies over a mountain stream, a short walk from downtown Gatlinburg. Ask for a king suite with a fireplace.',
         'https://www.oldcreeklodgegatlinburg.com/') +
    card('Townsend · Lodge & cabins', 'Dancing Bear Lodge',
         'A romantic lodge and cabins, many with hot tubs, on the quiet side of the Smokies, with its own Appalachian bistro.',
         'https://dancingbearlodge.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One picnic.',
    'Mountain dining is casual. Reserve where you can, and pack a picnic for the park.') +
    '<div class="grid three">' +
    card('Friday dinner · Steakhouse', 'The Peddler Steakhouse',
         'A long-running Gatlinburg favorite in a log building beside the river, where you choose your steak cut at the table.',
         'https://peddlergatlinburg.com/') +
    card('Saturday dinner · Appalachian', 'Dancing Bear Appalachian Bistro',
         'Seasonal mountain cooking at Dancing Bear Lodge in Townsend. Reserve ahead.',
         'https://dancingbearlodge.com/dining/') +
    card('Lunch · In the park', 'A picnic in Cades Cove',
         'Pick up subs and sandwiches at J.O.E. and Pop’s Sub Shoppe in Gatlinburg, then eat in the meadows of Cades Cove or beside a stream. Many couples say it is the best meal of the weekend.',
         'https://www.joeandpops.com/', 'J.O.E. and Pop’s Sub Shoppe') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Into the park.',
    'Start early; the park is busiest from late morning.') +
    '<div class="explore-list">' +
    explore(1, 'Cades Cove',
            'An 11-mile one-way loop through a mountain valley of meadows, historic cabins and churches, with deer and often black bears. Go at sunrise to beat the traffic.',
            'https://www.nps.gov/grsm/', 'Park information') +
    explore(2, 'Newfound Gap Road & Kuwohi',
            'Drive over the crest of the Smokies to Newfound Gap, then on to Kuwohi (formerly Clingmans Dome), the park’s highest point, for a short, steep walk to the observation tower. Check road status in winter.') +
    explore(3, 'A waterfall hike',
            'Choose your effort: Laurel Falls is a short paved walk, Grotto Falls lets you walk behind the water, and Alum Cave is a longer climb to dramatic views.') +
    explore(4, 'Arts & crafts loop',
            'The Great Smoky Arts & Crafts Community outside Gatlinburg has dozens of working studios along an eight-mile loop: pottery, woodwork, brooms and quilts.') +
    explore(5, 'Dollywood',
            'Dolly Parton’s theme park in Pigeon Forge, known for its mountain setting, crafts and seasonal festivals. A fun day if the weather turns.') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the park and town calendars. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Late May–June', 'Synchronous fireflies',
         'Fireflies flash in unison at Elkmont for about two weeks. Viewing is by lottery; apply in spring.') +
    card('Mid–late October', 'Fall color',
         'Peak color moves down the mountains through October. Beautiful and very busy; book early.') +
    card('November–February', 'Smoky Mountain Winterfest',
         'Millions of holiday lights across Gatlinburg, Pigeon Forge and Sevierville. Quieter trails, too.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the town calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.gatlinburg.com/" target="_blank" rel="noopener">Browse Gatlinburg events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: an inn, a sunrise drive and a waterfall. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KGKT, subject to weather and your actual flight plan, and pick up the rental car.'),
        ('Afternoon', 'Drive to your inn, then wander the arts and crafts loop.'),
        ('Evening', 'Dinner at The Peddler.')]) +
    day('SAT', 'Into the park', [
        ('Sunrise', 'Drive the Cades Cove loop while the wildlife is out.'),
        ('Afternoon', 'A picnic, then a waterfall hike.'),
        ('Evening', 'Dinner at Dancing Bear Appalachian Bistro in Townsend.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'A slow breakfast and a drive to Newfound Gap, if clouds allow.'),
        ('Before leaving', 'Return the car and allow time at the FBO.'),
        ('Fly home', 'Mountain clouds can linger in the morning; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Rental car and lodging first, then dinners.'),
          ('Park parking tags', 'Required to park in the national park for more than 15 minutes. Buy one online or at a visitor center.'),
          ('Crowds', 'Summer weekends and October are very busy. Start early and avoid Gatlinburg’s main strip at peak times.'),
          ('Mountain flying', 'High terrain, haze and quick-building storms. Fly in the morning and keep a backup day.')]) +
    '</section>')

P.append(page_end(number=18, place='Great Smoky Mountains, Tennessee', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
