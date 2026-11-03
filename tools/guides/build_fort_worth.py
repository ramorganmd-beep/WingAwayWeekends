"""Generate docs/fort-worth/index.html (Fort Worth and the Stockyards, Texas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='fort-worth', name='Fort Worth & the Stockyards', state='Texas', number=64, reviewed=None,
    airport='KFTW', nm=926, flight_time='~6 hr 26 <small>min</small>', style='Rideshare + walks',
    place='Fort Worth, Texas',
    description='A curated Fort Worth getaway for GA pilots and their partners, from KMYR to KFTW. A daily cattle drive in the Stockyards, a honky-tonk, steakhouses, world-class art museums and a vintage aircraft museum on the field.',
    lede='Cowtown: longhorns, steaks and great art.',
    intro='Fort Worth is where the West begins. Watch longhorns parade down Exchange Avenue in the Stockyards’ daily cattle drive, two-step at Billy Bob’s, eat a steak at a 1940s steakhouse, then spend a morning at the Kimbell and Amon Carter art museums. Pilots can start at the Vintage Flying Museum right on the airfield.',
    pills=['Stockyards', 'Steakhouses', 'Art museums'],
    flight=dict(
        title='Land five minutes from the Stockyards.',
        intro='KFTW, Fort Worth Meacham International, is a towered airport just north of downtown, about five minutes from the Stockyards.',
        fbo=('Texas Jet', '200 Texas Way, Fort Worth, TX 76106', '817-624-8438'),
        notes=['Texas Jet is open 24 hours. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Meacham sits under the Dallas–Fort Worth Class B airspace, among the busiest in the country. Brief your arrival carefully. About 930 nm from Myrtle Beach: plan a fuel stop and three nights. Review the sectional and current NOTAMs.'],
        around_title='Rideshare, then walk.',
        around='The Stockyards are walkable. The museums and downtown are a short ride away.'),
    stay=dict(title='In the Stockyards or downtown.', intro='Rates and availability need travel dates.',
        cards=[('Stockyards · Luxury', 'Hotel Drover', 'A ranch-style luxury hotel in the Stockyards, with a pool and 97 West Kitchen & Bar.', 'https://hoteldrover.com/'),
               ('Stockyards · Since 1907', 'Stockyards Hotel', 'A historic hotel on Exchange Avenue, in the middle of the action.', 'https://stockyardshotel.com/'),
               ('Explore more', 'Visit Fort Worth', 'More hotels downtown and in the Cultural District.', 'https://www.fortworth.com/')]),
    eat=dict(title='Steaks, Tex-Mex and a ranch kitchen.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Since 1947', 'Cattlemen’s Steak House', 'A classic Stockyards steakhouse, a Fort Worth institution.', 'https://www.cattlemenssteakhouse.com/'),
               ('Saturday dinner · Hotel Drover', '97 West Kitchen & Bar', 'Ranch-inspired cooking at Hotel Drover.', 'https://hoteldrover.com/dining/97-west-kitchen-and-bar/'),
               ('Lunch · Since 1935', 'Joe T. Garcia’s', 'Tex-Mex in a huge garden patio near the Stockyards. A Fort Worth tradition.', 'https://www.joetgarcias.com/')]),
    explore=dict(title='Cowboys, art and airplanes.', intro='One day in the Stockyards, one in the museums.',
        items=[('Fort Worth Stockyards', 'The daily longhorn cattle drive, rodeos on weekends and Western shops along Exchange Avenue.', 'https://www.fortworthstockyards.org/', 'Stockyards information'),
               ('Billy Bob’s Texas', 'The “world’s largest honky-tonk,” with live country music and dance lessons.', 'https://www.billybobstexas.com/', 'Shows'),
               ('Vintage Flying Museum', 'On Meacham Field, home of the B-17 Chuckie and other vintage aircraft.', 'https://vintageflyingmuseum.org/', 'Visit information'),
               ('Kimbell Art Museum', 'A world-class collection in a celebrated Louis Kahn building, in the Cultural District.'),
               ('Amon Carter Museum of American Art', 'Remington, Russell and American masters, with free admission.', 'https://www.cartermuseum.org/', 'Visit information')]),
    events=dict(url='https://www.fortworth.com/', button='Browse Fort Worth events',
        cards=[('January–February', 'Fort Worth Stock Show & Rodeo', 'A huge rodeo and livestock show. Book early.'),
               ('Weekends', 'Stockyards Championship Rodeo', 'Rodeo every Friday and Saturday night.'),
               ('Spring & fall', 'Best seasons', 'Mild weather; summers are hot.')]),
    itinerary=dict(intro='A sample long weekend: the Stockyards, a honky-tonk and the museums. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & airplanes', [('Arrival', 'Land at KFTW, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'The Vintage Flying Museum on the field, then check in.'), ('Evening', 'Dinner at Cattlemen’s.')]),
              ('DAY 2', 'The Stockyards', [('Morning', 'The cattle drive on Exchange Avenue.'), ('Afternoon', 'Lunch at Joe T. Garcia’s.'), ('Evening', 'Dinner at 97 West, then Billy Bob’s.')]),
              ('DAY 3', 'Art & home', [('Morning', 'The Kimbell and the Amon Carter.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'A long trip home. Start early and let weather set the plan.')])]),
    know=[('Book in this order', 'Lodging first, then dinners and show tickets.'),
          ('Class B airspace', 'Meacham is under DFW’s Class B. Brief your route carefully.'),
          ('Long flight', 'About 930 nm. Plan a fuel stop and extra nights.'),
          ('Weather', 'Spring brings severe storms; summer is hot.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
