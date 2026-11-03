"""Generate docs/lake-placid/index.html (Lake Placid, New York)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='lake-placid', name='Lake Placid', state='New York', number=42, reviewed=None,
    airport='KLKP', nm=676, flight_time='~4 hr 46 <small>min</small>', style='Walks + a car',
    place='Lake Placid, New York',
    description='A curated two-night Lake Placid getaway for GA pilots and their partners, from KMYR to KLKP. Two-time Olympic village, Adirondack lakes and peaks, lakeside resorts and spas, and mountain hikes.',
    lede='An Olympic village on a mountain lake.',
    intro='High in the Adirondacks, Lake Placid hosted the Winter Olympics twice, in 1932 and 1980. Land just outside the village, walk around Mirror Lake, see the Olympic ski jumps and the rink of the “Miracle on Ice,” drive to the top of Whiteface Mountain and warm up by the fire at a lakeside lodge.',
    pills=['Olympic history', 'Adirondack lakes', 'Lodges & spas'],
    flight=dict(
        title='Land a mile from the village.',
        intro='KLKP, Lake Placid Airport, is a small mountain field about a mile south of the village.',
        fbo=('Adirondack Flying Service', 'Lake Placid Airport, 27 Airport Lane, Lake Placid, NY 12946', '518-523-2473'),
        notes=['A small field with limited services. Call ahead about fuel, tie-downs, hours and a taxi or rental car. No live fuel price is shown.',
               'Mountain flying: high peaks surround the field, with turbulence, valley fog and fast-changing weather, and winter conditions from November to April. Check runway length and performance. About 680 nm from Myrtle Beach; plan a fuel stop.'],
        around_title='Walk the village.',
        around='Main Street, Mirror Lake and the Olympic Center are walkable. A car helps for Whiteface, the ski jumps and trailheads.'),
    stay=dict(title='Lakeside or in the woods.', intro='Rates and availability need travel dates.',
        cards=[('Mirror Lake · Resort & spa', 'Mirror Lake Inn', 'A polished lakeside resort with a spa, fine dining and fireplaces, a short walk from Main Street.', 'https://mirrorlakeinn.com/'),
               ('Adirondack lodge · Luxury', 'Whiteface Lodge', 'A grand Adirondack-style lodge of timber and stone, with a spa and suites with fireplaces.', 'https://www.thewhitefacelodge.com/'),
               ('Mirror Lake · Classic', 'Golden Arrow Lakeside Resort', 'A relaxed, family-run hotel on Mirror Lake with its own beach and canoes.', 'https://www.golden-arrow.com/')]),
    eat=dict(title='Two dinners. One brewpub lunch.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Casual', 'Lisa G’s', 'A lively local favorite at the edge of the village, by the Olympic ski jumps.', 'https://www.lisags.com/'),
               ('Saturday dinner · Lakeside', 'Mirror Lake Inn', 'Fine dining with views over Mirror Lake. Book ahead.', 'https://mirrorlakeinn.com/'),
               ('Lunch · Brewpub', 'Big Slide Brewery', 'Craft beer and wood-fired food a short walk from Main Street.', 'https://bigslidebrewery.com/')]),
    explore=dict(title='Olympics, lakes and peaks.', intro='Mix one big view with one short hike.',
        items=[('The Olympic Center', 'Walk onto the rink of the 1980 “Miracle on Ice” and visit the Lake Placid Olympic Museum.'),
               ('Olympic Jumping Complex', 'Ride the elevator to the top of the 1980 ski jumps for views over the High Peaks.'),
               ('Whiteface Veterans Memorial Highway', 'Drive to near the summit of Whiteface Mountain for a 360-degree view. Seasonal.'),
               ('Mirror Lake', 'An easy 2.7-mile walk around the lake from Main Street, or a canoe rental.'),
               ('High Falls Gorge', 'Waterfalls and walkways through a granite gorge, 15 minutes away.', 'https://highfallsgorge.com/', 'Visit information')]),
    spa=dict(title='A lakeside spa', body='Mirror Lake Inn and Whiteface Lodge both have spas with couples treatments and fireside lounges.'),
    events=dict(url='https://www.lakeplacid.com/', button='Browse Lake Placid events',
        cards=[('Late September–early October', 'Fall color', 'Spectacular Adirondack foliage. Book early.'),
               ('Summer', 'Lakes & hiking', 'Canoes, hikes and cool evenings.'),
               ('Winter', 'Olympic winter', 'Skating, skiing and bobsled rides; winter flying needs careful planning.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: Olympic sites, a mountaintop view and two good dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Mirror Lake', [('Arrival', 'Land at KLKP, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in and walk around Mirror Lake.'), ('Evening', 'Dinner at Lisa G’s.')]),
              ('SAT', 'Olympics & Whiteface', [('Morning', 'The Olympic Center and the ski jumps.'), ('Afternoon', 'Lunch at Big Slide, then the Whiteface highway or the spa.'), ('Evening', 'Dinner at Mirror Lake Inn.')]),
              ('SUN', 'An easy departure', [('Morning', 'High Falls Gorge, or a canoe on the lake.'), ('Before leaving', 'Check fuel and weather.'), ('Fly home', 'Mountain fog often lifts by mid-morning.')])]),
    know=[('Book in this order', 'Lodging first, then dinners and ground transport.'),
          ('Mountain airport', 'High terrain, fog and limited services. Call the FBO before you go.'),
          ('Fuel stop', 'Plan a fuel stop for most piston aircraft.'),
          ('Seasons', 'Whiteface highway and some attractions are seasonal.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
