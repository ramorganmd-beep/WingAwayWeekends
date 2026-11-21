"""Add a "Leave the driving to someone else" box of established wine-tour drivers.

Usage: python3 tools/guides/winetours.py docs/<slug>/index.html [...]
Idempotent (replaces the wa-wine block). Goes at the end of the Wine section, or of Explore.
Each company was checked on its own website (Nov 2026); founding years only where the company states them.
"""
import re, sys
from pathlib import Path
START, END = '<!--wa-wine-->', '<!--/wa-wine-->'
BLOCK = re.compile(re.escape(START) + '.*?' + re.escape(END), re.S)
GRAPELINE = ('Grapeline Wine Tours', 'Private and shared tours, or a driver for your own plan.', 'https://www.gogrape.com/')
FL = [('Quality Wine & Brew Tours', 'Driver-guides for the Finger Lakes wine trails.', 'https://www.qualitywineandbrewtours.com/'),
      ('Finger Lakes Winery Tours', 'Family-owned tours around Seneca, Cayuga and Keuka lakes.', 'https://www.fingerlakeswinerytours.com/')]
DRIVERS = {
    'napa-sonoma': [('California Wine Tours & Transportation', 'Driving Napa and Sonoma since 1986, from sedans to small coaches.', 'https://www.californiawinetours.com/'),
                    ('Beau Wine Tours', 'Private chauffeured tours of Napa Valley and Sonoma.', 'https://www.beauwinetours.com/')],
    'paso-robles': [GRAPELINE, ('Uncorked Wine Tours', 'Local Paso Robles tours and dinner shuttles.', 'https://www.uncorkedwinetours.net/')],
    'temecula': [GRAPELINE, ('Destination Temecula', 'Private and small-group wine country tours.', 'https://www.destinationtemecula.com/')],
    'willamette-valley': [('Black Tie Tours', 'Custom Willamette Valley wine tours, based in Newberg.', 'https://www.blacktietours.com/'),
                          ('NW Wine Shuttle', 'Private tours and hourly transportation in wine country.', 'https://www.nwwineshuttle.com/')],
    'walla-walla': [('NW Touring & Concierge', 'Walla Walla wine tours, dinner rides and airport service.', 'https://www.nwtouring.com/')],
    'finger-lakes': FL, 'seneca-lake': FL,
    'charlottesville': [('Monticello Wine Tour & Coach Co.', 'Monticello Wine Trail tours from downtown Charlottesville.', 'https://www.monticellowinetour.com/')],
    'fredericksburg': [('Texas Wine Tours', 'One of the original Fredericksburg wine tour operators.', 'https://www.texaswinetours.com/')],
    'traverse-city': [('Blue Lakes By The Bay', 'Group and private wine tours on Old Mission and Leelanau, daily.', 'https://www.bluelakesbythebay.com/')],
    'yadkin-valley': [('Yadkin Valley Wine Tours', 'Private tours for two to thirty, plus airport transfers.', 'https://www.yadkinvalleywinetours.com/')],
}


def block(items):
    lis = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener"><b>{n}</b></a> · {t}</li>' for n, t, u in items)
    return (START + '<div class="wa-wine" style="margin:22px 0 0;padding:16px 20px;background:#f7f1f4;border:1px solid #e6d3dc;border-left:4px solid #7b2d4f;border-radius:3px">'
            '<h3 style="margin:0 0 6px;font-size:1.05rem">Leave the driving to someone else</h3>'
            '<p style="margin:0 0 8px;color:#51666f;font-size:.95rem">You flew in; let a local driver handle the wine roads. Established companies we found:</p>'
            f'<ul style="margin:0;padding-left:18px;line-height:1.6">{lis}</ul>'
            '<p style="margin:8px 0 0;font-size:.82rem;color:#647784">Checked Nov 2026. Book ahead for weekends; tours are often priced per hour or per person.</p></div>' + END)


for path in map(Path, sys.argv[1:]):
    k = path.parent.name; s = BLOCK.sub('', path.read_text())
    if k in DRIVERS:
        sec = '<section id="wine"' if '<section id="wine"' in s else '<section id="explore"'
        i = s.find(sec); j = s.find('</section>', i)
        s = s[:j] + block(DRIVERS[k]) + s[j:]
    path.write_text(s)
