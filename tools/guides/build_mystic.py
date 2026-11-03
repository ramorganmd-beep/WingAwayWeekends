"""Generate docs/mystic/index.html (Mystic and Stonington, Connecticut)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='mystic', name='Mystic', state='Connecticut', number=38, reviewed='November 3, 2026',
    airport='KGON', nm=564, flight_time='~4 hr 1 <small>min</small>', style='Rental car + walks',
    place='Mystic, Connecticut',
    description='A curated two-night Mystic and Stonington getaway for GA pilots and their partners, from KMYR to KGON. A seaport museum of tall ships, a drawbridge town, oysters, lobster and the first nuclear submarine.',
    lede='Tall ships, a drawbridge and lobster by the water.',
    intro='Mystic was a 19th-century shipbuilding town, and its waterfront still feels like it. Explore tall ships at Mystic Seaport Museum, watch the drawbridge rise downtown, walk the quiet streets of Stonington Borough, and tour the world’s first nuclear-powered submarine a few minutes from the airport.',
    pills=['Seaport museum', 'Waterfront town', 'Seafood'],
    flight=dict(
        title='Land 10 minutes from Mystic.',
        intro='KGON, Groton–New London Airport, is a towered field on the water, about 10 minutes from downtown Mystic.',
        fbo=('Modern Aviation · Groton', '193 Tower Avenue, Groton, CT 06340', '860-715-8800'),
        notes=['Directories list hours of 5 a.m. to 9 p.m. daily; one source lists the address as 175 Tower Avenue, so confirm it. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Coastal fog and sea breezes are common, and the Navy submarine base lies just up the Thames River. Review the sectional and current NOTAMs, and plan a fuel stop for most piston aircraft.'],
        around_title='A car, then your feet.',
        around='Downtown Mystic is walkable, and the Seaport is a short walk up the river. A car helps for Stonington, Noank and the submarine museum.'),
    stay=dict(title='Downtown or on the river.', intro='Rates and availability need travel dates.',
        cards=[('Downtown · Boutique', 'Whaler’s Inn', 'A comfortable inn steps from the drawbridge, shops and restaurants.', 'https://whalersinnmystic.com/'),
               ('Riverfront · Romantic', 'Steamboat Inn', 'A small inn right on the Mystic River downtown, with fireplaces and whirlpool tubs in many rooms.', 'https://www.steamboatinnmystic.com/'),
               ('Hillside · Harbor views', 'Inn at Mystic', 'A hilltop inn and mansion with views over Pequotsepos Cove and the harbor.', 'https://www.innatmystic.com/')]),
    eat=dict(title='Two dinners. One lobster lunch.', intro='Reserve weekend dinners in summer.',
        cards=[('Friday dinner · Farm & sea', 'Oyster Club', 'Local oysters, seafood and farm cooking in downtown Mystic, with a treehouse deck in summer.', 'https://www.oysterclubct.com/'),
               ('Saturday dinner · Stonington', 'Stonington Borough', 'Choose one of the small restaurants on Water Street in the old fishing village, about 10 minutes east. Book ahead.'),
               ('Lunch · Noank', 'Ford’s Lobster', 'A casual waterfront spot in the fishing village of Noank, famous for its hot buttered lobster roll. Seasonal.', 'https://www.fordslobster.com/')]),
    explore=dict(title='Ships, submarines and old villages.', intro='One big outing a day, and time on the water.',
        items=[('Mystic Seaport Museum', 'A re-created 19th-century seafaring village with historic ships, including the Charles W. Morgan, the last wooden whaling ship. Allow half a day.', 'https://www.mysticseaport.org/', 'Museum information'),
               ('Submarine Force Museum & USS Nautilus', 'Go aboard the world’s first nuclear-powered submarine in Groton, minutes from the airport. Free.'),
               ('Mystic Aquarium', 'Beluga whales, seals and penguins, a short drive from downtown.', 'https://www.mysticaquarium.org/', 'Tickets'),
               ('Stonington Borough', 'A quiet 18th-century fishing village on a point, with antique shops and a lighthouse museum.'),
               ('The drawbridge & the river', 'Watch the 1922 bascule bridge rise downtown, then take a river cruise or a sail.')]),
    events=dict(url='https://gomystic.org/', button='Browse Mystic events',
        cards=[('May–October', 'Sailing season', 'River cruises, sails and the Seaport’s ships in full swing.'),
               ('Summer', 'Waterfront season', 'Busy, lively and warm. Book early.'),
               ('December', 'Holidays at the Seaport', 'Lantern-light tours and a festive downtown.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the Seaport, a submarine, a lobster roll and two coastal dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the submarine', [('Arrival', 'Land at KGON, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'USS Nautilus, then check in and watch the drawbridge.'), ('Evening', 'Dinner at Oyster Club.')]),
              ('SAT', 'The Seaport', [('Morning', 'Mystic Seaport Museum.'), ('Afternoon', 'A lobster roll at Ford’s in Noank, then a river cruise.'), ('Evening', 'Dinner in Stonington Borough.')]),
              ('SUN', 'An easy departure', [('Morning', 'Mystic Aquarium, or a walk around Stonington.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Morning fog is common on the coast; let weather set the departure.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('Fuel stop', 'Plan a fuel stop for most piston aircraft.'),
          ('Summer', 'July and August are busy; spring and fall are easier.'),
          ('Coastal weather', 'Fog and sea breezes are common. Keep a backup day.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
