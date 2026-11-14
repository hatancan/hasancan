---
baslik: EEM438 Veri İletişimi: Ağ Modelleri: OSI, TCP/IP ve Adresleme (Gazi Üniversitesi, Suat Özdemir)
ozet: Gazi Üniversitesi’nden Suat Özdemir’in Veri İletişimi ders slaytları: OSI ve TCP/IP katman modelleri, her katmanın görevleri ve fiziksel, mantıksal, port ve özel adresleme.
---

Gazi Üniversitesi Bilgisayar Mühendisliği Bölümü’nden Suat Özdemir’in “Veri İletişimi / Data Communications” dersi için hazırladığı 2. bölüm (Ağ Modelleri) slaytlarıdır (slayt tarihi 4 Mart 2011; alt bilgide BM 403 Veri İletişimi yazar). EEM438 klasöründe ikinci bir hocanın ders materyali olarak saklanmıştır. Slayt metni aşağıya aktarıldı; kitaptan alınmış şekiller ve tablolar yayımlanmadı, metni olmayan slaytlar belirtildi. Orijinal PDF yazının sonunda indirilebilir.

Kapsam: OSI ve TCP/IP katman modelleri, her katmanın görevleri ve fiziksel, mantıksal, port ve özel adresleme.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Ağ Modelleri

- Bir ağ bir noktadan diğer bir noktaya veri ileten donanım ve yazılımların tümüdür.
- Donanım fiziksel elemanlardan, yazılım ise komut kümelerinden oluşur.
- Bir verinin bir noktadan diğerine iletilmesi çok sayıda iş parçasına bölünebilir.
- Her iş katmanlar (layers) halinde gösterilebilir. Örnek: posta ile mektup gönderimi.
- Bilgisayar ağlarında 1990 yılına kadar OSI (Open Systems Interconnection) modeli yaygın kullanılmıştır.

## Ağ modelleri

- Geleneksel yolla posta gönderimi.

## OSI modeli

- Bir açık sistem (open system) iki sistemin altyapılarına bağlı kalmaksızın iletişimini sağlayan protokoller kümesidir.
- OSI bir protokol değildir ! OSI bir ağ mimarisinin tasarlanması ve anlaşılmasında kullanılan modeldir
- OSI birbirinden ayrı ancak ilişkide olan 7 katmandan oluşur.
- Her katman iletişim için kendisine atanmış bazı işlemleri yapar.

## OSI modeli (2)

- A ve B arasında veri giderken aradaki bir çok node’dan geçebilir.
- Her katman bir altındakinden hizmet alır ve bir üstündekine hizmet sunar.
- Cihazlar arasında, aynı seviyedeki katmanlar kendi arasında haberleşir (peer-to-peer process).
- Her katman kendi bilgisini pakete ekler ve bir alt katmana gönderir. Alıcı her katmanda kendi bilgisini açarak üst katmana iletir.
- Komşu katmanlar arasında arayüzler (interface) vardır.
- Arayüzler modülerlik sağlar.

## OSI katmanları arasında etkileşim

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## OSI modeli katmanlar

- Katmanlar 3 grupta toplanır. Network support layers (fiziksel, data link ve network), user support layers (oturum, sunuş ve uygulama) ve transport layer iki grubu birbirine bağlar.
- Üst katmanlar hemen hemen tümüyle yazılımla gerçekleştirilir, alt katmanlar ise genellikle yazılım ve donanımla gerçekleştirilir. Fiziksel katman çoğunlukla donanımla gerçekleştirilir.
- Her katmanda veriye header ve/veya trailer eklenir. Trailer data link katmanında eklenir.
- Her katman üst katmandaki verinin tümünü (header, trailer, data) data olarak alır. (Encapsulation)

## OSI modeli katmanlar (2)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## OSI modeli - Physical layer

- Fiziksel ortamda bitlerin taşınması için gerekli işlemler gerçekleştirilir.
- Arayüz ve iletim ortamının mekaniksel, elektriksel özellikleri belirlenir.
- Bitlerin gösterimi tanımlanır. Bitlerin sinyallerle ifade ediliş şeklini (encode) belirler.
- Data rate belirlenir. (bps)
- Alıcı ve gönderici arasında bit seviyesinde senkronizasyon yapılır.
- Point-to-point veya multipoint line konfigürasyonu belirlenir.
- Topoloji tanımlanır. (mesh, star, bus, ring)
- İletim modu tanımlanır. (simplex, half-duplex, full-duplex)

## OSI modeli - Data link layer

- Fiziksel katmandaki basit veri iletimini güvenilir bağlantıya çevirir.
- Network layer’dan gelen bitleri frame’lere böler.
- Fiziksel adresleme yapar. Frame’lere header (alıcı ve verici adresleri) ve trailer (hata kontrol bilgisi) ekler.
- Frame bazında akış kontrolü yapar.
- Hata denetimi yapar. Kaybolan ve bozulan frame’ler yeniden gönderilir (retransmit).
- Erişim denetimi yapar. Tek bağlantı üzerindeki cihazların paylaşımını denetleyen protokol çalıştırılır.

## OSI modeli - Data link layer (2)

- Hop-to-hop (node-to-node) iletim yapar.
- Şekilde A ile F arasında veri gönderimi görülmektedir.

## OSI model – Network layer

- Birden fazla ağdan geçerek source-to-destination paket gönderimden sorumludur.
- Data link katmanı aynı ağdaki iki node arasında veri iletimi yaparken, network katmanı iki ağ arasında veri iletimi yapar.

## OSI model - Network layer

- Logical addressing (mantıksal adresleme) yapar. Alıcı ve göndericinin mantıksal adresleri pakete eklenir.
- Routing yapar. Paketlerin farklı ağlardan geçmesi sırasında yönlendirme yapar.

## OSI model - Transport layer

- Tüm mesajın process-to-process gönderimden sorumludur. Bir process uygulama programıdır.
- Network layer gönderilen paketler arasında ilişki oluşturmaz. Transport layer tüm mesajı oluşturmaz. Sıralar, hata denetimi ve akış denetimi yapar.

## OSI model - Transport layer (2)

- Service-point adresleme yapar. Her uygulama için adresleme (port) yapar.
- Segmentation ve reassembly yapar. Mesaj iletilebilecek segmentlere bölünür ve sıra numarası verilir.
- Connection-oriented (TCP) ve connectionless (UDP) iletişim yapar.
- Tüm mesaj için end-to-end akış kontrolü yapar, data link layer bir bağlantı için yapar.
- Tüm mesaj için process-to-process hata denetimi yapar.

## OSI model - Session layer

- Dialog kontrolörü görevi yapar.
- Process tarafından veriye checkpoint eklenmesini sağlar (senkronizasyon). Bir hata oluştuğunda en son doğru giden kısımdan itibaren yeniden gönderim yapılır.
- İki sistemin half duplex veya full duplex diyalog yapmasını sağlar.
  - Örnek: 1000 sayfalık bir dökümanın gönderilmesi?

## OSI model - Presentation layer

- İki sistem arasında iletilen verinin syntax ve semantics özelliklerini belirler.
- Translation. Farklı bilgisayarlar farklı kodlama teknikleri kullandığından gönderen bilgisayar bilgiyi ortak bir formata çevirir
  - char string → bit stream
- Encryption. Bilginin gizliliğini ve güvenliğini sağlamak için şifreler.
- Compression. Ağ trafiğini azaltmak için veri daha az bitle ifade edilir.

## OSI model - Application layer

- e-mail, uzak erişim, dosya transferi, veritabanı yönetimi veya dağıtık uygulamalar için kullanıcı arayüzlerini sağlar.
- X.400 mesaj alma (e mail) hizmeti, X.500 dizin hizmeti, FTAM (file transfer and management) hizmeti vb. hizmetleri sunar.

## TCP/IP Protocol Architecture

- TCP/IP, ARPANET üzerinde yürütülen protokol araştırma ve geliştirme çalışmalarının sonucudur; “TCP/IP protocol suite” olarak anılır ve İnternet standardı olan çok sayıda protokolden oluşur.
- OSI modelinden önce geliştirildiği için katmanlar farklıdır.
- Orijinal TCP/IP’de 4 katman vardır. (host-to-network, internet, transport ve TCP/IP protokol kümesi application)
- Host-to-network layer, OSI’de physical ve data link layer’ın birleşimine eşittir.
- Internet layer, OSI’de network layer’a eşittir.
- Application layer, OSI’de session, presentation ve application layer’a eşit.
- Sonuç olarak, günümüzde TCP/IP 5 katman olarak tanımlanır: physical, data link, network, transport ve application.

## TCP/IP protokolü

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## TCP/IP protokolü (2)

- Physical ve data link katmanları herhangi özel bir protokolü desteklemez.
- Network katmanı IP (Internetworking Protocol)nı destekler. IP Datagram’ların yönlendirilmesi ve best-effort (hata denetimi yapmaz) gönderimini yapar.
- ARP (Address Resolution Protocol). Mantıksal adresi fiziksel adresle ilişkilendirir.
- RARP (Reverse Address Resolution Protocol). Sadece fiziksel adresini bilen host için Internet adresi atar. (Disksiz bilgisayar)
- ICMP (Internet Control Message Protocol). Datagram’lardaki problemlerin gönderene bildirilmesi için kullanılır.

## TCP/IP protokolü (3)

- IGMP (Internet Group Message Protocol). Eşzamanlı bir grup mesaj göndermek için kullanılır.
- Transport katmanı UDP ve TCP yi destekler. UDP (User Datagram Protocol). Sadece port adresi, hata denetim bitleri ve bilgi boyutunu pakete ekler. Connectionless çalışır. (ping)
- TCP (Transmission Control Protocol). Güvenilirdir ve connection oriented çalışır. Veriyi segmentlere böler, sıralar, sırayı denetler.
- SCTP (Stream Control Transmission Protocol). Yeni Internet uygulamalarını sağlar (VoIP). UDP ve TCP’nin birleşimidir.

## Adresleme

- TCP/IP protokol kümesiyle fiziksel (physical), mantıksal (logical), port ve özel (specific) olarak 4 seviyeli adresleme yapılır.

## Adresleme - Fiziksel adresleme

- Data link layer’da frame içinde bulunur. Ağ yapısına göre farklı uzunluktadır. (Ethernet için 6 byte NIC, LocalTalk Apple için 1 byte)

## Adresleme - Mantıksal adresleme

- Adres bilgisi network layer’da paket içinde bulunur.
- Internet için 32 bit boyutundadır (IPv4)
- IPv6 128 bit adresleme yapar.

## Adresleme - Mantıksal adresleme (2)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Adresleme - Port adresleme

- IP adresi ve fiziksel adres bilgisayarlar arasında source-to-destination iletişim için yeterlidir.
- Ancak günümüzde bilgisayarlar aynı anda birden fazla program çalıştırabilir.
- TCP/IP’de port adresi her uygulama için atanır ve 16-bit (0-65535) uzunluğundadır.
- Fiziksel adres hop-to-hop değişir, mantıksal ve port adresi sabit kalır.

## Adresleme - Port adresleme (2)

*Bu slayt yalnızca şekil/tablo içerir; görsel orijinal PDF'te yer alır.*


## Adresleme - Özel adresleme

- Bazı uygulamalar kullanıcı için kolay adreslemeler yapar. (forouzan@fhda.edu, www.mhhe.com)
- Özel adresler port adreslerine ve mantıksal adreslere dönüştürülür
