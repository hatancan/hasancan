---
baslik: EEM424 Mikrodalga Teorisi: Elektromanyetik Dalga Yayılımı - Dispersiyon Etkisi Proje Raporu (Kare ve Üçgen Dalga, MATLAB)
ozet: İki arkadaşın EEM424 Mikrodalga Teorisi dersi 2015 proje raporu: kare ve üçgen işaretlerin dispersiyonlu yayılımda uğradığı bozulma; kavram ve işletim, iş kırılım ağacı, çalışma takvimi, araştırma ara sonuçları ve MATLAB kodları. Kişisel bilgiler çıkarıldı.
---

Bu yazı, **EEM 424 Mikrodalga Teorisi** dersinde (Prof. Dr. S. Gökhun Tanyer) iki arkadaşımın hazırladığı proje raporunu (17 Nisan 2015, "Elektromanyetik Dalga Yayılımı – Dispersiyon Etkisi") ve proje klasöründeki ek belgeleri anlatır. Öğrenci adları ve numaraları çıkarılmış, rapor sayfaları maskelenmiştir. Maskelenmiş rapor ve MATLAB dosyaları yazının sonunda ZIP olarak indirilebilir.

## Kavram ve işletim

1. Girdi olarak verilen **kare ve üçgen işaretlerin EM dalga yayılımında uğrayabilecekleri genlik bozulmalarının** dalgaya etkileri incelenecektir.
2. Açık kaynak incelemesiyle şu konular araştırılır: Fourier serisi/dönüşümü, hızlı Fourier dönüşümü, ayrık Fourier dönüşümü, distorsiyon, dispersiyon, kanal modelleme, kanal dengeleme.
3. Girdi olarak kare ve üçgen dalga verilir; dalga değişkenleri ile zayıflama fonksiyonları belirlenir.
4. Çıktı olarak: giriş dalga şekillerinin zamanda gösterimi, frekans spektrumu, belirlenen uzaklıkta dalga şekilleri (tek grafikte) ve bu uzaklıkta dalga şekillerinin frekans spektrumu (tek grafikte).
5. **Sürüm 1:** tüm girdiler yazılım metnine elle girilerek koşturulur. **Sürüm 2:** girdiler grafiksel arayüzden girilir.
6. Proje raporu hazırlanır.

## İş kırılım ağacı ve çalışma takvimi

Ağaç: 1.0 EM dalga yayılımı – dispersiyon etkisi → 1.1 hazırlık çalışması (açık kaynak araştırması) → 1.2 sürüm 1 çalışmaları (girdilerin yazılıma elle girilmesi) → 1.3 sürüm 2 çalışmaları (girdilerin grafiksel arayüzle girilmesi) → 1.4 derleme → 1.5 testler → 1.6 dokümanların hazırlanması.

Takvim: 7. hafta kavram ve işletim, iş kırılım ağacı; 9. hafta hazırlık çalışması, sürüm 1'in tamamlanması; 10. hafta girdilerin MATLAB'da hazırlanması; 11. hafta çıktıların MATLAB'da elde edilmesi; 12. hafta sürüm 2'nin tamamlanması ve makale biçiminde rapor; 13. hafta proje teslimi.

## Araştırma ara sonuçları

- **Fourier serisi / dönüşümü:** periyodik bir fonksiyonu sinüs ve kosinüslü sonsuz seriye açar; Fourier ilk kez metal çubuk veya levhadaki ısı denklemi için kullanmıştır. Dönüşüm, zaman düzlemindeki işareti frekans düzlemine çevirir. Bir diğer çalışma, Fourier serisini Euler açılımıyla üssel forma getirmenin ve periyodik olmayan işaretleri fazör uzayında göstermek için dönüşüm kullanmanın özetidir.
- **FFT:** zaman düzlemindeki işaretleri frekans düzlemine aktarmak için ayrık Fourier dönüşümünde kullanılan bir algoritmadır (Cooley–Tukey en yaygın olanıdır, mantığı Gauss'un çalışmalarına dayanır); verilerin eşit aralıklı alınmış olması gerekir.
- **Ayrık Fourier dönüşümü:** Fourier dönüşümünün eşit aralıklı frekanslardaki örneklerine eşittir; sonlu sayıda nokta için değerlendirme sağlar.
- **Distorsiyon:** sinyal genliğinde oluşan bozulmadır; çıkış sinyalinde girişte olmayan harmonikler görülür, bunların sinyale oranı dB olarak ifade edilir. Genlik, frekans, faz, harmonik ve grup hızı bozulması gibi türleri vardır; müzikte (elektro gitar) sıkça kullanılır, haberleşmede önlenmeye çalışılan bir etkidir.
- **Nyquist oranı:** bant sınırlı sinyallerde aliasing olmaması için gereken minimum örnekleme oranı (fmax'ın iki katı).
- **Dispersiyon (dağılma):** bir sinyali oluşturan farklı dalga boylu bileşenlerin farklı faz hızlarıyla ilerlemesinin dalga şeklinde yarattığı bozulma; akustik, optik, haberleşme, sismik ve okyanus dalgalarında görülür.
- **Kanal modelleme:** bir kanalı kodlama ve işleme aşamasından önce, çevre koşullarının yeterince iyi modellenmesi (performans, maliyet ve zaman tasarrufu). **Kanal dengeleme:** kanal boyunca iletilen sinyalde oluşan bozulmaları tersine çevirmek için kullanılır.
- **Radar darbe görev faktörü:** darbe süresinin boşluk süresine oranı.

## MATLAB kodları

Üçgen ve kare dalga girdileri (ZIP'te `ucgen-dalga.m` ve `kare-dalga.m`):

```matlab
fs = 1000;
t = 0:1/fs:1;
x1 = sawtooth(2*pi*50*t);
plot(211),plot(t,x1), axis([0 0.2 -1.2 1.2])
xlabel('Zaman (san)');
ylabel('Genlik');
title('Ucgen Dalga');
```

```matlab
fs = 10000;
t = 0:1/fs:1.5;
x1 = square(2*pi*50*t);
subplot(211)
plot(t,x1)
axis([0 0.2 -1.2 1.2]);
xlabel('Zaman');
ylabel('Genlik');
title('Kare Dalga');
```

50 Hz'lik kare ve üçgen (testere) dalga üretilir ve ilk 0,2 saniyesi çizilir; üretilen şekiller ZIP içinde PNG olarak da vardır. Klasördeki kodlar yalnızca giriş dalgalarını üretir; dispersiyonlu yayılım hesabı (belirli uzaklıkta dalga şekli) klasörde bulunmayan sürüm 2'ye bırakılmıştır, rapor ise yalnızca kavram, takvim ve araştırma ara sonuçlarını içerir.

*Not: Rapor kapağındaki ad ve numaralar çıkarılmıştır. Klasörde ayrıca farklı bir derse ait (BME 314) proje dosyaları, "ÖDEV 3" adlı bir üç fazlı devre ödevi ve bir ders slaytı da bulunuyordu; bunlar bu yazıya dahil edilmemiştir.*
