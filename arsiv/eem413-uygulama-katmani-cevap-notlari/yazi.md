---
baslik: EEM413 Bilgisayar Ağları: Uygulama Katmanı İçin Kısa Cevap Notları
ozet: Uygulama Katmanı İçin Kısa Cevap Notları. Ders arşivinden soru, açıklama ve belgeler.
---

Ders klasöründeki bir arkadaşın hazırladığı kısa cevap notlarıdır; kişisel bilgiler çıkarılmıştır. Uygulama mimarisi, HTTP, e-posta ve P2P konularını kapsar. Belgelerin PDF kopyaları yazının sonunda indirilebilir.

## network-1

**2.** Bilgisayar ağları mimarisi,kommunikasyon organizasyonunu katmanlara ayırır. Uygulama mimarisi ise, bir uygulama geliştiricisi tarafından dizayn edilir ve uygulamanın nasıl olacağını belirler.

**3.** Mesajlaşma ilk olarak ortak servera bağlanarak alıcının IP adresini belirler. Daha sonra mesaj alcı ve verici arasında direk yollanır.

**6.** Alıcının IP adresi ve alıcı soketinin port numaraları.

yollamadan önce kontrol paketlerini değişiyorsa kullanır. STMP ise HTTP nin bulunmadığı

**12.** Pipelingsiz HTTPde, Web Tarayıcı yeni HTTP isteğini yayınlamadan önce ilk olarak serverdan HTTP cevabı almayı bekler. Pipelingli de ise, web tarayıcı HTTP isteğini serverdan cevap almayı beklemeden ihtiyaç olduğu anda yayınlar.

sunucusunun baglı bulunduğu LANa aktarır. Ayrıca tüm objeler için gecikmeyi önler, bağlantılar üzerindeki trafiği azaltır.

**16.** Mesaj Alice’in sunucusundan mail serverına HTTP üzerinden yollanır. Alice’in mail serverı mesajı Bob’un mail serverına SMTP ile yollar. Daha sonra Bob mesajı kendi mail serverından sunucusuna POP3 ile transfer eder.

**20.** P2P dosya paylaşım sistemindeki ağ dosya paylaşım sistemindeki düğüm noktalarından ve bu noktalar arasındaki mantıksal bağlantılardan oluşur. Nokta A Nokta B’nin IP adresine yönlendirilmiş olan dataları yolladığında, Nokta A’dan Nokta B’ye direk bir mantıksak bağlantı adresi oluşur. Yönlendiricisi yoktur. Herhangi bir düğüm noktası Gnutella’ya katılmak istediğinde ilk başta bağlı olan diğer düğüm noktalarının IP adresleri bulunur,daha sonra bu düğüm noktalarına katılım mesajı yollanır. Düğüm noktası onayı aldığı zaman, Gnutella ağının bir üyesi haline gelir. Düğüm noktaları kendi mantıksal bağlantılarını periyodik yenileme mesajları ile belirlerler.

**21.** Kazaa, eDonkey, Bit Torrent

*Not: Metindeki “STMP” yazımı SMTP olarak anlaşılmalıdır. Bunlar öğrenci cevaplarıdır; eksik soru numaraları kaynakta da yoktur.*

