---
baslik: BIL437 Bilgisayarlı Görü: Uzamsal Süzgeçleme, Keskinleştirme (Laplace, Sobel) ve Frekans Uzayında Süzgeçleme
ozet: BIL437 Bilgisayarlı Görü dersinin 2 ve 3. hafta sunumları: komşuluk işlemleri, ortalama ve medyan süzgeç, kenar sorunu, korelasyon-evrişim, Laplace ve Sobel, ayrık Fourier dönüşümü, ideal/Butterworth/Gauss alçak ve yüksek geçiren süzgeçler.
---

BIL437 Bilgisayarlı Görü (Başkent Üniversitesi, 2015 yaz) dersinin Lecture 2_1, 2_2 ve 3_1 sunumlarının ders notu özetidir. Sunumlardaki görüntüler Gonzalez & Woods, *Digital Image Processing* kitabından alınmıştır; slaytlarda yazar adı yazmıyor, ama PDF belge özelliklerinde yazar **Brian Mac Namee** olarak kayıtlı. Orijinal sunumlar yazının sonunda ZIP olarak indirilebilir. Önceki yazı: giriş ve histogram/nokta işleme.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Uzamsal süzgeçleme 1: komşuluk işlemleri ve yumuşatma

**Komşuluk işlemleri**, nokta işlemlerinden farklı olarak merkez pikselin etrafındaki bir dikdörtgen komşuluğu kullanır. Basit örnekler:

- **Min**: piksel, komşuluktaki en küçük değere ayarlanır,
- **Max**: en büyük değere ayarlanır,
- **Medyan**: komşuluk değerleri sıralanınca ortadaki değer (örneğin [1, 7, 15, 18, 24] kümesinin medyanı 15'tir). Bazen ortalamadan daha iyi sonuç verir.

### Süzgeçleme işlemi

3×3 bir süzgeç maskesi (w) görüntü üzerinde gezdirilir; her konumda maske katsayıları ile altındaki piksellerin çarpımları toplanır ve sonuç merkez piksele yazılır:

g(x, y) = Σ_s Σ_t w(s, t) · f(x + s, y + t)  (s = −a..a, t = −b..b)

**Ortalama (yumuşatma) süzgeci**: 3×3 maskenin tüm katsayıları 1/9'dur; gürültüyü giderir ve ayrıntıyı bulanıklaştırır. Örnekte 3×3 komşuluğun değerleri (104 100 108 / 99 106 98 / 95 90 85) için merkez piksel 98,33 olur. 500×500'lük bir görüntüde süzgeç boyu 3, 5, 9, 15, 35 yapıldıkça ayrıntı giderek kaybolur. **Ağırlıklı ortalama** süzgeçte merkeze yakın pikseller daha önemlidir: 1/16 × [1 2 1; 2 4 2; 1 2 1].

Gürültülü görüntüde (tuz-biber gürültüsü gibi) ortalama süzgeç yerine **medyan süzgeç** çoğu zaman daha iyi sonuç verir.

### Kenarlarda ne olur?

Görüntünün kenarındaki piksellerde komşuluk eksiktir. Çözümler: eksik pikselleri atlamak (yalnız bazı süzgeçlerde olur), görüntüyü tümüyle siyah ya da beyaz pikselle **doldurmak (zero padding)** ya da kenar piksellerini **kopyalamak (replicate)**.

### Korelasyon ve evrişim

Şimdiye kadar anlatılan işlem **korelasyondur**. **Evrişimde** süzgeç maskesi 180° döndürülmüş (ters çevrilmiş) kullanılır. Simetrik süzgeçlerde ikisi aynı sonucu verir.

## Uzamsal süzgeçleme 2: keskinleştirme

Keskinleştirme süzgeçleri ince ayrıntıyı ve kenarları vurgular, bulanıklığı azaltır; uzamsal **türev** alma esasına dayanır.

- 1. türev: ∂f/∂x = f(x + 1) − f(x) (ardışık değerler arasındaki fark).
- 2. türev: ∂²f/∂x² = f(x + 1) + f(x − 1) − 2f(x).

Örnek bir sinyal (5 5 4 3 2 1 0 0 0 6 0 0 0 0 1 3 1 0 0 0 0 7 7 7 7) için 1. türev 0 −1 −1 −1 −1 0 0 6 −6 0 0 0 1 2 −2 −1 0 0 0 7 0 0 0 olur. 2. türev görüntü iyileştirmede daha yararlıdır: ince ayrıntıya daha güçlü yanıt verir ve gerçeklemesi daha basittir.

### Laplace süzgeci

∇²f = [f(x+1, y) + f(x−1, y) + f(x, y+1) + f(x, y−1)] − 4f(x, y)

Buna karşılık gelen maske: 0 1 0 / 1 −4 1 / 0 1 0 (izotropiktir). Laplace sonucu tek başına iyileştirilmiş görüntü değildir; keskinleştirilmiş görüntü g(x, y) = f(x, y) − ∇²f ile elde edilir. İkisi tek maskede birleştirilince: 0 −1 0 / −1 5 −1 / 0 −1 0. Köşegenleri de katan bir Laplace türü 1 1 1 / 1 −8 1 / 1 1 1; bunun tek adımlık keskinleştirme karşılığı −1 −1 −1 / −1 9 −1 / −1 −1 −1'dir.

### 1. türev: gradyan ve Sobel

Gradyanın büyüklüğü |∇f| ≈ |Gx| + |Gy| ile yaklaşıklanır. **Sobel** işleçleri: Gy için −1 −2 −1 / 0 0 0 / 1 2 1, Gx için −1 0 1 / −2 0 2 / −1 0 1. Görüntü iki işleçle ayrı ayrı süzülüp sonuçlar toplanır. Sobel çoğunlukla kenar bulmada kullanılır (örnek: kontakt lens görüntüsünde kusurların belirginleştirilmesi).

**1. ve 2. türevlerin karşılaştırması**: 1. türev daha kalın kenar verir ve gri seviye basamağına daha güçlü yanıt verir; 2. türev ince çizgi gibi ayrıntılara daha güçlü yanıt verir ama basamak değişimlerinde çift yanıt üretir.

### Yöntemleri birleştirme

Başarılı iyileştirme tek işlemle olmaz. Sunumdaki kemik sintigrafisi örneğinde sırayla: Laplace süzgeci → Laplace'ı çıkararak keskinleştirme → Sobel süzgeci → Sobel'in 5×5 ortalamayla yumuşatılması → Laplace'la keskinleştirilmiş görüntü ile yumuşatılmış Sobel'in çarpılarak maske oluşturulması → maskenin keskin görüntüyle toplanması → son olarak kuvvet yasası dönüşümü uygulanıyor.

## Frekans uzayında süzgeçleme

### Fourier ve ayrık Fourier dönüşümü

Jean Baptiste Joseph Fourier (1768, Auxerre), *La Théorie Analytique de la Chaleur* adlı çalışmasıyla bilinir. Temel fikir: kendini periyodik olarak tekrarlayan her fonksiyon, farklı frekanstaki sinüs ve kosinüslerin katsayılı toplamı (Fourier serisi) olarak yazılabilir.

M×N boyutlu f(x, y) görüntüsünün **ayrık Fourier dönüşümü (DFT)**:

F(u, v) = Σ_x Σ_y f(x, y) · e^(−j2π(ux/M + vy/N))

ve ters dönüşüm f(x, y) = (1/MN) Σ_u Σ_v F(u, v) · e^(j2π(ux/M + vy/N)). Dönüşüm tümüyle tersinirdir. Görüntü tayfı (frekans bileşenleri) görselleştirilebilir; örnekte bir entegre devrenin elektron mikroskobu görüntüsü ve tayfı gösteriliyor.

### Frekans uzayında süzgeçleme adımları

1. Görüntünün DFT'si F(u, v) hesaplanır.
2. F(u, v), süzgeç fonksiyonu H(u, v) ile çarpılır: G(u, v) = H(u, v) F(u, v).
3. Sonucun ters DFT'si alınır.

### Yumuşatma (alçak geçiren) süzgeçler

Yüksek frekanslar atılarak yumuşatma sağlanır. D(u, v) = [(u − M/2)² + (v − N/2)²]^(1/2) merkezden uzaklık ve D0 kesim uzaklığı olmak üzere:

- **İdeal alçak geçiren**: D ≤ D0 ise H = 1, aksi hâlde 0. D0 = 5, 15, 30, 80, 230 yarıçaplarıyla yapılan örneklerde küçük yarıçapta görüntü çok bulanıklaşır ve halka biçimli salınımlar (ringing) görülür.
- **Butterworth**: H(u, v) = 1 / (1 + [D(u, v)/D0]^(2n)) (n: derece). 2. derece Butterworth'ta ringing çok daha azdır.
- **Gauss**: H(u, v) = e^(−D²(u, v) / 2D0²). Ringing yoktur. Gauss alçak geçiren süzgeç, kopuk metin karakterlerini birleştirmek için de kullanılır.

### Keskinleştirme (yüksek geçiren) süzgeçler

Yüksek geçiren süzgeç, alçak geçirenin tersidir: H_hp(u, v) = 1 − H_lp(u, v).

- **İdeal**: D ≤ D0 ise 0, D > D0 ise 1.
- **Butterworth**: H = 1 / (1 + [D0/D(u, v)]^(2n)).
- **Gauss**: H = 1 − e^(−D²(u, v) / 2D0²).

D0 = 15, 30, 80 için sonuçlar karşılaştırılıyor; ayrıca yüksek frekans vurgulama ve ardından histogram eşitlemenin örneği ile **frekans uzayında Laplace** işleci (uzamsal Laplace maskesinin 2 boyutlu görüntüsüyle karşılaştırılarak) gösteriliyor.

### Hızlı Fourier dönüşümü (FFT) ve uzamsal-frekans karşılaştırması

Fourier tabanlı yöntemlerin yaygınlaşmasının nedeni, dönüşüm süresini 100–600 kat azaltan **FFT** algoritmasıdır. Benzer işler hem uzamsal hem frekans uzayında yapılabilir: uzamsal süzgeçleme daha kolay anlaşılır, frekans uzayında süzgeçleme ise özellikle büyük görüntülerde çok daha hızlıdır.
