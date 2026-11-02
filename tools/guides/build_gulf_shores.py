"""Generate docs/gulf-shores/index.html (Gulf Shores and Orange Beach, Alabama)."""
import json
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from guide_helpers import card, head, explore, day, page_start, page_end, fbo, know  # noqa: E402

OUT = sys.argv[1]
PHOTO = json.load(open(__file__.rsplit("/", 1)[0] + '/photos.json'))['gulf-shores']
NAV = [('flight', 'Fly & arrive'), ('stay', 'Stay'), ('eat', 'Eat'), ('explore', 'Explore'),
       ('events', 'Events'), ('itinerary', 'Itinerary')]
P = [page_start(
    slug='gulf-shores', name='Gulf Shores', state='Alabama', number=16,
    description='A curated two-night Gulf Shores and Orange Beach getaway for GA pilots and their partners, from KMYR to KJKA. Sugar-white beaches, Gulf seafood, Gulf State Park and the National Naval Aviation Museum.',
    lede='White sand, Gulf seafood, naval aviation.',
    intro='Alabama’s small stretch of coast has some of the whitest sand on the Gulf. Land minutes from the beach, bike the trails of Gulf State Park, eat shrimp straight off the boats, and save a morning for the National Naval Aviation Museum, an easy drive away in Pensacola.',
    pills=['Beaches', 'Gulf seafood', 'Naval aviation'],
    photo=PHOTO['slug'], widths=PHOTO['widths'], alt=PHOTO['alt'], img_w=PHOTO['w'], img_h=PHOTO['h'],
    caption=PHOTO['caption'], airport='KJKA', nm=489, flight_time='~3 hr 31 <small>min</small>',
    style='Crew car or rental car', nav=NAV)]

P.append('<section id="flight">' + head('01', 'Aviation & getting around', 'Land a few minutes from the sand.',
    'KJKA, Jack Edwards National in Gulf Shores, sits just north of the beach and Gulf State Park.') +
    '<div class="arrival-grid"><div class="arrival-main"><h3>The FBO</h3>' +
    fbo('Gulf Air Center', '3190 Airport Drive, Gulf Shores, AL 36542', '251-968-5200') +
    '<p class="note">Gulf Air Center lists crew cars and rental cars; pilots also report rental delivery to the FBO from local agencies. Ask about two-night parking, fees and after-hours fuel. No live fuel price is shown.</p>'
    '<p class="note">Busy military training airspace surrounds the Pensacola and Mobile areas, and NAS Pensacola is close by. Review the sectional, restricted areas and current NOTAMs, and expect summer thunderstorms most afternoons.</p></div>'
    '<aside><span class="eyebrow">Getting around</span><h3>You’ll want a car.</h3><p>Gulf Shores and Orange Beach stretch along about 30 miles of coast. Use a crew car for short trips or rent a car for the weekend. Pensacola’s aviation museum is about an hour east.</p></aside></div></section>')

P.append('<section id="stay">' + head('02', 'Where to stay', 'Choose your stretch of beach.',
    'A state-park lodge, a high-rise with a private balcony over the Gulf, or a classic beach resort. Rates and availability need travel dates.') +
    '<div class="grid three">' +
    card('Beachfront · State park', 'The Lodge at Gulf State Park',
         'A beachfront Hilton inside Gulf State Park, with trails out the back door, a pool and Perch restaurant. The easiest romantic base.') +
    card('Orange Beach · Condo resort', 'Turquoise Place',
         'Gulf-front condominium suites with big balconies, many with private hot tubs, in Orange Beach. Choose it for space and views.') +
    card('Orange Beach · Classic resort', 'Perdido Beach Resort',
         'A long-running beachfront resort with Voyagers, the area’s best-known fine-dining room, downstairs.') +
    '</div></section>')

P.append('<section id="eat">' + head('03', 'Where to eat', 'Two dinners. One seafood lunch.',
    'Gulf shrimp and oysters are the point. Reserve weekend dinners, especially in summer.') +
    '<div class="grid three">' +
    card('Friday dinner · Fine dining', 'Voyagers',
         'Upscale Gulf-front dining at Perdido Beach Resort in Orange Beach. The special-occasion choice.') +
    card('Saturday dinner · Gulf views', 'Perch',
         'Seasonal coastal cooking with Gulf views at The Lodge at Gulf State Park. Refined but relaxed; time it for sunset.') +
    card('Lunch · Local classic', 'Doc’s Seafood Shack & Oyster Bar',
         'An Orange Beach institution since 1983, famous for fried shrimp and gumbo. For a waterfront afternoon instead, try Lulu’s on the Intracoastal or Wolf Bay Lodge.') +
    '</div></section>')

P.append('<section id="explore">' + head('04', 'Things to do', 'Beach, trails and a world-class hangar.',
    'Choose one outing a day and leave plenty of time for the beach.') +
    '<div class="explore-list">' +
    explore(1, 'National Naval Aviation Museum',
            'One of the world’s great aviation museums, at NAS Pensacola about an hour east, with more than 150 aircraft and Blue Angels history. Base access rules for visitors have changed in recent years; check the museum’s current entry requirements before you go.',
            'https://www.navalaviationmuseum.org/', 'Museum information') +
    explore(2, 'Gulf State Park',
            'Two miles of beach, a fishing pier and the Backcountry Trail, more than 25 miles of paved paths through dunes and pine forest. Rent bikes and ride for an hour or two.') +
    explore(3, 'Fort Morgan',
            'A brick fort at the tip of the peninsula, about 40 minutes west, where the Battle of Mobile Bay was fought in 1864. Quiet beaches nearby.') +
    explore(4, 'A sunset or dolphin cruise',
            'Cruises leave from Orange Beach and Perdido Pass. Dolphins are common in the bays and passes.') +
    explore(5, 'The Wharf & the Flora-Bama',
            'The Wharf in Orange Beach has waterfront shops, restaurants and a Ferris wheel. The Flora-Bama, a famous beach bar on the state line, has live music day and night.') +
    '</div></section>')

P.append('<section id="events">' + head('05', 'What’s happening', 'Sometimes the event is the reason to fly.',
    'This prototype links to the local calendar. It does not yet match events to your travel dates.') +
    '<div class="grid three">' +
    card('Spring', 'Blue Angels in Pensacola',
         'The Blue Angels’ home base is NAS Pensacola. Practice shows and the homecoming air show are seasonal; check the schedule and public-access rules.') +
    card('October', 'National Shrimp Festival',
         'Gulf Shores’ big beachfront festival with food, music and art. Fun and crowded; book early.') +
    card('Spring & fall', 'Best seasons',
         'Warm water and quieter beaches. Summer is hot and busy, with afternoon storms; hurricane season runs June–November.') +
    '</div><div class="calendar"><div><h3>Concerts, festivals & local happenings</h3><p>Check the local calendar when choosing a weekend, and confirm dates and tickets with the organizer.</p></div>'
    '<a class="button" href="https://www.gulfshores.com/" target="_blank" rel="noopener">Browse Gulf Shores events</a></div></section>')

P.append('<section id="itinerary">' + head('06', 'Suggested itinerary', 'Friday in. Sunday home.',
    'A sample Friday–Sunday weekend: beach, bikes, naval aviation and two seafood dinners. No bookings or availability confirmed.') +
    '<div class="days">' +
    day('FRI', 'Arrive & unwind', [
        ('Late-morning arrival', 'Land at KJKA, subject to weather and your actual flight plan, and pick up the car.'),
        ('Afternoon', 'Check in and head straight to the beach.'),
        ('Evening', 'Dinner at Voyagers.')]) +
    day('SAT', 'Bikes & beach', [
        ('Morning', 'Ride the Backcountry Trail in Gulf State Park.'),
        ('Afternoon', 'Fried shrimp at Doc’s, then a dolphin cruise or more beach time.'),
        ('Evening', 'Sunset dinner at Perch.')]) +
    day('SUN', 'Naval aviation & home', [
        ('Morning', 'The National Naval Aviation Museum, if base access allows, or a slow beach walk.'),
        ('Before leaving', 'Return the car and allow time at the FBO; storms build through summer afternoons.'),
        ('Fly home', 'Let weather and your flight plan set the departure.')]) +
    '</div></section>')

P.append('<section id="know">' + head('07', 'Good to know', 'Keep the weekend easy to change.',
    'These details make the difference between an appealing list and a usable getaway.') +
    know([('Book in this order', 'Car and lodging first, then dinners.'),
          ('Military airspace', 'Pensacola and Mobile have busy military training areas. Brief them before you go.'),
          ('Hurricane season', 'June through November. Watch the tropics and keep plans flexible.'),
          ('Dates come next', 'Rates and restaurant hours are date-dependent. No availability or live price is implied here.')]) +
    '</section>')

P.append(page_end(number=16, place='Gulf Shores, Alabama', note='Several picks have no website link because official addresses could not be confirmed; check each one, and confirm hours, prices and availability directly before booking.',
    credit_html=PHOTO['credit_html']))

with open(OUT, 'w') as f:
    f.write('\n'.join(P))
