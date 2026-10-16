---
baslik: EEM211 Sayısal Mantık Tasarımı: Başka Kurumların Lojik Devre Deney Kitapçıkları (İTÜ, SDÜ, kumanda.org, MEGEP)
ozet: EEM211 klasöründeki beş Türkçe deney kitapçığı: İTÜ Sayısal Sistem Tasarımı Uygulamaları deneyleri (2004), TTL gerilim seviyelerinden dizi detektörüne dokuz deneylik "Lojik Deneyleri" (2005), Süleyman Demirel Üniversitesi Sayısal Elektronik II deney raporları kataloğu, kumanda.org otomasyon atölyesi kapı ve gösterge deneyleri ve MEB MEGEP "Lojik Uygulamaları 3" modülü (sayıcılar, kaydediciler, DAC/ADC).
---

Bu yazı, EEM211 Sayısal Mantık Tasarımı dersinin klasöründe, laboratuvara hazırlanırken başvurmak için toplanmış beş Türkçe deney kitapçığını tanıtıyor. Hepsi başka kurumlara ya da internet sitelerine ait; her birinin kaynağı ve içerdiği deneyler aşağıda listelendi. Beş PDF yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## İTÜ: Sayısal sistem tasarımı uygulamaları deneyleri (2004)

İstanbul Teknik Üniversitesi Elektrik-Elektronik Fakültesi Elektronik Mühendisliği Programı, Devreler ve Sistemler Anabilim Dalı'nın 40 sayfalık deney föyleri (PDF Ağustos 2004 tarihli, dosya adı "sstu_2005_deneyler"). Dokuz deney:

1. TTL ve CMOS kapı karakteristikleri (giriş/çıkış seviyeleri, propagasyon gecikmesi, çıkış yelpazesi; TTL ve CMOS NAND kapılarının ölçümü).
1. Boole fonksiyonlarının SSI kapı elemanları ve MSI kod çözücü/çoklayıcılarla gerçekleştirilmesi.
1. SSI ve MSI elemanlarıyla kombinezonsal devre sentezi.
1. Senkron ardışıl devre analizi.
1. Dizi dedektörü.
1. Senkron ardışıl devre sentezi.
1. Asenkron ve senkron sayıcılar.
1. Ötelemeli yazıcılar (kaydırmalı yazmaçlar).
1. SSI ve MSI elemanlarıyla toplama ve çıkarma devreleri.

## Lojik Deneyleri (2005)

32 sayfalık bu föy kitapçığının hazırlayanı ve kurumu belgede yazmıyor (PDF Kasım 2005 tarihli); deneylerde "ders notlarının 7., 8. ve 10. bölümlerine" atıf yapılıyor. Dokuz deney:

1. Lojik kapıların lojik gerilim seviyeleri (ör. TTL bir DEĞİL kapısında V_IL = 0,8 V, V_IH = 2 V, V_OL = 0,2 V, V_OH = 3,4 V).
1. Kapı elemanlarıyla bir kod dönüştürücü ve bir kodlayıcı tasarımı.
1. SSI elemanlarıyla gerçekleştirilen paralel toplama devresi.
1. MUX ve dekoder MSI elemanlarıyla lojik devre uygulamaları.
1. Paralel toplayıcı ve EPROM LSI tümdevreleri.
1. Ardışıl devre analizi (bir Mealy makinesinin analizi).
1. Ardışıl devre sentezi: dört uzunluklu (0101) dizisini algılayan dizi detektörü.
1. Asenkron sayıcılar.
1. Orta ölçekli tümleşik devre elemanı yazmacın bir uygulaması.

## Süleyman Demirel Üniversitesi: Sayısal Elektronik II deney raporları (2001)

"Mantık Devreleri II Dersi Deney Kataloğu" (sürüm 2.5.2), Süleyman Demirel Üniversitesi Teknik Eğitim Fakültesi Elektronik-Bilgisayar Eğitimi Bölümü'nde **Sayısal Elektronik II** dersi için 2001 bahar yarıyılında hazırlanmış deney raporlarının, raporu hazırlayan öğrencinin kendi internet sitesinde (SevketKeser.Net) yayımladığı derlemesi. Her raporda deneyin amacı, kullanılan malzemeler, teorik bilgi ve devre tasarımı, bağlantı şeması ve deneyin sonucu var. Deneyler:

- Büyüklük karşılaştırıcılar (7485 ile iki bitlik iki sayının karşılaştırılması).
- 4x1 çoklayıcının (multiplexer) 74151 entegresiyle incelenmesi.
- J-K flip-flop entegresiyle verilen şartları sağlayan devre tasarımı.
- Mod 7 senkron sayıcı (J-K flip-floplarla 0'dan 6'ya sayan).
- Doğrudan sıfırlamalı ve aşağı/yukarı mod 8 asenkron sayıcı.
- 0'dan 9'a sayıp başa dönen sıfırlamalı asenkron sayıcı, 4'ten 9'a sayan ön kurmalı asenkron sayıcı.
- D flip-floplarla Johnson sayıcı.
- Seri giriş-paralel çıkış (74164) ve paralel giriş-paralel çıkış (74174) kaydediciler.
- Transistörlü kararsız (astable) multivibratör ve op-amp uygulamaları.

## kumanda.org: Otomasyon atölyesi dijital deneyleri (2007)

"Otomasyon Atölyesi Ders Notları – Deneyler" (www.kumanda.org), 15 sayfa. Her deneyde kullanılan elemanlar (entegre, 220 Ω dirençler, kırmızı ve yeşil LED'ler) ve kurulacak devreler var:

1. VE kapısı uygulamaları – 7408
1. VEYA kapısı uygulamaları – 7432
1. DEĞİL kapısı uygulamaları – 7404
1. VEDEĞİL kapısı uygulamaları – 7400
1. VEYADEĞİL kapısı uygulamaları – 7402
1. ÖZEL VEYA kapısı uygulamaları – 7486
1. Gösterge (display) uygulamaları – CQY91A
1. Kod çözücü uygulamaları – 7447 (BCD-7 parçalı gösterge kod çözücüsü)

## MEB MEGEP: Lojik Uygulamaları 3 (2007)

Millî Eğitim Bakanlığı'nın Mesleki Eğitim ve Öğretim Sisteminin Güçlendirilmesi Projesi (MEGEP) kapsamında Elektrik Elektronik Teknolojisi alanı için hazırlanmış "Lojik Uygulamaları 3" modülü (Ankara 2007, modül kodu 523EO0018, 77 sayfa). Modüllerin internetten ücretsiz erişilebildiği ve ticari amaçla kullanılamayacağı belirtiliyor. Üç öğrenme faaliyeti var:

1. **Sayıcılar:** asenkron yukarı ve aşağı sayıcılar, senkron yukarı ve aşağı sayıcılar, modlu sayıcılar.
1. **Kaydediciler:** seri giriş-seri çıkış, seri giriş-paralel çıkış, paralel giriş-seri çıkış ve paralel giriş-paralel çıkış kaydediciler.
1. **Dijital/analog ve analog/dijital çeviriciler:** D/A çeviricilerin esasları, temel R-2R merdiven tipi D/A çevirici, D/A entegreleri; A/D çeviricilerin esasları, paralel karşılaştırıcılı A/D çevirici, A/D entegreleri.

Her faaliyetin sonunda uygulama faaliyeti, ölçme ve değerlendirme soruları ve performans testi; modülün sonunda cevap anahtarları var.
