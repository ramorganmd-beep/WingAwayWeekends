"""Generate docs/huntsville/index.html (Huntsville, Alabama)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='huntsville', name='Huntsville', state='Alabama', number=75, reviewed='November 4, 2026',
    airport='KHSV', nm=394, flight_time='~2 hr 52 <small>min</small>', style='Rental car',
    place='Huntsville, Alabama',
    description='A curated Huntsville getaway for GA pilots and their partners, from KMYR to KHSV. Rocket City: a Saturn V at the U.S. Space & Rocket Center, a botanical garden, Monte Sano Mountain and a lively downtown.',
    lede='Rocket City: a Saturn V, a mountain and a lively downtown.',
    intro='Huntsville built the rockets that took Americans to the Moon, and the U.S. Space & Rocket Center has a full Saturn V hanging overhead. Add a walk at the Huntsville Botanical Garden, sunset from Monte Sano Mountain, studios at Lowe Mill and dinner downtown, and it is an easy, aviation-minded weekend.',
    pills=['Space & aviation', 'Gardens & mountain', 'Downtown dining'],
    flight=dict(
        title='Fly to Rocket City.',
        intro='KHSV, Huntsville International, is a towered airport about 15 minutes from the Space & Rocket Center and downtown.',
        fbo=('Signature Aviation', 'Huntsville International Airport, Huntsville, AL', '256-772-9341'),
        notes=['Huntsville Executive Airport (KMDQ), north of the city, is a non-towered alternative with its own FBO (256-828-1403). Confirm hours, fees and cars. No live fuel price is shown.',
               'About 395 nm from Myrtle Beach. Expect mountain-adjacent weather and summer afternoon storms.'],
        around_title='Rent a car.',
        around='Downtown is walkable, but the space center, garden and Monte Sano need a car.'),
    stay=dict(title='Downtown or next to the rockets.', intro='Rates and availability need travel dates.',
        cards=[('Downtown · Boutique', '106 Jefferson', 'A stylish hotel downtown, home of the Revivalist restaurant.', 'https://www.106jefferson.com/'),
               ('Space center · On site', 'Huntsville Marriott at the Space & Rocket Center', 'Wake up beside the Saturn V.', 'https://www.marriott.com/en-us/hotels/hsval-huntsville-marriott-at-the-space-and-rocket-center/overview/'),
               ('Bridge Street · Shopping', 'The Westin Huntsville', 'A full-service hotel at Bridge Street Town Centre.', 'https://www.marriott.com/en-us/hotels/hsvwi-the-westin-huntsville/overview/')]),
    eat=dict(title='Dinner downtown.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · Classic', 'Cotton Row', 'Refined Southern dining in an 1821 building on the Square.', 'https://www.cottonrowrestaurant.com/'),
               ('Saturday dinner · Southern', 'Revivalist', 'Southern cooking at 106 Jefferson.', 'https://www.revivalisthuntsville.com/'),
               ('Drinks · Rooftop', 'Rhythm on Monroe', 'A rooftop restaurant and bar at the Von Braun Center.', 'https://www.vonbrauncenter.com/rhythm-on-monroe/')]),
    explore=dict(title='Rockets, gardens and a mountain.', intro='One big museum and plenty of fresh air.',
        items=[('U.S. Space & Rocket Center', 'A Saturn V, the Space Shuttle Pathfinder and decades of rocketry. Allow most of a day.', 'https://www.rocketcenter.com/', 'Space center'),
               ('Huntsville Botanical Garden', 'Gardens, woodland paths and a butterfly house.', 'https://hsvbg.org/', 'Garden'),
               ('Monte Sano State Park', 'Trails and overlooks on the mountain above town.', 'https://www.alapark.com/parks/monte-sano-state-park', 'Park'),
               ('Lowe Mill ARTS & Entertainment', 'Artists’ studios in an old cotton mill.', 'https://lowemill.art/', 'Lowe Mill'),
               ('Twickenham Historic District', 'Antebellum homes near downtown.', 'https://www.huntsvilleal.gov/historicmarkers/twikenham-historic-district/', 'District')]),
    events=dict(url='https://www.huntsville.org/', button='Browse Huntsville events',
        cards=[('Late April', 'Panoply Arts Festival', 'Art and music in Big Spring Park.', 'https://www.artshuntsville.org/event/panoply/', 'Panoply'),
               ('Holidays', 'Galaxy of Lights', 'A light show at the Botanical Garden.', 'https://hsvbg.org/visit/exhibits/galaxy-of-lights/', 'Galaxy of Lights'),
               ('Spring & fall', 'Best seasons', 'Mild weather for the mountain trails.')]),
    itinerary=dict(intro='A sample weekend: space, gardens and a mountain. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & downtown', [('Arrival', 'Land at KHSV, subject to weather and your actual flight plan.'), ('Afternoon', 'Big Spring Park and downtown.'), ('Evening', 'Dinner at Cotton Row.')]),
              ('DAY 2', 'Rockets', [('Morning', 'The U.S. Space & Rocket Center.'), ('Afternoon', 'The Botanical Garden.'), ('Evening', 'Dinner at Revivalist, then the rooftop.')]),
              ('DAY 3', 'The mountain & home', [('Morning', 'A hike on Monte Sano.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then dinners.'),
          ('Space center time', 'Plan most of a day; it is big.'),
          ('Airports', 'KHSV is closest to the space center; KMDQ is a non-towered alternative.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
