---
baslik: EEM413 Bilgisayar Ağları: Bölüm 2: Uygulama Katmanı ve HTTP
ozet: Bölüm 2: Uygulama Katmanı ve HTTP. Ders arşivinden soru, açıklama ve belgeler.
---


## Uygulama mimarileri

İstemci–sunucu ve P2P mimarileri; süreçler arası haberleşme; IP adresi ve port; soketin uygulama ile taşıma katmanı arasındaki arayüz olması açıklanır.

![Uygulama mimarileri — el yazısı, sayfa 1](belge-113-sayfa-01.jpg "Uygulama mimarileri — el yazısı, sayfa 1")

## Uygulamanın taşıma gereksinimleri

Veri bütünlüğü, zamanlama, throughput ve güvenlik gereksinimleri ayrı ele alınır. Dosya aktarımı kayba duyarlı, gerçek zamanlı ses gecikmeye duyarlıdır.

![Uygulamanın taşıma gereksinimleri — el yazısı, sayfa 1](belge-114-sayfa-01.jpg "Uygulamanın taşıma gereksinimleri — el yazısı, sayfa 1")

## TCP ve UDP servisleri

TCP bağlantı odaklı, güvenilir ve akış/tıkanıklık kontrollüdür. UDP bağlantısızdır. İkisinin de tek başına asgari aktarım hızı veya kesin gecikme garantisi yoktur.

![TCP ve UDP servisleri — el yazısı, sayfa 1](belge-115-sayfa-01.jpg "TCP ve UDP servisleri — el yazısı, sayfa 1")

## HTTP bağlantıları

HTTP istek ve cevap mesajlarıyla çalışır. Kalıcı olmayan bağlantıda nesne başına bağlantı kurulumu yapılır. Basit hesapta yanıt süresi 2 RTT + nesne iletim süresidir; kalıcı bağlantı tekrar kurulumu azaltır.

![HTTP bağlantıları — el yazısı, sayfa 1](belge-116-sayfa-01.jpg "HTTP bağlantıları — el yazısı, sayfa 1")

## HTTP mesajları ve durum kodları

İstek satırı yöntem, yol ve sürümü içerir. Host, User-Agent, Connection ve Accept-Language başlıkları örneklenir. Yanıt durum kodu ve açıklaması taşır; 200 başarı, 301 yönlendirme, 400 hatalı istek ve 404 bulunamayan kaynak örnekleridir.

![HTTP mesajları ve durum kodları — el yazısı, sayfa 1](belge-117-sayfa-01.jpg "HTTP mesajları ve durum kodları — el yazısı, sayfa 1")
