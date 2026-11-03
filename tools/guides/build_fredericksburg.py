"""Generate docs/fredericksburg/index.html (Fredericksburg and the Texas Hill Country)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='fredericksburg', name='Fredericksburg & the Hill Country', state='Texas', number=62, reviewed=None,
    airport='KT82', nm=1037, flight_time='~7 hr 10 <small>min</small>', style='Rental car + walks',
    place='Fredericksburg, Texas',
    description='A curated Fredericksburg and Texas Hill Country getaway for GA pilots and their partners, from KMYR to T82. A WWII-themed hotel on the airport, the National Museum of the Pacific War, Hill Country wineries and Enchanted Rock.',
    lede='A hangar hotel, German Main Street and Hill Country wine.',
    intro='Fredericksburg was settled by German immigrants in 1846, and its Main Street still mixes biergartens with boutiques and tasting rooms. Stay at a 1940s-style hotel right on the airport, spend a morning at the National Museum of the Pacific War, taste along Wine Road 290, and watch the sunset from the granite dome of Enchanted Rock.',
    pills=['Hangar hotel', 'Pacific War museum', 'Hill Country wine'],
    flight=dict(
        title='Taxi to your hotel.',
        intro='T82, Gillespie County Airport, is about two miles south of downtown, with the Hangar Hotel and its diner right on the field.',
        fbo=('Fredericksburg FBO', '217 Airport Road, Fredericksburg, TX 78624', '830-997-3313'),
        notes=['Listed hours are 8 a.m. to 6 p.m. daily, with after-hours service for a fee by arrangement. Ask about rental cars, parking and fees. No live fuel price is shown.',
               'This is a long trip, about 1,040 nm from Myrtle Beach: plan one or two fuel stops and three or four nights. Summer heat raises density altitude; spring brings storms. Review the sectional and current NOTAMs.'],
        around_title='A car for the Hill Country.',
        around='Main Street is walkable. Use a car, or a winery shuttle, for Wine Road 290 and Enchanted Rock.'),
    stay=dict(title='On the airport or on Main Street.', intro='Rates and availability need travel dates.',
        cards=[('On the airport · WWII-themed', 'Hangar Hotel', 'A 1940s-style hotel built like an aircraft hangar, on the field, with the Airport Diner and the Officers’ Club. Adults only (18 and up).', 'https://hangarhotel.com/'),
               ('Main Street · Boutique', 'Albert Hotel', 'A stylish boutique hotel near Main Street with a pool, restaurant and bar.', 'https://alberthotel.com/'),
               ('Downtown · Classic', 'Inn on Barons Creek', 'A comfortable hotel and spa a short walk from Main Street.', 'https://www.innonbaronscreek.com/')]),
    eat=dict(title='German, Texan and a diner by the runway.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · German-inspired', 'Otto’s German Bistro', 'Modern German cooking in a restored house near Main Street.', 'https://www.ottosfbg.com/'),
               ('Saturday dinner · Texas', 'Cabernet Grill', 'Texas cooking with one of the largest all-Texas wine lists anywhere.', 'https://www.cabernetgrill.com/'),
               ('Breakfast or lunch · On the field', 'Hangar Hotel Airport Diner', 'A 1940s-style diner at the Hangar Hotel, steps from the ramp.', 'https://hangarhotel.com/')]),
    explore=dict(title='History, wine and granite.', intro='Allow half a day for the museum.',
        items=[('National Museum of the Pacific War', 'A large museum of the war in the Pacific in Admiral Nimitz’s hometown, with aircraft, a combat zone and a Japanese garden.', 'https://www.pacificwarmuseum.org/', 'Museum information'),
               ('Wine Road 290', 'Dozens of wineries between Fredericksburg and Johnson City. Taste on the non-flying day, with a driver or shuttle.'),
               ('Enchanted Rock State Natural Area', 'A huge pink granite dome to climb, about 25 minutes north. Reserve day passes ahead.', 'https://tpwd.texas.gov/state-parks/enchanted-rock', 'Park information'),
               ('LBJ Ranch', 'President Johnson’s “Texas White House,” with a driving tour.', 'https://www.nps.gov/lyjo/', 'Park information'),
               ('Wildseed Farms', 'Fields of wildflowers in spring and a market.', 'https://wildseedfarms.com/', 'Visit information')]),
    events=dict(url='https://www.visitfredericksburgtx.com/', button='Browse Fredericksburg events',
        cards=[('March–April', 'Wildflower season', 'Bluebonnets along the roads.'),
               ('October', 'Oktoberfest', 'German food, music and beer. Book early.'),
               ('November–December', 'Holidays on Main Street', 'Lights and a festive town.')]),
    itinerary=dict(intro='A sample long weekend: the hangar hotel, the Pacific War museum, wine and a granite summit. Plan three or four nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & Main Street', [('Arrival', 'Land at T82, subject to weather, your fuel stops and your actual flight plan; check in at the Hangar Hotel.'), ('Afternoon', 'Walk Main Street.'), ('Evening', 'Dinner at Otto’s.')]),
              ('DAY 2', 'History & wine', [('Morning', 'The National Museum of the Pacific War.'), ('Afternoon', 'Wine Road 290 with a driver.'), ('Evening', 'Dinner at Cabernet Grill.')]),
              ('DAY 3', 'Enchanted Rock & home', [('Sunrise', 'Climb Enchanted Rock.'), ('Before leaving', 'Breakfast at the Airport Diner.'), ('Fly home', 'A long trip home. Start early and let weather set the plan.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners and Enchanted Rock passes.'),
          ('Long flight', 'About 1,040 nm. Plan fuel stops and extra nights.'),
          ('Bottle to throttle', 'Taste on the non-flying day; 8 hours minimum by rule.'),
          ('Hangar Hotel', 'Adults only (18 and up).')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
