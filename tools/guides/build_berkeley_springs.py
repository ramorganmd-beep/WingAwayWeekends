"""Generate docs/berkeley-springs/index.html."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='berkeley-springs', name='Berkeley Springs', state='West Virginia', number=89, reviewed='November 4, 2026',
    airport='KMRB', nm=347, flight_time='~2 hr 33 <small>min</small>', style='Rental car',
    place='Berkeley Springs, West Virginia',
    description='A curated Berkeley Springs getaway for GA pilots and their partners, from KMYR to KMRB. “America’s first spa”: warm mineral springs George Washington bathed in, a historic inn, art galleries and the Cacapon mountains.',
    lede='America’s first spa, in a little mountain town.',
    intro='Berkeley Springs has drawn visitors to its warm mineral springs since George Washington’s day. Soak in the historic Roman bath house at the state park, stay at the Country Inn or a cabin at Coolfont, browse galleries in the old Ice House, take in the view from Panorama Overlook and hike at Cacapon Resort State Park.',
    pills=['Mineral springs spa', 'Small-town inns', 'Mountain views'],
    flight=dict(
        title='Land at Martinsburg.',
        intro='KMRB, Eastern West Virginia Regional Airport, is a towered field about 35 minutes from Berkeley Springs.',
        fbo=('Eastern WV Regional Airport FBO', 'Eastern West Virginia Regional Airport, Martinsburg, WV', '304-262-2507'),
        notes=['Confirm FBO hours, fees and rental cars. No live fuel price is shown.',
               'The DC Special Flight Rules Area lies to the east; check your route. About 345 nm from Myrtle Beach.'],
        around_title='Rent a car.',
        around='The town is walkable, but you need a car for the drive and for Cacapon.'),
    stay=dict(title='A historic inn or a woodland retreat.', intro='Rates and availability need travel dates.',
        cards=[('In town · Historic', 'The Country Inn of Berkeley Springs', 'A classic inn beside the state park, with a restaurant.', 'https://www.thecountryinnwv.com/'),
               ('Woods · Retreat', 'Coolfont', 'Cabins and lodging in the woods outside town.', 'https://www.coolfont.com/'),
               ('State park · Resort', 'Cacapon Resort State Park', 'A lodge with golf and trails in the mountains.', 'https://wvstateparks.com/parks/cacapon-resort-state-park/')]),
    eat=dict(title='Small-town dining.', intro='Reserve weekend dinners.',
        cards=[('Saturday dinner · Upscale', 'Lot 12 Public House', 'Seasonal cooking in a historic house.', 'https://www.lot12.com/'),
               ('Friday dinner · Whiskey bar', 'Proof on Washington', 'A restaurant and whiskey bar in town.', 'https://proofonwashington.com/'),
               ('Dinner · Classic', 'The Country Inn restaurant', 'Dinner at the inn.', 'https://www.thecountryinnwv.com/restaurant')]),
    explore=dict(title='Springs, galleries and views.', intro='A slow, restorative weekend.',
        items=[('Berkeley Springs State Park', 'Private soaks in the historic Roman baths.', 'https://wvstateparks.com/park/berkeley-springs-state-park/', 'Bath house'),
               ('The Ice House', 'Galleries and performances from the Morgan Arts Council.', 'https://www.macicehouse.org/', 'Ice House'),
               ('Panorama Overlook', 'A sweeping view over three states.', 'https://www.berkeleysprings.com/', 'Berkeley Springs'),
               ('Cacapon Resort State Park', 'Trails, a lake and golf.', 'https://wvstateparks.com/parks/cacapon-resort-state-park/', 'Cacapon')]),
    spa=dict(title='The Roman baths', body='Book a private soak in the state park’s historic Roman bath house, and look for massages at town spas.'),
    events=dict(url='https://www.berkeleysprings.com/', button='Browse Berkeley Springs events',
        cards=[('October', 'Apple Butter Festival', 'Apple butter cooked in copper kettles in town.', 'https://www.berkeleysprings.com/', 'Berkeley Springs'),
               ('February', 'Winter Festival of the Waters', 'A celebration of the springs.', 'https://www.berkeleysprings.com/', 'Berkeley Springs'),
               ('Fall', 'Best season', 'Mountain color and cool air.')]),
    itinerary=dict(intro='A sample weekend: a soak, galleries and a mountain view. No bookings or availability confirmed.',
        days=[('DAY 1', 'Arrive & settle in', [('Arrival', 'Land at KMRB, subject to weather and your actual flight plan.'), ('Afternoon', 'Drive to town and walk the park.'), ('Evening', 'Dinner at Proof on Washington.')]),
              ('DAY 2', 'Soak & galleries', [('Morning', 'A Roman bath soak.'), ('Afternoon', 'The Ice House and Panorama Overlook.'), ('Evening', 'Dinner at Lot 12.')]),
              ('DAY 3', 'Cacapon & home', [('Morning', 'A hike at Cacapon.'), ('Before leaving', 'Allow time for the drive to KMRB.'), ('Fly home', 'Leave before afternoon storms.')])]),
    know=[('Book in this order', 'Lodging and bath times first, then dinners.'),
          ('Airspace', 'Check the DC SFRA if your route goes east.'),
          ('Drive time', 'About 35 minutes from KMRB.'),
          ('Best seasons', 'Fall and spring.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
