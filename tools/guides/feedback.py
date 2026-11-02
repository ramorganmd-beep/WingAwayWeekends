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
        s = s.replace(a, a + f'<p class="feedback" style="margin:10px 0 0"><a href="{link}" style="color:inherit">Suggest a destination or a correction</a> · {EMAIL}</p>')
    else:
        name = re.search(r'<h1>([^<]+)</h1>', s).group(1)
        link = mailto(f'WingAway feedback: {name} guide')
        note_anchor = '</p><p class="note">WingAway Weekends helps you discover the destination.'
        assert s.count(note_anchor) == 1, path
        s = s.replace(note_anchor, f' <span class="feedback">Spotted something out of date, or have a favorite we missed? <a href="{link}">Email us at {EMAIL}</a>.</span>' + note_anchor)
        foot = re.search(r'(<footer><a class="brand" href="#main">WingAway Weekends</a><p>[^<]*</p>)', s)
        assert foot, path
        s = s.replace(foot.group(1), foot.group(1) + f'<p class="feedback"><a href="{link}">Suggest a correction or a destination</a></p>', 1)
    path.write_text(s)
    print('feedback link:', path)
