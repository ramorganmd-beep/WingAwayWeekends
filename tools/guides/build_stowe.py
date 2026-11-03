"""Generate docs/stowe/index.html (Stowe, Vermont)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='stowe', name='Stowe', state='Vermont', number=33, reviewed='November 3, 2026',
    airport='KMVL', nm=714, flight_time='~5 hr 1 <small>min</small>', style='Car needed',
    place='Stowe, Vermont',
    description='A curated two-night Stowe getaway for GA pilots and their partners, from KMYR to KMVL. A New England village below Mount Mansfield, mountain resorts, fall color, cider and craft beer.',
    lede='A white steeple, a big mountain and the best fall color.',
    intro='Stowe is the classic New England village: a white church steeple below Mount Mansfield, Vermont’s highest peak. Fly into the valley, drive up the mountain, walk or bike the riverside path, stop for cider donuts and craft beer, and end the day by the fire at a mountain resort.',
    pills=['Mountain village', 'Fall color', 'Resorts & spas'],
    flight=dict(
        title='Land 15 minutes from the village.',
        intro='KMVL, Morrisville–Stowe State Airport, is a small state-owned field about 15 minutes north of Stowe village.',
        fbo=('Morrisville–Stowe State Airport (no full-service FBO listed)', '2305 Laporte Road, Morrisville, VT 05661'),
        notes=['Directories list no full-service FBO here, so confirm fuel, parking and ground transport before you go, and arrange a rental car or taxi from Stowe ahead. For full services, Heritage Aviation at Burlington (KBTV, 228 Aviation Avenue, South Burlington) is about 45 minutes from Stowe.',
               'Mountain flying: Mount Mansfield and the Green Mountains rise just south and west of the field. Expect valley fog and gusty winds, and winter weather from November to April. This is about 700 nm from Myrtle Beach; plan a fuel stop.'],
        around_title='You’ll need a car.',
        around='The village, the mountain resorts and the Mountain Road restaurants are spread along a few miles. The Stowe Recreation Path is perfect on foot or by bike.'),
    stay=dict(title='Mountain resort or village inn.', intro='Rates and availability need travel dates.',
        cards=[('Mountain Road · Resort & spa', 'Topnotch Resort', 'A polished resort below Mount Mansfield with one of New England’s best-known spas and a fire-pit terrace.', 'https://www.topnotchresort.com/'),
               ('Spruce Peak · Ski-in, ski-out', 'The Lodge at Spruce Peak', 'A luxury lodge at the base of the mountain, with a spa and the Spruce Peak village.', 'https://www.sprucepeak.com/'),
               ('Hillside · Austrian-inspired', 'Trapp Family Lodge', 'The von Trapp family’s mountain resort, with sweeping views, trails, a bierhall and a brewery.', 'https://www.vontrappresort.com/')]),
    eat=dict(title='Two dinners. One long lunch.', intro='Farm-to-table cooking and great beer. Reserve on fall and ski weekends.',
        cards=[('Friday dinner · Village', 'Plate', 'Seasonal, farm-driven cooking in a cozy room in Stowe village.', 'https://www.platestowe.com/'),
               ('Saturday dinner · Waterbury', 'Hen of the Wood', 'Vermont’s celebrated farm-to-table restaurant, about 20 minutes away in Waterbury. Book ahead.', 'https://www.henofthewood.com/'),
               ('Lunch · Trapp Family Lodge', 'von Trapp Bierhall', 'Austrian-style lunch and lagers brewed on site, with mountain views.', 'https://www.vontrappresort.com/')]),
    explore=dict(title='Mountains, trails and treats.', intro='One outing a day, and time for the village.',
        items=[('Mount Mansfield', 'Ride the gondola or drive the Auto Toll Road for views across Vermont to Lake Champlain and the Adirondacks. Seasonal.'),
               ('The Stowe Recreation Path', 'A 5.3-mile paved path along the river from the village, with covered bridges and mountain views.'),
               ('Smugglers’ Notch', 'A narrow mountain pass with towering cliffs and boulders, open to cars in summer and fall.'),
               ('Cider, cheese and ice cream', 'Cold Hollow Cider Mill’s cider donuts, the Ben & Jerry’s factory in Waterbury and local cheesemakers.'),
               ('Moss Glen Falls', 'A short walk to a pretty waterfall a few minutes from the village.')]),
    spa=dict(title='The spa at Topnotch', body='Topnotch’s spa offers couples treatments, indoor and outdoor pools and quiet lounges with mountain views.'),
    events=dict(url='https://gostowe.com/', button='Browse Stowe events',
        cards=[('Late September–early October', 'Fall color', 'Some of the best foliage in New England. Spectacular and very busy; book months ahead.'),
               ('December–April', 'Ski season', 'Stowe Mountain Resort’s ski season. Winter flying needs careful planning.'),
               ('Summer', 'Mountain summer', 'Hiking, music and cool evenings.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the mountain, the path and two Vermont dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the village', [('Arrival', 'Land at KMVL, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk the village.'), ('Evening', 'Dinner at Plate.')]),
              ('SAT', 'Up the mountain', [('Morning', 'The gondola or Toll Road up Mount Mansfield.'), ('Afternoon', 'Lunch at the von Trapp Bierhall, then the spa or Smugglers’ Notch.'), ('Evening', 'Dinner at Hen of the Wood.')]),
              ('SUN', 'An easy departure', [('Morning', 'Bike or walk the Recreation Path, with cider donuts.'), ('Before leaving', 'Return the car and check fuel and weather.'), ('Fly home', 'Valley fog often lifts by mid-morning.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('No FBO', 'Confirm fuel and ground transport at KMVL, or use Burlington for full services.'),
          ('Mountain weather', 'Ridges, fog and early winter. Keep a backup day.'),
          ('Foliage season', 'Late September and early October fill months ahead.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
