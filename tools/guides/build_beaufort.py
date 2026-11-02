"""Generate docs/beaufort/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 2, 2026'  # owner review date; None while still a draft
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('shopping', 'Shop'), ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='beaufort', name='Beaufort', state='South Carolina', number=5, reviewed=REVIEWED,
    description='A curated two-night Beaufort getaway for GA pilots and their partners, from KMYR to KARW. Lowcountry inns, waterfront dining, Hunting Island and an unhurried pace.',
    lede='A short flight. Lowcountry time.',
    intro='Antebellum homes under live oaks, a waterfront park made for slow evenings and salt marsh in every direction. Beaufort is small, quiet and easy, and the airport is just across the river from town.',
    pills=['Waterfront', 'Historic inns', 'Marsh & beach'],
    photo='beaufort-bay-street', widths=[480, 960], alt='Historic storefronts along Bay Street in downtown Beaufort, South Carolina', img_w=960, img_h=720,
    caption='Bay Street · Downtown Beaufort at golden hour', img_style='object-position:50% 65%', airport='KARW', nm=115, flight_time='~1 hr 1 <small>min</small>',
    style='Courtesy car + walks', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then cross the river.',
    'KARW, Beaufort Executive Airport (formerly Beaufort County Airport), is on Lady’s Island, a few minutes across the bridge from downtown.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The airport FBO</h3>' +
    fbo('Beaufort Executive Airport', '39 Airport Circle, Beaufort, SC 29907', '843-255-2972', 'https://www.beaufortcountyairport.com/') +
    '<p class="note">The airport runs its own FBO, with 100LL, transient parking, a courtesy car and rental cars listed. Listed hours are roughly 8 AM–5:30 PM weekdays and 9 AM–4 PM Saturday, so call about Sunday departures and after-hours access. Ask about the nightly transient fee and any waiver with fuel. No live fuel price is shown.</p>'
    '<p class="note">Marine Corps Air Station Beaufort is nearby. Review the sectional, restricted areas and current NOTAMs, and expect military traffic. Check runway length and obstacles in the Chart Supplement.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Short hops, then on foot.</h3><p>Downtown is about 10 minutes from the field. Ask about the courtesy car for short trips, or arrange a rental car if you plan to visit Hunting Island or the Penn Center.</p><p>The historic district and waterfront are best explored on foot.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'Beaufort is a town of inns rather than big hotels. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Boutique waterfront inn', 'Anchorage 1770',
         'A restored 18th-century house on the Bay Street waterfront, with its own restaurant, the Ribaut Social Club. The most romantic choice; ask for a water-view room.',
         'https://anchorage1770.com/') +
    card('Historic district · Classic inn', 'The Rhett House Inn',
         'An antebellum inn with wide verandas, a short walk from the waterfront. Classic Lowcountry charm and a good base for exploring on foot.',
         'https://rhetthouseinn.com/') +
    card('In town · Historic', 'The Beaufort Inn',
         'A well-reviewed historic inn in the heart of downtown, close to restaurants and the waterfront park. Confirm room type and parking.',
         'https://www.beaufortinn.com/') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One easy lunch.',
    'A small town with a strong seafood scene. Reserve the anchor dinners, especially in spring and fall.') +
    '<div class="grid three">' +
    card('Friday dinner · On the water', 'Saltus River Grill',
         'Beaufort’s best-known restaurant: contemporary seafood with views of the river and the swing bridge. Ask for a table near the windows or on the terrace at sunset.',
         'https://saltusrivergrill.com/') +
    card('Saturday dinner · European-Lowcountry', 'Ribaut Social Club',
         'The restaurant at Anchorage 1770, with a European sensibility and a Lowcountry table. Quieter and more intimate than Friday. Reserve ahead.',
         'https://ribautsocialclub.com/') +
    card('Lunch · Bay Street', 'Plums',
         'A casual, long-running Bay Street spot backing onto the waterfront park. Easy for lunch between walks. For a dressier alternative, try Wren Bistro & Bar.',
         'https://plumsrestaurant.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Under the oaks. Out on the marsh.',
    'Beaufort rewards an unhurried pace. Pick one outing beyond town and let the rest of the weekend be slow.') +
    '<div class="explore-list">' +
    explore(1, 'Historic district & Waterfront Park',
            'Antebellum homes, live oaks and Spanish moss, many of them film locations. End at the Henry C. Chambers Waterfront Park, with its swings facing the river: the best seat in town at sunset.') +
    explore(2, 'Horse-drawn carriage tour',
            'A relaxed way to hear the town’s history from a local guide. Tours leave from Bay Street; Southurn Rose Carriage Tours is one operator. Book ahead in busy seasons.') +
    explore(3, 'Hunting Island State Park',
            'A wild barrier-island beach about 30 minutes away, with marsh boardwalks, maritime forest and a historic lighthouse. Check whether the lighthouse is open for climbing on your dates.') +
    explore(4, 'Penn Center, St. Helena Island',
            'One of the first schools for formerly enslaved people, and part of the Reconstruction Era National Historical Park. A meaningful stop on the drive to Hunting Island. Check hours.') +
    explore(5, 'Spanish Moss Trail',
            'A flat rail-trail along the marsh, made for an easy walk or bike ride. Ask locally about bike rentals.') +
    explore(6, 'Parris Island Museum',
            'The history of the Marine Corps recruit depot. It is on an active military base, so check current visitor access rules and ID requirements before going.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>Time for two</h3>'
    '<p>Beaufort’s romance is mostly outdoors: the waterfront swings, a carriage ride, a sunset boat outing from the downtown marina. For a massage, ask your inn which local spas it recommends or whether it can arrange in-room treatments.</p>'
    '<p>Visit Beaufort’s own romantic-getaway itinerary includes spa ideas and current openings.</p>'
    '<a href="https://beaufortsc.org/plan-your-visit/suggested-itineraries/romantic-getaway/" target="_blank" rel="noopener">Visit Beaufort romantic getaway ideas</a></div></section>')

P.append('<section id="shopping">' + head('05', 'Shopping & boutiques', 'Bring home something with a story.',
    'Bay Street is the heart of it: a few walkable blocks of galleries, boutiques and bookshops.') +
    '<div class="grid three">' +
    card('Downtown', 'Bay Street shops & galleries',
         'Independent boutiques, home goods, Lowcountry art and a bookshop or two, all within a short stroll of the waterfront park.') +
    card('Local art', 'Lowcountry galleries',
         'Marsh landscapes, sweetgrass baskets and Gullah art. A meaningful souvenir that is genuinely from here.') +
    '</div></section>')

P.append('<section id="events">' + head('06', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the destination calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('July', 'Beaufort Water Festival',
         'The town’s big summer celebration on the waterfront, with boats, music and events. Lively, hot and busy; book lodging early.') +
    card('October', 'Pat Conroy Literary Festival',
         'A celebration of Beaufort’s best-known writer and Southern literature, with readings and events around town.') +
    card('Spring & fall', 'Best seasons',
         'Mild weather, azaleas in spring and comfortable evenings on the water. Summer is hot, humid and buggy on the marsh.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://beaufortsc.org/" target="_blank" rel="noopener">Browse Beaufort events</a></div></section>')

P.append('<section id="itinerary">' + head('07', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the historic town, one beach and history day, and two waterfront dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KARW, subject to the actual flight plan, and drive the few minutes into town.'),
        ('Afternoon', 'Lunch at Plums, a carriage tour, then check in and rest on the veranda.'),
        ('Evening', 'Sunset on the waterfront park swings, then dinner at Saltus River Grill.')]) +
    day('SAT', 'Island day', [
        ('Morning', 'Drive out to the Penn Center, then on to Hunting Island for the beach and marsh boardwalks.'),
        ('Afternoon', 'Back to town to browse Bay Street, or walk part of the Spanish Moss Trail.'),
        ('Evening', 'Dinner at the Ribaut Social Club.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast at your inn and a last walk under the oaks.'),
        ('Before leaving', 'Return the car and allow time at the FBO, especially if it keeps shorter weekend hours.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('08', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Inn first (there are few rooms in town), then ground transport and the two dinners.'),
          ('Allow for the season', 'Summer brings heat, afternoon storms and no-see-ums on the marsh. Bring insect repellent.'),
          ('Check FBO hours', 'Weekend hours are shorter than at bigger airports. Confirm fuel and access for your departure time.'),
          ('Dates come next', 'Inn rates, tours and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=5, place='Beaufort, South Carolina', reviewed=REVIEWED, note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html='Bay Street Downtown Beaufort.JPG by Cdamgen (BeaufortTiger), English Wikipedia, <a href="https://commons.wikimedia.org/wiki/File:Bay_Street_Downtown_Beaufort.JPG">Wikimedia Commons</a>, public domain. Cropped and resized for display.'))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
