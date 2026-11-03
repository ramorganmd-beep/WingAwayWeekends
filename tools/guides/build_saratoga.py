"""Generate docs/saratoga/index.html (Saratoga Springs, New York)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='saratoga', name='Saratoga Springs', state='New York', number=34, reviewed=None,
    airport='5B2', nm=611, flight_time='~4 hr 20 <small>min</small>', style='Rental car or taxi + walks',
    place='Saratoga Springs, New York',
    description='A curated two-night Saratoga Springs getaway for GA pilots and their partners, from KMYR to 5B2. Thoroughbred racing, mineral springs and spa baths, Victorian streets and summer concerts.',
    lede='Horse racing, mineral baths and a lively main street.',
    intro='Saratoga Springs has drawn visitors to its mineral springs for two centuries, and to its racetrack since 1863. Spend a summer afternoon at one of the oldest tracks in the country, soak at the Roosevelt Baths, walk Broadway’s Victorian blocks and catch an evening concert under the trees.',
    pills=['Thoroughbred racing', 'Spa baths', 'Summer concerts'],
    flight=dict(
        title='Land 10 minutes from downtown.',
        intro='5B2, Saratoga County Airport, sits just west of the city, about 10 minutes from Broadway.',
        fbo=('North American Flight Services', '405 Greenfield Avenue, Ballston Spa, NY 12020', '518-885-5470'),
        notes=['Directories list hours from about 7:30 a.m. to dusk. Ask about rental cars or a taxi, parking and fees, and expect very busy weekends during the summer racing season. No live fuel price is shown.',
               'At about 600 nm from Myrtle Beach, plan a fuel stop. Albany’s Class C airspace lies to the south. Review the sectional and current NOTAMs.'],
        around_title='Walk downtown.',
        around='Broadway, the restaurants and Congress Park are walkable. Use a car or taxi for the racetrack, the state park and SPAC in summer.'),
    stay=dict(title='Grand, intimate or in the park.', intro='Rates and availability need travel dates, and racing season is much pricier.',
        cards=[('Broadway · Grand hotel', 'The Adelphi Hotel', 'A restored 1877 grand hotel on Broadway, with a pool, a lively bar and Victorian flair.', 'https://theadelphihotel.com/'),
               ('Broadway · Boutique', 'Saratoga Arms', 'A small, elegant hotel in an 1870 brick house, with a wide porch on Broadway.', 'https://www.saratogaarms.com/'),
               ('State park · Historic', 'The Gideon Putnam', 'A 1935 Georgian Revival hotel inside Saratoga Spa State Park, next to the Roosevelt Baths.', 'https://www.gideonputnam.com/')]),
    eat=dict(title='Two dinners. One fried-chicken lunch.', intro='Reserve dinners, especially in July and August.',
        cards=[('Friday dinner · Steak & seafood', '15 Church', 'An elegant downtown restaurant with a garden patio, known for steaks, raw bar and wine.', 'https://www.15churchrestaurant.com/'),
               ('Saturday dinner · Italian', 'Osteria Danny', 'Seasonal Italian cooking in an intimate room. Book well ahead.', 'https://osteriadanny.com/'),
               ('Lunch · Since 1938', 'Hattie’s', 'A Saratoga institution for Southern fried chicken and biscuits.', 'https://hattiesrestaurants.com/')]),
    explore=dict(title='Races, springs and music.', intro='Choose one big outing a day and leave time for Broadway.',
        items=[('Saratoga Race Course', 'One of the oldest and most beautiful racetracks in the country, open for its summer meet from July to Labor Day. Arrive early for a picnic table.', 'https://www.nyra.com/saratoga/', 'Race schedule'),
               ('Saratoga Spa State Park', 'Mineral springs, trails and grand 1930s buildings. Taste the springs along the Geyser Creek trail.', 'https://parks.ny.gov/visit/state-parks/saratoga-spa-state-park', 'Park information'),
               ('National Museum of Racing and Hall of Fame', 'Across from the track, with the story of American thoroughbred racing.', 'https://racingmuseum.org/', 'Museum information'),
               ('Saratoga Performing Arts Center', 'An open-air amphitheater in the state park, summer home of the Philadelphia Orchestra and New York City Ballet.', 'https://spac.org/', 'SPAC schedule'),
               ('Saratoga National Historical Park', 'About 30 minutes away, the battlefield where American forces won a turning point of the Revolution in 1777.')]),
    spa=dict(title='The Roosevelt Baths & Spa', body='Soak in Saratoga’s naturally carbonated mineral water in private tubs, a tradition since the 1930s.'),
    events=dict(url='https://www.discoversaratoga.org/', button='Browse Saratoga events',
        cards=[('July–Labor Day', 'Racing season', 'The summer meet, including the Travers Stakes in late August. Lodging prices soar; book very early.'),
               ('June–August', 'SPAC season', 'Orchestra, ballet, jazz and rock concerts in the park.'),
               ('Fall', 'Quieter weekends', 'Fall color, easier dinner reservations and lower rates.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the track or the baths, Broadway and two good dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Broadway', [('Arrival', 'Land at 5B2, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in and walk Broadway and Congress Park.'), ('Evening', 'Dinner at 15 Church.')]),
              ('SAT', 'Races or springs', [('Morning', 'Breakfast at the track in season, or the state park.'), ('Afternoon', 'An afternoon at the races, or a soak at the Roosevelt Baths.'), ('Evening', 'Dinner at Osteria Danny, or a SPAC concert.')]),
              ('SUN', 'An easy departure', [('Morning', 'The Racing Museum, or fried chicken at Hattie’s.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging first, especially in racing season, then dinners and spa time.'),
          ('Racing season', 'July and August are busiest. Spring and fall are calmer and cheaper.'),
          ('Fuel stop', 'Plan a fuel stop for most piston aircraft.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
