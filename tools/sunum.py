#!/usr/bin/env python3
"""Bir PowerPoint sunumunu arşiv sayfasına çevirir.

Kullanım:
  python3 -I tools/sunum.py KAYNAK.ppt SLUG --ders "EEM101 – ..." --sinif 1 --tarih 2009-10-30 [--baslik "..."]

Üretir:  arsiv/SLUG/index.html, slayt görselleri (s-NN.jpg), orijinal dosya ve PDF kopyası.
Ayrıca arsiv/arsiv.json kaydını günceller ve arsiv/index.html'i yeniden üretir.
Gerekenler: LibreOffice (soffice), poppler-utils (pdftoppm, pdftotext).
Fontlar: Arial Narrow için Liberation Sans Narrow, Tahoma için Wine Tahoma ~/.local/share/fonts altında olmalı;
yoksa bazı slaytlarda yazılar sıkışık çıkar.
"""
import argparse, html, json, re, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

KOK = Path(__file__).resolve().parent.parent
ARSIV = KOK / 'arsiv'
A_NS = '{http://schemas.openxmlformats.org/drawingml/2006/main}'


def calistir(*komut):
    subprocess.run(komut, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def donustur(kaynak, gecici):
    profil = f'-env:UserInstallation=file://{gecici}/lo-profil'
    for bicim in ('pdf', 'pptx'):
        calistir('soffice', '--headless', '--norestore', profil, '--convert-to', bicim, '--outdir', str(gecici), str(kaynak))
    return gecici / (kaynak.stem + '.pdf'), gecici / (kaynak.stem + '.pptx')


def slayt_metinleri(pptx, pdf):
    """Metni sunumun XML'inden al; gömülü nesne slaytlarında (XML'de metin yok) PDF'e düş."""
    z = zipfile.ZipFile(pptx)
    adlar = sorted((n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)),
                   key=lambda n: int(re.findall(r'\d+', n)[0]))
    metinler = []
    for i, ad in enumerate(adlar, 1):
        kok = ET.fromstring(z.read(ad))
        satirlar = []
        for p in kok.iter(A_NS + 'p'):
            t = re.sub(r'\s+', ' ', ''.join(r.text or '' for r in p.iter(A_NS + 't'))).strip()
            if t:
                satirlar.append(t)
        if not satirlar:
            cikti = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-enc', 'UTF-8', str(pdf), '-'],
                                   capture_output=True, text=True).stdout
            satirlar = [re.sub(r'\s+', ' ', s).strip() for s in cikti.splitlines() if s.strip()]
        metinler.append(satirlar)
    return metinler


def parca(kaynak_html, desen):
    m = re.search(desen, kaynak_html, re.S)
    if not m:
        sys.exit(f'index.html içinde bulunamadı: {desen}')
    # Ana sayfadaki "#bolum" bağlantıları alt sayfalardan da çalışsın
    return re.sub(r'href="#', 'href="/#', m.group(0))


def kabuk(baslik, sekme, yol, govde):
    ana = (KOK / 'index.html').read_text(encoding='utf-8')
    ust = parca(ana, r'<header class="ust">.*?</header>')
    menu = parca(ana, r'<nav class="sekmeler".*?</nav>').replace(' class="aktif"', '')
    alt = parca(ana, r'<footer class="alt">.*?</footer>')
    yol_html = ' <span aria-hidden="true">»</span> '.join(
        f'<a href="{h}"{a}>{t}</a>' if h else f'<span{a}>{t}</span>' for t, h, a in yol)
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(baslik)} — hasancan.net</title>
<meta name="description" content="{html.escape(baslik)} · hasancan.net arşivi">
<meta name="theme-color" content="#3b5998">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body data-sekme="{sekme}" data-baslik="{html.escape(baslik)}">
<!-- Bu sayfa tools/ altındaki betikle üretildi; elle düzenleme, betiği yeniden çalıştır. -->
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


def sunum_sayfasi(kayit, metinler):
    n = len(metinler)
    e = html.escape
    no_listesi = ''.join(f'<li><a href="#s{i}">{i}</a></li>' for i in range(1, n + 1))
    slaytlar = []
    for i, satirlar in enumerate(metinler, 1):
        alt = e(' · '.join(satirlar))[:300] or f'Slayt {i}'
        metin = '\n'.join(e(s) for s in satirlar)
        detay = (f'<details><summary data-i18n="arch.slideText"></summary><p class="slayt-metin">{metin}</p></details>'
                 if satirlar else '')
        slaytlar.append(f'''        <figure class="slayt" id="s{i}">
          <figcaption class="slayt-bar"><span><span data-i18n="arch.slide"></span> {i} / {n}</span><a href="#ust" data-i18n="arch.top"></a></figcaption>
          <img src="s-{i:02d}.jpg" width="1440" height="1080" loading="{'eager' if i <= 2 else 'lazy'}" decoding="async" alt="{alt}">
          {detay}
        </figure>''')
    d = kayit
    govde = f'''  <div class="kolonlar iki" id="ust">
    <aside class="sol">
      <section class="kutu">
        <h2 class="turuncu" data-i18n="arch.download"></h2>
        <div class="kutu-ic indir">
          <a class="buton turuncu" href="{e(d['dosya'])}" download><span>{e(d['dosya'])}</span><small>{boyut_yaz(d['boyut'])}</small></a>
          <a class="buton" href="{e(d['pdf'])}" download><span>PDF</span><small>{boyut_yaz(d['pdf_boyut'])}</small></a>
        </div>
      </section>
      <section class="kutu">
        <h2 class="mavi" data-i18n="arch.fileInfo"></h2>
        <dl class="bilgiler">
          <dt data-i18n="arch.course"></dt><dd>{e(d['ders'])}</dd>
          <dt data-i18n="arch.year"></dt><dd><span>{d['sinif']}.</span> <span data-i18n="arch.yearSuffix"></span></dd>
          <dt data-i18n="arch.date"></dt><dd>{'.'.join(reversed(d['tarih'].split('-')))}</dd>
          <dt data-i18n="arch.format"></dt><dd>{e(d['bicim'])}</dd>
          <dt data-i18n="arch.slides"></dt><dd>{n}</dd>
        </dl>
      </section>
      <section class="kutu">
        <h2 class="mavi" data-i18n="arch.jump"></h2>
        <ol class="sayfa-no">{no_listesi}</ol>
      </section>
    </aside>
    <main class="orta">
      <section class="kutu">
        <h2 class="mavi" data-i18n="arch.presentation"></h2>
        <div class="kutu-ic">
          <div class="dosya-ust">
            <span class="dosya-ikon ppt" aria-hidden="true">PPT</span>
            <div>
              <h1 class="dosya-baslik">{e(d['baslik'])}</h1>
              <p class="kucuk">{e(d['ders'])} · {'.'.join(reversed(d['tarih'].split('-')))} · {n} <span data-i18n="arch.slidesLower"></span></p>
            </div>
          </div>
          <p class="indir-satir">
            <a class="buton turuncu kucuk-buton" href="{e(d['dosya'])}" download>⬇ {e(d['dosya'])} ({boyut_yaz(d['boyut'])})</a>
            <a class="buton kucuk-buton" href="{e(d['pdf'])}" download>⬇ PDF ({boyut_yaz(d['pdf_boyut'])})</a>
          </p>
          <p class="telif" data-i18n="arch.copyright"></p>
        </div>
      </section>
      <section class="kutu">
        <div class="kutu-ic">
{chr(10).join(slaytlar)}
        </div>
      </section>
    </main>
  </div>'''
    yol = [('<span data-i18n="nav.home"></span>', '/', ''), ('<span data-i18n="nav.archive"></span>', '/arsiv/', ''),
           (f'{d["sinif"]}. <span data-i18n="arch.yearSuffix"></span>', '/arsiv/#sinif-' + str(d['sinif']), ''),
           (e(d['ders'].split(' ')[0]), '', ''), (e(d['dosya']), '', ' aria-current="page"')]
    return kabuk(d['baslik'], 'arsiv', yol, govde)


def arsiv_dizini(kayitlar):
    e = html.escape
    satirlar = []
    for sinif in sorted({k['sinif'] for k in kayitlar}):
        satirlar.append(f'<tr class="sinif-satir" id="sinif-{sinif}"><td colspan="4">{sinif}. <span data-i18n="arch.yearSuffix"></span></td></tr>')
        for k in sorted((k for k in kayitlar if k['sinif'] == sinif), key=lambda k: (k['ders'], k['slug'])):
            satirlar.append(f'''<tr><td><span class="mini-ikon ppt" aria-hidden="true"></span><a href="/arsiv/{k['slug']}/">{e(k['baslik'])}</a></td>
              <td>{e(k['ders'])}</td><td class="gizle-mobil">{'.'.join(reversed(k['tarih'].split('-')))}</td><td class="gizle-mobil">{boyut_yaz(k['boyut'])}</td></tr>''')
    govde = f'''  <div class="kolonlar iki" id="ust">
    <aside class="sol">
      <section class="kutu">
        <h2 class="mavi" data-i18n="arch.about"></h2>
        <div class="kutu-ic"><p class="kucuk" data-i18n="arch.aboutText"></p></div>
      </section>
      <section class="kutu">
        <h2 class="yesil" data-i18n="arch.stats"></h2>
        <dl class="bilgiler">
          <dt data-i18n="arch.files"></dt><dd>{len(kayitlar)}</dd>
          <dt data-i18n="arch.lastAdded"></dt><dd>{e(kayitlar[-1]['baslik']) if kayitlar else '–'}</dd>
        </dl>
      </section>
    </aside>
    <main class="orta">
      <section class="kutu">
        <h2 class="mavi" data-i18n="arch.title"></h2>
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
    yol = [('<span data-i18n="nav.home"></span>', '/', ''), ('<span data-i18n="nav.archive"></span>', '', ' aria-current="page"')]
    return kabuk('Başkent Üniversitesi Arşivi', 'arsiv', yol, govde)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('kaynak', type=Path)
    ap.add_argument('slug')
    ap.add_argument('--ders', required=True)
    ap.add_argument('--sinif', type=int, required=True)
    ap.add_argument('--tarih', required=True, help='YYYY-AA-GG')
    ap.add_argument('--baslik')
    a = ap.parse_args()

    hedef = ARSIV / a.slug
    hedef.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as g:
        g = Path(g)
        pdf, pptx = donustur(a.kaynak.resolve(), g)
        for eski in hedef.glob('s-*.jpg'):
            eski.unlink()
        calistir('pdftoppm', '-r', '144', '-jpeg', '-jpegopt', 'quality=78,optimize=y', str(pdf), str(hedef / 's'))
        metinler = slayt_metinleri(pptx, pdf)
        shutil.copyfile(a.kaynak, hedef / a.kaynak.name)
        shutil.copyfile(pdf, hedef / pdf.name)

    # pdftoppm sayfa sayısına göre 1, 01 ya da 001 diye adlandırır; iki haneye sabitle
    for f in hedef.glob('s-*.jpg'):
        f.rename(hedef / f's-{int(f.stem[2:]):02d}.jpg')

    kayit = {
        'slug': a.slug, 'baslik': a.baslik or a.kaynak.stem, 'ders': a.ders, 'sinif': a.sinif, 'tarih': a.tarih,
        'dosya': a.kaynak.name, 'boyut': a.kaynak.stat().st_size, 'pdf': pdf.name,
        'pdf_boyut': (hedef / pdf.name).stat().st_size, 'bicim': 'PowerPoint (.' + a.kaynak.suffix.lstrip('.') + ')',
        'slayt': len(metinler),
    }
    (hedef / 'index.html').write_text(sunum_sayfasi(kayit, metinler), encoding='utf-8')

    kayit_dosyasi = ARSIV / 'arsiv.json'
    kayitlar = json.loads(kayit_dosyasi.read_text(encoding='utf-8')) if kayit_dosyasi.exists() else []
    kayitlar = [k for k in kayitlar if k['slug'] != a.slug] + [kayit]
    kayit_dosyasi.write_text(json.dumps(kayitlar, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ARSIV / 'index.html').write_text(arsiv_dizini(kayitlar), encoding='utf-8')
    print(f'{len(metinler)} slayt → arsiv/{a.slug}/')


if __name__ == '__main__':
    main()
