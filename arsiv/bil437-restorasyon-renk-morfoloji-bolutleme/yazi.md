---
baslik: BIL437 Bilgisayarlı Görü: Gürültü Giderme, Renkli Görüntü İşleme, Morfolojik İşleme ve Bölütleme
ozet: BIL437 Bilgisayarlı Görü dersinin 4 ve 5. hafta sunumları: gürültü modelleri ve süzgeçleri (ortalama, medyan, sıra istatistiği), band durduran süzgeç, renk modelleri (RGB, HSI), erozyon, dilatasyon, kenar bulma ve eşikleme.
---

BIL437 Bilgisayarlı Görü dersinin Lecture 4_1, 4_2, 5_1, 5_2 ve 5_3 sunumlarının (2012 tarihli, Başkent Üniversitesi'nde 2015 yaz okulunda dağıtılan) ders notu özetidir. Sunumlardaki görüntüler Gonzalez & Woods, *Digital Image Processing* kitabından alınmıştır; slaytlarda yazar adı yazmıyor, ama PDF belge özelliklerinde yazar **Brian Mac Namee** olarak kayıtlı. Orijinal sunumlar yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Görüntü onarma: gürültü giderme (Lecture 4_1)

**Görüntü onarma (restoration)**, bozulmuş görüntüyü düzeltmeye çalışır: bozulma sürecini belirleyip tersine çevirmek; iyileştirmeye benzer ama daha nesneldir.

Gürültü, görüntü edinme (sensörlerin çevre koşullarından etkilenmesi) ve iletim sırasında ortaya çıkar. Gürültülü görüntü şöyle modellenir:

g(x, y) = f(x, y) + η(x, y)

(f: özgün piksel, η: gürültü terimi, g: bozulmuş piksel). Gürültü modelleri: **Gauss** (en yaygın), Rayleigh, Erlang, üstel, düzgün (uniform) ve **dürtü (tuz-biber)** gürültüsü.

### Uzamsal süzgeçlerle gürültü giderme

- **Aritmetik ortalama**: f̂(x, y) = (1/mn) Σ g(s, t); basit yumuşatma, görüntüyü bulanıklaştırır.
- **Geometrik ortalama**: aritmetik ortalamaya benzer yumuşatma, ama ayrıntıyı daha az kaybeder.
- **Harmonik ortalama**: f̂ = mn / Σ (1/g(s, t)); tuz gürültüsünde iyi, biber gürültüsünde başarısız; Gauss gürültüsünde de iyidir.
- **Kontraharmonik ortalama**: f̂ = Σ g^(Q+1) / Σ g^Q; Q süzgecin derecesidir. Q > 0 biber gürültüsünü, Q < 0 tuz gürültüsünü giderir (örnekte Q = 1,5 ve Q = −1,5). Q yanlış seçilirse sonuç felaket olabilir.
- **Sıra istatistiği süzgeçleri**: komşuluktaki piksel değerlerinin sıralanmasına dayanır.
  - **Medyan**: yumuşatma etkisi olmadan mükemmel gürültü giderir; özellikle tuz-biber gürültüsünde iyidir (birkaç geçişle daha da iyileşir).
  - **Max süzgeç** biber gürültüsünde, **min süzgeç** tuz gürültüsünde iyidir.
  - **Orta nokta (midpoint)**: (max + min) / 2; Gauss ve düzgün gürültüde iyidir.
  - **Alfa kırpılmış ortalama**: en düşük d/2 ve en yüksek d/2 seviye atılıp kalan mn − d pikselin ortalaması alınır.

Sayısal bir örnek de verilir: 7×5'lik bir parça içinde 204 ve 0 değerli bozuk pikseller (tuz ve biber) süzgeçlerle gideriliyor.

### Periyodik gürültü ve band durduran süzgeçler

Elektriksel ya da elektromanyetik girişimden kaynaklanan, görüntüde düzenli desenler oluşturan **periyodik gürültü** en iyi Fourier uzayında giderilir: belirli bir frekans aralığı **band durduran süzgeçle** atılır. İdeal band durduran süzgeç: D(u, v) < D0 − W/2 ve D(u, v) > D0 + W/2 için 1, aradaki W genişlikli halkada 0. Butterworth (1. derece) ve Gauss sürümleri de vardır; sinüzoidal gürültü taşıyan görüntü ve Fourier tayfı üzerinde örnek gösterilir.

### Uyarlanır süzgeçler

Uyarlanır (adaptive) süzgeçlerin davranışı, süzgeç penceresi içindeki görüntü özelliklerine göre değişir. Tuz-biber olasılığı Pa = Pb = 0,25 olan görüntüde 7×7 medyan ile uyarlanır medyan süzgeç karşılaştırılıyor.

Özet: Onarma iyileştirmeden daha nesneldir; rastgele gürültüde uzamsal, periyodik gürültüde frekans uzayı teknikleri daha etkilidir.

## Renkli görüntü işleme (Lecture 4_2)

- 1666'da Isaac Newton, güneş ışığının cam prizmadan geçince renk tayfına ayrıldığını buldu.
- Bir nesnede algıladığımız renk, yansıyan ışığın niteliğine bağlıdır (yeşil nesne 500–570 nm aralığını yansıtır, geri kalanı soğurur). Kromatik ışık yaklaşık 400–700 nm aralığını kapsar; insan gözünde 6–7 milyon koni renk görmeyi sağlar.
- Renkli ışığı betimleyen üç nicelik: **ışıma (radiance)**: kaynaktan çıkan toplam enerji (watt); **ışık akısı (luminance)**: gözlemcinin algıladığı enerji (lümen), yüksek ışıma ama düşük ışık akısı olabilir; **parlaklık (brightness)**: öznel, ölçülemeyen şiddet kavramı.
- **CIE renklilik (chromaticity) diyagramı**: x ekseni kırmızının, y ekseni yeşilin oranını gösterir; mavi oranı z = 1 − (x + y). Sınırdaki renkler tamamen doygundur; eşit enerji noktası CIE standardında saf beyazdır. Üç rengin birleşimiyle bütün renk aralığı gösterilemez; RGB monitörlerin ve yüksek kaliteli yazıcıların renk gamutları diyagramda farklı üçgen/şekillerle görünür.

### Renk modelleri

- **RGB**: kırmızı, yeşil, mavi bileşenlerin Kartezyen koordinat sisteminde küp biçiminde gösterimi; siyah orijinde, beyaz orijinden en uzak köşede, cyan-magenta-sarı diğer üç köşededir. Renkli görüntü üç bileşen görüntüsünden oluşur; piksel başına bit sayısı renk derinliğidir. 24 bitlik görüntü 2^24 = 16.777.216 renk verir (tam renk).
- **HSI**: renk (hue), doygunluk (saturation), şiddet (intensity). RGB donanım gerçeklemesi için uygundur, ama insanlar renkleri doğal olarak ton, doygunluk ve parlaklıkla anlatır: RGB renk üretimi, HSI renk betimlemesi için uygundur.

## Morfolojik görüntü işleme (Lecture 5_1)

Bölütleme tamamlandıktan sonra morfolojik işlemlerle bölütlemedeki kusurlar giderilir ve görüntünün biçimi/yapısı hakkında bilgi çıkarılır. Tartışma, nesne piksellerinin 1, arka plan piksellerinin 0 olduğu ikili (bi-level) görüntüler için yapılır.

- **Yapı elemanı (structuring element)** herhangi bir boyut ve şekilde olabilir (derste kolaylık için merkezi orijinli dikdörtgen/artı biçimleri).
- **Sığma (fit)**: yapı elemanındaki tüm "açık" pikseller görüntüdeki açık piksellerin üzerine düşer. **Çarpma (hit)**: yapı elemanındaki herhangi bir açık piksel görüntüdeki açık bir piksele denk gelir.
- **Erozyon (aşındırma)**: f ⊖ s; yapı elemanı g(x, y) için "s, f'ye sığıyorsa 1, aksi hâlde 0". Birleşik nesneleri ayırır, çıkıntıları siler; ama nesneleri küçültür. 3×3 ve 5×5 kare eleman ile disk (yarıçap 5, 10, 20) örnekleri verilmiştir.
- **Dilatasyon (genişletme)**: f ⊕ s; "s, f'ye çarpıyorsa 1". Kopuklukları ve girintileri onarır, nesneleri büyütür.
- Bunların bileşimi olan işlemlere (açma, kapama vb.) ve morfolojik algoritmalara geçilir.

## Bölütleme 1: süreksizlikler, noktalar, çizgiler, kenarlar (Lecture 5_2)

**Bölütleme**, görüntünün piksellerini nesnelerle güçlü ilişkili gruplara ayırır; otomatik bilgisayarlı görü uygulamalarının genellikle ilk adımıdır. Üç tür gri seviye süreksizliği aranır: **nokta, çizgi, kenar**; maske ve korelasyonla bulunur.

- **Nokta algılama**: tek bir maske uygulanır, süzülmüş görüntüde eşiği aşan pikseller nokta sayılır (türbin kanadı röntgeninde örnek).
- **Çizgi algılama**: bir piksel kalınlığında ve belirli yönde (yatay, düşey, +45°, −45°) çizgileri çıkaran maskelerle yapılır (tel bağlantı örneği).
- **Kenar**: iki bölge arasındaki sınırda yer alan bağlı piksel kümesi. 1. türev kenarın yerini, 2. türev kenar yönünü gösterir. Türev tabanlı kenar bulucular gürültüye çok duyarlıdır; bu yüzden kenar bulmadan önce görüntüyü yumuşatmak yararlıdır. Yaygın 3×3 kenar bulucular (3×3 bölge için): yatay ve düşey gradyan bileşenleri birleştirilir.
- **Laplace**, gürültüye çok duyarlı olduğu için tek başına kullanılmaz; **Laplace of Gaussian (LoG, "Meksika şapkası")** Gauss ile gürültü giderip Laplace ile kenar bulur.

## Bölütleme 2: eşikleme (Lecture 5_3)

Eşikleme çoğu bölütleme yaklaşımının ilk adımıdır. Tek eşikle: f(x, y) > T ise g = 1, aksi hâlde 0. Eşik yanlış seçilirse (çok düşük ya da çok yüksek) sonuç kötü olur. Poker oynayan robotun kartları yorumlaması örnek olarak verilir.

**Temel genel (global) eşikleme algoritması**:

1. T için başlangıç tahmini seç (genellikle görüntünün ortalama gri seviyesi).
2. Görüntüyü T ile iki gruba ayır: G1 (gri seviye > T) ve G2 (≤ T).
3. G1 ve G2'nin ortalama gri seviyeleri μ1 ve μ2'yi hesapla.
4. Yeni eşik T = (μ1 + μ2) / 2.
5. T'deki değişim önceden belirlenen sınırdan küçük olana kadar 2–4'ü yinele.

Algoritma, histogram uygunsa (iki tepeli, bimodal) çok iyi çalışır. Başka histogramlar tek eşikle bölütlenemez; düzensiz aydınlatma da tek eşiği bozar (şişelerin içeriğini ayırma örneği). Çare: **uyarlanır (adaptive) eşikleme**: görüntü alt görüntülere bölünür ve her biri ayrı eşiklenir; sorunlu alt görüntüler daha da bölünerek başarılı sonuç alınır.
