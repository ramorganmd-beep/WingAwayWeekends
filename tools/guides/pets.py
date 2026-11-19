"""Add a "Dogs welcome" note to stay cards whose hotel's own website confirms it.

Usage: python3 tools/guides/pets.py docs/<slug>/index.html [...]
Idempotent (replaces the wa-pet spans). Only hotels in PETS get a note; the homepage
"Bringing the dog" switch uses destinations.js "pets": true, set for these guides.
Each note was checked on the hotel's own pet page or FAQ on the date in CHECKED.
"""
import re, sys
from pathlib import Path
CHECKED = 'Nov 2026'
PETS = {
    'charleston': {
        'The Ansonborough': 'Dogs welcome; optional pet package.',
        'Wentworth Mansion': 'Dogs welcome in limited rooms, $40 a day; book through the concierge.',
        'The Vendue': 'Dogs welcome, one-time pet fee.',
        'The Charleston Place': 'Pets welcome, up to two; tell reservations ahead.',
        'Hotel Bennett': 'Dogs welcome in guest rooms, not in public spaces.',
    },
    'sedona': {
        'L’Auberge de Sedona': 'Dogs welcome in designated rooms; call reservations to book one.',
        'Enchantment Resort': 'Dogs welcome, with a pet program and dog-friendly trails.',
    },
    'bar-harbor': {
        'West Street Hotel': 'Dogs welcome in select rooms; fees and restrictions apply.',
        'Balance Rock Inn': 'Pets welcome in a few rooms, $50 per pet per night; call to book.',
    },
    'key-west': {
        'Sunset Key Cottages': 'Dogs up to 50 lbs welcome.',
    },
    'smoky-mountains': {
        'Dancing Bear Lodge': 'Dogs welcome in the standalone cabins (two max), $75 per stay.',
    },
    'savannah': {
        'Olde Harbour Inn': 'Pet-friendly suites; ask about fees when you book.',
        'Hotel Bardo Savannah': 'Dogs welcome: one up to 50 lbs, or two totaling 75 lbs; $200 nonrefundable fee.',
    },
    'asheville': {
        'The Foundry Hotel': 'Pets welcome, $75 per pet per stay.',
        'The Windsor Boutique Hotel': 'Dogs welcome in designated King Suites, $50 per pet per night.',
    },
    'st-augustine': {
        'St. Francis Inn': 'Dog-friendly rooms; see the inn’s dog-friendly lodging page.',
    },
    'destin': {
        'Henderson Beach Resort': 'Dogs welcome in select rooms; arrange it with the resort in advance.',
        'Sandestin Golf and Beach Resort': 'Select pet-friendly units; limited, so book early.',
    },
    'beaufort': {
        'Anchorage 1770': 'Dog-friendly inn; ask for details when you book.',
    },
    '30a': {
        'The Pearl Hotel': 'One pet under 30 lbs in designated rooms; request it when you book.',
        'Hotel Effie': 'Well-trained dogs up to 65 lbs welcome.',
    },
}
MARK = re.compile(r'<p class="wa-pet"[^>]*>.*?</p>', re.S)


def note(t):
    return (f'<p class="wa-pet" style="margin:8px 0 0;font-size:.88rem;color:#2d5a3d">'
            f'<span aria-hidden="true">🐾</span> <b>Dogs:</b> {t} <span style="color:#647784">Checked {CHECKED}; confirm when you book.</span></p>')


for path in map(Path, sys.argv[1:]):
    slug = path.parent.name
    s = MARK.sub('', path.read_text())
    for name, t in PETS.get(slug, {}).items():
        m = re.search(r'(<article class="card">(?:(?!</article>).)*?<h3>' + re.escape(name) + r'</h3>(?:(?!</article>).)*?)(<a class="textlink"|</article>)', s, re.S)
        if not m:
            print('pets: no card', slug, name, file=sys.stderr); continue
        s = s[:m.end(1)] + note(t) + s[m.end(1):]
    path.write_text(s)
