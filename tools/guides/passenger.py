"""Passenger view for every guide: one page, two views.

Usage: python3 tools/guides/passenger.py docs/<guide>/index.html [...]

Adds a "Send to my passenger" button to the guide's hero. It shares (or copies) the guide's link with
?for=passenger, which opens a jargon-free view: the route box, weather and FBO details and the
Aviation section are hidden, and a short "Your weekend" box explains the flight and what to pack.
Idempotent: everything sits between <!--wa-pax...--> markers.
"""
import re
import sys
from pathlib import Path

HEAD = ('<!--wa-pax-head--><script>if(/[?&]for=passenger\\b/.test(location.search))document.documentElement.classList.add("wa-pax")</script>'
        '<style>html.wa-pax .snapshot,html.wa-pax #route-note,html.wa-pax .estimate,html.wa-pax .wa-wx,html.wa-pax .wa-ground,'
        'html.wa-pax #flight,html.wa-pax a[href="#flight"],html.wa-pax .wa-pax-send{display:none!important}'
        '.wa-pax-box{display:none}html.wa-pax .wa-pax-box{display:block;margin:22px 0 8px;padding:20px 22px;background:#fff;'
        'border:1px solid #dbe3e9;border-left:4px solid #efbd70;border-radius:3px}.wa-pax-box h2{margin:0 0 8px;font-size:1.5rem}'
        '.wa-pax-box ul{margin:8px 0 10px;padding-left:20px;line-height:1.65;color:#33475a}.wa-pax-box p{margin:6px 0;color:#33475a}'
        '.wa-pax-box .wa-pax-jump a{margin-right:14px;font-weight:600}.wa-pax-box .wa-pax-note{font-size:.85rem;color:#647784}'
        '.wa-pax-send{font:inherit;font-size:14px;cursor:pointer;background:none;border:0;padding:0;color:#18548c;text-decoration:underline;text-underline-offset:4px}.wa-pax-sent{margin-left:10px;font-size:.9rem;color:#3f6d4f}.wa-pax-toggle{display:inline-flex;border:1px solid #102d40;border-radius:999px;overflow:hidden}.wa-pax-toggle a{padding:6px 14px;font-size:14px;font-weight:600;color:#102d40;text-decoration:none;white-space:nowrap}html:not(.wa-pax) .wa-pax-toggle a[data-pax-view=pilot],html.wa-pax .wa-pax-toggle a[data-pax-view=pax]{background:#102d40;color:#fff}</style><!--/wa-pax-head-->')

PACK = [
    'Pack light in soft bags.',
    'Dress in layers. It can be cool in the air and warm on the ramp.',
    'Plans may shift with the weather: a later start, an earlier trip home or an unexpected extra night is part of flying ourselves.',
    'Let’s remember to bring water, a snack, sunglasses and any medicine we might need.',
    'Reminder: we’ll need our walking shoes.',
]


def box(name, sections):
    jump = ' '.join(f'<a href="#{sid}">{label}</a>' for sid, label in sections)
    items = ''.join(f'<li>{t}</li>' for t in PACK)
    return ('<!--wa-pax-box--><div class="wa-pax-box" aria-label="Our weekend">'
            f'<h2>Our weekend in {name}</h2>'
            '<p data-pax-flight>In our plane it’s a short flight.</p>'
            f'<p class="wa-pax-jump">{jump}</p>'
            '<h3 class="subhead" style="margin:14px 0 4px">What you need to know for this flight</h3>'
            f'<ul>{items}</ul>'
            '<p class="wa-pax-note">I’ll handle the flight planning; you handle the fun planning!</p></div><!--/wa-pax-box-->')


SCRIPT = ('<!--wa-pax-js--><script>(function(){var d=document,pax=d.documentElement.classList.contains("wa-pax");'
          'var fr=new URLSearchParams(location.search).get("from");try{fr=fr||localStorage.getItem("wingaway-home")}catch(e){}'
          'fr=fr&&/^[A-Za-z0-9]{3,4}$/.test(fr)?fr.toUpperCase():"";'
          'd.querySelectorAll("[data-pax-view]").forEach(function(a){var v=a.getAttribute("data-pax-view");'
          'a.href=location.pathname+(v==="pax"?"?for=passenger"+(fr?"&from="+fr:""):(fr?"?from="+fr:""));'
          'if((v==="pax")===pax)a.setAttribute("aria-current","page");});'
          'if(pax){var t=d.querySelector("[data-time]"),f=d.querySelector("[data-pax-flight]"),l=d.querySelector(".intro .lede");if(l)l.textContent="Our exciting weekend!";'
          'setTimeout(function(){if(t&&f){var x=t.textContent.replace(/\\s+/g," ").trim();'
          'var hr=+((x.match(/(\\d+) hr/)||[0,0])[1]);f.textContent="In our plane it will be about "+x.replace(/^~/,"")+(hr>=4?" of flying, with a stop or two for fuel along the way.":".");}},400);return;}'
          'var b=d.querySelector(".wa-pax-send");if(!b)return;b.addEventListener("click",function(){'
          'var h=new URLSearchParams(location.search).get("from");try{h=h||localStorage.getItem("wingaway-home")}catch(e){}var u=location.origin+location.pathname+"?for=passenger"+(h&&/^[A-Za-z0-9]{3,4}$/.test(h)?"&from="+h.toUpperCase():""),title=d.title.split("|")[0].trim();'
          'var done=function(m){var s=b.nextElementSibling;if(!s||!s.classList.contains("wa-pax-sent")){s=d.createElement("span");'
          's.className="wa-pax-sent";b.after(s);}s.textContent=m;};'
          'if(navigator.share){navigator.share({title:title,text:"Our weekend: here’s the plan",url:u}).catch(function(){});}'
          'else if(navigator.clipboard){navigator.clipboard.writeText(u).then(function(){done("Link copied. Paste it in a text or email.")});}'
          'else{prompt("Copy this link for your passenger:",u);}});})();</script><!--/wa-pax-js-->')

LABELS = [('stay', 'Where we’re staying'), ('eat', 'Dinner'), ('explore', 'Things to do'), ('shopping', 'Shopping'),
          ('itinerary', 'The plan')]
MARK = re.compile(r'<!--wa-pax-(head|box|js|btn)-->.*?<!--/wa-pax-\1-->', re.S)


def main(paths):
    n = 0
    for p in map(Path, paths):
        s = MARK.sub('', p.read_text())
        if 'data-dest=' not in s or '<div class="snapshot"' not in s or '<div class="hero-actions">' not in s:
            continue
        name = re.search(r'<h1>([^<]+)</h1>', s).group(1)
        sections = [(sid, label) for sid, label in LABELS if f'<section id="{sid}"' in s]
        s = s.replace('</head>', HEAD + '</head>', 1)
        i = s.index('<div class="hero-actions">')
        j = s.index('</div>', i)
        s = s[:j] + ('<!--wa-pax-btn--><span class="wa-pax-toggle" role="group" aria-label="View">'
                     '<a href="?" data-pax-view="pilot">Pilot view</a><a href="?for=passenger" data-pax-view="pax">Passenger view</a></span>'
                     '<button type="button" class="secondary wa-pax-send">Send to my passenger</button>'
                     '<!--/wa-pax-btn-->') + s[j:]
        s = s.replace('<div class="snapshot"', box(name, sections) + '<div class="snapshot"', 1)
        s = s.replace('</body>', SCRIPT + '</body>', 1)
        p.write_text(s)
        n += 1
    print(f'passenger view: {n} guides')


if __name__ == '__main__':
    main(sys.argv[1:])
