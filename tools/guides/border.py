"""Add a "Flying to Canada" section to guides in the Canada region.

Usage: python3 tools/guides/border.py docs/<slug>/index.html [...]
Idempotent (replaces the block between wa-border markers). Inserted right after the flight section.
The guide supplies the U.S. customs airports for the return via RETURN below.
"""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
START, END = '<!--wa-border-->', '<!--/wa-border-->'
BLOCK = re.compile(re.escape(START) + '.*?' + re.escape(END), re.S)
RETURN = {'niagara-on-the-lake': 'Niagara Falls International (KIAG) or Buffalo (KBUF)',
          'quebec-city': 'Plattsburgh (KPBG) or Burlington (KBTV)',
          'victoria-bc': 'Friday Harbor (KFHR) or Bellingham (KBLI)'}
def dests():
    s = (ROOT / 'docs/destinations.js').read_text(); s = s[s.index('['):s.rindex(']') + 1]
    return {d['guide'].strip('/'): d for d in json.loads(s) if d.get('guide')}
def li(items): return ''.join(f'<li>{x}</li>' for x in items)
def block(slug, d):
    ret = RETURN.get(slug, 'a U.S. airport with customs')
    before = ['<b>Passports</b> for everyone aboard, plus your pilot certificate and medical.',
              '<b>Radio paperwork:</b> an FCC Restricted Radiotelephone Operator Permit for the pilot and an aircraft radio station license for international flight.',
              '<b>Insurance:</b> proof of liability insurance that meets Canadian requirements, carried on board.',
              '<b>CBP user-fee decal</b> on the aircraft for the return to the U.S.',
              '<b>Flight plan:</b> file one for the border crossing and keep your transponder on with an assigned code.']
    going = ['File <b>eAPIS</b> at least 60 minutes before leaving the U.S.',
             f'Call <b>CANPASS at 1-888-226-7277</b> 2 to 48 hours before you arrive, and land at {d["airport"]} within your stated arrival window.',
             'After landing, follow the CBSA instructions you were given; stay with the aircraft until you are cleared.']
    home = ['File <b>eAPIS</b> again at least 60 minutes before leaving Canada.',
            f'Land first at a U.S. airport with customs, such as {ret}. Confirm CBP hours and any advance-notice call before you go.',
            'Fuel in Canada is sold by the liter in Canadian dollars, plus taxes.']
    return (START + '<section id="border" style="padding-top:0"><div style="background:#fbf6ec;border:1px solid #eadcc0;border-radius:3px;padding:20px 22px">'
            '<span class="eyebrow">Crossing the border</span><h2 style="margin:6px 0 8px">Flying to Canada</h2>'
            f'<p style="margin:0 0 10px">{d["airport"]} is a Canadian airport of entry. A trip to Canada takes a little paperwork each way; here is the checklist.</p>'
            '<details style="margin:6px 0"><summary style="cursor:pointer;font-weight:700">Before you go</summary><ul style="line-height:1.6">' + li(before) + '</ul></details>'
            '<details style="margin:6px 0"><summary style="cursor:pointer;font-weight:700">Flying into Canada</summary><ul style="line-height:1.6">' + li(going) + '</ul></details>'
            '<details style="margin:6px 0"><summary style="cursor:pointer;font-weight:700">Coming home to the U.S.</summary><ul style="line-height:1.6">' + li(home) + '</ul></details>'
            '<p style="margin:12px 0 0;font-size:14px;color:#526471">Rules change; check the current requirements before every trip: '
            '<a href="https://www.aopa.org/go-fly/destinations/international-travel/canada" target="_blank" rel="noopener">AOPA’s Canada guide</a> · '
            '<a href="https://www.cbsa-asfc.gc.ca/prog/canpass/menu-eng.html" target="_blank" rel="noopener">CBSA CANPASS</a> · '
            '<a href="https://eapis.cbp.dhs.gov/" target="_blank" rel="noopener">CBP eAPIS</a></p></div></section>' + END)
D = dests()
for path in map(Path, sys.argv[1:]):
    slug = path.parent.name; d = D.get(slug)
    s = BLOCK.sub('', path.read_text())
    if d and d.get('region') == 'Canada':
        i = s.find('<section id="flight"'); j = s.find('</section>', i) + len('</section>')
        s = s[:j] + '\n' + block(slug, d) + s[j:]
    path.write_text(s)
