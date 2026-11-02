"""Generate docs/amelia-island/index.html."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['amelia-island']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'), ('spa', 'Spa'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='amelia-island', name='Amelia Island', state='Florida', number=12,
    description='A curated two-night Amelia Island getaway for GA pilots and their partners, from KMYR to KFHB. Historic Fernandina Beach, quiet beaches, resort spas and Fort Clinch.',
    lede='Land in town. Walk to dinner.',
    intro='Fernandina Beach’s Victorian seaport is minutes from the runway: brick storefronts on Centre Street, shrimp boats at sunset, and wide, quiet beaches lined with dunes. Add a resort spa and it is an easy romantic weekend.',
    pills=['Historic seaport', 'Beaches', 'Resort spas'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KFHB', nm=225, flight_time='~1 hr 45 <small>min</small>',
    style='Crew car + walks', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land, then roll into town.',
    'KFHB, Fernandina Beach Municipal, is a non-towered field just south of downtown, a few minutes from Centre Street.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Bent Wing Flight Services', '680 Airport Road, Fernandina Beach, FL 32034', '904-849-4321') +
    '<p class="note">Bent Wing lists full-service and self-serve 100LL, Jet A and a crew car. Pilots report a small crew-car fee that may be waived with fuel; ask about the current policy, facility fees and two-night parking. No live fuel price is shown.</p>'
    '<p class="note">Rental cars generally come from Jacksonville International (JAX); confirm delivery in advance rather than counting on it. Jacksonville’s airspace lies to the south; review the sectional.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>Short hops, then on foot.</h3><p>Downtown is a few minutes from the airport. Use the crew car or a taxi, then walk the historic district.</p><p>The resorts are 15–20 minutes south on the island; arrange a ride or rental if you stay there.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your kind of weekend.',
    'A grand oceanfront resort, a big resort with everything, or a beach inn near town. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Oceanfront · Splurge', 'The Ritz-Carlton, Amelia Island',
         'A polished oceanfront resort with a spa, golf and its seafood restaurant, Coast. The most indulgent choice.') +
    card('Resort · Spa & golf', 'Omni Amelia Island Resort & Spa',
         'A large oceanfront resort with a spa, golf and more than ten restaurants. Easy if you want everything on site.',
         'https://www.omnihotels.com/hotels/amelia-island') +
    card('Beach inn · Near town', 'Elizabeth Pointe Lodge',
         'A shingle-style inn right on the beach, a short ride from downtown. Quiet and romantic. Confirm room type and dining.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One long lunch.',
    'Downtown Fernandina has excellent small restaurants. Reserve weekend dinners.') +
    '<div class="grid three">' +
    card('Friday dinner · Fine dining', 'David’s Restaurant & Lounge',
         'Often called the island’s finest dining, at 802 Ash Street downtown, with a cocktail lounge that sometimes has live music.') +
    card('Saturday dinner · Tapas', 'España Restaurant & Tapas',
         'Spanish and Portuguese dishes at 22 South 4th Street, a short walk from Centre Street. Reservations suggested on weekends.') +
    card('Alternative · Highly rated', 'Burlingame',
         'A small, much-praised restaurant at 20 South 5th Street. Swap it in for either night.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Seaport, fort and beach.',
    'Easy, low-key pleasures. Choose one outing a day and leave room for the beach.') +
    '<div class="explore-list">' +
    explore(1, 'Centre Street & the historic district',
            'Victorian storefronts, galleries and shops running down to the harbor. Have a drink at the Palace Saloon, said to be Florida’s oldest continuously operating bar.') +
    explore(2, 'Fort Clinch State Park',
            'A 19th-century brick fort at the north end of the island, with beaches, trails and live oaks.') +
    explore(3, 'Horseback riding on the beach',
            'Guided beach rides are a memorable couples outing. Book ahead and check age, weight and season rules.') +
    explore(4, 'Sunset on the Amelia River',
            'Watch the shrimp boats come in from the downtown harbor, or take a sunset river cruise.') +
    '</div>')

P.append('<div id="spa" class="couples"><span class="eyebrow">Optional / Spa & relaxation</span><h3>A resort spa · Time for two</h3>'
    '<p>The Ritz-Carlton and Omni resorts both have full-service spas, a short drive from downtown.</p>'
    '<p><strong>Booking:</strong> Ask about couples treatments, access for non-resort guests, current pricing and cancellation policy. No prices are shown here, and no appointment has been booked.</p></div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the destination calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('March', 'Amelia Island Concours d’Elegance',
         'One of the country’s best-known classic-car shows. Spectacular, and the island fills up; book far ahead.') +
    card('Spring', 'Isle of Eight Flags Shrimp Festival',
         'Fernandina’s big downtown festival celebrating its shrimping history. Fun and crowded.') +
    card('Spring & fall', 'Best seasons',
         'Mild weather and quieter beaches. Summer is hot and humid, with afternoon storms; hurricane season runs June–November.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the destination calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.ameliaisland.com/" target="_blank" rel="noopener">Browse Amelia Island events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: the seaport, a beach day and two downtown dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KFHB, subject to weather and your actual flight plan, and head downtown.'),
        ('Afternoon', 'Lunch and a slow walk up Centre Street; a drink at the Palace Saloon.'),
        ('Evening', 'Sunset at the harbor, then dinner at David’s.')]) +
    day('SAT', 'Fort & beach', [
        ('Morning', 'Fort Clinch State Park, or a horseback ride on the beach.'),
        ('Afternoon', 'Beach time, or a couples spa treatment at one of the resorts.'),
        ('Evening', 'Dinner at España.')]) +
    day('SUN', 'An easy departure', [
        ('Morning', 'Breakfast and a last walk through the historic district.'),
        ('Before leaving', 'Return the crew car and allow time at the FBO.'),
        ('Fly home', 'Plan around afternoon storms in warm months.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Lodging and ground transport first, then dinners and any spa time.'),
          ('Big weekends', 'The Concours in March and the Shrimp Festival fill the island. Check dates before booking.'),
          ('Allow for the season', 'Summer storms build in the afternoon; hurricane season runs June–November.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=12, place='Amelia Island, Florida', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
