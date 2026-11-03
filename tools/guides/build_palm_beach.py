"""Generate docs/palm-beach/index.html (Palm Beach, Florida)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='palm-beach', name='Palm Beach', state='Florida', number=59, reviewed=None,
    airport='KLNA', nm=430, flight_time='~3 hr 7 <small>min</small>', style='Rental car + bikes',
    place='Palm Beach, Florida',
    description='A curated two-night Palm Beach getaway for GA pilots and their partners, from KMYR to KLNA. A legendary oceanfront resort, Worth Avenue, Henry Flagler’s mansion, the Lake Trail and elegant dinners.',
    lede='Gilded Florida: Worth Avenue, The Breakers and Flagler’s mansion.',
    intro='Palm Beach is Florida at its most glamorous: an island of grand hotels, Mediterranean mansions and hedge-lined streets. Stay at The Breakers, shop and stroll Worth Avenue’s courtyards, tour Henry Flagler’s Gilded Age mansion, and bike the Lake Trail along the Intracoastal at sunset.',
    pills=['Grand hotels', 'Worth Avenue', 'Gilded Age history'],
    flight=dict(
        title='Land at Lantana, 20 minutes south.',
        intro='KLNA, Palm Beach County Park Airport in Lantana, is a general aviation airport about 20 minutes from the island.',
        fbo=('Stellar Aviation of South Palm Beach', '2633 Lantana Road, Lantana, FL 33462', '561-656-9815'),
        notes=['Listed hours are about 8 a.m. to 6:30 p.m. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Presidential and VIP TFRs over Palm Beach are common and can close nearby airspace with little notice; check TFRs before every flight. Palm Beach International’s Class C airspace is just north. Summer brings afternoon storms.'],
        around_title='A car, then bikes.',
        around='Rent a car to reach the island; then bikes or walking for Worth Avenue and the Lake Trail.'),
    stay=dict(title='Grand or intimate.', intro='Rates and availability need travel dates; winter is peak season.',
        cards=[('Oceanfront · Since 1896', 'The Breakers', 'Palm Beach’s legendary Italian Renaissance–style resort on the ocean, with a spa and several restaurants.', 'https://www.thebreakers.com/'),
               ('Near Worth Avenue · Classic', 'The Colony', 'A pink, playful 1947 hotel a block from the beach and Worth Avenue.', 'https://thecolonypalmbeach.com/'),
               ('In-town · Boutique', 'The Brazilian Court', 'A quiet 1926 hotel of courtyards and fountains, home to Café Boulud.', 'https://www.thebraziliancourt.com/')]),
    eat=dict(title='Two dinners. One Palm Beach institution.', intro='Reserve dinners, especially in season.',
        cards=[('Friday dinner · French', 'Café Boulud', 'Daniel Boulud’s elegant restaurant at The Brazilian Court.', 'https://www.cafeboulud.com/palmbeach/'),
               ('Saturday dinner · Lively', 'Buccan', 'Inventive small plates in a buzzing room.', 'https://www.buccanpalmbeach.com/'),
               ('Lunch · Since 1941', 'Ta-boó', 'A Worth Avenue institution for lunch and people-watching.', 'https://www.taboorestaurant.com/')]),
    explore=dict(title='Mansions, shops and the Lake Trail.', intro='Bike or walk the island.',
        items=[('Flagler Museum', 'Whitehall, Henry Flagler’s 75-room 1902 mansion, and his private railcar.', 'https://flaglermuseum.org/', 'Museum information'),
               ('Worth Avenue', 'Four blocks of shops and hidden “vias,” or courtyards, in Mediterranean Revival style.'),
               ('The Lake Trail', 'A paved path along the Intracoastal past grand homes. Best by bike at sunset.'),
               ('Norton Museum of Art', 'A major art museum across the bridge in West Palm Beach.'),
               ('The beach', 'Quiet public beaches along the island’s ocean side.')]),
    spa=dict(title='The spa at The Breakers', body='The Breakers’ oceanfront spa offers couples treatments and pools by the sea.'),
    events=dict(url='https://www.thepalmbeaches.com/', button='Browse Palm Beach events',
        cards=[('December–April', 'The season', 'Galas, polo and warm, dry weather. Book early.'),
               ('Winter', 'Polo in Wellington', 'International polo about 30 minutes inland.'),
               ('Summer & fall', 'Quiet season', 'Lower rates, afternoon storms and hurricane season.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: Worth Avenue, Flagler’s mansion and two elegant dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the island', [('Arrival', 'Land at KLNA, subject to weather, TFRs and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk Worth Avenue.'), ('Evening', 'Dinner at Café Boulud.')]),
              ('SAT', 'Mansions & bikes', [('Morning', 'The Flagler Museum.'), ('Afternoon', 'Lunch at Ta-boó, then the spa or the beach.'), ('Evening', 'Bike the Lake Trail at sunset, then dinner at Buccan.')]),
              ('SUN', 'An easy departure', [('Morning', 'The Norton Museum or a beach walk.'), ('Before leaving', 'Check TFRs again and allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('TFRs', 'VIP TFRs are frequent here. Check before every flight.'),
          ('Season', 'Winter is busiest and priciest; summer is quiet.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
