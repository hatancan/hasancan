#!/usr/bin/env python3
"""Üst başlık ve sekme menüsünü (ve stil/betik sürümlerini) ana sayfadan bütün alt sayfalara eşitler.

Ana sayfa (index.html) tek kaynaktır; Origmark mühür satırı da oradan bütün sayfaların <head>'ine eklenir. Kendi şablonunu taşıyan üreticiler (Buzanittin, eski sayfalar)
menüyü güncel tutamadığı için bu betik, verilen klasörlerdeki her index.html'de
<header class="ust">…</header> ve <nav class="sekmeler">…</nav> bloklarını ana sayfadakiyle değiştirir.
  python3 -I tools/menu_esitle.py [klasör ...]     (varsayılan: /var/www/hasancan)
deploy.sh her yayından sonra çalıştırır; buzanittin/tools/seri.py de kendi çıktısından sonra çağırır.
"""
import re, sys
from pathlib import Path

ANA = Path(__file__).resolve().parent.parent / 'index.html'


def parcalar():
    s = ANA.read_text(encoding='utf-8')
    ust = re.search(r'<header class="ust">.*?</header>', s, re.S).group(0)
    menu = re.search(r'<nav class="sekmeler".*?</nav>', s, re.S).group(0).replace(' class="aktif"', '')
    menu = re.sub(r'href="#', 'href="/#', menu)
    ust = re.sub(r'href="#', 'href="/#', ust)
    surum = re.search(r'style\.css\?v=(\d+)', s)
    return ust, menu, surum.group(1) if surum else None


def esitle(kok):
    ust, menu, surum = parcalar()
    n = 0
    for f in Path(kok).rglob('index.html'):
        if f.resolve() == ANA.resolve() or f.parent.resolve() == Path('/var/www/hasancan').resolve():
            continue
        s = f.read_text(encoding='utf-8', errors='replace')
        if '<nav class="sekmeler"' not in s:
            continue
        y = re.sub(r'<header class="ust">.*?</header>', lambda _: ust, s, count=1, flags=re.S)
        y = re.sub(r'<nav class="sekmeler".*?</nav>', lambda _: menu, y, count=1, flags=re.S)
        muhur = re.search(r'<script src="https://verify\.origmark\.com/muhur\.js[^"]*" async></script>', ANA.read_text(encoding='utf-8'))
        if muhur and 'muhur.js' not in y and '</head>' in y:  # Origmark mührü: ana sayfadaki satır her sayfanın <head>'ine
            y = y.replace('</head>', muhur.group(0) + '\n</head>', 1)
        if surum:
            y = re.sub(r'(/assets/(?:css/style\.css|lang/(?:tr|en|de)\.js|js/site\.js))(\?v=\d+)?"', rf'\1?v={surum}"', y)
        if y != s:
            f.write_text(y, encoding='utf-8'); n += 1
    print(f'menu_esitle: {kok} · {n} sayfa güncellendi')


if __name__ == '__main__':
    for k in (sys.argv[1:] or ['/var/www/hasancan']):
        esitle(k)
