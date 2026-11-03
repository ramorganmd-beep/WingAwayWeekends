"""Generate docs/kennebunkport/index.html (Kennebunkport, Maine)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='kennebunkport', name='Kennebunkport', state='Maine', number=40, reviewed=None,
    airport='KSFM', nm=699, flight_time='~4 hr 55 <small>min</small>', style='Rental car',
    place='Kennebunkport, Maine',
    description='A curated two-night Kennebunkport getaway for GA pilots and their partners, from KMYR to KSFM. Sea captains’ houses, a rocky coast drive, lobster shacks, beaches and a celebrated inn.',
    lede='Lobster rolls, a rocky coast and a famous inn.',
    intro='Kennebunkport is a classic Maine harbor village of sea captains’ houses, sailboats and lobster boats. Stroll Dock Square, drive Ocean Avenue past the crashing surf and Walker’s Point, order a lobster roll at a harbor shack, and end with a candlelit dinner at a celebrated inn.',
    pills=['Coastal village', 'Lobster', 'Beaches'],
    flight=dict(
        title='Land 25 minutes from the coast.',
        intro='KSFM, Sanford Seacoast Regional, is a non-towered airport inland, about 25 minutes from Kennebunkport.',
        fbo=('Southern Maine Aviation', '199 Airport Road, Sanford, ME 04073', '207-324-8919'),
        notes=['Ask about rental cars, parking, fees and hours. No live fuel price is shown.',
               'Portsmouth’s airspace lies to the south. Coastal fog and low clouds are common in summer. About 700 nm from Myrtle Beach; plan a fuel stop. Review the sectional and current NOTAMs.'],
        around_title='You’ll want a car.',
        around='Dock Square and the harbor are walkable once you arrive; a car helps for the beaches, Ocean Avenue and the coast.'),
    stay=dict(title='A famous inn, an ocean view or a grand old hotel.', intro='Rates and availability need travel dates.',
        cards=[('Kennebunk · Auberge', 'The White Barn Inn', 'One of New England’s most celebrated inns, with a candlelit restaurant in a restored barn and a spa.', 'https://auberge.com/white-barn-inn/'),
               ('Ocean Avenue · Views', 'Cape Arundel Inn', 'A small, elegant inn on Ocean Avenue with sweeping views of the Atlantic.', 'https://www.capearundelinn.com/'),
               ('Ocean Avenue · Classic', 'The Colony Hotel', 'A grand 1914 seaside hotel with a pool, a lawn above the sea and a casual summer feel.', 'https://thecolonyhotel.com/')]),
    eat=dict(title='Two dinners. One lobster roll.', intro='Reserve summer dinners well ahead.',
        cards=[('Friday dinner · Ocean views', 'Cape Arundel Inn', 'Dinner by the windows at Cape Arundel Inn, looking over the surf toward Walker’s Point.', 'https://www.capearundelinn.com/'),
               ('Saturday dinner · Celebrated', 'The White Barn Inn', 'A romantic, candlelit tasting dinner in a restored 19th-century barn. Book well ahead.', 'https://auberge.com/white-barn-inn/'),
               ('Lunch · Lobster rolls', 'The Clam Shack', 'A tiny, famous shack by the bridge, known for its lobster roll. Seasonal.', 'https://www.theclamshack.net/')]),
    explore=dict(title='Harbor, surf and beaches.', intro='Slow down and follow the coast.',
        items=[('Dock Square', 'Shops, galleries and cafés in the heart of the village, by the harbor.'),
               ('Ocean Avenue', 'A short drive along the rocky coast past Spouting Rock, Blowing Cave and Walker’s Point, the Bush family summer home.'),
               ('Goose Rocks Beach', 'A wide, quiet beach about 15 minutes north. Check parking rules in summer.'),
               ('Seashore Trolley Museum', 'The world’s first and largest electric railway museum, with rides on restored trolleys.', 'https://trolleymuseum.org/', 'Museum information'),
               ('Lighthouses', 'Goat Island Light offshore, and the much-photographed Nubble Light in York, about 30 minutes south.')]),
    spa=dict(title='The spa at The White Barn Inn', body='The inn’s spa offers couples treatments in a quiet setting a short walk from the village.'),
    events=dict(url='https://gokennebunks.com/', button='Browse Kennebunkport events',
        cards=[('June–September', 'Summer on the coast', 'Lobster shacks open, beaches and boat trips. Book early.'),
               ('Early October', 'Fall color', 'Crisp days and fewer crowds.'),
               ('December', 'Christmas Prelude', 'The village’s much-loved holiday festival.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: the village, the coast and two memorable dinners. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & the village', [('Arrival', 'Land at KSFM, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk Dock Square.'), ('Evening', 'Dinner at Cape Arundel Inn.')]),
              ('SAT', 'The coast', [('Morning', 'Drive Ocean Avenue and walk Goose Rocks Beach.'), ('Afternoon', 'A lobster roll at The Clam Shack, then the spa.'), ('Evening', 'Dinner at The White Barn Inn.')]),
              ('SUN', 'An easy departure', [('Morning', 'A drive to Nubble Light, or the trolley museum.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Coastal fog often lifts by late morning.')])]),
    know=[('Book in this order', 'Lodging and a car first, then dinners.'),
          ('Fuel stop', 'Plan a fuel stop for most piston aircraft.'),
          ('Seasons', 'Many places close from late fall to spring.'),
          ('Coastal weather', 'Fog and low clouds are common in summer. Keep a backup day.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
