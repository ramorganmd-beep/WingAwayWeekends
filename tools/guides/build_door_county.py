"""Generate docs/door-county/index.html (Door County, Wisconsin)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='door-county', name='Door County', state='Wisconsin', number=49, reviewed=None,
    airport='KSUE', nm=777, flight_time='~5 hr 26 <small>min</small>', style='Rental car',
    place='Door County, Wisconsin',
    description='A curated two-night Door County getaway for GA pilots and their partners, from KMYR to KSUE. A peninsula of harbor villages, cherry orchards, lighthouses, a fish boil and goats on a restaurant roof.',
    lede='Harbor villages, cherries and a fish boil.',
    intro='Door County is a long peninsula between Green Bay and Lake Michigan, lined with small harbor villages, orchards and 11 historic lighthouses. Drive the bay shore through Fish Creek and Ephraim, hike the bluffs of Peninsula State Park, watch a traditional fish boil boil over, and see the goats on the roof at Al Johnson’s.',
    pills=['Harbor villages', 'Lighthouses', 'Cherries & fish boils'],
    flight=dict(
        title='Land at the gateway to the peninsula.',
        intro='KSUE, Door County Cherryland Airport, is just outside Sturgeon Bay, about 30 minutes from Fish Creek and 45 from Ephraim and Sister Bay.',
        fbo=('Tailwind Flight Center', '3538 Park Drive, Sturgeon Bay, WI 54235', '920-746-2581'),
        notes=['Ask about rental cars, parking, fees and hours. No live fuel price is shown.',
               'Lake effect weather and fog are common, especially in spring and summer. About 780 nm from Myrtle Beach: plan a fuel stop and consider a third night. Review the sectional and current NOTAMs.'],
        around_title='You’ll want a car.',
        around='The villages are strung along Highway 42 on the bay side and Highway 57 on the lake side. Each is walkable once you park.'),
    stay=dict(title='A historic inn or a bay view.', intro='Rates and availability need travel dates; summer and fall fill early.',
        cards=[('Fish Creek · Since 1896', 'The White Gull Inn', 'A classic inn in Fish Creek, famous for its fish boils and its breakfast.', 'https://www.whitegullinn.com/'),
               ('Ephraim · Harbor', 'Eagle Harbor Inn', 'A grown-up inn a few minutes’ walk from Ephraim’s harbor and beach.', 'https://www.eagleharborinn.com/'),
               ('Fish Creek · Boutique', 'Whistling Swan', 'An 1887 boutique inn in the middle of Fish Creek.', 'https://www.whistlingswan.com/')]),
    eat=dict(title='A fish boil, a pizza and a famous roof.', intro='Reserve the fish boil ahead.',
        cards=[('Friday dinner · Tradition', 'Fish boil at The White Gull Inn', 'Whitefish and potatoes boiled over an open fire until the “boil over” flares up. A Door County tradition.', 'https://www.whitegullinn.com/'),
               ('Saturday dinner · Wood-fired', 'Wild Tomato', 'Wood-fired pizza and local beer in Fish Creek and Sister Bay.', 'https://wildtomatopizza.com/'),
               ('Breakfast or lunch · Sister Bay', 'Al Johnson’s Swedish Restaurant', 'Swedish pancakes, lingonberries and goats grazing on the sod roof.', 'https://aljohnsons.com/')]),
    explore=dict(title='Bluffs, lighthouses and orchards.', intro='Bay side one day, lake side the next.',
        items=[('Peninsula State Park', 'Bluffs, beaches, a lighthouse and a bike trail between Fish Creek and Ephraim.'),
               ('Cana Island Lighthouse', 'An 1869 lighthouse reached by a stone causeway on the lake side.'),
               ('Cave Point County Park', 'Limestone cliffs and sea caves where Lake Michigan waves crash in.'),
               ('Cherry orchards & farm markets', 'Pick cherries in July, or buy pies and jams year-round.', 'https://seaquistorchards.com/', 'Seaquist Orchards'),
               ('Washington Island', 'A car ferry across “Death’s Door” from the tip of the peninsula to a quiet island.')]),
    events=dict(url='https://www.doorcounty.com/', button='Browse Door County events',
        cards=[('July', 'Cherry harvest', 'Pick-your-own cherries and roadside pies.'),
               ('October', 'Fall Fest & color', 'Sister Bay’s Fall Fest and spectacular foliage.'),
               ('Summer', 'Peninsula Players', 'America’s oldest professional resident summer theater, in the woods near Fish Creek.')]),
    itinerary=dict(intro='A sample weekend: the bay villages, a fish boil and a lighthouse. A third night makes the long flight easier. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Fish Creek', [('Arrival', 'Land at KSUE, subject to weather, your fuel stop and your actual flight plan, and pick up the car.'), ('Afternoon', 'Drive up the bay shore to Fish Creek.'), ('Evening', 'The fish boil at The White Gull Inn.')]),
              ('SAT', 'The peninsula', [('Morning', 'Peninsula State Park by bike or on foot.'), ('Afternoon', 'Ephraim, Sister Bay and lunch at Al Johnson’s.'), ('Evening', 'Pizza at Wild Tomato.')]),
              ('SUN', 'The lake side & home', [('Morning', 'Cana Island Lighthouse and Cave Point.'), ('Before leaving', 'Return the car and allow time at the FBO.'), ('Fly home', 'Lake fog often lifts by late morning.')])]),
    know=[('Book in this order', 'Lodging and a car first, then the fish boil.'),
          ('Long flight', 'About 780 nm. Plan a fuel stop and consider a third night.'),
          ('Seasons', 'Many places are open May to October.'),
          ('Lake weather', 'Fog and lake-effect weather are common. Keep a backup day.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
