"""Generate docs/lancaster/index.html (Lancaster & Amish Country, Pennsylvania)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='lancaster', name='Lancaster & Amish Country', state='Pennsylvania', number=36, reviewed='November 3, 2026',
    airport='KLNS', nm=407, flight_time='~2 hr 58 <small>min</small>', style='Rental car',
    place='Lancaster & Amish Country, Pennsylvania',
    description='A curated two-night Lancaster County getaway for GA pilots and their partners, from KMYR to KLNS. Amish farmland, a steam railroad, the oldest farmers market in America and farm-to-table dinners.',
    lede='Farmland, a steam train and the oldest market in America.',
    intro='Lancaster County is a patchwork of Amish farms, covered bridges and small towns, with a lively historic city at its center. Shop America’s oldest farmers market, ride a steam train through the fields, drive the back roads past horse-drawn buggies and finish with dinner in a converted factory.',
    pills=['Amish countryside', 'Steam railroad', 'Farm-to-table'],
    flight=dict(
        title='Land between Lancaster and Lititz.',
        intro='KLNS, Lancaster Airport, is a towered field just north of the city, about 15 minutes from downtown Lancaster and 10 from Lititz.',
        fbo=('Alliance Aviation', '500 Airport Road, Suite G, Lititz, PA 17543', '717-735-9507'),
        notes=['Directories list hours of about 7 a.m. to 9 p.m. daily. Ask about rental cars, two-night parking and fees. No live fuel price is shown.',
               'Harrisburg’s airspace lies to the west. Review the sectional, current NOTAMs and TFRs.'],
        around_title='You’ll want a car.',
        around='The farms, the railroad and the small towns are spread across the county. Drive slowly and give horse-drawn buggies plenty of room.'),
    stay=dict(title='City, small town or a factory loft.', intro='Rates and availability need travel dates.',
        cards=[('Lancaster city · Art hotel', 'Lancaster Arts Hotel', 'A boutique hotel in a restored 1880s tobacco warehouse, filled with local art, with John J. Jeffries restaurant downstairs.', 'https://www.lancasterartshotel.com/'),
               ('Lititz · Boutique', 'Hotel Rock Lititz', 'A modern boutique hotel in Lititz, one of America’s prettiest small towns, a short walk from Main Street.', 'https://www.hotelrock.com/'),
               ('Lancaster city · Loft', 'Cork Factory Hotel', 'Loft-style rooms in a restored 1865 cork factory, with exposed brick and timber.', 'https://www.corkfactoryhotel.com/')]),
    eat=dict(title='Two dinners. One market lunch.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Italian', 'LUCA', 'Wood-fired Italian cooking in a lively room in Lancaster city.', 'https://lucalancaster.com/'),
               ('Saturday dinner · Farm-to-table', 'John J. Jeffries', 'Seasonal cooking from Lancaster County farms at the Lancaster Arts Hotel.', 'https://johnjjeffries.com/'),
               ('Lunch · Since 1730', 'Lancaster Central Market', 'America’s oldest continuously operating farmers market, with Amish baked goods, local cheese and lunch stands. Open Tuesday, Friday and Saturday mornings.', 'https://centralmarketlancaster.com/')]),
    explore=dict(title='Farms, trains and small towns.', intro='Take the back roads, and leave time for the farm stands.',
        items=[('Strasburg Rail Road', 'America’s oldest operating short-line railroad, with steam trains through Amish farmland. Ride in a first-class or dining car.', 'https://strasburgrailroad.com/', 'Train schedule'),
               ('Railroad Museum of Pennsylvania', 'Across the road, a huge hall of historic locomotives and cars.', 'https://www.rrmuseumpa.org/', 'Museum information'),
               ('Amish Farm and House', 'A guided tour of a working farm and house, and a respectful introduction to Amish life.', 'https://amishfarmandhouse.com/', 'Tour information'),
               ('Lititz', 'A pretty Moravian town with shops, a park and the Julius Sturgis Pretzel Bakery, the first commercial pretzel bakery in America.', 'https://juliussturgis.com/', 'Pretzel bakery'),
               ('A back-roads drive', 'Covered bridges, farm stands and quilt shops around Bird-in-Hand, Intercourse and Strasburg. Many shops close on Sundays.')]),
    events=dict(url='https://www.discoverlancaster.com/', button='Browse Lancaster events',
        cards=[('Spring', 'Mud sales', 'Amish auctions of quilts, crafts and more, held by volunteer fire companies from February to June.'),
               ('June–October', 'Farm season', 'Farm stands, festivals and corn mazes.'),
               ('December', 'Holiday trains', 'Strasburg Rail Road’s holiday rides. Book early.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the market, the railroad, the back roads and two good dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the market', [('Arrival', 'Land at KLNS, subject to weather and your actual flight plan, and pick up the car.'), ('Late morning', 'Lunch at Central Market (open Fridays), then check in.'), ('Evening', 'Dinner at LUCA.')]),
              ('SAT', 'Trains & farms', [('Morning', 'Strasburg Rail Road and the Railroad Museum.'), ('Afternoon', 'The Amish Farm and House and a back-roads drive.'), ('Evening', 'Dinner at John J. Jeffries.')]),
              ('SUN', 'Lititz & home', [('Morning', 'Twist a pretzel at Julius Sturgis and walk Main Street in Lititz.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'A car and lodging first, then dinners and train tickets.'),
          ('Market days', 'Central Market is open Tuesday, Friday and Saturday mornings only.'),
          ('Sundays', 'Many Amish-run shops and farm stands close on Sundays.'),
          ('Respect', 'Ask before photographing Amish people; many prefer not to be photographed.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
