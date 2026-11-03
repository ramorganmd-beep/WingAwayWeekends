"""Generate docs/mackinac/index.html (Mackinac Island, Michigan)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='mackinac', name='Mackinac Island', state='Michigan', number=46, reviewed=None,
    airport='KMCD', nm=777, flight_time='~5 hr 26 <small>min</small>', style='Horses, bikes + walks',
    place='Mackinac Island, Michigan',
    description='A curated two-night Mackinac Island getaway for GA pilots and their partners, from KMYR to KMCD. A car-free island of horse-drawn carriages, the Grand Hotel’s famous porch, a historic fort, bike rides and fudge.',
    lede='No cars. Just horses, bikes and the Grand Hotel’s porch.',
    intro='Cars have been banned on Mackinac Island since the 1890s, so the clip-clop of horses and the ring of bicycle bells set the pace. Land on the island’s own runway, take a horse-drawn taxi to the Grand Hotel, bike the eight-mile shore road, explore an 18th-century fort and sample the famous fudge.',
    pills=['Car-free island', 'Grand Hotel', 'Bikes & carriages'],
    flight=dict(
        title='Land on the island itself.',
        intro='KMCD, Mackinac Island Airport, sits on the island’s plateau, about a mile and a half from downtown. It is run by the Mackinac Island State Park Commission.',
        fbo=('Mackinac Island Airport (state park; not a full-service FBO)', 'Mackinac Island, MI 49757', '906-847-3231', 'https://www.mackinacparks.com/'),
        notes=['Call ahead about landing and parking fees, fuel, hours and seasonal operations. The island is busiest from June to August; arrange a horse-drawn taxi to town from the airport.',
               'Runway 8/26 is about 3,500 feet, on high ground with trees at both ends; Lake Huron winds bring crosswinds and fog. Brief performance and an alternate such as Pellston. About 780 nm from Myrtle Beach: plan a fuel stop, and consider a third night.'],
        around_title='Leave the car behind (you have to).',
        around='Walk, rent bikes or take horse-drawn taxis and carriage tours. The island is about eight miles around.'),
    stay=dict(title='A grand porch or the water’s edge.', intro='Rates and availability need travel dates. Most hotels are open roughly May to October.',
        cards=[('Hilltop · Since 1887', 'Grand Hotel', 'A landmark hotel with the world’s longest porch, afternoon tea, formal dinners and a dress code after 6 p.m.', 'https://www.grandhotel.com/'),
               ('Waterfront · Downtown', 'Chippewa Hotel Waterfront', 'A harborfront hotel on Main Street, home to the Pink Pony bar.', 'https://www.chippewahotel.com/'),
               ('Lakeside · Resort', 'Mission Point Resort', 'A sprawling resort on 18 acres at the quiet end of downtown, with lawns down to the lake.', 'https://www.missionpoint.com/')]),
    eat=dict(title='Two dinners. One fudge crawl.', intro='Reserve Grand Hotel dinner, and check its dress code.',
        cards=[('Friday dinner · Waterfront', 'The Pink Pony', 'A lively waterfront bar and restaurant on Main Street, with harbor views.', 'https://www.pinkponymackinac.com/'),
               ('Saturday dinner · Formal', 'Grand Hotel Main Dining Room', 'A five-course dinner in the Grand Hotel’s grand dining room. Jackets for men in the evening.', 'https://www.grandhotel.com/dining/'),
               ('Afternoon · A tradition', 'Fudge on Main Street', 'Watch fudge made on marble slabs at the shops along Main Street. Everyone has a favorite.')]),
    explore=dict(title='Forts, bluffs and the shore road.', intro='Everything is by bike, horse or on foot.',
        items=[('Fort Mackinac', 'A hilltop fort built by the British in 1780, with cannon and rifle firings and views over the harbor.', 'https://www.mackinacparks.com/', 'Tickets'),
               ('Bike around the island', 'M-185, the only state highway with no cars, runs eight flat miles around the shore.'),
               ('Arch Rock', 'A natural limestone arch 146 feet above the water, in Mackinac Island State Park.'),
               ('A carriage tour', 'A narrated horse-drawn tour of the island’s history, bluffs and cottages.'),
               ('The Grand Hotel porch', 'Have a drink or afternoon tea on the 660-foot porch overlooking the Straits.')]),
    events=dict(url='https://www.mackinacisland.org/', button='Browse Mackinac Island events',
        cards=[('June', 'Lilac Festival', 'The island’s famous lilacs in bloom, with a parade.'),
               ('Summer', 'High season', 'Busy, lively and pricey. Book early.'),
               ('September–October', 'Quieter season', 'Fall color and fewer crowds until the hotels close for winter.')]),
    itinerary=dict(intro='A sample weekend: the fort, a bike ride and a Grand Hotel dinner. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & downtown', [('Arrival', 'Land at KMCD, subject to weather, your fuel stop and your actual flight plan, and take a horse-drawn taxi to town.'), ('Afternoon', 'Check in and walk Main Street.'), ('Evening', 'Dinner at the Pink Pony.')]),
              ('SAT', 'Around the island', [('Morning', 'Bike the eight-mile shore road to Arch Rock and back.'), ('Afternoon', 'Fort Mackinac, then tea on the Grand Hotel porch.'), ('Evening', 'Dinner at the Grand Hotel.')]),
              ('SUN', 'An easy departure', [('Morning', 'A carriage tour and a box of fudge.'), ('Before leaving', 'Book a taxi to the airport ahead.'), ('Fly home', 'Lake fog and winds can delay departures; keep the day flexible.')])]),
    know=[('Book in this order', 'Lodging and airport arrangements first, then dinner reservations.'),
          ('Long flight', 'About 780 nm. Plan a fuel stop and consider a third night.'),
          ('Seasons', 'Most hotels and services run May to October.'),
          ('Runway', 'About 3,500 feet with trees at both ends. Check performance.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
