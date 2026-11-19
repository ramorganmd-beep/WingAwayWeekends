"""Add a "Best for kids" box to family guides, just before the flight section.

Usage: python3 tools/guides/kids.py docs/<slug>/index.html [...]
Idempotent (replaces the block between wa-kids markers). Guides not in KIDS are left without a box.
Facts in KIDS are checked by hand; airport notes come from the airport listing, not from memory.
"""
import re, sys
from pathlib import Path
START, END = '<!--wa-kids-->', '<!--/wa-kids-->'
BLOCK = re.compile(r'\n?' + re.escape(START) + '.*?' + re.escape(END), re.S)
KIDS = {
    'mackinac': dict(
        ages='3 to 12',
        why='No cars on the island: kids can bike, ride in a horse-drawn carriage and walk everywhere.',
        top=['Bike the flat eight-mile road around the island; rent bikes, trailers and tag-alongs in town.',
             'Fort Mackinac, with soldiers in period uniform and cannon and rifle firings through the day in season.',
             'A horse-drawn carriage tour, and watching the fudge being made on the marble slabs in the shops.'],
        airport='KMCD has a 3,501 ft runway, no fuel and no FBO, and a landing fee. Arrive with fuel for the return, and arrange the horse-drawn taxi into town ahead of time.'),
    'traverse-city': dict(
        ages='4 to 12',
        why='Warm freshwater beaches with no salt or sharks, and a giant sand dune to run down.',
        top=['The Dune Climb at Sleeping Bear Dunes: up the sand, then roll or run back down.',
             'A beach afternoon on Grand Traverse Bay at Clinch Park, right downtown.',
             'Cherry picking at a local orchard in July, around the National Cherry Festival.'],
        airport='KTVC is a towered airline airport with a 7,016 ft runway and a landing fee. Avflight is the FBO. Summer weekends are busy.'),
    'wisconsin-dells': dict(
        ages='3 to 12',
        why='The self-styled Waterpark Capital of the World, with indoor waterparks that make it a year-round, rain-or-shine trip.',
        top=['An indoor waterpark resort, open all year.',
             'The Original Wisconsin Ducks: an amphibious tour that drives straight into the river.',
             'A swim and an easy hike at Devil’s Lake State Park.'],
        airport='KDLL is non-towered with a 5,010 ft main runway. Spring City Aviation (608-356-2270) is the FBO.'),
    'branson': dict(
        ages='4 to 12',
        why='Silver Dollar City, a lake and live family shows, all within a short drive.',
        top=['Silver Dollar City: an 1880s-themed park with coasters, water rides and craftsmen at work.',
             'A swim or a boat day on Table Rock Lake.',
             'The Lost Canyon cave and nature trail by cart at Top of the Rock.'],
        airport='KBBG, Branson Airport, is towered with a 7,140 ft runway. Allow a 20 to 30 minute drive into town on hilly roads.'),
    'smoky-mountains': dict(
        ages='4 to 12',
        why='Dollywood, cabins with room for everyone and black bears in the national park.',
        top=['Dollywood: coasters, a water park in summer and areas built for younger kids.',
             'The Cades Cove loop at dawn or dusk to look for deer, turkeys and black bears.',
             'Ripley’s Aquarium of the Smokies in Gatlinburg on a rainy day.'],
        airport='KGKT is non-towered with a 5,506 ft runway in mountain terrain. Its instrument approaches (RNAV and VOR/DME) serve runway 10 only, so plan an alternate in low weather. The airport runs the FBO (865-453-8393).'),
    'williamsburg': dict(
        ages='5 to 12',
        why='History kids can touch: costumed interpreters, ships to climb aboard and a big theme park nearby.',
        top=['Colonial Williamsburg: talk with the townspeople and catch the fife and drum corps.',
             'Jamestown Settlement: board the replica ships and explore the fort.',
             'Busch Gardens Williamsburg, plus Water Country USA in summer.'],
        airport='KJGG has a short 3,204 ft runway, no tower and a landing fee, and its instrument approaches are circling only. Check your aircraft’s performance, or use Newport News (KPHF) as a backup.'),
    'hershey': dict(
        ages='3 to 12',
        why='A whole town built around chocolate, with rides sized for every height.',
        top=['Hersheypark, with rides grouped by height so little ones always have something to do.',
             'The free chocolate tour ride at Hershey’s Chocolate World.',
             'ZooAmerica, a small zoo of North American animals next to the park.'],
        airport='KCXY, Capital City, is towered with a 5,000 ft runway, close to Harrisburg International’s airspace. Skyport Aviation (717-525-9999) is the FBO.'),
    'bar-harbor': dict(
        ages='5 to 12',
        why='Tide pools, flat carriage roads and short hikes with big views.',
        top=['Walk to Bar Island at low tide and look for crabs and sea stars in the pools.',
             'Bike the flat, car-free carriage roads in Acadia.',
             'Popovers at Jordan Pond House, and the Junior Ranger program at the park.'],
        airport='KBHB is non-towered with a 5,200 ft runway and a landing fee. Coastal fog is common in summer mornings. Modern Aviation (207-667-5534) is the FBO.'),
    'chattanooga': dict(
        ages='3 to 12',
        why='A walkable riverfront packed with things for kids, close together.',
        top=['The Tennessee Aquarium: river and ocean buildings, penguins and a butterfly garden.',
             'The Creative Discovery Museum, a hands-on children’s museum downtown.',
             'Ruby Falls, an underground waterfall inside Lookout Mountain.'],
        airport='KCHA is a towered airline airport with a 7,400 ft runway.'),
    'destin': dict(
        ages='2 to 10',
        why='Calm, clear water and soft white sand, with almost nothing to plan.',
        top=['A beach day at Henderson Beach State Park.',
             'A dolphin cruise from the harbor.',
             'The free Air Force Armament Museum, with aircraft outside to walk around.'],
        airport='KDTS is towered with a 5,001 ft runway, surrounded by Eglin military airspace. Check restricted areas and NOTAMs.'),
    'monterey-carmel': dict(
        ages='3 to 12',
        why='One of the best aquariums anywhere, and sea otters you can watch from shore.',
        top=['The Monterey Bay Aquarium: plan at least half a day.',
             'Rent a surrey or bikes on the waterfront trail along Cannery Row and look for sea otters.',
             'Tide pools at Point Lobos at low tide.'],
        airport='KMRY is a towered airline airport with a 7,175 ft runway. Summer fog and low clouds are common; plan late-morning arrivals.'),
    'colorado-springs': dict(
        ages='5 to 12',
        why='Big outdoors and a mountain zoo, with a train to the top of a 14,000-foot peak.',
        top=['Cheyenne Mountain Zoo on the mountainside, known for feeding the giraffes.',
             'Scramble around the red rocks at Garden of the Gods.',
             'The Pikes Peak Cog Railway to 14,115 ft: dress warmly and watch young kids for altitude sickness.'],
        airport='KCOS sits at 6,187 ft. Expect high density altitude on warm days and check your takeoff performance. It is a towered airline airport with long runways and a landing fee.'),
    'san-antonio': dict(
        ages='3 to 12',
        why='Boat rides through the middle of town and two big kid stops.',
        top=['A narrated river barge ride on the River Walk.',
             'The DoSeum, San Antonio’s hands-on children’s museum.',
             'The San Antonio Zoo.'],
        airport='KSSF, Stinson, is towered with a 5,000 ft runway, under San Antonio’s Class C airspace.'),
    'carlsbad': dict(
        ages='3 to 12',
        why='LEGOLAND is built for exactly this age, and the beach is minutes away.',
        top=['LEGOLAND California and Miniland USA.',
             'The SEA LIFE Aquarium at the park.',
             'Carlsbad State Beach, and the Flower Fields in spring.'],
        airport='KCRQ is towered with a 4,897 ft runway and a landing fee. A morning marine layer is common in late spring and early summer.'),
    'space-coast': dict(
        ages='5 to 12',
        why='Real rockets, a warbird museum on the field and, with luck, a launch.',
        top=['Kennedy Space Center Visitor Complex: Space Shuttle Atlantis and the Saturn V.',
             'The Valiant Air Command Warbird Museum, right on the airport.',
             'Black Point Wildlife Drive to spot alligators and birds, then the beach.'],
        airport='KTIX is towered with a 7,319 ft runway. Launches bring temporary flight restrictions; check NOTAMs and TFRs.'),
}
def block(k):
    d = KIDS[k]
    tops = ''.join(f'<li>{t}</li>' for t in d['top'])
    return (START + '<section id="kids" style="padding-top:0"><div style="background:#eef5f9;border:1px solid #c9dde8;border-radius:3px;padding:20px 22px">'
            '<span class="eyebrow">Flying with children</span><h2 style="margin:6px 0 8px">Best for kids</h2>'
            f'<p style="margin:0 0 10px"><b>Best ages: {d["ages"]}.</b> {d["why"]}</p>'
            f'<p style="margin:0 0 4px;font-weight:700">Top three for kids</p><ol style="line-height:1.6;margin:0 0 10px;padding-left:22px;list-style:decimal">{tops}</ol>'
            f'<p style="margin:0;font-size:15px"><b>At the airport:</b> {d["airport"]}</p></div></section>' + END)
for path in map(Path, sys.argv[1:]):
    k = path.parent.name; s = BLOCK.sub('', path.read_text())
    if k in KIDS:
        i = s.find('<section id="flight"')
        s = s[:i] + block(k) + '\n' + s[i:]
    path.write_text(s)
