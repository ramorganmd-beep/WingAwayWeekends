"""Generate docs/bar-harbor/index.html (Bar Harbor and Acadia National Park, Maine)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='bar-harbor', name='Bar Harbor & Acadia', state='Maine', number=32, reviewed='November 3, 2026',
    airport='KBHB', nm=811, flight_time='~5 hr 40 <small>min</small>', style='Rental car or shuttle',
    place='Bar Harbor & Acadia, Maine',
    description='A curated two-night Bar Harbor and Acadia National Park getaway for GA pilots and their partners, from KMYR to KBHB. Granite coast, Cadillac Mountain, carriage roads, lobster and popovers.',
    lede='Granite cliffs, lobster and the first sunrise.',
    intro='On Mount Desert Island, Acadia National Park’s granite mountains rise straight out of the Atlantic. Fly in over the islands, watch the sunrise from Cadillac Mountain, bike the old carriage roads, have popovers at Jordan Pond and a lobster dinner on the dock.',
    pills=['National park', 'Rocky coast', 'Lobster'],
    flight=dict(
        title='Land at the gateway to the island.',
        intro='KBHB, Hancock County–Bar Harbor, sits on the mainland in Trenton, about 20 minutes from downtown Bar Harbor.',
        fbo=('Modern Aviation · Bar Harbor', '112 Caruso Drive, Trenton, ME 04605', '207-667-5534', 'https://bhbairport.com/general.html'),
        notes=['Ask the FBO about rental cars, overnight parking and fees. No live fuel price is shown.',
               'This is a long trip, about 800 nm from Myrtle Beach; plan at least one fuel stop and consider making it a three-night weekend. Coastal fog is frequent in summer. Review the sectional and current NOTAMs.'],
        around_title='A car, then the park shuttle.',
        around='Rent a car for the weekend. In season, the free Island Explorer buses link Bar Harbor with the park’s trailheads and beaches.'),
    stay=dict(title='On the harbor or in town.', intro='Harborfront hotels and a gracious inn. Rates and availability need travel dates.',
        cards=[('Harborfront · Classic', 'Bar Harbor Inn', 'A long-running hotel on the water at the foot of Main Street, with a spa and the Reading Room restaurant.', 'https://barharborinn.com/'),
               ('Harborfront · Modern', 'West Street Hotel', 'An adults-oriented hotel overlooking Frenchman Bay, with a rooftop pool and a short walk to town.', 'https://www.opalcollection.com/west-street/'),
               ('Oceanfront · Inn', 'Balance Rock Inn', 'A gracious 1903 summer house on the Shore Path, with ocean views and a quiet garden.', 'https://www.balancerockinn.com/')]),
    eat=dict(title='Two dinners. One with popovers.', intro='Lobster, fine dining and a park tradition. Reserve summer dinners.',
        cards=[('Friday dinner · Downtown', 'Havana', 'Inventive Latin-inspired dining in downtown Bar Harbor, one of the town’s best tables.', 'https://www.havanamaine.com/'),
               ('Lunch · In the park', 'Jordan Pond House', 'Popovers and tea on the lawn above Jordan Pond, a park tradition since the 1890s. Seasonal.', 'https://jordanpondhouse.com/'),
               ('Saturday dinner · Lobster', 'Thurston’s Lobster Pound', 'A classic working-harbor lobster pound in Bernard, on the quiet side of the island. Seasonal.', 'https://www.thurstonforlobster.com/')]),
    explore=dict(title='Mountains that meet the sea.', intro='Start early. The park is busiest from late morning.',
        items=[('Cadillac Mountain', 'The highest point on the Atlantic coast of the U.S., and one of the first places in the country to see the sunrise. Vehicle reservations are required in season.', 'https://www.nps.gov/acad/', 'Park information'),
               ('Ocean Path & Thunder Hole', 'An easy walk along the granite shore from Sand Beach to Otter Cliff.'),
               ('The carriage roads', 'Forty-five miles of crushed-stone roads and stone bridges, closed to cars. Rent bikes in Bar Harbor.'),
               ('Jordan Pond Path', 'A flat loop around a clear mountain lake below the Bubbles.'),
               ('Bar Island at low tide', 'Walk across a gravel bar from town to Bar Island when the tide is out. Check the tide table.')]),
    spa=dict(title='The spa at Bar Harbor Inn', body='Bar Harbor Inn’s spa overlooks Frenchman Bay, an easy afternoon between hikes.'),
    events=dict(url='https://www.visitbarharbor.com/', button='Browse Bar Harbor events',
        cards=[('Late September', 'Acadia Night Sky Festival', 'Stargazing, talks and dark skies over the island.'),
               ('Early October', 'Fall color', 'The island turns gold and red; beautiful and busy.'),
               ('June–September', 'Whale watching', 'Whale-watch and puffin cruises leave from the Bar Harbor waterfront.')]),
    itinerary=dict(intro='A sample weekend: the park loop, the carriage roads and two Maine dinners. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & town', [('Arrival', 'Land at KBHB, subject to weather, your fuel stops and your actual flight plan, and pick up the car.'), ('Afternoon', 'Check in and walk the Shore Path.'), ('Evening', 'Dinner at Havana.')]),
              ('SAT', 'Acadia', [('Sunrise', 'Cadillac Mountain, with a vehicle reservation.'), ('Morning', 'Ocean Path to Thunder Hole, then popovers at Jordan Pond House.'), ('Afternoon & evening', 'Bike the carriage roads, then lobster at Thurston’s.')]),
              ('SUN', 'An easy departure', [('Morning', 'Bar Island at low tide, or a whale watch.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'A long trip home. Start early and let weather set the plan.')])]),
    know=[('Book in this order', 'Lodging and a car first, then the Cadillac reservation and dinners.'),
          ('Long flight', 'About 800 nm. Plan fuel stops and consider a third night.'),
          ('Seasons', 'Many restaurants and the Island Explorer run late spring to mid-October.'),
          ('Coastal fog', 'Summer fog is common. Keep a backup day.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
