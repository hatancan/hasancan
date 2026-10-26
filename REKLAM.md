# Reklam alanları

Sitedeki reklam alanları boş yer tutucu olarak açıldı; içerikleri (FreshSignal reklamları) ayrı bir
oturumda yerleştirilecek. Bu dosya o iş için başvuru kaynağıdır. Tasarım çerçevesi için önce `DESIGN.md`'yi oku.

## Alanlar

| `data-reklam` | Ölçü (masaüstü) | Telefon (≤640px) | Nerede | Kaynağı |
|---|---|---|---|---|
| `ust-banner` | 728×90 | 320×100 | Tüm sayfalar: menü/şeridin (alt sayfalarda yol çubuğunun) altında | `index.html` (alt sayfalar `tools/sunum.py` ile buradan kopyalar) |
| `sag-kare` | 200×200 | 200×200 | Ana sayfa, sağ sütunun başı (sayaçtan sonra) | `index.html` |
| `sol-dikey` | 160×600 | gizli | Ders Notlarım dizini ve her yazı sayfası, sol sütunun sonu | `tools/sunum.py` → `reklam('sol-dikey', '160x600')` |
| `yazi-sonu` | 468×60 | 320×100 | Her yazı sayfası, yazının sonunda, indirme kutusundan önce | `tools/sunum.py` → `reklam('yazi-sonu', '468x60')` |

Her alanın yapısı:

```html
<aside class="reklam reklam-728x90 yer-tutucu" data-reklam="ust-banner" data-i18n-attr="aria-label:ad.label">
  <span class="reklam-etiket" data-i18n="ad.label"></span>          <!-- "Reklam / Advertisement / Anzeige" -->
  <div class="reklam-yer">[<span data-i18n="ad.slot"></span> · 728×90]</div>
</aside>
```

## Doldururken

- Reklam kodu `.reklam-yer` kutusunun **içine** konur; yer tutucu metni (`[…]`) silinir ve `aside`'dan
  `yer-tutucu` sınıfı kaldırılır. "Reklam" etiketi kalır.
- `.reklam-yer` ölçüsü CSS'te sabittir (`assets/css/style.css`, "Reklam alanları" bölümü) ve kaymayı (CLS) önler;
  farklı ölçüde reklam gerekirse oradaki sınıfları güncelle.
- **Ana sayfa:** `index.html`'i doğrudan düzenle.
- **Arşiv sayfaları (540+ sayfa) elle düzenlenmez.** `ust-banner` `index.html`'den otomatik kopyalanır;
  `sol-dikey` ve `yazi-sonu` için `tools/sunum.py` içindeki `reklam()` fonksiyonunu güncelle. Sonra bütün sayfaları
  yeniden üret:
  `for s in $(python3 -I -c "import json;print(' '.join(k['slug'] for k in json.load(open('arsiv/arsiv.json'))))"); do python3 -I tools/sunum.py sayfa $s; done`
- Harici betik eklenirse alt sayfaların `<head>`'i `tools/sunum.py` → `kabuk()` içinde üretilir.
- Metin eklenirse üç dile birden ekle (`assets/lang/{tr,en,de}.js`).
- Yayına alma: `./deploy.sh` (Caddy, `/var/www/hasancan`). Değişen stil/betik için sayfalardaki `?v=` sürümünü yenile.
