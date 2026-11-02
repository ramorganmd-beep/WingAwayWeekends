"""Add the feedback email link (hello@wingawayweekends.com) to site pages.

Usage: python3 tools/guides/feedback.py docs/index.html docs/*/index.html

Idempotent. Guides get a link in the footer and a line in the "Draft for
review" note; the homepage gets a footer link. Each mailto link carries a
subject naming the page. Run after (re)building a guide.
"""
import re
import sys
import urllib.parse
from pathlib import Path

EMAIL = 'hello@wingawayweekends.com'
MARK = re.compile(r'<(p|span) class="feedback"[^>]*>.*?</\1>', re.S)


def mailto(subject):
    return f'mailto:{EMAIL}?subject=' + urllib.parse.quote(subject)


for path in map(Path, sys.argv[1:]):
    s = MARK.sub('', path.read_text())
    if path.parent.name == 'docs':  # homepage
        link = mailto('WingAway Weekends feedback')
        a = 'WingAway Weekends · A short flight. A slower weekend.'
        assert s.count(a) == 1, path
        if '<div class="foot-brand">' not in s:
            s = s.replace(a, '<div class="foot-brand">' + a + '</div>')
        s = s.replace(a, a + f'<p class="feedback" style="margin:8px 0 0;color:#e6edf1;font-size:.9rem"><strong>Help us improve and grow.</strong> <a href="{link}" style="color:#ffffff">Suggest a destination or a correction</a> · {EMAIL}</p>')
    else:
        name = re.search(r'<h1>([^<]+)</h1>', s).group(1)
        link = mailto(f'WingAway feedback: {name} guide')
        note_anchor = '</p><p class="note">WingAway Weekends helps you discover the destination.'
        assert s.count(note_anchor) == 1, path
        s = s.replace(note_anchor, f' <span class="feedback">Spotted something out of date, or have a favorite we missed? <a href="{link}">Email us at {EMAIL}</a>.</span>' + note_anchor)
        brand = '<footer><a class="brand" href="#main">WingAway Weekends</a>'
        assert s.count(brand) == 1, path
        s = s.replace(brand, brand + f'<p class="feedback"><strong>Help us improve and grow.</strong> <a href="{link}">Suggest a correction or a destination</a></p>', 1)
    path.write_text(s)
    print('feedback link:', path)
