"""Add a "Check the weekend weather" link to each guide's route box, pointing at the weather outlook (docs/wx/).

Usage: python3 tools/guides/wx_link.py docs/<slug>/index.html [...]
Idempotent (replaces the block between wa-wx markers). The link opens /wx/ with this guide as the
destination; a small script adds the home airport the guide is showing (?from= or the saved home).
"""
import re, sys
from pathlib import Path
START, END = '<!--wa-wx-->', '<!--/wa-wx-->'
BLOCK = re.compile(re.escape(START) + '.*?' + re.escape(END), re.S)
ANCHOR = 'Use ForeFlight for your actual flight plan.</p>'


def block(slug):
    return (START + f'<p class="estimate wa-wx" style="margin-top:10px"><a class="textlink" data-wx href="../wx/?to={slug}">'
            'Check the weekend weather at both ends →</a> <span style="color:#647784">Flight category, your minimums and '
            'the crosswind on the best runway.</span></p>'
            '<script>(function(){var a=document.querySelector("[data-wx]");if(!a)return;var h=new URLSearchParams(location.search).get("from");'
            'try{h=h||localStorage.getItem("wingaway-home")}catch(e){}if(h&&/^[A-Za-z0-9]{3,4}$/.test(h))a.href+="&from="+h.toUpperCase()})()</script>' + END)


for path in map(Path, sys.argv[1:]):
    s = BLOCK.sub('', path.read_text())
    i = s.find(ANCHOR)
    if i < 0:
        print('no route box', path); continue
    i += len(ANCHOR)
    path.write_text(s[:i] + block(path.parent.name) + s[i:])
