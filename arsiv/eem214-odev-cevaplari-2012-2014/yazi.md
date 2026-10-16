---
baslik: EEM214 Elektronik I: Ödev Cevapları (2012–2014), Diyot Türleri, Datasheet Raporları, Direnç ve Kondansatör Çeşitleri
ozet: EEM214 Elektronik I dersinin 2012, 2013 ve 2014 ödevlerine öğrencilerin hazırladığı cevaplar: tünel, varikap, Schottky, foto ve LED diyot; 1N4148/1N4448, MJE521, 2N3055, 2N6660, VN2222L ve BAR17 datasheet raporları; direnç renk kodları ve kondansatör çeşitleri.
---

Bu yazı, Başkent Üniversitesi **EEM214 Elektronik I** dersinde 2012, 2013 ve 2014 bahar dönemlerinde verilen ödevlere öğrencilerin hazırladığı cevapları bir araya getiriyor. Hepsi arkadaşların çalışması; ad ve öğrenci numaraları çıkarıldı (2013 ödevlerinin dosya adlarındaki numara da kaldırıldı). Ödev metinlerinin 2013 sürümü arşivde [EEM214 Ödevler (2013)](/arsiv/eem214-odevler-2013/) yazısında bulunuyor; 2012 ödev listesi neredeyse aynı (Ödev 2–4, veriliş 12.04.2012, dönüş 11.05.2012) ve ZIP'e eklendi. Kişisel bilgileri kapatılmış PDF'ler yazının sonunda ZIP olarak indirilebilir.

## 2012 ve 2013: Ödev 1 – Diyot türleri

İki öğrencinin cevabı, istenen beş diyot türünü yapı, çalışma prensibi, karakteristik ve kullanım alanı başlıklarıyla anlatıyor:

- **Tünel diyot:** Saf silisyum ve germanyuma fazla katkı maddesi katılarak yapılır; P-N birleşim yüzeyi çok incedir. Karakteristiğinde gerilim belli bir değere kadar artarken akım da artar, sonra akım düşer (negatif direnç bölgesi, eğimi −1/R) ve tekrar yükselir. Bu negatif direnç sayesinde yükselteç, MHz mertebesinde osilatör (rezonans devresinin direnci negatif dirençten, örneğin 80 Ω'dan küçük olmalı) ve multivibratör, flip-flop gibi devrelerde anahtar olarak kullanılır; 10 000 MHz'e kadar çalışabilir.
- **Varikap diyot:** Ters polarmada çalışır; ters gerilim arttıkça nötr (boşaltılmış) bölge genişler ve kapasite düşer. Pahalı, büyük ve elle ayarlanan değişken kondansatörlerin yerini alır; TV ve FM alıcılarında otomatik frekans kontrolü, frekans modülatörleri ve frekans çoğaltıcılarda kullanılır.
- **Schottky diyot:** Çok yüksek frekanslarda iletim ve kesim arasında hızla geçebilen diyot; mikrodalga alıcılarında karıştırıcı, modülatör, demodülatör ve dedektör olarak kullanılır.
- **Fotodiyot:** Ters polarmada kullanılır; birleşim yüzeyine ışık düşene kadar yalıtkandır, ışık düşünce elektron–delik çiftleri oluşur ve akım (yaklaşık 20 µA) geçer. Uzaktan kumanda alıcıları, alarm ve sayma devreleri, yangın ihbar sistemlerinde kullanılır.
- **LED:** GaAs, GaAsP, GaP katkılı P-N diyottur; doğru polarmada birleşim yüzeyinde elektron ve deliklerin birleşmesiyle açığa çıkan enerji ışık olarak yayılır. Dijital göstergeler, işaret lambaları ve optokuplörlerde kullanılır.

*Not: Cevaplarda tünel diyotun "ters polarma altında çalıştığı" ve Schottky diyotun "P-N birleşim yüzeyinin platinle kaplanmasıyla" yapıldığı yazılmış. Tünel diyotun negatif direnç bölgesi ileri yöndedir; Schottky diyot ise P-N eklemi değil metal–yarıiletken (metal–n) eklemidir, bu yüzden ileri gerilim düşümü küçük (yaklaşık 0.2–0.3 V) ve anahtarlama hızı yüksektir.*

## 2012 ve 2013: Datasheet raporları (Ödev 2–4)

Bu ödevlerde öğrenciler seçtikleri bir diyot, bir BJT ve bir FET/MOSFET'in datasheet'ini bölüm bölüm (üretici bilgisi, kılıf ve pin yapısı, mutlak maksimum değerler, ısıl özellikler, elektriksel karakteristikler, tipik karakteristik eğrileri, kılıf ölçüleri) inceleyip yorumlamış; raporlarda datasheet'ten alınmış kesitler de var.

**2013 raporları:**

- **Diyot – 1N/FDLL 914, 916, 4148, 4448 (Fairchild):** yüksek iletkenlikli hızlı diyot; FDLL tipinin renk bantları, maksimum değerler (T_A = 25 °C), ısıl karakteristikler, ileri gerilim–akım, ters akım, kapasite ve ters toparlanma süresi eğrileri.
- **BJT – MJE521 (Motorola):** plastik kılıflı orta güç NPN silisyum transistör, 4 A, 40 V, 40 W; genel amaçlı yükselteç ve anahtarlama, özellikle tamamlayıcı simetri ile 5–10 W ses yükselteçleri için önerilmiş, PNP eşi MJE371; güvenli çalışma bölgesi ve DC akım kazancı eğrileri.
- **MOSFET – 2N6660 ve VQ1004J/P (Vishay Siliconix):** tekli ve dörtlü N kanallı, 60 V MOSFET; V(BR)DSS, r_DS(on), V_GS(th) özet tablosu, çıkış ve transfer karakteristikleri, sıcaklıkla r_DS(on) değişimi, kapasiteler ve geçici ısıl empedans.

**2012 raporu:**

- **BJT – 2N3055 (NPN güç transistörü):** DC akım kazancı β 20–70; V_CE(sat) = 1.1 V (I_C = 4 A, I_B = 400 mA); V_CEO(sus) en az 60 V (I_C = 200 mA), V_CER(sus) en az 70 V (R_BE = 100 Ω); I_CEO en fazla 0.7 mA (V_CE = 30 V); I_CEX en fazla 1.0 mA (T_C = 150 °C'de 5 mA); I_EBO en fazla 5 mA (V_BE = 7 V); h_FE'nin akım ve sıcaklıkla değişimi.
- **MOSFET – VN2222L (N kanallı):** gövde ve terminaller, mutlak maksimum değerler, savak–kaynak kırılma gerilimi (en az 60 V), eşik gerilimi (0.6–2.5 V), sıfır kapı gerilimli savak akımı, açık durum direnci (r_DS(on) en fazla 7.5 Ω), ileri geçiş iletkenliği, giriş ve çıkış kapasiteleri ve tipik eğriler.
- **PIN diyot – BAR17:** silisyum PIN diyot; depolama ve çalışma sıcaklıkları, güç harcaması, ters gerilim, ileri akım, ters akım, diyot kapasitesi, ileri direncin akımla ve kapasitenin ters gerilimle değişimi eğrileri.

## 2014: Diyot türleri, dirençler ve kondansatörler

2014 bahar döneminde 25.04.2014'te verilen ve final sınavında sorulacağı belirtilen ödevler üç başlıktı: diyot çeşitleri (tünel, varikap, Schottky, foto, LED), direnç çeşitleri ve renk kodları (karbon, taş, film, entegre, SMD, ayarlı ve değişken dirençler; 3, 4 ve 5 renkli dirençlerin okunması) ve kondansatör çeşitleri (yalıtkanına ve kapasite değerine göre). Cevap dosyasında:

- **Direnç renk kodu:** ilk iki bant değerin ilk iki rakamını, üçüncü bant eklenecek sıfır sayısını (çarpanı), dördüncü bant toleransı verir. Ezber için "SoKaKTa SaYaMaM GiBi Ama Görürüm" (siyah, kahverengi, kırmızı, turuncu, sarı, yeşil, mavi, mor, gri, beyaz, altın, gümüş). Örnekler: kırmızı–sarı–mavi–gümüş = 24 MΩ ± %10; sarı–mor–kahverengi–altın = 470 Ω ± %5; mavi–gri–siyah–altın = 68 Ω ± %5.
- **Yalıtkanına göre kondansatörler:** vakumlu (10–1000 pF, 10 000 V'a kadar, radyo vericileri), havalı (ayarlanabilir, RF ayarı), plastik film (polikarbonat, polyester, polipropilen; sinyal ve filtre devreleri), mikalı (50 pF – 20 nF, yüksek gerilim ve frekans), kâğıtlı (300 pF – 4 µF, artık neredeyse kullanılmıyor), camlı (kararlı, pahalı), seramik (kuplaj ve filtreleme, yüksek frekans), alüminyum elektrolitik (kutuplu, yüksek frekansta zayıf), tantal elektrolitik, OS-CON, süper kondansatör (karbon aerojel) ve "gimmick" kondansatör (birbirine dolanmış iki tel).
- **Kapasite değerine göre:** sabit kondansatörler ve ayarlanabilir kondansatörler (varyabl, trimer, varaktör).

*Not: Cevap dosyasında kırmızı–kırmızı–turuncu–altın için "22 kΩ ± %7" yazılmış; altın bant ± %5 toleransı gösterir.*

Ayrıca 2009 tarihli kısa bir Türkçe not dosyası da var: P ve N tipi yarıiletkenler (katkıyla değerlik bandının yukarı ya da iletkenlik bandının aşağı çekilmesi), iletken–yarıiletken–yalıtkan ayrımı, elektrik akımı ve akım yönü kabulü, katılarda serbest elektronlar.

## İndirme

ZIP dosyası yıllara göre klasörlenmiş ödev cevaplarının kişisel bilgileri kapatılmış PDF kopyalarını ve 2012 ödev listesinin Word dosyasını içeriyor.
