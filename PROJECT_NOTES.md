# WingAway Weekends — Project Notes

Updated: November 1, 2026 (after migration from ChatGPT to Claude and GitHub Pages).

## Goals and agreed direction

WingAway Weekends helps general aviation pilots and their travel companions discover worthwhile short getaways. The experience connects an appealing destination with practical arrival, lodging, dining and activity information, with an initial emphasis on couples.

The agreed MVP is a curated discovery homepage with 5–10 handpicked destinations from KMYR and only 1–2 developed guides. The current site contains ten destination cards and two developed guides, Savannah and Charleston. Automatic recommendations for every airport are outside the current MVP.

The design uses navy, cream and gold, an aspirational destination hero photograph, the headline “Where will your wings take you this weekend?”, prominent airport and flight-time controls, and destination cards. ForeFlight remains the pilot’s operational flight-planning tool; WingAway provides destination discovery rather than weather, routing or dispatch decisions.

## Current source and publication status

- **Source of truth:** this GitHub repository, `ramorganmd-beep/WingAwayWeekends` (public). The project moved from ChatGPT to Claude on November 1, 2026. Older ChatGPT ZIPs and chats are history, not competing baselines.
- **Live site:** https://ramorganmd-beep.github.io/WingAwayWeekends/ — GitHub Pages, publishing the `docs/` folder of the `main` branch. Any change merged into `main` goes live within a minute or two.
- **Workflow:** Claude makes changes on a separate branch and pushes it; the user reviews and merges the pull request on GitHub.
- The ten-photo set, including the four replacements (Asheville, Key West, Pinehurst, Greenville), was **approved and published** on November 1, 2026.
- The site is public; the ChatGPT-hosted access gate no longer applies. Review pages (`photo-review.html`, `mobile-review.html`) are marked `noindex`.
- **Former hosting (retired):** ChatGPT Sites at https://wingaway-savannah.ramorganmd.chatgpt.site (project `appgprj_6abe9d437ef8819196353f64245055a8`, last confirmed version 7). It no longer receives updates and can be left or deleted.

## Features built

### Discovery homepage

- Responsive hero and destination-card grid, with layouts for desktop, tablet and mobile.
- Departure airport input (default KMYR) covering 695 public airports in NC, SC, GA, FL, VA, TN and AL, with suggestions as you type. It accepts K-codes (KCHS), codes without the K (CHS) and 3-character FAA IDs (2J9). Airports outside the region show a “coming soon” message. A destination is hidden if it is the home airport or within 40 NM of it.
- Trip length sets the maximum estimated flight-time options (default in bold):
  - Day trip: 1, **1½** or 2 hours
  - Weekend (page default): 2, **3** or 3½ hours
  - Longer stay: 3, 3½ or **4½** hours
  Changing trip length resets flight time to that trip's default.
- Interest checkboxes, in this order: Boutique stays, Dining, Wine, Spa, Romance, History, Outdoors, Golf and Aviation museums. Aviation museums is currently tagged on Savannah (Mighty Eighth Air Force Museum) Charleston (Patriots Point / USS Yorktown) and Asheville (Western North Carolina Air Museum, Hendersonville); other destinations need review before tagging.
- Multiple selected interests use AND matching: a destination must have every selected tag.
- Live result count and an empty-state message when nothing matches.
- Savannah and Charleston link to their guides. The other eight cards display “Guide coming soon.”

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

Key West estimates about 4 hours (label “~4 hr 2 min”), so it appears only with Longer stay at 4½ hours.

### Savannah guide

The developed guide covers FBO comparisons, arrival/ground transport, hotels, restaurants, attractions and boat outings, spa options, shopping, wine, breweries, sports/events links, a suggested weekend itinerary and practical booking considerations. It contains official-source links and explanatory notes, but no live pricing, availability or booking functionality. Refreshed November 1, 2026: the October 2026 trip dates became a sample Friday–Sunday itinerary; stale spa prices were removed; a note was added that Spa Bleu may be weekday-only, so Saturday appointments need confirming; the unverifiable “Savannah Underground” item was removed; Savannah Steel was updated (UPSHOT League, first season summer 2026); and the flight-time snapshot now uses the discovery page’s model (~1 hr 15 min).

### Charleston guide (draft, added November 1, 2026)

`docs/charleston/` follows the Savannah guide’s structure and styling: KCHS arrival with Atlantic Aviation and Signature, three stays (Zero George, Wentworth Mansion, The Vendue), FIG / Leon’s Oyster Shop / Husk, Patriots Point and the USS Yorktown as the pilot’s highlight, Fort Sumter, the Battery and Rainbow Row, Gibbes Museum, Middleton Place, Schooner Pride sunset sail, The Spa at The Charleston Place, King Street shopping, wine bars, breweries, RiverDogs / Stingrays / Battery and a sample Friday–Sunday itinerary. The hero uses the existing Rainbow Row card photo (CC0).

Research was done through web search only; the research environment could not open venue websites. Facts confirmed in search results include Patriots Point admission contents and hours, the Fort Sumter ferry departure points and duration, Atlantic Aviation’s CHS address and phone, the Charleston Place spa address and phone, and Schooner Pride’s departure point and sail length. **These official links were written from known domains but not opened, so click-check them:** figcharleston.com, leonsoystershop.com, huskrestaurant.com, hallschophouse.com, gibbesmuseum.org, middletonplace.org, croghansjewelbox.com, graftchs.com, edmundsoast.com, thevendue.com, zerogeorge.com, wentworthmansion.com, charleston.com/schooner-pride, the Signature CHS page and the Belmond spa page. Signature’s address and phone are omitted because directory listings conflict.

### Photography and review tools

All ten cards have downloaded destination photographs with recorded commercial reuse licenses. The last update replaced only Asheville, Key West, Pinehurst and Greenville. The other six photo sets were verified byte-for-byte unchanged against the attached source ZIP.

Images use WebP with JPEG fallbacks, responsive `srcset`, descriptive alternative text, lazy loading and asynchronous decoding. All cards have 480px and 960px image versions; the four replacement sets also have 1600px versions. Credits record photographer, title, source links, license requirements, modification notes, file sizes and checksums. ShareAlike photo adaptations retain their source license. None of the four selected replacement licenses was left unverified.

`photo-review.html` shows all ten cards for visual review, intentionally bypassing discovery filtering on that page only. A mobile-review page displays the review in a narrow iframe. These are review tools, not additional destination guides.

## Tech stack

- Buildless static HTML5, CSS and vanilla JavaScript; no application framework, bundler, dependency installation or build step is required for the current package.
- Destination records, interest tags, photograph mappings, distance calculation and DOM rendering are embedded in the discovery HTML.
- Shared `style.css` plus page-specific inline styles.
- Local WebP/JPEG assets and JSON attribution records; Wikimedia Commons supplies the source imagery and file-specific license evidence.
- `docs/airports-southeast.js` holds airport codes, names and coordinates generated from OurAirports (public domain): land airports with a K-prefixed ICAO code or a 3-character FAA ID, which leaves out most private strips.
- GitHub Pages hosts the static site from `docs/` on `main`. `docs/.nojekyll` makes Pages serve the files as-is.
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
| `docs/airports-southeast.js` | Southeast departure airports (OurAirports data) |
| `docs/savannah/index.html` | Savannah destination guide |
| `docs/savannah.jpg` | Hero/guide photograph |
| `docs/charleston/index.html` | Charleston destination guide (draft) |
| `docs/assets/destinations/` | 48 destination images (WebP + JPEG, 480/960 and some 1600px) |
| `docs/photo-credits.json` | Attribution records served by the website |
| `docs/photo-review.html` | All-ten visual review (bypasses filters) |
| `docs/mobile-review.html` | Narrow iframe for mobile layout inspection |

To preview locally, open `docs/index.html` in a browser or run `python3 -m http.server -d docs`.

## Open issues and limitations

1. ~~Latest photos are not live.~~ Resolved November 1, 2026: photos approved and published on GitHub Pages.
2. **Two developed guides.** Savannah and Charleston have guides; eight cards remain editorial summaries.
3. **Departure airports cover the Southeast only.** NC, SC, GA, FL, VA, TN and AL as of November 1, 2026. Expanding means regenerating `docs/airports-southeast.js` with more states. Destination guides still show KMYR-based route snapshots.
4. ~~Trip length is inactive.~~ Resolved November 1, 2026: it now sets the flight-time options.
5. ~~Time labels can obscure cutoff behavior.~~ Resolved November 1, 2026: labels now show hours and minutes, rounded up (Nashville “~3 hr 3 min”). The filter is unchanged.
6. ~~Key West is beyond the selector range.~~ Resolved November 1, 2026: Longer stay offers 4½ hours, which includes Key West.
7. ~~Savannah content needs refresh.~~ Refreshed November 1, 2026. The Charleston draft’s links still need a click-check (see the Charleston guide section).
8. **Pinehurst imagery is archival.** The chosen sharp golf photograph dates to 2010 and should not be treated as a current course-layout reference.
9. **Review and homepage code are duplicated.** A future cleanup could share destination data and rendering to reduce drift, while preserving the simple static architecture.
10. **No live planning or commerce.** Weather, NOTAMs, fuel prices, hotel rates, events availability, reservations, ticket purchases and operational flight plans are not supplied.
11. **Photos approved; testing is limited.** Browser inspection confirmed that all ten images loaded. Local image links, JavaScript syntax, unchanged feature logic and preservation checks passed; comprehensive accessibility and cross-device testing is not documented for the latest package.
12. **Verify after publishing.** Under ChatGPT hosting, an earlier archive once served the Savannah guide as the home page. After each merge, check the live homepage and `/savannah/` rather than assuming the deploy worked.

## Recommended next steps

1. Click-check the Charleston guide’s links and review its picks with Ross and Diana.
2. Choose the next full guide only after the first two are reviewed, without expanding beyond the curated MVP prematurely.
3. Test the experience with Ross, Diana and a small pilot/couples group; use their feedback to judge destination appeal and ease of choosing a getaway.
4. Consider sharing destination data between `index.html` and `photo-review.html` to stop the two drifting apart.
5. Keep this document current as decisions are made.

## History of these notes

Originally written in ChatGPT from the final package `WingAwayWeekends_Four_Photos_Replaced.zip` and the conversation history there. Revised in Claude on November 1, 2026, after the files moved to GitHub, the site was tested in a browser and published on GitHub Pages, the flight-time labels were changed, trip length was activated, Asheville was tagged for aviation museums, Southeast departure airports were added, the Charleston guide was drafted and the Savannah guide was refreshed.
