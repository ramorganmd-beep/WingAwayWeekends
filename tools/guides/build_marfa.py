"""Generate docs/marfa/index.html (Marfa and Big Bend, Texas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='marfa', name='Marfa & Big Bend', state='Texas', number=67, reviewed=None,
    airport='KMRF', nm=1289, flight_time='~8 hr 51 <small>min</small>', style='Rental car',
    place='Marfa, Texas',
    description='A curated Marfa and Big Bend getaway for GA pilots and their partners, from KMYR to KMRF. A high-desert art town, Donald Judd’s Chinati Foundation, the Marfa Lights, McDonald Observatory star parties and Big Bend.',
    lede='High-desert art, dark skies and the Marfa Lights.',
    intro='Marfa is a tiny ranching town in the high desert of West Texas that became a world-famous art destination after the artist Donald Judd moved here in the 1970s. See his work at the Chinati Foundation, watch for the mysterious Marfa Lights, join a star party at McDonald Observatory under some of the darkest skies in the country, and drive to the canyons of Big Bend.',
    pills=['Art town', 'Dark skies', 'Big Bend'],
    flight=dict(
        title='Land in the high desert.',
        intro='KMRF, Marfa Municipal, is a few minutes north of town, at about 4,850 feet.',
        fbo=('Marfa Municipal Airport (Presidio County)', '45101 State Highway 17, Marfa, TX 79843', '432-295-0979'),
        notes=['Self-serve 100LL and Jet A are listed around the clock; confirm the FBO phone (sources differ), hours and a rental car ahead, since rentals are scarce. No live fuel price is shown.',
               'High elevation and summer heat make density altitude a serious factor; check performance. Winds can be strong, and the area is remote. This is the longest trip on the site, about 1,290 nm: plan two fuel stops and four or more nights.'],
        around_title='You’ll need a car.',
        around='Marfa is walkable, but Fort Davis, the observatory and Big Bend are an hour or more away.'),
    stay=dict(title='A modern hotel, a desert motel or a ranch.', intro='Rates and availability need travel dates. Hotel Paisano is closed for renovation until 2027.',
        cards=[('Downtown · Modern', 'Hotel Saint George', 'A stylish downtown hotel with a bookstore, pool and restaurant.', 'https://www.marfasaintgeorge.com/'),
               ('Highway 90 · Retro motel', 'Thunderbird Marfa', 'A restored 1959 motor court with minimalist rooms and a pool.', 'https://www.thunderbirdmarfa.com/'),
               ('Shafter · Ranch resort', 'Cibolo Creek Ranch', 'A secluded historic ranch resort about 40 minutes south. A splurge.', 'https://cibolocreekranch.com/')]),
    eat=dict(title='Small town, big flavors.', intro='Hours are limited and change with the seasons; check before you go.',
        cards=[('Friday dinner · Seasonal', 'Cochineal', 'A celebrated restaurant with a garden patio.', 'https://www.cochinealmarfa.com/'),
               ('Saturday dinner · Pizza & wine', 'Stellina', 'Wood-fired cooking and natural wines downtown.', 'https://stellinamarfa.com/'),
               ('Lunch · Hotel', 'Hotel Saint George', 'The hotel’s restaurant and bar for an easy lunch.', 'https://www.marfasaintgeorge.com/')]),
    explore=dict(title='Art, stars and desert canyons.', intro='Allow one day for art and one for Big Bend.',
        items=[('Chinati Foundation', 'Donald Judd’s vast installations in a former army fort. Book tours ahead.', 'https://www.chinati.org/', 'Tours'),
               ('The Marfa Lights viewing area', 'Watch for the unexplained lights east of town after dark.'),
               ('McDonald Observatory', 'Star parties and telescopes in the Davis Mountains, about 45 minutes away.', 'https://mcdonaldobservatory.org/', 'Star parties'),
               ('Big Bend National Park', 'Desert, mountains and Rio Grande canyons, about two hours south.', 'https://www.nps.gov/bibe/', 'Park information'),
               ('Prada Marfa', 'The famous roadside art installation near Valentine, about 35 minutes west.')]),
    events=dict(url='https://visitmarfa.com/', button='Browse Marfa events',
        cards=[('October', 'Chinati Weekend', 'The art foundation’s open house weekend. Busy; book early.'),
               ('Spring & fall', 'Best seasons', 'Mild days and cool nights.'),
               ('Year-round', 'Dark skies', 'Some of the darkest night skies in the country.')]),
    itinerary=dict(intro='A sample long weekend: art, stars and a day in Big Bend. Plan four or more nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the lights', [('Arrival', 'Land at KMRF, subject to weather, density altitude, your fuel stops and your actual flight plan.'), ('Evening', 'Dinner at Cochineal, then the Marfa Lights viewing area.'), ('Night', 'Look up.')]),
              ('DAY 2', 'Art & stars', [('Morning', 'A Chinati Foundation tour.'), ('Afternoon', 'Prada Marfa and Fort Davis.'), ('Evening', 'A star party at McDonald Observatory.')]),
              ('DAY 3', 'Big Bend', [('All day', 'Drive to Big Bend National Park for canyon views and short hikes.'), ('Evening', 'Dinner at Stellina.'), ('Next day', 'A long trip home. Start early and let weather set the plan.')])]),
    know=[('Book in this order', 'Lodging and a car first, then Chinati and observatory tickets.'),
          ('Density altitude', 'About 4,850 feet and hot in summer. Check performance.'),
          ('Very long flight', 'About 1,290 nm. Plan fuel stops and extra nights.'),
          ('Remote', 'Services are far apart. Carry water and fill up when you can.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
