"""Generate docs/berkshires/index.html (The Berkshires, Massachusetts)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='berkshires', name='The Berkshires', state='Massachusetts', number=41, reviewed='November 3, 2026',
    airport='KPSF', nm=589, flight_time='~4 hr 11 <small>min</small>', style='Rental car',
    place='The Berkshires, Massachusetts',
    description='A curated two-night Berkshires getaway for GA pilots and their partners, from KMYR to KPSF. Tanglewood concerts, the Norman Rockwell Museum, grand estates, art museums and country inns.',
    lede='Music under the stars and art in the hills.',
    intro='The rolling hills of western Massachusetts have drawn artists and writers for 150 years. Picnic on the lawn at a Tanglewood concert, see Norman Rockwell’s paintings in Stockbridge, visit Edith Wharton’s country house and a world-class art museum, and stay at a grand estate or a classic New England inn.',
    pills=['Tanglewood', 'Art museums', 'Country inns'],
    flight=dict(
        title='Land in the middle of the hills.',
        intro='KPSF, Pittsfield Municipal, is a non-towered airport south of Pittsfield, about 15 minutes from Lenox and 25 from Stockbridge.',
        fbo=('Lyon Aviation', '832 Tamarack Road, Pittsfield, MA 01201', '413-443-6700'),
        notes=['Ask about rental cars, parking, fees and hours. No live fuel price is shown.',
               'Hilly terrain surrounds the field, with valley fog on fall mornings. About 590 nm from Myrtle Beach; plan a fuel stop. Review the sectional and current NOTAMs.'],
        around_title='You’ll need a car.',
        around='Lenox, Stockbridge, Great Barrington and Williamstown are spread along the valley.'),
    stay=dict(title='Grand estate, spa or classic inn.', intro='Rates and availability need travel dates; Tanglewood weekends fill early.',
        cards=[('Lenox · Relais & Châteaux', 'Blantyre', 'A Tudor-style 1902 mansion on a private estate, with a spa and fine dining. The romantic splurge.', 'https://www.blantyre.com/'),
               ('Lenox · Wellness resort', 'Canyon Ranch Lenox', 'An all-inclusive wellness resort in a Gilded Age mansion, with spa, fitness and healthy dining.', 'https://www.canyonranch.com/lenox'),
               ('Stockbridge · Historic inn', 'The Red Lion Inn', 'A classic New England inn on Main Street since 1773, with a big front porch and a tavern.', 'https://www.redlioninn.com/')]),
    eat=dict(title='Two dinners. One country lunch.', intro='Reserve dinners, especially in summer and fall.',
        cards=[('Friday dinner · Stockbridge', 'The Red Lion Inn', 'Classic New England dining at the inn, or a casual supper in the Widow Bingham’s Tavern.', 'https://www.redlioninn.com/'),
               ('Saturday dinner · Lenox', 'Blantyre', 'Elegant dinner in the mansion’s dining room. Book well ahead.', 'https://www.blantyre.com/'),
               ('Lunch · Great Barrington', 'Prairie Whale', 'Farm-driven cooking in a cozy house in Great Barrington.', 'https://www.prairiewhale.com/')]),
    explore=dict(title='Music, art and great houses.', intro='One or two outings a day.',
        items=[('Tanglewood', 'Summer home of the Boston Symphony Orchestra. Bring a picnic for the lawn. July and August.', 'https://www.bso.org/tanglewood', 'Concert schedule'),
               ('Norman Rockwell Museum', 'The largest collection of Rockwell’s work, in Stockbridge, where he lived and painted.'),
               ('The Mount', 'Edith Wharton’s 1902 country house and gardens in Lenox.', 'https://edithwharton.org/', 'Visit information'),
               ('The Clark & MASS MoCA', 'A celebrated art museum in Williamstown, and a vast contemporary art museum in old factory buildings in North Adams.', 'https://massmoca.org/', 'MASS MoCA'),
               ('Hancock Shaker Village', 'A historic Shaker village with its famous round stone barn and working farm.', 'https://hancockshakervillage.org/', 'Visit information')]),
    spa=dict(title='A Berkshires spa', body='Canyon Ranch and Blantyre both offer spa treatments in grand estate settings.'),
    events=dict(url='https://berkshires.org/', button='Browse Berkshires events',
        cards=[('July & August', 'Tanglewood season', 'Concerts on the lawn. Lodging fills early.'),
               ('Summer', 'Jacob’s Pillow & summer theater', 'Dance and theater festivals across the hills.'),
               ('Late September–October', 'Fall color', 'Some of the best foliage in southern New England.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: art, music and two country dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Stockbridge', [('Arrival', 'Land at KPSF, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'The Norman Rockwell Museum.'), ('Evening', 'Dinner at The Red Lion Inn.')]),
              ('SAT', 'Houses & music', [('Morning', 'The Mount, Edith Wharton’s house.'), ('Afternoon', 'Lunch in Great Barrington, then the spa.'), ('Evening', 'A Tanglewood concert in summer, or dinner at Blantyre.')]),
              ('SUN', 'Art & home', [('Morning', 'The Clark or Hancock Shaker Village.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Valley fog often lifts by mid-morning.')])]),
    know=[('Book in this order', 'Lodging and a car first, then concert tickets and dinners.'),
          ('Fuel stop', 'Plan a fuel stop for most piston aircraft.'),
          ('Tanglewood', 'July and August weekends fill months ahead.'),
          ('Hills', 'Terrain and morning fog. Keep a backup day.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
