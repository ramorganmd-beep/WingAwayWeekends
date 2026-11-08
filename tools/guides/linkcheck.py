"""Check every outside link on the published site and report the ones that need a look.

Usage: python3 tools/guides/linkcheck.py [--out reports/linkcheck-YYYY-MM-DD.md] [--workers 12]

What it checks: each hotel, restaurant, FBO, park and visitor-info link in docs/*/index.html.
Skipped: our own pages, photo-credit links (Unsplash, Wikimedia, Creative Commons, LOC),
Google Maps, Stay22 partner links and mailto links.

Each link is sorted into:
  broken   - 404/410, server errors, or the site can't be reached (closed, expired domain)
  parked   - the page now looks like a parked or for-sale domain
  moved    - it redirects to a different website (rebrand, new owner, or a closure page)
  blocked  - the site refuses automated checks (403/429); check by hand if it matters
Only problems are written to the report, grouped by page, with the link text so you know which business it is.
Uses an honest User-Agent and checks each unique URL once.
"""
import argparse, collections, concurrent.futures as cf, datetime, glob, html, re, sys
from pathlib import Path
from urllib.parse import urlparse
import os
import requests

ROOT = Path(__file__).resolve().parents[2]
CA = os.environ.get('REQUESTS_CA_BUNDLE') or ('/root/.ccr/ca-bundle.crt' if os.path.exists('/root/.ccr/ca-bundle.crt') else True)
UA = 'WingAwayWeekends-linkcheck/1.0 (https://wingawayweekends.com; hello@wingawayweekends.com)'
SKIP = ('wingawayweekends.com', 'unsplash.com', 'wikimedia.org', 'wikipedia.org', 'creativecommons.org', 'loc.gov',
        'google.com', 'goo.gl', 'stay22.com', 'apple.com/maps', 'maps.apple.com')
SKIP_PAGES = {'photo-options', 'hero-options', 'cirrus'}
PARKED = ('domain is for sale', 'buy this domain', 'this domain may be for sale', 'hugedomains.com', 'sedoparking',
          'afternic.com', 'parkingcrew', 'bodis.com', 'this domain has expired', 'domain has expired and is pending',
          'godaddy.com/domainsearch', 'is parked free', 'this web page is parked')
CLOSED = ('permanently closed', 'closed permanently', 'closed for good', 'has closed its doors', 'have closed our doors',
          'we have closed', 'is now closed', 'ceased operations')
A_RE = re.compile(r'<a\b[^>]*href="(https?://[^"#]+)[^"]*"[^>]*>(.*?)</a>', re.S | re.I)

def base(host):
    host = host.lower().split(':')[0]
    if host.startswith('www.'): host = host[4:]
    parts = host.split('.')
    return '.'.join(parts[-3:]) if len(parts) > 2 and len(parts[-1]) == 2 and len(parts[-2]) <= 3 else '.'.join(parts[-2:])

def collect():
    links = collections.defaultdict(list)  # url -> [(page, text)]
    for f in sorted(glob.glob(str(ROOT / 'docs/*/index.html'))):
        page = Path(f).parent.name
        if page in SKIP_PAGES: continue
        s = Path(f).read_text(errors='ignore')
        for url, inner in A_RE.findall(s):
            u = html.unescape(url)
            if any(k in u for k in SKIP): continue
            text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', inner))).strip()[:80]
            links[u].append((page, text))
    return links

def check(url):
    s = requests.Session(); s.headers.update({'User-Agent': UA, 'Accept': 'text/html,*/*'})
    last = None
    for attempt in range(2):
        try:
            r = s.get(url, timeout=20, allow_redirects=True, stream=True, verify=CA)
            body = ''
            ctype = r.headers.get('content-type', '')
            if 'html' in ctype:
                body = r.raw.read(200000, decode_content=True).decode(r.encoding or 'utf-8', 'ignore').lower()
            r.close()
            code = r.status_code
            if code in (401, 403, 405, 406, 429, 999):
                return 'blocked', f'HTTP {code}', r.url
            if code in (404, 410) or code >= 500:
                last = ('broken', f'HTTP {code}', r.url)
                continue
            if any(p in body for p in CLOSED):
                return 'closed', 'page mentions a closure', r.url
            if any(p in body for p in PARKED):
                return 'parked', 'looks like a parked or for-sale domain', r.url
            if base(urlparse(r.url).netloc) != base(urlparse(url).netloc):
                return 'moved', 'redirects to another website', r.url
            return 'ok', f'HTTP {code}', r.url
        except requests.exceptions.SSLError as e:
            msg = str(e)
            last = ('broken', 'security certificate has expired (browsers show a warning)', url) if 'expired' in msg else ('unreachable', 'certificate could not be verified from the checker', url)
        except requests.exceptions.ConnectionError as e:
            last = ('unreachable', 'could not connect from the checker', url)
        except requests.exceptions.Timeout:
            last = ('unreachable', 'timed out', url)
        except Exception as e:
            last = ('broken', type(e).__name__, url)
    return last

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out'); ap.add_argument('--workers', type=int, default=12); ap.add_argument('--limit', type=int)
    a = ap.parse_args()
    links = collect()
    urls = list(links)[:a.limit] if a.limit else list(links)
    print(f'checking {len(urls)} unique links on {len({p for v in links.values() for p, _ in v})} pages', file=sys.stderr)
    results = {}
    with cf.ThreadPoolExecutor(a.workers) as ex:
        futs = {ex.submit(check, u): u for u in urls}
        for i, f in enumerate(cf.as_completed(futs), 1):
            results[futs[f]] = f.result()
            if i % 250 == 0: print(f'  {i}/{len(urls)}', file=sys.stderr)
    counts = collections.Counter(r[0] for r in results.values())
    today = datetime.date.today().isoformat()
    out = Path(a.out) if a.out else ROOT / f'reports/linkcheck-{today}.md'
    out.parent.mkdir(parents=True, exist_ok=True)
    label = {'closed': 'Closure notice', 'broken': 'Broken', 'parked': 'Parked or for sale', 'moved': 'Redirects to another site', 'blocked': 'Site blocks automated checks'}
    bypage = collections.defaultdict(list)
    for u, (kind, why, final) in results.items():
        if kind in ('ok', 'blocked', 'unreachable'): continue
        for page, text in links[u]:
            bypage[page].append((kind, text, u, why, final))
    lines = [f'# Link check, {today}', '',
             f'{len(results)} unique outside links checked: {counts["ok"]} OK, {counts["closed"]} with a closure notice, {counts["broken"]} broken, {counts["parked"]} parked, {counts["unreachable"]} unreachable from the checker, '
             f'{counts["moved"]} redirect to another site, {counts["blocked"]} blocked automated checks.', '',
             'Fix broken and parked links first. "Redirects" are often fine (a hotel joining a brand) but can mean a closure. '
             '"Blocked" sites usually work in a normal browser.', '']
    order = ['closed', 'broken', 'parked', 'moved']
    for page in sorted(bypage, key=lambda p: (min(order.index(k) for k, *_ in bypage[p]), p)):
        lines.append(f'## {page}')
        for kind, text, u, why, final in sorted(bypage[page], key=lambda x: order.index(x[0])):
            extra = f' → {final}' if final and final != u and kind == 'moved' else ''
            lines.append(f'- **{label[kind]}**: {text or "(no link text)"} — {u} ({why}){extra}')
        lines.append('')
    unreach = sorted({u for u, r in results.items() if r[0] == 'unreachable'})
    if unreach:
        lines += ['## Could not reach from the checker', '', 'Often a network quirk on our side; open these in a browser to confirm.', ''] + [f'- {links[u][0][1] or u} ({links[u][0][0]}) — {u}' for u in unreach] + ['']
    blocked = sorted({base(urlparse(u).netloc) for u, r in results.items() if r[0] == 'blocked'})
    if blocked:
        lines += ['## Sites that block automated checks', '', 'These usually open fine in a browser; spot-check one or two now and then.', '', ', '.join(blocked), '']
    out.write_text('\n'.join(lines))
    print(f'wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}; ' + ', '.join(f'{k} {v}' for k, v in counts.items()), file=sys.stderr)

if __name__ == '__main__':
    main()
