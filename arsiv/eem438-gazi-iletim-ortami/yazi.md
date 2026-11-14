---
baslik: EEM438 Veri İletişimi: İletim Ortamı: Büklümlü Çift, Koaksiyel, Fiber ve Kablosuz (Gazi Üniversitesi, Suat Özdemir)
ozet: Gazi Üniversitesi’nden Suat Özdemir’in Veri İletişimi ders slaytları: yönlendirilmiş (büklümlü çift, koaksiyel, fiber optik) ve yönlendirilmemiş iletim ortamları, SDH/SONET.
---

Gazi Üniversitesi Bilgisayar Mühendisliği Bölümü’nden Suat Özdemir’in “Veri İletişimi / Data Communications” dersi için hazırladığı 7. bölüm (İletim ortamı) slaytlarıdır (slayt tarihi 21 Mart 2011; alt bilgide BM 403 Veri İletişimi yazar). EEM438 klasöründe ikinci bir hocanın ders materyali olarak saklanmıştır. Slayt metni aşağıya aktarıldı; kitaptan alınmış şekiller ve tablolar yayımlanmadı, metni olmayan slaytlar belirtildi. Orijinal PDF yazının sonunda indirilebilir.

Kapsam: yönlendirilmiş (büklümlü çift, koaksiyel, fiber optik) ve yönlendirilmemiş iletim ortamları, SDH/SONET.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Giriş

- Transmission media (iletim ortamı), kaynak ile hedef arasında bilgi taşıyan herhangi bir şeydir.
- İletim ortamı, fiziksel katmanın altında yer alır ve fiziksel katman tarafından kontrol edilir.
- İletim ortamı, metal kablo, fiber optik veya boşluk olabilir.
- Uzak mesafelerde elektrik sinyalleriyle iletişim 1900’lerde Morse tarafından telgrafın bulunmasıyla başlamıştır.
- 1869 yılında ilk telefon bulundu.

## Giriş (2)

- Kablosuz iletişim, ilk defa 1895 yılında Hertz tarafından yüksek frekanslı sinyallerle yapılmıştır.
- Daha iyi metal kablolar (twisted pair, koaksiyel kablo) bulundu.
- Fiber optik kullanımı iletişim hızını çok önemli oranda artırmıştır.
- Modülasyon ve multiplex teknikleriyle boşluk veri iletişiminde etkin kullanılmıştır.
- Elektromanyetik spektrum, radyo dalgaları, infrared, görünen ışık, ultraviyole ışık, X, gamma, ... oluşur.

## Guided Media

- Twisted-pair (büklümlü çift) kablo, koaksiyel kablo ve fiber optik kablo guided media olarak adlandırılır.
- Twisted-pair kablo

## Twisted-pair kablo

- Tellerden birisi sinyal taşımak için diğeri ground bağlantısı için kullanılır.
- Büklümlü kabloda noise ikisini aynı oranda etkiler. Alıcı iki tel arasındaki farkı değerlendirir.

## Twisted-pair kablo (2)

- İletişimde genellikle unshielded twisted-pair (UTP) kullanılır. IBM shielded twisted-pair (STP) kablo üretmiştir.
- RJ45 (registered jack 45) konnektör UTP kablolar için kullanılır.

## Twisted-pair kablo (3)

- UTP kabloları EIA (Electronic Industries Association) sınıflandırmıştır.

## Twisted-pair kablo (4)

- Twisted-pair kablonun performansı, frekans ve mesafeye göre attenuation değeriyle ölçülür. Şekilde gauge, AWG numarasını gösterir ve telin kalınlığıyla ilgilidir.

## Twisted-pair kablo (5)

- UTP kablolar, telefon hatlarında ses ve veri iletişiminde kullanılır.
- UTP kablolar, DSL hatlarında yüksek hızda iletişim için kullanılır.
- Twisted-pair kablolar, 10Base-T, 100Base-T gibi yerel alan ağlarında kullanılır.

## Koaksiyel kablo

- Koaksiyel kablo, twisted-pair kablodan daha yüksek frekans aralığında sinyalleri taşır.
- Koaksiyel kablo, merkezde bir iletken bulundurur.

## Koaksiyel kablo (2)

- Koaksiyel kablo, RG (radio government) değerleriyle sınıflandırılır.
- Konnektör olarak BNC (Bayone-Neill-Concelman) kullanılır.

## Koaksiyel kablo (3)

- Koaksiyel kablonun performansı twisted-pair kablodaki gibi ölçülebilir.
- Şekilde, inner conductor/shield çaplarının oranına göre değişimi verilmiştir.

## Koaksiyel kablo (4)

- Koaksiyel kablo, analog telefon ağlarında kullanılır (bir coax kablo 10.000 ses sinyali taşır).
- Sayısal telefon ağlarında kullanılır (bir coax kablo 600 Mbps sayısal veri taşır).
- Kablo TV ağlarında coax kablo (RG-59) kullanılır.
- Ethernet ağlarda kullanılır (10Base-2 ve thin ethernet RG-58 kullanır (10Mbps, 185m), 10Base-5 ve thick ethernet RG-11 kullanır (10Mbps, 5.000m)).

## Fiber optik kablo

- Fiber optik kablo cam veya plastikten yapılır ve ışık sinyalleri iletir.
- Işık farklı yoğunluktaki ortamlardan geçerken yön değiştirir.
- Fiber optik, reflection özelliğiyle ışığı kontrol eder.

## Fiber optik kablo (2)

- Fiber optik kablo ile multimode veya single mode yayılım yapılabilir.
- Multimode, step-index veya graded-index olarak iki türdür.

## Fiber optik kablo (3)

- Multimode yayılımda, çok sayıda ışık kaynaktan farklı yollarla çıkar.
- Multimode step-index fiber’da merkezin (core) yoğunluğu merkezden kenarlara doğru sabittir.
- Multimode graded-index fiber’da merkezin (core) yoğunluğu merkezden kenarlara doğru gidildikçe azalır.
- Single mode fiber’da merkez çapı çok küçüktür ve kaynak ışığı çok iyi odaklanır.

## Fiber optik kablo (4)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Fiber optik kablo (5)

- Fiber optik kabloların boyutu, merkezin çapı ve kenarın çapıyla belirlenir.

## Fiber optik kablo (6)

- Outer jacket, PVC veya teflondan yapılır. Kevlar kablonun dayanıklı olmasını sağlar.
- 3 tür konnektör kullanılır. SC (subscriber connector), kablo TV için kullanılır.
- ST (straight tip) ağ cihazlarına bağlantı için kullanılır kullanılır.
- MT-RJ (Mechanical Transfer Registered Jack), RJ45 ile aynı boyuttadır.

## Fiber optik kablo (7)

- Performans şekildeki gibidir.

## Fiber optik kablo (8)

- Geniş bant genişliğinden dolayı backbone ağlarda kullanılır.
- WDM ile 1600 Gbps(1,6 Tbps) hızında iletişim yapılabilir.
- SONET(Synchronous Optical NETwork) ağlarda kullanılır.
- Yerel alan ağlarında (100Base-FX ve 1000Base-X) fiber optik kablo kullanılır.

## SDH/SONET

- Fiber optik iletişimin hedefi, en uzun mesafeye en fazla veriyi en az kayıpla iletmektir
- Şebekenin sağlamlığı konusunda en kritik husus, kullanıcılara sağlanan hizmetler kesintiye uğramadan, link problemleri ya da şebeke elemanlarında oluşan arızaların bir kaç on milisaniye içerisinde fark edilerek, gerekli tedbirlerin alınmasıdır.

## SDH/SONET (2)

- SDH/SONET teknolojileri yüksek oranda güvenilirlik ve kullanılabilirliğe sahiptir. Servis sağlayıcıları, şebeke üzerinde sağlanan hizmetlerde kullanılabilirlik oranının % 99,99 ile % 99,999 arasında olmasına ihtiyaç duymaktadır.
- Bu oranlar, şebekede yılda ortalama 3 ile 5 dakika arasında kesinti olması anlamına gelmektedir.
- SDH/SONET şebekeleri, karmaşık servis düzenleme mekanizmaları ile bu başarımı sağlamaktadır.

## SDH/SONET (3)

- WDM ile birden fazla data modülasyonlu dalgaboyunu aynı fiberde çoklamak suretiyle, tek bir fiber üzerinde çok sayıda optik kanalı ve eşit veri kapasitelerini taşımak mümkün hale gelmiştir.

## SDH/SONET (4)

- SDH/SONET teknolojisi, artan trafik çeşitliliğine ve ihtiyaçlara paralel olarak, on yıllar içerisinde gelişimini sürdürmüştür.
- Servis sağlayıcıları, tanınan ve güvenirliği ispatlanmış SDH/SONET üzerinde taşınan zaman bölüşümlü çoğullanmış trafik ile beraber Gigabit Ethernet (GE) trafiğini taşımak gereksinimi duymuştur.
- SDH/SONET teknolojisi ATM, ethernet ve TDM trafiğini bir arada taşıyabilmek için yüzünü çoklu servis hizmetlerini sağlayabileceği Gelecek Nesil Şebekelere (Next Generation Networks (NGN)) çevirmiştir

## Fiber optik kablo (9)

- Avantajları
  - Yüksek bantgenişliği
  - Düşük sinyal attenuation
  - Elektromanyetik gürültüden etkilenmez
  - Korozyona karşı daha dirençlidir.
  - Ağırlığı hafiftir.
  - Güvenlidir. Bağlantı noktalarında, bakır kablolardaki gibi anten etkisi oluşturmaz.
- Dezavantajları
  - Kurulum ve işletim için uzman personel gerekir.
  - Işık tek yönlüdür, iki yönlü iletişim için iki fiber optik kablo gerekir.
  - Maliyet yüksektir.

## Unguided media

- Kablosuz ortam elektromanyetik dalgaları fiziksel iletken olmadan taşır.
- Bu tür iletişim kablosuz iletişim (wireless networks) olarak adlandırılır.
- Kablosuz iletişimde kullanılan elektromanyetik spektrum 3kHz-900THz arasındadır.

## Unguided media (2)

- Unguided sinyaller kaynaktan hedefe üç şekilde yayılır: ground propagation, sky propagation ve line-of-sight(LOS).

## Ground Wave Propagation

- Yer kabuğunu takip eder
  - Elektro manyetik dalgalar yerkabuğu üzerinde akım oluşturur, sinyali yavaşlatır ve büker
  - Diffraction (dağılarak kırılma)
- Çok uzun mesafelerde yol alabilir
- 2 Mhz kadar olan frekanslarda kullanılır
- Örnek
  - AM radio

## Sky Wave Propagation

- Sinyal atmosferdeki iyonosfer tabakası ve yerkabuğu arasında yansıtılır
- Sinyal iyonosfer tabakası ve yerkabuğu arasında birçok kez gidip gelebilir
- Yansıma etkisi ışın kırılmasıyla oluşur
- Örnek
  - Amatör radio (telsiz iletişimi)
  - BBC international, Voice of America

## Görüş çizgisi yayılma (Line-of-Sight Propagation)
- Sinyal yayan ve alan antenler mutlaka birbirlerinin görüş alanı içinde olmalıdırlar
  - Uydu iletişimi – 30 MHz in üzerindeki sinyaller iyonosfer tarafından yansıtılmaz
  - Yer iletişimi (ground communication) – antenler birbirlerinin etkin görüş alanı içindedirler

## Etkin (radio) görüş çizgisi

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Görüş Çizgisi Eşitlikleri

- Optik görüş çizgisi - optical line of sight d = 3.57 √h
- Etkin ya da radyo görüş çizgisi - Effective, or radio, line of sight d = 3.57 √(K·h)
- d = anten ve ufuk çizgisi arasındaki mesafe (km)
- h = anten yüksekliği (m)
- K = kırılma faktörü, genel kural K = 4/3

## Görüş Çizgisi Eşitlikleri (2)

- Görüş Çizgisi (LOS) için iki anten arasındaki maksimum mesafe. d = 3.57 (√(K·h1) + √(K·h2))
- h1 = 1. antenin yüksekliği
- h2 = 2. antenin yüksekliği

## Unguided media (3)

- Elektromanyetik spektrumda mikrodalga ve radyo dalgaları 8 kısımda gösterilir.

## Unguided media (4)

- Kablosuz iletişim üç gruba ayrılır: radio dalgaları, mikrodalgalar ve infrared dalgalar.

## Unguided media (5)

- Radio dalgaları
  - Elektromanyetik dalga frekansları 3 kHz- 1GHz arasında ise radyo dalgası, 1 GHz-300 GHz arasında ise mikrodalga olarak adlandırılır.
  - Radyo dalgaları omnidirectional (her yöne) yayılır.
  - Alıcı ve verici antenlerin hizalandırılması gerekmez.
  - Radyo dalgaları sky mod yayılırlar ve uzak mesafelere gidebilirler.
  - AM radyolar radyo dalgaları kullanır.

## Unguided media (6)

- Mikro dalgalar
  - 1 GHz-300 GHz arasındaki banda sahiptir.
  - Mikrodalga unidirectional (tek yönlü) yayılır.
  - Alıcı ve verici antenler hizalandırılmalıdır. Mikrodalgalar LOS yayılır.
  - Uzun mesafelerde repeater gereklidir.
  - Çok yüksek frekanslardaki mikrodalgalar duvarlardan geçemez.
  - Parabolik çanak anten veya horn anten kullanılır.

## Unguided media (7)

- Infrared dalgalar
  - 300 GHz-400 THz (1mm-770nm dalga boyu) arasındaki banda sahiptir.
  - Kısa mesafedeki iletişimde kullanılır.
  - Duvarlardan geçemez.
  - Kapalı ortamlarda kullanılır.
  - Bilgisayarda IrDA (Infrared Data Association) portu klavye, mouse veya printer bağlantısı için kulanılır.
  - LOS iletişim yapılır.

*Not: Görüş çizgisi formüllerindeki karekök işaretleri PDF metninde kaybolmuştu; d = 3,57·√(K·h) biçiminde geri yazıldı.*
