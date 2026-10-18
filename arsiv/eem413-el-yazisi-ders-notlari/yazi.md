---
baslik: EEM413 Bilgisayar Ağları: El Yazısı Ders Notları: İnternetten VLAN’a
ozet: El Yazısı Ders Notları: İnternetten VLAN’a. Ders arşivinden soru, açıklama ve belgeler.
---


## İnternet, protokoller ve erişim ağları

Protokoller, mesajların biçimini, sırasını ve mesaj alındığında yapılacak işlemleri tanımlar. RFC belgeleri ve IETF, İnternet standartlarının geliştirilmesiyle ilişkilidir. Ağın kenarında uç sistemler; çekirdeğinde yönlendiriciler vardır. İstemci–sunucu ve P2P uygulama mimarileri karşılaştırılır.

Erişim örnekleri çevirmeli bağlantı, DSL, kablo/HFC, FTTH ve kablosuz bağlantıdır. DSLAM, DSL hatlarını servis sağlayıcı tarafında toplar. FTTH şemasında OLT, optik dağıtım ve ONT yer alır. PON pasif, AON aktif optik dağıtımdır. Fiziksel ortamlar bükümlü çift, koaksiyel, fiber ve radyo olarak sıralanır.

![İnternet, protokoller ve erişim ağları — el yazısı, sayfa 2](belge-105-sayfa-02.jpg "İnternet, protokoller ve erişim ağları — el yazısı, sayfa 2")

![İnternet, protokoller ve erişim ağları — el yazısı, sayfa 3](belge-105-sayfa-03.jpg "İnternet, protokoller ve erişim ağları — el yazısı, sayfa 3")

![İnternet, protokoller ve erişim ağları — el yazısı, sayfa 4](belge-105-sayfa-04.jpg "İnternet, protokoller ve erişim ağları — el yazısı, sayfa 4")

![İnternet, protokoller ve erişim ağları — el yazısı, sayfa 5](belge-105-sayfa-05.jpg "İnternet, protokoller ve erişim ağları — el yazısı, sayfa 5")

## Paket ve devre anahtarlama

Devre anahtarlamada bağlantı boyunca kaynak ayrılır; FDM frekansı, TDM zamanı paylaştırır. Paket anahtarlamada bağlantı kaynakları paketler arasında paylaşılır.

Örnekte 640.000 bit, 1,536 Mbit/s hat ve 24 zaman dilimi vardır. Kullanıcı hızı 1.536.000/24 = 64.000 bit/s; iletim 10 saniye, 0,5 saniyelik kurulumla toplam 10,5 saniyedir.

![Paket ve devre anahtarlama — el yazısı, sayfa 6](belge-105-sayfa-06.jpg "Paket ve devre anahtarlama — el yazısı, sayfa 6")

![Paket ve devre anahtarlama — el yazısı, sayfa 7](belge-105-sayfa-07.jpg "Paket ve devre anahtarlama — el yazısı, sayfa 7")

## Uygulama gereksinimleri, TCP ve UDP

Uygulamalar veri kaybına tolerans, zamanlama, aktarım hızı ve güvenlik gereksinimleriyle karşılaştırılır. TCP güvenilir aktarım, akış ve tıkanıklık kontrolü sağlar. UDP bağlantı kurmadan datagram gönderir; teslim, sıralama ve bant genişliği garantisi vermez.

*Not: TCP de mutlak zamanlama veya asgari hız garantisi vermez. Kaynaktaki hata sorumluluğuna ilişkin kısa ifadeler protokolün hata denetimi ve yeniden iletim işlevlerini dışlamaz.*

![Uygulama gereksinimleri, TCP ve UDP — el yazısı, sayfa 8](belge-105-sayfa-08.jpg "Uygulama gereksinimleri, TCP ve UDP — el yazısı, sayfa 8")

![Uygulama gereksinimleri, TCP ve UDP — el yazısı, sayfa 9](belge-105-sayfa-09.jpg "Uygulama gereksinimleri, TCP ve UDP — el yazısı, sayfa 9")

## HTTP, çerezler, önbellek ve FTP

HTTP istemci–sunucu istek/yanıt modeliyle anlatılır. Kalıcı ve kalıcı olmayan bağlantılar, RTT ve nesne aktarım süresi karşılaştırılır. İstek satırı ve Host, User-Agent, Connection, Accept-Language başlıkları gösterilir. GET, POST, HEAD, PUT ve DELETE yöntemleri listelenir.

Durum kodu örnekleri 200 OK ve 301 Moved Permanently’dir. Çerezler durum bilgisinin sürdürülmesine, web önbelleği gecikmenin ve erişim trafiğinin azaltılmasına yardım eder. Conditional GET, nesne değişmediyse yeniden indirmeyi önler. FTP kontrol bağlantısı ile veri bağlantısını ayırır; notta kontrol için 21, aktif veri için 20 portu verilmiştir.

![HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 10](belge-105-sayfa-10.jpg "HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 10")

![HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 11](belge-105-sayfa-11.jpg "HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 11")

![HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 12](belge-105-sayfa-12.jpg "HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 12")

![HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 13](belge-105-sayfa-13.jpg "HTTP, çerezler, önbellek ve FTP — el yazısı, sayfa 13")

## E-posta ve DNS

E-posta kullanıcı aracıları, posta sunucuları ve SMTP ile açıklanır. Gönderici sunucudan alıcı sunucuya SMTP kullanılır. POP3 ve IMAP posta kutusuna erişim içindir; web tabanlı erişim HTTP kullanabilir. IMAP klasörleri sunucu üzerinde yönetir.

DNS ad–adres çözümlemesini dağıtık olarak yapar. Kök, üst düzey alan ve yetkili sunucular ile yinelemeli sorgu çizilmiştir. Kaynak kaydı biçimi (name, value, type, TTL) olarak verilir.

![E-posta ve DNS — el yazısı, sayfa 14](belge-105-sayfa-14.jpg "E-posta ve DNS — el yazısı, sayfa 14")

![E-posta ve DNS — el yazısı, sayfa 15](belge-105-sayfa-15.jpg "E-posta ve DNS — el yazısı, sayfa 15")

![E-posta ve DNS — el yazısı, sayfa 16](belge-105-sayfa-16.jpg "E-posta ve DNS — el yazısı, sayfa 16")

![E-posta ve DNS — el yazısı, sayfa 17](belge-105-sayfa-17.jpg "E-posta ve DNS — el yazısı, sayfa 17")

![E-posta ve DNS — el yazısı, sayfa 18](belge-105-sayfa-18.jpg "E-posta ve DNS — el yazısı, sayfa 18")

## P2P dağıtımı ve DHT

F dosya boyutu, N alıcı sayısı, uₛ sunucunun yükleme hızı, dᵢ alıcının indirme ve uᵢ eşin yükleme hızıdır.

- İstemci–sunucu alt sınırı: Dcs ≥ max(NF/uₛ, F/min(dᵢ)).
- P2P alt sınırı: Dp2p ≥ max(F/uₛ, F/min(dᵢ), NF/(uₛ+Σuᵢ)).

BitTorrent parçalara ayırma, parça alışverişi ve tit-for-tat yaklaşımıyla anlatılır. DHT, anahtar–değer eşlemesini eşler arasında dağıtır. Halka örneğinde anahtar 13, eş 14’te; anahtar 15, eş 1’de tutulur. Kısayol bağlantıları aramayı hızlandırır. Ayrılan eşlerin yerine geçmek için ardıl bilgisi kullanılır.

*Not: DHT’de karma fonksiyonu ile anahtar yerleştirme, tek başına şifreleme veya gizlilik sağlamaz.*

![P2P dağıtımı ve DHT — el yazısı, sayfa 19](belge-105-sayfa-19.jpg "P2P dağıtımı ve DHT — el yazısı, sayfa 19")

![P2P dağıtımı ve DHT — el yazısı, sayfa 20](belge-105-sayfa-20.jpg "P2P dağıtımı ve DHT — el yazısı, sayfa 20")

![P2P dağıtımı ve DHT — el yazısı, sayfa 21](belge-105-sayfa-21.jpg "P2P dağıtımı ve DHT — el yazısı, sayfa 21")

![P2P dağıtımı ve DHT — el yazısı, sayfa 22](belge-105-sayfa-22.jpg "P2P dağıtımı ve DHT — el yazısı, sayfa 22")

## Soketler, çoğullama ve güvenilir aktarım

TCP soketi bağlantıya, UDP soketi datagramlara dayanır. Çoklama ve ayırma uygulama süreçlerini taşıma katmanına bağlar. TCP bağlantıları kaynak IP, kaynak port, hedef IP ve hedef port dörtlüsüyle ayırt edilir. UDP alıcı tarafında hedef adres/port bilgileriyle uygulamaya teslim edilir.

Checksum bire tümleyen toplama ile hesaplanır. rdt1.0 hatasız kanalı; rdt2.x bit hatalarını, ACK/NAK ve sıra numaralarını; rdt3.0 ise kayıp ve zaman aşımını ele alır. Yinelenen paket ve bozuk ACK sorunları ayrı çizilmiştir.

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 23](belge-105-sayfa-23.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 23")

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 24](belge-105-sayfa-24.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 24")

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 25](belge-105-sayfa-25.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 25")

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 26](belge-105-sayfa-26.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 26")

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 27](belge-105-sayfa-27.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 27")

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 28](belge-105-sayfa-28.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 28")

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 29](belge-105-sayfa-29.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 29")

![Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 30](belge-105-sayfa-30.jpg "Soketler, çoğullama ve güvenilir aktarım — el yazısı, sayfa 30")

## Tıkanıklık kontrolü

ATM ABR için NI, CI ve ER alanları not edilmiştir. TCP gönderim hızı yaklaşık cwnd/RTT’dir. Slow start sırasında pencere RTT başına yaklaşık iki katına çıkar; congestion avoidance sırasında artış yaklaşık RTT başına 1 MSS olur.

MSS = 500 bayt ve RTT = 200 ms için bir MSS/RTT = 2500 bayt/s = 20 kbit/s’dir. Kayıp sonrasında eşik çoğunlukla önceki pencerenin yarısı olarak alınır. Zaman aşımı ile üç yinelenen ACK tepkileri karşılaştırılır.

*Not: Notlardaki Reno açıklamasında zaman aşımından sonra pencerenin 1 MSS’ye düşmediği izlenimi vardır; klasik Reno’da timeout ile üç yinelenen ACK farklı durumlardır, timeout sonrası başlangıç penceresine dönülür.*

![Tıkanıklık kontrolü — el yazısı, sayfa 32](belge-105-sayfa-32.jpg "Tıkanıklık kontrolü — el yazısı, sayfa 32")

![Tıkanıklık kontrolü — el yazısı, sayfa 33](belge-105-sayfa-33.jpg "Tıkanıklık kontrolü — el yazısı, sayfa 33")

![Tıkanıklık kontrolü — el yazısı, sayfa 34](belge-105-sayfa-34.jpg "Tıkanıklık kontrolü — el yazısı, sayfa 34")

![Tıkanıklık kontrolü — el yazısı, sayfa 35](belge-105-sayfa-35.jpg "Tıkanıklık kontrolü — el yazısı, sayfa 35")

![Tıkanıklık kontrolü — el yazısı, sayfa 36](belge-105-sayfa-36.jpg "Tıkanıklık kontrolü — el yazısı, sayfa 36")

## Yönlendirme ve otonom sistemler

Uzaklık vektöründe iyi haber hızlı, kötü haber yavaş yayılabilir; count-to-infinity problemi anlatılır. Otonom sistem içi ve sistemler arası yönlendirme ayrılır. RIP atlama sayısı kullanır, 15 atlamayla sınırlıdır; OSPF bağlantı durumu ve Dijkstra yaklaşımını kullanır.

BGP’de AS-PATH ve NEXT-HOP, yerel tercih, yol uzunluğu ve hot-potato yönlendirme not edilir. Broadcast ile spanning tree, multicast ile RPF, DVMRP, IGMP ve PIM dense/sparse mode karşılaştırılır.

![Yönlendirme ve otonom sistemler — el yazısı, sayfa 38](belge-105-sayfa-38.jpg "Yönlendirme ve otonom sistemler — el yazısı, sayfa 38")

![Yönlendirme ve otonom sistemler — el yazısı, sayfa 39](belge-105-sayfa-39.jpg "Yönlendirme ve otonom sistemler — el yazısı, sayfa 39")

![Yönlendirme ve otonom sistemler — el yazısı, sayfa 40](belge-105-sayfa-40.jpg "Yönlendirme ve otonom sistemler — el yazısı, sayfa 40")

![Yönlendirme ve otonom sistemler — el yazısı, sayfa 41](belge-105-sayfa-41.jpg "Yönlendirme ve otonom sistemler — el yazısı, sayfa 41")

![Yönlendirme ve otonom sistemler — el yazısı, sayfa 42](belge-105-sayfa-42.jpg "Yönlendirme ve otonom sistemler — el yazısı, sayfa 42")

![Yönlendirme ve otonom sistemler — el yazısı, sayfa 43](belge-105-sayfa-43.jpg "Yönlendirme ve otonom sistemler — el yazısı, sayfa 43")

## Bağlantı katmanı ve hata denetimi

Bağlantı katmanı çerçeveleme, ortama erişim, hata denetimi ve yerel teslimle ilişkilidir. Ethernet MAC adresi 48 bittir. Parite, iki boyutlu parite ve CRC örnekleri çizilir. CRC’de D verisine r sıfır eklenir; G üreteciyle modulo-2 bölmenin kalanı R olur. Gönderilen D·2ʳ XOR R, G ile kalansız bölünür.

Web erişim örneğinde DHCP ile yapılandırma, ARP ile yerel komşunun bulunması, DNS ile ad çözümlemesi ve HTTP ile nesne isteği birlikte gösterilir.

![Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 44](belge-105-sayfa-44.jpg "Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 44")

![Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 45](belge-105-sayfa-45.jpg "Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 45")

![Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 46](belge-105-sayfa-46.jpg "Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 46")

![Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 48](belge-105-sayfa-48.jpg "Bağlantı katmanı ve hata denetimi — el yazısı, sayfa 48")

## ATM, MPLS, anahtarlar ve VLAN

Sınav kapsamına ilişkin kısa listede ARP, hata denetimi, protokoller ve ağ erişimi yer alır. ATM, MPLS ve sanal bağlantı kavramları karşılaştırılır. MPLS etiket tabanlı iletim kullanır.

Hub, köprü ve anahtar ayrımı yapılır. Anahtar kaynak MAC adresinden hangi portun hangi cihaza ulaştığını öğrenir; bilinmeyen hedefi uygun portlara yayar. VLAN, aynı fiziksel anahtarlama altyapısında mantıksal ağ ayrımı sağlar.

![ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 49](belge-105-sayfa-49.jpg "ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 49")

![ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 50](belge-105-sayfa-50.jpg "ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 50")

![ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 51](belge-105-sayfa-51.jpg "ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 51")

![ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 52](belge-105-sayfa-52.jpg "ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 52")

![ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 53](belge-105-sayfa-53.jpg "ATM, MPLS, anahtarlar ve VLAN — el yazısı, sayfa 53")

*Not: Kapak ve boş sayfalar yazı görsellerine alınmadı; 53 sayfalık PDF içinde sıraları korunur. Kaynakta gün bilgisi yoktur; tarih dosyanın son değiştirilme kaydıdır.*

