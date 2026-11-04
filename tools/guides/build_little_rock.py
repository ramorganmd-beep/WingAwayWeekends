"""Generate docs/little-rock/index.html (Little Rock, Arkansas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='little-rock', name='Little Rock', state='Arkansas', number=82, reviewed=None,
    airport='KLIT', nm=663, flight_time='~4 hr 40 <small>min</small>', style='Rental car or rideshare',
    place='Little Rock, Arkansas',
    description='A curated Little Rock getaway for GA pilots and their partners, from KMYR to KLIT. A river city with Central High School’s civil rights history, the Clinton Presidential Center, the Big Dam Bridge, Pinnacle Mountain and a good restaurant scene.',
    lede='A river city of history, bridges and trails.',
    intro='Little Rock is an easy, friendly capital on the Arkansas River. Tour Central High School, where nine Black students integrated the school in 1957, visit the Clinton Presidential Center, bike the Arkansas River Trail over the Big Dam Bridge, climb Pinnacle Mountain for the view and stay at the elegant 1870s Capital Hotel.',
    pills=['Civil rights history', 'River trails', 'Historic hotel'],
    flight=dict(
        title='Land at Clinton National.',
        intro='KLIT, Bill and Hillary Clinton National Airport, is a towered airport about 10 minutes from downtown and the River Market.',
        fbo=('Atlantic Aviation', 'Clinton National Airport, Little Rock, AR', '501-376-7777'),
        notes=['Signature Aviation (501-374-6582) is a second FBO. Confirm hours, fees and rental cars. No live fuel price is shown.',
               'Summer brings afternoon storms. About 665 nm from Myrtle Beach: plan a fuel stop and three nights.'],
        around_title='Rent a car.',
        around='Downtown and the River Market are walkable; a car or bikes cover the trail, the bridge and Pinnacle Mountain.'),
    stay=dict(title='A grand old hotel or a boutique stay.', intro='Rates and availability need travel dates.',
        cards=[('Downtown · Since 1870s', 'The Capital Hotel', 'An elegant historic hotel downtown, home of One Eleven restaurant.', 'https://www.capitalhotel.com/'),
               ('West Little Rock · Boutique', 'The Burgundy Hotel', 'A stylish boutique hotel.', 'https://www.theburgundyhotel.com/'),
               ('Local guide', 'More places to stay', 'Browse hotels near the River Market.', 'https://www.littlerock.com/', 'Little Rock CVB')]),
    eat=dict(title='Southern dining, river views.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Upscale', 'Petit & Keet', 'A lively spot for steaks, seafood and Southern dishes.', 'https://www.petitandkeet.com/'),
               ('Saturday dinner · On the river', 'Brave New Restaurant', 'A long-time favorite with river views.', 'https://www.bravenewrestaurant.com/'),
               ('Lunch · Farm to table', 'The Root Café', 'Local comfort food.', 'https://www.therootcafe.com/'),
               ('Dinner · Classic', 'Doe’s Eat Place', 'Steaks and tamales in a Little Rock institution.', 'https://www.doeseatplace.com/')]),
    explore=dict(title='History, bridges and a mountain.', intro='Mix a museum with time outdoors.',
        items=[('Little Rock Central High School NHS', 'The 1957 integration story, with ranger-led tours of the school.', 'https://www.nps.gov/chsc/', 'Historic site'),
               ('Clinton Presidential Center', 'A museum and library on the river, with a replica Oval Office.', 'https://www.clintonpresidentialcenter.org/', 'Clinton Center'),
               ('Arkansas River Trail & the Big Dam Bridge', 'A loop trail with one of the longest pedestrian bridges in the country.', 'https://arkansasrivertrail.org/', 'River Trail'),
               ('Pinnacle Mountain State Park', 'A short, steep climb to a summit view.', 'https://www.arkansasstateparks.com/parks/pinnacle-mountain-state-park', 'Park'),
               ('Arkansas Museum of Fine Arts', 'A striking new museum in MacArthur Park.', 'https://arkmfa.org/', 'Museum')]),
    events=dict(url='https://www.littlerock.com/', button='Browse Little Rock events',
        cards=[('Spring', 'Riverfest & spring events', 'Check the city calendar for festivals.', 'https://www.littlerock.com/', 'Little Rock CVB'),
               ('Saturdays', 'River Market farmers market', 'Seasonal market downtown.', 'https://www.rivermarket.info/', 'River Market'),
               ('Spring & fall', 'Best seasons', 'Mild weather for the trails.')]),
    itinerary=dict(intro='A sample long weekend: history, the river and a mountain. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & downtown', [('Arrival', 'Land at KLIT, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'The River Market and the Clinton Center.'), ('Evening', 'Dinner at Petit & Keet.')]),
              ('DAY 2', 'History & the river', [('Morning', 'Central High School with a ranger.'), ('Afternoon', 'Bike the River Trail and the Big Dam Bridge.'), ('Evening', 'Dinner at Brave New Restaurant.')]),
              ('DAY 3', 'The mountain & home', [('Morning', 'Climb Pinnacle Mountain.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then Central High tour times and dinners.'),
          ('Central High', 'It is a working school; tours are ranger-led and need reservations.'),
          ('Long flight', 'About 665 nm. Plan a fuel stop and extra nights.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
