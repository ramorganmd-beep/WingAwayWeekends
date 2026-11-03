"""Generate docs/marthas-vineyard/index.html (Martha's Vineyard, Massachusetts)."""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from simple_guide import build  # noqa: E402

GUIDE = dict(
    slug='marthas-vineyard', name='Martha’s Vineyard', state='Massachusetts', number=43, reviewed='November 3, 2026',
    airport='KMVY', nm=609, flight_time='~4 hr 19 <small>min</small>', style='Bikes, buses + taxis',
    place='Martha’s Vineyard, Massachusetts',
    description='A curated two-night Martha’s Vineyard getaway for GA pilots and their partners, from KMYR to KMVY. Edgartown’s captains’ houses, Oak Bluffs’ gingerbread cottages, the Aquinnah cliffs and Menemsha sunsets.',
    lede='Captains’ houses, gingerbread cottages and island sunsets.',
    intro='Seven miles off Cape Cod, Martha’s Vineyard is a big, varied island of harbor towns, farms and beaches. Stroll Edgartown’s white captains’ houses, ride the oldest carousel in the country in Oak Bluffs, see the clay cliffs at Aquinnah and eat lobster on the dock at Menemsha as the sun goes down.',
    pills=['Island towns', 'Beaches & cliffs', 'Sunsets'],
    flight=dict(
        title='Land in the middle of the island.',
        intro='KMVY, Martha’s Vineyard Airport, is a towered airport in the middle of the island, about 15 minutes from Edgartown, Oak Bluffs and Vineyard Haven.',
        fbo=('Martha’s Vineyard Airport FBO', '71 Airport Road, Vineyard Haven, MA 02568', '508-693-7022'),
        notes=['Summer is very busy; ask the FBO about parking availability, fees and hours well ahead. No live fuel price is shown.',
               'It is a short hop over water from Cape Cod, and fog can close the island for hours, especially in late spring and early summer. Plan a mainland alternate, carry safety gear and expect a fuel stop on the way.'],
        around_title='Leave the car behind.',
        around='Island buses, taxis and bike paths link the towns. Rent bikes in Edgartown or Oak Bluffs.'),
    stay=dict(title='Edgartown elegance or harbor views.', intro='Rates and availability need travel dates.',
        cards=[('Edgartown · Historic', 'The Charlotte Inn', 'An intimate, antique-filled inn in a cluster of 19th-century houses in Edgartown.', 'https://thecharlotteinn.com/'),
               ('Edgartown · Harborfront', 'Harbor View Hotel', 'A classic 1891 hotel with a long porch overlooking Edgartown Harbor and the lighthouse.', 'https://harborviewhotel.com/'),
               ('Katama · Resort', 'Winnetu Oceanside Resort', 'A relaxed resort near South Beach, outside Edgartown.', 'https://www.winnetu.com/')]),
    eat=dict(title='Two dinners. One sunset lobster.', intro='Reserve summer dinners well ahead.',
        cards=[('Friday dinner · Edgartown', 'Atria', 'New American cooking in an 18th-century sea captain’s house.', 'https://www.atriamv.com/'),
               ('Saturday dinner · French', 'l’étoile', 'Refined French cooking in Edgartown, one of the island’s special-occasion tables.', 'https://www.letoile.net/'),
               ('Sunset · Menemsha', 'Larsen’s Fish Market', 'Lobster and oysters on the dock in the fishing village of Menemsha. Stay for the sunset.', 'https://www.larsensfishmarket.com/')]),
    explore=dict(title='Towns, cliffs and beaches.', intro='Each town has its own character. Try to see three.',
        items=[('Edgartown', 'White captains’ houses, the harbor and Edgartown Lighthouse.'),
               ('Oak Bluffs', 'Hundreds of colorful gingerbread cottages and the Flying Horses Carousel, the oldest operating platform carousel in the country.', 'https://vineyardtrust.org/', 'Flying Horses Carousel'),
               ('Aquinnah Cliffs', 'Dramatic clay cliffs and the Gay Head Lighthouse at the island’s western tip.'),
               ('Menemsha', 'A working fishing village famous for its sunsets.'),
               ('Martha’s Vineyard Museum', 'Island history in a restored 1895 hospital in Vineyard Haven.', 'https://mvmuseum.org/', 'Museum information')]),
    events=dict(url='https://www.mvy.com/', button='Browse Martha’s Vineyard events',
        cards=[('August', 'Grand Illumination', 'Oak Bluffs’ cottages lit with paper lanterns for one evening.'),
               ('August', 'Agricultural Fair', 'A classic island fair in West Tisbury.'),
               ('September–October', 'Quieter season', 'Warm water, easier reservations and fewer crowds.')]),
    itinerary=dict(intro='A sample Friday–Sunday weekend: three towns, the cliffs and a sunset on the dock. No bookings or availability confirmed.',
        days=[('FRI', 'Arrive & Edgartown', [('Arrival', 'Land at KMVY, subject to weather, your fuel stop and your actual flight plan.'), ('Afternoon', 'Check in and walk to Edgartown Lighthouse.'), ('Evening', 'Dinner at Atria.')]),
              ('SAT', 'Up-island', [('Morning', 'Oak Bluffs’ cottages and the carousel.'), ('Afternoon', 'The Aquinnah Cliffs.'), ('Evening', 'Sunset lobster at Larsen’s in Menemsha, or dinner at l’étoile.')]),
              ('SUN', 'An easy departure', [('Morning', 'A bike ride to South Beach, or the museum.'), ('Before leaving', 'Allow time at the FBO; summer is busy.'), ('Fly home', 'Island fog can delay departures. Keep the day flexible.')])]),
    know=[('Book in this order', 'FBO parking and lodging first, then dinners.'),
          ('Over water', 'A short stretch of open water from Cape Cod. Brief safety gear.'),
          ('Fog', 'Fog can close the island for hours. Have a mainland alternate and a backup day.'),
          ('Seasons', 'Many places close from late fall to spring. Check opening dates.')])

if __name__ == '__main__':
    build(GUIDE, sys.argv[1])
