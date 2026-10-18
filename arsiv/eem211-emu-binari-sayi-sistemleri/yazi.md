---
baslik: EEM211 Sayısal Mantık Tasarımı: Binari Sayı Sistemleri ve Mantık Devreleri (DAÜ Web Notu)
ozet: Sayısal dalga şekilleri, taban dönüşümleri, kapılar, Karnaugh haritaları ve on iki laboratuvar uygulaması.
---

Doğu Akdeniz Üniversitesi `sct.emu.edu.tr/ilkan/ex/kitap134.htm` adresinden kaydedilmiş “Binari Sayı Sistemleri” ders metni. Sayfada açık bir yazar ve yayın tarihi bulunmuyor; dosyanın 25 Aralık 2006 arşiv tarihi kullanıldı. Kuramsal notlar, çözümlü örnekler, on iki deney ve çalışma soruları içerir. Görselsiz HTML metni yazının sonunda indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Sayısal sinyaller ve zaman ölçüleri

İkili sistemde 0 ve 1 kullanılır. Kaynak bu seviyeleri örnek devrelerinde 0 V ve 5 V ile gösterir. Yükselme zamanı darbenin %10 ile %90, alçalma zamanı %90 ile %10 seviyeleri arasındaki süredir. Darbe genişliği iki kenarın %50 noktaları arasında ölçülür.

Periyot T, frekans f=1/T ve görev oranı DC=tw/T kavramları örneklenir. T=10 ms olan sinyalin frekansı 100 Hz'dir; tw=1 ms ise görev oranı %10 olur. 10 kHz'lik bir saat 100 ms içinde 1000 darbe üretir.

## Seri ve paralel veri aktarımı

Seri aktarımda bitler bir hat üzerinden sırayla, paralel aktarımda ayrı hatlardan birlikte gönderilir. Kaynağın 100 kHz örneğinde bir bit zamanı 0,01 ms; sekiz bitin seri aktarımı 0,08 ms olarak verilir.

*Not: Aynı örneğin paralel aktarım satırında “0.01ms = 10ms” yazıyor. Doğru dönüşüm 0,01 ms = 10 µs'dir.*

## Sayı sistemleri ve dönüşümler

İkili sayıların basamak ağırlıkları 1, 2, 4, 8… şeklindedir. Onaltılık sistem 0–9 ve A–F karakterlerini kullanır. Dört bit bir onaltılık basamağa karşılık gelir.

| Kaynaktaki dönüşüm | Sonuç |
| --- | --- |
| 77 (onluk) | 1001101 (ikili) |
| 0010 0111 (ikili) | 27 (onaltılık), 39 (onluk) |
| 1C (onaltılık) | 28 (onluk) |
| 650 (onluk) | 28A (onaltılık) |

Bu örneklerin sonuçları yeniden hesaplanarak doğrulandı. İkili toplamada 1+1=10, yani toplam biti 0 ve elde 1 olur.

## Mantık kapıları ve örnek tasarımlar

NOT, AND, NAND, OR, NOR, XOR ve XNOR kapılarının sembolleri ve doğruluk tabloları verilir. n girişin 2ⁿ farklı birleşimi vardır. XOR iki giriş farklı olduğunda 1, XNOR aynı olduğunda 1 üretir.

Uygulama sorularında iki su deposunun doluluk bilgisi, uçağın iniş takımı algılayıcıları ve iki dört bitlik sayının eşitlik kontrolü kullanılır. Sensör çıkışlarının hangi fiziksel durumu 1 ile temsil ettiği her tasarımda ayrıca tanımlanır.

## Boolean cebri ve standart ifadeler

Değişme, birleşme, dağılma ve De Morgan kuralları devre sadeleştirmeye uygulanır. Çarpımların toplamı SOP, toplamların çarpımı POS biçimidir. Standart terimde her değişkenin kendisi veya tümleyeni bulunur.

Harita yönteminde 2, 3 ve 4 değişken için sırasıyla 4, 8 ve 16 hücre kullanılır. Birler ikinin kuvveti büyüklüğünde komşu gruplara ayrılır; grupta değişmeyen değişkenler sonuç terimini verir. Karşı kenarların komşuluğu ve aynı hücrenin birden çok grupta kullanılabilmesi açıklanır.

## Kombinezonsal devreler

Fonksiyondan devreye, doğruluk tablosundan fonksiyona ve verilmiş devreden daha küçük bir gerçekleştirmeye geçiş örneklenir. NAND ve NOR kapılarının evrenselliği, yalnız tek kapı türü kullanarak tasarım yapılmasıyla gösterilir.

Yarım toplayıcı iki girişten toplam ve elde üretir. Tam toplayıcı bir önceki basamaktan gelen eldeyi de alır. Karşılaştırıcı, kodlayıcı, kod çözücü ve yedi parçalı gösterge sürücüsü başlıkları daha büyük işlev bloklarına geçiş sağlar. Son kuramsal kısım flip-flop, sayıcı ve kaydırmalı yazmaç kavramlarına giriş yapar.

## Laboratuvar uygulamaları

| Deney | İçerik |
| --- | --- |
| 1 | Tümdevre bağlantıları; 7404, 7408, 7432 |
| 2 | 7404 ile NOT kapısı |
| 3 | 7408 ile AND kapısı |
| 4 | 7432 ile OR kapısı |
| 5 | 7486 ile XOR kapısı |
| 6 | Dört bitlik sayıların XOR ile karşılaştırılması |
| 7 | Birleşimsel mantık devrelerinin çıkış tabloları |
| 8 | NAND ile NOT, AND ve OR elde edilmesi |
| 9 | NOR ile NOT, AND ve OR elde edilmesi |
| 10 | 7408 ve 7486 ile yarım toplayıcı |
| 11 | 7483 ile dört bitlik toplama |
| 12 | 7447 ve ortak anotlu yedi parçalı gösterge |

Her uygulamada amaç, kısa bilgi, araç gereç listesi, bağlantı şekli ve doldurulacak tablo bulunur. Son çalışma soruları sayı tabanları, dalga şekilleri, kapı hataları, sadeleştirme, Karnaugh haritaları ve gösterge tasarımını birleştirir.

*Not: Kaydedilmiş sayfanın bazı formülleri ve üst çizgileri gömülü görsellerle verilmiş. Düz metin çıkarımında bu işaretler kaybolduğu için belirsiz cebirsel örnekler burada yeniden kurulmadı. Kaynağın NOR deneyindeki bir alt açıklama da “NAND” sözcüğünü kullanıyor; bölüm bağlamı NOR uygulamasıdır.*
