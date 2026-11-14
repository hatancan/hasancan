---
baslik: EEM438 Veri İletişimi: Analog Veri İletimi: ASK, FSK, PSK, QAM, AM ve FM (Gazi Üniversitesi, Suat Özdemir)
ozet: Gazi Üniversitesi’nden Suat Özdemir’in Veri İletişimi ders slaytları: sayısal-analog ve analog-analog çevirme: ASK, FSK, PSK, QAM, AM, FM ve PM.
---

Gazi Üniversitesi Bilgisayar Mühendisliği Bölümü’nden Suat Özdemir’in “Veri İletişimi / Data Communications” dersi için hazırladığı 5. bölüm (Analog veri iletimi) slaytlarıdır (slayt tarihi 21 Mart 2011; alt bilgide BM 403 Veri İletişimi yazar). EEM438 klasöründe ikinci bir hocanın ders materyali olarak saklanmıştır. Slayt metni aşağıya aktarıldı; kitaptan alınmış şekiller ve tablolar yayımlanmadı, metni olmayan slaytlar belirtildi. Orijinal PDF yazının sonunda indirilebilir.

Kapsam: sayısal-analog ve analog-analog çevirme: ASK, FSK, PSK, QAM, AM, FM ve PM.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Sayısal analog çevirme

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Sayısal analog çevirme (2)

- Sayısal datanın band pass analog sinyale çevrilmesi sayısal-analog çevirme olarak adlandırılır.
- Low pass analog sinyalin band pass analog sinyale çevrilmesi analog-analog çevirme olarak adlandırılır.
- Sayısal-analog çevirme analog sinyalin karakteristik özelliklerinden birisinin sayısal dataya göre değiştirilmesi işlemidir.

## Sayısal analog çevirme (3)

- Bir sinüs dalgası genlik (amplitude), frekans ve faz (phase) ile tanımlanır.
- Amplitude shift keying (ASK), frequency shift keying (FSK), phase shift keying(PSK) ve quadrature amplitude keying (QAM) olarak 4 modülasyon yöntemi vardır. En yaygın kullanılan QAM’dir.

## Sayısal analog çevirme (4)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Sayısal analog çevirme (5)

- Data element, en küçük bilgidir (bit). Signal element, en küçük sabit sinyaldir.
- Carrier signal (taşıyıcı sinyal), gönderen cihaz tarafından üretilen yüksek frekanslı sinyaldir.
- Bant genişliği sinyal rate ile doğru orantılıdır
  - FSK hariç
- Örnek: Bit rate 8000bps. Baud rate 1000 baud. Her sinyal elementinde kaç bit var? Kaç farklı sinyal elementine ihtiyaç vardır?
  - r= N/S = 8000/1000=8
  - r=log₂L → L=256

## ASK – Amplitude Shift Keying

- Taşıyıcı sinyalin genliği değiştirilir. Birçok genlik seviyesi oluşturulabilir.
- Genellikle birisi 0 olmak üzere iki seviyeli değişim yapılır (On-off keying).
- BW en az S, en fazla 2S kadardır. 0<d<1, modülasyon filtre işlemine bağlıdır.

## ASK – Amplitude Shift Keying (2)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## ASK – Amplitude Shift Keying (3)

- Eğer sayısal data unipolar NRZ ile ifade edilirse, NRZ ile taşıyıcı sinyal çarpılarak ASK oluşturulur.
- İki seviye yerine 4, 8 veya daha fazla seviye kullanılabilir. Full-duplex ASK için gereken bant genişliği her yönde ayrı taşıyıcı kullanılması nedeniyle artar.

## ASK – Amplitude Shift Keying (4)

- Ani güç değişikliklerinden etkilenir
- Kolay ama verimsiz bir modülasyon tekniğidir
- Ses hatlarında (voice-grade line), 1200 bps data rate’e kadar kullanilir
- Sayısal veriyi optik fiber üzerinde iletmek icin kullanılabilir

## FSK - Frequency Shift Keying

- Taşıyıcı sinyalin frekansı değiştirilir.
- Binary FSK ile iki farklı frekansta sinyal kullanılır.

## Frequency-Shift Keying

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## FSK - Frequency Shift Keying (2)

- Voltage-controlled oscillator (VCO) tarafından oluşturulabilir.
- NRZ ile VCO kullanılarak BFSK oluşturulması şekilde görülmektedir.

## Binary Frequency-Shift Keying (BFSK)

- ASK dan daha az hata olusur
- Ses hatlarinda (voice-grade line), 1200 bps data rate’e kadar kullanılır
- Yüksek frekansli (3 to 30 MHz) radio iletişimi için kullanılabilir
- Coaxial kablo kullanan LAN’larda daha yüksek frekanslarda kullanılabilir

## Multiple Frequency-Shift Keying (MFSK)
- İki frekansdan fazlası kullanılıyor
- Bant genişliği olarak daha verimlidir ama hataya daha yatkındır. s_i(t) = A cos(2π f_i t), 1 ≤ i ≤ M
- f_i = f_c + (2i – 1 – M) f_d
- f_c = taşıyıcı frekans
- f_d = fark frekansı
- M = sinyal seviye sayısı = 2^L
- L = sinyal elemanı başına bit sayısı

## Multiple Frequency-Shift Keying (MFSK) (2)

*Bu slayt yalnızca şekil içerir.*

## Multiple Frequency-Shift Keying (MFSK) (3)
- Giriş veri hızına uymak için her çıkış sinyal elemanı Ts süre bekletilir: Ts = LT saniye (T bit periyodudur, veri hızı = 1/T).
- Bir sinyal elemani L bit input datayı kodlar

## Multiple Frequency-Shift Keying (MFSK) (4)
- Toplam bantgenişliği 2Mfd
- Gereken en küçük frekans ayrımı: 2fd = 1/Ts
- Dolayısıyla modülatör için gereken bant genişliği Wd = 2Mfd = M/Ts olur.
- FSK icin gerekli olan bandwidth taşıyıcı frekansları arasındaki uzaklığa bağlı

## Örnek

- Bit rate 3 Mbps. Bir anda 3 bit birden göndermek isteniyor. Taşıyıcı frekans 10MHz. Kaç seviye gerekir, baud rate nedir, bant genişliği nedir.
  - M = 2³ = 8
  - S=3000/3=1000 baud
  - En düşük S kadar ara olmalı 2fd=1000 B=2Mfd=8x1000=8000

## PSK – Phase Shift Keying

- Taşıyıcı sinyalin fazı değiştirilir.
- BPSK’da 0° ve 180° faz farklı iki sinyal kullanılır.
- PSK gürültüden ASK’ya göre az etkilenir.
- PSK sadece bir tane taşıyıcı frekans gerektirir, FSK seviye sayısı kadar gerektirir.

## Two-level PSK

- Taşıyıcı sinyalin fazı, veriyi ifade edebilmek için kaydırılır. Faz kayması sabit bir referans sinyale göredir.

## Phase-Shift Keying (PSK) - Differential PSK

- Differential PSK
  - Phase kaydırması referans sinyale göre degil, transmit edilen önceki bite gore yapilir
  - Zamanlama mekanizmasına ihtiyaç duymaz

## Phase-Shift Keying (PSK) - DPSK

- Differential PSK (DPSK)
  - Bir önceki bite göre phase kaydırması yapar
- Binary 0 – bir önceki bitle aynı phasede bir sinyal gonder
- Binary 1 – bir önceki bitin tam tersi phasede bir sinyal gonder

## QPSK – Quadrature Phase Shift Keying

- Bir sinyalle iki bit gönderilir.
- Her iki bit’e iki ayrı multiplier tarafından işlem yapılır.
- İki sinyal toplanarak 45°, -45 °, 135 °,-135 ° fazlarda sinyal oluşur.

## Constellation Diagram

- Sinyalin genlik ve faz değerlerini göstermek için kullanılır.
- ASK, PSK ve QAM için kullanılır. Her nokta faz ve genlik değerlerini gösterir.

## QAM - Quadrature Amplitude Keying

- ASK ve PSK birlikte kullanılır.
- Şekilde unipolar NRZ ile 4-QAM kullanımı görülmektedir.

## Analog analog çevirme

- Analog bilgi analog sinyal ile ifade edilir.
- Ortam bant geçiren ise analog analog çevir gereklidir.
- Analog analog çevirme amplitude modulation (AM), frequency modulation (FM) ve phase modulation (PM) ile yapılır.

## Amplitude Modulation

- Taşıyıcı sinyalin genliği değiştirilir.

## Amplitude Modulation (2)

- BW, modüle eden sinyalin iki katıdır.
- AM radyo kanalları 10 kHz BW sahiptir.
- Interference olmaması için her iki komşu kanal arasına 10 kHz guard band konur.
- AM taşıyıcı frekansları 530-1700 kHz arasındadır.

## Frequency Modulation

- Taşıyıcı sinyalin frekansı değiştirilir.
- BW, 2(1+ β)B olur. β modulasyon oranıdır ve genellikle 4 olarak alınır.

## Frequency Modulation (2)

- FM radyo kanalları 200 kHz BW sahiptir.
- FM taşıyıcı frekansları 88-108 MHz arasındadır.

## Phase Modulation

- Taşıyıcı sinyalin fazı modüle eden sinyalin genliğine göre değiştirilir.
- PM için BW, FM ile aynıdır.
