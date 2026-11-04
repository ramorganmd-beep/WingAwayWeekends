"""Generate docs/bay-st-louis/index.html (Bay St. Louis, Mississippi)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='bay-st-louis', name='Bay St. Louis', state='Mississippi', number=71, reviewed=None,
    airport='KHSA', nm=571, flight_time='~4 hr 03 <small>min</small>', style='Rental car',
    place='Bay St. Louis, Mississippi',
    description='A curated Bay St. Louis getaway for GA pilots and their partners, from KMYR to KHSA. A small, artsy Gulf Coast town: Old Town galleries, beachfront dining, NASA’s INFINITY Science Center and Walter Anderson’s art.',
    lede='An artsy little town on the Mississippi Gulf Coast.',
    intro='Bay St. Louis calls itself “a place apart”: a small town on the Gulf with galleries, porches and seafood restaurants along Beach Boulevard. Walk Old Town on Second Saturday, eat oysters looking over the bay, visit the INFINITY Science Center beside NASA’s rocket-engine test site and drive to Ocean Springs for Walter Anderson’s art.',
    pills=['Gulf Coast town', 'Art & galleries', 'Seafood'],
    flight=dict(
        title='Land at Stennis.',
        intro='KHSA, Stennis International Airport, is a towered field with a long runway, about 15 minutes north of Old Town Bay St. Louis.',
        fbo=('Million Air Stennis', 'Stennis International Airport, Bay St. Louis, MS', '228-463-2389'),
        notes=['Confirm FBO hours, ramp fees and rental-car or courtesy-car options. No live fuel price is shown.',
               'Expect military and training traffic. Summer brings afternoon storms, and hurricane season runs June to November. About 570 nm from Myrtle Beach: plan a fuel stop or a long nonstop leg.'],
        around_title='Bring a car.',
        around='Old Town is walkable; a car covers the airport, INFINITY and Ocean Springs.'),
    stay=dict(title='A small inn or a resort on the coast.', intro='Rates and availability need travel dates.',
        cards=[('Old Town · Inn', 'The Bay Town Inn', 'A small inn across from the beach in Old Town.', 'https://baytowninn.com/'),
               ('Bay St. Louis · Resort', 'Hollywood Casino Gulf Coast', 'A resort on the bay with a golf course and pools.', 'https://www.hollywoodgulfcoast.com/'),
               ('Biloxi · Luxury', 'Beau Rivage', 'A large resort with a spa, about 45 minutes east.', 'https://beaurivage.mgmresorts.com/')]),
    eat=dict(title='Seafood on Beach Boulevard.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · On the bay', '200 North Beach', 'Seafood, steaks and cocktails with views of the bay.', 'https://200northbeach.com/'),
               ('Saturday dinner · Steaks & oysters', 'Field’s Steak & Oyster Bar', 'A local favorite for steaks, oysters and Gulf fish.', 'https://fieldssteaks.com/'),
               ('Lunch · On the beach', 'Lemoine’s Landing', 'A casual beach restaurant for a long lunch.', 'https://lemoineslandingbsl.com/')]),
    explore=dict(title='Galleries, space and the Gulf.', intro='An easy, low-key weekend.',
        items=[('Old Town Bay St. Louis', 'Galleries, antique shops and cafés; the Second Saturday art walk is the liveliest night.'),
               ('INFINITY Science Center', 'A space and earth science museum and the visitor center for NASA’s Stennis Space Center.', 'https://www.visitinfinity.com/', 'INFINITY'),
               ('The beach & the bay bridge', 'Walk or bike the beachfront and the bridge to Pass Christian.'),
               ('Walter Anderson Museum of Art', 'Vivid work by the Gulf Coast artist, in Ocean Springs.', 'https://www.walterandersonmuseum.org/', 'Museum')]),
    events=dict(url='https://coastalmississippi.com/', button='Browse Gulf Coast events',
        cards=[('Monthly', 'Second Saturday', 'An art walk with open galleries and music in Old Town.'),
               ('Late winter', 'Mardi Gras', 'Parades along the Mississippi Gulf Coast.'),
               ('Spring & fall', 'Best seasons', 'Warm, with fewer storms than summer.')]),
    itinerary=dict(intro='A sample weekend: art, seafood and space. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & Old Town', [('Arrival', 'Land at KHSA, subject to weather and your actual flight plan.'), ('Afternoon', 'Walk Old Town and the beach.'), ('Evening', 'Dinner at 200 North Beach.')]),
              ('DAY 2', 'Space & art', [('Morning', 'INFINITY Science Center, near the airport.'), ('Afternoon', 'Drive to Ocean Springs for the Walter Anderson Museum.'), ('Evening', 'Dinner at Field’s.')]),
              ('DAY 3', 'Beach & home', [('Morning', 'Lunch at Lemoine’s Landing.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then dinners.'),
          ('Second Saturday', 'Plan around it for the liveliest Old Town evening.'),
          ('Long flight', 'About 570 nm. Plan a fuel stop or a long nonstop leg.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
