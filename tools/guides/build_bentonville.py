"""Generate docs/bentonville/index.html (Bentonville and Crystal Bridges, Arkansas)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='bentonville', name='Bentonville & Crystal Bridges', state='Arkansas', number=53, reviewed='November 3, 2026',
    airport='KVBT', nm=768, flight_time='~5 hr 23 <small>min</small>', style='Bikes + short drives',
    place='Bentonville, Arkansas',
    description='A curated two-night Bentonville getaway for GA pilots and their partners, from KMYR to KVBT. Crystal Bridges Museum of American Art, the Momentary, forest trails, a lively square and coffee on the airfield.',
    lede='World-class art, forest trails and coffee on the ramp.',
    intro='Bentonville, home of Walmart, has become one of the country’s surprise art and outdoor towns. Walk the forest trails to Crystal Bridges Museum of American Art, see contemporary art at the Momentary, ride some of the best mountain-bike trails in the country, and have coffee at a café on the airport named for aviation pioneer Louise Thaden.',
    pills=['Crystal Bridges', 'Trails', 'Aviation history'],
    flight=dict(
        title='Land at Louise Thaden Field.',
        intro='KVBT, Bentonville Municipal–Louise M. Thaden Field, is a few minutes from downtown. It is named for the Bentonville-born pilot who won the first women’s air derby and the 1936 Bendix race.',
        fbo=('Legends Air Center', '2205 SW I Street, Bentonville, AR 72712', '479-254-0817'),
        notes=['Sources disagree on the FBO phone number, so confirm it. Ask about rental cars, bikes, parking and fees. Airship Coffee is on the field. No live fuel price is shown.',
               'Northwest Arkansas National (KXNA) and Razorback Approach are nearby. About 770 nm from Myrtle Beach: plan a fuel stop and consider a third night. Review the sectional and current NOTAMs.'],
        around_title='Bikes do most of the work.',
        around='Paved trails link the square, Crystal Bridges and the Momentary. Rent bikes downtown, or drive the short distances.'),
    stay=dict(title='An art hotel or a short ride away.', intro='Rates and availability need travel dates.',
        cards=[('Downtown · Art hotel', '21c Museum Hotel Bentonville', 'A boutique hotel with its own contemporary art galleries, a block from the square and the trail to Crystal Bridges.', 'https://www.21cmuseumhotels.com/bentonville/'),
               ('Explore more', 'Visit Bentonville', 'More hotels and rentals near the square and the trails.', 'https://www.visitbentonville.com/'),
               ('On the airfield · Coffee', 'Airship Coffee at Thaden Field', 'Not a hotel, but a favorite first stop: a café on the airport with views of the runway.', 'https://www.airshipcoffee.com/')]),
    eat=dict(title='Two dinners. One in a former church.', intro='Reserve weekend dinners.',
        cards=[('Friday dinner · A restored church', 'The Preacher’s Son', 'Gluten-free, farm-driven dining in a restored 1900s stone church.', 'https://www.thepreachersson.com/'),
               ('Saturday dinner · Southern', 'Tusk & Trotter', 'A downtown American brasserie known for Southern and smoked dishes.', 'https://www.tuskandtrotter.com/'),
               ('Lunch · At the museum', 'Crystal Bridges', 'The museum’s restaurant overlooks the ponds and bridges.', 'https://crystalbridges.org/')]),
    explore=dict(title='Art, trails and the square.', intro='Allow half a day for Crystal Bridges.',
        items=[('Crystal Bridges Museum of American Art', 'A celebrated museum of five centuries of American art, set over ponds in a forested ravine. Free general admission.', 'https://crystalbridges.org/', 'Museum information'),
               ('The Momentary', 'A contemporary art and performance space in a former cheese factory.', 'https://themomentary.org/', 'Visit information'),
               ('Trails', 'Miles of paved and mountain-bike trails through the forest, right from downtown.'),
               ('The square & the Walmart Museum', 'A lively town square and Sam Walton’s original five-and-dime.'),
               ('Thaden Field', 'Coffee and airplanes at the airport named for one of America’s great early aviators.')]),
    events=dict(url='https://www.visitbentonville.com/', button='Browse Bentonville events',
        cards=[('Spring & fall', 'Trail season', 'The best weather for bikes and forest walks.'),
               ('Year-round', 'Museum exhibitions', 'Crystal Bridges and the Momentary change their shows through the year.'),
               ('Summer', 'First Fridays', 'Monthly street parties on the square.')]),
    itinerary=dict(intro='A sample weekend: Crystal Bridges, trails and two good dinners. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & coffee', [('Arrival', 'Land at KVBT, subject to weather, your fuel stop and your actual flight plan; coffee at Airship.'), ('Afternoon', 'Check in and walk the square.'), ('Evening', 'Dinner at The Preacher’s Son.')]),
              ('SAT', 'Art & trails', [('Morning', 'Walk or bike the trail to Crystal Bridges.'), ('Afternoon', 'Lunch at the museum, then the Momentary.'), ('Evening', 'Dinner at Tusk & Trotter.')]),
              ('SUN', 'An easy departure', [('Morning', 'A bike ride on the forest trails.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Let weather and your flight plan set the departure.')])]),
    know=[('Book in this order', 'Lodging first, then dinners and bikes.'),
          ('Long flight', 'About 770 nm. Plan a fuel stop and consider a third night.'),
          ('Museum days', 'Crystal Bridges is closed some days of the week; check hours.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
