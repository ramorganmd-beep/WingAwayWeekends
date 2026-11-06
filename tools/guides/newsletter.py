"""Add the newsletter signup box (Buttondown) just above the footer of site pages.

Usage: python3 tools/guides/newsletter.py docs/index.html docs/*/index.html

Idempotent: the block is wrapped in <!--wa-newsletter--> markers and replaced on each run.
The form posts to Buttondown and opens the confirmation in a new tab.
"""
import re
import sys
from pathlib import Path

USERNAME = 'wingawayweekends'
START, END = '<!--wa-newsletter-->', '<!--/wa-newsletter-->'
STYLE = ('<style>.wa-nl{background:#eef2f4;border-top:1px solid #dbe3e9;padding:34px 16px}'
         '.wa-nl-in{max-width:760px;margin:0 auto;display:flex;flex-wrap:wrap;gap:14px 28px;align-items:center;justify-content:space-between}'
         '.wa-nl h2{font:400 1.5rem/1.2 Georgia,serif;color:#102d40;margin:0 0 4px}'
         '.wa-nl p{margin:0;color:#526471;font:15px/1.45 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}'
         '.wa-nl form{display:flex;gap:8px;flex:1 1 300px;max-width:400px}'
         '.wa-nl input[type=email]{flex:1;min-width:0;font-size:16px;padding:11px 12px;border:1px solid #bac9d4;border-radius:4px;background:#fff;color:#102d40}'
         '.wa-nl button{font:600 15px system-ui,sans-serif;padding:11px 16px;border:0;border-radius:4px;background:#102d40;color:#fff;cursor:pointer}'
         '.wa-nl button:hover{background:#ba7d2f}'
         '.wa-nl .wa-nl-note{font-size:12px;color:#7a8a96;margin-top:6px}</style>')


def block():
    return (START + STYLE + '<section class="wa-nl" aria-label="Newsletter signup"><div class="wa-nl-in"><div>'
            '<h2>Get a new getaway in your inbox</h2>'
            '<p>One fly-in weekend, a Fly to Lunch pick and the newest guides, about once a month.</p>'
            '<p class="wa-nl-note">Free. Unsubscribe anytime.</p></div>'
            f'<form action="https://buttondown.com/api/emails/embed-subscribe/{USERNAME}" method="post" target="_blank" rel="noopener">'
            '<label for="wa-nl-email" style="position:absolute;left:-9999px">Email address</label>'
            '<input id="wa-nl-email" type="email" name="email" placeholder="you@example.com" autocomplete="email" required>'
            '<input type="hidden" name="embed" value="1">'
            '<button type="submit">Subscribe</button></form></div></section>' + END)


FOOTER = re.compile(r'<footer[ >]')
for path in map(Path, sys.argv[1:]):
    s = path.read_text()
    s = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', s, flags=re.S)
    m = FOOTER.search(s)
    if not m:
        continue
    s = s[:m.start()] + block() + s[m.start():]
    path.write_text(s)
    print('newsletter:', path)
