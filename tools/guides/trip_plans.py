"""Add trip-length plans (Day trip / Longer stay) to destination guides.

Usage: python3 tools/guides/trip_plans.py docs/*/index.html

Idempotent: removes any previously inserted plans and re-adds them. Marks the
route box's "Weekend style" value so docs/guide-route.js can relabel it, and
inserts two hidden plans into the itinerary section. guide-route.js shows the
one matching the visitor's trip length (?trip=... from the homepage cards, or
the last choice saved on the homepage). Run after building/personalizing a guide.
"""
import re
import sys
from pathlib import Path

PLANS = {
    'savannah': {
        'day': [('Arrive', 'Land at KSAV mid-morning and ride downtown.'),
                ('Midday', 'Walk Forsyth Park and a few squares, then lunch at The Collins Quarter or on River Street.'),
                ('Afternoon', 'Browse Broughton Street, then head back to the FBO for a late-afternoon departure.')],
        'extra': [('Morning', 'A private dolphin tour from Whitemarsh Island, or a sunrise walk along the river.'),
                  ('Afternoon', 'Starland District and a brewery stop at Two Tides or Hop Atomica.'),
                  ('Evening', 'Dinner at Vic’s on the River, or a sunset riverboat dinner cruise.')]},
    'charleston': {
        'day': [('Arrive', 'Land at KCHS mid-morning and ride to Patriots Point.'),
                ('Midday', 'Explore the USS Yorktown and its aircraft, then lunch downtown.'),
                ('Afternoon', 'A walk past Rainbow Row to the Battery, then back to the FBO.')],
        'extra': [('Morning', 'A slow morning on Lower King for antiques and galleries.'),
                  ('Afternoon', 'Fort Sumter by ferry from Liberty Square, then a brewery stop at Edmund’s Oast.'),
                  ('Evening', 'Dinner at Halls Chophouse.')]},
    'asheville': {
        'day': [('Arrive', 'Land at KAVL early and pick up a car.'),
                ('Midday', 'Biltmore House and gardens with a timed entry, plus lunch on the estate.'),
                ('Afternoon', 'Winery tasting for the non-pilot, then back to the airport before mountain afternoon weather builds.')],
        'extra': [('Morning', 'Drive the Blue Ridge Parkway for overlooks and a short walk, if open.'),
                  ('Afternoon', 'The Western North Carolina Air Museum in Hendersonville (open select days), or the River Arts District.'),
                  ('Evening', 'Sunset on the Grove Park Inn terrace and a relaxed dinner downtown.')]},
    'pinehurst': {
        'day': [('Arrive', 'Land at KSOP mid-morning and head to the village.'),
                ('Midday', 'Nine holes at The Cradle or a putting match at Thistle Dhu, then lunch at Pinehurst Brewing Co.'),
                ('Afternoon', 'A drink at The Deuce overlooking No. 2’s 18th green, then fly home.')],
        'extra': [('Morning', 'A second round at Mid Pines or Pine Needles, or a long spa morning.'),
                  ('Afternoon', 'Browse downtown Southern Pines and walk the Reservoir Park loop.'),
                  ('Evening', 'A brewery stop in Southern Pines or Aberdeen, then a quiet dinner in the village.')]},
    'beaufort': {
        'day': [('Arrive', 'Land at KARW mid-morning; borrow the courtesy car or arrange a ride across the river.'),
                ('Midday', 'Lunch on Bay Street, then a horse-drawn carriage tour of the historic district.'),
                ('Afternoon', 'The waterfront park swings, then back to the FBO well before it closes.')],
        'extra': [('Morning', 'The Spanish Moss Trail by bike or on foot.'),
                  ('Afternoon', 'The Parris Island Museum (check base access) or more beach time at Hunting Island.'),
                  ('Evening', 'A sunset boat outing from the downtown marina.')]},
    'st-augustine': {
        'day': [('Arrive', 'Land at KSGJ early and ride into the old city.'),
                ('Midday', 'Castillo de San Marcos, then lunch at The Columbia on St. George Street.'),
                ('Afternoon', 'A San Sebastian Winery tasting or a Flagler College tour, then fly home ahead of afternoon storms.')],
        'extra': [('Morning', 'Beach time on Anastasia Island or a quiet walk at Crescent Beach.'),
                  ('Afternoon', 'The St. Augustine Distillery tour and a wander through Lincolnville.'),
                  ('Evening', 'A sunset cruise on Matanzas Bay, then dinner at the Casa Monica.')]},
    'greenville': {
        'day': [('Arrive', 'Land at KGMU and ride ten minutes to Main Street.'),
                ('Midday', 'Falls Park and Liberty Bridge, then lunch on Main Street.'),
                ('Afternoon', 'A short bike ride on the Swamp Rabbit Trail, then back to the airport.')],
        'extra': [('Morning', 'Rent a car for a Blue Ridge drive: waterfalls, overlooks and small towns under an hour away.'),
                  ('Afternoon', 'Unity Park and The Commons food hall, or a Greenville Drive game in season.'),
                  ('Evening', 'A show at the Peace Center.')]},
    'charlottesville': {
        'day': [('Arrive', 'Land at KCHO early and pick up a car.'),
                ('Midday', 'Monticello with a timed entry, then lunch at a nearby winery.'),
                ('Afternoon', 'A stroll on the Downtown Mall, then back to the airport. Leave tastings to the passenger.')],
        'extra': [('Morning', 'Drive to Skyline Drive or the Blue Ridge Parkway for overlooks.'),
                  ('Afternoon', 'Barboursville Vineyards and its Jefferson-designed ruins, with lunch at the winery.'),
                  ('Evening', 'A relaxed dinner at your estate hotel.')]},
    'nashville': {
        'day': [('A long day', 'At about three hours each way from KMYR, Nashville is a stretch for a day trip; it works better from closer airports.'),
                ('Midday', 'Ryman Auditorium tour and lunch downtown.'),
                ('Afternoon', 'Country Music Hall of Fame, then back to KJWN with daylight to spare.')],
        'extra': [('Morning', 'Brunch and a wander through The Gulch or 12 South.'),
                  ('Afternoon', 'A tour of a historic home or a distillery outside town (you’ll want a car).'),
                  ('Evening', 'A quieter listening room for songwriters, then dinner at The Optimist.')]},
    'key-west': {
        'day': [('Not a day trip', 'At about four hours each way from KMYR, Key West is not a day trip from most of the Southeast.'),
                ('If you are closer', 'From south Florida airports: lunch at First Flight, then a bike loop through Old Town.'),
                ('Afternoon', 'Hemingway Home, then back to the FBO well before it closes.')],
        'extra': [('Morning', 'A snorkel or sail trip on the reef, or a lazy beach morning at Casa Marina.'),
                  ('Afternoon', 'Bike to the Southernmost Point and Fort Zachary Taylor’s beach.'),
                  ('Evening', 'A sunset sail, then a casual dinner in Old Town.')]},
    'outer-banks': {
        'day': [('Arrive', 'Land at KMQI mid-morning and take the courtesy car or a rental.'),
                ('Midday', 'Wright Brothers National Memorial, then lunch on the Manteo waterfront.'),
                ('Afternoon', 'A short climb at Jockey’s Ridge, then fly home before the afternoon winds build.')],
        'extra': [('Morning', 'Drive south through Cape Hatteras National Seashore toward the Cape Hatteras Lighthouse.'),
                  ('Afternoon', 'Beach time, or the North Carolina Aquarium on Roanoke Island.'),
                  ('Evening', 'In summer, The Lost Colony outdoor drama; otherwise a quiet dinner in Duck.')]},
    'amelia-island': {
        'day': [('Arrive', 'Land at KFHB mid-morning and borrow the crew car.'),
                ('Midday', 'Lunch downtown and a stroll up Centre Street to the harbor.'),
                ('Afternoon', 'Fort Clinch and a walk on the beach, then back to the FBO.')],
        'extra': [('Morning', 'A guided horseback ride on the beach.'),
                  ('Afternoon', 'A long spa afternoon at one of the oceanfront resorts.'),
                  ('Evening', 'A sunset river cruise, then dinner at Burlingame.')]},
    'yadkin-valley': {
        'day': [('Arrive', 'Land at KZEF mid-morning and pick up the courtesy car or a rental.'),
                ('Midday', 'Lunch and a tasting for the non-pilot at Elkin Creek Vineyard.'),
                ('Afternoon', 'A glass on the terrace at Raffaldini for the non-pilot, then back to the FBO before it closes.')],
        'extra': [('Morning', 'Hike to the overlooks at Pilot Mountain or Stone Mountain State Park.'),
                  ('Afternoon', 'Downtown Elkin, or a side trip to Mount Airy.'),
                  ('Evening', 'Live music at the Reeves Theater.')]},
    'hunt-country': {
        'day': [('Arrive', 'Land at KJYO (SFRA procedures) or KHWY mid-morning and pick up a car.'),
                ('Midday', 'The Udvar-Hazy Center: the Space Shuttle, the SR-71 and more.'),
                ('Afternoon', 'Lunch and a stroll in Middleburg, with a tasting for the non-pilot, then fly home.')],
        'extra': [('Morning', 'Historic Leesburg and Morven Park.'),
                  ('Afternoon', 'A couples spa afternoon at Salamander.'),
                  ('Evening', 'A splurge dinner at The Inn at Little Washington, with a driver.')]},
    'dahlonega': {
        'day': [('Arrive', 'Land at KGVL mid-morning and pick up the rental car.'),
                ('Midday', 'Lunch on the square and the Gold Museum.'),
                ('Afternoon', 'A tasting-room stop on the square for the non-pilot, then the drive back to the FBO.')],
        'extra': [('Morning', 'Amicalola Falls and its staircase trail.'),
                  ('Afternoon', 'A gold-mine tour and a little panning.'),
                  ('Evening', 'Sunset with a glass at Wolf Mountain, then dinner on the square.')]},
    'gulf-shores': {
        'day': [('Arrive', 'Land at KJKA mid-morning and borrow a crew car.'),
                ('Midday', 'Fried shrimp and gumbo at Doc’s Seafood Shack in Orange Beach.'),
                ('Afternoon', 'An hour on the beach at Gulf State Park, then fly home before the afternoon storms.')],
        'extra': [('Morning', 'A long morning at the National Naval Aviation Museum in Pensacola.'),
                  ('Afternoon', 'Fort Morgan and its quiet beaches.'),
                  ('Evening', 'Live music at the Flora-Bama or dinner at The Wharf.')]},
    'chattanooga': {
        'day': [('Arrive', 'Land at KCHA mid-morning and head downtown.'),
                ('Midday', 'The Incline Railway up Lookout Mountain and lunch at the top.'),
                ('Afternoon', 'A walk across the Walnut Street Bridge, then back to the FBO.')],
        'extra': [('Morning', 'The Tennessee Aquarium.'),
                  ('Afternoon', 'Ruby Falls, or a drive up Signal Mountain for the views.'),
                  ('Evening', 'The tasting menu at Calliope.')]},
    'smoky-mountains': {
        'day': [('Arrive', 'Land at KGKT early and pick up the rental car.'),
                ('Midday', 'A short waterfall walk at Laurel Falls and a picnic in the park.'),
                ('Afternoon', 'Browse the arts and crafts loop, then fly out before mountain afternoon weather.')],
        'extra': [('Morning', 'The Alum Cave trail, or Grotto Falls.'),
                  ('Afternoon', 'Dollywood, or a long lunch at Blackberry Farm.'),
                  ('Evening', 'Sunset from Newfound Gap, if the road is open.')]},
    'lake-lure': {
        'day': [('Arrive', 'Land at KFQD mid-morning and borrow the courtesy car or pick up a rental.'),
                ('Midday', 'Lunch by the lake at Rumbling Bald.'),
                ('Afternoon', 'A look out over the gorge at Chimney Rock, then back to the FBO before it closes.')],
        'extra': [('Morning', 'A longer hike at Rumbling Bald or Bat Cave.'),
                  ('Afternoon', 'A boat on the lake, or an afternoon at the beach.'),
                  ('Evening', 'Dinner at La Strada.')]},
    'lake-keowee': {
        'day': [('Arrive', 'Land at KCEU or KLQK mid-morning and pick up a car.'),
                ('Midday', 'Lunch at the Tiki Hut by Keowee Marina.'),
                ('Afternoon', 'A short pontoon cruise on Lake Keowee, then fly home.')],
        'extra': [('Morning', 'The summit trail at Table Rock State Park.'),
                  ('Afternoon', 'Kayaks on Lake Jocassee, or Whitewater Falls.'),
                  ('Evening', 'A second sunset at The Lighthouse.')]},
    'lake-lanier': {
        'day': [('Arrive', 'Land at KGVL mid-morning and pick up a rental car.'),
                ('Midday', 'A few hours on a rented pontoon.'),
                ('Afternoon', 'A late lunch on Gainesville’s square, then back to the FBO.')],
        'extra': [('Morning', 'A drive to Dahlonega and its Gold Museum.'),
                  ('Afternoon', 'A winery tasting for the non-pilot.'),
                  ('Evening', 'Dinner at Cotto Modern Italian.')]},
    'harpers-ferry': {
        'day': [('Arrive', 'Land at KMRB mid-morning and pick up the crew car or a rental.'),
                ('Midday', 'The lower town and the national historical park, with lunch in town.'),
                ('Afternoon', 'A short walk to Jefferson Rock for the view, then back to the FBO.')],
        'extra': [('Morning', 'A bike ride on the C&O Canal towpath.'),
                  ('Afternoon', 'Antietam National Battlefield, or tubing on the river in summer.'),
                  ('Evening', 'Dinner and a stroll in Shepherdstown.')]},
    'hilton-head': {
        'day': [('Arrive', 'Land at KHXD mid-morning and ride to the beach.'),
                ('Midday', 'Rent bikes and ride the beach at low tide, then lunch near Coligny.'),
                ('Afternoon', 'Harbour Town and the lighthouse, then back to the FBO.')],
        'extra': [('Morning', 'A round at Harbour Town Golf Links or another island course.'),
                  ('Afternoon', 'The ferry to Daufuskie Island for lunch and a golf-cart ramble.'),
                  ('Evening', 'Late-night jazz at The Jazz Corner.')]},
    'highlands-cashiers': {
        'day': [('Arrive', 'Land at K1A5 early and pick up the car.'),
                ('Midday', 'Dry Falls and Bridal Veil Falls on the drive up, then lunch in Highlands.'),
                ('Afternoon', 'Sunset Rock or a stroll on Main Street, then down the mountain before dark.')],
        'extra': [('Morning', 'The Whiteside Mountain loop.'),
                  ('Afternoon', 'A drive to Whitewater Falls, or a spa afternoon at Old Edwards.'),
                  ('Evening', 'Dinner in Cashiers.')]},
    'st-michaels': {
        'day': [('Arrive', 'Land at KESN mid-morning and pick up the car.'),
                ('Midday', 'The Chesapeake Bay Maritime Museum, then crabs at The Crab Claw.'),
                ('Afternoon', 'A stroll around the St. Michaels harbor, then back to the FBO.')],
        'extra': [('Morning', 'Bikes and the Oxford–Bellevue Ferry to Oxford.'),
                  ('Afternoon', 'A sunset sail or a skipjack cruise.'),
                  ('Evening', 'Dinner at a waterfront restaurant on Tilghman Island.')]},
    'cape-may': {
        'day': [('Arrive', 'Land at KWWD mid-morning and walk to the NAS Wildwood Aviation Museum.'),
                ('Midday', 'A ride into Cape May and lunch at The Lobster House.'),
                ('Afternoon', 'A walk through the Victorian district, then back to the FBO.')],
        'extra': [('Morning', 'Birding at Cape May Point State Park and a climb of the lighthouse.'),
                  ('Afternoon', 'A winery tasting for the non-pilot.'),
                  ('Evening', 'Dinner and live music at the Blue Pig Tavern.')]},
    'shenandoah': {
        'day': [('Arrive', 'Land at KLUA early and pick up the car.'),
                ('Midday', 'Luray Caverns, then lunch in Luray.'),
                ('Afternoon', 'A drive up to an overlook on Skyline Drive, then back before afternoon storms.')],
        'extra': [('Morning', 'Hike to Hawksbill, the park’s highest summit.'),
                  ('Afternoon', 'Paddle or float the Shenandoah River.'),
                  ('Evening', 'Stargazing at Big Meadows.')]},
    'homestead': {
        'day': [('Arrive', 'Land at KHSP mid-morning, during FBO hours.'),
                ('Midday', 'A soak at the Warm Springs Pools, booked ahead.'),
                ('Afternoon', 'Lunch and tea at The Homestead, then back up the mountain to fly home.')],
        'extra': [('Morning', 'Fly-fishing or sporting clays at the resort.'),
                  ('Afternoon', 'A drive to Lake Moomaw or Douthat State Park.'),
                  ('Evening', 'A concert at Garth Newel Music Center.')]},
    'greenbrier': {
        'day': [('Arrive', 'Land at KLWB mid-morning and transfer to the resort.'),
                ('Midday', 'The Bunker tour and lunch at the resort.'),
                ('Afternoon', 'A walk around the grounds, then back to the FBO.')],
        'extra': [('Morning', 'A bike ride on the Greenbrier River Trail.'),
                  ('Afternoon', 'Lost World Caverns, or galleries in Lewisburg.'),
                  ('Evening', 'Dinner at The General Lewis Inn in Lewisburg.')]},
    'newport': {
        'day': [('Arrive', 'Land at KUUU mid-morning and pick up the car.'),
                ('Midday', 'The Breakers, then lunch at The Mooring.'),
                ('Afternoon', 'Part of the Cliff Walk, then back to the FBO.')],
        'extra': [('Morning', 'The International Tennis Hall of Fame, or Marble House.'),
                  ('Afternoon', 'A sail on an America’s Cup yacht.'),
                  ('Evening', 'Raw bar and sunset on Bowen’s Wharf.')]},
    'nantucket': {
        'day': [('Arrive', 'Land at KACK early and ride into town.'),
                ('Midday', 'The Whaling Museum and lunch on the wharf.'),
                ('Afternoon', 'Brant Point Lighthouse, then back to the airport before evening fog.')],
        'extra': [('Morning', 'An over-sand tour to Great Point.'),
                  ('Afternoon', 'Cisco Brewers for the non-pilot, and Surfside Beach.'),
                  ('Evening', 'Sunset at Madaket.')]},
    'bar-harbor': {
        'day': [('Arrive', 'Land at KBHB early and pick up the car.'),
                ('Midday', 'The Park Loop Road and popovers at Jordan Pond House.'),
                ('Afternoon', 'Cadillac Mountain, then back to the FBO.')],
        'extra': [('Morning', 'A whale-watch or puffin cruise.'),
                  ('Afternoon', 'The quiet side: Southwest Harbor and Bass Harbor Head Light.'),
                  ('Evening', 'Sunset on the Shore Path.')]},
    'stowe': {
        'day': [('Arrive', 'Land at KMVL early and pick up the car.'),
                ('Midday', 'The gondola up Mount Mansfield and lunch at the von Trapp Bierhall.'),
                ('Afternoon', 'The Recreation Path, then back before mountain afternoon weather.')],
        'extra': [('Morning', 'A hike to Sterling Pond or Stowe Pinnacle.'),
                  ('Afternoon', 'Ben & Jerry’s and Cold Hollow Cider Mill in Waterbury.'),
                  ('Evening', 'A spa evening and dinner at your resort.')]},
    'saratoga': {
        'day': [('Arrive', 'Land at 5B2 mid-morning and ride downtown.'),
                ('Midday', 'Lunch at Hattie’s and a walk on Broadway.'),
                ('Afternoon', 'A soak at the Roosevelt Baths, then back to the FBO.')],
        'extra': [('Morning', 'Saratoga National Historical Park.'),
                  ('Afternoon', 'The Racing Museum, or a day at the track in season.'),
                  ('Evening', 'A SPAC concert in summer.')]},
    'gettysburg': {
        'day': [('Arrive', 'Land at KW05 mid-morning and pick up the car.'),
                ('Midday', 'A Licensed Battlefield Guide tour.'),
                ('Afternoon', 'The Museum and Cyclorama, then back to the FBO.')],
        'extra': [('Morning', 'Eisenhower National Historic Site.'),
                  ('Afternoon', 'Adams County orchards and a winery for the non-pilot.'),
                  ('Evening', 'A ghost tour downtown.')]},
    'lancaster': {
        'day': [('Arrive', 'Land at KLNS mid-morning and pick up the car.'),
                ('Midday', 'Lunch at Central Market (Tue, Fri or Sat), then the Strasburg Rail Road.'),
                ('Afternoon', 'A back-roads drive past Amish farms, then back to the FBO.')],
        'extra': [('Morning', 'Sight & Sound Theatres for a big Biblical stage show.'),
                  ('Afternoon', 'Wineries and the chocolate shops of Lititz.'),
                  ('Evening', 'Dinner in a Lancaster city brewpub.')]},
    'hudson-valley': {
        'day': [('Arrive', 'Land at KPOU early and pick up the car.'),
                ('Midday', 'FDR’s home and lunch at the Culinary Institute.'),
                ('Afternoon', 'The Walkway Over the Hudson, then back to the FBO.')],
        'extra': [('Morning', 'Storm King Art Center.'),
                  ('Afternoon', 'Dia Beacon and a walk along Beacon’s Main Street.'),
                  ('Evening', 'Dinner in Kingston’s historic Stockade District.')]},
    'mystic': {
        'day': [('Arrive', 'Land at KGON mid-morning and pick up the car.'),
                ('Midday', 'Mystic Seaport Museum.'),
                ('Afternoon', 'A lobster roll in Noank, then back to the FBO.')],
        'extra': [('Morning', 'Mystic Aquarium.'),
                  ('Afternoon', 'A sail on the river or Fishers Island Sound.'),
                  ('Evening', 'Dinner in Stonington Borough.')]},
    'portsmouth': {
        'day': [('Arrive', 'Land at KPSM mid-morning and ride downtown.'),
                ('Midday', 'Strawbery Banke and lunch on the harbor.'),
                ('Afternoon', 'Market Square and Prescott Park, then back to the FBO.')],
        'extra': [('Morning', 'A cruise to the Isles of Shoals.'),
                  ('Afternoon', 'The coast road to Rye and Odiorne Point.'),
                  ('Evening', 'Dinner and the spa at Wentworth by the Sea.')]},
    'kennebunkport': {
        'day': [('Arrive', 'Land at KSFM mid-morning and pick up the car.'),
                ('Midday', 'Dock Square and a lobster roll at The Clam Shack.'),
                ('Afternoon', 'Ocean Avenue past Walker’s Point, then back to the FBO.')],
        'extra': [('Morning', 'Nubble Light and the beaches of York.'),
                  ('Afternoon', 'Ogunquit and the Marginal Way cliff walk.'),
                  ('Evening', 'A sunset harbor cruise.')]},
    'berkshires': {
        'day': [('Arrive', 'Land at KPSF mid-morning and pick up the car.'),
                ('Midday', 'The Norman Rockwell Museum and lunch in Stockbridge.'),
                ('Afternoon', 'The Mount, then back to the FBO.')],
        'extra': [('Morning', 'The Clark in Williamstown.'),
                  ('Afternoon', 'MASS MoCA in North Adams.'),
                  ('Evening', 'A summer evening at Jacob’s Pillow dance festival.')]},
    'lake-placid': {
        'day': [('Arrive', 'Land at KLKP mid-morning.'),
                ('Midday', 'The Olympic Center and lunch on Main Street.'),
                ('Afternoon', 'A walk around Mirror Lake, then back to the airport before afternoon mountain weather.')],
        'extra': [('Morning', 'A hike up Mount Jo or Cascade Mountain.'),
                  ('Afternoon', 'A boat tour on Lake Placid.'),
                  ('Evening', 'A spa evening by the fire.')]},
    'marthas-vineyard': {
        'day': [('Arrive', 'Land at KMVY early and ride to Edgartown.'),
                ('Midday', 'Lunch in Edgartown and a walk to the lighthouse.'),
                ('Afternoon', 'Oak Bluffs’ cottages, then back to the airport before evening fog.')],
        'extra': [('Morning', 'A bike ride to South Beach.'),
                  ('Afternoon', 'The Aquinnah Cliffs.'),
                  ('Evening', 'Sunset at Menemsha.')]},
    'bardstown': {
        'day': [('Arrive', 'Land at KBRY mid-morning; arrange a driver ahead.'),
                ('Midday', 'Lunch on the square and the Getz Museum.'),
                ('Afternoon', 'My Old Kentucky Home, then back to the FBO (the non-pilot can taste; the pilot waits for next time).')],
        'extra': [('Morning', 'Jim Beam’s American Stillhouse in Clermont, with a driver.'),
                  ('Afternoon', 'The Abraham Lincoln Birthplace, about 40 minutes away.'),
                  ('Evening', 'A bourbon dinner in Louisville.')]},
    'dayton': {
        'day': [('Arrive', 'Land at KMGY early and pick up the car.'),
                ('Midday', 'The National Museum of the U.S. Air Force.'),
                ('Afternoon', 'Carillon Park and the Wright Flyer III, then back to the FBO.')],
        'extra': [('Morning', 'The Wright Cycle Company and Hawthorn Hill tour.'),
                  ('Afternoon', 'Glen Helen and Clifton Gorge.'),
                  ('Evening', 'Dinner in the Oregon District.')]},
    'mackinac': {
        'day': [('Arrive', 'Land at KMCD mid-morning and take a carriage to town.'),
                ('Midday', 'Fort Mackinac and lunch on Main Street.'),
                ('Afternoon', 'Fudge and the Grand Hotel porch, then back to the airport.')],
        'extra': [('Morning', 'A ferry to St. Ignace or Mackinaw City for the bridge view.'),
                  ('Afternoon', 'A bike ride through the island’s interior trails.'),
                  ('Evening', 'Sunset at Mission Point.')]},
    'french-lick': {
        'day': [('Arrive', 'Land at KFRH mid-morning and take the shuttle.'),
                ('Midday', 'A historic tour of the West Baden dome and lunch at the resort.'),
                ('Afternoon', 'A spa treatment, then back to the airport.')],
        'extra': [('Morning', 'A second round, on the Donald Ross Course.'),
                  ('Afternoon', 'Horseback riding at the resort stables.'),
                  ('Evening', 'Live music at the resort.')]},
    'galena': {
        'day': [('Arrive', 'Land at KDBQ early and drive to Galena.'),
                ('Midday', 'Grant’s home and lunch on Main Street.'),
                ('Afternoon', 'A drive through the hills, then back to Dubuque.')],
        'extra': [('Morning', 'The National Mississippi River Museum in Dubuque.'),
                  ('Afternoon', 'A riverboat cruise.'),
                  ('Evening', 'Dinner overlooking the river.')]},
    'door-county': {
        'day': [('Arrive', 'Land at KSUE early and pick up the car.'),
                ('Midday', 'Fish Creek and Peninsula State Park.'),
                ('Afternoon', 'Lunch in Ephraim, then back to the FBO.')],
        'extra': [('Morning', 'The Washington Island ferry.'),
                  ('Afternoon', 'Wineries and orchards on the lake side.'),
                  ('Evening', 'A sunset cruise from Sister Bay.')]},
    'branson': {
        'day': [('Arrive', 'Land at KBBG mid-morning and pick up the car.'),
                ('Midday', 'Lunch and the nature trail at Top of the Rock.'),
                ('Afternoon', 'Lost Canyon Cave, then back to the FBO.')],
        'extra': [('Morning', 'Silver Dollar City.'),
                  ('Afternoon', 'A pontoon boat on Table Rock Lake.'),
                  ('Evening', 'A live show in town.')]},
    'lake-ozarks': {
        'day': [('Arrive', 'Land at KAIZ mid-morning.'),
                ('Midday', 'Ha Ha Tonka State Park’s castle ruins.'),
                ('Afternoon', 'Lunch by the lake, then back to the airport.')],
        'extra': [('Morning', 'A cave tour.'),
                  ('Afternoon', 'A second day on the water.'),
                  ('Evening', 'Sunset at a lakeside bar.')]},
    'hot-springs': {
        'day': [('Arrive', 'Land at KHOT mid-morning and drive downtown.'),
                ('Midday', 'Bathhouse Row and a thermal soak.'),
                ('Afternoon', 'Lunch at Superior Bathhouse Brewery, then back to the FBO.')],
        'extra': [('Morning', 'Garvan Woodland Gardens.'),
                  ('Afternoon', 'Hot Springs Mountain Tower and trails.'),
                  ('Evening', 'Live music at The Ohio Club.')]},
    'bentonville': {
        'day': [('Arrive', 'Land at KVBT mid-morning; coffee at Airship.'),
                ('Midday', 'Crystal Bridges and lunch at the museum.'),
                ('Afternoon', 'The square, then back to the FBO.')],
        'extra': [('Morning', 'A mountain-bike ride on the forest trails.'),
                  ('Afternoon', 'The Momentary.'),
                  ('Evening', 'Dinner in Rogers or Fayetteville.')]},
    'eureka-springs': {
        'day': [('Arrive', 'Land at 4M1 early and drive to town.'),
                ('Midday', 'Thorncrown Chapel and the historic loop.'),
                ('Afternoon', 'Lunch downtown, then back to the airport.')],
        'extra': [('Morning', 'Turpentine Creek Wildlife Refuge.'),
                  ('Afternoon', 'Beaver Lake.'),
                  ('Evening', 'A ghost tour at the Crescent.')]},
    'duluth': {
        'day': [('Arrive', 'Land at KDLH early and pick up the car.'),
                ('Midday', 'Canal Park and the Aerial Lift Bridge.'),
                ('Afternoon', 'Smoked fish at Northern Waters, then back to the FBO.')],
        'extra': [('Morning', 'Drive farther up the North Shore to Tettegouche State Park.'),
                  ('Afternoon', 'The Great Lakes Aquarium.'),
                  ('Evening', 'A sunset harbor cruise.')]},
    'naples': {
        'day': [('Arrive', 'Land at KAPF mid-morning and pick up the car.'),
                ('Midday', 'Lunch on Fifth Avenue South and the beach.'),
                ('Afternoon', 'The pier, then back to the FBO before afternoon storms.')],
        'extra': [('Morning', 'Corkscrew Swamp Sanctuary.'),
                  ('Afternoon', 'A shelling cruise to Keewaydin Island.'),
                  ('Evening', 'Sunset dinner by the Gulf.')]},
    'sanibel': {
        'day': [('Arrive', 'Land at KFMY early and drive to Sanibel.'),
                ('Midday', '“Ding” Darling and lunch on the island.'),
                ('Afternoon', 'Shelling, then back across the causeway.')],
        'extra': [('Morning', 'A kayak trip through the mangroves.'),
                  ('Afternoon', 'A boat to Cabbage Key for lunch.'),
                  ('Evening', 'Sunset on Captiva.')]},
    'islamorada': {
        'day': [('Arrive', 'Land at KMTH early and drive north.'),
                ('Midday', 'Tarpon at Robbie’s and lunch on the water.'),
                ('Afternoon', 'A swim, then back to Marathon.')],
        'extra': [('Morning', 'A backcountry fishing charter.'),
                  ('Afternoon', 'A boat to Indian Key Historic State Park.'),
                  ('Evening', 'Sunset in the sand at Morada Bay.')]},
    'palm-beach': {
        'day': [('Arrive', 'Land at KLNA mid-morning and drive to the island.'),
                ('Midday', 'Lunch at Ta-boó and Worth Avenue.'),
                ('Afternoon', 'The Flagler Museum, then back to the FBO.')],
        'extra': [('Morning', 'Polo in Wellington in season.'),
                  ('Afternoon', 'The Norton Museum of Art.'),
                  ('Evening', 'Dinner on Clematis Street in West Palm Beach.')]},
    'cedar-key': {
        'day': [('Arrive', 'Land at KCDK mid-morning and pick up a golf cart.'),
                ('Midday', 'Chowder at Tony’s and Dock Street.'),
                ('Afternoon', 'A short kayak, then fly before afternoon storms.')],
        'extra': [('Morning', 'A boat tour of the refuge islands.'),
                  ('Afternoon', 'Bikes around the island.'),
                  ('Evening', 'Sunset on Dock Street.')]},
    '30a': {
        'day': [('Arrive', 'Land at KECP early and pick up the car.'),
                ('Midday', 'Seaside and lunch at a beach café.'),
                ('Afternoon', 'A swim, then back to the airport.')],
        'extra': [('Morning', 'A paddle on a coastal dune lake.'),
                  ('Afternoon', 'Shops in Rosemary and Alys Beach.'),
                  ('Evening', 'Sunset at Grayton Beach.')]},
    'fredericksburg': {
        'day': [('Arrive', 'Land at T82 early.'),
                ('Midday', 'Breakfast at the Airport Diner and the Pacific War museum.'),
                ('Afternoon', 'Main Street, then back to the field.')],
        'extra': [('Morning', 'Johnson City and the LBJ Ranch.'),
                  ('Afternoon', 'A second day on Wine Road 290 for the non-pilot.'),
                  ('Evening', 'Live music in Luckenbach.')]},
    'san-antonio': {
        'day': [('Arrive', 'Land at KSSF early.'),
                ('Midday', 'Mission San José and lunch at Mi Tierra.'),
                ('Afternoon', 'The Alamo, then back to Stinson.')],
        'extra': [('Morning', 'The other missions by bike on the Mission Reach trail.'),
                  ('Afternoon', 'The Pearl and the San Antonio Museum of Art.'),
                  ('Evening', 'A river barge dinner cruise.')]},
    'fort-worth': {
        'day': [('Arrive', 'Land at KFTW mid-morning.'),
                ('Midday', 'The cattle drive and lunch at Joe T. Garcia’s.'),
                ('Afternoon', 'The Vintage Flying Museum, then fly home.')],
        'extra': [('Morning', 'The Kimbell and the Modern Art Museum.'),
                  ('Afternoon', 'The Fort Worth Botanic Garden.'),
                  ('Evening', 'A rodeo night in the Stockyards.')]},
    'new-orleans': {
        'day': [('Arrive', 'Land at KNEW mid-morning.'),
                ('Midday', 'Beignets and Jackson Square, then lunch in the Quarter.'),
                ('Afternoon', 'Preservation Hall’s early set, then back to the FBO.')],
        'extra': [('Morning', 'The National WWII Museum.'),
                  ('Afternoon', 'The St. Charles streetcar and the Garden District.'),
                  ('Evening', 'A jazz dinner cruise on the Steamboat Natchez.')]},
    'natchez': {
        'day': [('Arrive', 'Land at KHEZ mid-morning.'), ('Midday', 'Melrose with a ranger, then lunch downtown.'), ('Afternoon', 'The bluff, then back to the airport.')],
        'extra': [('Morning', 'Longwood.'), ('Afternoon', 'Drive the Natchez Trace to Emerald Mound.'), ('Evening', 'Sunset on the bluff.')]},
    'oxford': {
        'day': [('Arrive', 'Land at KUOX mid-morning.'), ('Midday', 'Lunch on the Square and Square Books.'), ('Afternoon', 'Rowan Oak, then back to the FBO.')],
        'extra': [('Morning', 'The University Museum and Bailey’s Woods.'), ('Afternoon', 'Walk the campus and the Grove.'), ('Evening', 'Thacker Mountain Radio, if it’s on.')]},
    'bay-st-louis': {
        'day': [('Arrive', 'Land at KHSA mid-morning.'), ('Midday', 'INFINITY Science Center.'), ('Afternoon', 'Lunch on the beach in Old Town, then back to the FBO.')],
        'extra': [('Morning', 'The Walter Anderson Museum in Ocean Springs.'), ('Afternoon', 'Galleries in Old Town.'), ('Evening', 'Sunset over the bay.')]},
    'st-francisville': {
        'day': [('Arrive', 'Land at KBTR early and drive north.'), ('Midday', 'Rosedown’s gardens and lunch in town.'), ('Afternoon', 'The historic district, then back to BTR.')],
        'extra': [('Morning', 'The Audubon State Historic Site.'), ('Afternoon', 'A hike in the Tunica Hills.'), ('Evening', 'Dinner at The Myrtles.')]},
    'lafayette': {
        'day': [('Arrive', 'Land at KLFT mid-morning.'), ('Midday', 'Boudin at Johnson’s and Vermilionville.'), ('Afternoon', 'A Lake Martin swamp tour, then back to the FBO.')],
        'extra': [('Morning', 'Zydeco breakfast at Buck & Johnny’s.'), ('Afternoon', 'Avery Island and Tabasco.'), ('Evening', 'Dancing at the Blue Moon Saloon.')]},
    'fairhope': {
        'day': [('Arrive', 'Land at KCQF mid-morning.'), ('Midday', 'Lunch downtown and the pier.'), ('Afternoon', 'Bellingrath Gardens, then back to the FBO.')],
        'extra': [('Morning', 'The USS Alabama.'), ('Afternoon', 'The spa at The Grand.'), ('Evening', 'Sunset on the pier.')]},
    'huntsville': {
        'day': [('Arrive', 'Land at KHSV early.'), ('Midday', 'The U.S. Space & Rocket Center.'), ('Afternoon', 'Lunch downtown, then back to the FBO.')],
        'extra': [('Morning', 'The Botanical Garden.'), ('Afternoon', 'Monte Sano State Park.'), ('Evening', 'Rooftop drinks downtown.')]},
    'lake-martin': {
        'day': [('Arrive', 'Land at KALX mid-morning.'), ('Midday', 'Lunch at Russell Crossroads.'), ('Afternoon', 'A short boat ride, then back to the airport.')],
        'extra': [('Morning', 'The Smith Mountain fire tower.'), ('Afternoon', 'A boat day.'), ('Evening', 'Dinner at SpringHouse.')]},
    'birmingham': {
        'day': [('Arrive', 'Land at KBHM mid-morning.'), ('Midday', 'The Southern Museum of Flight, beside the field.'), ('Afternoon', 'Lunch at Chez Fonfon, then back to the FBO.')],
        'extra': [('Morning', 'The Civil Rights Institute.'), ('Afternoon', 'Barber Vintage Motorsports Museum.'), ('Evening', 'Sunset at Vulcan Park.')]},
    'memphis': {
        'day': [('Arrive', 'Land at KMEM early.'), ('Midday', 'Sun Studio and lunch at Central BBQ.'), ('Afternoon', 'The National Civil Rights Museum, then back to the FBO.')],
        'extra': [('Morning', 'Graceland.'), ('Afternoon', 'Stax Museum.'), ('Evening', 'Beale Street.')]},
    'golden-isles': {
        'day': [('Arrive', 'Land at KSSI mid-morning.'), ('Midday', 'Bike to the lighthouse and lunch in the village.'), ('Afternoon', 'The beach, then back to the FBO.')],
        'extra': [('Morning', 'Driftwood Beach on Jekyll.'), ('Afternoon', 'The Jekyll Island Club and Turtle Center.'), ('Evening', 'Sunset over the marsh.')]},
    'clarksdale': {
        'day': [('Arrive', 'Land at KCKM mid-morning.'), ('Midday', 'The Delta Blues Museum and tamales.'), ('Afternoon', 'Cat Head and the Crossroads, then back to the airport.')],
        'extra': [('Morning', 'A Blues Trail drive.'), ('Afternoon', 'Barbecue at Abe’s.'), ('Evening', 'Red’s Lounge.')]},
    'natchitoches': {
        'day': [('Arrive', 'Land at KIER mid-morning.'), ('Midday', 'Meat pies at Lasyone’s and Front Street.'), ('Afternoon', 'Oakland Plantation, then back to the airport.')],
        'extra': [('Morning', 'Melrose Plantation.'), ('Afternoon', 'A historic-district walk.'), ('Evening', 'Sunset on Cane River Lake.')]},
    'little-rock': {
        'day': [('Arrive', 'Land at KLIT early.'), ('Midday', 'Central High School with a ranger.'), ('Afternoon', 'The River Market, then back to the FBO.')],
        'extra': [('Morning', 'Bike the Big Dam Bridge.'), ('Afternoon', 'Pinnacle Mountain.'), ('Evening', 'Dinner on the river.')]},
    'st-louis': {
        'day': [('Arrive', 'Land at KCPS early.'), ('Midday', 'The Gateway Arch tram.'), ('Afternoon', 'Lunch on The Hill, then back to the FBO.')],
        'extra': [('Morning', 'The Art Museum in Forest Park.'), ('Afternoon', 'The Botanical Garden.'), ('Evening', 'Ted Drewes custard.')]},
    'kansas-city': {
        'day': [('Arrive', 'Land at KMKC mid-morning.'), ('Midday', 'The TWA Museum on the field, then barbecue at Joe’s.'), ('Afternoon', 'The Nelson-Atkins, then back to the FBO.')],
        'extra': [('Morning', 'The WWI Museum.'), ('Afternoon', '18th & Vine.'), ('Evening', 'Jazz at the Blue Room.')]},
    'annapolis': {
        'day': [('Arrive', 'Land at KANP mid-morning.'), ('Midday', 'A Naval Academy tour and lunch at Middleton Tavern.'), ('Afternoon', 'Walk the harbor, then back to the airport.')],
        'extra': [('Morning', 'The State House and Paca House garden.'), ('Afternoon', 'A sail on the Woodwind.'), ('Evening', 'Dinner in Eastport.')]},
    'ocean-city': {
        'day': [('Arrive', 'Land at KOXB mid-morning.'), ('Midday', 'The boardwalk and Thrasher’s fries.'), ('Afternoon', 'The beach, then back to the airport.')],
        'extra': [('Morning', 'Wild horses at Assateague.'), ('Afternoon', 'Berlin’s Main Street.'), ('Evening', 'Sunset at Fager’s Island.')]},
    'deep-creek-lake': {
        'day': [('Arrive', 'Land at 2G4 mid-morning.'), ('Midday', 'Swallow Falls State Park.'), ('Afternoon', 'Lunch by the lake, then back to the airport.')],
        'extra': [('Morning', 'A pontoon on the lake.'), ('Afternoon', 'The mountain coaster at Wisp.'), ('Evening', 'Dinner at Mountain State Brewing.')]},
    'new-river-gorge': {
        'day': [('Arrive', 'Land at KBKW early.'), ('Midday', 'The Canyon Rim Visitor Center and lunch in Fayetteville.'), ('Afternoon', 'Long Point Trail, then back to the airport.')],
        'extra': [('Morning', 'Whitewater rafting.'), ('Afternoon', 'The Bridge Walk.'), ('Evening', 'Pies & Pints.')]},
    'berkeley-springs': {
        'day': [('Arrive', 'Land at KMRB early and drive west.'), ('Midday', 'A Roman bath soak.'), ('Afternoon', 'The Ice House, then back to the airport.')],
        'extra': [('Morning', 'Cacapon Resort State Park.'), ('Afternoon', 'Panorama Overlook.'), ('Evening', 'Dinner at Lot 12.')]},
    'lexington': {
        'day': [('Arrive', 'Land at KLEX early.'), ('Midday', 'Keeneland and the track kitchen.'), ('Afternoon', 'Old Friends Farm, then back to the FBO.')],
        'extra': [('Morning', 'The Kentucky Horse Park.'), ('Afternoon', 'Woodford Reserve.'), ('Evening', 'Dinner at Holly Hill Inn.')]},
    'louisville': {
        'day': [('Arrive', 'Land at KLOU mid-morning.'), ('Midday', 'The Derby Museum and a Hot Brown.'), ('Afternoon', 'Whiskey Row, then back to the FBO.')],
        'extra': [('Morning', 'The Slugger Museum.'), ('Afternoon', 'The Ali Center and Big Four Bridge.'), ('Evening', 'Dinner at Jack Fry’s.')]},
    'paducah': {
        'day': [('Arrive', 'Land at KPAH mid-morning.'), ('Midday', 'The National Quilt Museum.'), ('Afternoon', 'The floodwall murals, then back to the FBO.')],
        'extra': [('Morning', 'LowerTown galleries.'), ('Afternoon', 'The River Discovery Center.'), ('Evening', 'Dinner at Freight House.')]},
    'finger-lakes': {
        'day': [('Arrive', 'Land at KITH early.'), ('Midday', 'Taughannock Falls and lunch in Ithaca.'), ('Afternoon', 'A Cayuga Lake winery, then back to the FBO.')],
        'extra': [('Morning', 'Watkins Glen.'), ('Afternoon', 'Seneca Lake wineries.'), ('Evening', 'Dinner at Gola Osteria.')]},
    'bucks-county': {
        'day': [('Arrive', 'Land at KDYL mid-morning.'), ('Midday', 'New Hope and Lambertville.'), ('Afternoon', 'Washington Crossing, then back to the FBO.')],
        'extra': [('Morning', 'The Mercer Museum.'), ('Afternoon', 'The Michener Art Museum.'), ('Evening', 'A Playhouse show.')]},
    'poconos': {
        'day': [('Arrive', 'Land at KMPO mid-morning.'), ('Midday', 'Bushkill Falls.'), ('Afternoon', 'Lunch, then back to the airport.')],
        'extra': [('Morning', 'The Delaware Water Gap.'), ('Afternoon', 'The Lehigh Gorge train.'), ('Evening', 'Dinner by the fire.')]},
    'camden': {
        'day': [('Arrive', 'Land at KRKD early.'), ('Midday', 'The Owls Head Transportation Museum.'), ('Afternoon', 'Lunch in Rockland, then back to the FBO.')],
        'extra': [('Morning', 'Mount Battie.'), ('Afternoon', 'A windjammer sail.'), ('Evening', 'Lobster by the harbor.')]},
    'portland-maine': {
        'day': [('Arrive', 'Land at KPWM mid-morning.'), ('Midday', 'Lunch at Eventide and the Old Port.'), ('Afternoon', 'Portland Head Light, then back to the FBO.')],
        'extra': [('Morning', 'A Casco Bay ferry.'), ('Afternoon', 'The Portland Museum of Art.'), ('Evening', 'Dinner at Fore Street.')]},
    'chatham': {
        'day': [('Arrive', 'Land at KCQX mid-morning.'), ('Midday', 'Lunch at the fish pier.'), ('Afternoon', 'The lighthouse and beach, then back to the airport.')],
        'extra': [('Morning', 'A seal tour.'), ('Afternoon', 'Bike the rail trail.'), ('Evening', 'Dinner on Main Street.')]},
    'princeton': {
        'day': [('Arrive', 'Land at 39N mid-morning.'), ('Midday', 'Campus and the art museum.'), ('Afternoon', 'Grounds For Sculpture, then back to the airport.')],
        'extra': [('Morning', 'Morven.'), ('Afternoon', 'Lake Carnegie.'), ('Evening', 'A McCarter show.')]},
    'block-island': {
        'day': [('Arrive', 'Land at KBID mid-morning.'), ('Midday', 'Rent bikes and ride to Mohegan Bluffs.'), ('Afternoon', 'The beach, then back to the airport.')],
        'extra': [('Morning', 'North Light and Clay Head Trail.'), ('Afternoon', 'The beach.'), ('Evening', 'Sunset at the Atlantic Inn.')]},
    'providence': {
        'day': [('Arrive', 'Land at KPVD mid-morning.'), ('Midday', 'Walk Benefit Street and College Hill.'), ('Afternoon', 'Federal Hill, then back to the airport.')],
        'extra': [('Morning', 'The RISD Museum.'), ('Afternoon', 'Federal Hill.'), ('Evening', 'Dinner at Oberlin, then WaterFire.')]},
    'watch-hill': {
        'day': [('Arrive', 'Land at KWST mid-morning.'), ('Midday', 'Walk the village and ride the carousel.'), ('Afternoon', 'The spa, then back to the airport.')],
        'extra': [('Morning', 'Napatree Point.'), ('Afternoon', 'The spa.'), ('Evening', 'Dinner at Ocean House.')]},
    'new-haven': {
        'day': [('Arrive', 'Land at KHVN mid-morning.'), ('Midday', 'The Yale University Art Gallery.'), ('Afternoon', 'The Center for British Art, then back to the airport.')],
        'extra': [('Morning', 'The Peabody Museum.'), ('Afternoon', 'The Center for British Art.'), ('Evening', 'Dinner at Union League, then Yale Rep.')]},
    'essex-ct': {
        'day': [('Arrive', 'Land at KSNC mid-morning.'), ('Midday', 'Walk Essex village and the river museum.'), ('Afternoon', 'Gillette Castle, then back to the airport.')],
        'extra': [('Morning', 'The Essex Steam Train and riverboat.'), ('Afternoon', 'Gillette Castle.'), ('Evening', 'A Goodspeed show.')]},
    'litchfield-hills': {
        'day': [('Arrive', 'Land at KOXC mid-morning.'), ('Midday', 'Drive to the inn; walk the grounds.'), ('Afternoon', 'Hopkins Vineyard and Lake Waramaug, then back to the airport.')],
        'extra': [('Morning', 'The spa.'), ('Afternoon', 'Hopkins Vineyard and Lake Waramaug.'), ('Evening', 'Dinner at the Hopkins Inn.')]},
    'asbury-park': {
        'day': [('Arrive', 'Land at KBLM mid-morning.'), ('Midday', 'The boardwalk and Silverball.'), ('Afternoon', 'Spring Lake, then back to the airport.')],
        'extra': [('Morning', 'The beach.'), ('Afternoon', 'Spring Lake.'), ('Evening', 'Pizza at Talula’s.')]},
    'atlantic-city': {
        'day': [('Arrive', 'Land at KACY mid-morning.'), ('Midday', 'The boardwalk at sunset.'), ('Afternoon', 'Absecon Lighthouse, then back to the airport.')],
        'extra': [('Morning', 'The spa.'), ('Afternoon', 'Absecon Lighthouse.'), ('Evening', 'Dinner at the Knife & Fork Inn and a show.')]},
    'woodstock-vt': {
        'day': [('Arrive', 'Land at KLEB early.'), ('Midday', 'Walk the village green and covered bridge.'), ('Afternoon', 'Billings Farm and the national park, then back to the airport.')],
        'extra': [('Morning', 'Billings Farm and the national park.'), ('Afternoon', 'Quechee Gorge and Simon Pearce glassblowing.'), ('Evening', 'Dinner at Simon Pearce.')]},
    'manchester-vt': {
        'day': [('Arrive', 'Land at KDDH early.'), ('Midday', 'Walk Manchester Village and the Northshire Bookstore.'), ('Afternoon', 'Hildene, then back to the airport.')],
        'extra': [('Morning', 'Hildene.'), ('Afternoon', 'Skyline Drive, then the spa.'), ('Evening', 'Dinner at The Silver Fork.')]},
    'burlington-vt': {
        'day': [('Arrive', 'Land at KBTV early.'), ('Midday', 'Church Street and the waterfront.'), ('Afternoon', 'Shelburne Farms, then back to the airport.')],
        'extra': [('Morning', 'Shelburne Farms.'), ('Afternoon', 'The Shelburne Museum.'), ('Evening', 'A sunset cruise, then Honey Road.')]},
    'bretton-woods': {
        'day': [('Arrive', 'Land at KHIE early.'), ('Midday', 'Check in and sit on the veranda.'), ('Afternoon', 'The Cog Railway to the summit, then back to the airport.')],
        'extra': [('Morning', 'The Cog Railway to the summit.'), ('Afternoon', 'The spa.'), ('Evening', 'Dinner at Sugar Hill Inn.')]},
    'lake-winnipesaukee': {
        'day': [('Arrive', 'Land at KLCI early.'), ('Midday', 'Walk Meredith’s waterfront.'), ('Afternoon', 'A cruise on the M/S Mount Washington, then back to the airport.')],
        'extra': [('Morning', 'A cruise on the M/S Mount Washington.'), ('Afternoon', 'Castle in the Clouds.'), ('Evening', 'Dinner at Wolfe’s Tavern.')]},
    'north-conway': {
        'day': [('Arrive', 'Land at KIZG early.'), ('Midday', 'Drive through the covered bridge to Jackson.'), ('Afternoon', 'The Conway Scenic Railroad, then back to the airport.')],
        'extra': [('Morning', 'The Conway Scenic Railroad.'), ('Afternoon', 'The Kancamagus Highway.'), ('Evening', 'Dinner at Moat Mountain.')]},
    'black-hills': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Custer State Park.'), ('Afternoon', 'The Wildlife Loop.')],
        'extra': [('Morning', 'The Wildlife Loop.'), ('Afternoon', 'The Needles Highway and Sylvan Lake.'), ('Evening', 'Dinner at Delmonico Grill.')]},
    'deadwood': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Walk Main Street.'), ('Afternoon', 'Spearfish Canyon waterfalls.')],
        'extra': [('Morning', 'Spearfish Canyon waterfalls.'), ('Afternoon', 'Mount Moriah Cemetery.'), ('Evening', 'Dinner at the Bullock.')]},
    'badlands': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to the park; sunset on the Loop Road.'), ('Afternoon', 'Sunrise hike on the Door Trail.')],
        'extra': [('Morning', 'Sunrise hike on the Door Trail.'), ('Afternoon', 'The Minuteman Missile site.'), ('Evening', 'Dinner at the lodge.')]},
    'sioux-falls': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Falls Park.'), ('Afternoon', 'SculptureWalk.')],
        'extra': [('Morning', 'SculptureWalk.'), ('Afternoon', 'The Washington Pavilion.'), ('Evening', 'Dinner at Minervas.')]},
    'medora': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Medora.'), ('Afternoon', 'The park’s scenic loop at sunrise.')],
        'extra': [('Morning', 'The park’s scenic loop at sunrise.'), ('Afternoon', 'The Presidential Library.'), ('Evening', 'Dinner at Theodore’s.')]},
    'fargo': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Fargo Air Museum, on the field.'), ('Afternoon', 'The Plains Art Museum.')],
        'extra': [('Morning', 'The Plains Art Museum.'), ('Afternoon', 'Walk downtown.'), ('Evening', 'A show at the Fargo Theatre.')]},
    'bismarck': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The State Capitol.'), ('Afternoon', 'The Heritage Center & State Museum.')],
        'extra': [('Morning', 'The Heritage Center & State Museum.'), ('Afternoon', 'Fort Abraham Lincoln.'), ('Evening', 'Dinner at Pirogue Grille.')]},
    'peace-garden': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Settle in at the lake.'), ('Afternoon', 'The International Peace Garden.')],
        'extra': [('Morning', 'The International Peace Garden.'), ('Afternoon', 'A paddle on Lake Metigoshe.'), ('Evening', 'Dinner in Bottineau.')]},
    'omaha': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Old Market and the pedestrian bridge.'), ('Afternoon', 'The SAC Aerospace Museum.')],
        'extra': [('Morning', 'The SAC Aerospace Museum.'), ('Afternoon', 'Lauritzen Gardens.'), ('Evening', 'Steaks at Gorat’s.')]},
    'lincoln-ne': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The State Capitol observation deck.'), ('Afternoon', 'The Sheldon Museum of Art.')],
        'extra': [('Morning', 'The Sheldon Museum of Art.'), ('Afternoon', 'The International Quilt Museum.'), ('Evening', 'Dinner in the Haymarket.')]},
    'scottsbluff': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Scotts Bluff summit road.'), ('Afternoon', 'Hike the Saddle Rock Trail.')],
        'extra': [('Morning', 'Hike the Saddle Rock Trail.'), ('Afternoon', 'Chimney Rock.'), ('Evening', 'Sunset at the rock.')]},
    'valentine': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Settle in near the river.'), ('Afternoon', 'Float the Niobrara.')],
        'extra': [('Morning', 'Float the Niobrara.'), ('Afternoon', 'Smith Falls.'), ('Evening', 'Dinner in town.')]},
    'wichita': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'The Kansas Aviation Museum.'), ('Afternoon', 'Botanica.')],
        'extra': [('Morning', 'Botanica.'), ('Afternoon', 'Old Cowtown Museum.'), ('Evening', 'Dinner in Old Town.')]},
    'flint-hills': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Cottonwood Falls.'), ('Afternoon', 'Tallgrass Prairie National Preserve.')],
        'extra': [('Morning', 'Tallgrass Prairie National Preserve.'), ('Afternoon', 'The Flint Hills Scenic Byway.'), ('Evening', 'Dinner at Hays House.')]},
    'lawrence': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Walk Mass Street.'), ('Afternoon', 'The Spencer Museum of Art.')],
        'extra': [('Morning', 'The Spencer Museum of Art.'), ('Afternoon', 'Campus and the overlook.'), ('Evening', 'Dinner at 715, then Liberty Hall.')]},
    'lindsborg': {
        'day': [('Arrive', "A day trip isn't practical from the Southeast; this is a long-flight destination."), ('Midday', 'Drive to Lindsborg.'), ('Afternoon', 'The Sandzén Gallery and Coronado Heights.')],
        'extra': [('Morning', 'The Sandzén Gallery and Coronado Heights.'), ('Afternoon', 'Drive to Abilene.'), ('Evening', 'Dinner in Abilene.')]},
    'traverse-city': {
        'day': [('Arrive', 'Land at KTVC early.'), ('Midday', 'Walk downtown and the bay.'), ('Afternoon', 'Sleeping Bear Dunes, then back to the airport.')],
        'extra': [('Morning', 'Sleeping Bear Dunes.'), ('Afternoon', 'Leelanau wineries and Farm Club.'), ('Evening', 'Dinner at Mission Table.')]},
    'saugatuck': {
        'day': [('Arrive', 'Land at KBIV early.'), ('Midday', 'Walk Saugatuck’s galleries.'), ('Afternoon', 'Oval Beach, then back to the airport.')],
        'extra': [('Morning', 'Oval Beach.'), ('Afternoon', 'A dune ride.'), ('Evening', 'Dinner at Everyday People Cafe.')]},
    'harbor-springs': {
        'day': [('Arrive', 'Land at KMGN early.'), ('Midday', 'Walk Harbor Springs.'), ('Afternoon', 'Drive the Tunnel of Trees, then back to the airport.')],
        'extra': [('Morning', 'Drive the Tunnel of Trees.'), ('Afternoon', 'Lunch at Legs Inn, then Petoskey State Park.'), ('Evening', 'Dinner in Petoskey.')]},
    'kohler': {
        'day': [('Arrive', 'Land at KSBM early.'), ('Midday', 'Check in and walk the village.'), ('Afternoon', 'The Kohler Waters Spa, then back to the airport.')],
        'extra': [('Morning', 'The Kohler Waters Spa.'), ('Afternoon', 'The Arts Center.'), ('Evening', 'Dinner at The Immigrant.')]},
    'lake-geneva': {
        'day': [('Arrive', 'Land at KBUU early.'), ('Midday', 'Walk downtown and part of the Shore Path.'), ('Afternoon', 'The Mail Boat cruise, then back to the airport.')],
        'extra': [('Morning', 'The Mail Boat cruise.'), ('Afternoon', 'The spa.'), ('Evening', 'Dinner at Pier 290.')]},
    'madison': {
        'day': [('Arrive', 'Land at KMSN early.'), ('Midday', 'Walk the Capitol and State Street.'), ('Afternoon', 'The farmers’ market, then back to the airport.')],
        'extra': [('Morning', 'The farmers’ market.'), ('Afternoon', 'Taliesin.'), ('Evening', 'Dinner at L’Etoile.')]},
    'bayfield': {
        'day': [('Arrive', 'Land at KASX early.'), ('Midday', 'Walk the harbor.'), ('Afternoon', 'A sea-cave cruise or kayak tour, then back to the airport.')],
        'extra': [('Morning', 'A sea-cave cruise or kayak tour.'), ('Afternoon', 'The ferry to Madeline Island.'), ('Evening', 'Dinner at the Old Rittenhouse Inn.')]},
    'put-in-bay': {
        'day': [('Arrive', 'Land at 3W2 early and rent a cart.'), ('Midday', 'Perry’s Victory memorial and lunch at The Boardwalk.'), ('Afternoon', 'Heineman’s Winery, then back to the airport.')],
        'extra': [('Morning', 'Kelleys Island by ferry.'), ('Afternoon', 'Stone Lab’s lighthouse tour.'), ('Evening', 'Sunset on the west shore.')]},
    'hocking-hills': {
        'day': [('Arrive', 'Land at KLHQ early.'), ('Midday', 'Old Man’s Cave.'), ('Afternoon', 'Ash Cave, then back to the FBO.')],
        'extra': [('Morning', 'Cedar Falls and Conkle’s Hollow.'), ('Afternoon', 'A canopy zip-line tour.'), ('Evening', 'Dinner at The Inn at Cedar Falls.')]},
    'cleveland': {
        'day': [('Arrive', 'Land at KBKL mid-morning.'), ('Midday', 'The Rock & Roll Hall of Fame.'), ('Afternoon', 'Lunch at the West Side Market, then back to the airport.')],
        'extra': [('Morning', 'The Cleveland Museum of Art.'), ('Afternoon', 'The Botanical Garden.'), ('Evening', 'A Playhouse Square show.')]},
    'indianapolis': {
        'day': [('Arrive', 'Land at KEYE mid-morning.'), ('Midday', 'The Speedway museum and a track tour.'), ('Afternoon', 'Lunch on Mass Ave, then back to the FBO.')],
        'extra': [('Morning', 'Bike the Cultural Trail.'), ('Afternoon', 'Newfields.'), ('Evening', 'Dinner at St. Elmo.')]},
    'brown-county': {
        'day': [('Arrive', 'Land at KBMG early.'), ('Midday', 'The galleries in Nashville.'), ('Afternoon', 'A drive through Brown County State Park, then back to the airport.')],
        'extra': [('Morning', 'T.C. Steele State Historic Site.'), ('Afternoon', 'A winery in Nashville.'), ('Evening', 'Dinner at Story Inn.')]},
    'indiana-dunes': {
        'day': [('Arrive', 'Land at KMGC early.'), ('Midday', 'The Three Dune Challenge.'), ('Afternoon', 'West Beach, then back to the airport.')],
        'extra': [('Morning', 'A trail through the woods.'), ('Afternoon', 'Washington Park beach.'), ('Evening', 'Dinner at Lucrezia.')]},
    'chicago': {
        'day': [('Arrive', 'Land at KPWK early and take a rideshare downtown.'), ('Midday', 'The architecture river cruise.'), ('Afternoon', 'Deep dish at Lou Malnati’s, then back to the airport.')],
        'extra': [('Morning', 'The Art Institute.'), ('Afternoon', 'Millennium Park.'), ('Evening', 'Dinner at Girl & The Goat.')]},
    'starved-rock': {
        'day': [('Arrive', 'Land at KVYS early.'), ('Midday', 'Hike to St. Louis Canyon.'), ('Afternoon', 'Lunch at the lodge, then back to the airport.')],
        'extra': [('Morning', 'Matthiessen State Park.'), ('Afternoon', 'Wine in Utica.'), ('Evening', 'Dinner at Starved Rock Lodge.')]},
    'shawnee-hills': {
        'day': [('Arrive', 'Land at KMWA early.'), ('Midday', 'Lunch at Blue Sky Vineyard.'), ('Afternoon', 'A second winery, then back to the airport.')],
        'extra': [('Morning', 'Giant City’s sandstone trails.'), ('Afternoon', 'StarView and Rustle Hill.'), ('Evening', 'Dinner at Giant City Lodge.')]},
    'bedford-springs': {
        'day': [('Arrive', 'Land at KHMZ early.'), ('Midday', 'Lunch at Jean Bonnet Tavern.'), ('Afternoon', 'A soak in the resort’s indoor pool, then back to the airport.')],
        'extra': [('Morning', 'Flight 93 National Memorial.'), ('Afternoon', 'Old Bedford Village.'), ('Evening', 'Dinner in the 1796 Room.')]},
    'laurel-highlands': {
        'day': [('Arrive', 'Land at KLBE early.'), ('Midday', 'Fallingwater.'), ('Afternoon', 'Kentuck Knob, then back to the airport.')],
        'extra': [('Morning', 'Ohiopyle’s falls.'), ('Afternoon', 'Ligonier’s shops.'), ('Evening', 'Dinner at Ligonier Tavern.')]},
    'pittsburgh': {
        'day': [('Arrive', 'Land at KAGC mid-morning.'), ('Midday', 'The Duquesne Incline and lunch on Mount Washington.'), ('Afternoon', 'The Warhol Museum, then back to the airport.')],
        'extra': [('Morning', 'The Strip District.'), ('Afternoon', 'Phipps Conservatory.'), ('Evening', 'Dinner at Eleven.')]},
    'pine-creek-gorge': {
        'day': [('Arrive', 'Land at N38 early.'), ('Midday', 'Leonard Harrison’s overlooks.'), ('Afternoon', 'Lunch on Main Street, then back to the airport.')],
        'extra': [('Morning', 'Bike the Pine Creek Rail Trail.'), ('Afternoon', 'Colton Point.'), ('Evening', 'Dinner at The Steak House.')]},
    'hershey': {
        'day': [('Arrive', 'Land at KCXY mid-morning.'), ('Midday', 'Hershey Gardens.'), ('Afternoon', 'The Hershey Story, then back to the airport.')],
        'extra': [('Morning', 'A spa treatment.'), ('Afternoon', 'Chocolate World and a winery.'), ('Evening', 'Dinner at The Circular.')]},
    'erie': {
        'day': [('Arrive', 'Land at KERI mid-morning.'), ('Midday', 'Presque Isle’s beaches.'), ('Afternoon', 'The Flagship Niagara, then back to the airport.')],
        'extra': [('Morning', 'Wine country tastings.'), ('Afternoon', 'Tom Ridge Environmental Center.'), ('Evening', 'Dinner at Oliver’s Rooftop.')]},
    'minocqua': {
        'day': [('Arrive', 'Land at KARV early.'), ('Midday', 'Walk the island and downtown.'), ('Afternoon', 'A pontoon ride, then back to the airport.')],
        'extra': [('Morning', 'Bike the Bearskin Trail.'), ('Afternoon', 'Wildwood Wildlife Park.'), ('Evening', 'The Min-Aqua Bats show.')]},
    'elkhart-lake': {
        'day': [('Arrive', 'Land at KSBM early.'), ('Midday', 'Swim at the village beach.'), ('Afternoon', 'Lunch at Off the Rail, then back to the airport.')],
        'extra': [('Morning', 'Aspira Spa.'), ('Afternoon', 'Road America.'), ('Evening', 'Dinner at Lola’s on the Lake.')]},
    'wisconsin-dells': {
        'day': [('Arrive', 'Land at KDLL early.'), ('Midday', 'Hike the bluffs at Devil’s Lake.'), ('Afternoon', 'A Duck tour, then back to the airport.')],
        'extra': [('Morning', 'Paddle Mirror Lake.'), ('Afternoon', 'The International Crane Foundation.'), ('Evening', 'Sunset dinner at Ishnala.')]},
    'hayward': {
        'day': [('Arrive', 'Land at KHYR early.'), ('Midday', 'The Fishing Hall of Fame.'), ('Afternoon', 'Lunch at the Angry Minnow, then back to the airport.')],
        'extra': [('Morning', 'Paddle the Chippewa Flowage.'), ('Afternoon', 'Hike the Birkie Trail.'), ('Evening', 'Dinner at The Ranch.')]},
    'north-shore': {
        'day': [('Arrive', 'Land at KCKC early.'), ('Midday', 'Artist’s Point and the harbor.'), ('Afternoon', 'Lunch at the Angry Trout, then back to the airport.')],
        'extra': [('Morning', 'The Lutsen gondola.'), ('Afternoon', 'Waterfalls along the shore.'), ('Evening', 'Dinner at Naniboujou.')]},
    'twin-cities': {
        'day': [('Arrive', 'Land at KSTP mid-morning.'), ('Midday', 'The Walker sculpture garden.'), ('Afternoon', 'A Jucy Lucy at Matt’s Bar, then back to the airport.')],
        'extra': [('Morning', 'Mill City Museum and the Stone Arch Bridge.'), ('Afternoon', 'Minnehaha Falls.'), ('Evening', 'Dinner at Owamni.')]},
    'stillwater': {
        'day': [('Arrive', 'Land at 21D early.'), ('Midday', 'Walk the Lift Bridge loop.'), ('Afternoon', 'Lunch on Main Street, then back to the airport.')],
        'extra': [('Morning', 'A trolley tour.'), ('Afternoon', 'Bluffs at William O’Brien.'), ('Evening', 'Dinner at Domaćin.')]},
    'tulsa': {
        'day': [('Arrive', 'Land at KRVS mid-morning.'), ('Midday', 'The Gathering Place.'), ('Afternoon', 'The Bob Dylan Center, then back to the airport.')],
        'extra': [('Morning', 'Philbrook’s villa and gardens.'), ('Afternoon', 'The Woody Guthrie Center.'), ('Evening', 'A show at Cain’s Ballroom.')]},
    'oklahoma-city': {
        'day': [('Arrive', 'Land at KPWA mid-morning.'), ('Midday', 'The National Memorial.'), ('Afternoon', 'Lunch at Cattlemen’s, then back to the airport.')],
        'extra': [('Morning', 'The Cowboy & Western Heritage Museum.'), ('Afternoon', 'The First Americans Museum.'), ('Evening', 'Dinner at Vast.')]},
    'wichita-mountains': {
        'day': [('Arrive', 'Land at KLAW early.'), ('Midday', 'The wildlife refuge.'), ('Afternoon', 'A Meersburger, then back to the airport.')],
        'extra': [('Morning', 'Mount Scott.'), ('Afternoon', 'Medicine Park’s creek.'), ('Evening', 'Dinner in Medicine Park.')]},
    'broken-bow': {
        'day': [('Arrive', 'Land at 4O4 early.'), ('Midday', 'Beavers Bend State Park.'), ('Afternoon', 'Pizza at Grateful Head, then back to the airport.')],
        'extra': [('Morning', 'Paddle the Mountain Fork.'), ('Afternoon', 'Broken Bow Lake.'), ('Evening', 'Dinner at Abendigo’s.')]},
    'okoboji': {
        'day': [('Arrive', 'Land at KSPW early.'), ('Midday', 'A Queen II cruise.'), ('Afternoon', 'Lunch at Maxwell’s, then back to the airport.')],
        'extra': [('Morning', 'A swim and a boat rental.'), ('Afternoon', 'Arnolds Park.'), ('Evening', 'A summer theatre show.')]},
    'des-moines': {
        'day': [('Arrive', 'Land at KIKV mid-morning.'), ('Midday', 'The sculpture park.'), ('Afternoon', 'The botanical garden, then back to the airport.')],
        'extra': [('Morning', 'The Saturday farmers’ market.'), ('Afternoon', 'The capitol.'), ('Evening', 'Dinner at 801 Chophouse.')]},
    'dubuque': {
        'day': [('Arrive', 'Land at KDBQ mid-morning.'), ('Midday', 'The Fenelon Place Elevator.'), ('Afternoon', 'The river museum, then back to the airport.')],
        'extra': [('Morning', 'The Field of Dreams.'), ('Afternoon', 'Wine at Stone Cliff.'), ('Evening', 'Dinner at Brazen.')]},
    'amana-colonies': {
        'day': [('Arrive', 'Land at KIOW early.'), ('Midday', 'The Amana villages.'), ('Afternoon', 'Family-style lunch at the Ox Yoke, then back to the airport.')],
        'extra': [('Morning', 'The woolen mill and Millstream Brewing.'), ('Afternoon', 'Downtown Iowa City and Prairie Lights.'), ('Evening', 'Dinner in downtown Iowa City.')]},
    'rehoboth-lewes': {
        'day': [('Arrive', 'Land at KGED mid-morning.'), ('Midday', 'Walk historic Lewes.'), ('Afternoon', 'Lunch at Dogfish Head, then back to the airport.')],
        'extra': [('Morning', 'Bike Cape Henlopen.'), ('Afternoon', 'The Rehoboth boardwalk.'), ('Evening', 'Dinner at The Pines.')]},
    'bethany-beach': {
        'day': [('Arrive', 'Land at KGED mid-morning.'), ('Midday', 'The Bethany boardwalk.'), ('Afternoon', 'Delaware Seashore State Park, then back to the airport.')],
        'extra': [('Morning', 'Kayak the inland bays.'), ('Afternoon', 'The Fenwick Island lighthouse.'), ('Evening', 'Dinner at Off the Hook.')]},
    'brandywine-valley': {
        'day': [('Arrive', 'Land at KILG mid-morning.'), ('Midday', 'Winterthur.'), ('Afternoon', 'Hagley, then back to the airport.')],
        'extra': [('Morning', 'Longwood Gardens.'), ('Afternoon', 'Nemours Estate.'), ('Evening', 'Dinner at Le Cavalier.')]},
    'dover-de': {
        'day': [('Arrive', 'Land at 33N mid-morning.'), ('Midday', 'The Air Mobility Command Museum.'), ('Afternoon', 'First State Heritage Park, then back to the airport.')],
        'extra': [('Morning', 'Bombay Hook at dawn.'), ('Afternoon', 'The speedway.'), ('Evening', 'Dinner at Grey Fox Grille.')]},
    'moosehead-lake': {
        'day': [('Arrive', 'Land at 3B1 or 52B early.'), ('Midday', 'Watch the floatplanes in the cove.'), ('Afternoon', 'Lunch at Kelly’s Landing, then back to the airport.')],
        'extra': [('Morning', 'A Katahdin cruise.'), ('Afternoon', 'Mount Kineo.'), ('Evening', 'Dinner at Blair Hill.')]},
    'rangeley': {
        'day': [('Arrive', 'Land at 8B0 or M57 early.'), ('Midday', 'A scenic floatplane flight.'), ('Afternoon', 'The Height of Land overlook, then back to the airport.')],
        'extra': [('Morning', 'Paddle Rangeley Lake.'), ('Afternoon', 'Saddleback.'), ('Evening', 'Dinner at Forks in the Air.')]},
    'tavares': {
        'day': [('Arrive', 'Splash in at FA1 or land at KLEE mid-morning.'), ('Midday', 'Wooton Park and lunch downtown.'), ('Afternoon', 'Mount Dora’s antique shops, then back to the base.')],
        'extra': [('Morning', 'A day at Jack Brown’s.'), ('Afternoon', 'Downtown Mount Dora.'), ('Evening', 'Dinner at Pisces Rising.')]},
    'havre-de-grace': {
        'day': [('Arrive', 'Land at 0W3 or M06 mid-morning.'), ('Midday', 'The promenade and the lighthouse.'), ('Afternoon', 'The Decoy Museum, then back to the airport.')],
        'extra': [('Morning', 'Antique shops downtown.'), ('Afternoon', 'The waterfront.'), ('Evening', 'Dinner at MacGregor’s.')]},
    'long-lake-ny': {
        'day': [('Arrive', 'Land at SLK or NY9 mid-morning.'), ('Midday', 'Lunch on the Adirondack Hotel veranda.'), ('Afternoon', 'The town beach or a seaplane ride, then back to the airport.')],
        'extra': [('Morning', 'The Adirondack Experience.'), ('Afternoon', 'Paddle Long Lake.'), ('Evening', 'Dinner in the Victorian Room.')]},
    'lake-wawasee': {
        'day': [('Arrive', 'Land at GSH or 01D mid-morning.'), ('Midday', 'Lunch at the Oakwood Resort on the lake.'), ('Afternoon', 'A lake cruise, then back to the airport.')],
        'extra': [('Morning', 'Shipshewana.'), ('Afternoon', 'Bike the Pumpkinvine.'), ('Evening', 'The tiki bar at sunset.')]},
    'drummond-island': {
        'day': [('Arrive', 'Land at DRM or D22 mid-morning.'), ('Midday', 'Lunch at Pins Bar & Grill.'), ('Afternoon', 'Freighter watching, then back to the airport.')],
        'extra': [('Morning', 'Paddle the heritage water trail.'), ('Afternoon', 'A round at The Rock.'), ('Evening', 'Dinner on the island.')]},
    'gunflint-trail': {
        'day': [('Arrive', "Land at M56 mid-morning (from CKC, the lodge is an hour's drive)."), ('Midday', 'Lunch on the patio at Gunflint Lodge.'), ('Afternoon', 'A short paddle, then back to the airport.')],
        'extra': [('Morning', 'A Boundary Waters paddle.'), ('Afternoon', 'Chik-Wauk at the end of the trail.'), ('Evening', "Dinner at Justine's.")]},
    'aspen': {
        'day': [('Arrive', 'Land at KASE mid-morning.'), ('Midday', 'Lunch downtown.'), ('Afternoon', 'The Silver Queen Gondola, then back to the airport before the afternoon wind.')],
        'extra': [('Morning', 'The Maroon Bells.'), ('Afternoon', 'Shops and galleries downtown.'), ('Evening', 'Dinner at Matsuhisa.')]},
    'santa-fe': {
        'day': [('Arrive', 'Land at KSAF mid-morning.'), ('Midday', 'Lunch at The Shed.'), ('Afternoon', 'The Plaza and Canyon Road, then back to the airport.')],
        'extra': [('Morning', "The O'Keeffe Museum."), ('Afternoon', 'Meow Wolf.'), ('Evening', 'A soak at Ten Thousand Waves.')]},
    'jackson-hole': {
        'day': [('Arrive', 'Land at KJAC mid-morning.'), ('Midday', 'Lunch on the town square.'), ('Afternoon', 'Jenny Lake, then back to the airport.')],
        'extra': [('Morning', 'Wildlife at Oxbow Bend.'), ('Afternoon', 'The tram at Teton Village.'), ('Evening', 'Dinner at Snake River Grill.')]},
    'sun-valley': {
        'day': [('Arrive', 'Land at KSUN mid-morning.'), ('Midday', 'Lunch in Ketchum.'), ('Afternoon', 'The lodge and the ice rink, then back to the airport.')],
        'extra': [('Morning', 'Bald Mountain.'), ('Afternoon', 'A drive toward the Sawtooths.'), ('Evening', 'Dinner at the Pioneer Saloon.')]},
    'moab': {
        'day': [('Arrive', 'Land at KCNY early.'), ('Midday', 'The Windows in Arches (check timed entry).'), ('Afternoon', 'A scenic flight, then home before the heat.')],
        'extra': [('Morning', 'Mesa Arch at sunrise.'), ('Afternoon', 'Dead Horse Point.'), ('Evening', 'Delicate Arch at sunset.')]},
    'sedona': {
        'day': [('Arrive', 'Land at KSEZ mid-morning.'), ('Midday', 'Lunch at the Mesa Grill by the runway.'), ('Afternoon', 'Tlaquepaque, then back to the airport.')],
        'extra': [('Morning', 'Cathedral Rock.'), ('Afternoon', 'A Jeep tour.'), ('Evening', 'Sunset dinner at Mariposa.')]},
    'red-river-gorge': {
        'day': [('Arrive', 'Land at KIOB early and pick up the car.'), ('Midday', 'Natural Bridge and lunch at the lodge.'), ('Afternoon', 'Sky Bridge, then back to the airport.')],
        'extra': [('Morning', 'Chimney Top Rock.'), ('Afternoon', 'The Nada Tunnel drive.'), ('Evening', "Pizza at Miguel's.")]},
    'bowling-green': {
        'day': [('Arrive', 'Land at KBWG mid-morning.'), ('Midday', 'The National Corvette Museum.'), ('Afternoon', 'A boat ride at Lost River Cave, then back to the airport.')],
        'extra': [('Morning', 'A Mammoth Cave tour.'), ('Afternoon', "The park's surface trails."), ('Evening', 'Dinner at 440 Main.')]},
    'buffalo-river': {
        'day': [('Arrive', 'Land at KHRO early and pick up the car.'), ('Midday', 'Lost Valley Trail.'), ('Afternoon', 'Lunch at the Ozark Cafe in Jasper, then back to the airport.')],
        'extra': [('Morning', 'Float from Ponca.'), ('Afternoon', 'Hawksbill Crag.'), ('Evening', 'Elk in the Boxley Valley.')]},
    'mountain-view-ar': {
        'day': [('Arrive', 'Land at 7M2 mid-morning.'), ('Midday', 'Lunch at the Skillet.'), ('Afternoon', 'The Folk Center crafts village, then back to the airport.')],
        'extra': [('Morning', 'Blanchard Springs Caverns.'), ('Afternoon', 'White River trout fishing.'), ('Evening', "Pickin' on the square.")]},
    'glacier-whitefish': {
        'day': [('Arrive', 'Land at KGPI early and pick up the car.'), ('Midday', 'Lake McDonald in Glacier.'), ('Afternoon', 'Downtown Whitefish, then back to the airport.')],
        'extra': [('Morning', 'Going-to-the-Sun Road to Logan Pass.'), ('Afternoon', 'Flathead Lake.'), ('Evening', 'Dinner at Tupelo Grille.')]},
    'bozeman-big-sky': {
        'day': [('Arrive', 'Land at KBZN mid-morning.'), ('Midday', 'Lunch on Main Street.'), ('Afternoon', 'The Museum of the Rockies, then back to the airport.')],
        'extra': [('Morning', 'Yellowstone via Gardiner.'), ('Afternoon', 'Chico Hot Springs.'), ('Evening', 'Dinner at Blackbird.')]},
    'santa-barbara': {
        'day': [('Arrive', 'Land at KSBA mid-morning, after the fog lifts.'), ('Midday', 'The courthouse tower and lunch downtown.'), ('Afternoon', 'Stearns Wharf, then back to the airport.')],
        'extra': [('Morning', 'The Old Mission.'), ('Afternoon', 'Santa Ynez Valley wineries.'), ('Evening', 'Dinner at Bouchon.')]},
    'catalina-island': {
        'day': [('Arrive', 'Land at KAVX mid-morning (8 a.m.–5 p.m. only).'), ('Midday', 'A buffalo burger at the DC-3 Grill.'), ('Afternoon', 'The shuttle to Avalon and back; leave before 5 p.m.')],
        'extra': [('Morning', 'A glass-bottom boat.'), ('Afternoon', 'The Casino and the museum.'), ('Evening', 'Sunset on the pier.')]},
    'palm-springs': {
        'day': [('Arrive', 'Land at KPSP early.'), ('Midday', 'The Palm Springs Air Museum on the field.'), ('Afternoon', 'Lunch downtown, then back to the FBO before the afternoon heat.')],
        'extra': [('Morning', 'The aerial tramway.'), ('Afternoon', 'Pool time.'), ('Evening', 'Sunset in Joshua Tree.')]},
    'san-diego': {
        'day': [('Arrive', 'Land at KMYF mid-morning.'), ('Midday', 'The USS Midway Museum.'), ('Afternoon', 'Lunch on Coronado, then back to the airport.')],
        'extra': [('Morning', 'Balboa Park and the zoo.'), ('Afternoon', 'La Jolla Cove.'), ('Evening', "Dinner at George's at the Cove.")]},
    'monterey-carmel': {
        'day': [('Arrive', 'Land at KMRY late morning, after the fog lifts.'), ('Midday', 'The Monterey Bay Aquarium.'), ('Afternoon', 'Carmel village, then back to the airport.')],
        'extra': [('Morning', 'Point Lobos.'), ('Afternoon', '17-Mile Drive.'), ('Evening', 'Dinner at Passionfish.')]},
    'paso-robles': {
        'day': [('Arrive', 'Land at KPRB mid-morning.'), ('Midday', 'The Estrella Warbirds Museum, then lunch at Fish Gaucho.'), ('Afternoon', 'Two wineries with a driver, then back to the airport.')],
        'extra': [('Morning', 'Wineries west of town.'), ('Afternoon', 'Hearst Castle.'), ('Evening', 'Dinner at Catch.')]},
    'yosemite': {
        'day': [('Arrive', 'Land at KMPI early and pick up the car.'), ('Midday', 'Yosemite Valley and Lower Yosemite Fall.'), ('Afternoon', 'Tunnel View, then back to the airport.')],
        'extra': [('Morning', 'Mariposa Grove.'), ('Afternoon', 'Glacier Point.'), ('Evening', 'Dinner at the Ahwahnee.')]},
    'big-sur': {
        'day': [('Arrive', 'Land at KMRY late morning.'), ('Midday', 'Bixby Bridge and lunch at Nepenthe.'), ('Afternoon', 'Back to Monterey before the evening fog.')],
        'extra': [('Morning', 'McWay Falls.'), ('Afternoon', 'Point Lobos.'), ('Evening', 'Sunset dinner at Sierra Mar.')]},
    'napa-sonoma': {
        'day': [('Arrive', 'Land at KAPC mid-morning.'), ('Midday', 'Lunch at Oxbow Public Market.'), ('Afternoon', 'Two wineries with a driver, then back to the airport.')],
        'extra': [('Morning', 'Wineries up valley.'), ('Afternoon', 'The Wine Train.'), ('Evening', 'Dinner at Bouchon.')]},
    'lake-tahoe': {
        'day': [('Arrive', 'Land at KTRK early, before the afternoon density altitude.'), ('Midday', 'Lunch on the pier at Gar Woods.'), ('Afternoon', 'Sand Harbor, then back to the airport.')],
        'extra': [('Morning', 'Emerald Bay.'), ('Afternoon', 'A paddle from Tahoe City.'), ('Evening', "Dinner at Moody's in Truckee.")]},
    'mendocino': {
        'day': [('Arrive', 'Land at KLLR once the fog lifts.'), ('Midday', 'Walk the headlands and lunch in the village.'), ('Afternoon', 'Point Cabrillo lighthouse, then back to the airport.')],
        'extra': [('Morning', 'The Skunk Train.'), ('Afternoon', 'The botanical gardens.'), ('Evening', 'Dinner at Café Beaujolais.')]},
    'san-francisco': {
        'day': [('Arrive', 'Land at KOAK mid-morning.'), ('Midday', 'BART to the Ferry Building for lunch.'), ('Afternoon', 'A cable-car ride, then back to Oakland.')],
        'extra': [('Morning', 'Alcatraz.'), ('Afternoon', 'The Golden Gate Bridge.'), ('Evening', 'Dinner at Tadich Grill.')]},
    'san-juan-islands': {
        'day': [('Arrive', 'Land at KFHR or W33 mid-morning.'), ('Midday', 'Walk into town and the Whale Museum.'), ('Afternoon', 'Lime Kiln Point for whales, then back to the airport.')],
        'extra': [('Morning', 'English Camp.'), ('Afternoon', 'Roche Harbor.'), ('Evening', "Dinner at McMillin's.")]},
    'hood-river': {
        'day': [('Arrive', 'Land at 4S2 mid-morning, before the wind builds.'), ('Midday', 'WAAAM on the airport.'), ('Afternoon', 'Lunch downtown, then back to the airport.')],
        'extra': [('Morning', 'The Fruit Loop.'), ('Afternoon', 'Multnomah Falls.'), ('Evening', 'Dinner at Celilo.')]},
    'willamette-valley': {
        'day': [('Arrive', 'Land at KMMV mid-morning.'), ('Midday', 'The Spruce Goose next door.'), ('Afternoon', 'Two Dundee Hills wineries, then back to the airport.')],
        'extra': [('Morning', 'Wineries with a driver.'), ('Afternoon', 'The spa at the Allison.'), ('Evening', 'Dinner at the Joel Palmer House.')]},
    'oregon-coast': {
        'day': [('Arrive', 'Land at KAST mid-morning.'), ('Midday', 'The Columbia River Maritime Museum and lunch on the waterfront.'), ('Afternoon', 'The Astoria Column, then back to the airport.')],
        'extra': [('Morning', 'Haystack Rock at low tide.'), ('Afternoon', 'Ecola State Park.'), ('Evening', 'Dinner in Cannon Beach.')]},
    'talkeetna-denali': {
        'day': [('Arrive', 'Land at PATK mid-morning.'), ('Midday', 'A Denali flightseeing tour with a glacier landing.'), ('Afternoon', 'Main Street and pie at the Roadhouse, then back to the airport.')],
        'extra': [('Morning', 'A river walk.'), ('Afternoon', 'A second flightseeing route or a float trip.'), ('Evening', 'Dinner at Denali Brewing.')]},
    'homer': {
        'day': [('Arrive', 'Land at PAHO or 5BL mid-morning.'), ('Midday', 'Lunch on the Spit.'), ('Afternoon', 'Eagles and otters at the harbor, then back to the airport.')],
        'extra': [('Morning', 'A halibut charter.'), ('Afternoon', 'The ferry to Halibut Cove.'), ('Evening', 'Dinner at the Saltry.')]},
    'seward': {
        'day': [('Arrive', 'Land at PAWD early.'), ('Midday', 'A half-day glacier and wildlife cruise.'), ('Afternoon', 'The SeaLife Center, then back to the airport.')],
        'extra': [('Morning', 'Exit Glacier.'), ('Afternoon', 'A longer fjords cruise.'), ('Evening', "Dinner at Ray's Waterfront.")]},
    'ketchikan': {
        'day': [('Arrive', 'Land at PAKT or 5KE mid-morning.'), ('Midday', 'Misty Fjords by floatplane.'), ('Afternoon', 'Creek Street, then back to the airport.')],
        'extra': [('Morning', 'Totem Bight.'), ('Afternoon', 'Saxman totem poles.'), ('Evening', "Dinner at Annabelle's.")]},
    'juneau': {
        'day': [('Arrive', 'Land at PAJN mid-morning.'), ('Midday', 'Mendenhall Glacier and Nugget Falls.'), ('Afternoon', 'King crab downtown, then back to the airport.')],
        'extra': [('Morning', 'Whale watching.'), ('Afternoon', 'The Mount Roberts tram.'), ('Evening', 'Dinner downtown.')]},
    'fairbanks': {
        'day': [('Arrive', 'Land at PAFA mid-morning.'), ('Midday', 'The Riverboat Discovery.'), ('Afternoon', 'Lunch on the river, then back to the airport.')],
        'extra': [('Morning', 'Drive to Chena Hot Springs.'), ('Afternoon', 'A soak and the ice museum.'), ('Evening', 'Aurora watching (late August to April).')]},
    'las-vegas': {
        'day': [('Arrive', 'Land at KHND mid-morning.'), ('Midday', 'Lunch at the Landings on the field, then the Strip.'), ('Afternoon', 'The Neon Museum, then back to the airport.')],
        'extra': [('Morning', 'Valley of Fire.'), ('Afternoon', 'Pool time.'), ('Evening', 'A show and dinner.')]},
    'boulder-city': {
        'day': [('Arrive', 'Land at KBVU early.'), ('Midday', 'A Hoover Dam tour.'), ('Afternoon', 'The historic district, then back to the airport.')],
        'extra': [('Morning', 'A Grand Canyon air tour.'), ('Afternoon', 'Lake Mead.'), ('Evening', 'Sunset from the bypass bridge.')]},
    'reno-virginia-city': {
        'day': [('Arrive', 'Land at KRNO mid-morning.'), ('Midday', 'Virginia City.'), ('Afternoon', 'The steam train, then back to the airport.')],
        'extra': [('Morning', 'The Nevada Museum of Art.'), ('Afternoon', "Lake Tahoe's north shore."), ('Evening', "Dinner at Louis' Basque Corner.")]},
    'great-basin': {
        'day': [('Arrive', 'Land at KELY early and pick up the car.'), ('Midday', 'Lehman Caves tour.'), ('Afternoon', 'Back to Ely and the airport.')],
        'extra': [('Morning', 'The bristlecone trail.'), ('Afternoon', 'A steam train in Ely.'), ('Evening', 'Stargazing in the park.')]},
    'redwood-coast': {
        'day': [('Arrive', 'Land at KACV once the fog lifts.'), ('Midday', 'Prairie Creek redwoods and the elk meadows.'), ('Afternoon', 'Old Town Eureka, then back to the airport.')],
        'extra': [('Morning', 'Fern Canyon.'), ('Afternoon', "Trinidad's harbor and lighthouse."), ('Evening', 'Dinner at Restaurant 301.')]},
    'mount-shasta': {
        'day': [('Arrive', 'Land at O46 mid-morning.'), ('Midday', 'The McCloud River falls.'), ('Afternoon', 'Lake Siskiyou, then back to the airport.')],
        'extra': [('Morning', 'Everitt Memorial Highway.'), ('Afternoon', 'Mount Shasta city.'), ('Evening', 'Dinner at the McCloud Hotel.')]},
    'crater-lake': {
        'day': [('Arrive', 'Land at KLMT early.'), ('Midday', 'Drive to the rim and lunch at the lodge.'), ('Afternoon', 'Part of the Rim Drive, then back to the airport.')],
        'extra': [('Morning', 'A boat tour to Wizard Island.'), ('Afternoon', 'Garfield Peak.'), ('Evening', 'Dinner at Crater Lake Lodge.')]},
    'ashland': {
        'day': [('Arrive', 'Land at S03 mid-morning.'), ('Midday', 'Lithia Park and lunch downtown.'), ('Afternoon', 'A matinee, then back to the airport.')],
        'extra': [('Morning', 'Rogue Valley wineries.'), ('Afternoon', 'Jacksonville.'), ('Evening', 'Dinner at Amuse and a play.')]},
    'bend-sunriver': {
        'day': [('Arrive', 'Land at S21 mid-morning.'), ('Midday', 'Lunch at the resort and a bike ride.'), ('Afternoon', 'The High Desert Museum, then back to the airport.')],
        'extra': [('Morning', 'Lava Butte.'), ('Afternoon', 'Mount Bachelor.'), ('Evening', 'Dinner at Pine Tavern in Bend.')]},
    'lanai': {
        'day': [('Arrive', 'Land at PHNY mid-morning (one-hour ramp limit without permission).'), ('Midday', 'Lunch in Lanai City.'), ('Afternoon', 'Hulopoe Bay, then back to the airport.')],
        'extra': [('Morning', 'Snorkel Hulopoe Bay.'), ('Afternoon', 'Keahiakawelo by jeep.'), ('Evening', 'Dinner at the resort.')]},
    'hana': {
        'day': [('Arrive', 'Land at PHHN mid-morning.'), ('Midday', 'Waianapanapa black-sand beach (reservation).'), ('Afternoon', 'Lunch in Hana, then back to the airport.')],
        'extra': [('Morning', 'The Pipiwai Trail at Kipahulu.'), ('Afternoon', 'The resort spa.'), ('Evening', 'Dinner at the resort.')]},
    'molokai': {
        'day': [('Arrive', 'Land at PHMK mid-morning.'), ('Midday', 'The Kalaupapa lookout at Palaau State Park.'), ('Afternoon', 'Kaunakakai, then back to the airport.')],
        'extra': [('Morning', 'The east end toward Halawa.'), ('Afternoon', 'The wharf.'), ('Evening', 'Dinner at Hotel Molokai.')]},
    'kauai': {
        'day': [('Arrive', 'Land at PHLI early.'), ('Midday', 'Waimea Canyon overlooks.'), ('Afternoon', 'Lunch in Poipu, then back to the airport.')],
        'extra': [('Morning', 'A Na Pali boat trip.'), ('Afternoon', 'Hanalei.'), ('Evening', "Dinner at Merriman's.")]},
    'kona': {
        'day': [('Arrive', 'Land at PHKO mid-morning.'), ('Midday', 'Puuhonua o Honaunau.'), ('Afternoon', 'A Kona coffee farm, then back to the airport.')],
        'extra': [('Morning', 'Drive to Hawaii Volcanoes National Park.'), ('Afternoon', 'Kilauea crater.'), ('Evening', 'A manta-ray night snorkel.')]},
    'galveston': {
        'day': [('Arrive', 'Land at KGLS mid-morning.'),
                ('Midday', 'The Strand and lunch on the seawall.'),
                ('Afternoon', 'Bishop’s Palace, then back to the FBO.')],
        'extra': [('Morning', 'Moody Gardens.'),
                  ('Afternoon', 'A dolphin boat tour in the harbor.'),
                  ('Evening', 'Sunset on the seawall.')]},
    'south-padre': {
        'day': [('Arrive', 'Land at KPIL early and cross the causeway.'),
                ('Midday', 'Sea Turtle, Inc. and lunch by the bay.'),
                ('Afternoon', 'The beach, then back to the airport.')],
        'extra': [('Morning', 'A fishing charter in the Gulf.'),
                  ('Afternoon', 'Laguna Atascosa National Wildlife Refuge.'),
                  ('Evening', 'A sunset bay cruise.')]},
    'marfa': {
        'day': [('Arrive', 'Land at KMRF early in the cool air.'),
                ('Midday', 'A Chinati tour and lunch in town.'),
                ('Afternoon', 'Prada Marfa, then fly before afternoon heat and winds.')],
        'extra': [('Morning', 'Davis Mountains State Park.'),
                  ('Afternoon', 'Balmorhea State Park’s spring-fed pool.'),
                  ('Evening', 'A second observatory star party.')]},
}
STYLE_RE = re.compile(r'<span>WEEKEND STYLE</span><strong(?: data-style data-transport="[^"]*")?>Two nights <small>· ([^<]+)</small></strong>')


def block(kind, title, eyebrow, items):
    lis = ''.join(f'<li><strong>{t}</strong><p>{p}</p></li>' for t, p in items)
    return (f'<div class="trip-plan" data-trip="{kind}" hidden><span class="eyebrow">{eyebrow}</span>'
            f'<h3>{title}</h3><ol>{lis}</ol></div>')


for path in map(Path, sys.argv[1:]):
    slug = path.parent.name
    if slug not in PLANS:
        print('skip (no plans):', path)
        continue
    s = path.read_text()
    s = re.sub(r'<div class="trip-plan".*?</ol></div>', '', s)
    m = STYLE_RE.search(s)
    if not m:
        sys.exit(f'weekend style not found in {path}')
    s = s.replace(m.group(0), f'<span>WEEKEND STYLE</span><strong data-style data-transport="{m.group(1)}">Two nights <small>· {m.group(1)}</small></strong>', 1)
    p = PLANS[slug]
    day = block('Day trip', 'Just for the day', 'Day trip version', p['day'])
    extra = block('Longer stay', 'With an extra day', 'Longer stay · Add a day', p['extra'])
    i = s.index('<section id="itinerary">')
    j = s.index('<div class="days">', i)
    s = s[:j] + day + s[j:]
    k = s.index('</section>', j)
    s = s[:k] + extra + s[k:]
    path.write_text(s)
    print('trip plans added:', path)
