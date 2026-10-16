---
baslik: EEM211 Sayısal Mantık Tasarımı: D Flip-Floplu 3 Bitlik Gray Kod Sayacı (2012 Dönem Projesi)
ozet: EEM211 Sayısal Mantık Tasarımı 2012 dönem projelerinden 3 bitlik Gray kod sayacının D flip-floplarla tasarımı: doğruluk tablosu, 000-001-011-010-110-111-101-100 durum diyagramı, Karnaugh haritalarından D1 = BC' + AB + AC, D2 = A'C + BC', D3 = A'B' + AB ve devre şeması.
---

Bu yazı, EEM211 Sayısal Mantık Tasarımı dersinin 2012 güz dönemi projelerinden "3 bitlik Gray kod sayacı tasarlayınız (D flip-flop)" konusuna ait iki sayfalık bir proje çalışmasının, 28 Aralık 2012'de telefonla çekilmiş fotoğraflarından metne aktarılmış hâlidir (proje konusu arşivdeki *Dönem Projesi Konuları* yazısında 8. sırada). Fotoğraflanmış sayfalardan metne aktarıldı; fotoğrafların kendisi yayınlanmadı.

## Doğruluk tablosu

D flip-flopun karakteristik denklemi Q(t+1) = D olduğundan, 3 bitlik Gray kod sayacının doğruluk tablosu şöyledir (A en anlamlı bit):

| A(t) B(t) C(t) | A(t+1) B(t+1) C(t+1) | D1 | D2 | D3 |
|---|---|---|---|---|
| 000 | 001 | 0 | 0 | 1 |
| 001 | 011 | 0 | 1 | 1 |
| 011 | 010 | 0 | 1 | 0 |
| 010 | 110 | 1 | 1 | 0 |
| 110 | 111 | 1 | 1 | 1 |
| 111 | 101 | 1 | 0 | 1 |
| 101 | 100 | 1 | 0 | 0 |
| 100 | 000 | 0 | 0 | 0 |

## Durum diyagramı

Sayaç sekiz durumu bir halka hâlinde dolaşır; her adımda yalnızca bir bit değişir:

000 → 001 → 011 → 010 → 110 → 111 → 101 → 100 → 000

## Karnaugh haritaları ve D girişleri

| | BC = 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| D1, A = 0 | 0 | 0 | 0 | 1 |
| D1, A = 1 | 0 | 1 | 1 | 1 |
| D2, A = 0 | 0 | 1 | 1 | 1 |
| D2, A = 1 | 0 | 0 | 0 | 1 |
| D3, A = 0 | 1 | 1 | 0 | 0 |
| D3, A = 1 | 0 | 0 | 1 | 1 |

- **D1 = BC' + AB + AC = B(C' + A) + AC**
- **D2 = A'C + BC'**
- **D3 = A'B' + AB**

*Not: Üç ifade doğruluk tablosunun sekiz satırı için tek tek kontrol edildi; hepsi doğru sonraki durumu veriyor.*

## Devre

İkinci sayfadaki şemada üç D flip-flop (A, B, C) ortak bir saat sinyaliyle sürülüyor; D girişleri yukarıdaki ifadeleri gerçekleştiren AND, OR ve tümleyici kapılarıyla üretiliyor. Flip-flop çıkışları Q2, Q1, Q0 olarak birer direnç üzerinden üç LED'e bağlanmış; LED'lerde Gray kod sırası izleniyor.
