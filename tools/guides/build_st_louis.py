"""Generate docs/st-louis/index.html (St. Louis, Missouri)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='st-louis', name='St. Louis', state='Missouri', number=83, reviewed=None,
    airport='KCPS', nm=618, flight_time='~4 hr 22 <small>min</small>', style='Rental car or rideshare',
    place='St. Louis, Missouri',
    description='A curated St. Louis getaway for GA pilots and their partners, from KMYR to KCPS. The Gateway Arch, Forest Park’s free museums, the Missouri Botanical Garden, Italian dinners on The Hill and frozen custard.',
    lede='The Arch, Forest Park and dinner on The Hill.',
    intro='St. Louis has some of the country’s best free attractions. Ride the tram to the top of the Gateway Arch, spend a day in Forest Park at the Art Museum, walk the Missouri Botanical Garden, play at the wild City Museum, eat toasted ravioli on The Hill and finish with frozen custard at Ted Drewes on old Route 66.',
    pills=['Gateway Arch', 'Free museums', 'Italian on The Hill'],
    flight=dict(
        title='Land across the river.',
        intro='KCPS, St. Louis Downtown Airport, is a towered field in Cahokia, Illinois, about 15 minutes from the Arch and downtown.',
        fbo=('Jet Aviation', 'St. Louis Downtown Airport, Cahokia Heights, IL', '618-646-8262'),
        notes=['Spirit of St. Louis Airport (KSUS), west of the city, is an alternative with a Signature FBO (636-532-8882) and is closer to Forest Park and the western suburbs. Confirm hours, fees and cars. No live fuel price is shown.',
               'Brief the St. Louis Class B. About 620 nm from Myrtle Beach: plan a fuel stop and three nights.'],
        around_title='Rent a car or rideshare.',
        around='Downtown is compact, but Forest Park, The Hill and Ted Drewes are spread out.'),
    stay=dict(title='Near the park or by the river.', intro='Rates and availability need travel dates.',
        cards=[('Forest Park · Boutique', 'The Cheshire', 'A literary-themed boutique hotel across from Forest Park.', 'https://www.cheshirestl.com/'),
               ('Downtown · Luxury', 'Four Seasons Hotel St. Louis', 'River and Arch views, with a spa and rooftop pool.'),
               ('Downtown · Historic', 'St. Louis Union Station Hotel', 'A hotel in the 1894 rail station, with a light show in the Grand Hall.', 'https://www.stlouisunionstation.com/')]),
    eat=dict(title='Toasted ravioli, barbecue and custard.', intro='Reserve weekend dinners on The Hill.',
        cards=[('Friday dinner · The Hill', 'Charlie Gitto’s', 'Classic Italian on The Hill, where toasted ravioli was said to be born.', 'https://www.charliegittos.com/'),
               ('Lunch · Barbecue', 'Pappy’s Smokehouse', 'Memphis-style ribs; arrive early.', 'https://www.pappyssmokehouse.com/'),
               ('Lunch · The Hill', 'Gioia’s Deli', 'Famous for its hot salami sandwich.', 'https://www.gioiasdeli.com/'),
               ('Dessert · Since 1929', 'Ted Drewes Frozen Custard', 'A “concrete” on Route 66.', 'https://www.teddrewes.com/')]),
    explore=dict(title='The Arch and Forest Park.', intro='Many of the city’s best attractions are free.',
        items=[('Gateway Arch National Park', 'Ride the tram 630 feet to the top; reserve tram times.', 'https://www.gatewayarch.com/', 'Tickets'),
               ('Forest Park', 'A huge park with the free Saint Louis Art Museum, zoo and history museum.', 'https://www.forestparkforever.org/', 'Forest Park'),
               ('Saint Louis Art Museum', 'A free museum in Forest Park.', 'https://www.slam.org/', 'Museum'),
               ('Missouri Botanical Garden', 'One of the oldest botanical gardens in the country, with a Japanese garden.'),
               ('City Museum', 'A playground for adults built from salvaged architecture.', 'https://www.citymuseum.org/', 'City Museum')]),
    events=dict(url='https://www.explorestlouis.com/', button='Browse St. Louis events',
        cards=[('July 4th weekend', 'Fair Saint Louis', 'Fireworks and music under the Arch.'),
               ('Summer', 'The Muny', 'Outdoor musicals in Forest Park.'),
               ('Spring & fall', 'Best seasons', 'Summers are hot and humid.')]),
    itinerary=dict(intro='A sample long weekend: the Arch, Forest Park and The Hill. Plan three nights for the flight. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the Arch', [('Arrival', 'Land at KCPS, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'The Gateway Arch tram.'), ('Evening', 'Dinner at Charlie Gitto’s on The Hill.')]),
              ('DAY 2', 'Forest Park', [('Morning', 'The Art Museum.'), ('Afternoon', 'The Botanical Garden.'), ('Evening', 'Ted Drewes for dessert.')]),
              ('DAY 3', 'City Museum & home', [('Morning', 'City Museum or Pappy’s for lunch.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then Arch tram times and dinners.'),
          ('Airports', 'KCPS is closest to downtown; KSUS is closer to the western suburbs.'),
          ('Long flight', 'About 620 nm. Plan a fuel stop and extra nights.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
