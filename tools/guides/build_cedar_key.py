"""Generate docs/cedar-key/index.html (Cedar Key, Florida)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='cedar-key', name='Cedar Key', state='Florida', number=60, reviewed=None,
    airport='KCDK', nm=345, flight_time='~2 hr 34 <small>min</small>', style='Golf cart + walks',
    place='Cedar Key, Florida',
    description='A curated two-night Cedar Key getaway for GA pilots and their partners, from KMYR to KCDK. A tiny Old Florida island town on the Gulf: a short runway by the water, golf carts, clams, kayaking and sunsets.',
    lede='Old Florida, a short runway by the water and a golf cart.',
    intro='Cedar Key is a tiny island town on the Gulf coast, with weathered wooden buildings on stilts, working clam farms and some of the best sunsets in Florida. Land on a short runway at the water’s edge, ride a golf cart into town, kayak to a deserted island, eat award-winning clam chowder and watch the sun drop into the Gulf from Dock Street.',
    pills=['Old Florida', 'Golf carts', 'Clams & sunsets'],
    flight=dict(
        title='Land at the water’s edge.',
        intro='KCDK, George T. Lewis Airport, is a small county airport on the island, a short golf-cart ride from town.',
        fbo=('George T. Lewis Airport (no FBO or fuel)', '14703 SW Airport Road, Cedar Key, FL 32625'),
        notes=['There is no fuel or FBO. Arrange a golf-cart rental ahead; pilots report carts can meet you at the airport. Tie-downs are available; confirm fees with Levy County.',
               'The single runway is about 2,300 feet, with water close by. Check landing and takeoff performance carefully, especially on hot days, and arrive with plenty of fuel. Watch for birds, gusty sea breezes and afternoon storms in summer.'],
        around_title='Golf carts and your feet.',
        around='The town is tiny. Rent a golf cart or bikes, or simply walk.'),
    stay=dict(title='Harbor views and historic rooms.', intro='Rates and availability need travel dates.',
        cards=[('Harbor · Suites', 'Cedar Key Harbour Master Suites', 'Suites with balconies over the harbor in the middle of town.', 'https://www.cedarkeyharbourmaster.com/'),
               ('Downtown · Historic', 'The Downtown Historic Island Hotel', 'Rooms in an 1859 building on Second Street, now rented as suites. Confirm current arrangements when you book.'),
               ('Explore more', 'Visit Cedar Key', 'Cottages, condos and small inns around the island.', 'https://www.cedarkey.org/')]),
    eat=dict(title='Chowder, clams and a Gulf view.', intro='Hours change with the seasons and storm repairs; confirm before you go.',
        cards=[('Lunch · Award-winning chowder', 'Tony’s Seafood', 'Famous for its championship clam chowder, in a historic building on Second Street.', 'https://www.tonyschowder.com/'),
               ('Dinner · Local clams', 'Steamers Clam Bar & Grill', 'Steamed Cedar Key clams and oysters; after a 2024 fire it moved to Second Street. Confirm hours.', 'https://www.steamerscedarkey.com/'),
               ('Sunset · Dock Street', 'Dock Street at sunset', 'Several Dock Street restaurants were rebuilding after recent storms. Ask locally which waterfront decks are open, and go for the sunset.')]),
    explore=dict(title='Islands, birds and sunsets.', intro='Slow down. This is Old Florida.',
        items=[('Kayak to Atsena Otie Key', 'Paddle or take a boat to the ruins of an old town on a nearby island.'),
               ('Cedar Keys National Wildlife Refuge', 'Islands of pelicans, herons and ibis, by kayak or boat tour.', 'https://www.fws.gov/refuge/cedar-keys', 'Refuge information'),
               ('Cedar Key Museum State Park', 'The town’s history as a 19th-century port, rail terminus and pencil-wood center.'),
               ('Dock Street & the sunset', 'Shops, galleries and the classic Gulf sunset.'),
               ('Shell Mound', 'A walk on an ancient Native American shell mound north of town.')]),
    events=dict(url='https://www.cedarkey.org/', button='Browse Cedar Key events',
        cards=[('April', 'Spring Arts Festival', 'Artists fill the town.'),
               ('October', 'Seafood Festival', 'The island’s big fall festival. Busy; book early.'),
               ('Winter', 'Birding season', 'Migrating birds and cool, clear days.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: a golf cart, a kayak and two Gulf sunsets. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Dock Street', [('Arrival', 'Land at KCDK with fuel to spare, subject to weather and your actual flight plan; pick up the golf cart.'), ('Afternoon', 'Check in and explore Dock Street.'), ('Evening', 'Sunset on Dock Street, then dinner at Steamers.')]),
              ('SAT', 'Islands & clams', [('Morning', 'Kayak to Atsena Otie Key or a refuge boat tour.'), ('Afternoon', 'Chowder at Tony’s and the museum.'), ('Evening', 'Another sunset and Cedar Key clams.')]),
              ('SUN', 'An easy departure', [('Morning', 'The Shell Mound trail.'), ('Before leaving', 'Check density altitude for the short runway.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging and a golf cart first.'),
          ('Short runway, no fuel', 'About 2,300 feet and no fuel. Check performance and plan fuel elsewhere.'),
          ('Storm repairs', 'Some restaurants are rebuilding after recent storms. Confirm hours.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
