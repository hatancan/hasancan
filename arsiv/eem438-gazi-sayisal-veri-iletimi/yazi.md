---
baslik: EEM438 Veri İletişimi: Sayısal Veri İletimi: Hat Kodlama ve PCM (Gazi Üniversitesi, Suat Özdemir)
ozet: Gazi Üniversitesi’nden Suat Özdemir’in Veri İletişimi ders slaytları: hat kodlama teknikleri (NRZ, Manchester, AMI, 4B/5B, B8ZS, HDB3), PCM ile örnekleme, paralel ve seri iletim.
---

Gazi Üniversitesi Bilgisayar Mühendisliği Bölümü’nden Suat Özdemir’in “Veri İletişimi / Data Communications” dersi için hazırladığı 4. bölüm (Sayısal veri iletimi) slaytlarıdır (slayt tarihi 5 Mart 2011; alt bilgide BM 403 Veri İletişimi yazar). EEM438 klasöründe ikinci bir hocanın ders materyali olarak saklanmıştır. Slayt metni aşağıya aktarıldı; kitaptan alınmış şekiller ve tablolar yayımlanmadı, metni olmayan slaytlar belirtildi. Orijinal PDF yazının sonunda indirilebilir.

Kapsam: hat kodlama teknikleri (NRZ, Manchester, AMI, 4B/5B, B8ZS, HDB3), PCM ile örnekleme, paralel ve seri iletim.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Sayısal sayısal çevirme

- Bilginin iki nokta arasında iletilmesi için analog veya sayısal sinyale çevrilmesi gerekir.
- Sayısal sayısal çevirmede sayısal veri sayısal sinyale dönüştürülür.
- Analog sayısal çevirmede analog veri sayısal sinyale dönüştürülür.
- Çevirme işleminden elde edilen sinyal paralel veya seri olarak iki nokta arasında iletilir.

## Sayısal sayısal çevirme (2)

- Line coding sayısal veriyi sayısal sinyale dönüştürme işlemidir.
- Veri iletişiminde amaç, veri parçalarının iletilmesidir. En küçük parça bit olarak adlandırılır.
- Şekilde r bir sinyal parçasıyla taşınan veri parçasının sayısını göstermektedir.

## Sayısal sayısal çevirme (3)

- Data rate, bir saniyede iletilen bit sayısını gösterir (bps, bit/s).
- Signal rate, bir saniyede iletilen sinyal sayısını gösterir (baud).
- Data rate genellikle bit rate olarak ifade edilir.
- Signal rate ise baud rate, pulse rate ya da modulation rate olarak ifade edilir.
- Amaç baud rate düşürülürken bit rate değerini artırmaktır.
- Bandwidth, sinyali taşımak için gereken frekans bant genişliğini gösterir.
- Sinyaldeki değişim sayısını artırırken daha geniş frekans bandı kullanılır.

## Sinyal iletiminde sorunlar

- Sinyal kodlamada uzun 1 ve 0 serilerinin alıcıda doğru çözülmesi zordur. Önlem alınması gerekir.
- Bir sayısal sinyal belirli bir süre sabit kalırsa DC bileşen oluşur ve düşük frekansları geçirmeyen sistemler için problem oluşur. (Telefon hattı 200Hz altını geçirmez)
- İki sistemde (alıcı ve verici) bit aralığının aynı olması gerekir.
- Self-synchronizing sayısal sinyalin zamanlama bilgisini içinde bulundurmasıdır.

## Sayısal sinyal kodlama teknikleri

- 5 temel grupta toplanır

## Unipolar (non-return-to-zero)

- Bit 1 pozitif gerilim ve bit 0 negatif gerilim veya 0 V ile tanımlar.
- Sinyal bitin ortasında 0’a dönmediği için non-return-to-zero denilmektedir.

## Polar (non-return-to-zero)

- İki seviyeli sinyal kullanılır. NRZ-Level ve NRZ-Invert olarak iki türdür.
- NRZ-L kodlamada bit 0 pozitif gerilim ve bit 1 negatif gerilim ile tanımlar.
- NRZ-I da gerilim seviyesindeki değişim bit 1 ve değişmeme bit 0 dır.
- Uzun 1 ve 0 serilerinin algılanması zordur (NRZ-L da daha fazla).
- Senkronizasyon problemi her ikisinde vardır (NRZ-L da daha fazla)

## Polar (return-to-zero)

- NRZ kodlamada problem alıcı verici senkronizasyonu olmamasıdır.
- Return-to-zero’da pozitif, sıfır ve negatif gerilim seviyesi görülür.
- RZ de sinyal bitin ortasında o seviyesine döner.
- Bir bit için daha çok değişim gerekir(daha fazla band genişliği)
- DC bileşen problemi yoktur.

## Polar (Biphase: Manchester ve Differential Manchester)
- Manchester’da, sinyal bit 1 ve bit 0 için belirli işaretlere sahiptir.
- Differential Manchester’da bit 0 için bit başında değişim olur, bit 1 için değişim olmaz.
- Her ikisinde de bitin ortasında seviye değiştirilir. (senkronizasyon sağlanır)

## Polar (Biphase: Manchester ve Differential Manchester) (2)
- Manchester ve Differential Manchester kodlamalarda DC bileşen yoktur. Her bit hem pozitif hem de negatif gerilime sahiptir.
- Signal rate NRZ kodlamaya göre iki kat olur. (Bant genişliği iki kat olur)

## Bipolar (AMI – Alternate Mark Inversion ve Pseudoternary)
- AMI kodlamada, bit 0 için seviye 0 dır, bit 1 için pozitif ve negatif arasında sürekli değişir.
- Pseudoternary kodlamada, bit 1 için seviye 0 dır, bit 0 için pozitif ve negatif arasında sürekli değişir.
- Bipolar kodlamada DC bileşen yoktur. Sürekli pozitif ve negatif arasında değişim yapılır.

## Multilevel (2B1Q, 8B6T, 4D-PAM5)

- Kodlamada temel amaç veri hızını artırmak ve bant genişliğini azaltmaktır.
- m veri parçası sayısını, n sinyal parçası sayısını göstersin.
- Binary veri için 1 ve 0 olduğundan m adet veriyi 2^m farklı sinyalle gösterebiliriz.
- Her sinyalde L seviye olursa L^n adet farklı sinyal elde edilir.

## Multilevel (2B1Q, 8B6T, 4D-PAM5) (2)

- 2^m = L^n olursa her veri için bir sinyal kullanabiliriz.
- 2^m < L^n olursa tüm veriler sinyallerin bir kısmıyla ifade edilebilir.
- 2^m > L^n olursa tüm veriler elde edilen sinyallerle ifade edilemez.
- Bu şekildeki kodlama mBnL olarak adlandırılır.
- Burada, m binary verinin uzunluğunu, B binary veriyi, n sinyal uzunluğunu ve L sinyal seviye sayısını gösterir.
- L=2 ise B (binary), L=3 ise T (ternary), L=4 ise Q (quaternary) kullanılır.
- İlk ikisi (mB) veriyi, son ikisi (nL) sinyali gösterir.

## Multilevel (2B1Q)

- 2B1Q(two-binary- one-quaternary), kodlamada bir sinyal ile kodlanan veri boyutu 2 bit ve sinyaldeki toplam seviye sayısı 4 tür.
- 2B1Q, DSL(digital subscriber line) teknolojisinde kullanılır.

## Multilevel (8B6T)

- 8B6T(eight-binary-six-ternary), kodlamada 8-bit data 3 seviyeli sinyalle gösterilir.
- 2⁸ = 256 farklı veri ve 3⁶ = 729 farklı sinyal kullanılır.
- Sinyallerin bir kısmı senkronizasyon ve hata denetimi için kullanılır.
- Her bit grubu için kullanılacak sinyal grubu sabittir.
- 8B6T, 10Base-4T ağlarda kullanılır.

## Multilevel (4D-PAM5)

- 4D-PAM5 (four-dimensional five-level pulse-amplitude-modulation), kodlamada 4D verinin 4 kablo ile iletildiğini gösterir.
- 5 farklı sinyal seviyesi (-2,-1,0,1,2) kullanılır.
- Bir sinyal elemanıyla 8 bit gönderilir.
- Sinyal 4 parçayla gösterilir her parçası bir kablodan iletilir.
- 4D-PAM5 kodlama Gigabit LAN ağlarda kullanılır.

## Multiline İletişim (MLT-3)

- NRZ-I ve Differential Manchester datayı kodlarken iki geçiş kuralı uygular.
- MLT-3 (Multiline Transmission, Three Level) kodlama, iki seviyeden fazla seviyeye sahip veri için kullanılır MLT-3 üç seviyeli (+V 0 -V) geçiş kuralı kullanılır.
- Daha az değişim olduğu için bant genişliği ¼ oranındadır. (BW = ¼ Bit rate)
- Bir sonraki bit 0 ise geçiş olmaz.
- Bir sonraki bit 1 ise ve şimdiki seviye 0 değilse, bir sonraki seviye 0 olur.
- Bir sonraki bit 1 ise şimdiki seviye 0 ise, bir sonraki seviye 0 olmayan son seviyenin tersi olur.

## Multiline İletişim (MLT-3) (2)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Line coding yöntemleri özet

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Blok kodlama

- Senkronizasyonu daha iyi yapmak ve hata denetimi yapmak için ekstra bitlere ihtiyaç olur.

## Blok kodlama (2)

- Block coding, m adet biti n adet bit haline çevirir (mB/nB). Burada (n > m).
- “/” işareti blok kodlamayı, multilevel kodlamadan ayırır (8B6T).
- m-bit grup n-bit grup yerine yerleştirilir.
- 4B/5B de orijinal bitler 4-bit gruplara ayrılır ve her 4-bit yerine 5-bit yazılır.

## Blok kodlama (4B/5B)

- 4B/5B (four binary/five binary) kodlama NRZ-I ile birlikte kullanılır. NRZ-I kodlama uzun 0 larda senkronizasyon problemi vardır. NRZ-I kodlamadan önce uzun 0 olmayacak şekilde değişiklik gerekir. Alıcı önce NRZ-I ile bitleri elde eder daha sonra fazlalık olan 1-bit atılır. 4B/5B ikiden fazla 0 bulundurmaz. Tüm gruplar içinde üçten fazla 0 olmaz.
- Eklenen 1 bit %20 fazla trafik gerektirir. DC bileşen hala vardır.

## Blok kodlama (4B/5B) (2)

- Örnek: 1 Mbps hızda veri göndermek istiyoruz. 4B/5B ve NRZ-I ile Manchester kullanıldığında gereken minimum bant genişliği nedir ? 4B/5B bit rate değerini 1.25 Mbps olarak artırır. NRZ-I kodlama N/2 bant genişliği gerektirdiğinden 625 kHz gerekir. Manchester kodlama 1 MHz bant genişliği gerektirir. NRZ-I da DC bileşen vardır, Manchester’da DC bileşen yoktur.

## Blok kodlama (8B/10B)

- 8B/10B (eight binary/ten binary) kodlama 8-bit yerine 10-bit kullanır.
- Bir tane 5B/6B ile (soldaki 5 bit için) bir tane 3B/4B (sağdaki 3 bit için) vardır.
- Disparity controller hata denetimi yapar. 2¹⁰ – 2⁸ = 768 fazla grup oluşur.

## Scrambling

- Biphase yöntemi kısa mesafede iki istasyon arasında (LAN içinde) uygundur ancak geniş bant genişliği gerektirdiği için uzun mesafede uygun değildir.
- Blok kodlama ve NRZ nin birlikte kullanımı da uzun mesafede DC bileşen olduğu için uygun değildir.
- Bipolar AMI kodlama dar bant genişliği gerektirir ve DC bileşen yoktur. Ancak uzun 0 larda senkronizasyon yoktur.
- Belirli sayıdaki 0 serisi farklı bir seriyle değiştirilir.

## Scrambling (B8ZS – Bipolar with 8-zero substitution)
- 8 artarda gelen 0 seviye gerilim yerine 000VB0VB yerleştirilir.
- V, AMI kodlamada bir önceki gerilim seviyesinin aynısını gösterir.
- B, bipolar bir önceki gerilim seviyesinin tersini gösterir.

## Scrambling (HDB3 – High-density bipolar 3-zero)
- 4 artarda sıfır gerilim seviyesi 000V veya B00V ile değiştirilir.
- Son substitution’ dan sonra eğer sıfırdan farklı pulse sayısı tek ise, 000V işareti kullanılır. Böylece sıfırdan farklı pulse sayısı çift olur.
- Son substitution’ dan sonra eğer sıfırdan farklı pulse sayısı çift ise, B00V işareti kullanılır. Böylece sıfırdan farklı pulse sayısı çift olur.

## Analog sayısal çevirme

- Bazı uygulamalarda analog sinyal vardır (mikrofon veya kamera üretir).
- Analog sinyal sayısal dataya çevirilir ardından sayısal sinyale dönüştürülür.
- Pulse code modulation (PCM) En yaygın kullanılan analog sinyal-sayısal data dönüştürme yöntemidir.

## Analog sayısal çevirme (2)

- Analog sayısal çevirmenin 3 aşaması vardır
  - Örnekleme (Sampling)
  - Sayısallaştırma (Quantization)
  - Orijinal sinyali tekrar oluşturma

## Örnekleme - Sampling

- Her Ts aralığında analog sinyal örneklenir (sampling rate, sampling frequency).
- Üç farklı örnekleme yapılır. Sample and hold (flat-top) yaygın kullanılır.

## Sampling rate

- Nyquist teoremine göre örnekleme frekansı (sampling rate) en yüksek frekansın en az iki katı olmalıdır.

## Sampling rate (2)

- Örnekleme frekansı düşükse saat ters dönüyor gibi görünür.
- Bir filmde saniyede 24 frame geçer. 12’den az örnekleme undersampling’tir.

## Sayısallaştırma – Quantization

- Örneklenen değerler analogtur. Minimum ve maksimum arası L seviyeye bölünür. İki seviye arasındaki fark Δ = (Vmax–Vmin )/L olur.
- Örnekte, Vmax = +20 V, Vmin = -20 V, L=8

## Orijinal sinyali tekrar oluşturmak

- Bit dizisi tekrar analog sinyali oluşturmak için kullanılır.

## Delta modülasyonu

- Delta modülasyonu PCM’den daha basittir.
- Örneklenen değer bir öncekinden büyükse artış, küçükse azalış gerçekleştirilir.

## İletişim modları

- Paralel ve seri iletişim yapılır.

## Paralel iletişim

- Aynı anda n bit gönderilir.
- Maliyet yüksektir, hızlıdır. Kısa mesafelerde kullanılır.

## Seri iletişim

- Aynı anda 1 bit gönderilir.
- Maliyet düşüktür, yavaştır. Uzun mesafelerde kullanılır.

## Seri iletişim - asenkron

- Bilgi gruplar halinde gönderilir. Bir grupta genellikle 8 bit olur.
- Bir grubun geldiğini alıcıya start biti, bittiğini stop biti gösterir.
- Byte seviyesinde asenkrondur, ama bit seviyesinde senkron yapmak gerekir.
- Keyboard, mouse örnektir.

## Seri iletişim - senkron

- Start ve stop biti olmadan bitler ardarda gönderilir.
- Bitleri gruplara ayırmak ve zamanlama işlemleri alıcı tarafından yapılır.
- Asenkrona göre daha hızlıdır. 
## Isochronous iletişim
- Gerçek zamanlı video ve audio uygulamalarında frame’ler arasında bekleme istenmez.
- Isochronous iletişim sabit hızda verinin iletimini sağlar.

*Not: Slaytlardaki üs ve alt simgeler PDF metninde düz rakam olarak çıktığı için (2^m, L^n, 2⁸, 3⁶, 2¹⁰) düzeltildi.*
