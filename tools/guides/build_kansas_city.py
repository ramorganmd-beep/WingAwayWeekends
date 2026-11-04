"""Generate docs/kansas-city/index.html (Kansas City, Missouri)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='kansas-city', name='Kansas City', state='Missouri', number=84, reviewed='November 4, 2026',
    airport='KMKC', nm=823, flight_time='~5 hr 44 <small>min</small>', style='Rental car or streetcar',
    place='Kansas City, Missouri',
    description='A curated Kansas City getaway for GA pilots and their partners, from KMYR to KMKC. Barbecue, jazz at 18th & Vine, the Nelson-Atkins, the National WWI Museum, the Country Club Plaza and the TWA Museum at the downtown airport.',
    lede='Barbecue, jazz and fountains, from a downtown airport.',
    intro='Kansas City is a barbecue capital and a jazz town, and its downtown airport sits just across the river from the skyline. Visit the TWA Museum at the airport, see the giant shuttlecocks at the Nelson-Atkins, spend a morning at the National WWI Museum, hear jazz at 18th & Vine and eat burnt ends at Joe’s.',
    pills=['Barbecue', 'Jazz', 'Aviation & museums'],
    flight=dict(
        title='Land downtown.',
        intro='KMKC, Charles B. Wheeler Downtown Airport, is a towered airport across the Missouri River from downtown, about 5 minutes from the skyline. The TWA Museum is on the field.',
        fbo=('Atlantic Aviation', 'Charles B. Wheeler Downtown Airport, Kansas City, MO', '816-949-8900'),
        notes=['A second FBO operates on the field (816-842-8484). Confirm hours, fees and cars; 100LL availability varies by FBO. No live fuel price is shown.',
               'Brief the Kansas City Class B. About 825 nm from Myrtle Beach: plan one or two fuel stops and three nights.'],
        around_title='Streetcar or car.',
        around='The free KC Streetcar runs from River Market through downtown to Union Station; a car or rideshare covers the Plaza and barbecue spots.'),
    stay=dict(title='Near the Plaza or downtown.', intro='Rates and availability need travel dates.',
        cards=[('Country Club Plaza · Luxury', 'The Fontaine', 'A modern hotel on the Plaza with a rooftop pool.', 'https://www.thefontainehotel.com/'),
               ('Plaza · Historic', 'The Raphael Hotel', 'A 1927 boutique hotel by the Plaza.', 'https://www.raphaelkc.com/'),
               ('Downtown · Art deco', 'Hotel Phillips', 'A restored 1931 art deco hotel downtown.', 'https://www.hotelphillips.com/')]),
    eat=dict(title='Burnt ends and beyond.', intro='Barbecue lines can be long; go early.',
        cards=[('Lunch · Barbecue', 'Joe’s Kansas City Bar-B-Que', 'Famous barbecue in a gas station; get the Z-Man.', 'https://www.joeskc.com/'),
               ('Friday dinner · Barbecue', 'Q39', 'Competition-style barbecue in a sit-down restaurant.', 'https://www.q39kc.com/'),
               ('Saturday dinner · Fine dining', 'Corvino', 'A celebrated tasting-menu and supper-club restaurant.', 'https://www.corvino.com/'),
               ('Dinner · Classic', 'Jack Stack Barbecue', 'Burnt ends and lamb ribs in the Freight House.', 'https://www.jackstackbbq.com/')]),
    explore=dict(title='Museums, jazz and fountains.', intro='Several excellent museums are free or inexpensive.',
        items=[('TWA Museum', 'Airline history in TWA’s old headquarters at the downtown airport.', 'https://www.twamuseum.com/', 'TWA Museum'),
               ('Nelson-Atkins Museum of Art', 'A free museum with a great sculpture lawn.', 'https://www.nelson-atkins.org/', 'Museum'),
               ('National WWI Museum and Memorial', 'The country’s WWI museum, with a view from the Liberty Memorial tower.', 'https://www.theworldwar.org/', 'Museum'),
               ('18th & Vine', 'The American Jazz Museum, the Blue Room and the Negro Leagues Baseball Museum.', 'https://www.americanjazzmuseum.org/', 'Jazz Museum'),
               ('Country Club Plaza', 'Spanish-style shopping and fountains, lit up for the holidays.', 'https://www.countryclubplaza.com/', 'The Plaza')]),
    events=dict(url='https://www.visitkc.com/', button='Browse Kansas City events',
        cards=[('Thanksgiving–January', 'Plaza Lights', 'The Plaza outlined in lights.', 'https://www.countryclubplaza.com/', 'The Plaza'),
               ('Fall', 'American Royal', 'A famous barbecue competition.', 'https://www.americanroyal.com/', 'American Royal'),
               ('Spring & fall', 'Best seasons', 'Summers are hot; winters can be icy.')]),
    itinerary=dict(intro='A sample long weekend: barbecue, jazz and museums. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & aviation', [('Arrival', 'Land at KMKC, subject to weather, your fuel stops and your actual flight plan.'), ('Afternoon', 'The TWA Museum on the field.'), ('Evening', 'Dinner at Q39.')]),
              ('DAY 2', 'Art & jazz', [('Morning', 'The Nelson-Atkins.'), ('Afternoon', 'Lunch at Joe’s, then the WWI Museum.'), ('Evening', 'Dinner at Corvino, then jazz at the Blue Room.')]),
              ('DAY 3', 'The Plaza & home', [('Morning', 'A walk around the Plaza fountains.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then Corvino and jazz.'),
          ('Airspace', 'Brief the Kansas City Class B.'),
          ('Long flight', 'About 825 nm. Plan fuel stops and extra nights.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
