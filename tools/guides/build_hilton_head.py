"""Generate docs/hilton-head/index.html."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
REVIEWED = 'November 3, 2026'  # owner review date; None while still a draft
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['hilton-head']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='hilton-head', name='Hilton Head', state='South Carolina', number=23, reviewed=REVIEWED,
    description='A curated two-night Hilton Head Island getaway for GA pilots and their partners, from KMYR to KHXD. Wide beaches, bike paths, Harbour Town, golf and Lowcountry dinners.',
    lede='Land on the island. Ride a bike to the beach.',
    intro='Hilton Head’s airport sits right on the island, minutes from wide, hard-packed beaches and more than 60 miles of bike paths under the live oaks. Ride to the beach, watch the sunset at Harbour Town’s red-and-white lighthouse, and book a long Lowcountry dinner on the water.',
    pills=['Beaches & bikes', 'Golf', 'Sunset dinners'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KHXD', nm=125, flight_time='~1 hr 5 <small>min</small>',
    style='Bikes + short rides', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land on the island.',
    'KHXD, Hilton Head Airport, is a towered field on the north end of the island, about 15–25 minutes from the beaches and Sea Pines.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Signature Aviation', '52 Gateway Circle, Hilton Head Island, SC 29926', '843-689-3200') +
    '<p class="note">Signature lists courtesy and rental cars and can arrange resort transfers. Ask about overnight parking, facility fees and fee waivers with fuel. The airport has airline service and a relatively short runway; check performance for your aircraft, especially in summer heat. No live fuel price is shown.</p>'
    '<p class="note">Savannah’s Class C airspace lies just to the southwest. Review the sectional and current NOTAMs, and expect afternoon storms in summer.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Bikes do most of the work.</h3><p>Most resorts rent bikes, and the island’s paths and flat beaches make them the best way around. Use a rental car or rideshare for dinners across the island and the drive to Sea Pines.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your stretch of beach.',
    'Oceanfront resorts on the island’s Atlantic side. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Oceanfront · Spa', 'The Westin Hilton Head Island Resort & Spa',
         'A large oceanfront resort on a quiet stretch of beach, with a full spa and couples packages. Easy for a beach-and-spa weekend.',
         'https://www.marriott.com/HHHWI') +
    card('Oceanfront · Classic', 'Omni Hilton Head Oceanfront Resort',
         'A long-running resort right on the beach in Palmetto Dunes, with pools, restaurants and bikes to rent.',
         'https://www.omnihotels.com/hotels/hilton-head') +
    card('Oceanfront · Relaxed', 'Sonesta Resort Hilton Head Island',
         'A beachfront resort near Shipyard, with on-site dining and an easy, relaxed feel.',
         'https://www.sonesta.com/sonesta-hotels-resorts/sc/hilton-head-island/sonesta-resort-hilton-head-island') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One by the water.',
    'Lowcountry seafood and sunsets over the marsh. Reserve weekend dinners.') +
    '<div class="grid three">' +
    card('Friday dinner · On the water', 'Skull Creek Boathouse',
         'Lowcountry seafood with wide water views on the island’s north end, near the airport. Go early for sunset.',
         'https://www.skullcreekboathouse.com/') +
    card('Saturday dinner · French country', 'Charlie’s L’Etoile Verte',
         'An elegant French country room with one of the island’s highest diner ratings. The special-occasion dinner.',
         'https://www.charliesgreenstar.com/') +
    card('Sunset · Harbour Town', 'CQ’s Restaurant',
         'A Harbour Town favorite in a historic building. Book a sunset table, then stroll the harbor and lighthouse after dinner.',
         'https://www.cqsrestaurant.com/') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Beach, bikes and the lighthouse.',
    'Slow and easy. Leave plenty of time for the beach.') +
    '<div class="explore-list">' +
    explore(1, 'Bike the beach and the paths',
            'At low tide the beach is firm enough to ride for miles. More than 60 miles of paved paths run through the island’s neighborhoods and forests.') +
    explore(2, 'Harbour Town & the lighthouse',
            'The red-and-white lighthouse in Sea Pines overlooks the yacht basin and the 18th green of Harbour Town Golf Links. Climb it for the view, then stay for sunset.') +
    explore(3, 'Golf',
            'Harbour Town Golf Links, home of the RBC Heritage, is the headline, with dozens of other courses on and near the island.') +
    explore(4, 'Sea Pines Forest Preserve',
            'Boardwalks and trails through marsh, ponds and live oaks, a quiet hour away from the beach.') +
    explore(5, 'Dolphins and Daufuskie Island',
            'Dolphin cruises and kayak tours leave from several marinas, and ferries run to car-free Daufuskie Island for lunch and a golf-cart ramble.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>An oceanfront resort spa · Time for two</h3>'
    '<p>The Westin’s Heavenly Spa offers couples treatments and spa packages, an easy afternoon between beach and dinner.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-resort guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the island visitor site. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('April', 'RBC Heritage',
         'The island’s PGA Tour event at Harbour Town. Exciting, and the busiest week of spring; book early or avoid it.') +
    card('Spring & fall', 'Best seasons',
         'Warm days, quieter beaches and easier tee times. Summer is hot and busy, with afternoon storms.') +
    card('Year-round', 'Live jazz',
         'The Jazz Corner has been the island’s jazz club and restaurant since 1999. A fun late evening.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the island calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.hiltonheadisland.org/" target="_blank" rel="noopener">Browse Hilton Head events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: beach, bikes, Harbour Town and two Lowcountry dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KHXD, subject to weather and your actual flight plan, and ride to the resort.'),
        ('Afternoon', 'Bikes and the beach.'),
        ('Evening', 'Sunset dinner at Skull Creek Boathouse.')]) +
    day('SAT', 'Island day', [
        ('Morning', 'A round of golf, or a dolphin cruise.'),
        ('Afternoon', 'A spa treatment, or the Sea Pines Forest Preserve.'),
        ('Evening', 'Dinner at Charlie’s L’Etoile Verte.')]) +
    day('SUN', 'Harbour Town & home', [
        ('Morning', 'Climb the Harbour Town lighthouse and walk the harbor.'),
        ('Before leaving', 'Allow time at the FBO; summer afternoons bring storms.'),
        ('Fly home', 'A short hop home.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging first, then dinners, tee times and any spa time.'),
          ('Heritage week', 'The RBC Heritage in April fills the island. Check dates before booking.'),
          ('Runway & heat', 'KHXD’s runway is on the short side for some aircraft. Check performance, especially on hot days.'),
          ('Hurricane season', 'June through November. Watch the tropics and keep plans flexible.')]) +
    '</section>')

P.append(page_end(number=23, place='Hilton Head, South Carolina', reviewed=REVIEWED, note='Confirm hours, prices and availability directly with each place before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
