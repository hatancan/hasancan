---
baslik: EEM413 Bilgisayar Ağları: Fotoğraflardan Ağ ve Taşıma Katmanı Notları
ozet: Fotoğraflardan Ağ ve Taşıma Katmanı Notları. Ders arşivindeki sayfalardan okunabilir metin aktarımı.
---

Ders arşivindeki anonim notlar, fotoğraflanmış sayfalardan metne aktarıldı. Fotoğraflar özel arşivde saklanır; bu yazıda indirme dosyası yoktur. Belge üzerinde tarih yoksa kaynak dosyanın tarih kaydı kullanılmıştır.

## Ağ mimarisi ve protokoller

Protokol, iletişimdeki mesajların biçimini, sırasını ve mesajlar alındığında yapılacak işlemleri tanımlar. Uç sistemler ağın kenarında, yönlendiriciler ağın çekirdeğindedir. İstemci–sunucu mimarisinde sürekli erişilebilir bir sunucuya başvurulur. P2P’de uçlar hem kaynak sunabilir hem kaynak alabilir; eşler bağlantıya girip çıkabilir.

DSL, telefon erişim hattını veri için de kullanır; DSLAM servis sağlayıcı tarafında birleştirme yapar. Kablo/HFC erişiminde ortam paylaşılır. FTTH’de OLT ve ONT optik uçlardır; PON pasif, AON aktif dağıtımı belirtir. Yerel erişimde Ethernet ve Wi-Fi, geniş alan kablosuz erişimde hücresel sistemler örneklenmiştir.

Fiziksel ortamlar bükümlü çift, koaksiyel, fiber ve radyo olarak sıralanır. Çekirdekte devre anahtarlama ve paket anahtarlama karşılaştırılır. Devre anahtarlama bağlantı için kaynak ayırır. FDM frekansı, TDM zamanı dilimlere böler. Paket anahtarlamada kaynaklar talebe göre paylaşılır; kuyruk ve paket kaybı oluşabilir.

## Gecikme, trafik yoğunluğu ve throughput

- d_düğüm = d_işleme + d_kuyruk + d_iletim + d_yayılım.
- İletim gecikmesi d_iletim = L/R: L paket uzunluğu, R bağlantı hızıdır.
- Yayılım gecikmesi d_yayılım = d/s: d mesafe, s ortam içindeki yayılma hızıdır.
- Trafik yoğunluğu La/R: a saniyedeki ortalama paket sayısıdır.
- Yolun aktarım hızı, dar boğaz oluşturan bağlantıyla sınırlanır; basit iki bağlantılı örnekte min(Rₛ, R𝚌).

İşleme sırasında başlık ve bit hataları incelenir. Kuyruk gecikmesi yükle değişir. Tampon doluysa gelen paket atılabilir. Store-and-forward’da yönlendirici paketi tamamen almadan bir sonraki bağlantıya aktarmaya başlamaz. İletim gecikmesi ile yayılım gecikmesi aynı şey değildir.

## Katmanlar ve güvenlik notları

Beş katman: uygulama, taşıma, ağ, bağlantı ve fiziksel. Uygulama mesajı taşıma katmanında segment/datagram, ağ katmanında datagram/paket, bağlantı katmanında çerçeve olarak kapsüllenir. OSI ayrıca sunum ve oturum katmanlarını ayırır.

Güvenlik başlığında virüs, solucan, Truva atı, casus yazılım, botnet, DoS/DDoS, paket dinleme ve adres sahteciliği sıralanmıştır. Bunlar tarihsel ders notlarındaki tehdit sınıflarıdır.

## Uygulama katmanı, soket ve taşıma seçimi

Süreçler soket arayüzüyle haberleşir. IP adresi makineyi, port numarası uygulama ucunu ayırır. Uygulamanın veri kaybına toleransı, zamanlama ihtiyacı, throughput ve güvenlik gereksinimi taşıma seçimini etkiler.

TCP güvenilir sıralı aktarım, akış ve tıkanıklık kontrolü sağlar; bağlantı kurulumu vardır. UDP bağlantısız datagram aktarır, teslim veya sıralama garantisi vermez. Uygulama gerekirse UDP üzerinde kendi güvenilirlik mekanizmasını kurabilir. TCP ve UDP tek başlarına sabit gecikme veya asgari bant genişliği garantisi sağlamaz.

## HTTP ve web önbelleği

HTTP istek/yanıt modelidir. Kalıcı olmayan bağlantıda her nesne için yeni TCP bağlantısı açılır. Basit tek nesne hesabı 2 RTT + dosyanın iletim süresidir. Kalıcı bağlantıda birden fazla istek aynı TCP bağlantısını kullanır; bağlantı kurulumunun tekrar edilmesi önlenir.

İstek satırı yöntem, kaynak yolu ve sürümü taşır. Host, User-Agent, Connection ve Accept-Language başlıkları örneklenir. GET nesne ister; POST veri gönderir; HEAD yanıtın başlıklarını ister. Kaynakta PUT ve DELETE de listelenir. Yanıtta durum kodu, sürüm, başlıklar ve gövde bulunur.

Çerezler önceki etkileşimle ilişki kurulmasına yardım eder. Proxy/web cache istemci adına nesne saklar; erişim bağlantısındaki yük ve yanıt süresi azalabilir. Conditional GET ile önbellekteki kopyanın güncelliği sınanır; değişmediyse nesne gövdesi tekrar gönderilmez.

## FTP, e-posta ve DNS

FTP’de kontrol ve veri bağlantıları ayrıdır; bu yapı out-of-band kontrol örneği olarak verilmiştir. Kontrol portu 21’dir. E-postada kullanıcı aracısı, posta sunucusu ve SMTP bulunur. SMTP sunucular arasında gönderim içindir; POP3 ve IMAP alıcı posta kutusuna erişir. HTTP tabanlı posta arayüzü bu işlemlerden ayrı bir erişim biçimidir.

DNS hiyerarşisi kök, üst düzey alan ve yetkili sunuculardan oluşur; yerel DNS çözümleyicisi sorguları yürütür. Recursive ve iterative sorgu farkı çizimlerde gösterilmiştir. DNS kayıt biçimi (name, value, type, TTL) olarak not edilir. A adresi, NS yetkili sunucuyu, CNAME takma adı ve MX posta sunucusunu belirtir.

## P2P dosya paylaşımı

Merkezî dizin, sorgu yayma (query flooding) ve dağıtık karma tablosu (DHT) yaklaşımları karşılaştırılır. Dosya parçalara ayrılabilir; eşler indirdikleri parçaları başkalarına yükler. BitTorrent notlarında parça seçimi ve tit-for-tat alışverişi vardır.

F dosya boyutu, N alıcı sayısı, uₛ sunucunun yükleme hızı, d_min en yavaş alıcı indirme hızı, uᵢ eşin yükleme hızı olsun:

- Dcs ≥ max(NF/uₛ, F/d_min).
- Dp2p ≥ max(F/uₛ, F/d_min, NF/(uₛ+Σuᵢ)).

DHT’de anahtarlar kimlik uzayındaki eşlere dağıtılır. Halka ve kısayol bağlantıları arama yolunu belirler; eşin ayrılması durumunda ardıl bilgisi güncellenir.

## Güvenilir aktarım: rdt ve pencereleme

rdt1.0 hatasız kanalı varsayar. rdt2.0 bit hatalarına karşı checksum ve ACK/NAK kullanır. ACK/NAK da bozulabileceğinden sıra numarası ve yinelenen paket denetimi gerekir. rdt2.2 NAK yerine yinelenen ACK kullanır. rdt3.0 kayıp için zamanlayıcı ve yeniden iletim ekler.

Stop-and-wait göndericisi paketi yollar ve alındıyı bekler. Kullanım oranı yaklaşık (L/R)/(RTT+L/R)’dir. 1 Gbit/s, 8000 bit paket ve 30 ms RTT örneğinde L/R = 8 µs; kullanım yaklaşık 0,000267, yani %0,0267’dir. Pipelining birden fazla paketin yolda olmasına izin verir.

Go-Back-N kümülatif ACK kullanır; kayıp/zaman aşımı sonrasında ilgili paketten itibaren bekleyen paketler yeniden yollanır. Selective Repeat ayrı ACK ve alıcı tamponu kullanarak yalnız eksik paketleri tekrar ister. Gönderici ve alıcı pencereleri, sıra numarası uzayına uygun seçilmelidir.

## TCP: başlık, RTT ve yeniden iletim

TCP başlığında kaynak/hedef port, sıra numarası, ACK numarası, pencere, checksum ve bayraklar yer alır. Sıra numarası baytları sayar; ACK numarası sıradaki beklenen baytı gösterir. SYN, SYN-ACK ve ACK bağlantı kurulumunu oluşturur. FIN bağlantı kapatma bağlamında gösterilir.

- EstimatedRTT = (1−α)EstimatedRTT + α SampleRTT.
- DevRTT = (1−β)DevRTT + β|SampleRTT−EstimatedRTT|.
- TimeoutInterval = EstimatedRTT + 4 DevRTT.

Zamanlayıcı kayıp tespitine yardım eder. Üç yinelenen ACK hızlı yeniden iletimi tetikleyebilir. Alıcı pencere akış kontrolünü, congestion window ağ tıkanıklığına göre gönderim sınırını temsil eder. Bunlar farklı mekanizmalardır. Kaynakta slow start, congestion avoidance ve kayıp sonrası pencere değişimleri çizilmiştir.

## Yönlendiricinin içi ve tamponlar

Giriş portları başlık inceler, iletim tablosunu kullanır ve anahtarlama yapısına erişir. Bellek üzerinden, ortak veriyolu üzerinden ve çapraz bağlantı (crossbar) üzerinden anahtarlama karşılaştırılır. Bellek ve veriyolu ortak kaynak hâline gelebilir; crossbar eşzamanlı farklı giriş–çıkış yollarını destekler.

Çıkışta paketler kuyruklanır. Girişteki ilk paketin beklemesi, arkasındaki başka çıkışa gidebilecek paketleri engelleyebilir: head-of-line blocking. Tampon boyutu için RTT×C ve çok sayıda bağımsız TCP akışında yaklaşık RTT×C/√N ifadeleri not edilmiştir. Burada C bağlantı kapasitesi, N akış sayısıdır.

## DHCP ve NAT

DHCP sırası Discover → Offer → Request → ACK olarak verilmiştir. İstemci yalnız IP adresi değil; ağ maskesi, varsayılan ağ geçidi ve DNS sunucusu gibi yapılandırma bilgileri de alır. Süreli adres kullanımı lease kavramıyla açıklanır.

NAT yerel adres/port ile dış adres/port arasında çeviri tablosu tutar. Giden paketin kaynak adresi ve portu, dönen paketin hedefi çevrilir. Az sayıda genel adresle çok sayıda yerel istemci çıkabilir. Dışarıdan başlatılan bağlantılar için sabit eşleme, UPnP/IGD ve aracı/relay yöntemleri not edilmiştir.

## ICMP ve IPv6

ICMP ağ hata ve durum mesajlarını taşır; ping ve traceroute bağlamında ele alınır. IPv6 adresleri 128 bittir, temel başlık 40 bayttır. Traffic class/priority, flow label, payload length, next header ve hop limit alanları listelenir. IPv4’teki başlık checksum’u IPv6 temel başlığında yoktur; ek özellikler uzantı başlıklarıyla taşınır. Geçiş şemasında IPv6 paketi IPv4 içine tünellenir.

*Not: Bu yazı tekrar eden fotoğrafları birleştirir. Kişisel kenar notları aktarılmadı. Formüllerde bit/bayt ve saniye birimleri ayrıldı; hesap örneği yeniden kontrol edildi. Eski protokol ve cihaz açıklamaları dersin tarihsel bağlamındadır.*

