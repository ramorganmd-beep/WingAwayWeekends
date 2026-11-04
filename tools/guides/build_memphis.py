"""Generate docs/memphis/index.html (Memphis, Tennessee)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='memphis', name='Memphis', state='Tennessee', number=78, reviewed='November 4, 2026',
    airport='KMEM', nm=553, flight_time='~3 hr 56 <small>min</small>', style='Rental car or rideshare',
    place='Memphis, Tennessee',
    description='A curated Memphis getaway for GA pilots and their partners, from KMYR to KMEM. Blues on Beale Street, Graceland, Sun Studio and Stax, the National Civil Rights Museum, the Peabody ducks and Memphis barbecue.',
    lede='Blues, soul, rock ’n’ roll and barbecue on the Mississippi.',
    intro='Memphis is where the blues found a home and rock ’n’ roll was born. Watch the Peabody ducks march, tour Graceland and the tiny Sun Studio where Elvis first recorded, hear soul history at Stax, spend a sobering morning at the National Civil Rights Museum and finish with ribs and live blues on Beale Street.',
    pills=['Music history', 'Barbecue', 'Grand hotel'],
    flight=dict(
        title='Land at Memphis.',
        intro='KMEM, Memphis International, is a busy towered airport and FedEx’s home base, about 15 minutes from downtown.',
        fbo=('Wilson Air Center', 'Memphis International Airport, Memphis, TN', '901-345-2992'),
        notes=['Wilson Air Center is a well-regarded GA FBO. General DeWitt Spain Airport (M01), just north of downtown, is a quieter non-towered alternative (901-358-0028). Confirm hours, fees and cars. No live fuel price is shown.',
               'Expect heavy cargo traffic at night and a Class B arrival. About 555 nm from Myrtle Beach: plan a fuel stop or a long nonstop leg.'],
        around_title='Rideshare downtown.',
        around='Downtown and Beale Street are walkable; use a car or rideshare for Graceland, Stax and Sun Studio.'),
    stay=dict(title='The South’s grand hotel, or Elvis’s.', intro='Rates and availability need travel dates.',
        cards=[('Downtown · Since 1869', 'The Peabody Memphis', 'The famous grand hotel, where ducks march to the lobby fountain every day.', 'https://www.peabodymemphis.com/'),
               ('Graceland · Themed', 'The Guest House at Graceland', 'A polished hotel beside Elvis’s home.', 'https://www.guesthousegraceland.com/'),
               ('Downtown · Unusual', 'Big Cypress Lodge', 'A lodge-style hotel inside the Pyramid, with treehouse-style rooms.', 'https://big-cypress.com/')]),
    eat=dict(title='Ribs, steaks and Southern cooking.', intro='Reserve weekend dinners; barbecue spots are first come, first served.',
        cards=[('Friday dinner · Since 1948', 'Charlie Vergos’ Rendezvous', 'Famous dry-rub ribs in a downtown basement.', 'https://www.hogsfly.com/'),
               ('Lunch · Barbecue', 'Central BBQ', 'A local favorite for pulled pork and ribs.', 'https://www.cbqmemphis.com/'),
               ('Saturday dinner · Wood-fired', 'The Gray Canary', 'Wood-fired seafood and steaks by the river.', 'https://www.thegraycanary.com/'),
               ('Dinner · Steakhouse', 'Folk’s Folly', 'Memphis’s original prime steakhouse.', 'https://www.folksfolly.com/')]),
    explore=dict(title='Music, history and Beale Street.', intro='Pick two big sites a day and save the evenings for music.',
        items=[('Graceland', 'Elvis’s home, cars and private jets.', 'https://www.graceland.com/', 'Graceland'),
               ('Sun Studio', 'The small studio where Elvis, Johnny Cash and others first recorded.', 'https://www.sunstudio.com/', 'Sun Studio'),
               ('National Civil Rights Museum', 'Built around the Lorraine Motel, where Dr. Martin Luther King Jr. was killed.', 'https://www.civilrightsmuseum.org/', 'Museum'),
               ('Stax Museum of American Soul Music', 'The story of Otis Redding, Isaac Hayes and Memphis soul.', 'https://www.staxmuseum.com/', 'Stax'),
               ('Beale Street', 'Blues clubs and neon, best after dark.', 'https://www.bealestreet.com/', 'Beale Street')]),
    events=dict(url='https://www.memphisinmay.org/', button='Browse Memphis in May',
        cards=[('May', 'Memphis in May', 'The Beale Street Music Festival and the World Championship Barbecue Cooking Contest.', 'https://www.memphisinmay.org/', 'Festival'),
               ('August', 'Elvis Week', 'Fans gather at Graceland; book early or avoid.', 'https://www.graceland.com/elvis-week', 'Elvis Week'),
               ('Spring & fall', 'Best seasons', 'Summers are hot and humid.')]),
    itinerary=dict(intro='A sample weekend: music, history and barbecue. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & Beale Street', [('Arrival', 'Land at KMEM, subject to weather and your actual flight plan.'), ('Afternoon', 'The Peabody duck march at 5 p.m.'), ('Evening', 'Ribs at the Rendezvous, then Beale Street.')]),
              ('DAY 2', 'Elvis & soul', [('Morning', 'Graceland.'), ('Afternoon', 'Sun Studio, then Stax.'), ('Evening', 'Dinner at The Gray Canary.')]),
              ('DAY 3', 'History & home', [('Morning', 'The National Civil Rights Museum.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then Graceland tickets and dinners.'),
          ('Airspace', 'Brief the Memphis Class B and heavy cargo traffic.'),
          ('Long leg', 'About 555 nm. Plan a fuel stop or check range and reserves.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
