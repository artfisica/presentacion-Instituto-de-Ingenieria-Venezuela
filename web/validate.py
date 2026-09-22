#!/usr/bin/env python3
"""Check both editions and their local dependencies, without network access."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parent

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs = path, [], []
        self.lang, self.headings, self.images = None, [], 0
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'h1':
            self.headings.append(tag)
        if tag == 'img':
            self.images += 1
            assert a.get('alt'), f'{self.path.name}: missing image description'
        for key in ('src', 'href'):
            if a.get(key):
                self.refs.append(a[key])

def main():
    pages = {name: Page(ROOT/name) for name in ('index.html', 'en.html')}
    count = 0
    project_count = 0
    for name, page in pages.items():
        assert page.lang == ('es' if name == 'index.html' else 'en')
        assert len(page.headings) == 1, f'{name}: expected one primary heading'
        assert len(page.ids) == len(set(page.ids)), f'{name}: duplicate IDs'
        assert page.ids.index('charla') < page.ids.index('arturo')
        page_project_count = sum(x.startswith('project-') for x in page.ids)
        assert page_project_count == 10
        project_count += page_project_count
        for ref in page.refs:
            u = urlsplit(ref)
            if u.scheme or u.netloc:
                assert u.scheme in ('https', 'mailto'), f'Unexpected URL: {ref}'
                continue
            dest = (page.path.parent/unquote(u.path)).resolve() if u.path else page.path
            assert dest.is_relative_to(ROOT), f'Outside project: {ref}'
            assert dest.is_file(), f'{name}: missing {ref}'
            if u.fragment and dest.suffix == '.html':
                target = pages.get(dest.name) or Page(dest)
                assert unquote(u.fragment) in target.ids, f'{name}: missing anchor {ref}'
            count += 1
    css = ROOT/'assets/style.css'
    for ref in re.findall(r'url\([\'"]?([^\)\'\"]+)', css.read_text()):
        assert (css.parent/ref).is_file(), f'Missing CSS dependency: {ref}'
    asset_bytes = sum(p.stat().st_size for p in (ROOT/'assets').rglob('*') if p.is_file())
    assert asset_bytes <= 600_000, f'Web assets exceed 600 kB: {asset_bytes:,} bytes'
    print(f'Web asset budget: {asset_bytes:,} / 600,000 bytes (PDF TTF fonts are not served).')
    print(f'OK: two languages, {project_count} project cards, {count} local references, image descriptions and font files.')
    print('External URLs are editorial references; this check does not request them.')

if __name__ == '__main__':
    main()
