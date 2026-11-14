---
baslik: EEM438 Veri İletişimi: Veri ve Sinyaller (Gazi Üniversitesi, Suat Özdemir)
ozet: Gazi Üniversitesi’nden Suat Özdemir’in Veri İletişimi ders slaytları: analog ve sayısal sinyaller, frekans ve bant genişliği, zayıflama, Nyquist ve Shannon sınırları, performans ölçütleri.
---

Gazi Üniversitesi Bilgisayar Mühendisliği Bölümü’nden Suat Özdemir’in “Veri İletişimi / Data Communications” dersi için hazırladığı 3. bölüm (Veri ve Sinyaller) slaytlarıdır (slayt tarihi 5 Mart 2011; alt bilgide BM 403 Veri İletişimi yazar). EEM438 klasöründe ikinci bir hocanın ders materyali olarak saklanmıştır. Slayt metni aşağıya aktarıldı; kitaptan alınmış şekiller ve tablolar yayımlanmadı, metni olmayan slaytlar belirtildi. Orijinal PDF yazının sonunda indirilebilir.

Kapsam: analog ve sayısal sinyaller, frekans ve bant genişliği, zayıflama, Nyquist ve Shannon sınırları, performans ölçütleri.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Analog ve sayısal sinyal

- Fiziksel katmanın önemli işlevlerinden birisi iletim ortamında sinyaller ile veriyi taşımaktır.
- Analog data sürekli bilgiyi, sayısal data ayrık durumlu bilgiyi gösterir.
- Analog sinyal belirli bir zaman aralığında sonsuz değere sahiptir (continuous).
- Sayısal sinyal sınırlı sayıda değere sahiptir. Genellikle 0 ve 1 değerlerini ifade eder (discrete).

## Analog ve sayısal sinyal (2)

- Periyodik sinyal belirli bir zaman aralığında sürekli aynı işareti tekrarlar.
- Periyodik sinyalde bir işaret için zaman aralığı periyot ve tekrar edilen işaret cycle olarak adlandırılır. Frekans 1 saniyedeki tekrar sayısıdır.
- Aperiyodik sinyal tekrarlayan işaret bulundurmaz.
- Aperiyodik sinyallerde periyot süresi sonsuzdur, frekans değeri sıfırdır.

## Periyodik analog sinyal

- Periyodik analog sinyaller basit ve birleşik(composite) olarak iki gruptur.
- Basit analog sinyal olan sinüs sinyali daha basit sinyallere ayrıştırılamaz.
- Birleşik analog sinyaller basit sinüs sinyalleriyle oluşturulabilir.
- Bir sinüs sinyali genlik (amplitude), frekans (frequency) ve faz (phase) ile ifade edilir.

## Periyodik analog sinyal (2)

- Periyod sinyalin bir cycle tamamlaması için geçen süreyi ve frekans 1 saniyedeki periyod sayısını gösterir. f=1/T,T=1/f
- Periyod (s) ile frekans Hertz (Hz) ile ifade edilir.
- Hiç değişmeyen sinyalin frekansı 0 ve periyodu sonsuzdur.
- Ani değişen sinyalin periyodu 0 ve frekansı sonsuzdur.

## Periyodik analog sinyal (3)

- Faz (phase), zaman t=0 iken sinyalin pozisyonunu gösterir.
- Yanda 0º, 90º ve 180º faz açısına sahip sinyaller görülmektedir.

## Periyodik analog sinyal (4)

- Dalga boyu (wavelength), sinyalin bir periyotta aldığı yolun uzunluğudur. Birimi metredir. λ = c/f = c·T (c = 3×10⁸ m/s)

## Periyodik analog sinyal (5)

- Zaman düzlemi (time-domain) grafiği sinyalin zamana göre değişimini gösterir.
- Frekans düzlemi (frequency-domain) frekans ve genlik arasındaki ilişkiyi gösterir.

## Periyodik analog sinyal (6)

- Şekilde iki sinüs sinyali ile DC sinyalin frekans düzleminde gösterimi verilmiştir.
- Şekildeki DC sinyalin frekansı 0 ve genliği 15 tir.

## Periyodik analog sinyal (7)

- Composite sinyal çok sayıda sinüs sinyalinin birleşimiyle oluşur.
- 1900lerde Jean-Baptiste Fourier, herhangi bir composite sinyalin, genliği, frekansı ve fazı farklı basit sinüs sinyallerinin birleşimi olduğunu göstermiştir.
- f, fundemantal (temel) frekans veya 1.harmonik, 3f, 3.harmonik, ve 9f, 9.harmoniktir.

## Periyodik analog sinyal (8)

- Şekilde aperiyodik sinyalin frekans-düzleminde gösterimi verilmiştir.

## Periyodik analog sinyal (9)

- Composite sinyali oluşturan sinyallerin frekans aralığı bant genişliği (bandwidth) olarak adlandırılır.

## Periyodik analog sinyal (10)

- Örnek: 100,300,500,700 ve 900Hz frekanslarında 10V genlikli 5 tane sinüs sinyalinden oluşan periyodik sinyalin frekans düzlemi grafiğini çiziniz.

## Periyodik analog sinyal (11)

- Örnek: Bir periyodik sinyalin bant genişliği 20Hz dir. En yüksek 60Hz ise en düşük frekans nedir ? Sinyalin tüm bileşenleri aynı genlikte olduğuna göre spektrumu çiziniz.

## Sayısal sinyal

- Bilgi analog sinyalle gösterilebildiği gibi sayısal sinyalle de gösterilebilir.
- 1 pozitif gerilimle, 0 ise sıfır genlikle gösterilebilir.
- Sayısal sinyal ikiden fazla genliğe sahip olabilir. L tane seviyeye sahip sinyalin her seviyesinde log₂L bit ifade edilir.

## Sayısal sinyal (2)

- Sayısal sinyallerin çoğu periyodik değildir.
- Bit rate saniyede gönderilen bit sayısıdır (bps).
- Bit length bir bit için iletim ortamında alınan yoldur. bit length = propagation speed * bit duration
- Örnek: Her sayfada 24 satır ve 80 sütun olan 100 sayfalık dosya 1 saniyede download edilmiştir. Her karakter 8 bit olduğuna göre bit rate nedir? Bit rate = 100*24*80*8 = 1.536.000 bps = 1,536 Mbps
- Örnek: HDTV için bit rate nedir ? HDTV ekranı 16:9 boyutundadır. Ekranda 1920*1080 piksel vardır. Her piksel 24 bitle gösterilir ve ekran saniyede 30 defa yenilenir. Bit rate = 1920*1080*30*24 = 1.492.992.000 bps = 1,5 Gbps

## Sayısal sinyal (3)

- Bir sayısal sinyal sonsuz bant genişliğine sahip analog composite sinyaldir.
- Şekilde periyodik ve aperiyodik sayısal sinyallerin bant genişliği verilmiştir.

## Sayısal sinyal (4)

- Sayısal sinyal iletimi baseband veya broadband (modülasyon kullanılarak) şeklinde yapılabilir.
- Baseband iletişimde sayısal sinyal (analog sinyale çevirmeden) gönderilir.
- Baseband iletişimde bir low-pass (alçak geçiren) kanal kullanılır. İletim ortamı sadece bir kanal oluşturur.

## Sayısal sinyal (5)

- Baseband iletişim, sınırlı bant genişliği (limited bandwidth) ve geniş bant genişliği (wide bandwidth) ile oluşturulan low-pass kanal ile yapılabilir.

## Sayısal sinyal (6)

- Genişbant genişliğine sahip iletim ortamıyla iki cihaz çok iyi haberleşebilir.
- Şekilde f1 sıfıra yakın f2 ise çok yüksek bir frekanstır.
- Sayısal sinyalin baseband iletiminde orijinal şekli korunur. Low-pass kanalın 0 ile yüksek bir bant genişliğine sahip olması gerekir.
- LAN ağlarda bir kanal oluşturulur ve tüm bant genişliği iki cihaz arasındaki iletişime ayrılır.

## Sayısal sinyal (7)

- Sınırlı bant genişliğine sahip iletim ortamıyla yapılan iletişimde analog sinyal ile sayısal sinyal yaklaşık elde edilir.
- Elde edilen sinyalin, orijinal sayısal sinyale benzeme oranı bant genişliğine bağlıdır.
- Şekilde N bit oranını gösterir. Analog sinyalin maksimum frekansı en kötü durum olan 1010 veya 0101 için N/2 dir. Diğerleri için N/4 tür.
- Bant genişliği = N/2 – 0 =N/2

## Sayısal sinyal (8)

- Analog sinyali, orijinal sayısal sinyale daha çok benzetmek için daha fazla harmonik kullanılması gerekir. (Bant genişliğinin artırılması gerekir.)
- Baseband iletişimde gereken bant genişliği bit rate değerine bağlıdır.
- Baseband iletişimde, daha hızlı veri göndermek için bant genişliğini artırmak gerekir.

## Sayısal sinyal (9)

- Tabloda farklı hızlarda (N) veri göndermek için gereken bant genişlikleri (B) verilmiştir.
- Baseband iletişimde gereken bant genişliği bit rate değerine bağlıdır.

## Sayısal sinyal (10)

- Örnek: Baseband iletişimle 1 Mbps hızla veri göndermek için gerekli bant genişliği ne olmalıdır ? Low-pass kanal için minimum BW = N / 2 = 1Mbps / 2 = 500KHz ( sadece 1.harmonik) Daha iyi BW = 3 * 500 KHz = 1.5 MHz (1. ve 3. harmonik) 5.Harmonik kullanılırsa BW = 5 * 500 KHz = 2.5 MHz (1., 3., 5. harmonik)
- Örnek: 100 KHz bant genişliğinde low-pass kanal ile maksimum bit rate nedir ? 1 Harmonik kullanılır maksimum bit rate elde edilir. BW = N/2, N (Bit rate) = 100 KHz * 2 = 200 Kbps

## Sayısal sinyal (11)

- Broadband iletişimde sayısal sinyal modüle edilerek analog sinyale çevrilir.
- Modülasyon bant geçiren kanal oluşturmayı sağlar.
- Telefon hatları 0-4KHz bant genişliğinde ses sinyalleri için tasarlanmıştır.
- Baseband iletişim yapılırsa maksimum bit rate 8 Kbps olur.

## Sayısal sinyal (12)

- Broadband iletişim yapılırsa sayısal sinyali analog sinyale dönüştürmek gerekir. Bunun için modem (modulator/demodulator) kullanılır.

## İletişim zayıflaması

- İletim ortamında sinyal zayıflar ve gönderilenle aynı olmaz.
- Sinyal zayıflamasının attenuation, distortion ve noise olarak 3 nedeni vardır.
- Attenuation, sinyalin enerjisinin ortamın direncinden dolayı azalmasıdır.
- Sinyaldeki zayıflama ve kazanç decibel (dB) ile ifade edilir. dB = 10log₁₀ (P2/P1)

## İletişim zayıflaması (2)

- Örnek: P2 = ½ P1 ise attenuation nedir? 10 log₁₀(P2/P1) = 10.log₁₀(0.5 P1/P1) = 10 . (-0.3) = -3 dB
- Örnek: P2 = 10P1 ise attenuation nedir ? 10 log₁₀(P2/P1) = 10.log₁₀(10) = 10 . (1) = 10 dB

## İletişim zayıflaması (3)

- Distortion, sinyalin şeklinin değişmesini ifade eder.
- Sinyaldeki bileşenlerin hepsi farklı hızlarda ilerler. Hedefe varış süreleri farklıdır ve elde edilen sinyalin şekli orijinalden farklıdır.

## İletişim zayıflaması (4)

- Noise, sinyalde bozulma yapan etkilerdir. Thermal noise, induced noise, crosstalk ve impulse noise sinyali bozabilir.
- Thermal noise, telde elektron hareketlerinden oluşur.
- Induced noise, motor veya diğer cihazlardan oluşabilir.
- Crosstalk bir kablonun diğerini etkilemesiyle oluşur.
- Impulse noise, öngörülemeyen ve aniden oluşan (şimşek vb.) etkilerdir.

## Categories of Noise

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Categories of Noise (2)

- Crosstalk: Impulse Noise:
  - caused by external electromagnetic interferences
  - noncontinuous, consisting of irregular pulses or spikes
  - short duration and high amplitude
  - minor annoyance for analog signals but a major source of error in digital data
  - a signal from one line is picked up by another
  - can occur by electrical coupling between nearby twisted pairs or when microwave antennas pick up unwanted signals

## İletişim zayıflaması (5)

- Signal-to-Noise Ratio (SNR), sinyal gücünün noise gücüne oranıdır. Şekilde yüksek ve düşük SNR örnekleri verilmiştir.
- SNRdB = 10 log 10 SNR olarak ifade edilir.
- Örnek: Sinyal gücü 10mW ve noise gücü 1μW ise SNR ve SNRdB nedir? SNR = 10.000μW/1μW = 10.000, SNRdB = 10log₁₀SNR = 10log₁₀10.000 = 40dB

## Veri iletişim limitleri

- Veri iletişim oranı 3 faktöre bağlıdır:
  - Kullanılan bant genişliğine
  - Kullanılan sinyaldeki seviye sayısına
  - Kanal kalitesine (noise seviyesine)
- Nyquist tarafından gürültüsüz ve Shannon tarafından gürültülü kanal için data rate oranı belirlenmiştir. Nyquist Bit Rate = 2*BW*log₂L bps BW = Bandwidth, L = Sinyal seviye sayısı
- L arttıkça sistemin güvenilirliği azalır.

## Veri iletişim limitleri (2)

- Örnek: BW = 3000 Hz olan bir sistemde L=2 ise maksimum bit rate nedir? Bit rate = 2 * BW * log₂L = 6000 * log₂ 2 = 6000 bps Sinyal seviye sayısı 4 olursa, Bit rate = 2 * BW * log₂4 = 6000 * 2 = 12000 bps
- Örnek: 265 kbps bit rate için, BW=20 kHz olan gürültüsüz ortamda kaç seviyeli, sinyal kullanılmalıdır. 265000 = 2*20000*log₂L → 265000/40000 = log₂L → L = 98.7 seviye gereklidir.

## Veri iletişim limitleri (3)

- Claude Shannon 1944’te gürültülü kanal için teorik en yüksek bit rate’i belirlemiştir. Capacity = BW*log₂(1+SNR) bps
- Kapasite bir kanalın özelliğini belirler iletişim metodunu değil !
- Kapasite, kaç seviye kullanılırsa kullanılsın maksimum bit rate değerini gösterir.

## Veri iletişim limitleri (4)

- Örnek: SNR değeri yaklaşık 0 olan çok gürültülü bir kanalda kapasite ne kadardır ? C = BW*log₂(1+SNR) = BW*log₂1 = 0 olur.
- Örnek: Telefon hatlarında BW=3000Hz (3300-300Hz) dir. SNR değeri genellikle 3162 dir. Kanal kapasitesi nedir ? C =BW*log₂(1+SNR) = 3000*log₂(1+3162) = 3000*11.62 = 34.860 bps
- Örnek: SNRdB = 36 ve BW = 2 MHz olan kanalda teorik kanal kapasitesi nedir ? SNRdB = 10log₁₀SNR → SNR = 3981 C = BW * log₂(1+SNR) = 2×10⁶ × log₂(3982) ≈ 24 Mbps

## Performans

- Bant genişliği, ağ performansını belirleyen ölçütlerden birisidir.
- Bant genişliği Hz olarak frekans bandını veya bps olarak bir rate değerini gösterir.
- Throughput, bir bağlantının gerçek bps değeridir.
- Latency (delay), ilk bitin kaynaktan çıkmasından sonra tüm mesajın tamamının hedefe ulaşması için geçen süredir.
- Latency = PT+TT+QT+PD, PT=Propagation time, TT=Transmission time, QT=Queuing time, PD=Process delay
- Propagation time, uzaklığın yayılım hızına oranıdır.
- PT = D/PS, D = distance, PS = Propagation speed
- Transmission time, mesaj boyutunun bant genişliğine oranıdır.
- TT = MS/BW, MS= Message size

## Performans (2)

- Örnek: 2.5kbyte bir e-mail için 1Gbps bant genişliği olan ağda PT ve TT değerleri nedir? Alıcı verici arasında 12000km mesafe var ve yayılım hızı 2,4×10⁸ m/s. PT = (12000×10³)/(2,4×10⁸) = 50 ms, TT = (2500×8)/10⁹ = 0,02 ms

## Performans (3)

- Bandwidth-delay çarpımı bağlantıda aynı anda bulunan bit sayısını gösterir.
- Jitter, farklı paketlerdeki gecikme sürelerinin değişimidir.

## Performans (4)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*

*Not: Slayttaki “2*BW*log₂1 = 0” ifadesinde baştaki 2 çarpanı Shannon formülünde yoktur; sonuç 0 olduğundan değişmez, metinde C = BW·log₂(1+SNR) biçiminde yazıldı. Dalga boyu ve hesaplardaki üslü sayılar (10⁸, 10⁶, 10³, 10⁹) PDF metninde düz rakam olarak çıktığı için üst simgeyle düzeltildi.*
