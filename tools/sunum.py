#!/usr/bin/env python3
"""Arşiv: PowerPoint sunumlarını blog yazısı biçiminde sayfaya çevirir.

İki adım:
  1) python3 -I tools/sunum.py donustur KAYNAK.ppt SLUG --ders "EEM101 – ..." --sinif 1 --tarih 2009-10-30
     → arsiv/SLUG/ içine orijinal dosya, PDF, tüm slayt görselleri (s-NN.jpg) ve slaytlar.txt (metin dökümü).
  2) arsiv/SLUG/yazi.md dosyasını yaz (slaytlar.txt'den, blog yazısı gibi; biçim aşağıda).
  3) python3 -I tools/sunum.py sayfa SLUG
     → arsiv/SLUG/index.html, arsiv/index.html, sitemap.xml. Yazıda kullanılmayan s-NN.jpg ve slaytlar.txt silinir.

yazi.md biçimi: başta '---' arasında 'baslik:' ve 'ozet:' satırları; sonra '## ' / '### ' başlıklar, paragraflar,
'- ' ve '1. ' listeler, '> ' alıntı, '| a | b |' tablolar, '![alt](s-NN.jpg "alt yazı")' görseller,
satır içinde **kalın** ve *eğik*.

Gerekenler: LibreOffice (soffice), poppler-utils (pdftoppm, pdftotext). Fontlar: Arial Narrow için Liberation Sans
Narrow, Tahoma için Wine Tahoma ~/.local/share/fonts altında olmalı; yoksa bazı slaytlarda yazılar sıkışık çıkar.
"""
import argparse, html, json, re, shutil, subprocess, sys, tempfile, zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

KOK = Path(__file__).resolve().parent.parent
ARSIV = KOK / 'arsiv'
SITE = 'https://hasancan.net'
A_NS = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
e = html.escape


# ---------------------------------------------------------------- dönüştürme

def calistir(*komut):
    subprocess.run(komut, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def slayt_metinleri(pptx, pdf):
    """Metni sunumun XML'inden al; gömülü nesne slaytlarında (XML'de metin yok) PDF'e düş."""
    z = zipfile.ZipFile(pptx)
    adlar = sorted((n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)),
                   key=lambda n: int(re.findall(r'\d+', n)[0]))
    metinler = []
    for i, ad in enumerate(adlar, 1):
        satirlar = []
        for p in ET.fromstring(z.read(ad)).iter(A_NS + 'p'):
            t = re.sub(r'\s+', ' ', ''.join(r.text or '' for r in p.iter(A_NS + 't'))).strip()
            if t:
                satirlar.append(t)
        if not satirlar:
            cikti = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-enc', 'UTF-8', str(pdf), '-'],
                                   capture_output=True, text=True).stdout
            satirlar = [re.sub(r'\s+', ' ', s).strip() for s in cikti.splitlines() if s.strip()]
        metinler.append(satirlar)
    return metinler


def kayitlari_oku():
    f = ARSIV / 'arsiv.json'
    return json.loads(f.read_text(encoding='utf-8')) if f.exists() else []


def kayitlari_yaz(kayitlar):
    (ARSIV / 'arsiv.json').write_text(json.dumps(kayitlar, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def donustur(a):
    hedef = ARSIV / a.slug
    hedef.mkdir(parents=True, exist_ok=True)
    kaynak = a.kaynak.resolve()
    pdf_kaynak = kaynak.suffix.lower() == '.pdf'
    with tempfile.TemporaryDirectory() as g:
        g = Path(g)
        if pdf_kaynak:
            pdf = kaynak
        else:
            profil = f'-env:UserInstallation=file://{g}/lo-profil'
            for bicim in ('pdf', 'pptx'):
                calistir('soffice', '--headless', '--norestore', profil, '--convert-to', bicim, '--outdir', str(g), str(kaynak))
            pdf, pptx = g / (kaynak.stem + '.pdf'), g / (kaynak.stem + '.pptx')
        for eski in hedef.glob('s-*.jpg'):
            eski.unlink()
        calistir('pdftoppm', '-r', '144', '-jpeg', '-jpegopt', 'quality=78,optimize=y', str(pdf), str(hedef / 's'))
        if pdf_kaynak:  # PDF'te metnin bir kısmı görsel olabilir: s-NN.jpg'lere de bak
            metinler = []
            for i in range(1, len(list(hedef.glob('s-*.jpg'))) + 1):
                cikti = subprocess.run(['pdftotext', '-layout', '-f', str(i), '-l', str(i), '-enc', 'UTF-8', str(pdf), '-'],
                                       capture_output=True, text=True).stdout
                metinler.append([l.rstrip() for l in cikti.splitlines() if l.strip()])
        else:
            metinler = slayt_metinleri(pptx, pdf)
        shutil.copyfile(kaynak, hedef / kaynak.name)
        if not pdf_kaynak:
            shutil.copyfile(pdf, hedef / pdf.name)
    for f in hedef.glob('s-*.jpg'):  # pdftoppm 1/01/001 diye adlandırabilir; iki haneye sabitle
        f.rename(hedef / f's-{int(f.stem[2:]):02d}.jpg')
    (hedef / 'slaytlar.txt').write_text(
        '\n\n'.join(f'## {"Sayfa" if pdf_kaynak else "Slayt"} {i}\n' + '\n'.join(s) for i, s in enumerate(metinler, 1)) + '\n', encoding='utf-8')

    kayitlar = [k for k in kayitlari_oku() if k['slug'] != a.slug]
    kayitlar.append({
        'slug': a.slug, 'ders': a.ders, 'sinif': a.sinif, 'tarih': a.tarih, 'eklenme': date.today().isoformat(),
        'tur': 'pdf' if pdf_kaynak else 'sunum', 'dosya': kaynak.name, 'boyut': kaynak.stat().st_size,
        'pdf': None if pdf_kaynak else pdf.name,
        'pdf_boyut': None if pdf_kaynak else (hedef / pdf.name).stat().st_size,
        'bicim': 'PDF' if pdf_kaynak else 'PowerPoint (.' + kaynak.suffix.lstrip('.') + ')',
        'sayfa': len(metinler),
    })
    kayitlari_yaz(kayitlar)
    print(f'{len(metinler)} {"sayfa" if pdf_kaynak else "slayt"} → arsiv/{a.slug}/  (şimdi yazi.md yaz, sonra: sunum.py sayfa {a.slug})')


# ---------------------------------------------------------------- yazı (küçük markdown)

def satir_ici(t):
    t = e(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', t)
    return t


def kimlik(baslik):
    t = baslik.lower().translate(str.maketrans('çğıöşüâî', 'cgiosuai'))
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


def yazi_coz(metin):
    """Ön bilgi + gövde HTML + içindekiler + kullanılan görseller."""
    m = re.match(r'---\n(.*?)\n---\n', metin, re.S)
    on = dict(re.findall(r'^(\w+):\s*(.+)$', m.group(1), re.M)) if m else {}
    satirlar = metin[m.end():].split('\n') if m else metin.split('\n')
    cikti, icindekiler, gorseller, i = [], [], [], 0
    while i < len(satirlar):
        s = satirlar[i]
        if not s.strip():
            i += 1
        elif s.startswith('```'):
            i += 1
            kod = []
            while i < len(satirlar) and not satirlar[i].startswith('```'):
                kod.append(satirlar[i])
                i += 1
            i += 1
            cikti.append('<pre class="kod"><code>' + e('\n'.join(kod), quote=False) + '</code></pre>')
        elif s.startswith('#'):
            seviye = len(s) - len(s.lstrip('#'))
            yazi = s[seviye:].strip()
            k = kimlik(yazi)
            if seviye == 2:
                icindekiler.append((k, yazi))
            cikti.append(f'<h{seviye} id="{k}">{satir_ici(yazi)}</h{seviye}>')
            i += 1
        elif s.startswith('!['):
            g = re.match(r'!\[(.*?)\]\((\S+?)(?:\s+"(.*?)")?\)', s)
            gorseller.append(g.group(2))
            alt_yazi = f'<figcaption>{satir_ici(g.group(3))}</figcaption>' if g.group(3) else ''
            cikti.append(f'<figure class="yazi-gorsel"><img src="{e(g.group(2))}" width="1440" height="1080" '
                         f'loading="lazy" decoding="async" alt="{e(g.group(1))}">{alt_yazi}</figure>')
            i += 1
        elif s.startswith('|'):
            blok = []
            while i < len(satirlar) and satirlar[i].startswith('|'):
                blok.append([h.strip() for h in satirlar[i].strip().strip('|').split('|')])
                i += 1
            bas, govde = blok[0], [r for r in blok[2:]]
            th = ''.join(f'<th scope="col">{satir_ici(h)}</th>' for h in bas)
            tr = ''.join('<tr>' + ''.join((f'<th scope="row">{satir_ici(h)}</th>' if j == 0 else f'<td>{satir_ici(h)}</td>')
                                          for j, h in enumerate(r)) + '</tr>' for r in govde)
            cikti.append(f'<div class="tablo-kap"><table class="yazi-tablo"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
        elif s.startswith('- ') or s.startswith('1. '):  # numaralı liste 1. ile başlamalı ("13. yüzyılda..." paragraftır)
            sirali = s.startswith('1. ')
            ogeler = []
            desen = r'\d+\. ' if sirali else r'- '
            while i < len(satirlar) and re.match(desen, satirlar[i]):
                ogeler.append(re.sub('^' + desen, '', satirlar[i]))
                i += 1
            etiket = 'ol' if sirali else 'ul'
            cikti.append(f'<{etiket}>' + ''.join(f'<li>{satir_ici(o)}</li>' for o in ogeler) + f'</{etiket}>')
        elif s.startswith('> '):
            parca = []
            while i < len(satirlar) and satirlar[i].startswith('> '):
                parca.append(satirlar[i][2:])
                i += 1
            cikti.append(f'<blockquote><p>{satir_ici(" ".join(parca))}</p></blockquote>')
        else:
            parca = []
            while i < len(satirlar) and satirlar[i].strip() and not re.match(r'(#|!\[|\||- |1\. |> |```)', satirlar[i]):
                parca.append(satirlar[i])
                i += 1
            cikti.append(f'<p>{satir_ici(" ".join(parca))}</p>')
    return on, '\n'.join(cikti), icindekiler, gorseller


# ---------------------------------------------------------------- sayfa kabuğu

def parca(kaynak_html, desen):
    m = re.search(desen, kaynak_html, re.S)
    if not m:
        sys.exit(f'index.html içinde bulunamadı: {desen}')
    return re.sub(r'href="#', 'href="/#', m.group(0))  # ana sayfa bölüm bağlantıları alt sayfalardan da çalışsın


def kabuk(baslik, aciklama, yol_url, yol, govde, ek_bas=''):
    ana = (KOK / 'index.html').read_text(encoding='utf-8')
    ust = parca(ana, r'<header class="ust">.*?</header>')
    menu = parca(ana, r'<nav class="sekmeler".*?</nav>').replace(' class="aktif"', '')
    alt = parca(ana, r'<footer class="alt">.*?</footer>')
    yol_html = ' <span aria-hidden="true">»</span> '.join(
        f'<a href="{h}">{t}</a>' if h else f'<span aria-current="page">{t}</span>' for t, h in yol)
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(baslik)} — hasancan.net</title>
<meta name="description" content="{e(aciklama)}">
<link rel="canonical" href="{SITE}{yol_url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(baslik)}">
<meta property="og:description" content="{e(aciklama)}">
<meta property="og:url" content="{SITE}{yol_url}">
<meta property="og:locale" content="tr_TR">
<meta name="theme-color" content="#3b5998">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/style.css">
{ek_bas}</head>
<body data-sekme="arsiv" data-baslik="{e(baslik)}">
<!-- Bu sayfa tools/sunum.py ile üretildi; elle düzenleme, yazi.md'yi değiştirip betiği yeniden çalıştır. -->
<div id="sayfa">
  {ust}
  {menu}
  <nav class="yol" data-i18n-attr="aria-label:arch.crumbs">{yol_html}</nav>
{govde}
  {alt}
</div>
<script src="/assets/lang/tr.js"></script>
<script src="/assets/lang/en.js"></script>
<script src="/assets/lang/de.js"></script>
<script src="/assets/js/site.js"></script>
</body>
</html>
'''


def boyut_yaz(n):
    return f'{n / 1048576:.1f} MB' if n >= 1048576 else f'{n / 1024:.0f} KB'


def tarih_yaz(t):
    return '.'.join(reversed(t.split('-')))


def yazi_sayfasi(k, on, govde, icindekiler):
    baslik, ozet = on['baslik'], on['ozet']
    url = f'/arsiv/{k["slug"]}/'
    kod = k['ders'].split(' ')[0]
    ld = json.dumps({
        '@context': 'https://schema.org', '@type': 'Article', 'headline': baslik, 'description': ozet,
        'inLanguage': 'tr', 'datePublished': k['eklenme'], 'url': SITE + url,
        'author': {'@type': 'Person', 'name': 'Hasan Can Öztürk', 'url': SITE + '/'},
        'isPartOf': {'@type': 'CollectionPage', 'name': 'Başkent Üniversitesi Arşivi', 'url': SITE + '/arsiv/'},
        'about': k['ders'],
        'associatedMedia': {'@type': 'MediaObject', 'name': k['dosya'], 'contentUrl': f'{SITE}{url}{k["dosya"]}'},
    }, ensure_ascii=False)
    pdf_kaynak = k.get('tur') == 'pdf'
    ikon = 'pdf' if pdf_kaynak else 'ppt'
    birim = 'arch.pagesLower' if pdf_kaynak else 'arch.slidesLower'
    toc = ''.join(f'<li><a href="#{a}">{satir_ici(t)}</a></li>' for a, t in icindekiler)
    indir = f'''<section class="kutu indir-kutu" id="indir">
        <h2 class="turuncu" data-i18n="arch.download"></h2>
        <div class="kutu-ic">
          <div class="dosya-ust">
            <span class="dosya-ikon {ikon}" aria-hidden="true">{ikon.upper()}</span>
            <div>
              <p class="indir-ad"><a href="{e(k['dosya'])}" download>{e(k['dosya'])}</a></p>
              <p class="kucuk">{e(k['bicim'])} · {boyut_yaz(k['boyut'])} · {k['sayfa']} <span data-i18n="{birim}"></span> · {tarih_yaz(k['tarih'])}</p>
            </div>
          </div>
          <p class="indir-satir">
            <a class="buton turuncu" href="{e(k['dosya'])}" download>⬇ <span data-i18n="{'arch.downloadFile' if pdf_kaynak else 'arch.downloadPpt'}"></span> ({boyut_yaz(k['boyut'])})</a>
            {'' if pdf_kaynak else f'<a class="buton" href="{e(k["pdf"])}" download>⬇ <span data-i18n="arch.downloadPdf"></span> ({boyut_yaz(k["pdf_boyut"])})</a>'}
          </p>
          <p class="telif" data-i18n="arch.copyright"></p>
        </div>
      </section>'''
    govde_html = f'''  <div class="kolonlar iki" id="ust">
    <aside class="sol">
      <section class="kutu">
        <h2 class="mavi" data-i18n="arch.fileInfo"></h2>
        <dl class="bilgiler">
          <dt data-i18n="arch.course"></dt><dd>{e(k['ders'])}</dd>
          <dt data-i18n="arch.year"></dt><dd>{k['sinif']}. <span data-i18n="arch.yearSuffix"></span></dd>
          <dt data-i18n="arch.date"></dt><dd>{tarih_yaz(k['tarih'])}</dd>
          <dt data-i18n="arch.format"></dt><dd>{e(k['bicim'])}</dd>
        </dl>
        <div class="kutu-ic"><a class="buton turuncu indir-yan" href="#indir">⬇ <span data-i18n="arch.download"></span></a></div>
      </section>
      <nav class="kutu" aria-labelledby="icindekiler-baslik">
        <h2 class="mavi" id="icindekiler-baslik" data-i18n="arch.toc"></h2>
        <ol class="icindekiler">{toc}</ol>
      </nav>
    </aside>
    <main class="orta">
      <article class="kutu yazi-sayfa" lang="tr">
        <h2 class="mavi"><span data-i18n="arch.post"></span> · {e(kod)}</h2>
        <div class="kutu-ic">
          <header class="yazi-bas">
            <h1>{e(baslik)}</h1>
            <p class="kucuk">{e(k['ders'])} · {tarih_yaz(k['tarih'])} · <span data-i18n="arch.addedOn"></span> {tarih_yaz(k['eklenme'])}</p>
          </header>
          <div class="yazi-govde-metin">
{govde}
          </div>
        </div>
      </article>
      {indir}
    </main>
  </div>'''
    yol = [('<span data-i18n="nav.home"></span>', '/'), ('<span data-i18n="nav.archive"></span>', '/arsiv/'),
           (f'{k["sinif"]}. <span data-i18n="arch.yearSuffix"></span>', f'/arsiv/#sinif-{k["sinif"]}'), (e(kod), '')]
    return kabuk(baslik, ozet, url, yol, govde_html,
                 f'<script type="application/ld+json">{ld}</script>\n')


def arsiv_dizini(kayitlar):
    satirlar = []
    hazir = [k for k in kayitlar if k.get('baslik')]
    for sinif in sorted({k['sinif'] for k in hazir}):
        satirlar.append(f'<tr class="sinif-satir" id="sinif-{sinif}"><td colspan="4">{sinif}. <span data-i18n="arch.yearSuffix"></span></td></tr>')
        for k in sorted((k for k in hazir if k['sinif'] == sinif), key=lambda k: (k['ders'], k['slug'])):
            satirlar.append(f'''<tr><td><span class="mini-ikon {'pdf' if k.get('tur') == 'pdf' else 'ppt'}" aria-hidden="true"></span><a href="/arsiv/{k['slug']}/">{e(k['baslik'])}</a></td>
              <td>{e(k['ders'])}</td><td class="gizle-mobil">{tarih_yaz(k['tarih'])}</td><td class="gizle-mobil">{boyut_yaz(k['boyut'])}</td></tr>''')
    son = max(hazir, key=lambda k: k['eklenme'])['baslik'] if hazir else '–'
    govde = f'''  <div class="kolonlar iki" id="ust">
    <aside class="sol">
      <section class="kutu">
        <h2 class="mavi" data-i18n="arch.about"></h2>
        <div class="kutu-ic"><p class="kucuk" data-i18n="arch.aboutText"></p></div>
      </section>
      <section class="kutu">
        <h2 class="yesil" data-i18n="arch.stats"></h2>
        <dl class="bilgiler">
          <dt data-i18n="arch.files"></dt><dd>{len(hazir)}</dd>
          <dt data-i18n="arch.lastAdded"></dt><dd>{e(son)}</dd>
        </dl>
      </section>
    </aside>
    <main class="orta">
      <section class="kutu">
        <h1 class="kutu-h1 mavi" data-i18n="arch.title"></h1>
        <div class="kutu-ic">
          <p data-i18n="arch.intro"></p>
          <table class="dosya-tablo">
            <thead><tr><th data-i18n="arch.file"></th><th data-i18n="arch.course"></th><th class="gizle-mobil" data-i18n="arch.date"></th><th class="gizle-mobil" data-i18n="arch.size"></th></tr></thead>
            <tbody>
            {chr(10).join(satirlar)}
            </tbody>
          </table>
        </div>
      </section>
    </main>
  </div>'''
    yol = [('<span data-i18n="nav.home"></span>', '/'), ('<span data-i18n="nav.archive"></span>', '')]
    return kabuk('Başkent Üniversitesi Arşivi',
                 'Hasan Can Öztürk\'ün Başkent Üniversitesi Elektrik-Elektronik Mühendisliği yıllarından ders notları ve sunumlar.',
                 '/arsiv/', yol, govde)


def site_haritasi(kayitlar):
    adresler = [('/', None), ('/arsiv/', None)] + [(f'/arsiv/{k["slug"]}/', k['eklenme']) for k in kayitlar if k.get('baslik')]
    ogeler = ''.join(f'  <url><loc>{SITE}{u}</loc>' + (f'<lastmod>{t}</lastmod>' if t else '') + '</url>\n' for u, t in adresler)
    (KOK / 'sitemap.xml').write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{ogeler}</urlset>\n',
        encoding='utf-8')


def sayfa(a):
    hedef = ARSIV / a.slug
    kayitlar = kayitlari_oku()
    k = next((k for k in kayitlar if k['slug'] == a.slug), None)
    if not k:
        sys.exit(f'arsiv.json içinde {a.slug} yok; önce "donustur" çalıştır.')
    on, govde, icindekiler, gorseller = yazi_coz((hedef / 'yazi.md').read_text(encoding='utf-8'))
    for gerekli in ('baslik', 'ozet'):
        if gerekli not in on:
            sys.exit(f'yazi.md ön bilgisinde "{gerekli}:" yok')
    eksik = [g for g in gorseller if not (hedef / g).exists()]
    if eksik:
        sys.exit(f'yazi.md şu görselleri istiyor ama yoklar: {eksik}')
    k['baslik'] = on['baslik']
    (hedef / 'index.html').write_text(yazi_sayfasi(k, on, govde, icindekiler), encoding='utf-8')
    for f in hedef.glob('s-*.jpg'):  # yazıda kullanılmayan slayt görselleri yayına gitmesin
        if f.name not in gorseller:
            f.unlink()
    (hedef / 'slaytlar.txt').unlink(missing_ok=True)
    kayitlari_yaz(kayitlar)
    (ARSIV / 'index.html').write_text(arsiv_dizini(kayitlar), encoding='utf-8')
    site_haritasi(kayitlar)
    print(f'arsiv/{a.slug}/index.html · {len(icindekiler)} bölüm · {len(gorseller)} görsel')


def main():
    ap = argparse.ArgumentParser()
    alt = ap.add_subparsers(dest='komut', required=True)
    d = alt.add_parser('donustur')
    d.add_argument('kaynak', type=Path)
    d.add_argument('slug')
    d.add_argument('--ders', required=True)
    d.add_argument('--sinif', type=int, required=True)
    d.add_argument('--tarih', required=True, help='YYYY-AA-GG')
    s = alt.add_parser('sayfa')
    s.add_argument('slug')
    a = ap.parse_args()
    donustur(a) if a.komut == 'donustur' else sayfa(a)


if __name__ == '__main__':
    main()
