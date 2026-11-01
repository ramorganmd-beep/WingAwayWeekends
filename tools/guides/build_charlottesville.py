"""Generate docs/charlottesville/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('wine', 'Wine'), ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='charlottesville', name='Charlottesville', state='Virginia', number=8,
    description='A curated two-night Charlottesville getaway for GA pilots and their partners, from KMYR to KCHO. Virginia wine country, Monticello, estate hotels and the Downtown Mall.',
    lede='Wine country, with Jefferson for company.',
    intro='Rolling vineyards under the Blue Ridge, Thomas Jefferson’s Monticello and university, and a lively pedestrian Downtown Mall. Charlottesville is a weekend of long lunches, tastings and country drives.',
    pills=['Wineries', 'History', 'Estate hotels'],
    photo='charlottesville', widths=[480, 960], alt='Tree-lined Downtown Mall in Charlottesville', img_w=960, img_h=640,
    caption='The Downtown Mall', airport='KCHO', nm=269, flight_time='~2 hr 3 <small>min</small>',
    style='Rental car', estimate_extra='The Blue Ridge lies just west of the field; check mountain weather and terrain on your route. ', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then head for the vineyards.',
    'KCHO, Charlottesville-Albemarle Airport, is a towered field about 15 minutes north of town.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Signature Aviation', 'Charlottesville-Albemarle Airport', None, 'https://www.signatureaviation.com/locations/CHO') +
    '<p class="note">Signature is the FBO; directory listings give different phone numbers, so use its own page. Ask about 100LL pricing, facility fees, two-night parking, waivers with fuel and after-hours access. No live price is shown.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>A car is essential.</h3><p>Wineries, Monticello and the estate hotels are spread across the countryside. Arrange a rental car before you fly.</p><p>Plan a designated driver, or book a winery tour with a driver for tasting days.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Three different stays: a country estate, a resort with a spa and an inn near the university.') +
    '<div class="grid three">' +
    card('Country estate · Splurge', 'Keswick Hall',
         'A luxury estate hotel in the countryside east of town, with fine dining, a bar, golf and grounds made for a romantic stroll.') +
    card('Resort · Spa & golf', 'Boar’s Head Resort',
         'A resort near the university with a spa, golf course and several restaurants. Easy for a spa-and-wine weekend.') +
    card('Boutique inn · Near UVA', 'Oakhurst Inn',
         'A well-reviewed boutique inn near the university and the Rotunda, close to restaurants. Choose it if you want to be in town.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long winery lunch.',
    'Charlottesville’s best tables fill quickly on weekends. Reserve dinners ahead.') +
    '<div class="grid three">' +
    card('Friday dinner · Speakeasy feel', 'The Alley Light',
         'A small, atmospheric restaurant and bar on Second Street off the Downtown Mall. An easy, romantic first night.') +
    card('Saturday dinner · Date night', 'Oakhart Social',
         'A popular date-night spot that fills up fast. Reserve well ahead.') +
    card('Lunch · Classic', 'C&O Restaurant',
         'A warm, intimate long-time favorite near the Downtown Mall with a varied menu. Or have lunch at a winery.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'History, mountains and the Mall.',
    'Mix one history stop with wine and a country drive.') +
    '<div class="explore-list">' +
    explore(1, 'Monticello',
            'Thomas Jefferson’s mountaintop home and gardens, just outside town. Book timed tickets ahead and allow at least half a day.') +
    explore(2, 'University of Virginia',
            'Jefferson’s Academical Village and the Rotunda, a UNESCO World Heritage Site with Monticello. Lovely for a walk.') +
    explore(3, 'The Downtown Mall',
            'A tree-lined brick pedestrian street with shops, galleries, cafés and outdoor tables. The heart of the evening.') +
    explore(4, 'Blue Ridge drive',
            'Skyline Drive and the Blue Ridge Parkway meet about 30 minutes west, with overlooks and fall color. Check road status.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>A resort spa · Time for two</h3>'
    '<p>Boar’s Head Resort and Keswick Hall both have spas. A couples treatment pairs well with an afternoon of tastings.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-hotel guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="wine">' + head('05', 'Wine', 'Taste your way through the countryside.',
    'The Monticello Wine Trail has dozens of wineries. Pick two or three a day and leave room for a long lunch.') +
    '<div class="grid three">' +
    card('Historic estate', 'Barboursville Vineyards',
         'One of Virginia’s most historic wineries, with the ruins of a Jefferson-designed mansion on the grounds and a restaurant. About 40 minutes northeast.') +
    card('Mountain views', 'King Family Vineyards',
         'A popular Crozet winery with Blue Ridge views, known for polo on summer Sundays. Check tasting reservations and the polo schedule.') +
    card('Plan a route', 'Monticello Wine Trail',
         'Many wineries cluster around Charlottesville. Use the trail map to plan a short route and book tastings ahead on weekends.') +
    '</div></section>')

P.append('<section id="events">' + head('06', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the destination calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Spring & fall', 'Foxfield Races',
         'Steeplechase races in the countryside, a Charlottesville social tradition. Book lodging early.') +
    card('October', 'Fall color & harvest',
         'Peak season for vineyards and the mountains. Expect full tasting rooms and higher hotel rates.') +
    card('UVA', 'University weekends',
         'Football games and graduation fill hotels quickly. Check the university calendar before you book.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.visitcharlottesville.org/" target="_blank" rel="noopener">Browse Charlottesville events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: Monticello, a winery day and two dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KCHO, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Lunch at C&O, then a walk on the Downtown Mall and through UVA’s Academical Village.'),
        ('Evening', 'Dinner at The Alley Light.')]) +
    day('SAT', 'Wine country', [
        ('Morning', 'Monticello with timed entry.'),
        ('Afternoon', 'Two winery tastings, perhaps King Family and one more on the trail, with a designated driver.'),
        ('Evening', 'Dinner at Oakhart Social.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Spa time at your resort, or a short drive toward the Blue Ridge.'),
        ('Before leaving', 'Return the car and allow time at the FBO.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('08', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and car first, then Monticello tickets, dinners and winery tastings.'),
          ('Wine and flying', 'Plan tastings well away from flying, and use a driver or tour on tasting days.'),
          ('Allow for the season', 'Fall is peak; spring is lovely. Summer afternoons can bring storms over the mountains.'),
          ('Dates come next', 'Rates, tastings and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=8, place='Charlottesville, Virginia', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html='Downtown Mall, Charlottesville, Virginia, by Alex Proimos from Sydney, Australia, <a href="https://commons.wikimedia.org/wiki/File:Downtown_Mall,_Charlottesville,_Virginia_(5867535213).jpg">Wikimedia Commons</a>, <a href="https://creativecommons.org/licenses/by/2.0">CC BY 2.0</a>. Resized for display.'))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
