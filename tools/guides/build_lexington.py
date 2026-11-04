"""Generate docs/lexington/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='lexington', name='Lexington & Horse Country', state='Kentucky', number=90, reviewed='November 4, 2026',
    airport='KLEX', nm=380, flight_time='~2 hr 47 <small>min</small>', style='Rental car',
    place='Lexington, Kentucky',
    description='A curated Lexington getaway for GA pilots and their partners, from KMYR to KLEX. The Horse Capital of the World: Keeneland across from the airport, thoroughbred farms, bourbon distilleries and Shaker Village.',
    lede='Keeneland, horse farms and bourbon.',
    intro='Lexington’s airport sits across the road from Keeneland, one of the world’s most beautiful racetracks. Watch the morning workouts, visit retired champions at Old Friends, tour Woodford Reserve, drive the stone-fenced lanes of horse country, spend a day at Shaker Village and have dinner at Holly Hill Inn.',
    pills=['Horse racing', 'Bourbon', 'Horse farms'],
    flight=dict(
        title='Land across from Keeneland.',
        intro='KLEX, Blue Grass Airport, is a towered airport directly across Versailles Road from Keeneland and about 15 minutes from downtown.',
        fbo=('Signature Aviation', 'Blue Grass Airport, Lexington, KY', '859-255-7724'),
        notes=['Confirm FBO hours, fees and rental cars; race meets bring heavy traffic. No live fuel price is shown.',
               'About 380 nm from Myrtle Beach, over the Appalachians; check weather over the mountains.'],
        around_title='Rent a car.',
        around='Horse farms, distilleries and Shaker Village are spread across the countryside.'),
    stay=dict(title='Art hotel, historic inn or the countryside.', intro='Rates and availability need travel dates. Race meets book early.',
        cards=[('Downtown · Art hotel', '21c Museum Hotel Lexington', 'A hotel with a contemporary art museum inside.', 'https://www.21cmuseumhotels.com/lexington/'),
               ('Downtown · Historic', 'Gratz Park Inn', 'A boutique inn in a historic neighborhood.', 'https://www.gratzparkinn.com/'),
               ('Countryside · Inn', 'Shaker Village of Pleasant Hill', 'Rooms in restored Shaker buildings, about 45 minutes away.', 'https://www.shakervillageky.org/')]),
    eat=dict(title='Bluegrass cooking.', intro='Reserve weekend dinners.',
        cards=[('Saturday dinner · Countryside', 'Holly Hill Inn', 'Southern cooking in an 1845 house in Midway.', 'https://www.hollyhillinn.com/'),
               ('Friday dinner · Downtown', 'Dudley’s on Short', 'A Lexington favorite downtown.', 'https://www.dudleysonshort.com/'),
               ('Dinner · Fine dining', 'Distilled', 'Upscale dining and bourbon downtown.', 'https://distilledonjefferson.com/')]),
    explore=dict(title='Horses and bourbon.', intro='Go early: the horses work in the morning.',
        items=[('Keeneland', 'Racing in April and October; morning workouts and the track kitchen most of the year.', 'https://www.keeneland.com/', 'Keeneland'),
               ('Old Friends Farm', 'A retirement farm for famous thoroughbreds.', 'https://www.oldfriendsequine.org/', 'Tours'),
               ('Kentucky Horse Park', 'A park and museum devoted to the horse.', 'https://kyhorsepark.com/', 'Horse Park'),
               ('Woodford Reserve', 'A historic distillery in horse country.', 'https://www.woodfordreserve.com/', 'Tours'),
               ('Shaker Village of Pleasant Hill', 'A restored Shaker community with trails and a riverboat.', 'https://www.shakervillageky.org/', 'Shaker Village')]),
    events=dict(url='https://www.visitlex.com/', button='Browse Lexington events',
        cards=[('April', 'Keeneland Spring Meet', 'Three weeks of racing.', 'https://www.keeneland.com/', 'Keeneland'),
               ('October', 'Keeneland Fall Meet', 'Racing with fall color.', 'https://www.keeneland.com/', 'Keeneland'),
               ('Spring & fall', 'Best seasons', 'Green pastures and foals in spring.')]),
    itinerary=dict(intro='A sample weekend: horses, bourbon and Shaker Village. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & Keeneland', [('Arrival', 'Land at KLEX, subject to weather and your actual flight plan.'), ('Afternoon', 'Keeneland, across the road.'), ('Evening', 'Dinner at Dudley’s.')]),
              ('DAY 2', 'Horse country', [('Morning', 'Old Friends Farm.'), ('Afternoon', 'Woodford Reserve.'), ('Evening', 'Dinner at Holly Hill Inn.')]),
              ('DAY 3', 'Shakers & home', [('Morning', 'Shaker Village.'), ('Before leaving', 'Allow time at the FBO.'), ('Fly home', 'Check weather over the mountains.')])]),
    know=[('Book in this order', 'Lodging first, then farm and distillery tours.'),
          ('Race meets', 'April and October bring crowds and higher rates.'),
          ('Bourbon', 'Plan a designated driver or a tour.'),
          ('Best seasons', 'Spring and fall.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
