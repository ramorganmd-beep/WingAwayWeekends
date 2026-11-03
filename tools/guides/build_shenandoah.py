"""Generate docs/shenandoah/index.html (Shenandoah National Park and Luray, Virginia)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = None  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['shenandoah']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='shenandoah', name='Shenandoah & Luray', state='Virginia', number=27, reviewed=REVIEWED,
    description='A curated two-night Shenandoah National Park and Luray getaway for GA pilots and their partners, from KMYR to KLUA. Skyline Drive, Luray Caverns, mountain lodges and short summit hikes.',
    lede='Skyline Drive, caverns and a mountain lodge.',
    intro='Luray sits in the Page Valley between the Blue Ridge and Massanutten Mountain, a few minutes from Shenandoah National Park. Land in the valley, explore the great caverns, drive Skyline Drive to overlooks above the clouds, and stay at a lodge on the ridge or a gracious inn in town.',
    pills=['Skyline Drive', 'Caverns', 'Summit hikes'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KLUA', nm=300, flight_time='~2 hr 16 <small>min</small>',
    style='Car needed', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land in the valley below the park.',
    'KLUA, Luray Caverns Airport, is a few minutes from Luray and the caverns, and about 15 minutes from the park’s Thornton Gap entrance on Skyline Drive.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Luray Caverns Airport', '1504 Airport Road, Luray, VA 22835', '540-743-6070') +
    '<p class="note">A small field with listed hours of about 8 a.m. to 6 p.m. Rental cars are limited here; call ahead about a courtesy car or a rental delivered to the airport. Ask about overnight parking and fees. No live fuel price is shown.</p>'
    '<p class="note">This is mountain flying: the Blue Ridge rises just east of the field and Massanutten Mountain to the west. Expect turbulence on windy days and valley fog in the morning. The Washington, DC SFRA lies to the east; review terrain, the sectional and current NOTAMs and TFRs.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>You’ll need a car.</h3><p>Skyline Drive, the lodges and the trailheads are spread along the ridge. The speed limit on Skyline Drive is 35 mph, so allow plenty of time.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'On the ridge or in town.',
    'Park lodges are seasonal, usually spring through fall. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('In the park · Seasonal', 'Skyland',
         'A historic lodge at the highest point of Skyline Drive, with sweeping views over the valley and rooms near the Stony Man trail.') +
    card('Luray · Historic inn', 'The Mimslyn Inn',
         'A gracious 1931 Colonial Revival inn on a hill above Luray, with Circa ’31 restaurant and the Speakeasy bar. Open year-round.') +
    card('In the park · Seasonal', 'Big Meadows Lodge',
         'A rustic 1939 stone-and-timber lodge beside a wide mountain meadow, known for deer at dusk and dark night skies.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One with a view.',
    'Dining is simple here, with one famous exception. Reserve ahead.') +
    '<div class="grid three">' +
    card('Friday dinner · Luray', 'Circa ’31',
         'The dining room at The Mimslyn Inn, with Southern-inspired dishes in an elegant room.') +
    card('Special occasion · About 45 minutes', 'The Inn at Little Washington',
         'One of the most celebrated restaurants in the country, in the village of Washington, Virginia, over Thornton Gap. Book far ahead.') +
    card('Lunch · Skyline Drive', 'Pollock Dining Room at Skyland',
         'Simple lodge cooking with big windows over the Shenandoah Valley. Seasonal.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Underground and on top.',
    'Mix one big view with one short hike each day.') +
    '<div class="explore-list">' +
    explore(1, 'Luray Caverns',
            'The largest caverns in the East, with huge chambers and the Great Stalacpipe Organ. The ticket includes a car and carriage museum. About an hour underground.') +
    explore(2, 'Skyline Drive',
            'A 105-mile road along the crest of the Blue Ridge with more than 70 overlooks. Thornton Gap to Big Meadows makes a beautiful half day.',
            'https://www.nps.gov/shen/', 'Park information') +
    explore(3, 'Stony Man',
            'A short, moderate walk near Skyland to cliffs with one of the best views in the park. Under two miles round trip.') +
    explore(4, 'Hawksbill & Dark Hollow Falls',
            'Hawksbill is the park’s highest peak; Dark Hollow Falls is a short, steep walk to a waterfall near Big Meadows.') +
    explore(5, 'The Shenandoah River',
            'Canoe, kayak or float the South Fork near Luray in summer with a local outfitter.') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the season is the reason to fly.',
    'This prototype links to the park’s site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('October', 'Fall color',
         'Usually mid-to-late October. Spectacular and very busy; expect lines at the park entrances on weekends.') +
    card('May', 'Wildflowers',
         'Spring wildflowers and fresh green along the ridge, with quieter weekends.') +
    card('Summer', 'Cool mornings',
         'The ridge is cooler than the valley. Start early; afternoon storms are common.') +
    '</div><div class="calendar"><div><h3>Park news, closures & ranger programs</h3><p>Check the park site for Skyline Drive closures, lodge seasons and permits, and confirm with the organizer.</p></div>'
    '<a class="button" href="https://www.nps.gov/shen/planyourvisit/calendar.htm" target="_blank" rel="noopener">Browse park events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the caverns, Skyline Drive and a summit walk. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & underground', [
        ('Late-morning arrival', 'Land at KLUA, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Luray Caverns, then check in.'),
        ('Evening', 'Dinner at Circa ’31.')]) +
    day('SAT', 'Up on the ridge', [
        ('Morning', 'Drive Skyline Drive south from Thornton Gap and walk to Stony Man.'),
        ('Afternoon', 'Lunch at Skyland, then Dark Hollow Falls or Hawksbill.'),
        ('Evening', 'Dinner at The Inn at Little Washington, or a quiet evening at the lodge.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'A sunrise overlook, or an easy morning in Luray.'),
        ('Before leaving', 'Return the car and allow time at the airport.'),
        ('Fly home', 'Valley fog often burns off by mid-morning; let weather set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'A car first, then lodging and dinners.'),
          ('Park entry', 'Shenandoah charges an entrance fee. Old Rag requires a separate day-use ticket in season.'),
          ('Mountain flying', 'Ridges on both sides, morning fog and afternoon storms. Keep a backup day.'),
          ('Seasons', 'Park lodges and Skyline Drive services close in winter, and the drive can close for snow or ice.')]) +
    '</section>')

P.append(page_end(number=27, place='Shenandoah & Luray, Virginia', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
