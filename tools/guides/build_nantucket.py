"""Generate docs/nantucket/index.html (Nantucket, Massachusetts)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='nantucket', name='Nantucket', state='Massachusetts', number=31, reviewed=None,
    airport='KACK', nm=620, flight_time='~4 hr 24 <small>min</small>', style='Bikes + shuttles',
    place='Nantucket, Massachusetts',
    description='A curated two-night Nantucket getaway for GA pilots and their partners, from KMYR to KACK. Cobblestone streets, lighthouses, beaches, bikes and island dinners, 30 miles out to sea.',
    lede='Fly out to the island. Ride a bike to the lighthouse.',
    intro='Thirty miles off Cape Cod, Nantucket was once the whaling capital of the world. Today its cobblestone town, gray-shingled cottages and wide beaches make it one of New England’s great escapes. Fly straight to the island, bike to Sconset, watch the sunset at Madaket and dine by the harbor.',
    pills=['Island town', 'Bikes & beaches', 'Lighthouses'],
    flight=dict(
        title='Land on the island.',
        intro='KACK, Nantucket Memorial, is a towered airport about three miles from town, with a town-run FBO next to the terminal.',
        fbo=('Nantucket Memorial Airport FBO', '14 Airport Road, Nantucket, MA 02554', '508-325-5307'),
        notes=['Summer is extremely busy; ask the FBO about parking availability and reservations well ahead, and confirm hours and fees. No live fuel price is shown.',
               'It is about 25 nm over open water from Cape Cod, and fog can close the island for hours, especially in late spring and early summer. Carry appropriate safety gear, plan a mainland alternate such as Hyannis, and expect a fuel stop on the way.'],
        around_title='Leave the car behind.',
        around='Taxis and seasonal shuttle buses run from the airport. On the island, bikes are the best way around; paved paths run to Sconset, Surfside and Madaket.'),
    stay=dict(title='In town or by the sea.', intro='A secluded resort, a harborside classic or a stylish small hotel in town. Rates and availability need travel dates.',
        cards=[('Wauwinet · Relais & Châteaux', 'The Wauwinet', 'A secluded luxury inn between the harbor and the ocean, eight miles from town, with a shuttle, a beach and TOPPER’S restaurant.', 'https://www.wauwinet.com/'),
               ('Harbor · Classic', 'White Elephant', 'A polished harborfront hotel a short walk from Main Street, with gardens and a spa.', 'https://www.whiteelephantnantucket.com/'),
               ('Town · Boutique', 'Greydon House', 'A small, stylish hotel in a restored house in the historic district, with an excellent restaurant.', 'https://greydonhouse.com/')]),
    eat=dict(title='Two dinners. One very special.', intro='Reserve summer dinners well ahead.',
        cards=[('Friday dinner · Town', 'The Club Car', 'A Nantucket institution in an old railway car, with refined dinners and a lively piano bar.', 'https://www.theclubcar.com/'),
               ('Saturday dinner · The Wauwinet', 'TOPPER’S', 'Fine dining at The Wauwinet, with a terrace over the harbor. Take the inn’s boat or shuttle from town in season.', 'https://www.wauwinet.com/'),
               ('Lunch · Harborside', 'Straight Wharf Restaurant', 'A summer favorite on the wharf, known for seafood and a buzzing bar.', 'https://straightwharfrestaurant.com/')]),
    explore=dict(title='Cobblestones, lighthouses and beaches.', intro='Slow down. This is an island for bikes, beaches and long lunches.',
        items=[('The Whaling Museum', 'The Nantucket Historical Association’s museum in a former candle factory, with a 46-foot sperm whale skeleton and the island’s whaling story.', 'https://nha.org/', 'Museum information'),
               ('Bike to Sconset', 'A flat, paved 8-mile path to the village of Siasconset, with rose-covered cottages, the Bluff Walk and Sankaty Head Lighthouse.'),
               ('Sunset at Madaket', 'The island’s classic sunset beach, at the end of the western bike path.'),
               ('Brant Point Lighthouse', 'The little lighthouse at the harbor entrance. Tradition says toss a penny as the ferry passes to promise a return.'),
               ('Great Point', 'Over-sand tours run out to the lighthouse and seal colonies at the island’s wild northern tip.')]),
    events=dict(url='https://www.nantucketchamber.org/', button='Browse Nantucket events',
        cards=[('April', 'Daffodil Festival', 'Millions of daffodils and a parade of antique cars to Sconset.'),
               ('June', 'Nantucket Film Festival', 'Screenings and talks in town. A fun early-summer weekend.'),
               ('Early December', 'Christmas Stroll', 'Decorated streets, carolers and shops lit for the holidays.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: bikes, beaches, a lighthouse and two island dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & town', [('Arrival', 'Land at KACK, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in and walk Main Street and the wharves.'), ('Evening', 'Dinner at The Club Car.')]),
              ('SAT', 'Bikes & beaches', [('Morning', 'Bike to Sconset and walk the Bluff Walk.'), ('Afternoon', 'Lunch on Straight Wharf, then the Whaling Museum or the beach.'), ('Evening', 'Dinner at TOPPER’S.')]),
              ('SUN', 'An easy departure', [('Morning', 'A ride to Brant Point and breakfast in town.'), ('Before leaving', 'Allow time at the FBO; summer is busy.'), ('Fly home', 'Island fog can delay departures. Keep the day flexible.')])]),
    know=[('Book in this order', 'FBO parking and lodging first, then dinners.'),
          ('Over water', 'About 25 nm of open water from Cape Cod. Brief safety gear and gliding distance.'),
          ('Fog', 'Fog can close the island for hours. Have a mainland alternate and a backup day.'),
          ('Seasons', 'Many places close from late fall to spring. Check opening dates.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
