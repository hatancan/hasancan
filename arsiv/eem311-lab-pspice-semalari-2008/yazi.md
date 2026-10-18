---
baslik: EEM311 Elektronik II: 2008 Laboratuvarının PSpice Şemaları ve Direnç Değerleri Tablosu
ozet: MOSFET, JFET–BJT, akım aynası, aktif yük, fark yükselteci ve frekans cevabı deneylerinin on OrCAD Capture şeması; laboratuvarda kullanılan standart direnç listesi.
---

Bu yazı, Başkent Üniversitesi **EEM311 Elektronik II** laboratuvarının 2008 döneminden arkadaşların hazırladığı **on OrCAD Capture/PSpice devre şemasını** bir araya getiriyor. Kişisel kullanıcı yolları temizlendi. Yanlarına, deney klasöründe dağıtılan 7 Eylül 2005 tarihli **Standard Resistor Values** tablosu eklendi; PDF'nin yazar üstverisi kaldırıldı. Dosyalar yazının sonunda ZIP olarak indirilebilir.

Ön çalışma ve rapor metinleri daha önce [Deney 1–4](/arsiv/eem311-lab-raporlari-2008-deney-1-4/) ve [Deney 5–8](/arsiv/eem311-lab-raporlari-2008-deney-5-8/) yazılarında aktarıldı. Bu pakette o yazılara eklenmemiş düzenlenebilir şema kaynakları bulunuyor.

## Deney 3: Ortak kaynaklı MOSFET

`deney3/O.C.DSN`, CD4007 modelinden `nnMOS` kullanılan ortak kaynaklı yükselteç. Dosyada 15 V besleme, 178 kΩ dren direnci, 50 mV ve 1 kHz sinüs kaynağı, 10 µF baypas kondansatörü kayıtlı.

Şemaya kaydedilmiş çalışma noktası değerleri: I_D = 74,01 µA, V_G = 3,409 V, V_D = 1,826 V, V_S = 1,480 V. Direnç bölücüsü akımı 170,5 µA; kaynaktan çekilen toplam akım 244,5 µA. Bunlar dosyada saklanan eski sonuçlardır.

## Deney 4: İki katlı JFET–BJT yükselteç

Üç şema var:

- `deney4/on-calisma/BIAS.DSN`: DC çalışma noktası devresi.
- `deney4/on-calisma/O.C.4.DSN`: kuplaj ve baypas kondansatörleriyle geçici analiz devresi.
- `deney4/rapor/O.C.4.DSN`: rapor için saklanan sürüm; dosyada 70 mV giriş ayarı da bulunuyor.

JFET **J2N4860**, BJT **Q2N3904**. Besleme 12 V, yük 100 kΩ, emetör direnci 2,2 kΩ. Şema kayıtlarında 0,1 mV ve 1 kHz giriş ayarı; 10 µF, 22 µF ve 100 µF kondansatörler yer alıyor.

Kaydedilmiş DC değerler: I_D = 6,135 mA, I_C = 2,842 mA, I_B = 18,55 µA; V_D = 5,865 V, V_S = 2,024 V, V_B = 6,985 V, V_E = 6,292 V, V_C = 9,158 V.

## Deney 5: MOSFET akım aynası

`deney5/ONCALISMA.DSN`, CD4007 MOSFET modelleriyle kurulan akım aynası. İki 5 V kaynağı ve referans dirençli kol bulunuyor. Kaydedilmiş son değerler arasında **I_REF = 1,434 mA**, **I_OUT = 1,444 mA**, düğüm gerilimi **3,566 V** var.

Aynı dosyada daha önceki denemelerin sayısal kayıtları ve bir `NET0075` hata kaydı da kalmış. Bu nedenle içerdiği her bias değerinin tek bir son çalıştırmaya ait olduğu varsayılmamalı.

## Deney 6: Aktif yüklü CMOS yükselteç

`deney6/AAAAAAA.DSN` içinde `nnMOS` ve `ppMOS` modelleri, 15 V besleme, 10 µF kuplaj kondansatörleri, 1 MΩ ve 100 kΩ dirençler bulunuyor. Giriş ayarı 25 mV, 5 kHz. Referans direnç denemeleri arasında 20,16 kΩ ve 25,42 kΩ görülüyor.

Dosyada birden fazla denemeden kalmış bias değerleri var. Son kayıt grubunda yaklaşık 500,5 µA ve 557,4 µA kol akımları, 2,754 V ve 12,72 V düğüm gerilimleri bulunuyor. Devrenin teorisi [aktif yüklü CMOS deney föyünde](/arsiv/eem311-deney-5-6-akim-aynasi-aktif-yuk/) açıklanıyor.

## Deney 7: BJT fark yükselteci

`deney7/OC.DSN`, dört Q2N3904 transistörlü akım kaynaklı fark yükselteci. ±15 V kaynaklar, 9,7 kΩ kolektör dirençleri, 2,2 kΩ dirençler ve 4,95 kΩ referans direnci kaydedilmiş. İki giriş 1 kHz'de +50 mV ve −50 mV sinüs olarak ayarlanmış.

Çalışma noktası kayıtlarında yaklaşık 984–991 µA fark çifti akımları, 1,98 mA mertebesinde akım kaynağı kol akımları, −663,5 mV ortak emetör ve yaklaşık 5,452 V kolektör düğümü bulunuyor.

## Deney 8: Ortak emetörlü yükseltecin frekans cevabı

- `deney8/DC ANALIZ.DSN`: DC çalışma noktası.
- `deney8/ONCALISMA8.DSN`: kuplaj ve baypas kondansatörlü ön çalışma.
- `deney8/PART D.DSN`: deneyin C_E kaldırılan bölümüne ait şema.

Model Q2N3904; R₁ = 8,2 kΩ, R₂ = 3,9 kΩ, R_C = 6,3 kΩ, R_E = 3,3 kΩ, besleme 12 V. Dosyalarda 1 kHz giriş için 10 mV ve 20 mV ayarları saklanmış.

DC kayıtları: I_C = 958,1 µA, I_B = 7,078 µA, I_E = 965,2 µA; V_B = 3,849 V, V_E = 3,185 V, V_C = 5,964 V. Bunlardan V_CE = **2,779 V**.

## Laboratuvarın direnç değerleri tablosu

**Standard Resistor Values**, 07.09.2005 revizyonlu tek sayfalık liste. Altında Başkent Üniversitesi'ndeki `~kocaturk` ve `~hhatip` ders sayfalarının adresleri yazıyor. İçerdiği değerler:

| Aralık | Belgede listelenen dirençler |
| --- | --- |
| 1 Ω altı | 0,68 Ω |
| 1–100 Ω | 1,6; 2,2; 2,7; 3; 3,6; 3,9; 4,7; 7,6; 8,2; 10; 15; 20; 25; 27; 33; 43; 47; 51; 56; 68; 75; 91; 100 Ω |
| 100 Ω–1 kΩ arası | 120; 150; 180; 220; 270; 330; 390; 430; 470; 560; 620; 680; 820; 910 Ω |
| 1–10 kΩ | 1; 1,2; 1,5; 1,8; 2,2; 2,7; 3; 3,3; 3,6; 3,9; 4,7; 5,1; 5,6; 6,2; 6,8; 7,5; 8,2; 10 kΩ |
| 10–100 kΩ arası | 12; 15; 18; 20; 22; 27; 30; 33; 39; 47; 56; 62; 68; 75; 82 kΩ |
| 100 kΩ ve üstü | 100; 120; 150; 180; 220; 270; 300 kΩ |

*Not: Belgedeki 7,6 Ω, 25 Ω ve diğer sıra dışı değerler aynen korundu. Bu listeyi eksiksiz bir E-serisi standardı olarak değerlendirmemek gerekir.*

## Şema dosyaları hakkında

`.DSN` dosyaları OrCAD Capture şemalarıdır; Proteus'un aynı uzantıyı kullanan şemalarıyla aynı biçimde değildir. Eski model/kütüphane yolları ve simülasyon kayıtları içerirler. CD4007 ve JFET modellerinin dosyada işaret edilen yerlerde bulunması gerekir; paket kendi başına bütün kütüphaneleri içermiyor.

Dosyalar burada çalıştırılmadı; yazıdaki sayılar kaydedilmiş şema özellikleri ve dönemin raporlarından aktarılmıştır. İndirme paketinde on şema ve bir direnç tablosu PDF'i vardır.
