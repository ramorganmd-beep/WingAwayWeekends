"""Generate docs/branson/index.html (Branson and Table Rock Lake, Missouri)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='branson', name='Branson & Table Rock Lake', state='Missouri', number=50, reviewed=None,
    airport='KBBG', nm=721, flight_time='~5 hr 4 <small>min</small>', style='Rental car',
    place='Branson, Missouri',
    description='A curated two-night Branson and Table Rock Lake getaway for GA pilots and their partners, from KMYR to KBBG. A wilderness lodge on the lake, Top of the Rock, Dogwood Canyon, Silver Dollar City and live shows.',
    lede='Ozark lakes, a wilderness lodge and live shows.',
    intro='Branson sits in the Ozark Mountains on the shores of Table Rock Lake and Lake Taneycomo. Stay at a rustic-luxe wilderness lodge on the lake, watch the sunset from Top of the Rock, ride through the waterfalls of Dogwood Canyon, and catch one of the town’s famous live shows.',
    pills=['Ozark lakes', 'Wilderness lodge', 'Live shows'],
    flight=dict(
        title='Land at a privately owned airline airport.',
        intro='KBBG, Branson Airport, is a towered field south of town, about 20 minutes from Big Cedar Lodge and the Branson strip.',
        fbo=('Branson Jet Center', '130 Wright Brothers Drive, Hollister, MO 65672', '417-334-8234'),
        notes=['Ask about rental cars, parking and fees. No live fuel price is shown.',
               'Ozark hills surround the field. Springfield’s airspace lies to the north. About 720 nm from Myrtle Beach: plan a fuel stop and consider a third night. Review the sectional and current NOTAMs.'],
        around_title='You’ll want a car.',
        around='The lodge, the lakes and the shows are spread out; traffic on the main strip can be slow on weekends.'),
    stay=dict(title='A lake lodge or a castle on the hill.', intro='Rates and availability need travel dates.',
        cards=[('Table Rock Lake · Wilderness resort', 'Big Cedar Lodge', 'A rustic-luxe resort on Table Rock Lake with cabins, a spa, golf and Top of the Rock nearby. The reason to come.', 'https://bigcedar.com/'),
               ('Table Rock Lake · Resort', 'Chateau on the Lake', 'A grand hotel on a hill above the lake, with a spa and marina.', 'https://www.chateauonthelake.com/'),
               ('Explore more', 'Explore Branson', 'More hotels and lake rentals from the visitor bureau.', 'https://www.explorebranson.com/')]),
    eat=dict(title='Two dinners. One at sunset.', intro='Reserve ahead, especially at Top of the Rock.',
        cards=[('Friday dinner · Lodge', 'Big Cedar Lodge restaurants', 'Lakeside dining at the lodge, from casual to a special-occasion dinner.', 'https://bigcedar.com/'),
               ('Saturday dinner · Sunset', 'Top of the Rock', 'Dinner on a ridgetop above Table Rock Lake. Time it for sunset.', 'https://bigcedar.com/top-of-the-rock/'),
               ('Lunch · Downtown', 'Branson Landing', 'Shops and restaurants along Lake Taneycomo, with a fountain show.')]),
    explore=dict(title='Lakes, caves and the Ozarks.', intro='Mix the outdoors with one show.',
        items=[('Top of the Rock', 'A ridgetop park with a golf course, a nature trail, Lost Canyon Cave and a waterfall bar.', 'https://bigcedar.com/top-of-the-rock/', 'Visit information'),
               ('Dogwood Canyon Nature Park', 'A 10,000-acre private canyon with waterfalls, bison and elk, by tram, bike or on foot.', 'https://dogwoodcanyon.org/', 'Tours'),
               ('Silver Dollar City', 'An 1880s-themed park with crafts, music and roller coasters. Festive at Christmas.', 'https://www.silverdollarcity.com/', 'Tickets'),
               ('A live show', 'Branson is known for music and variety shows; choose one that suits you.'),
               ('Table Rock Lake', 'Rent a pontoon boat, fish or kayak on the clear lake.')]),
    spa=dict(title='The spa at Big Cedar Lodge', body='Big Cedar’s spa offers couples treatments in a quiet wooded setting by the lake.'),
    events=dict(url='https://www.explorebranson.com/', button='Browse Branson events',
        cards=[('November–December', 'Ozark Mountain Christmas', 'Lights, holiday shows and Silver Dollar City’s Christmas festival.'),
               ('Spring', 'Dogwoods in bloom', 'Wildflowers and mild weather in the Ozarks.'),
               ('Summer', 'Lake season', 'Boats, swimming and busy weekends.')]),
    itinerary=dict(intro='A sample weekend: the lake, a sunset dinner and a canyon. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the lodge', [('Arrival', 'Land at KBBG, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in at the lake.'), ('Evening', 'Dinner at the lodge.')]),
              ('SAT', 'Canyon & sunset', [('Morning', 'Dogwood Canyon by tram or bike.'), ('Afternoon', 'The spa or a boat on Table Rock Lake.'), ('Evening', 'Sunset dinner at Top of the Rock.')]),
              ('SUN', 'An easy departure', [('Morning', 'Lost Canyon Cave or a lakeside walk.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners, show tickets and the spa.'),
          ('Long flight', 'About 720 nm. Plan a fuel stop and consider a third night.'),
          ('Traffic', 'The main strip can be slow; use back roads.'),
          ('Dates come next', 'Rates and show schedules are date-dependent. No availability or live price is implied here.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
