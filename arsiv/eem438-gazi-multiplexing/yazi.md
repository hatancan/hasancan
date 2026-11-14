---
baslik: EEM438 Veri İletişimi: Çoklama: FDM, WDM, TDM ve Yayılmış Spektrum (Gazi Üniversitesi, Suat Özdemir)
ozet: Gazi Üniversitesi’nden Suat Özdemir’in Veri İletişimi ders slaytları: FDM, WDM, senkron ve istatistiksel TDM, DS hizmetleri ve yayılmış spektrum (FHSS, DSSS).
---

Gazi Üniversitesi Bilgisayar Mühendisliği Bölümü’nden Suat Özdemir’in “Veri İletişimi / Data Communications” dersi için hazırladığı 6. bölüm (Multiplexing) slaytlarıdır (slayt tarihi 21 Mart 2011; alt bilgide BM 403 Veri İletişimi yazar). EEM438 klasöründe ikinci bir hocanın ders materyali olarak saklanmıştır. Slayt metni aşağıya aktarıldı; kitaptan alınmış şekiller ve tablolar yayımlanmadı, metni olmayan slaytlar belirtildi. Orijinal PDF yazının sonunda indirilebilir.

Kapsam: FDM, WDM, senkron ve istatistiksel TDM, DS hizmetleri ve yayılmış spektrum (FHSS, DSSS).

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Multiplexing

- Çoklama/Multiplexing’te amaç etkinliktir. Birden fazla kanal birleştirilerek bir kanal oluşturulur.
- Yayma/Spreading’te amaç gizlilik ve yığılmayı önlemektir. Bunun için bantgenişliği artırılır.
- İki cihazı bağlayan ortamın bant genişliği gerekenden fazla ise, bağlantı paylaşılabilir.
- Multiplexing bir bağlantı üzerinden çok sayıda sinyalin eş zamanlı iletimini sağlayan tekniklere verilen genel isimdir.
- Mux (multiplexer) çok girişi bir kaynakta birleştirir (many-to-one), demux (demultiplexer) ise bir kaynaktaki sinyalleri ayırır (one-to-many).
- Link, fiziksel bağlantıyı, kanal link içindeki bir kısmı ifade eder.

## Multiplexing (2)

- Üç temel teknik vardır.
  - Frequency-division multiplexing (FDM)
  - Wave-division multiplexing(WDM)
  - Time-division multiplexing (TDM)

## FDM -Frequency-division multiplexing

- FDM, bağlantının bant genişliği iletilecek sinyalin bant genişliğinden fazlaysa kullanılan analog bir tekniktir.
- FDM’de her cihaz ile farklı bir taşıyıcı sinyal modüle edilir.
- FDM analog sinyalleri birleştiren analog tekniktir.

## FDM

- Her sinyal ayrı bir taşıyıcıyı modüle eder (Multiplexer). Link ile birleştirilmiş sinyal iletilir.

## FDM (2)

- Demultiplexer bir dizi filtre ile sinyali ayrıştırır.

## FDM – Örnek 1

- Ses kanalları 4 kHz bant genişliğine sahiptir. 3 ses kanalını birleştirmek için 12 kHz bant genişliğinde linke ihtiyaç vardır. Örnek bir konfigürasyon aşağıdaki gibi olabilir.

## FDM – Örnek 2

- 4 kanalın her biri 1 Mbps iletişim yapmaktadır. Bir uydudaki 1 MHz kanalın FDM ile konfigürasyonu aşağıdaki gibi olabilir.
- Her kanal 250 kHz bant genişliğine sahiptir ve her kanalda 16-QAM (1 Hz ile 4-bit gönderilir) modülasyon yapılır.

## FDM – Örnek 3

- Düşük bant genişliğine sahip kanallar daha yüksek bant genişliğine sahip kanallara multiplex yapılır.

## FDM – Örnek 4

- AMPS (Advanced Mobile Phone System) iki bant kullanır. Gönderme için 824-849 MHz ve alma için 869-894 MHz bantları kullanılır. Her kullanıcı bir yönde 30 kHz bant genişliğine sahip kanal kullanır. Kaç kullanıcı eş zamanlı iletişim yapabilir? Her bant 25 MHz (849-824 ve 894-869) tir. 25 MHz / 30 kHz = 833.33 olur. Gerçekte her bant 832 kanala bölünür. Toplam 42 kanal kontrol için kullanılır. 790 kanal kullanıcılar için ayrılır. Her iki kanalda full-duplex eş zamanlı 790 kullanıcı iletişim yapabilir.

## FDM – Örnekler

- AM radyolar 530 kHz-1700 kHz arasındaki bantta FDM yapılarak 10 kHz kanallara yerleştirilirler.
- FM radyolar 88 MHz-108MHz arasındaki bantta FDM yapılarak 200 kHz kanallara yerleştirilirler.
- TV yayınları 6MHz bant genişliğine sahip kanallara yerleştirilirler.
- İlk jenerasyon cep telefonları FDM kullanır. Her kullanıcı için 30 kHz kanallar atanır. Ses sinyali 3 kHz bant genişliğine sahiptir ve FM de kanal bant genişliği 10 x modüle eden sinyal olduğundan toplam bant genişliği 30 kHz olur. Her kullanıcıya full-duplex iletişim için 60 kHz kanal atanır.

## WDM–Wavelength division mult.

- WDM,fiber optik kablonun yüksek bant genişliğini kullanmak için tasarlanmıştır. WDM, optik sinyalleri birleştiren multiplexing tekniğidir.
- WDM, SONET(Synchronous Optical Network) ağlarda kullanılır. Dense WDM (DWDM) kanalları çok yakın multiplex yaparak daha çok kanalı birleştirir.

## WDM–Wavelength division mult. (2)

- Günümüz WDM sistemleri 160 farklı sinyal elemetini destekleyebilir
  - Tek fiberden oluşan 10 Gbit/s lik sistem 1.6 Tbit/s veri taşıyabilir
- Bu nedenle WDM sistemleri telekomunikasyon firmaları tarafından fazlaca kullanılırlar.
- WDM ve optical amplifier’lar kullanarak telekomuikasyon şirketleri birden fazla teknolojiyi (OSI, TCP/IP) bir arada destekleyebilirler.

## TDM-Time division multiplexing

- TDM yüksek bant genişliğine sahip bir linki birden çok bağlantıya paylaştırır.
- FDM bandın bir kısmını paylaştırırken, TDM bandın tümünü zamana göre paylaştırır.
- TDM senkron ve istatistiksel olarak iki türdür. Senkron TDM’de veri olmasa bile her girişe belirli bir zaman ayrılır.

## TDM - Senkron

- Senkron TDM’de her girişin verisi birimlere ayrılır. Birim 1 bit, 1 karakter veya 1 blok olabilir.
- Girişlerin zaman aralıkları frame oluşturur. Bir frame, tüm girişlerin 1 birim verisinin birleşiminden oluşur.

## TDM - Senkron (2)

- Örnek
  - Şekilde bir birim veri 1 bittir.
  - Giriş bit süresi = 1 / 1 Mbps = 1 μs.
  - Çıkış bit süresi = 1 / 4 μs.
  - Çıkış bit rate = 1 / 4 μs = 4 Mbps. (4 x 1 Mbps = 4 Mbps)
  - Frame rate = 1 Mbps (1 girişin bit rate değeridir)

## TDM - Senkron (3)

- TDM iki uçta hızlı switch’lerle yapılır. İki switch senkron çalışır.
- Interleaving, her iki uçtada switch’lerin belirli aralıklarla her giriş/çıkış için bağlantı süresini ifade eder.

## TDM - Senkron (4)

- Örnek
  - Şekilde 4 kanal TDM kullanılarak multiplex yapılmaktadır. Her kanal 100 byte/s veri gönderme hızına sahiptir ve her kanal 1 byte/s multiplex yapılmaktadır.
  - Frame boyutu = 4 byte (32 bit).
  - Bir frame her girişten 1 byte/s alır. Frame rate = 100 frame/s.
  - Frame süresi = 1/100 s.
  - Bit rate = frame rate × frame boyutu = 100 frame/s × 32 bit = 3200 bps.

## TDM - Senkron (5)

- Örnek
  - Bir multiplexer 4 tane 100 kbps kanalı her zaman aralığında 2-bit alarak birleştiriyor.
  - Her kanaldan 2 bit alındığından link 100 kbps/2 = 50.000 frame/s hızındadır.
  - Frame süresi = 1 / 50.000 = 20 μs.
  - Bit rate = 50.000 * 8 = 400 kbps.
  - Bit süresi = 1 / 400 kbps = 2,5 μs.

## TDM - Senkron (6)

- Her girişe gönderecek verisi olmasa da zaman ayrılır.
- Frame’lerde boş slotlar ayrıldığından verim düşer.

## TDM - Senkron (7)

- Data rate management
  - Farklı hızlardaki girişleri birleştirilmesini gerekebilir.
  - Multilevel multiplexing

## TDM - Senkron (8)

- Data rate management
  - Multiple slot allocation
- Bir seri paralel çevirici kullanılmıştır.
  - Pulse stuffing
- Boş bitler ile bit rate istenen değere çıkarılır.

## TDM - Senkron (9)

- Multiplexer ve demultiplexer arasında frame bazında senkronizasyon yapılmalıdır.
- Her frame’in başına senkronizasyon bitleri konur (framing bits).
- Genellikle her frame başına 1 ve 0 değişimi yapan 1 bit konur.

## TDM - Senkron (10)

- Örnek
  - 4 kaynaktan 250 karakter/s veri oluşturuluyor. Interleaved birim 1 karakter ve frame başına 1 bit senkronizasyon biti konmaktadır.
  - Her giriş için data rate = 250 * 8 = 2000 bps = 2 kbps.
  - Bir karakter süresi = 1 / 250 = 4 ms.
  - Frame rate = 250 frame /s.
  - Her frame için süre = 1 / 250 = 4 ms.
  - Her frame’de 4*8+1 = 33 bit bulunur.
  - Link için data rate = 250 × 33 = 8250 bps.

## Digital Signal Service

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Digital Signal Service (2)

- A DS-0 service is a single digital channel of 64 kbps.
- DS-1 is a 1.544-Mbps service; 1.544 Mbps is 24 times 64 kbps plus 8 kbps of overhead. It can be used as a single service for 1.544-Mbps transmissions, or it can be used to multiplex 24 DS-0 channels or to carry any other combination desired by the user that can fit within its 1.544-Mbps capacity.
- DS-2 is a 6.312-Mbps service; 6.312 Mbps is 96 times 64 kbps plus 168 kbps of overhead.
- DS-3 is a 44.376-Mbps service; 44.376 Mbps is 672 times 64 kbps plus 1.368 Mbps of overhead.
- DS-4 is a 274.176-Mbps service; 274.176 is 4032 times 64 kbps plus 16.128 Mbps of overhead

## TDM - İstatistiksel

- Senkron TDM veri göndermeyen girişe zaman ayırdığından etkin değildir.
- TDM’de verisi olan girişe zaman ayrılır. Bir frame’deki slot sayısı giriş sayısından daha azdır.
- Multiplexer, girişleri round-robin yaklaşımıyla kontrol eder.

## TDM - İstatistiksel (2)

- Senkron TDM’de frame’ler sadece veri bulundurur. İstatistiksel TDM’de veri ile birlikte adres bilgiside gönderilir.
- Adresleme binary yapılır ve n bit ile N (n = log₂N) adet çıkış adreslenebilir.
- İstatistiksel TDM’de iletişimin etkinliği için adres ile veri arasındaki oran önemlidir.
- İstatistiksel TDM’de senkronizasyon bitlerine gereksinim yoktur.

## Spread spectrum

- Multiplexing birden çok kaynağa bir linki paylaştırır.
- Spread spectrum, birden çok kaynağa daha geniş bant genişliğine sahip bir linki paylaştırır.
- Spread spectrum kablosuz LAN ve kablosuz WAN’larda kullanılır.
- Her kanal için gereken bant genişliği B ise, spread spectrum B_ss’ye genişletir. (B_ss >> B)
- Spreading işlemi spread kod kullanılarak yapılır.

## Spread Spectrum

- Spread spectrum teknikleri gerekenden çok daha fazla bir bantgenişliği kullanır
  - Tek kullanıcı için gereksiz bantgenişliği israfı olur ancak çoklu kullanımda kullanıcılar aynı bantgenişliğini girişim olmadan kullanabilir
  - Dolayısı ile çoklu kullanımda spread spectrum bantgenişliği açısından etkin bir yöntemdir

## Spread Spectrum (2)

- Spread spectrum iletilecek veri için gerekli olan bantgenişliğinin yayılmasını içerir
- Örneğin CDMA spread spectrum tekniğine dayanan bir çoklu erişim modelidir. CDMA de ortak bir kanalı kullanan her bir kullanıcıya ayrı frekans bandını kaplayan bir sinyal (code) verilir.
  - Aynı bant üzerinde bir çok kullanıcı eş zamanlı olarak bulunabilir
  - Kullanıcılara ayrılan data rate değişken yük koşullarına göre ayarlanabilir
- Veriyi geniş bantgenişliğine yaymak jamming ve interception’ı zorlaştırır.

## Spread Spectrum (3)

- Dar bantlı girişim (narrowband interference) örneği: FDM çoklama ile 6 kanal kullanılıyor.
- Frekans planlaması gerekir.
- Kanal kalitesi frekansa bağlıdır; kanal kalitesi o frekanstaki girişimin bir ölçüsüdür.

## Spread Spectrum (4)

- Dar bantlı girişim yüzünden 3. ve 4. kanallardaki sinyal kalitesi çok düşük olduğundan alıcı tarafından doğru alınamaz.
- Çözüm?

## Spread Spectrum (5)

- Narrow band sinyali özel bir kod kullanarak broadband sinyal olarak yay
  - Pseudo-noise (PN) sequence, pseudo-noise code
  - Rasgele gibi görünen ikili dizisi (ancak alıcı tarafından tekrar üretebilir)
- spread spectrum narrowband interference’a karşı dayanıklılığı artırır

## Spread Spectrum (6)

- Bütün narrowband sinyaller aynı (geniş) frekans aralığında broadband sinyal olarak yayılırlar.

## Spread Spectrum (7)

- Boşa harcanan spectrum ne kazandırıyor?
  - Gürültüye karşı dayanım
  - Güvenlik-şifreleme
  - Birçok kullanıcı geniş bir bandı çok az bir girişim ile kullanabilir

## Spread spectrum teknikleri

- İki teknik vardır
  - Frequency Hoping Spread Spectrum (FHSS)
  - Direct Sequence Spread Spectrum (DSSS)

## Frequency Hoping Spread Spectrum (FHSS)
- M adet farklı taşıyıcı girişler tarafından modüle edilir.
- Bir zaman aralığında kaynak sinyal bir taşıyıcıyı modüle eder, diğer zaman aralığında başka bir taşıyıcıyı modüle eder.
- Pseudorandom code generator (pseudorandom noise - PN), k-bit pattern oluşturur. Her pattern, Th (hopping period) süresinde bir hop için kullanılır.

## Frequency Hoping Spread Spectrum (FHSS) (2)
- M = 8 ve k = 3 için frekans tablosundan 8 frekans 3 bitle belirlenmektedir.
  - Oluşturulan k-bit işaretin sırasını bilmeyen kişiler iletişimi takip edemezler.

## Frequency Hoping Spread Spectrum (FHSS) (3)
- Her döngüde tüm frekanslara bir kez atlanır.

## Frequency Hoping Spread Spectrum (FHSS) (4)
- FDM ile FHSS birlikte kullanılabilir.

## Direct Sequence Spread Spectrum (DSSS)
- Her data bit, n adet bitle (chips) değiştirilir.
- Wireless LAN için 11 bit Barker Sequence kullanılır.

## Direct Sequence Spread Spectrum (DSSS) (2)
- Şekilde 11-bit chip olarak 10110111000 kullanılmaktadır.
- Spread sinyal için bant genişliği 11 kat fazla olur.
- Spread kodu bilmeyen kişiler iletişimi anlayamazlar.
- Binary 1 için kodun kendisi, binary 0 için tersi gönderilir.
