---
baslik: EEM211 Sayısal Mantık Tasarımı: BME 231 Digital Design Ders Sunuları (Mehmet Yüksekkaya, 2006)
ozet: Başkent Üniversitesi Biyomedikal Mühendisliği BME 231 Digital Design dersinin 2006 güz dönemi haftalık sunuları: sayı sistemleri, işaretli sayılar ve kodlar, Boole cebri, Karnaugh haritası, kod çözücü ve kodlayıcılar, ardışıl devreler, yazmaç ve sayıcılar, ROM, PAL, PLA, RAM, ADC-DAC ve bir fonksiyonun yedi farklı yolla tasarımı.
---

Bu yazı, Başkent Üniversitesi Biyomedikal Mühendisliği Bölümü'nün **BME 231 Digital Design** dersinde, öğretim görevlisi **Mehmet Yüksekkaya**'nın 2006 güz döneminde kullandığı haftalık sunuları tanıtıyor; aynı dersin, biri İ. Cengiz Koçum'un adını taşıyan, sonraki bir döneme ait iki Türkçeleştirilmiş sunusu da (MSI ve PLD elemanları; senkron ardışıl mantık) dosyalar arasında. Ders kitabı M. Morris Mano'nun *Digital Design* (3. baskı, Prentice Hall, 2002) kitabı; sunulardaki şekillerin çoğu bu kitaptan. Her sununun konuları aşağıda özetlendi; on üç PowerPoint dosyası yazının sonunda ZIP olarak indirilebilir.

## Ders bilgileri

| | |
|---|---|
| Ders saati | Çarşamba 14:00–15:50 |
| Ders kitabı | Digital Design, 3. baskı, M. Morris Mano, Prentice Hall, 2002 |
| Devam + quiz + ödevler | %20 |
| Laboratuvar (ön çalışma + lab quizi + rapor) | %20 |
| Ara sınav | %25 |
| Final | %35 |

## Haftalık sunular

1. **Hafta 1 – Ders tanıtımı ve sayı sistemleri:** ders içeriği, tanımlar, sayısal devreler, başarı için öneriler; tabanlar arası dönüşümler (ikili, sekizli, onaltılı ve onluk arasında tüm yönler) ve alıştırmalar.
1. **Hafta 2 – İşaretli sayılar, kodlar ve Boole cebrine giriş:** işaretsiz ve işaretli sayılar, 2'ye tümleyen gösterimi ve tamsayı aralıkları, BCD, Gray ve ASCII kodları, AND ve OR kapıları, Boole cebri aksiyomları.
1. **Hafta 3 – Boole fonksiyonları ve sadeleştirme:** temel teoremler, De Morgan teoremleri, dualite, fonksiyonların tümleyeni, NAND ve NOR ile diğer kapıların kurulması, XOR ve XNOR, minterm-maksterm ve kanonik biçimler, doğruluk tablosundan ifadeye geçiş, Boole kurallarıyla sadeleştirme.
1. **Hafta 4 – Karnaugh haritalarıyla sadeleştirme.**
1. **Hafta 5 – Kapı düzeyinde sadeleştirme ve kombinezonsal devreler:** keyfi (don't care) durumlarla harita sadeleştirme, NAND-NAND ve NOR-NOR gerçekleştirme, kod çevirici ve tam çıkarıcı tasarımı.
1. **Hafta 6 – Kod çözücü ve kodlayıcılar:** 2'ye 4 ve 3'e 8 kod çözücüler, kod çözücüyle fonksiyon gerçekleştirme, iki 3'e 8'den 4'e 16 kod çözücü, 8'e 3 kodlayıcı, toplayıcı-çıkarıcı devresi, kod çevirme.
1. **Hafta 10 – Senkron ardışıl mantık, yazmaçlar ve sayıcılar:** S-R ve D mandalları, kenar tetiklemeli D, J-K ve T flip-floplar, asenkron girişler, çıkış ve durum denklemleri, durum tablosu ve diyagramı, tasarım örnekleri (ör. 00, 11, … sırasında sayan sayıcı, 0–10 arası sayan 4 bitlik sayıcı), paralel yüklemeli yazmaç, kaydırmalı yazmaçlar, seri aktarım, evrensel kaydırmalı yazmaç, senkron ve asenkron (ripple) sayıcılar. Sununun sonunda dönem projesinin tanımı var: dijital tümleşik devrelerin özel karakteristiklerini (çıkış yelpazesi, güç harcaması, yayılma gecikmesi, gürültü payı vb.) anlatan ve her öğrencinin seçtiği bir entegreyi veri sayfasından inceleyen bir rapor; son teslim 27 Aralık Çarşamba, geciken her gün için %25 kesinti.
1. **Hafta 13 – ROM ve programlanabilir mantık:** ROM iç yapısı ve bellek dizisi, ROM ile fonksiyon gerçekleştirme, PAL ve PLA.
1. **Hafta 14 – RAM:** RAM arayüz sinyalleri, boyut, okuma ve yazma işlemleri, RAM'in iç yapısı, bellek hiyerarşisi, ROM ile kare tablo (square lookup table), PLA ve PAL tasarım örnekleri.
1. **Hafta 14 – ADC ve DAC:** analog ve sayısal kavramları, analog-sayısal ve sayısal-analog dönüştürücüler, çıkış seviyeleri ve çözünürlük, örnekleme ve nicemleme.
1. **Hafta 14 – Farklı tasarım örnekleri:** verilen bir doğruluk tablosunun yedi farklı yolla tasarlanması: kapılarla, kod çözücüyle, 4x1 MUX ile, 2x1 MUX ile, PROM ile, PAL ile ve PLA ile.

## Sonraki dönemden iki Türkçe sunu

- **MSI ve PLD elemanları:** SSI, MSI, LSI, VLSI tanımları, toplayıcı-çıkarıcı devresi, kod çözücüler ve kodlayıcılar, tekilleyici (demultiplexer), öncelik kodlayıcısı, çoklayıcılar, programlanabilir mantık dizisi (PLA) ve PLA program tablosu, kod çevirme.
- **Senkron ardışıl lojik (İ. Cengiz Koçum):** NOR kapılı RS flip-flop, mandallar ve flip-floplar, asenkron girişler, durum denklemleri, tablo ve diyagramı; beş adımda ardışıl devre tasarımı, D flip-floplarla tasarım, sayıcı tasarımı, durum azaltma, durum tahsisi, kullanılmayan durumlarla tasarım, ikili olmayan dizili sayıcılar, yazmaçlar, kaydırmalı yazmaçlar ve seri toplayıcı.
