---
baslik: EEM438 Veri İletişimi: Kablosuz Ağlar ve Çoklu Ortam Vize Notları
ozet: Kablosuz Ağlar ve Çoklu Ortam Vize Notları. Ders arşivinden soru, açıklama ve belgeler.
---


## Kablosuz bağlantı, SNR ve CDMA

Kablosuz olmak ile hareketli olmak aynı değildir. Baz istasyonu altyapıya erişim sağlar; ad hoc yapıda merkezî baz istasyonu yoktur. Handoff bağlantı sürerken baz istasyonu değiştirmektir. Zayıflama, girişim ve çok yollu yayılım kablosuz kanalı etkiler. SNR sinyal/gürültü oranı, BER bit hata oranıdır.

Gizli terminal örneğinde birbirini duymayan A ve C, B’ye aynı anda göndererek çarpışabilir. CDMA kullanıcıları farklı kodlarla ayırır; alıcı kodla korelasyon yapar.

![Kablosuz bağlantı, SNR ve CDMA — el yazısı, sayfa 1](belge-295-sayfa-01.jpg "Kablosuz bağlantı, SNR ve CDMA — el yazısı, sayfa 1")

![Kablosuz bağlantı, SNR ve CDMA — el yazısı, sayfa 2](belge-295-sayfa-02.jpg "Kablosuz bağlantı, SNR ve CDMA — el yazısı, sayfa 2")

![Kablosuz bağlantı, SNR ve CDMA — el yazısı, sayfa 3](belge-295-sayfa-03.jpg "Kablosuz bağlantı, SNR ve CDMA — el yazısı, sayfa 3")

## 802.11, tarama ve CSMA/CA

BSS erişim noktası çevresindeki hizmet kümesidir; SSID ağı tanımlar. Pasif taramada beacon dinlenir, aktif taramada probe gönderilir. İlişkilendirme istek ve cevapla tamamlanır. CSMA/CA boş kanalda DIFS sonrasında gönderir; meşgul kanalda rastgele geri çekilme kullanır. ACK, SIFS sonrasında gelir.

RTS/CTS kanalı ayırmak ve gizli terminal etkisini azaltmak içindir; RTS paketleri yine çarpışabilir. Çerçevede kontrol, süre, adresler, sıra kontrolü, yük ve CRC alanları çizilmiştir. Güç yönetiminde erişim noktası uyuyan istemcinin verisini tamponlar.

![802.11, tarama ve CSMA/CA — el yazısı, sayfa 4](belge-295-sayfa-04.jpg "802.11, tarama ve CSMA/CA — el yazısı, sayfa 4")

![802.11, tarama ve CSMA/CA — el yazısı, sayfa 5](belge-295-sayfa-05.jpg "802.11, tarama ve CSMA/CA — el yazısı, sayfa 5")

![802.11, tarama ve CSMA/CA — el yazısı, sayfa 6](belge-295-sayfa-06.jpg "802.11, tarama ve CSMA/CA — el yazısı, sayfa 6")

![802.11, tarama ve CSMA/CA — el yazısı, sayfa 7](belge-295-sayfa-07.jpg "802.11, tarama ve CSMA/CA — el yazısı, sayfa 7")

![802.11, tarama ve CSMA/CA — el yazısı, sayfa 8](belge-295-sayfa-08.jpg "802.11, tarama ve CSMA/CA — el yazısı, sayfa 8")

## Hücresel ağlar ve Mobile IP

2G ses, 2.5G paket veri, 3G ses ve verinin birlikte taşınması bağlamında karşılaştırılır. Şemalarda BSC, MSC, SGSN ve GGSN yer alır. FDMA/TDMA ve CDMA yöntemleri not edilir.

Mobile IP için home network, permanent address, care-of address, home agent, foreign agent ve correspondent tanımlanır. Dolaylı yönlendirmede veri home agent üzerinden tünellenir. Doğrudan yönlendirmede muhatap geçici adresi öğrenir. Agent discovery, home agent’a registration ve indirect routing üç temel bileşendir.

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 9](belge-295-sayfa-09.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 9")

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 10](belge-295-sayfa-10.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 10")

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 11](belge-295-sayfa-11.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 11")

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 12](belge-295-sayfa-12.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 12")

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 13](belge-295-sayfa-13.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 13")

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 14](belge-295-sayfa-14.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 14")

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 15](belge-295-sayfa-15.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 15")

![Hücresel ağlar ve Mobile IP — el yazısı, sayfa 16](belge-295-sayfa-16.jpg "Hücresel ağlar ve Mobile IP — el yazısı, sayfa 16")

## Çoklu ortam, akış ve RTSP

QoS hizmet kalitesidir. Çoklu ortam saklanmış akış, canlı akış ve etkileşimli gerçek zamanlı iletişim olarak sınıflanır. Jitter paket gecikmelerinin değişmesidir. Alıcı tamponu ve geciktirilmiş oynatma dalgalanmayı yumuşatır.

Sunum dosyası/metafile ortamın nerede olduğunu ve oynatıcı bilgilerini taşır. UDP gönderici hızını uygulamaya bırakır; TCP tıkanıklık ve yeniden iletim nedeniyle değişken geliş hızı oluşturabilir. RTSP oynatma, duraklatma ve oturum kontrolüdür; ortam verisinin hangi taşıma protokolünü kullanacağını tek başına belirlemez. Kaynakta RTSP kontrol portu 554 verilmiştir.

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 17](belge-295-sayfa-17.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 17")

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 18](belge-295-sayfa-18.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 18")

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 19](belge-295-sayfa-19.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 19")

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 20](belge-295-sayfa-20.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 20")

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 21](belge-295-sayfa-21.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 21")

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 22](belge-295-sayfa-22.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 22")

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 23](belge-295-sayfa-23.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 23")

![Çoklu ortam, akış ve RTSP — el yazısı, sayfa 24](belge-295-sayfa-24.jpg "Çoklu ortam, akış ve RTSP — el yazısı, sayfa 24")

## Oynatma gecikmesi ve kayıp telafisi

tᵢ üretim, rᵢ alınma, pᵢ oynatma zamanıdır. Ağ gecikmesi rᵢ−tᵢ’dir.

- dᵢ = (1−u)dᵢ₋₁ + u(rᵢ−tᵢ)
- vᵢ = (1−u)vᵢ₋₁ + u|rᵢ−tᵢ−dᵢ|
- Konuşma başlangıcında pᵢ = tᵢ + dᵢ + Kvᵢ.

Oynatma tamponunu büyütmek geç gelen paket kaybını azaltır, etkileşimi geciktirir. FEC’de n paketin XOR’undan ek paket üretilir. Piggybacking önceki ses parçasının düşük kaliteli kopyasını sonraki pakete ekler. Interleaving küçük parçaları paketler arasında dağıtarak kaybın etkisini yayar, ancak bekleme ekler.

![Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 25](belge-295-sayfa-25.jpg "Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 25")

![Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 26](belge-295-sayfa-26.jpg "Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 26")

![Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 27](belge-295-sayfa-27.jpg "Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 27")

![Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 28](belge-295-sayfa-28.jpg "Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 28")

![Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 29](belge-295-sayfa-29.jpg "Oynatma gecikmesi ve kayıp telafisi — el yazısı, sayfa 29")

## RTP, RTCP ve SIP

RTP ortamın payload type, sıra numarası, zaman damgası ve SSRC bilgilerini taşır; zamanında teslim veya bant genişliği garantisi vermez. 64 kbit/s PCM’de 20 ms ses, 160 bayt eder. 8 kHz örneklemede örnek aralığı 125 µs’dir.

RTCP alıcı ve gönderici raporlarıyla kayıp, jitter ve zamanlama bilgisi sağlar; ses ve görüntü akışlarının eşzamanlanmasına yardım eder. Notta oturum bant genişliğinin %5’i RTCP’ye, bunun %75’i alıcılara ve %25’i göndericilere ayrılır. SIP oturum başlatma ve yönetim protokolüdür; INVITE, yanıt, ACK, registrar ve proxy örnekleri çizilmiştir.

![RTP, RTCP ve SIP — el yazısı, sayfa 30](belge-295-sayfa-30.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 30")

![RTP, RTCP ve SIP — el yazısı, sayfa 31](belge-295-sayfa-31.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 31")

![RTP, RTCP ve SIP — el yazısı, sayfa 32](belge-295-sayfa-32.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 32")

![RTP, RTCP ve SIP — el yazısı, sayfa 33](belge-295-sayfa-33.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 33")

![RTP, RTCP ve SIP — el yazısı, sayfa 34](belge-295-sayfa-34.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 34")

![RTP, RTCP ve SIP — el yazısı, sayfa 35](belge-295-sayfa-35.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 35")

![RTP, RTCP ve SIP — el yazısı, sayfa 36](belge-295-sayfa-36.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 36")

![RTP, RTCP ve SIP — el yazısı, sayfa 37](belge-295-sayfa-37.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 37")

![RTP, RTCP ve SIP — el yazısı, sayfa 38](belge-295-sayfa-38.jpg "RTP, RTCP ve SIP — el yazısı, sayfa 38")

## QoS, kuyruklama ve kaynak ayırma

H.323, çoklu hizmet sınıfları ve paket işaretleme anlatılır. FIFO, öncelik, round-robin ve Weighted Fair Queuing karşılaştırılır. Trafik denetimi average rate, peak rate ve burst size ile açıklanır. Token bucket birikmiş belirteçlerle patlamalı trafiğe izin verir.

DiffServ’de kenar yönlendirici sınıflandırma ve işaretleme, çekirdek yönlendirici sınıfa göre iletim yapar. PHB davranışları expedited ve assured forwarding başlıklarında ele alınır. IntServ kaynak ayırma ve çağrı kabulü kullanır; R-spec hizmet isteğini, T-spec trafik özelliklerini bildirir. RSVP sinyalleşir, yönlendirme algoritmasının yerini almaz.

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 39](belge-295-sayfa-39.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 39")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 40](belge-295-sayfa-40.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 40")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 41](belge-295-sayfa-41.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 41")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 42](belge-295-sayfa-42.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 42")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 43](belge-295-sayfa-43.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 43")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 44](belge-295-sayfa-44.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 44")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 45](belge-295-sayfa-45.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 45")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 46](belge-295-sayfa-46.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 46")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 47](belge-295-sayfa-47.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 47")

![QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 48](belge-295-sayfa-48.jpg "QoS, kuyruklama ve kaynak ayırma — el yazısı, sayfa 48")


