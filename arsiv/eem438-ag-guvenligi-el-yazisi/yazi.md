---
baslik: EEM438 Veri İletişimi: Ağ Güvenliği: SSL, IPsec ve Güvenlik Duvarları
ozet: Ağ Güvenliği: SSL, IPsec ve Güvenlik Duvarları. Ders arşivinden soru, açıklama ve belgeler.
---


## Güvenliğin bileşenleri ve şifreleme

Gizlilik, kimlik doğrulama, mesaj bütünlüğü ve erişilebilirlik ayrı hedeflerdir. Dinleme, kimliğe bürünme ve hizmet engelleme tehditleri listelenir. Düz metin m, şifreleme Kₐ ve çözme Kᵦ ile m = Kᵦ(Kₐ(m)) gösterilir. Monoalfabetik ve çok alfabeli yer değiştirme örnekleri açıklanır.

![Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 1](belge-299-sayfa-01.jpg "Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 1")

![Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 2](belge-299-sayfa-02.jpg "Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 2")

![Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 3](belge-299-sayfa-03.jpg "Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 3")

![Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 4](belge-299-sayfa-04.jpg "Güvenliğin bileşenleri ve şifreleme — el yazısı, sayfa 4")

## SSL el sıkışması ve kayıt katmanı

SSL için el sıkışma, sertifika, anahtar üretimi, veri transferi ve kapanış aşamaları yazılmıştır. İki yön için ayrı şifreleme ve MAC anahtarları kullanılabilir. Kayıt şemasında length, data ve MAC alanları gösterilir. Sıra numarası MAC hesabına katılarak yeniden sıralama/tekrar saldırılarına karşı kullanılır. Pre-master secret ve nonce anahtar türetme girdileri olarak anılır.

![SSL el sıkışması ve kayıt katmanı — el yazısı, sayfa 5](belge-299-sayfa-05.jpg "SSL el sıkışması ve kayıt katmanı — el yazısı, sayfa 5")

![SSL el sıkışması ve kayıt katmanı — el yazısı, sayfa 6](belge-299-sayfa-06.jpg "SSL el sıkışması ve kayıt katmanı — el yazısı, sayfa 6")

![SSL el sıkışması ve kayıt katmanı — el yazısı, sayfa 7](belge-299-sayfa-07.jpg "SSL el sıkışması ve kayıt katmanı — el yazısı, sayfa 7")

## VPN, IPsec ve güvenlik ilişkileri

VPN kurumlar arası trafiği korumak için anlatılır. Transport ve tunnel modları, AH ve ESP karşılaştırılır. AH gizlilik sağlamaz; ESP şifreleme ve doğrulama servisleriyle ilişkilidir. SA tek yönlüdür; iki yönlü trafik için iki ilişki gerekir. SPI, uç adresleri, algoritmalar ve anahtarlar SA bağlamında tutulur. SAD mevcut ilişkileri, SPD uygulanacak politikayı tanımlar.

![VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 8](belge-299-sayfa-08.jpg "VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 8")

![VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 9](belge-299-sayfa-09.jpg "VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 9")

![VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 10](belge-299-sayfa-10.jpg "VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 10")

![VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 11](belge-299-sayfa-11.jpg "VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 11")

![VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 12](belge-299-sayfa-12.jpg "VPN, IPsec ve güvenlik ilişkileri — el yazısı, sayfa 12")

## Kablosuz güvenlik ve erişim denetimi

WEP, paylaşılan anahtar ve IV ile akış şifreleme örneğinde anlatılır. IV tekrarları zayıflığa neden olur. Kimlik doğrulama sunucusu, AP, istemci, master key ve PMK ilişkileri çizilmiştir. EAP, EAPOL ve RADIUS kavramları yer alır.

Güvenlik duvarı paketleri adres, port ve protokole göre süzer. Stateless filtre durum tutmaz; stateful filtre bağlantı durumunu izler. Uygulama geçidi uygulama iletişimini aracılar. IDS paket içeriklerini ve trafik örüntülerini inceleyerek ihlal belirtilerini arar.

![Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 13](belge-299-sayfa-13.jpg "Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 13")

![Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 14](belge-299-sayfa-14.jpg "Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 14")

![Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 15](belge-299-sayfa-15.jpg "Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 15")

![Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 16](belge-299-sayfa-16.jpg "Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 16")

![Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 17](belge-299-sayfa-17.jpg "Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 17")

![Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 18](belge-299-sayfa-18.jpg "Kablosuz güvenlik ve erişim denetimi — el yazısı, sayfa 18")

*Not: SSL ve WEP açıklamaları tarihsel ders içeriğidir. IDS saldırıyı tespit etmeyi amaçlar; her IDS’nin trafiği doğrudan engellediği sonucu çıkarılmamalıdır. Kaynaktaki eksik el sıkışma maddeleri tamamlanmış gibi gösterilmedi.*

