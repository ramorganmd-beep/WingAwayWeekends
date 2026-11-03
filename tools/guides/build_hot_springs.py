"""Generate docs/hot-springs/index.html (Hot Springs, Arkansas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='hot-springs', name='Hot Springs', state='Arkansas', number=52, reviewed=None,
    airport='KHOT', nm=706, flight_time='~4 hr 58 <small>min</small>', style='Rental car + walks',
    place='Hot Springs, Arkansas',
    description='A curated two-night Hot Springs getaway for GA pilots and their partners, from KMYR to KHOT. A national park built around thermal springs, Bathhouse Row, a traditional bath, gardens and a brewery in a bathhouse.',
    lede='Thermal baths on Bathhouse Row.',
    intro='Hot Springs grew up around 47 natural hot springs in the Ouachita Mountains, and the grand bathhouses of the 1910s and ’20s now form the heart of a national park. Soak in thermal water at a historic bathhouse, walk Bathhouse Row, drink a beer brewed with spring water, and stroll the gardens on Lake Hamilton.',
    pills=['Thermal baths', 'National park', 'Historic downtown'],
    flight=dict(
        title='Land a few minutes from Bathhouse Row.',
        intro='KHOT, Memorial Field, is a city airport about 10 minutes from downtown Hot Springs.',
        fbo=('City of Hot Springs FBO · Memorial Field', '525 Airport Road, Hot Springs, AR 71913', '501-321-6750'),
        notes=['Ask about rental cars, parking, fees and hours. No live fuel price is shown.',
               'The Ouachita Mountains rise around the city. About 700 nm from Myrtle Beach: plan a fuel stop and consider a third night. Review the sectional and current NOTAMs.'],
        around_title='Walk Bathhouse Row.',
        around='Downtown and Bathhouse Row are walkable. A car helps for the gardens and Hot Springs Mountain.'),
    stay=dict(title='Historic grandeur or boutique suites.', intro='Rates and availability need travel dates.',
        cards=[('Bathhouse Row · Boutique', 'Hotel Hale', 'Suites in a restored 1892 bathhouse on Bathhouse Row, with thermal water piped to the tubs.', 'https://www.hotelhale.com/'),
               ('Downtown · Boutique', 'The Waters', 'A stylish boutique hotel in a restored 1913 building across from Bathhouse Row.', 'https://thewatershs.com/'),
               ('Downtown · Grand hotel', 'The Arlington Resort Hotel & Spa', 'A grand 1924 hotel at the head of Bathhouse Row, with thermal baths and a spa.', 'https://www.arlingtonhotel.com/')]),
    eat=dict(title='Two dinners. One brewery.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Latin', 'Rolando’s Nuevo Latino', 'A lively downtown favorite with Latin American dishes and a patio.', 'https://rolandosrestaurant.com/'),
               ('Saturday dinner · Downtown', 'Downtown Hot Springs', 'Choose from the restaurants along Central Avenue; ask your hotel for a reservation.'),
               ('Lunch · Brewery', 'Superior Bathhouse Brewery', 'The first brewery in a national park, in a 1916 bathhouse, using thermal spring water.', 'https://www.superiorbathhouse.com/')]),
    explore=dict(title='Baths, mountains and gardens.', intro='Slow down and soak.',
        items=[('Hot Springs National Park & Bathhouse Row', 'Eight historic bathhouses, a visitor center in the restored Fordyce Bathhouse and springs you can taste.', 'https://www.nps.gov/hosp/', 'Park information'),
               ('A traditional bath', 'Take a classic thermal bath at a historic bathhouse, or soak in the pools at Quapaw Baths & Spa.', 'https://quapawbaths.com/', 'Quapaw Baths'),
               ('Hot Springs Mountain Tower', 'A 216-foot tower with views over the Ouachitas.'),
               ('Garvan Woodland Gardens', 'Gardens and a striking wooden chapel on Lake Hamilton.', 'https://www.garvangardens.org/', 'Garden information'),
               ('The Ohio Club', 'The oldest bar in Arkansas, from 1905, with live music and gangster-era history.', 'https://www.theohioclub.com/', 'The Ohio Club')]),
    spa=dict(title='Thermal baths and spas', body='Soak in the springs at Quapaw Baths, the Arlington or a traditional bathhouse; couples soaks and massages are available.'),
    events=dict(url='https://www.hotsprings.org/', button='Browse Hot Springs events',
        cards=[('January–May', 'Racing season', 'Thoroughbred racing at Oaklawn.'),
               ('Spring', 'Gardens in bloom', 'Azaleas and tulips at Garvan Woodland Gardens.'),
               ('November–December', 'Holiday lights', 'Light displays at the gardens and downtown.')]),
    itinerary=dict(intro='A sample weekend: Bathhouse Row, a thermal soak and two good dinners. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Bathhouse Row', [('Arrival', 'Land at KHOT, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Walk Bathhouse Row and the Fordyce visitor center.'), ('Evening', 'Dinner at Rolando’s.')]),
              ('SAT', 'Soak & stroll', [('Morning', 'A traditional thermal bath.'), ('Afternoon', 'Lunch at Superior Bathhouse Brewery, then Garvan Woodland Gardens.'), ('Evening', 'Dinner downtown and a nightcap at The Ohio Club.')]),
              ('SUN', 'An easy departure', [('Morning', 'Hot Springs Mountain Tower.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging and a car first, then a bath and dinners.'),
          ('Long flight', 'About 700 nm. Plan a fuel stop and consider a third night.'),
          ('Bath reservations', 'Popular bath times fill on weekends; book ahead.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
