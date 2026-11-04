"""Generate docs/ocean-city/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='ocean-city', name='Ocean City & Berlin', state='Maryland', number=86, reviewed=None,
    airport='KOXB', nm=334, flight_time='~2 hr 28 <small>min</small>', style='Rental car or rideshare',
    place='Ocean City, Maryland',
    description='A curated Ocean City getaway for GA pilots and their partners, from KMYR to KOXB. A classic boardwalk beach town, bayside sunsets, Assateague’s wild horses and charming Berlin, “America’s Coolest Small Town.”',
    lede='A classic boardwalk, bayside sunsets and wild horses.',
    intro='Ocean City is Maryland’s classic beach town, with a three-mile boardwalk, Thrasher’s fries and sunsets over the bay. Pair it with a night in Berlin, a small historic town a few miles inland, and a morning at Assateague Island, where wild horses roam the dunes.',
    pills=['Beach & boardwalk', 'Wild horses', 'Small-town inn'],
    flight=dict(
        title='Land by the bay.',
        intro='KOXB, Ocean City Municipal Airport, is a non-towered field on the mainland a few minutes from the beach and about 10 minutes from Berlin.',
        fbo=('Ocean City Municipal Airport', 'Ocean City Municipal Airport, Berlin, MD', '410-213-2471'),
        notes=['The airport runs its own fuel and services. Confirm hours, fees and rental cars. No live fuel price is shown.',
               'Summer weekends are busy with banner-tow and sightseeing traffic. About 335 nm from Myrtle Beach.'],
        around_title='A car for the coast.',
        around='The boardwalk is walkable, and a bus runs along Coastal Highway; a car covers Berlin and Assateague.'),
    stay=dict(title='Oceanfront or a historic small-town inn.', intro='Rates and availability need travel dates. Summer books early.',
        cards=[('Oceanfront · Retro', 'SeaLoft Oceanfront Hotel', 'A remodeled oceanfront hotel with a surf-town feel.', 'https://www.sealoftoceanfronthotel.com/'),
               ('Oceanfront · Classic', 'Dunes Manor Hotel', 'A Victorian-style oceanfront hotel with afternoon tea.', 'https://www.dunesmanor.com/'),
               ('Berlin · Since 1895', 'The Atlantic Hotel', 'A restored Victorian hotel on Main Street in Berlin.', 'https://www.atlantichotel.com/')]),
    eat=dict(title='Bayside sunsets and boardwalk fries.', intro='Reserve summer weekend dinners.',
        cards=[('Friday dinner · Bayside', 'Fager’s Island', 'A bayfront restaurant famous for sunsets set to the “1812 Overture.”', 'https://www.fagers.com/'),
               ('Saturday dinner · Bayside', 'The Hobbit', 'A long-time bayside restaurant with sunset views.', 'https://www.thehobbitrestaurant.com/'),
               ('Evening · Bayside', 'Seacrets', 'A Jamaican-themed waterfront bar and restaurant with live music.', 'https://www.seacrets.com/')]),
    explore=dict(title='Boardwalk, horses and Berlin.', intro='Beach mornings, bay evenings.',
        items=[('The boardwalk', 'Three miles of fries, saltwater taffy and ocean views.', 'https://www.ococean.com/', 'Ocean City'),
               ('Assateague Island National Seashore', 'Wild horses, quiet beaches and bay kayaking.', 'https://www.nps.gov/asis/', 'Seashore'),
               ('Ocean City Life-Saving Station Museum', 'Local history at the south end of the boardwalk.', 'https://www.ocmuseum.org/', 'Museum'),
               ('Berlin', 'Antique shops, cafés and the Atlantic Hotel on Main Street.', 'https://www.atlantichotel.com/', 'Berlin')]),
    events=dict(url='https://www.ococean.com/', button='Browse Ocean City events',
        cards=[('September', 'Sunfest', 'A fall festival with music and food.', 'https://www.ococean.com/', 'Ocean City'),
               ('Spring & fall', 'Shoulder seasons', 'Warm days and fewer crowds.'),
               ('Summer', 'Peak season', 'Busy and lively; book everything early.')]),
    itinerary=dict(intro='A sample weekend: beach, horses and Berlin. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & the boardwalk', [('Arrival', 'Land at KOXB, subject to weather and your actual flight plan.'), ('Afternoon', 'The beach and boardwalk.'), ('Evening', 'Sunset dinner at Fager’s Island.')]),
              ('DAY 2', 'Assateague & Berlin', [('Morning', 'Wild horses at Assateague.'), ('Afternoon', 'Wander Berlin’s Main Street.'), ('Evening', 'Dinner at The Hobbit.')]),
              ('DAY 3', 'Beach & home', [('Morning', 'A beach walk.'), ('Before leaving', 'Allow time at the airport.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then dinners.'),
          ('Traffic', 'Watch for banner-tow aircraft along the beach.'),
          ('Wild horses', 'Stay at least 40 feet away; they bite and kick.'),
          ('Best seasons', 'June and September.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
