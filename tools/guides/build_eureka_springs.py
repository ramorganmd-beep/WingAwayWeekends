"""Generate docs/eureka-springs/index.html (Eureka Springs, Arkansas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='eureka-springs', name='Eureka Springs', state='Arkansas', number=54, reviewed='November 3, 2026',
    airport='4M1', nm=740, flight_time='~5 hr 11 <small>min</small>', style='Rental car + walks',
    place='Eureka Springs, Arkansas',
    description='A curated two-night Eureka Springs getaway for GA pilots and their partners, from KMYR to 4M1. A Victorian spa town built into Ozark hillsides, a famous 1886 hotel, Thorncrown Chapel and a wildlife refuge.',
    lede='A Victorian town carved into the Ozark hills.',
    intro='Eureka Springs is a Victorian spa town whose winding streets climb steep Ozark hillsides, with no two streets crossing at right angles. Stay at a grand 1886 hotel on the mountaintop, walk the historic loop of shops and springs, sit in the soaring glass Thorncrown Chapel in the woods, and ride a vintage train.',
    pills=['Victorian town', 'Historic hotels', 'Ozark woods'],
    flight=dict(
        title='Land 20 minutes from town.',
        intro='4M1, Carroll County Airport, is a small airport west of Berryville, about 20 minutes from Eureka Springs.',
        fbo=('Carroll County Airport', '518 County Road 308, Berryville, AR 72616', '870-423-8393'),
        notes=['A small field with self-serve 100LL. Call ahead about hours, parking and a rental car or ride into town. No live fuel price is shown.',
               'Ozark hills and ridges surround the field. About 740 nm from Myrtle Beach: plan a fuel stop and consider a third night. Review the sectional and current NOTAMs.'],
        around_title='A car, then the trolley.',
        around='Downtown’s steep streets are best on foot or by the town trolley. Park once and walk.'),
    stay=dict(title='A grand hotel on the hill or right downtown.', intro='Rates and availability need travel dates.',
        cards=[('Mountaintop · 1886', 'Crescent Hotel & Spa', 'A grand 1886 hotel on the hill above town, with a spa, a rooftop SkyBar and famous ghost tours.', 'https://crescent-hotel.com/'),
               ('Downtown · 1905', 'Basin Park Hotel', 'A historic hotel on Basin Spring Park in the middle of downtown.', 'https://basinpark.com/'),
               ('Explore more', 'Eureka Springs visitor guide', 'Dozens of B&Bs and cottages in the hills.', 'https://www.visiteurekasprings.com/')]),
    eat=dict(title='Two dinners. One café breakfast.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Crescent Hotel', 'Crystal Dining Room', 'Dinner in the Crescent’s grand dining room, then a rooftop drink at the SkyBar.', 'https://crescent-hotel.com/eat-drink/crystal-dining-room/'),
               ('Saturday dinner · Wine cave', 'Grotto Wood-Fired Grill & Wine Cave', 'Steaks and wood-fired dishes in a stone grotto downtown, a special-occasion favorite.', 'https://www.grottoeureka.com/'),
               ('Breakfast or lunch · Downtown', 'Mud Street Café', 'A cozy café below street level on Main Street.', 'https://www.mudstreetcafe.com/')]),
    explore=dict(title='Hills, springs and a glass chapel.', intro='Wear good walking shoes.',
        items=[('Thorncrown Chapel', 'A soaring wood-and-glass chapel in the forest, designed by E. Fay Jones.', 'https://www.thorncrown.com/', 'Visit information'),
               ('The historic loop', 'Victorian buildings, shops, galleries and springs along the winding streets.'),
               ('Eureka Springs & North Arkansas Railway', 'A vintage train ride through the hills. Seasonal.', 'https://www.esnarailway.com/', 'Train schedule'),
               ('Turpentine Creek Wildlife Refuge', 'A sanctuary for rescued big cats.', 'https://www.turpentinecreek.org/', 'Visit information'),
               ('Beaver Lake', 'Clear water and bluffs a short drive west.')]),
    spa=dict(title='The New Moon Spa at the Crescent', body='The Crescent Hotel’s spa offers couples treatments on the mountaintop.'),
    events=dict(url='https://www.visiteurekasprings.com/', button='Browse Eureka Springs events',
        cards=[('Spring & fall', 'Festival seasons', 'Music, arts and folk festivals fill the town.'),
               ('October', 'Fall color', 'The Ozark hills turn gold and red.'),
               ('November–December', 'Holiday lights', 'A festive Victorian Christmas.')]),
    itinerary=dict(intro='A sample weekend: the Victorian town, a glass chapel and two good dinners. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the Crescent', [('Arrival', 'Land at 4M1, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in and walk the historic loop.'), ('Evening', 'Dinner at the Crystal Dining Room.')]),
              ('SAT', 'Hills & woods', [('Morning', 'Thorncrown Chapel.'), ('Afternoon', 'The vintage train, or the spa.'), ('Evening', 'Dinner at the Grotto.')]),
              ('SUN', 'An easy departure', [('Morning', 'Breakfast at Mud Street Café.'), ('Before leaving', 'Drive back to the airport and check fuel.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners and the spa.'),
          ('Small airport', 'Self-serve fuel and limited services. Call ahead.'),
          ('Long flight', 'About 740 nm. Plan a fuel stop and consider a third night.'),
          ('Steep streets', 'Downtown is hilly; the trolley helps.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
