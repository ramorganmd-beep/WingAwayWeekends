# WingAway Weekends — Project Notes

Updated: November 1, 2026 (after migration from ChatGPT to Claude and GitHub Pages).

## Goals and agreed direction

WingAway Weekends helps general aviation pilots and their travel companions discover worthwhile short getaways. The experience connects an appealing destination with practical arrival, lodging, dining and activity information, with an initial emphasis on couples.

The agreed MVP is a curated discovery homepage with 5–10 handpicked destinations from KMYR and only 1–2 developed guides. The current site contains ten destination cards and guides for all twelve destinations. Automatic recommendations for every airport are outside the current MVP.

The design uses navy, cream and gold, an aspirational destination hero photograph, the headline “Where will your wings take you this weekend?”, prominent airport and flight-time controls, and destination cards. ForeFlight remains the pilot’s operational flight-planning tool; WingAway provides destination discovery rather than weather, routing or dispatch decisions.

## Current source and publication status

- **Source of truth:** this GitHub repository, `ramorganmd-beep/WingAwayWeekends` (public). The project moved from ChatGPT to Claude on November 1, 2026. Older ChatGPT ZIPs and chats are history, not competing baselines.
- **Live site:** https://wingawayweekends.com (also www.wingawayweekends.com) — Cloudflare Pages project `wingawayweekends`, connected to this repository: production branch `main`, no build command, output directory `docs`. Any change merged into `main` goes live within a minute or two. The domain is registered with Cloudflare; both custom domains were activated November 1, 2026. Test address: https://wingawayweekends.pages.dev.
- **Backup host:** GitHub Pages (https://ramorganmd-beep.github.io/WingAwayWeekends/) also publishes `docs/` from `main`, unless it has been turned off in the repository settings.
- **Workflow:** Claude makes changes on a separate branch and pushes it; the user reviews and merges the pull request on GitHub. Shorthand: when the owner writes “lg” (“looks good”) about a guide, mark that guide Reviewed. After a merge, a hard refresh (Cmd + Shift + R on Mac; pull down or a Private tab on iPhone/iPad) shows the new version; Cloudflare’s Purge Everything is rarely needed.
- The ten-photo set, including the four replacements (Asheville, Key West, Pinehurst, Greenville), was **approved and published** on November 1, 2026.
- The site is public; the ChatGPT-hosted access gate no longer applies. Review pages (`photo-review.html`, `mobile-review.html`) are marked `noindex`.
- **Former hosting (retired):** ChatGPT Sites at https://wingaway-savannah.ramorganmd.chatgpt.site (project `appgprj_6abe9d437ef8819196353f64245055a8`, last confirmed version 7). It no longer receives updates and can be left or deleted.

## Features built

### Discovery homepage

- Responsive hero and destination-card grid, with layouts for desktop, tablet and mobile.
- Departure airport input (default KMYR) covering 695 public airports in NC, SC, GA, FL, VA, TN and AL, with suggestions as you type. It accepts K-codes (KCHS), codes without the K (CHS) and 3-character FAA IDs (2J9). Airports outside the region show a “coming soon” message. A destination is hidden if it is the home airport or within 40 NM of it.
- Maximum estimated flight time offers 1 to 4½ hours in half-hour steps plus “Any distance” (shows all twelve, added November 2, 2026) for every trip length (changed November 1, 2026 at the owner’s request). Trip length only sets the starting value: Day trip 1½ hours, Weekend 3 hours (page default), Longer stay 4½ hours. Changing trip length resets flight time to that default.
- Interest checkboxes, in this order: Boutique stays, Dining, Wine, Spa, Romance, History, Outdoors, Hiking, Golf and Aviation museums. Aviation museums is currently tagged on Savannah (Mighty Eighth Air Force Museum) Charleston (Patriots Point / USS Yorktown) and Asheville (Western North Carolina Air Museum, Hendersonville); other destinations need review before tagging.
- Multiple selected interests use AND matching: a destination must have every selected tag.
- Live result count and an empty-state message when nothing matches.
- **Review status:** Reviewed by the owner: Charleston, Nashville, Beaufort, Charlottesville, Greenville, Pinehurst, Asheville, Outer Banks, Amelia Island, Yadkin Valley, Virginia Hunt Country, Dahlonega, St. Augustine, Key West, Harpers Ferry, Lake Lanier, Lake Lure, Great Smoky Mountains, Lake Keowee & Jocassee, Chattanooga and Gulf Shores (all “Reviewed November 2, 2026”; header “Destination guide”, footer “Couples guide”). All other guides are still “Draft for review”; review them one at a time the same way. To mark a guide reviewed, set `REVIEWED = 'Month D, YYYY'` in its build script and pass `reviewed=REVIEWED` to `page_start` and `page_end` (see `build_nashville.py`), then rerun the pipeline. Charleston, Pinehurst and Asheville have standalone builders, so their header, closing note and footer are edited directly.
- **Hotel and restaurant links (November 2, 2026):** every hotel and restaurant card links out. Picks with a confirmed official site show “Official details”; the rest show “Website & map”, a Google Maps search for the place (website, phone, hours), added by `tools/guides/maplinks.py`. Replace these with official links as each guide is reviewed.
- **Interests (November 2, 2026):** the “What makes a great getaway?” buttons are a uniform grid (5 across on desktop, 3 on tablets, 2 on phones; longer names wrap). Hiking was added and tagged on Asheville, Greenville and Charlottesville.
- **Feedback (November 2, 2026):** hello@wingawayweekends.com is a Cloudflare Email Routing address that forwards to the owner’s Gmail. Every page’s footer has “Help us improve and grow.” with a link to it, directly under the WingAway Weekends name, and each guide’s review note links to it too; each email’s subject names the page. Cloudflare Web Analytics is enabled on the Pages project (Metrics tab).
- **Aircraft profiles (November 1, 2026):** an “Aircraft performance” panel on the homepage, placed right after Departure airport and before flight time and trip length (`docs/aircraft.js`) with example presets (C172S, PA-28-181 Archer, SR22, Bonanza A36, Mooney M20J, TBM 960) and a Custom option. Every field is editable: cruise KTAS, cruise gal/hr, climb/descent/taxi minutes and gallons, usable fuel and reserve (default 45 min). Changes preview on the cards immediately but are only kept when the visitor taps “Save my numbers” (a status line shows unsaved changes); “Use the default estimate” clears the profile. Guides use the saved profile. With a profile, block time = distance ÷ KTAS + allowance; trip fuel = cruise time × gal/hr + allowance gallons; “Fuel stop likely” when trip fuel + reserve exceeds usable fuel. Cards show time and gallons; the flight-time filter uses the profile; guides show time, trip fuel or the fuel-stop warning in the route box. Without a profile, the original 150 KTAS + 15 min model applies and no fuel is shown. Straight-line, no wind; not a flight plan. Possible next steps: winds aloft, a pilot-entered fuel price.
- Every guide has a “Luxury alternatives” row under Where to stay (added November 1, 2026; picks in `tools/guides/luxury.py`, Charleston’s in its build script).
- All twelve cards link to their guides (four rows of three). The whole card is clickable (a stretched link over the card, with a hover lift and keyboard focus ring), not just “Explore destination”.
- Guide links carry the home airport (`?from=KPDK`), and the homepage remembers the last airport used (browser storage). Each guide’s route box then shows the distance and time from that airport, or “Drive instead” within 40 NM. Visitors who never entered an airport see the KMYR figures.
- Trip length also carries into the guides (`&trip=` on card links, and the homepage remembers the last choice). Longer stay relabels the route box “Three nights +” and shows a “With an extra day” plan after the itinerary; Day trip relabels it “Day trip” and shows a “Just for the day” plan above the itinerary. Weekend shows the standard two-night guide.

| Destination | Arrival airport | Photograph in latest review source |
| --- | --- | --- |
| Savannah | KSAV | Forsyth Park fountain |
| Charleston | KCHS | Rainbow Row |
| Asheville | KAVL | Biltmore House mansion |
| Beaufort | KARW | Salt marsh and Intracoastal Waterway |
| St. Augustine | KSGJ | Waterfront/city view from the lighthouse |
| Charlottesville | KCHO | Downtown Mall |
| Greenville | KGMU | Reedy River waterfall and Liberty Bridge |
| Pinehurst | KSOP | Pinehurst No. 4 golf course |
| Nashville | KJWN | Skyline and Cumberland River |
| Key West | KEYW | Duval Street |

### Flight-time behavior

The estimate is great-circle distance in nautical miles divided by 150 knots, plus 0.25 hour. It has no wind, route, terrain, altitude, aircraft-specific climb/descent or ATC adjustment. Filtering uses the unrounded estimate. Card labels show hours and minutes, rounded *up* to the next minute (for example “~3 hr 3 min”), so a label never looks inside a cutoff that excludes the destination.

Nashville uses John C. Tune (KJWN), as requested. Its estimate is about 3.046 hours (label “~3 hr 3 min”): excluded at 2 and 3 hours, included at 3½ hours. The earlier request to include Nashville at 3 hours was superseded by the decision to use KJWN and keep the strict cutoff.

Key West estimates about 4 hours (label “~4 hr 2 min”), so it appears from KMYR only when flight time is set to 4½ hours.

### Savannah guide

The developed guide covers FBO comparisons, arrival/ground transport, hotels, restaurants, attractions and boat outings, spa options, shopping, wine, breweries, sports/events links, a suggested weekend itinerary and practical booking considerations. It contains official-source links and explanatory notes, but no live pricing, availability or booking functionality. Refreshed November 1, 2026: the October 2026 trip dates became a sample Friday–Sunday itinerary; stale spa prices were removed; a note was added that Spa Bleu may be weekday-only, so Saturday appointments need confirming; the unverifiable “Savannah Underground” item was removed; Savannah Steel was updated (UPSHOT League, first season summer 2026); and the flight-time snapshot now uses the discovery page’s model (~1 hr 15 min).

### Charleston guide (draft, added November 1, 2026)

`docs/charleston/` follows the Savannah guide’s structure and styling: KCHS arrival with Atlantic Aviation and Signature, three stays (The Ansonborough, formerly the Ansonborough Inn, replacing Zero George at the user’s request; Wentworth Mansion; The Vendue), plus a “Luxury alternatives” row: The Charleston Place (charlestonplace.com), Hotel Bennett and The Cooper (thecooper.com) (new harborfront hotel, spring 2026; replaced The Dewberry at the owner’s request), FIG (Friday dinner), Rappahannock Oyster Bar (Saturday afternoon happy hour before the sunset sail), Chez Nous (later Saturday dinner) and Husk (Sunday brunch); Rappahannock replaced Leon’s and the slots were swapped at the owner’s request, things to do in the owner’s order (King Street shopping; the Battery, Waterfront Park and Rainbow Row; Patriots Point and the USS Yorktown; Fort Sumter; a foodie walking tour; an evening carriage ride before Friday dinner; Gibbes Museum and Middleton Place removed), Schooner Pride sunset sail, The Spa at The Charleston Place, King Street shopping, wine bars, breweries, RiverDogs / Stingrays / Battery and a sample Friday–Sunday itinerary. The hero uses the existing Rainbow Row card photo (CC0).

Research was done through web search only; the research environment could not open venue websites. Facts confirmed in search results include Patriots Point admission contents and hours, the Fort Sumter ferry departure points and duration, Atlantic Aviation’s CHS address and phone, the Charleston Place spa address and phone, and Schooner Pride’s departure point and sail length. **These official links were written from known domains but not opened, so click-check them:** eatatfig.com (corrected), cheznouschs.com, rroysters.com, huskrestaurant.com, hallschophouse.com, gibbesmuseum.org, middletonplace.org, croghansjewelbox.com, graftchs.com, edmundsoast.com, thevendue.com, wentworthmansion.com, charleston.com/schooner-pride, the Signature CHS page and the Belmond spa page. Signature’s address and phone are omitted because directory listings conflict.

### Asheville guide (draft, added November 1, 2026)

`docs/asheville/` uses the same format. KAVL has one FBO (Signature, 40 Lindbergh Lane, 828-687-7110); the airport is removing some GA hangars for a terminal expansion, so the guide tells pilots to confirm transient parking. The guide recommends a rental car. Picks: Omni Grove Park Inn, The Inn on Biltmore Estate and Kimpton Hotel Arras; Cúrate, Chai Pani and Corner Kitchen; Biltmore Estate and winery; the Western North Carolina Air Museum in Hendersonville (free, limited days); the Blue Ridge Parkway; downtown and the River Arts District; the Grove Park Inn spa; Sierra Nevada in Mills River; and the Asheville Tourists. The guide notes Hurricane Helene recovery: some restaurants (for example Rhubarb) closed permanently, so only places with recent evidence of being open were chosen. Same caveat as Charleston: links were written from known domains but not opened, so click-check them.

### Pinehurst guide (draft, added November 1, 2026)

`docs/pinehurst/` uses the same format. KSOP (Moore County Airport) has one county-run FBO, 910-692-3212, with transient tiedowns, hangars and courtesy cars listed. Ground transport needs arranging ahead because rideshare is scarce. Picks: The Carolina, The Holly Inn and Mid Pines Inn; Villaggio (Friday), Elliotts on Linden (Saturday) and Pinehurst Brewing Co. (lunch); Pinehurst No. 2 (resort guests), The Cradle and Thistle Dhu, the village, downtown Southern Pines, Mid Pines and Pine Needles; The Spa at Pinehurst; The Deuce; Southern Pines Brewing and Railhouse; and the U.S. Open (next in 2029). Several picks have no website link because official addresses could not be confirmed.

### Beaufort, St. Augustine and Greenville guides (drafts, added November 1, 2026)

- **Beaufort photo (November 1, 2026):** the marsh photo was replaced with “Bay Street Downtown Beaufort.JPG” (public domain, 2009), cropped to the storefronts to remove most of the roadway (cropping only, no retouching; some parked cars remain). The homepage card and guide hero use `object-position: 50% 65%` so the storefronts show in wide frames; set per photo with `"pos"` in `destinationPhotos` and `img_style` in the guide builder. License evidence: `licenses/beaufort-bay-street-evidence.json`.
- **Beaufort (`docs/beaufort/`):** KARW is now named Beaufort Executive Airport and runs its own FBO (843-255-2972, courtesy car, shorter weekend hours). Picks: Anchorage 1770, The Rhett House Inn and The Beaufort Inn; Saltus River Grill, Ribaut Social Club and Plums; the historic district and waterfront park, carriage tours, Hunting Island, the Penn Center, the Spanish Moss Trail and the Parris Island Museum (base access rules apply). No spa or brewery picks were verified.
- **St. Augustine (`docs/st-augustine/`):** KSGJ, Atlantic Aviation (904-824-1995) plus self-serve fuel. Picks: Casa Monica (and its spa), The Collector and St. Francis Inn; Collage, The Ice Plant Bar and The Columbia; Castillo de San Marcos, the lighthouse, Flagler College, St. George Street and a Matanzas Bay sunset; San Sebastian Winery and the St. Augustine Distillery; Nights of Lights.
- **Greenville (`docs/greenville/`):** KGMU, Vantage Aviation (formerly Greenville Jet Center, 864-232-7100). Picks: Grand Bohemian Lodge, The Westin Poinsett and Hotel Hartness; Jianna, Scoundrel (Michelin star) and Soby’s; Falls Park, the Swamp Rabbit Trail, Unity Park and Main Street; the Greenville Drive, the Peace Center and Fall for Greenville. No spa section.

### Charlottesville, Nashville and Key West guides (drafts, added November 1, 2026)

- **Charlottesville (`docs/charlottesville/`):** KCHO, Signature (phone listings conflict, so none is shown). Rental car needed. Picks: Keswick Hall, Boar’s Head Resort and Oakhurst Inn; The Alley Light, Oakhart Social and C&O; Monticello, UVA, the Downtown Mall and the Blue Ridge; Barboursville and King Family Vineyards; Foxfield Races.
- **Nashville (`docs/nashville/`):** KJWN, Contour Flight Support (615-350-5000; tower listed 7 AM–9 PM; Atlantic Aviation building a second FBO). Picks: The Hermitage Hotel, Omni Nashville (Mokara Spa) and Germantown Inn; Boqueria (Friday), Locust (Saturday) and Rolf & Daughters as the alternative (changed at the owner’s request); Broadway honky-tonks first, then the Ryman, the Opry, the Country Music Hall of Fame and Germantown; a downtown Shopping section (Fifth + Broadway, Lower Broadway boot shops, Hatch Show Print, The Arcade; Third Man Records nearby); the Predators.
- **Key West (`docs/key-west/`):** KEYW, Signature only (305-296-5422). The guide warns about high fuel and parking fees, the 9 PM closing fee, overwater flying, nearby military airspace and the need for a fuel stop. Picks: The Marquesa, Casa Marina, H2O Suites or Almond Tree; Latitudes, Hot Tin Roof and First Flight (Pan Am’s first ticket office, 301 Whitehead St.); the Dry Tortugas seaplane, Mallory Square and Old Town. Its day-trip plan says plainly that Key West is not a day trip from most of the Southeast.

### Outer Banks and Amelia Island guides (drafts, added November 2, 2026)

- **Outer Banks (`docs/outer-banks/`):** based at KMQI, Dare County Regional (county FBO, 252-475-5575, courtesy and rental cars), at the owner’s request; KFFA at the Wright Brothers National Memorial is offered only as an optional short hop with its caveats (3,000 ft, no fuel, deer, parking limits). Picks: The White Doe Inn, Tranquil House Inn and The Sanderling; 1587, Blue Point and Salt & Cypress; the memorial, Jockey’s Ridge, Manteo’s waterfront, The Lost Colony and Bodie Island Lighthouse. Photo: NASA on The Commons (first-flight boulder and monument), no known copyright restrictions.
- **Amelia Island (`docs/amelia-island/`):** KFHB, Bent Wing Flight Services (904-849-4321, crew car). Picks: The Ritz-Carlton, Omni Amelia Island and Elizabeth Pointe Lodge; David’s, España and Burlingame; Centre Street and the Palace Saloon, Fort Clinch, beach horseback rides and river sunsets. Photo: “Centre Street Businesses” by Upstateherd, CC BY-SA 4.0.
- **Wine destinations (added November 2, 2026), tagged Wine.** Each wine guide has a “Wineries” section and a pilot note on wine and flying (`wine_and_flying()` in `guide_helpers.py`: 14 CFR 91.17's 8 hours and 0.04%, a 12–24 hour personal minimum, taste on the non-flying day). Their hero and card images are **illustrated placeholders** (`*-vineyard-480/960`), drawn by us, until real photos are chosen; `photos.json` marks them `"placeholder": true`.
  - **Yadkin Valley (`docs/yadkin-valley/`, 13):** KZEF Elkin, Yadkin Valley Aviation (336-366-3433, courtesy car, daytime hours). Stay: Elkin Creek Vineyard cabins, The Rockford Inn, Hampton Inn & Suites at Shelton Vineyards. Eat: JOLO, Harvest Grill at Shelton, Elkin Creek pizza. Wineries: Shelton, Raffaldini, JOLO, Jones von Drehle, Elkin Creek, Carolina Heritage. Elkin Vine Line shuttle.
  - **Virginia Hunt Country (`docs/hunt-country/`, 14):** KJYO Leesburg (inside the DC SFRA; Kuhn Jet Center 703-665-3000) with KHWY Warrenton-Fauquier (outside the SFRA; 540-422-8285) as the alternative. Stay: Salamander Middleburg, Red Fox Inn, Goodstone Inn. Eat: Red Fox, The Conservatory at Goodstone, The Inn at Little Washington. Wineries: Boxwood, Cana, Greenhill, 50 West, Chrysalis, Slater Run. Udvar-Hazy Center.
  - **Dahlonega (`docs/dahlonega/`, 15):** KGVL Gainesville, Champion Aviation (770-532-4136; no courtesy car, rent one). Stay: Hall House Hotel, Dahlonega Square Hotel, Dahlonega Resort and Vineyard. Eat: Montaluce, Bourbon Street Grille, Crimson Moon. Wineries: Wolf Mountain, Montaluce, Frogtown, Kaya, Cavender Creek, square tasting rooms. Spa: Mountain Laurel Creek Inn.
  - **Nashville** gained an Arrington Vineyards wine side trip (Things to do #6) and the Wine tag.
- **Alabama and Tennessee guides (added November 2, 2026)**, also with illustrated placeholder images (`gulf-shores-beach`, `chattanooga-river`, `smoky-mountains-ridges`) until photos are chosen:
  - **Gulf Shores (`docs/gulf-shores/`, 16):** KJKA, Gulf Air Center (251-968-5200, crew cars). Stay: The Lodge at Gulf State Park, Turquoise Place, Perdido Beach Resort. Eat: Voyagers, Perch, Doc's Seafood Shack. National Naval Aviation Museum (check base-access rules), Gulf State Park, Fort Morgan. About 3½ hours from KMYR, so it appears with the 3½-hour or longer settings.
  - **Chattanooga (`docs/chattanooga/`, 17):** KCHA (Class C), Wilson Air Center (423-855-2299). Stay: The Edwin, The Read House, The Dwell. Eat: Easy Bistro, St. John's, Calliope. Lookout Mountain, Walnut Street Bridge, Tennessee Aquarium.
  - **Great Smoky Mountains (`docs/smoky-mountains/`, 18):** KGKT Sevierville (865-453-8393; no courtesy car, Enterprise on call); KTYS for Blackberry Farm. Stay: Buckhorn Inn, Old Creek Lodge, Dancing Bear Lodge; luxury Blackberry Farm and Blackberry Mountain. Eat: The Peddler, Dancing Bear Appalachian Bistro, a Cades Cove picnic. Park parking tags required.
- **Lake guides (added November 2, 2026)**, with illustrated placeholders (`lake-lure-gorge`, `lake-jocassee`, `lake-lanier`):
  - **Lake Lure (`docs/lake-lure/`, 19):** KFQD Rutherford County (828-287-0800; courtesy car, daytime hours). Written around Hurricane Helene recovery: lake reopened May 2026 with temporary rules, Chimney Rock State Park reopened 2025, Lake Lure Inn under new owners with renovations through 2026–27. Recheck status when reviewing.
  - **Lake Keowee & Jocassee (`docs/lake-keowee/`, 20):** Alternative airport KLQK Pickens County (240 Airport Road, Liberty, SC 29657; 864-843-5803; Titan fuel, courtesy car, about 8–5). The route box and homepage card still use KCEU. Photo: Lake Keowee in morning mist by Andy Montgomery, CC BY-SA 2.0, via Wikimedia Commons (`lake-keowee-morning`; Commons file “Lake Keowee (reservoir) in South Carolina.jpg”, 5634 × 2203; cropped from the 3840px Commons rendition). KCEU Clemson (864-882-2959; crew car, Hertz/Enterprise). Lake-house rentals, Devils Fork State Park villas, Fairfield Inn on Keowee; The Lighthouse, Tiki Hut, Copper River Grill; Jocassee waterfall boat tours, Whitewater Falls, Table Rock.
  - **Lake Lanier (`docs/lake-lanier/`, 21):** KGVL (same as Dahlonega; no courtesy car). Lanier Islands Legacy Lodge; Luna's, CHR Steak, Sidney's; pontoon day, Lake Lanier Olympic Park; links to the Dahlonega guide.
- Both photos were supplied by the owner as screenshots of the Commons originals because Commons downloads were rate-limited from the build environment. Builder photo data is in `tools/guides/photos.json`.

### Guide tools

`tools/guides/` (not published) holds the scripts that generate the guide pages: `guide_helpers.py` (shared markup and page template) and `build_<guide>.py` for every guide except Savannah, which is hand-written HTML. After rebuilding a guide, run `python3 tools/guides/personalize.py docs/<guide>/index.html` then `python3 tools/guides/trip_plans.py docs/<guide>/index.html`, then `python3 tools/guides/luxury.py docs/<guide>/index.html`, then `python3 tools/guides/maplinks.py docs/<guide>/index.html`, then `python3 tools/guides/feedback.py docs/<guide>/index.html` to restore the home-airport route box, the trip-length plans the “Luxury alternatives” row, the hotel and restaurant map links and the feedback links (Charleston’s luxury row is in its build script instead). Day-trip and extra-day content for every guide lives in `trip_plans.py`; add an entry there when a new guide is built. Edit the build script rather than the generated HTML, so later rebuilds keep the change.

### Photography and review tools

All ten cards have downloaded destination photographs with recorded commercial reuse licenses. The last update replaced only Asheville, Key West, Pinehurst and Greenville. The other six photo sets were verified byte-for-byte unchanged against the attached source ZIP.

Images use WebP with JPEG fallbacks, responsive `srcset`, descriptive alternative text, lazy loading and asynchronous decoding. All cards have 480px and 960px image versions; the four replacement sets also have 1600px versions. Credits record photographer, title, source links, license requirements, modification notes, file sizes and checksums. ShareAlike photo adaptations retain their source license. None of the four selected replacement licenses was left unverified.

`photo-review.html` shows all ten cards for visual review, intentionally bypassing discovery filtering on that page only. A mobile-review page displays the review in a narrow iframe. These are review tools, not additional destination guides.

## Tech stack

- Buildless static HTML5, CSS and vanilla JavaScript; no application framework, bundler, dependency installation or build step is required for the current package.
- Destination records, interest tags, photograph mappings, distance calculation and DOM rendering are embedded in the discovery HTML.
- Shared `style.css` plus page-specific inline styles.
- Local WebP/JPEG assets and JSON attribution records; Wikimedia Commons supplies the source imagery and file-specific license evidence.
- `docs/airports-us.js` holds airport codes, names and coordinates generated from OurAirports (public domain): land airports with a K-prefixed ICAO code or a 3-character FAA ID, which leaves out most private strips.
- Cloudflare Pages hosts the static site from `docs/` on `main` (no build step). GitHub Pages can serve the same folder as a backup; `docs/.nojekyll` makes it serve the files as-is.
- Source is managed in Git on GitHub. The ChatGPT `.openai/hosting.json` manifest was not carried over and is no longer needed.
- Python/Pillow were used as development tools for image resizing/conversion and archive checks. They are not browser runtime dependencies.
- No application backend, database, user accounts, payments, saved trips, live aviation data, booking API or ForeFlight integration is implemented. The hosting access gate is separate from application functionality.

## File structure

| Path | Purpose |
| --- | --- |
| `README.md` | Repository overview and local preview instructions |
| `PROJECT_NOTES.md` | This document |
| `PACKAGE_HISTORY.md` | README of the final ChatGPT package, kept for history |
| `VALIDATION.md` | Checks documented for the four-photo replacement package |
| `PHOTO_CREDITS.md` | Human-readable sources, photographers, licenses and requirements |
| `PHOTO_CREDITS.json` | Detailed attribution and image-file records |
| `licenses/commons-imageinfo-evidence.json` | Commons evidence for the six original photos |
| `licenses/replacement-imageinfo-evidence.json` | File-specific evidence for the four replacements |
| `docs/index.html` | Discovery homepage, destination data, filters and rendering logic |
| `docs/style.css` | Shared site styling |
| `docs/airports-us.js` | Southeast departure airports (OurAirports data) |
| `docs/savannah/index.html` | Savannah destination guide |
| `docs/savannah.jpg` | Hero/guide photograph |
| `docs/charleston/index.html` | Charleston destination guide (draft) |
| `docs/asheville/index.html` | Asheville destination guide (draft) |
| `docs/pinehurst/index.html` | Pinehurst destination guide (draft) |
| `docs/beaufort/`, `docs/st-augustine/`, `docs/greenville/`, `docs/charlottesville/`, `docs/nashville/`, `docs/key-west/` | Destination guides (drafts) |
| `docs/guide-route.js` | Personalizes each guide’s route box for the visitor’s home airport |
| `tools/guides/` | Guide build scripts (not published) |
| `docs/sitemap.xml`, `docs/robots.txt` | Search-engine sitemap and crawl rules (review pages excluded). Add new guide URLs to the sitemap. |
| `docs/assets/destinations/` | Destination images (WebP + JPEG, 480/960 and some 1600px) |
| `docs/photo-credits.json` | Attribution records served by the website |
| `docs/photo-review.html` | All-ten visual review (bypasses filters) |
| `docs/mobile-review.html` | Narrow iframe for mobile layout inspection |

To preview locally, open `docs/index.html` in a browser or run `python3 -m http.server -d docs`.

## Open issues and limitations

1. ~~Latest photos are not live.~~ Resolved November 1, 2026: photos approved and published on GitHub Pages.
2. **All ten guides are drafts.** They need a read-through and link check before the “Draft for review” labels come off.
3. **Departure airports cover the Southeast only.** NC, SC, GA, FL, VA, TN and AL as of November 1, 2026. Expanding means regenerating `docs/airports-us.js` with more states. Destination guides still show KMYR-based route snapshots.
4. ~~Trip length is inactive.~~ Resolved November 1, 2026: it now sets the flight-time options.
5. ~~Time labels can obscure cutoff behavior.~~ Resolved November 1, 2026: labels now show hours and minutes, rounded up (Nashville “~3 hr 3 min”). The filter is unchanged.
6. ~~Key West is beyond the selector range.~~ Resolved November 1, 2026: every trip length now offers up to 4½ hours, which includes Key West.
7. ~~Savannah content needs refresh.~~ Refreshed November 1, 2026. The Charleston draft’s links still need a click-check (see the Charleston guide section).
8. **Pinehurst imagery is archival.** The chosen sharp golf photograph dates to 2010 and should not be treated as a current course-layout reference.
9. **Review and homepage code are duplicated.** A future cleanup could share destination data and rendering to reduce drift, while preserving the simple static architecture.
10. **No live planning or commerce.** Weather, NOTAMs, fuel prices, hotel rates, events availability, reservations, ticket purchases and operational flight plans are not supplied.
11. **Photos approved; testing is limited.** Browser inspection confirmed that all ten images loaded. Local image links, JavaScript syntax, unchanged feature logic and preservation checks passed; comprehensive accessibility and cross-device testing is not documented for the latest package.
12. **Verify after publishing.** Under ChatGPT hosting, an earlier archive once served the Savannah guide as the home page. After each merge, check the live homepage and `/savannah/` rather than assuming the deploy worked.

## Recommended next steps

1. Click-check the Charleston and Asheville guide links and review the picks with Ross and Diana.
1a. Google Search Console is verified (Domain property) and indexing was requested November 1, 2026. Check the Sitemaps report occasionally.
2. Choose the next full guide only after the first two are reviewed, without expanding beyond the curated MVP prematurely.
3a. Test the experience with Ross, Diana and a small pilot/couples group; use their feedback to judge destination appeal and ease of choosing a getaway.
4. Consider sharing destination data between `index.html` and `photo-review.html` to stop the two drifting apart.
5. Keep this document current as decisions are made.

## History of these notes

Originally written in ChatGPT from the final package `WingAwayWeekends_Four_Photos_Replaced.zip` and the conversation history there. Revised in Claude on November 1, 2026, after the files moved to GitHub, the site was tested in a browser and published on GitHub Pages, the flight-time labels were changed, trip length was activated, Asheville was tagged for aviation museums, Southeast departure airports were added, the site moved to wingawayweekends.com on Cloudflare Pages, the Asheville, Pinehurst, Beaufort, St. Augustine and Greenville guides, home-airport route boxes and search-engine files were added, Google Search Console was verified and the sitemap submitted, the Charleston guide was drafted and the Savannah guide was refreshed.

## Fly to lunch: the $100 hamburger (`docs/fly-to-lunch/`, added November 2, 2026)

A standalone page listing Southeast airports with a well-reviewed restaurant on the field, a short walk away or a short ride away. The `SPOTS` array in the page's own script holds each entry (`code`, `name`, `where`, `meals`, `food`, `desc`, `pilot`, `phone`, `checked`; `lat`/`lon`/`city` only for strips not in `airports-us.js`). The page sorts by distance from the home airport (`?from=`, then `wingaway-home`, then KMYR), filters by maximum one-way flight time (default 1½ hours) and meal, uses the saved aircraft profile for times and round-trip fuel, and shows "drive instead" under 40 NM. The homepage links to it with a navy "Short hops" banner between the search filters and "Worth the flight", and every page has a "Fly to lunch" header link (added by `feedback.py`, which also adds it to rebuilt guides; on phones the small header label is hidden to make room). The Fly to lunch page itself is not run through `feedback.py`. Edit the HTML directly; there is no build script.

Entries (16): Pik N Pig (BQ1, formerly 5NC3), Low and Slow Smokehouse (KJNX), Howard's Pub (KW95), Hangar 28 Kitchen & Events (KGMU; replaced Runway Café, July 2026), Hunter-Gatherer Hangar (KCUB), Stanton's BBQ (private strip near Bennettsville), Beacon Drive-In (KSPA), Skull Creek Boathouse (KHXD), Barnstormer's Grill (GA2), Southern Soul BBQ (KSSI), Simply Suzanne's (KMTV), Charly's (KJGG), Lorraine's (KTGI), Airport Restaurant & Gin Mill (KDED), The Hangar (KSPG), Jet Runway Café (KFXE). Left out for now because recent status was unclear: 57 Alpha Café (KFQD; longtime chef left), Crosswind Café (KHKY; possibly closed), The Downwind (KPDK), Pyper Kub (X60), High Jackers/Landing Strip Tavern (KFIN), The Flying Machine (KLZU; mixed reviews). Airport restaurants change often; recheck entries periodically.

**Interest buttons (November 2, 2026):** 12 buttons in rows of four on desktop (three on tablets, two on phones): Stays (renamed from “Boutique stays” November 3, 2026), Dining, Wine, Spa, History, Outdoors, Hiking, Beach, Lake, Scenic views, Golf, Aviation museums. Romance was removed as a button when Lake was added (it matched nearly every destination, since every guide is a couples getaway); the Romance tags remain in the data, so it can be restored by adding it back to `interests`. Beach: Beaufort, St. Augustine, Outer Banks, Amelia Island, Gulf Shores, Key West. Scenic views: Asheville, Charlottesville, Greenville, Yadkin Valley, Virginia Hunt Country, Dahlonega, Chattanooga, Great Smoky Mountains, Key West. Lake: Lake Lure, Lake Keowee & Jocassee, Lake Lanier.

**FBO details (November 2, 2026):** every guide's FBO box shows the FBO name, full street address and phone (plus an "FBO details" link where one is confirmed). Addresses came from FAA/AirNav/AcuKwik-style listings; Wilson Air Center's (932 Jubilee Drive, Chattanooga) came from a single directory and is worth confirming. Hunt Country's two FBOs carry their airport IDs in the name (KJYO, KHWY).

- **Harpers Ferry (`docs/harpers-ferry/`, 22, added November 2, 2026; West Virginia):** KMRB Eastern WV Regional, Martinsburg (MRB Aviation, 170 Aviation Way, 304-262-2507; crew car and Enterprise). Notes the nearby DC SFRA, P-40 and frequent TFRs. Stay: The Town's Inn, The Bavarian Inn (Shepherdstown), Lily Garden B&B; luxury Hillbrook Inn. Eat: The Rabbit Hole, Redbook at Hillbrook Inn, Snallygasters. Explore: the national historical park, Maryland Heights, C&O Canal towpath, tubing, Shepherdstown and Antietam. Hilltop House Hotel is listed as closed, so it is left out. Placeholder illustration `harpers-ferry-rivers`. KMRB is not in airports-us.js (WV is outside the seven-state list); guides take destination coordinates from the homepage.

**Photos from the National Park Service (November 2, 2026):** Wikimedia now refuses automated requests from the cloud session, and other photo sites are blocked unless added to the environment's Allowed domains (www.nps.gov, unsplash.com, images.unsplash.com, api.unsplash.com, api.flickr.com and live.staticflickr.com were added). NPS NPGallery photos marked “Public domain” / “Full” are used with a courtesy credit: park gallery pages list album IDs; `www.nps.gov/npgallery/api/search/execute/albumid/<id>?pagesize=500&primarytype=image` lists photos; `www.nps.gov/npgallery/GetAsset/<id>/original.jpg` (or `/proxy/hires`) downloads them; `www.nps.gov/npgallery/Asset/<id>` gives the credit. Harpers Ferry now uses “View from Jefferson Rock” (`harpers-ferry-jefferson-rock`) and Chattanooga “Garrity’s Battery in Point Park at sunset” (`chattanooga-point-park-sunset`), and the Smokies “Fall Color on Rich Mountain Road Overlook” by Sam Hobbs, NPS (`smoky-mountains-rich-mountain`). The Smokies albums are on `grsm/learn/photosmultimedia/index.htm`. Unsplash and Flickr searches need a free developer key.

**Unsplash photos (November 2–3, 2026):** Gulf Shores (Steven Van Elk, Orange Beach), Lake Lure (haseeb riaz, Chimney Rock), Lake Lanier (Jo Anaya), Virginia Hunt Country (Serena T, Salamander Resort, Middleburg) and Yadkin Valley (Elijah Mears, Wilkes County, NC) use Unsplash photos. Always check a candidate's location tag via the API before using it; search matches are often elsewhere. and Dahlonega (Cesar Pimentel, Amicalola Falls). Every destination now has a real photo. Unsplash API rules require hotlinking, so these are **not** stored in the repo: `photos.json` holds the images.unsplash.com raw URL as `slug` (with `remote: "unsplash"`), `guide_helpers.page_start` builds crop URLs for remote photos, and the homepage/photo-review `destinationPhotos` entries carry a `remote` URL that the card code uses. Credits follow Unsplash's format ("Photo by <name> on Unsplash" with utm_source=wingaway_weekends&utm_medium=referral links), and each use was registered via the photo's download_location. The Unsplash Access Key is kept only in the session scratchpad, never in the repository. The cloud session cannot load images.unsplash.com, so local tests show these images as broken; browsers load them normally.

- **Hilton Head (`docs/hilton-head/`, 23) and Highlands–Cashiers (`docs/highlands-cashiers/`, 24), added November 3, 2026**, bringing the homepage to 24 destinations (eight even rows of three).
  - **Hilton Head:** KHXD, Signature Aviation (52 Gateway Circle, Hilton Head Island, SC 29926; 843-689-3200). Stay: The Westin (Heavenly Spa), Omni Oceanfront, Sonesta; luxury Montage Palmetto Bluff. Eat: Skull Creek Boathouse, Charlie's L'Etoile Verte, CQ's. Beach biking, Harbour Town lighthouse, golf, Sea Pines Forest Preserve, Daufuskie.
  - **Highlands–Cashiers:** K1A5 Macon County, Franklin (Macon Air, 1241 Airport Road, Franklin, NC 28734; 828-524-5529), with 24A Jackson County as an alternative. Stay: Old Edwards Inn & Spa, The White Birch Inn, Hotel Cashiers; luxury High Hampton. Eat: Madison's, The Orchard, Wolfgang's. Dry Falls, Bridal Veil Falls, Whiteside Mountain, Sunset Rock, Whitewater Falls.
  - Photos from Unsplash: Hilton Head by Justin Fisher (beach path), Highlands–Cashiers by Nik Shuliahin (mountain fog), both location-tagged.

## Expansion, Phase 1 (started November 3, 2026)

Plan: `plans/phase-1-plan.pdf` (source `plans/phase-1-plan.html`). Next region: Mid-Atlantic. Family toggle planned; solo audience not targeted. Regional reviewers to be recruited.

- **Step A done:**
  - **Nationwide airports:** `docs/airports-us.js` (5,044 U.S. public-use land airports, all 50 states + DC; ~330 KB) replaces `airports-southeast.js`. Rebuild with `python3 -I tools/airports/build_airports.py <OurAirports airports.csv> docs/airports-us.js` (the CSV downloads from raw.githubusercontent.com/davidmegginson/ourairports-data/main/airports.csv). Lookups on every page also accept a K-prefixed form of three-character codes (K01J finds 01J), so older saved home airports still work.
  - **Destination data file:** `docs/destinations.js` (`window.WINGAWAY_DESTINATIONS`) is now the single source for the homepage cards and the photo review page. Each entry: name, state, stateCode, region (Southeast or Mid-Atlantic; VA and WV are Mid-Atlantic, confirmed by the owner), airport, lat, lon, desc, tags, guide, family (null until decided) and photo. `personalize.py` reads guide coordinates from it. **Add new destinations here** (not in index.html).
  - **Wording:** Southeast-only phrasing removed from the homepage and Fly to Lunch.
- **Step B next:** region filter and region landing pages; “Traveling with kids” toggle using the `family` field.

### Phase 1 decisions (Nov 3, 2026)
- Confirmed: Virginia and West Virginia belong to the Mid-Atlantic region (Charlottesville, Virginia Hunt Country, Harpers Ferry). Everything else stays Southeast.
- Reviewer checklist: plans/reviewer-checklist.html and .pdf (one page). Hand it to recruited reviewers with the invitation.
- Region filter and kids toggle (Phase 1 Step B, live): homepage has a Region select (All / Southeast / Mid-Atlantic, matched on `region`) and a "Traveling with kids" switch (shows only `family: true`). Both sync to the URL, so links like `/?region=mid-atlantic` and `/?kids=1` work and can be shared. Family tags approved by owner: all true except Key West, Yadkin Valley, Virginia Hunt Country and Highlands–Cashiers. Unknown-airport message no longer lists states (all U.S. airports are covered).
- Airport suggestions: `docs/airport-suggest.js` (WingAwaySuggest) fills the datalist with only the top 10 matches as you type (code first, then name/city). Used on the homepage and fly-to-lunch. Do not load all 5,044 airports into a datalist again; it made typing slow on iPad.

### Mid-Atlantic batch 1 (added November 3, 2026; drafts awaiting owner review, numbers 25–29, all family: true)
- **St. Michaels & Easton (`docs/st-michaels/`, 25, MD):** KESN, Maryland Air (29137 Newnam Road, Suite 5, Easton, MD 21601; 410-822-0400); Easton Jet Service (410-820-8770) also on field. Stay: Inn at Perry Cabin, The Tidewater Inn (listed for sale in 2026, still operating), The Wylder Hotel. Eat: Bas Rouge, Stars, The Crab Claw. Maritime Museum, Oxford–Bellevue Ferry, Oxford, sails, Easton. Spa: Linden Spa.
- **Cape May (`docs/cape-may/`, 26, NJ):** KWWD, FlightLevel Aviation (201 Forrestal Road, Rio Grande, NJ 08242; 609-889-0750, per FlightLevel's site). Stay: Congress Hall, The Virginia Hotel, The Chalfonte. Eat: The Ebbitt Room, Peter Shields Inn, The Lobster House. NAS Wildwood Aviation Museum on the field (usnasw.org), Victorian district, lighthouse and Sunset Beach, wineries. Spa: Sea Spa at Congress Hall.
- **Shenandoah & Luray (`docs/shenandoah/`, 27, VA):** KLUA, Luray Caverns Airport (1504 Airport Road, Luray, VA 22835; 540-743-6070). Stay: Skyland, The Mimslyn Inn, Big Meadows Lodge; luxury The Inn at Little Washington. Eat: the Speakeasy at The Mimslyn (Circa '31 is breakfast and brunch only), The Inn at Little Washington, Pollock Dining Room. Luray Caverns, Skyline Drive, Stony Man, Hawksbill, Dark Hollow Falls, river.
- **The Homestead (`docs/homestead/`, 28, VA):** KHSP Ingalls Field (6240 Airport Road, Hot Springs, VA 24445; 540-839-5326), ridge-top near 3,800 ft. Stay: Omni Homestead, Inn at Gristmill Square, Vine Cottage Inn. Eat: Jefferson's, American Audubon Dining Room, Sam Snead's Tavern. Warm Springs Pools, Cascades golf, Garth Newel, Falling Spring Falls.
- **The Greenbrier (`docs/greenbrier/`, 29, WV):** KLWB, Greenbrier Valley Airport FBO (584 Airport Road, Suite 1, Lewisburg, WV 24901; 304-645-3961). Stay: The Greenbrier, its cottages, The General Lewis Inn. Eat: Prime 44 West, Main Dining Room, The General Lewis Inn restaurant (The French Goat closed January 2026). Bunker tour, Old White TPC, Lewisburg, Greenbrier River Trail.
- All five use illustrated placeholders (`st-michaels-harbor`, `cape-may-beach`, `shenandoah-ridges`, `homestead-valley`, `greenbrier-valley`) until Unsplash picks are made. Official links checked Nov 3, 2026 after the owner set network access to Full. Perry Cabin's spa is now "The Spa at Perry Cabin". WebFetch still cannot reach many hosts; curl with an honest user agent can (do not spoof a browser user agent).
- Remaining Mid-Atlantic candidates: Annapolis (ANP, inside the DC SFRA), Gettysburg & Lancaster, Chincoteague (KMFV), Rehoboth & Lewes (KGED), Bedford Springs (KHMZ).
- **Draft guides are hidden (Nov 3, 2026):** a destination with `"draft": true` in `docs/destinations.js` is left off the homepage unless the URL has `?preview=1` (the owner's preview link: wingawayweekends.com/?preview=1). Guides built with `REVIEWED = None` get `<meta name="robots" content="noindex">`, and drafts stay out of `sitemap.xml`. When the owner says "lg": set REVIEWED in the builder, rebuild and post-process, remove `"draft": true`, and add the guide to the sitemap. The draft pages still exist at their URLs, so anyone with a direct link can open them.
- Photo picking page: `docs/photo-options/index.html` (noindex, unlinked) shows the current Unsplash contact sheet at wingawayweekends.com/photo-options/. Replace it with each new sheet.
- Savannah is hidden (`"draft": true`, noindex, out of the sitemap) until the owner's friend reviews it.
- **Mid-Atlantic photos (Nov 3, 2026):** Cape May = Unsplash 2M22Gga202k (Cape May Lighthouse, rod m, geotag Cape May); Shenandoah = Unsplash YkpOqgtqulE (Blackrock Summit, durul dalkanat; location from the photographer's caption, no geotag). St. Michaels pick 6 was rejected: geotagged Elk Neck State Park (North East, MD), ~70 mi north; offered Unsplash k51d7hLJCAg (geotag Easton) instead. Wikimedia Commons is reachable now (curl with UA "WingAwayWeekendsPhotoBot/1.0 (https://wingawayweekends.com; hello@wingawayweekends.com)"), and the photo-options page shows Commons photos of The Homestead and The Greenbrier (Carol M. Highsmith, Library of Congress, public domain). Candidate data in the scratchpad `wm_picks.json`.
- Homestead = Commons "Homestead Resort old wing 2016.jpg" (Antony-22, CC BY-SA 4.0) as `homestead-old-wing`; Greenbrier = Commons "The Greenbrier Historic Resort Hotel.jpg" (Carol M. Highsmith, public domain) center-cropped 4:3 as `greenbrier-front`. Wikimedia returns 429 for original-size downloads; fetch the 1920px thumbnail instead. The old placeholder files (cape-may-beach, shenandoah-ridges) are unused and can be deleted.
- Owner reviewed ("lg") Cape May, Shenandoah & Luray, The Homestead and The Greenbrier on Nov 3, 2026: REVIEWED set, draft flag removed, added to sitemap. Still draft: St. Michaels & Easton (awaiting photo), Savannah (awaiting friend). St. Michaels photo options (Wikimedia Commons) are on /photo-options/; data in scratchpad wm_stm_sheet.json.
- St. Michaels reviewed Nov 3, 2026 with Commons "Hooper Strait Light, St. Michaels, Maryland.jpg" (Fletcher6, CC BY 3.0) as `st-michaels-hooper-strait`. Only Savannah remains a draft. Unused placeholder files: st-michaels-harbor, cape-may-beach, shenandoah-ridges (safe to delete).

### Northeast region (started November 3, 2026)
- Owner decision: Northeast = PA, NY, VT, NH, MA, CT, RI, ME (PA is Northeast, not Mid-Atlantic). Midwest comes after the Northeast is complete.
- New shared builder `tools/guides/simple_guide.py`: each `build_<slug>.py` defines a GUIDE dict and calls `build()`. Same post-processing pipeline as other guides.
- Homepage region list now hides regions with no public guides (Northeast appears only with ?preview=1 until a guide is reviewed).
- **Batch 1 (drafts, numbers 30–35, all family: true, placeholder illustrations):**
  - Newport RI (`newport`, KUUU): FlightLevel Aviation, 211 Airport Access Road, Middletown, RI 02842, 401-846-9400. Castle Hill Inn, The Chanler, The Vanderbilt; White Horse Tavern, Castle Hill, The Mooring.
  - Nantucket MA (`nantucket`, KACK): town FBO, 14 Airport Road, 508-325-5307. The Wauwinet, White Elephant, Greydon House; The Club Car, TOPPER'S, Straight Wharf.
  - Bar Harbor & Acadia ME (`bar-harbor`, KBHB): Modern Aviation, 112 Caruso Drive, Trenton, ME 04605, 207-667-5534. Bar Harbor Inn, West Street Hotel, Balance Rock Inn; Havana, Jordan Pond House, Thurston's.
  - Stowe VT (`stowe`, KMVL): no full-service FBO listed; Heritage Aviation at KBTV as the full-service alternative. Topnotch, Lodge at Spruce Peak, Trapp Family Lodge; Plate, Hen of the Wood, von Trapp Bierhall.
  - Saratoga Springs NY (`saratoga`, 5B2): North American Flight Services, 405 Greenfield Avenue, Ballston Spa, NY 12020, 518-885-5470. Adelphi, Saratoga Arms, Gideon Putnam; 15 Church, Osteria Danny, Hattie's.
  - Gettysburg PA (`gettysburg`, KW05): Blouch Aircraft Services, 1150 Chambersburg Road (address from directories, confirm), 717-357-5958. P-40 about 15 nm SW. Hotel Gettysburg, Federal Pointe Inn, Brickhouse Inn; Dobbin House, Farnsworth House, The Pub. (Inn at Herr Ridge dropped: website gone.)
- Batch 2 planned: Lancaster PA, Hudson Valley NY, Mystic CT, Portsmouth NH, Kennebunkport ME, the Berkshires MA, Lake Placid NY, Martha's Vineyard MA.
- Northeast photo options (Commons + Unsplash) on /photo-options/; data in scratchpad ne_photo_options.json. Wikimedia API rate-limited this session heavily (429s); Unsplash picks must be location-verified via /photos/:id before use.
- Northeast photos: Newport = Commons "The Breakers from the Southwest.jpg" (CopperDoodle, CC0) as newport-breakers; Nantucket = Unsplash Brant Point sunrise (Keenan Shepard; geotag Nantucket Sound, visually Brant Point); Gettysburg = Unsplash MwFLo2tBoeM cannon (John Kostyk; geotag Gettysburg visitor center). Owner asked for Bar Harbor harbor-with-boats and Saratoga racetrack photos; location-tagged options on /photo-options/ (scratchpad ne_sheet2.json). Helper scripts in scratchpad: apply_commons.py, apply_unsplash.py.
- Savannah luxury row: official links added from the friend’s review (Perry Lane on marriott.com, gastonian.com, The Alida on marriott.com; tracking parameters stripped). Savannah stays hidden until the friend says lg.
- Savannah reviewed and public Nov 3, 2026 (friend lg): removed personal "Diana/Ross" wording and the shortlist note, rewrote the Hyatt card, reviewed note box, removed noindex/draft, added to sitemap. Every guide is now reviewed except the Northeast batch.
- **Northeast batch 2 (drafts, numbers 36–43, family: true, placeholder illustrations):**
  - Lancaster & Amish Country PA (`lancaster`, KLNS): Alliance Aviation, 500 Airport Road Suite G, Lititz, PA 17543, 717-735-9507. Lancaster Arts Hotel, Hotel Rock Lititz, Cork Factory Hotel; LUCA, John J. Jeffries, Central Market. (Belvedere Inn dropped: site dead.)
  - Hudson Valley NY (`hudson-valley`, KPOU): FlightLevel Dutchess, 263 New Hackensack Road, Wappingers Falls, NY 12590, 845-849-3770. Hutton Brickyards, Wildflower Farms, Beekman Arms; CIA restaurants, Wildflower Farms, Beekman Arms tavern. Old Rhinebeck Aerodrome.
  - Mystic CT (`mystic`, KGON): Modern Aviation, 193 Tower Avenue (one source says 175), Groton, CT 06340, 860-715-8800. Whaler's Inn, Steamboat Inn, Inn at Mystic; Oyster Club, Stonington Borough (generic), Ford's Lobster. USS Nautilus.
  - Portsmouth NH (`portsmouth`, KPSM): Port City Air, 104 Grafton Drive, 603-430-1111 (from its site). Wentworth by the Sea, The Hotel Portsmouth, Ale House Inn; Moxy, Row 34, Jumpin' Jay's.
  - Kennebunkport ME (`kennebunkport`, KSFM): Southern Maine Aviation, 199 Airport Road, Sanford, ME 04073, 207-324-8919. White Barn Inn, Cape Arundel Inn, The Colony; Cape Arundel Inn, White Barn Inn, The Clam Shack.
  - The Berkshires MA (`berkshires`, KPSF): Lyon Aviation, 832 Tamarack Road, Pittsfield, MA 01201, 413-443-6700. Blantyre, Canyon Ranch Lenox, Red Lion Inn; Red Lion Inn, Blantyre, Prairie Whale.
  - Lake Placid NY (`lake-placid`, KLKP): Adirondack Flying Service, 518-523-2473 (address varies by source). Mirror Lake Inn, Whiteface Lodge, Golden Arrow; Lisa G's, Mirror Lake Inn, Big Slide Brewery.
  - Martha's Vineyard MA (`marthas-vineyard`, KMVY): airport FBO, 71 Airport Road, Vineyard Haven, MA 02568, 508-693-7022. Charlotte Inn, Harbor View Hotel, Winnetu; Atria, l'étoile, Larsen's Fish Market.
- With batch 2 all eight Northeast states have at least one guide. Next region: Midwest.
- Saratoga photo: Library of Congress "Race Course, Saratoga, N.Y." (Detroit Publishing Co., 1905 postcard, no known restrictions) as saratoga-race-course-1905, postcard border trimmed. Owner picks pending apply: Newport 8 (Unsplash -zle9Sv7QQo tall ship, replaces The Breakers), Bar Harbor 3 (Unsplash hTig1fjrMe8 docks), Stowe 3 (Commons "Stowe VT Community Church (51626887231).jpg", CC BY 2.0).
- Owner approved all 14 Northeast guides ("northeast region lg", Nov 3, 2026): REVIEWED set in every builder. Published now (photos in place): Newport, Nantucket, Gettysburg, Saratoga Springs. The other 10 stay "draft": true until their photos are applied; when a photo lands, remove the draft flag and add the guide to sitemap.xml.

### Midwest region (started November 3, 2026)
- Owner decision: Midwest = KY, OH, MI, IN, IL, WI.
- **Batch 1 (drafts, numbers 44–49, placeholder illustrations):**
  - Bardstown & Bourbon Country KY (`bardstown`, KBRY; family false): Samuels Field Aviation, 1924 Boston Road, Bardstown, KY 40004, 502-348-7858 (unattended Sundays). Talbott Tavern & Inn, Bourbon Manor, Bardstown Bourbon Co.; Old Talbott Tavern, Bottle & Bond. Bottle-to-throttle note; hire a driver.
  - Dayton OH (`dayton`, KMGY): First Flight Aviation, 10600 Springboro Pike, Miamisburg, OH 45342, 937-885-5580. National Museum of the USAF, Dayton Aviation Heritage NHP, Huffman Prairie, Carillon Park (Wright Flyer III), Yellow Springs. AC Hotel Dayton, Mills Park Hotel; Lily's Bistro, Salar, Young's Jersey Dairy.
  - Mackinac Island MI (`mackinac`, KMCD): state-park airport, 906-847-3231, not a full-service FBO; 3,500 ft runway. Grand Hotel, Chippewa Hotel, Mission Point; Pink Pony, Grand Hotel Main Dining Room.
  - French Lick IN (`french-lick`, KFRH): French Lick Municipal, 9764 W. County Road 375 S., 812-936-2222; resort shuttle. West Baden Springs, French Lick Springs, RidgeView Cottages; 1875: The Steakhouse, Sinclair's.
  - Galena IL (`galena`, KDBQ in Iowa, ~30 min): Dubuque Jet Center, 11000 Airport Road, Dubuque, IA 52003, 563-589-4136. DeSoto House, Eagle Ridge; Fritz & Frites, One Eleven Main.
  - Door County WI (`door-county`, KSUE): Tailwind Flight Center, 3538 Park Drive, Sturgeon Bay, WI 54235, 920-746-2581. White Gull Inn, Eagle Harbor Inn, Whistling Swan; White Gull fish boil, Wild Tomato, Al Johnson's.
- Batch 2 planned: Lexington KY, Put-in-Bay OH, Traverse City MI, Chicago IL, Lake Geneva WI, Oshkosh & EAA WI.
- Newport photo now Unsplash -zle9Sv7QQo (tall ship, Nancy McClure; replaces The Breakers). Bar Harbor photo Unsplash hTig1fjrMe8 (docks, Bob Shea); Bar Harbor published. Photo options for Northeast batch 2 + Midwest batch 1 on /photo-options/ (scratchpad photo_round3.json); verify location via /photos/:id before applying. Stowe 3 (Commons church) still waiting on Wikimedia.
- Stowe photo: Commons "Stowe VT Community Church (51626887231).jpg" (Shiva Shenoy, CC BY 2.0) as stowe-church; Stowe published.
- Round 3 photos applied (Unsplash, location-checked): Mackinac (Grand Hotel garden), French Lick (West Baden dome, visual ID), Galena, Door County, Martha’s Vineyard, Lake Placid, Berkshires, Kennebunkport, Portsmouth, Mystic (beluga), Lancaster (Poole Forge bridge). Published the 7 Northeast ones; 42 public. Rejected: Dayton 3 (New Mexico), Hudson 4 (Sleepy Hollow cemetery). New options: Dayton from NPS DAAV albums (scratchpad dayton_sheet.json; GetAsset/{id}/original.jpg, public domain), Hudson (hudson_sheet.json).
- Dayton photo: NPS "Wright B Flyer in the air above Huffman Prairie" (c. 1910, Harvey Gaylord Kittredge collection, public domain) as dayton-wright-b-flyer, cropped inside the album border. Bardstown 3 not used: it is a close-up of Woodford Reserve bottles (Woodford is in Versailles near Lexington, no location tag); suggested for the future Lexington guide.
- Bardstown photo: Unsplash Woodford Reserve bottles (owner chose it after the location note).
- Owner approved the Midwest ("midwest lg", Nov 3, 2026): all six published. 48 public; only Hudson Valley is still a draft (waiting on a photo pick). New map plans/coverage-map-central.png (four regions, eastern + central US).
- Hudson Valley photo pick: Unsplash Bear Mountain Bridge in fall (Danny Nanni; visually identified, pick_hudson.json). Applied and published.

### Region plan (owner decisions, Nov 3, 2026)
- **Florida** is its own region (St. Augustine, Amelia Island and Key West moved from Southeast). More Florida destinations to come.
- **Heartland** = MO, IA, MN, AR (next to build).
- **Great Plains** = ND, SD, NE, KS, OK.
- **Texas** is its own region.
- Region filter options: Southeast, Florida, Mid-Atlantic, Northeast, Midwest, Heartland, Great Plains, Texas (empty regions are hidden automatically).
- **Heartland batch 1 (drafts, numbers 50–55, family: true, placeholder illustrations):**
  - Branson & Table Rock Lake MO (`branson`, KBBG): Branson Jet Center, 130 Wright Brothers Drive, Hollister, MO 65672, 417-334-8234. Big Cedar Lodge, Chateau on the Lake; Top of the Rock, Dogwood Canyon, Silver Dollar City.
  - Lake of the Ozarks MO (`lake-ozarks`, KAIZ): City of Osage Beach FBO, Lee C. Fine Road, Brumley, MO 65017, 573-348-5251 (street number varies by source; field reportedly closed for a stretch in 2025). Old Kinderhook, Camden on the Lake; Ha Ha Tonka.
  - Hot Springs AR (`hot-springs`, KHOT): City FBO, 525 Airport Road, Hot Springs, AR 71913, 501-321-6750. Hotel Hale, The Waters, The Arlington; Rolando's, Superior Bathhouse Brewery; Bathhouse Row, Quapaw Baths, Garvan Gardens.
  - Bentonville & Crystal Bridges AR (`bentonville`, KVBT, Louise Thaden Field): Legends Air Center, 2205 SW I Street, 479-254-0817 (phone varies by source); Airship Coffee on the field. 21c Museum Hotel; The Preacher's Son, Tusk & Trotter; Crystal Bridges, the Momentary.
  - Eureka Springs AR (`eureka-springs`, 4M1): Carroll County Airport, 518 County Road 308, Berryville, AR 72616, 870-423-8393 (self-serve 100LL). Crescent Hotel, Basin Park Hotel; Crystal Dining Room, Mud Street Café; Thorncrown Chapel.
  - Duluth & the North Shore MN (`duluth`, KDLH, ~1,000 nm): Vantage Aviation (some directories say Monaco Air), 4535 Airport Approach Road, 218-727-2911. Pier B, Fitger's; Va Bene, Lake Avenue, Northern Waters Smokehaus; Glensheen, Split Rock, Gooseberry Falls.
  - Iowa (Okoboji or Decorah) moved to batch 2: Okoboji lodging/dining research was too thin.
- **Florida batch 1 (drafts, numbers 56–61, family: true, placeholder illustrations):**
  - Naples (`naples`, KAPF): Naples Aviation, 160 Aviation Drive North, Naples, FL 34104, 239-643-0404 (noise abatement). Ritz-Carlton Naples, LaPlaya, Inn on Fifth; Sea Salt, USS Nemo, The Dock at Crayton Cove.
  - Sanibel & Captiva (`sanibel`, KFMY Page Field): Base Operations, 5200 Captain Channing Page Drive, Fort Myers, FL 33907, 239-590-6600. 'Tween Waters, South Seas, Island Inn; Mucky Duck, Bubble Room, Doc Ford's. Hurricane Ian recovery note.
  - Islamorada (`islamorada`, KMTH Marathon, ~45 min): Million Air Florida Keys, 9400 Overseas Highway (number varies), 305-743-1995. Cheeca Lodge, The Moorings Village; Morada Bay Beach Café (cheeca.com page), Islamorada Fish Co.; Robbie's.
  - Palm Beach (`palm-beach`, KLNA Lantana): Stellar Aviation, 2633 Lantana Road, Lantana, FL 33462, 561-656-9815. VIP/presidential TFR warning. The Breakers, The Colony, Brazilian Court; Café Boulud, Buccan, Ta-boó; Flagler Museum.
  - Cedar Key (`cedar-key`, KCDK): no FBO or fuel; ~2,300 ft runway by the water; golf carts. Harbour Master Suites, the Downtown Historic Island Hotel (now rented as suites); Tony's chowder; Dock Street restaurants rebuilding after storms.
  - Seaside & 30A (`30a`, builder build_thirty_a.py, KECP): Sheltair, 5325 Johnny Reaver Road, Panama City, FL 32409, 850-233-4717. WaterColor Inn, The Pearl, Hotel Effie; Bud & Alley's, Restaurant Paradis, The Red Bar. Tyndall/Eglin airspace.
- Photo options for Heartland batch 1 + Florida batch 1 on /photo-options/ (scratchpad photo_round5.json). Lake of the Ozarks only 2 options.
- Round 5 photos applied (location-checked): Lake of the Ozarks (cove), Hot Springs (aerial), Bentonville (Crystal Bridges), Duluth (hills), Naples (dock at golden hour), Sanibel (shells), Palm Beach (Clematis St fountain, West Palm), Cedar Key (pelicans), 30A (Seaside paddleboard). Rejected Eureka 6 (France). Islamorada options in scratchpad islamorada_sheet.json. Branson (owner wants a country music/show photo) and Eureka searches pending Unsplash limit.
- **Restaurant fill-in (Nov 3, 2026):** replaced every generic restaurant card with a real, link-checked one: Bardstown (Toogie's Table), Branson (Devil's Pool, Osage, Arnie's Barn), Cedar Key (Steamers, now on Second St), Eureka Springs (Grotto Wood-Fired Grill & Wine Cave), Galena (Vinny Vanucchi's), Hot Springs (The Avenue at The Waters), Lake of the Ozarks (Windrose Marker 26, Shady Gators), Mackinac (Original Murdick's Fudge), Mystic (Water Street Cafe, Stonington), Islamorada (Atlantic's Edge; Morada Bay link now cheeca.com/dine-drink/the-beach-cafe). Added official links to Highlands–Cashiers, Hilton Head and Charleston cards that still used map links. No guide now has a "Website & map" fallback except Fly to Lunch.
- Highlands–Cashiers and Hilton Head builders now carry REVIEWED (they were owner-approved earlier but the builders still said None, which would have added noindex on rebuild).
- Fly to Lunch: each spot now has an official site (or a labeled tourism/chamber listing for Hangar 28, Barnstormer's, Lorraine's, Gin Mill, Simply Suzanne's) plus a separate Map link; added phones from official sites (Hunter-Gatherer, Beacon, Gin Mill, The Hangar, Jet Runway, Southern Soul) and corrected Charly's to its restaurant line 757-258-0034.
- Owner approved Heartland ("heartland lg", Nov 3, 2026). Published Lake of the Ozarks, Hot Springs, Bentonville, Duluth (53 public). Branson and Eureka Springs stay draft until photos: Eureka 6 was France and Eureka 1 was Bentonville (both rejected); Unsplash has no Branson-tagged music photos, so the photo page shows Branson-tagged lake, water tower and Silver Dollar City options (scratchpad branson_sheet.json). Islamorada photo applied (Unsplash sPU2kzPIf28); Florida still awaiting owner review.
- **Caching fix (Nov 3, 2026):** the owner's browser kept an old destinations.js, so new preview guides did not appear. index.html now loads its scripts with a ?v=YYYYMMDDHHMM tag (bump it whenever destinations.js or other homepage scripts change), and docs/_headers tells browsers to revalidate all .js files (Cache-Control: no-cache).
- **Texas batch 1 (drafts, numbers 62–67):** Fredericksburg (`fredericksburg`, T82; Hangar Hotel on the field, adults only), San Antonio (`san-antonio`, KSSF Stinson; GateOne), Fort Worth (`fort-worth`, KFTW; Texas Jet; Vintage Flying Museum; DFW Class B), Galveston (`galveston`, KGLS; Island Jet Center or Galveston Aviation Services), South Padre (`south-padre`, KPIL; Southwind; SpaceX TFRs), Marfa & Big Bend (`marfa`, KMRF; ~4,850 ft; family false). Hotel Paisano closed until 2027; Pearl South Padre is now Margaritaville; Hotel Galvez is Grand Galvez. Photo options on /photo-options/ (scratchpad photo_round8.json).

## Next up (Nov 3, 2026)
- New Orleans (KNEW) built as draft #68, Southeast region, illustration placeholder photo.
- MS and LA join Southeast. Built as drafts Nov 4: Natchez #69 (KHEZ), Oxford #70 (KUOX), Bay St. Louis #71 (KHSA), St. Francisville #72 (via KBTR), Lafayette & Cajun Country #73 (KLFT). All use placeholder photos. Dropped hijacked/dead sites: King’s Tavern, Ravine, Blue Dog Café, Café des Amis, Mulate’s (moved to New Orleans), 3V Tourist Court. Alabama built as drafts Nov 4: Fairhope & Mobile Bay #74 (KCQF), Huntsville #75 (KHSV), Lake Martin #76 (KALX), Birmingham #77 (KBHM). Dropped: Chuck’s Marina (hijacked site), The Bottle (closed 2025). AL now has 5. Batch 3 (Nov 4): Memphis #78 (KMEM, Wilson Air), Golden Isles #79 (KSSI), Clarksdale #80 (KCKM), Natchitoches #81 (KIER). TN, GA, MS, LA now at 4. Dropped hijacked: Yazoo Pass, saintsimonslighthouse.org (used coastalgeorgiahistory.org); Maglieaux’s site expired. Batch 4 (Nov 4): Little Rock #82 (KLIT), St. Louis #83 (KCPS, alt KSUS), Kansas City #84 (KMKC, TWA Museum). AR and MO now at 4. Dropped: Hotel Hale (it is in Hot Springs), Big Dam Bridge domain (not official), Vicia and Sidney Street Cafe (sites gone), Tony’s (hijacked). Batch 5 (Nov 4): Annapolis #85 (KANP; DC SFRA nearby), Ocean City & Berlin #86 (KOXB), Deep Creek Lake #87 (2G4), New River Gorge #88 (KBKW), Berkeley Springs #89 (KMRB), Lexington #90 (KLEX), Louisville #91 (KLOU), Paducah #92 (KPAH). MD, WV, KY now at 4. Dropped: Liquid Assets (domain redirects elsewhere), Horse Country org (Facebook only), bbqontheriver.org (hijacked), Thrasher’s and Tari’s (sites down), Lake Pointe Inn is at deepcreekinns.com. Next four-per-state targets: PA, NY, MA, then Northeast singles (NJ, RI, VT, CT, NH, ME) and Midwest singles (OH, MI, IN, IL, WI, MN) and the Northeast and Midwest singles.
- Goal from owner: at least four destinations in every state covered. Current counts: FL 9, NC 6, TX 6, SC 5, VA 4; TN/GA/MA/NY/AR 3; WV/ME/PA/MO 2; AL, MD, NJ, RI, VT, CT, NH, KY, OH, MI, IN, IL, WI, MN, LA 1. About 50 more guides needed; work region by region, drafts first.
- Still pending: Branson music photo, Eureka Springs photo, Texas review and photos, Great Plains region.

## Photos applied Nov 4 (published)
- New Orleans (Unsplash, French Quarter), St. Francisville (Rosedown), Huntsville (Space & Rocket Center), Birmingham (Railroad Park skyline with Sloss stacks, visually confirmed), Memphis, Golden Isles (Driftwood Beach), Branson (Table Rock Lake sunset; owner chose this over waiting for a music photo).
- Library of Congress (Carol M. Highsmith, public domain): Oxford (downtown Square), Clarksdale (Terry "Harmonica" Bean at Red's), Eureka Springs (fall road).
- Rejected by location check: Natchez 1 (Natchez steamboat in New Orleans), Bay St. Louis 2 (Louisville riverboat), Lafayette 9 (St. Louis Cathedral, New Orleans), Fairhope 1 (Noccalula Falls, Gadsden), Lake Martin 1 (O'Neill Bridge, Florence AL).
- Still need photos: Natchez, Bay St. Louis, Lafayette, Fairhope, Lake Martin, Natchitoches (Southeast, approved); plus Texas, Heartland batch 2, MD/WV/KY drafts.

## Northeast batch 1 (Nov 4, drafts)
- Finger Lakes #93 (KITH), New Hope & Bucks County #94 (KDYL), Pocono Mountains #95 (KMPO), Camden & Midcoast Maine #96 (KRKD, Owls Head museum on field), Portland ME #97 (KPWM), Chatham & Cape Cod #98 (KCQX), Princeton #99 (39N).
- Builders now generated from compact specs: scratchpad gen/mk.py + gen/ne1.py (simple_guide format).
- Dropped: Hazelnut Kitchen (site expired), Marsha Brown (domain parked), Frogtown Chophouse (empty site), Danforth Inn (site down).
- Batch 2a (Nov 4): Block Island #100 (KBID, no FBO/fuel), Providence #101, Watch Hill & Westerly #102 (KWST), New Haven #103 (KHVN), Essex & the CT River #104 (KSNC), Litchfield Hills #105 (KOXC), Asbury Park & Spring Lake #106 (KBLM), Atlantic City #107 (KACY). RI, CT, NJ now at 4. Dropped: Dean Hotel, Bee and Thistle, White House Subs link (sites down). Batch 2b (Nov 4): Woodstock VT #108 (KLEB), Manchester VT #109 (KDDH), Burlington VT #110 (KBTV), Bretton Woods & Franconia Notch #111 (KHIE), Lake Winnipesaukee #112 (KLCI), North Conway & Jackson #113 (KIZG). Every Northeast state now has 4+. Next: Great Plains (ND, SD, NE, KS, OK). Then the Great Plains region (ND, SD, NE, KS, OK).

## Great Plains batch 1 (Nov 4, drafts)
- SD: Black Hills & Custer SP #114 (KRAP), Deadwood & Spearfish Canyon #115 (KSPF), Badlands #116 (KRAP), Sioux Falls #117 (KFSD).
- ND: Medora & Theodore Roosevelt NP #118 (KDIK), Fargo #119 (KFAR, air museum on field), Bismarck & Mandan #120 (KBIS), International Peace Garden & Turtle Mountains #121 (D09).
- These are 1,000–1,340 nm from KMYR; mk.py now writes "two fuel stops, four or more nights" for >900 nm.
- Lodging links thin in ND (visitor-bureau cards used where hotel sites were unreachable). Dropped: adamsmuseumandhouse.org (hijacked), Rhombus Guys (site now fundraisers).
- Batch 2 (Nov 4): Omaha #122 (KMLE; SAC museum), Lincoln #123 (KLNK), Scotts Bluff & Chimney Rock #124 (KBFF), Valentine & the Niobrara #125 (KVTN), Wichita #126 (KICT; Kansas Aviation Museum), Flint Hills #127 (KEMP), Lawrence #128 (KLWC), Lindsborg & Abilene #129 (KSLN). Lodging thin in Lincoln, Scottsbluff, Lindsborg (CVB cards). Next: OK (batch 3).

## Fly to Lunch expansion (Nov 4)
- Added 19 spots, each confirmed on its current AirNav listing (or a 2025 article for Southern Flyer): OH (KI74, KTSO), MI (KMKG, 61D, KJXN), IN (05C), WI (KMSN), IL (1C5), MN (KSTP), NJ (KWWD), NH (KAFN), MD (KHGR), KY (2I3), OK (KADM, KPNC), AR (3M0), KS (KHUT, 07S), TX (11R).
- If nothing is within the chosen flight time, the page now shows the three closest spots instead of an empty list.
- Round 2 (Nov 4): +13 Northeast/West (KPOU, KPYM, 6B6, KPTW, KHYA, KCQX, B06, KAPA, KSEZ, 0S9, S43, KSQL, 3O8) and +5 South/West (KDYR, KFPR, KCHD, KSGU, LA52 private strip with lat/lon). 53 spots total.
- Not added (not on current AirNav or uncertain): Le Relais KLOU (domain for sale), Skyline Diner 38D, Tin Goose KPCW, Donna's 1N7, Hangar B KCQX, Bessie's KJVL, Blackerby's KBAK. Gaps: PA, NY, New England beyond NH, West Virginia, Plains north of KS, the West.

## Midwest batch (Nov 4, drafts)
- MI: Traverse City #130 (KTVC), Saugatuck & Holland #131 (KBIV), Harbor Springs & Petoskey #132 (KMGN). WI: Kohler #133 (KSBM), Lake Geneva #134 (KBUU), Madison #135 (KMSN), Bayfield & Apostle Islands #136 (KASX). MI now 4, WI 5.
- Dropped: maggies-bayfield.com (hijacked); CityFlats Holland (now Grand Rapids only). Unlinked (site down): Trattoria Stella, Palette Bistro, Greunke's, The Old Fashioned, Gordy's, Inn on Woodlake.
- Still at 1: OH, IN, IL (and MN at 1 under Heartland).

## Fly to Lunch AirNav sweep (Nov 4)
- Swept AirNav "Where to Eat" for 2,447 public 4-letter K airports outside NC/SC/VA/FL; kept listings marked "on airport" or within 0.3 mi. 55 airports had one; added 39 new (dropped campground, museum, sports park, Applebee's, off-field Chinese/pizza, Le Relais, Casa Machado duplicate). 92 spots total.
- These newer entries have generic descriptions ("details are limited; call ahead") and meals guessed from the name. AirNav listings can be stale.
- Not yet swept: non-K 3-character FAA IDs (small fields like 1C5, 6B6) and the Southeast states. Scripts: scratchpad sweep.py / sweep.json.

## Batch: Ohio, Indiana, Illinois (Nov 4, 2026)
Nine drafts (#137–145), spec in scratchpad gen/oil1.py: Put-in-Bay (3W2, no FBO; Erie Island Carts), Hocking Hills (KLHQ Sundowner), Cleveland (KBKL Signature), Indianapolis (KEYE Jet Access), Brown County (KBMG Cook Aviation, towered), Indiana Dunes (KMGC), Chicago (KPWK Atlantic), Starved Rock (KVYS Midwest Avtech), Shawnee Hills (KMWA Midwest Aviation, towered). FBOs from AirNav; every card has an official link (checked with the honest link-check UA). Dropped: lolabistro.com and oldlighthousemuseum.org (hijacked), mabelsbbq.com (redirects elsewhere).
