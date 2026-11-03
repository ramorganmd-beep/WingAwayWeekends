"""Generate docs/naples/index.html (Naples, Florida)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='naples', name='Naples', state='Florida', number=56, reviewed='November 3, 2026',
    airport='KAPF', nm=476, flight_time='~3 hr 26 <small>min</small>', style='Rental car + walks',
    place='Naples, Florida',
    description='A curated two-night Naples getaway for GA pilots and their partners, from KMYR to KAPF. Gulf beaches, sunset at the pier, Fifth Avenue dining, botanical gardens and a wild swamp sanctuary.',
    lede='Gulf sunsets, a historic pier and Fifth Avenue.',
    intro='Naples is a polished Gulf Coast town of white-sand beaches, palm-lined streets and spectacular sunsets. Watch the sun set from the 1888 Naples Pier, stroll Fifth Avenue South and Third Street for dinner, wander the Naples Botanical Garden, and walk the boardwalk through an ancient cypress swamp.',
    pills=['Gulf beaches', 'Sunsets', 'Dining'],
    flight=dict(
        title='Land five minutes from downtown.',
        intro='KAPF, Naples Municipal, is a towered airport a few minutes from Fifth Avenue South and the beaches.',
        fbo=('Naples Aviation', '160 Aviation Drive North, Naples, FL 34104', '239-643-0404'),
        notes=['Listed hours are 6 a.m. to 10 p.m. daily. Naples Jet Center is also on the field. Naples has noise-abatement procedures; review them before you go. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Fort Myers’ Class C airspace lies to the north. Summer brings afternoon storms; hurricane season runs June to November. Review the sectional and current NOTAMs.'],
        around_title='A car, then walk.',
        around='Downtown, the pier and Fifth Avenue are close together; a car helps for the garden and the swamp.'),
    stay=dict(title='On the Gulf or downtown.', intro='Rates and availability need travel dates; winter is peak season.',
        cards=[('Vanderbilt Beach · Luxury', 'The Ritz-Carlton, Naples', 'A grand beachfront resort with a spa, pools and Gulf sunsets.', 'https://www.ritzcarlton.com/en/hotels/naples/naples-beach'),
               ('Vanderbilt Beach · Boutique resort', 'LaPlaya Beach & Golf Resort', 'A stylish beachfront resort with a spa and a golf course nearby.', 'https://www.laplayaresort.com/'),
               ('Downtown · Fifth Avenue', 'Inn on Fifth', 'A Mediterranean-style hotel right on Fifth Avenue South, with a rooftop pool and spa.', 'https://www.innonfifth.com/')]),
    eat=dict(title='Two dinners. One by the bay.', intro='Reserve dinners, especially in winter.',
        cards=[('Friday dinner · Fifth Avenue', 'Sea Salt', 'Inventive seafood and a long wine list on Fifth Avenue South.', 'https://aielligroup.com/sea-salt-naples/home'),
               ('Saturday dinner · Creative', 'USS Nemo', 'A long-running local favorite for creative seafood.', 'https://ussnemorestaurant.com/'),
               ('Lunch · Waterfront', 'The Dock at Crayton Cove', 'Casual seafood on Naples Bay.', 'https://www.dockcraytoncove.com/')]),
    explore=dict(title='Beaches, gardens and wild Florida.', intro='Mix the beach with one outing a day.',
        items=[('Naples Pier at sunset', 'A 1,000-foot pier from 1888, rebuilt after storms, and the classic Naples sunset spot.'),
               ('Fifth Avenue South & Third Street South', 'Shops, galleries and restaurants in the heart of old Naples.'),
               ('Naples Botanical Garden', 'Tropical gardens from around the world, with orchids and water gardens.', 'https://www.naplesgarden.org/', 'Garden information'),
               ('Corkscrew Swamp Sanctuary', 'A 2.25-mile boardwalk through the largest old-growth bald cypress forest in North America, about 40 minutes inland.', 'https://www.audubon.org/corkscrew', 'Sanctuary information'),
               ('A boat on the Gulf', 'Dolphin, shelling and sunset cruises leave from Naples Bay.')]),
    spa=dict(title='A beachfront spa', body='The Ritz-Carlton and LaPlaya both have spas with couples treatments by the Gulf.'),
    events=dict(url='https://www.paradisecoast.com/', button='Browse Naples events',
        cards=[('December–April', 'High season', 'Warm, dry and busy. Book early.'),
               ('Spring', 'Garden season', 'Blooms at the botanical garden and pleasant beach weather.'),
               ('Summer & fall', 'Quiet season', 'Lower rates, afternoon storms and hurricane season.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the beach, the pier at sunset and two good dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the pier', [('Arrival', 'Land at KAPF, subject to weather and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk to the beach.'), ('Evening', 'Sunset at the pier, then dinner at Sea Salt.')]),
              ('SAT', 'Gardens & the Gulf', [('Morning', 'Naples Botanical Garden.'), ('Afternoon', 'Lunch at The Dock, then the beach or the spa.'), ('Evening', 'Dinner at USS Nemo.')]),
              ('SUN', 'An easy departure', [('Morning', 'Corkscrew Swamp, or a shelling cruise.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('Noise abatement', 'Naples has published noise procedures. Review them.'),
          ('Season', 'Winter is busiest; summer is hot with afternoon storms.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
