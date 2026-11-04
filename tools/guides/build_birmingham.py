"""Generate docs/birmingham/index.html (Birmingham, Alabama)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='birmingham', name='Birmingham', state='Alabama', number=77, reviewed=None,
    airport='KBHM', nm=391, flight_time='~2 hr 51 <small>min</small>', style='Rental car or rideshare',
    place='Birmingham, Alabama',
    description='A curated Birmingham getaway for GA pilots and their partners, from KMYR to KBHM. Award-winning restaurants, the Civil Rights District, the Southern Museum of Flight, Barber’s motorcycle museum and Vulcan’s view.',
    lede='Award-winning dining, civil rights history and a flight museum by the runway.',
    intro='Birmingham has one of the South’s best restaurant scenes and some of its most important history. Walk the Civil Rights District and the 16th Street Baptist Church, visit the Southern Museum of Flight next to the airport, see the world’s largest motorcycle collection at Barber, watch the sunset from Vulcan Park and book dinner at Bottega or Automatic Seafood.',
    pills=['Award-winning dining', 'Civil rights history', 'Aviation museum'],
    flight=dict(
        title='Land at Birmingham.',
        intro='KBHM, Birmingham–Shuttlesworth International, is a towered airport about 10 minutes from downtown. The Southern Museum of Flight is beside the field.',
        fbo=('Atlantic Aviation', 'Birmingham–Shuttlesworth International Airport, Birmingham, AL', '205-849-5520'),
        notes=['Million Air Birmingham is a second FBO on the field. Confirm hours, fees and rental cars. No live fuel price is shown.',
               'About 390 nm from Myrtle Beach. Summer brings afternoon storms.'],
        around_title='Rent a car.',
        around='Downtown is compact, but Barber, Vulcan and Mountain Brook need a car or rideshare.'),
    stay=dict(title='A historic downtown hotel or a Mountain Brook retreat.', intro='Rates and availability need travel dates.',
        cards=[('Downtown · Historic', 'Elyton Hotel', 'A restored 1909 tower downtown with a rooftop bar.', 'https://www.elytonhotel.com/'),
               ('Mountain Brook · Spa', 'Grand Bohemian Hotel Mountain Brook', 'An art-filled hotel with a spa and a rooftop restaurant.', 'https://www.kesslercollection.com/grand-bohemian-hotel-mountain-brook/'),
               ('Countryside · Resort', 'The Inn at Pursell Farms', 'A golf and spa resort about an hour away, for a quieter extra night.', 'https://www.pursellfarms.com/')]),
    eat=dict(title='A celebrated restaurant city.', intro='Reserve weekend dinners well ahead.',
        cards=[('Friday dinner · Italian-Southern', 'Bottega', 'A Southside institution from chef Frank Stitt.', 'https://www.bottegarestaurant.com/'),
               ('Lunch · French bistro', 'Chez Fonfon', 'Stitt’s casual French bistro, with a boules court.', 'https://www.fonfonbham.com/'),
               ('Saturday dinner · Seafood', 'Automatic Seafood and Oysters', 'James Beard Award–winning Gulf seafood.', 'https://www.automaticseafood.com/')]),
    explore=dict(title='History, flight and a view.', intro='Mix one heavy subject with lighter outings.',
        items=[('Birmingham Civil Rights Institute', 'The movement’s history, across from the 16th Street Baptist Church and Kelly Ingram Park.', 'https://www.bcri.org/', 'BCRI'),
               ('Southern Museum of Flight', 'Aircraft from the early days to the Cold War, beside the airport.', 'https://www.southernmuseumofflight.org/', 'Museum'),
               ('Barber Vintage Motorsports Museum', 'The world’s largest motorcycle collection, beside a racetrack.', 'https://www.barbermuseum.org/', 'Museum'),
               ('Vulcan Park and Museum', 'The giant iron statue and the best view of the city.', 'https://www.visitvulcan.com/', 'Vulcan'),
               ('Sloss Furnaces', 'A National Historic Landmark iron works.', 'https://www.slossfurnaces.org/', 'Sloss')]),
    spa=dict(title='The spa at Grand Bohemian Mountain Brook', body='The hotel’s spa offers couples treatments.'),
    events=dict(url='https://www.inbirmingham.com/', button='Browse Birmingham events',
        cards=[('Spring', 'Barber Motorsports Park races', 'Check the racing calendar at the park.'),
               ('September', 'Sidewalk Film Festival', 'Films in theaters across downtown.'),
               ('Spring & fall', 'Best seasons', 'Mild weather for walking.')]),
    itinerary=dict(intro='A sample weekend: history, flight and dinner. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & flight', [('Arrival', 'Land at KBHM, subject to weather and your actual flight plan.'), ('Afternoon', 'The Southern Museum of Flight, beside the field.'), ('Evening', 'Dinner at Bottega.')]),
              ('DAY 2', 'History & the view', [('Morning', 'The Civil Rights Institute and 16th Street Baptist Church.'), ('Afternoon', 'Lunch at Chez Fonfon, then Vulcan Park.'), ('Evening', 'Dinner at Automatic Seafood.')]),
              ('DAY 3', 'Motorcycles & home', [('Morning', 'Barber Vintage Motorsports Museum.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Summer storms build in the afternoon; leave early.')])]),
    know=[('Book in this order', 'Lodging first, then dinners.'),
          ('Museum hours', 'Several museums close one or two days a week; check before you go.'),
          ('Dining', 'Top restaurants book up on weekends.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
