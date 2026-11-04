"""Generate docs/san-antonio/index.html (San Antonio, Texas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='san-antonio', name='San Antonio', state='Texas', number=63, reviewed='November 4, 2026',
    airport='KSSF', nm=1032, flight_time='~7 hr 8 <small>min</small>', style='Rideshare + River Walk',
    place='San Antonio, Texas',
    description='A curated San Antonio getaway for GA pilots and their partners, from KMYR to KSSF. The Alamo, the River Walk, four Spanish missions next to the airport, the Pearl and Tex-Mex at Market Square.',
    lede='Missions, the River Walk and a hotel in an old brewery.',
    intro='San Antonio is one of America’s oldest cities, founded around a chain of 18th-century Spanish missions. Land at Stinson, one of the oldest general aviation airports in the country, a few minutes from the missions. Walk the River Walk, visit the Alamo, stay in a 19th-century brewhouse at the Pearl and finish with Tex-Mex at Market Square.',
    pills=['Spanish missions', 'River Walk', 'The Pearl'],
    flight=dict(
        title='Land at a historic airfield near the missions.',
        intro='KSSF, Stinson Municipal, dates to 1915 and sits on the south side of the city, about 15 minutes from downtown and minutes from Mission San José.',
        fbo=('GateOne Stinson (Imperial Aviation)', '8535 Mission Road, Suite 108, San Antonio, TX 78214', '210-922-1203'),
        notes=['Listed hours are about 7:30 a.m. to 6 p.m. weekdays and 8 a.m. to 5 p.m. weekends. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'San Antonio International’s Class C airspace and nearby military bases are busy. About 1,030 nm from Myrtle Beach: plan one or two fuel stops and three or four nights. Review the sectional and current NOTAMs.'],
        around_title='Rideshare, then walk.',
        around='Downtown, the River Walk and the Pearl are linked by the river path. A car helps for the missions.'),
    stay=dict(title='A brewhouse, a grande dame or a riverside hideaway.', intro='Rates and availability need travel dates.',
        cards=[('The Pearl · Luxury', 'Hotel Emma', 'A celebrated hotel in an 1894 brewhouse at the Pearl, on the River Walk’s quieter northern stretch.', 'https://thehotelemma.com/'),
               ('Downtown · Historic', 'The St. Anthony', 'A grand 1909 hotel downtown, now a Luxury Collection hotel, with a rooftop pool.', 'https://www.marriott.com/en-us/hotels/satlc-the-st-anthony-a-luxury-collection-hotel-san-antonio/overview/'),
               ('River Walk · Boutique', 'Hotel Havana', 'A small 1914 hotel on the River Walk with a moody bar.', 'https://www.bunkhousehotels.com/hotel-havana/')]),
    eat=dict(title='Two dinners. One Tex-Mex institution.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · The Pearl', 'Supper', 'Seasonal American cooking at Hotel Emma.', 'https://www.supperatemma.com/'),
               ('Saturday dinner · River Walk', 'Boudro’s Texas Bistro', 'A River Walk favorite known for tableside guacamole and Texas dishes.', 'https://www.boudros.com/'),
               ('Anytime · Market Square', 'Mi Tierra Café y Panadería', 'A festive Tex-Mex institution since 1941, with a bakery and mariachis.', 'https://lafamiliacortez.com/mi-tierra/')]),
    explore=dict(title='Missions, the river and the Alamo.', intro='Start early before the heat.',
        items=[('San Antonio Missions National Historical Park', 'Four 18th-century Spanish missions, including Mission San José, a few minutes from Stinson. A World Heritage Site.', 'https://www.nps.gov/saan/', 'Park information'),
               ('The Alamo', 'The 1718 mission and 1836 battle site in the heart of downtown. Reserve a timed entry.', 'https://www.thealamo.org/', 'Tickets'),
               ('The River Walk', 'Fifteen miles of paths along the river. Take a river barge tour.'),
               ('The Pearl', 'A former brewery turned into restaurants, shops and a weekend farmers market.', 'https://atpearl.com/', 'The Pearl'),
               ('Market Square', 'A lively Mexican market downtown.')]),
    events=dict(url='https://www.visitsanantonio.com/', button='Browse San Antonio events',
        cards=[('April', 'Fiesta San Antonio', 'The city’s huge spring festival. Book early.'),
               ('November–December', 'River Walk holiday lights', 'Thousands of lights over the river.'),
               ('Spring & fall', 'Best seasons', 'Pleasant weather; summers are very hot.')]),
    itinerary=dict(intro='A sample long weekend: the missions, the Alamo and the River Walk. Plan three or four nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the missions', [('Arrival', 'Land at KSSF, subject to weather, your fuel stops and your actual flight plan.'), ('Afternoon', 'Mission San José, minutes from the airport.'), ('Evening', 'Check in and dinner at Supper.')]),
              ('DAY 2', 'Downtown', [('Morning', 'The Alamo, then a river barge tour.'), ('Afternoon', 'Market Square and lunch at Mi Tierra.'), ('Evening', 'Dinner at Boudro’s.')]),
              ('DAY 3', 'The Pearl & home', [('Morning', 'The Pearl’s farmers market on weekends.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'A long trip home. Start early and let weather set the plan.')])]),
    know=[('Book in this order', 'Lodging first, then Alamo entry and dinners.'),
          ('Long flight', 'About 1,030 nm. Plan fuel stops and extra nights.'),
          ('Heat', 'Summers are very hot; plan outdoor time early.'),
          ('Airspace', 'Brief San Antonio’s Class C and military areas.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
