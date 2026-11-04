"""Generate docs/fairhope/index.html (Fairhope & Mobile Bay, Alabama)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='fairhope', name='Fairhope & Mobile Bay', state='Alabama', number=74, reviewed='November 4, 2026',
    airport='KCQF', nm=494, flight_time='~3 hr 32 <small>min</small>', style='Rental or courtesy car',
    place='Fairhope, Alabama',
    description='A curated Fairhope getaway for GA pilots and their partners, from KMYR to KCQF. A flower-filled bayside town on Mobile Bay: the Grand Hotel at Point Clear, the pier at sunset, Bellingrath Gardens and the USS Alabama.',
    lede='A flower-filled town on the bluffs of Mobile Bay.',
    intro='Fairhope sits on a bluff above Mobile Bay, with flower baskets on every corner, a walkable downtown and a long municipal pier made for sunsets. Stay at the Grand Hotel at Point Clear, a bayfront resort since 1847, wander downtown shops and galleries, see Bellingrath Gardens and tour the battleship USS Alabama and its aircraft pavilion.',
    pills=['Bayside town', 'Grand resort & spa', 'Gardens & sunsets'],
    flight=dict(
        title='Land on the Eastern Shore.',
        intro='KCQF, H.L. “Sonny” Callahan Airport, is a non-towered field on the east side of Fairhope, about 10 minutes from downtown.',
        fbo=('Flightline First Fairhope', 'H.L. “Sonny” Callahan Airport, Fairhope, AL', '251-572-4626'),
        notes=['Confirm FBO hours, overnight fees and courtesy-car or rental options. No live fuel price is shown.',
               'Summer brings afternoon storms, and hurricane season runs June to November. About 495 nm from Myrtle Beach: a long nonstop leg or a fuel stop.'],
        around_title='A car for the bay.',
        around='Downtown Fairhope is walkable; a car covers Point Clear, Bellingrath and the battleship.'),
    stay=dict(title='A grand resort or a downtown inn.', intro='Rates and availability need travel dates.',
        cards=[('Point Clear · Resort & spa', 'The Grand Hotel Golf Resort & Spa', 'A bayfront resort since 1847, with golf, a spa and sunset views.', 'https://www.grand1847.com/'),
               ('Downtown · Boutique', 'The Fairhope Hotel', 'A small hotel steps from shops and restaurants.', 'https://www.fairhopehotel1925.com/'),
               ('Downtown · Inn', 'The Fairhope Inn', 'A bed-and-breakfast with its own restaurant.', 'https://www.thefairhopeinn.com/')]),
    eat=dict(title='Gulf seafood, Southern style.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Cottage', 'The Wash House', 'Seafood and steaks in a cozy old cottage near Point Clear.', 'https://www.washhouserestaurant.com/'),
               ('Saturday dinner · Bistro', 'Camellia Café', 'A refined downtown bistro.', 'https://www.camelliacafe.com/'),
               ('Lunch · Local favorite', 'Panini Pete’s', 'Sandwiches and beignets in the French Quarter shops.', 'https://www.paninipetes.com/')]),
    explore=dict(title='Gardens, a battleship and the bay.', intro='Slow mornings downtown, one big outing a day.',
        items=[('Fairhope Municipal Pier', 'A quarter-mile pier with a rose garden at its foot. Go at sunset.', 'https://alabama.travel/places-to-go/fairhope-municipal-pier/', 'Pier'),
               ('Downtown & the French Quarter', 'Galleries, bookstores and boutiques under the flower baskets.', 'https://www.visitdowntownfairhope.com/', 'Downtown Fairhope'),
               ('Bellingrath Gardens and Home', 'Sixty-five acres of gardens on the Fowl River.', 'https://www.bellingrath.org/', 'Gardens'),
               ('USS Alabama Battleship Memorial Park', 'A WWII battleship, a submarine and an aircraft pavilion.', 'https://www.ussalabama.com/', 'Battleship')]),
    spa=dict(title='The spa at The Grand', body='The Grand Hotel’s spa offers couples treatments with views of Mobile Bay.'),
    events=dict(url='https://www.gulfcoastalabama.com/', button='Browse Gulf Coast events',
        cards=[('March', 'Fairhope Arts & Crafts Festival', 'One of the South’s largest outdoor art shows.', 'https://www.fairhopeartsandcraftsfestival.com/', 'Festival'),
               ('Late winter', 'Mardi Gras in Mobile', 'America’s oldest Mardi Gras, across the bay.', 'https://www.mobile.org/', 'Mobile'),
               ('Spring & fall', 'Best seasons', 'Warm, with fewer storms than summer.')]),
    itinerary=dict(intro='A sample weekend: the pier, gardens and a battleship. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & downtown', [('Arrival', 'Land at KCQF, subject to weather and your actual flight plan.'), ('Afternoon', 'Walk downtown and the pier.'), ('Evening', 'Dinner at Camellia Café.')]),
              ('DAY 2', 'Gardens & the spa', [('Morning', 'Bellingrath Gardens.'), ('Afternoon', 'The spa at The Grand.'), ('Evening', 'Dinner at The Wash House.')]),
              ('DAY 3', 'Battleship & home', [('Morning', 'The USS Alabama and aircraft pavilion.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then the spa and dinners.'),
          ('Sunsets', 'The pier faces west over the bay.'),
          ('Long leg', 'About 495 nm. Check range and reserves, or plan a fuel stop.'),
          ('Hurricane season', 'June through November. Keep plans flexible.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
