---
baslik: BIL437 Bilgisayarlı Görme: Kısa Sınav 1 (Histogram ve Dönüşüm) ve El Yazısı Sınav Çalışma Notu
ozet: BIL437 Bilgisayarlı Görme dersinin 2015 yaz okulu kısa sınavı (görüntü matrisi, histogram çizimi, parçalı dönüşüm fonksiyonu) ve sınav öncesi alınan el yazısı soru konusu listesinin metne aktarımı.
---

Bu yazı, 2015 yaz okulunda aldığım **BIL437 Bilgisayarlı Görme (Bilgisayarlı Görü)** dersindeki bir kısa sınavın ve sınava hazırlık için not ettiğim konu listesinin, fotoğraflanmış sayfalardan metne aktarılmış hâlidir. Fotoğrafların kendisi yayımlanmamıştır.

## Kısa Sınav 1 (süre 15 dakika)

Sınav kâğıdının üstünde "BİL-437 Bilgisayarla Görme – Quiz-1, süre: 15 dakika" yazıyor; kâğıttaki tarih 09.07.2014 olarak basılmış (fotoğraf 7 Temmuz 2015 tarihli olduğundan büyük olasılıkla yıl yazım hatasıdır).

**Soru.** Aşağıda f(x, y) görüntüsü verilmiştir (6 satır × 5 sütun):

| 10 | 12 | 14 | 17 | 17 |
|---|---|---|---|---|
| 12 | 12 | 14 | 18 | 19 |
| 14 | 12 | 24 | 10 | 21 |
| 12 | 12 | 18 | 18 | 18 |
| 14 | 17 | 18 | 18 | 18 |
| 12 | 14 | 17 | 17 | 18 |

Buna göre:

1. f(x, y) görüntüsünün histogramını çiziniz.
2. f(x, y) görüntüsüne aşağıdaki T(x, y) dönüşüm fonksiyonu uygulandığında oluşacak görüntünün yeni piksel değerlerini hesaplayınız (kesirli sayıları bir üst tam sayıya yuvarlayınız).

Dönüşüm fonksiyonu grafikle verilmiştir: yatay eksende eski değerler (0, 10, 12, 14, 16, 18, 20, 24), düşey eksende yeni değerler (8, 11, 12, 13, 14, 16 civarı) işaretli; 16'ya kadar artan, sonra 20'ye kadar sabit, 20'de aşağı sıçrayıp yeniden artan parçalı doğrusal bir eğridir. Grafik fotoğrafta ekran görüntüsü olarak okunaksız olduğu için eğrinin tam değerleri aktarılamadı.

**Histogram (benim hesabım).** Görüntüdeki gri seviyelerin sayıları: 10 → 2 piksel, 12 → 7, 14 → 5, 17 → 5, 18 → 8, 19 → 1, 21 → 1, 24 → 1 (toplam 30 piksel). Kâğıttaki el yazısı not da "hocam bu soruda her 10 eşit 12 değerlerini f(x,y) bütün piksellerin sıklığını yazın" diyor gibi okunuyor; yani histogramın her seviyenin piksel sayısını göstermesi isteniyor.

Kâğıtta elle yazılmış cevap matrisi (kesirli değerleri yukarı yuvarlanmış yeni görüntü), ilk satırı 8 9 11 13 13 olan 6×5'lik bir tablodur; satırlar: 8 9 11 13 13 / 9 9 11 14 14 / 11 9 18 8 16 / 9 9 14 14 14 / 11 13 14 14 14 / 9 11 13 13 14 (el yazısı okunuşu tam kesin değildir).

## Sınav öncesi çalışma notu (el yazısı)

Aşağıdaki liste, sınavda gelebileceğini düşündüğüm soru tiplerinin el yazısı kısa notudur (iki fotoğrafta aynı not):

1. **Soru 1**
   - a) RGB → CMY dönüşümü uygulayıp poster hazırlama; HSI ve I hesaplama (renkli görüntü işleme).
   - b) Uzamsal bölgeden frekans bölgesine geçiş: 2. dereceden bir süzgeç için uzamsal bölge çevirme formülü, işlem adımlarını yaz.
2. Bir resim ve histogramı verilmiş: histogramı çiz; ters (inverse) parlaklık, daha koyu/daha açık dönüşümleri.
3. Yoğunluk dilimleme (intensity slicing, gri): 8×8 bir matris verilmiş (yarısı siyah, yarısı beyaz, bir de ızgara çizimi); **ortalama (average) süzgeç uygula**.
4. Tuz-biber gürültülü bir resim verilmiş; altı seçenek içinde hangi süzgecin hangi resme karşılık geldiğini bul.
5. (Madde numarası 6 olarak çizilmiş) Parçalı bir T(r) fonksiyonu grafiği (80 ve 100 civarında kırılmalı, doğrusal kısım ile birlikte); bu dönüşümü yapan MATLAB kodunu yaz.

Bu konuların hepsi derste işlenen başlıklarla örtüşüyor: renk modelleri, histogram ve dönüşümler, ortalama/medyan süzgeçler. Bkz. serinin diğer yazıları.
