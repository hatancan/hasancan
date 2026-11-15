---
baslik: EEM323 Elektromanyetik II: Polarizasyon, Doppler Etkisi, Düşük Kayıplı Dielektrikler ve İyi İletkenler (Prof. S. Gökhun Tanyer)
ozet: Prof. Dr. S. Gökhun Tanyer'in EEM323 dersinde elektromanyetik dalgaların polarizasyonu (doğrusal, dairesel, eliptik), Doppler etkisi, kayıplı ortamda düzlem dalgalar, grup hızı ve Poynting vektörü notlarının metin özeti.
---

Prof. Dr. S. Gökhun Tanyer'in **EEM 323 Elektromanyetik II** dersinde (2013–2014 güz, Kasım 2013) işlediği üç notun metin içeriği: polarizasyon, Doppler etkisi ve kayıplı ortamlarda düzlem dalgalar. Şekiller ve kitaptan alınan denklemler çoğaltılmamıştır.

## 1. Elektromanyetik dalganın polarizasyonu

EM dalganın polarizasyonu, **elektrik alanın polarizasyonu** olarak tanımlanır. Dalga ilerleyişine göre farklı yönlerde gözlenebilir; özel olarak belirtilmedikçe gözlem yönü, dalganın ilerlediği yönden dalgaya doğru bakıştır. Polarizasyon çeşitleri:

- **Doğrusal** (linear),
- **Dairesel** (circular): saat yönünde (hocanın notasyonunda sol-el polarizasyonu, LHP) ya da saatin ters yönünde (sağ-el polarizasyonu, RHP),
- **Eliptik** (elliptical): yine saat yönünde ya da ters yönde; eliptik polarizasyonda eksen sapması (axis tilt) tanımlanır.

Slaytlarda Balanis'in (*Antenna Theory*) ve Collin'in (*Antennas and Radiowave Propagation*) gösterimleri izlenmiştir: −z yönünde ilerleyen elektrik alanı kartezyen koordinatlarda ve uzak alanda yazılıp, x ve y bileşenlerinin genlik ve faz farkına göre doğrusal, dairesel ve genel eliptik durumlar ayrıştırılıyor.

**Kitaplar arası gösterim farkı (hocanın vurgusu).** Dersin amacı, farklı kitaplardaki formülasyon ve gösterim farkları rahatsız etmeden araştırma yapabilme becerisi kazandırmaktır. Örnek: EEM 224/EEM 323'te kullanılan **Cheng**, +z yönünde ilerleyen dalgayı; EEM 423'te kullanılan **Balanis** ise −z yönünde ilerleyen doğrusal polarizasyonlu düzlem dalgayı inceler. Her iki yönde ilerleyen dalgaların fazına bakılıp ikisi birleştirilince görülür ki sağ-el yönünü gösteren oklar iki yönde birbirinin tersidir. Önemli örnek: +z yönünde ilerleyen dalgada fazlar arasındaki fark pozitifse polarizasyon saat yönündedir (CW), yani sağ-el yönünün tersindedir. Hocanın notuna göre keyfi yönde ilerleyen dalga polarizasyonu EEM 423 kapsamındadır; slaytlarda +z yönünde ve uzak alanda r yönünde ilerleyen dalga için polarizasyon belirleme örnekleri çözülmüştür.

**Ödevler ve sorular:**

- İnternet araştırması: polarize gözlük gerektiren 3 boyutlu TV ve sinemaların çalışma ilkesini inceleyiniz.
- MATLAB ile zaman içinde elektrik alan vektörünü çizdirerek polarizasyonun değişimini gözleyiniz; farklı zaman değerlerinde vektörü polarizasyon şekli üzerinde gösteriniz.

## 2. Doppler etkisi

Christian Doppler'in (1803–1853) adını taşıyan etki hocanın anlatımıyla şöyledir: **kaynak gözlemciye yaklaşırken** ardışık her dalga tepesi bir öncekinden daha yakın bir konumdan yayılır; böylece her dalga gözlemciye biraz daha kısa sürede ulaşır, ardışık tepelerin varış süreleri arasındaki zaman kısalır ve **frekans artar**. Yolculuk sırasında ardışık dalga cepheleri arası azalır, dalgalar "birikir". Kaynak **uzaklaşıyorsa** her dalga bir öncekinden daha uzak bir konumdan yayıldığı için varış süreleri uzar, frekans azalır ve dalga cepheleri arası açılır.

**Soru (hocanın sorusu):** Noktasal bir kaynaktan çıkan dalganın cephelerini çiziniz: (a) kaynak durağan; kaynak sağa doğru dalga hızının (b) 3/4'ü, (c) ona eşit, (d) 4/3'ü kadar hızla hareket ediyor.

Notta ayrıca şu uygulamalar gösteriliyor: uzak galaksilerden gelen dalgaların **kırmızıya kayması** (bir galaksi kümesinin optik spektrumundaki çizgilerin Güneş'inkilere göre kayması), **ultrason** Doppler görüntüleme (şah damarında renkli akış), Doppler hava radarı ve polis radarı. Hocanın düşündürdüğü soru: ultrasonik ses dalgalarında da Doppler etkisi geçerli midir?

## 3. Kayıplı ortamlarda düzlem dalgalar (düşük kayıplı dielektrikler ve iyi iletkenler)

- **İyi dielektrikler** düşük kayıplı, **iyi iletkenler** yüksek kayıplı ortamlardır (σ/ωε çok küçük ya da çok büyük). Her iki uç durumda Maxwell denklemleri yaklaşıklanarak daha basit çözümler elde edilir; ne iyi iletken ne iyi dielektrik olan ortamlarda **yaklaşıklama yoktur**, genel çözüm kullanılır.
- **Grup hızı**, dalga paketinin zarfının hızıdır; **faz hızı** ise dalga biçiminin fazının belirli bir yönde tanımlanan hızıdır. z ekseni boyunca ω açısal frekanslı dalga cos(ωt − βz) biçimindedir; grup hızı bu dalga biçiminin zarf fonksiyonundan hesaplanır.
- **Elektromanyetik güç ve Poynting vektörü**; dalga sayısı ve dalga yayılım vektörü; enine elektromanyetik (TEM) dalgalar için ilişkiler.
- Notun sonunda polarizasyon örnekleri (eksiksiz denklem görselleriyle) çözülmüştür.

## Kaynak notu

Bu yazı, Prof. Dr. S. Gökhun Tanyer'in Başkent Üniversitesi EEM 323 Elektromanyetik II dersi (2013–2014 güz) için hazırladığı ders sunumlarındaki **hocanın kendi metin içeriğinin** (başlıklar, anlatım, sorular, ödevler) özetlenip yazıya dökülmüş hâlidir (OGR-EEM323-DN-2G-Polarisation, 2H-DopplerEffect, 2I-LowLossGoodCond). Sunumlardaki şekiller, tablolar ve denklem görselleri, sunumların kendi ifadesine göre D. K. Cheng'in ders kitaplarından (*Fundamentals of Engineering Electromagnetics*, *Field and Wave Electromagnetics*) alınmıştır; bu yüzden **burada çoğaltılmamıştır** ve orijinal sunum dosyası indirmeye açılmamıştır. Şekil ve ayrıntılı türetmeler için Cheng'in kitabına bakılmalıdır.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*
