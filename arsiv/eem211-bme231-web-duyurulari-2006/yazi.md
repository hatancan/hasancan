---
baslik: EEM211 Sayısal Mantık Tasarımı: Ders Duyuruları, Proje Yönergesi ve PROM–PAL–PLA Örnekleri (Başkent, Mehmet Yüksekkaya)
ozet: 2006 BME231 dersinin çalışma konuları, proje ölçütleri ve programlanabilir mantık örneklerinin metin dökümü.
---

Başkent Üniversitesi Mehmet Yüksekkaya ders sayfasının 2006 tarihli kaydı ve 27 Aralık Çarşamba teslimli proje duyurusu. Kaynak sayfada ders kodu BME231; belgeler EEM211 klasöründe saklandığı için bu arşivde EEM211 altında yer alıyor. İki HTML metninin görselsiz kopyası yazının sonunda birlikte indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Dersin çalışma konuları

Ders sayfası 28 Eylül 2006'dan itibaren sayı sistemleri, Boolean cebri ve mantık kapıları, Boolean fonksiyonları ve sadeleştirme, Karnaugh haritaları, kapı düzeyinde sadeleştirme ve kombinezonsal devreler başlıklarını sıralar.

6 Kasım duyurusunda binary, BCD ve kaynakta “Axes-3” yazılan kod; kodlar arası dönüşüm; minterm ve maxterm gösterimleri; sıfırları gruplayarak toplamların çarpımı biçiminde Karnaugh sadeleştirmesi çalışma konusu olarak verilir.

*Not: Kaynaktaki “Axes-3” ifadesi Excess-3 kodunu anlatıyor.*

## Ödev ve quiz takvimi

| Duyuru | İçerik |
| --- | --- |
| 28 Eylül | Bir byte için verilen işaretli/işaretsiz sayı aralıklarından hareketle word için hesaplama; teslim 4 Ekim |
| 5 Ekim | İkinci ödev notlandırılmayacak; 11 Ekim quiz'inde ilgili sorular bulunacak |
| 16 Ekim | Quiz 1 çözümleri |
| 26 Ekim | Üçüncü ödev; teslim 1 Kasım |
| 4 Kasım | Üçüncü ödev çözümleri |
| 9 Kasım | Dördüncü ödev; teslim 15 Kasım |
| 17 Kasım | Dördüncü ödev ve Quiz 2 çözümleri |

İlk ödevde işaretsiz byte aralığı 0–255, işaretli byte aralığı −128–127 olarak verilir. Yalnız sonuçların değil, hesaplamaların da yazılması istenir. Kaynak word uzunluğunu bu duyuruda ayrıca tanımlamıyor.

## Dijital tümleşik devre araştırma projesi

Raporun önce dijital tümleşik devreleri ve başlıca elektriksel karakteristiklerini açıklaması istenir. Toplam maksimum çıkış, güç harcaması, zaman gecikmesi ve gürültü değerleri duyuruda örnek parametrelerdir.

İkinci kısımda seçilen bir dijital tümdevrenin işlevi ve özellikleri incelenir. Genel bölümde tanımlanan karakteristikler bu somut eleman için yorumlanır. Amaç, ihtiyaç duyulan dijital elemanı seçerken hangi özelliklere bakılması gerektiğini ve bu bilgilerin nasıl araştırılacağını öğrenmektir.

## Rapor koşulları

- Yeterli açıklama ve kaynak bilgisi bulunmalı.
- Seçilen elemanın veri sayfası temel araştırma kaynağı olarak kullanılmalı.
- Özellikleri gösteren birkaç veri sayfası sayfası rapora eklenmeli.
- Son teslim 27 Aralık 2006 Çarşamba ders saatidir.
- Duyuruda her gecikme günü için %25 puan kesintisi belirtilir.

Bunlar arşivdeki ödevin tarihsel yönergeleridir. Veri sayfaları ve ders kitabı bölümleri bu yayına eklenmedi.


## Ek çalışma: PROM, PAL ve PLA

Aynı BME231 koleksiyonundaki “BME 231 Examples — Instructor: Mehmet Yüksekkaya” başlıklı taranmış sayfa, bir arkadaşın el yazısı açıklamalarını da içeriyor. Sayfanın üzerinde tarih yok; 2006 ders koleksiyonuyla ilişkili ek çalışma olarak burada metne aktarıldı. Görüntü yayımlanmadı.

### PROM ile üç fonksiyon

Verilen fonksiyonlar F=AB+A′BC′, G=A′B′C+C′ ve H=AB′C′+ABC′+A′B′C. Üç giriş sekiz adres seçer; üç çıkış için gereken bellek düzeni 8×3 bittir.

| ABC | F | G | H |
| --- | --- | --- | --- |
| 000 | 0 | 1 | 0 |
| 001 | 0 | 1 | 1 |
| 010 | 1 | 1 | 0 |
| 011 | 0 | 0 | 0 |
| 100 | 0 | 1 | 1 |
| 101 | 0 | 0 | 0 |
| 110 | 1 | 1 | 1 |
| 111 | 1 | 0 | 0 |

A en anlamlı giriş olarak 3'ten 8'e kod çözücünün S2 ucuna, B S1'e, C S0'a bağlanır. F için 2, 6, 7; G için 0, 1, 2, 4, 6; H için 1, 4, 6 numaralı çıkışlar ilgili VEYA yoluna alınır. Tablo, fonksiyonların sekiz giriş birleşiminde hesaplanmasıyla kontrol edildi.

### Programlanabilir bölgeler

El yazısı not, PROM'da kod çözücünün sabit olduğunu, çıkış bağlantılarının programlandığını açıklar. PAL örneğinde programlanabilir VE düzlemi ve sabit VEYA bağlantıları; PLA örneğinde hem VE hem VEYA düzleminin programlanabilmesi gösterilir.

PLA çizimi üç giriş, dört çarpım terimi ve iki çıkış içerir. İşaretlenen çarpım satırları AB, AC, BC ve A′B′C′'dir. Çıkıştaki XOR kontrolü, seçilen toplamın kendisini ya da tümleyenini vermek için kullanılır: kontrol 0 iken doğrudan, 1 iken ters çıkış elde edilir.
