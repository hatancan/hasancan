---
baslik: EEM438 Veri İletişimi: Çoklu Ortam, RTP ve QoS: İkinci Not Takımı
ozet: Çoklu Ortam, RTP ve QoS: İkinci Not Takımı. Ders arşivinden soru, açıklama ve belgeler.
---


## UDP/TCP, RTSP ve Internet telefonu

UDP akışında gönderim hızı uygulamaya aittir; TCP güvenilir aktarım ve tıkanıklık kontrolü sağlar. RTSP oynatma ve duraklatma gibi kontrol işlemlerini yürütür. İnternet telefonunda sessizlik bastırılabilir; konuşma küçük ses parçalarına bölünür. Jitter tamponu ve oynatma gecikmesi zaman değişimini karşılar.

![UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 1](belge-298-sayfa-01.jpg "UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 1")

![UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 2](belge-298-sayfa-02.jpg "UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 2")

![UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 3](belge-298-sayfa-03.jpg "UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 3")

![UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 4](belge-298-sayfa-04.jpg "UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 4")

![UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 5](belge-298-sayfa-05.jpg "UDP/TCP, RTSP ve Internet telefonu — el yazısı, sayfa 5")

## FEC, serpiştirme ve CDN

FEC ek veri kullanarak kaybı telafi eder. XOR yaklaşımı bir grup içindeki tek kaybı kurtarabilir; düşük hızlı ses kopyası bir sonraki pakette taşınabilir. Serpiştirme aynı ses parçasını farklı paketlere dağıtır. CDN içeriği farklı sunuculara çoğaltır; istemci uygun kopyaya yönlendirilir.

![FEC, serpiştirme ve CDN — el yazısı, sayfa 6](belge-298-sayfa-06.jpg "FEC, serpiştirme ve CDN — el yazısı, sayfa 6")

![FEC, serpiştirme ve CDN — el yazısı, sayfa 7](belge-298-sayfa-07.jpg "FEC, serpiştirme ve CDN — el yazısı, sayfa 7")

![FEC, serpiştirme ve CDN — el yazısı, sayfa 8](belge-298-sayfa-08.jpg "FEC, serpiştirme ve CDN — el yazısı, sayfa 8")

## RTP, RTCP ve SIP

RTP sıra, yük türü ve zaman damgası taşır; UDP içinde taşınabilir, QoS garantisi vermez. 8 kHz örneklemede Tₛ = 1/8000 s = 125 µs; 20 ms ses için 160 örnek vardır. 8 bit/örnek PCM’de bu 160 bayttır. RTCP kayıp ve jitter raporlarını taşır, akışları eşzamanlar. SIP, INVITE ve yanıtlarla oturum kurar; registrar konumu, proxy sinyalleşme yolunu yönetir.

![RTP, RTCP ve SIP — el yazısı, sayfa 9](belge-298-sayfa-09.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 9")

![RTP, RTCP ve SIP — el yazısı, sayfa 10](belge-298-sayfa-10.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 10")

![RTP, RTCP ve SIP — el yazısı, sayfa 11](belge-298-sayfa-11.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 11")

![RTP, RTCP ve SIP — el yazısı, sayfa 12](belge-298-sayfa-12.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 12")

![RTP, RTCP ve SIP — el yazısı, sayfa 13](belge-298-sayfa-13.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 13")

![RTP, RTCP ve SIP — el yazısı, sayfa 14](belge-298-sayfa-14.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 14")

## DiffServ, IntServ ve RSVP

DiffServ kenarda akışları işaretler, çekirdekte sınıf tabanlı davranış uygular. PHB sınıfın yönlendiricide gördüğü hizmettir. IntServ uygulama gereksinimi için kaynak ayırır; çağrı kabulü mevcut yük ve yeni isteği değerlendirir. Token bucket ve WFQ şemasında r hız, b kova kapasitesidir; b/R gecikme sınırı gösterilir.

RSVP rezervasyon bilgisini taşır. Path ve reservation mesajları, multicast desteği ve teardown anlatılır. RSVP yönü seçmez; yönlendirme ile veri iletiminin yerini almaz.

![DiffServ, IntServ ve RSVP — el yazısı, sayfa 1](belge-297-sayfa-01.jpg "DiffServ, IntServ ve RSVP — el yazısı, sayfa 1")

![DiffServ, IntServ ve RSVP — el yazısı, sayfa 2](belge-297-sayfa-02.jpg "DiffServ, IntServ ve RSVP — el yazısı, sayfa 2")

![DiffServ, IntServ ve RSVP — el yazısı, sayfa 3](belge-297-sayfa-03.jpg "DiffServ, IntServ ve RSVP — el yazısı, sayfa 3")

![DiffServ, IntServ ve RSVP — el yazısı, sayfa 4](belge-297-sayfa-04.jpg "DiffServ, IntServ ve RSVP — el yazısı, sayfa 4")

![DiffServ, IntServ ve RSVP — el yazısı, sayfa 5](belge-297-sayfa-05.jpg "DiffServ, IntServ ve RSVP — el yazısı, sayfa 5")

![DiffServ, IntServ ve RSVP — el yazısı, sayfa 6](belge-297-sayfa-06.jpg "DiffServ, IntServ ve RSVP — el yazısı, sayfa 6")

![DiffServ, IntServ ve RSVP — el yazısı, sayfa 7](belge-297-sayfa-07.jpg "DiffServ, IntServ ve RSVP — el yazısı, sayfa 7")

*Not: Notlarda interleaving için gecikmenin küçüldüğü yönünde ifade vardır; parça yeniden birleştirme ek bekleme gerektirir. RTP’nin QoS garantisi olmaması, protokolün hata/durum raporlaması yapılamadığı anlamına gelmez.*

