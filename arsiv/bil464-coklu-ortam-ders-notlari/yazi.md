---
baslik: BIL464 Çoklu Ortam Sistemleri: Sayısal Teknoloji (Örnekleme, Nicemleme, Veri Depolama ve İletişim) ve Metin
ozet: Mustafa Sert'in (Başkent Üniversitesi) BIL464 Multimedia Systems dersi notları: analogdan sayısala dönüşüm, Nyquist, nicemleme hatası ve SNR, veri boyutları, bant genişliği, bit hızı ve baud hızı, karakter kümeleri, yazı tipleri ve dizgi ölçüleri.
---

**BIL464 Çoklu Ortam Sistemleri (Multimedia Systems)** dersinin ilk iki ders notu: *Lecture 01 – Digital Technology* ve *Lecture 02 – Multimedia Data Types: Text*. Notlar, Başkent Üniversitesi Bilgisayar Mühendisliği Bölümü'nden **Yrd. Doç. Dr. Mustafa Sert**'in (BIL464 Multimedia Systems, 2012) ders sunumlarıdır. Klasörün adı "Bilgisayar Dersi" idi; sunumların başlığından dersin gerçek adı Multimedia Systems olarak anlaşılıyor. İki sunumun orijinali yazının sonunda ZIP olarak indirilebilir. Aşağıda içerik, Türkçe özetle aktarılmıştır.

## Ders 1: Sayısal teknoloji

### Analog ve sayısal

Analog sinyaller sürekli sinyallerdir (akan bir su, grafikteki bir çizgi, sürekli dönen bir radyo düğmesi): iki nokta arasında sonsuz sayıda başka nokta vardır. Ayrık (discrete) sinyaller ise birbirinden net ayrılır. Canlı bir orkestra analog ses dalgaları üretir; standart bir mikrofon analog bir aygıttır ve sesi zamanla değişen sürekli bir gerilim dalgası olarak iletir. Bilgisayarda sürekli sinyalleri bir sayı dizisiyle göstermek gerekir: buna **analogdan sayısala dönüşüm** denir ve iki adımdan oluşur.

1. **Örnekleme**: sürekli sinyalden ayrık noktalarda örnek almak. Birim zaman ya da uzaydaki örnek sayısı **örnekleme hızı** (çözünürlük) olup birimi Hertz'dir (1 Hz = saniyede bir örnek; çoğu zaman kHz kullanılır). Görüntüde örnek noktaları uzayda, seste zamanda eşit aralıklıdır.
2. **Nicemleme (quantisation)**: her örneğin sabit sayıda bitle (örnek boyu ya da **bit derinliği**) gösterilmesi. Genelde 8 bit (256 seviye) ya da 16 bit (65.536 seviye) kullanılır. Dönüşümü yapan aygıta **ADC (analog-digital converter)** denir.

Sayısal işaret çalınırken yeniden kurulmalıdır; yaygın bir teknik **tut ve örnekle (sample and hold)**tir. Orijinale yakın bir işaret için yeterince örnek ve yeterince seviye gerekir.

### Nyquist ve örtüşme

**Nyquist örnekleme teoremi**: işareti yeniden kurabilmek için örnekleme hızı, işaretteki en yüksek frekansın iki katından az olmamalıdır. Örneğin en yüksek frekans 3000 Hz ise örnekleme hızı en az 6000 Hz olmalıdır. Az örneklenirse bazı frekans bileşenleri yanlışlıkla başka frekanslara dönüşür: **örtüşme (aliasing)**. Sunumdaki örnekte 637 Hz'lik bir ses dalgası 770 Hz ile örneklenince daha düşük frekanslı bir dalga olarak yeniden kurulur ve farklı duyulur.

### Nicemleme hatası ve SNR

Seviye sayısı az ise her örnekte büyük hata olur: örnek, en yakın ayrık seviyeye yuvarlanır ve gerçek değerle yuvarlanmış değer arasındaki fark **nicemleme hatasıdır**. Hatanın büyüklüğü **sinyal-gürültü oranı (SNR)** ile ölçülür; çözünürlük arttıkça gürültü azalır, kalite artar. Desibel tanımı güç için 10·log10(I/I0), genlik/gerilim için 20·log10(E/E0)'dır (R sabitken ikisi eşdeğerdir; log10(x²) = 2·log10(x)). Bit derinliğine göre SNR: **8 bit için yaklaşık 48 dB, 16 bit için yaklaşık 96 dB**.

### Veri depolama

Sayısal ortamla çalışmak çok veri işlemeyi gerektirir. Sunum, tipik görüntü, ses ve video dosyalarının boyutlarını tablolaştırır (RGB renk için piksel başına üç bayt; videoda saniyede yaklaşık 30 kare, her kare bir durağan görüntü gibi). Önek uyarısı: kilo/mega/giga bellek boyutlarında 2^10, 2^20, 2^30; Hertz ve veri hızında 10^3, 10^6, 10^9 olarak kullanılır. Üreticiler ortamları büyük göstermek için 10'un kuvvetlerini kullanır; bilgisayarlar ise dosya boyutunu 2'nin kuvvetleriyle gösterir (örneğin 3.686.456 bayt ≈ 3600 kB ≈ 3,52 MB). Derste bellek ve dosya boyutlarında 2'nin, veri hızlarında 10'un kuvvetleri esas alınır. Ardından depolama ortamlarının kapasiteleri listelenir.

### Veri iletişimi

Sayısal ortam dosyaları büyüktür ve paylaşılır (CD/DVD, e-posta, web sayfası); ses ve video **zamana bağlı** ortamlardır: yakalama ve iletim, oynatma hızına yetişmelidir. Bu yüzden bant genişliği ve veri hızı önemlidir. Sunum bant genişliği için üç tanım verir:

1. **Sayısal veri iletişiminde en büyük değişim hızı**: b Hz bant genişliğine sahip ve iki sinyal düzeyli bir sistemde veri hızı d = 2b (bit/s); k düzeyli sistemde **d = 2b·log2(k)**.
2. **Bir sinyalin frekans cinsinden bant genişliği**: w = f_maks − f_min. Örnek: 262, 330 ve 392 Hz bileşenli sinyalde w = 392 − 262 = 130 Hz.
3. **Bir iletişim kanalının bant genişliği**: kanala ayrılan frekans bandı aralığı (radyo ve televizyon bantlarından örneklerle).

**Veri (bit) hızı** bit/s cinsindendir; bant genişliği ise Hz cinsindendir. d = 2b·log2(k) kuramsal bir üst sınırdır; gürültü gerçek hızı sınırlar. Gürültülü kanal için **Shannon teoremi**: **c = b·log2(1 + s/p)** (s: sinyal gücü, p: gürültü gücü). Sunum, yaygın iletişim bağlantıları ve depolama aygıtlarının veri hızlarını tablolaştırır.

**Baud hızı**: en kesin tanımıyla, gönderen ve alan aygıtların bir özelliği olarak saniyedeki sinyal değişimi sayısıdır; bant genişliğiyle eşanlamlıdır, bit hızıyla değil: d = 2b·log2(k) ilişkisi baud hızı ile bit hızını bağlar. Pratikte modemlerin "56 kb/s baud hızı" denen değeri aslında bit hızıdır.

## Ders 2: Çoklu ortam veri tipleri: metin

İçerik: metin nedir, karakter kümeleri, yazı tipleri ve fontlar, anahatlı ve bitmap fontlar, çoklu ortamda metin kullanımı.

**Metin**, çoklu ortam sunumlarının hayati bir öğesidir ve aynı zamanda dilin görsel gösterimi ve kendi başına bir grafik öğedir; metnin nasıl gösterileceğini inceleyen alana **tipografi** denir (karakter şekilleri, aralık, satır ve paragraf düzeni).

### Karakter kümeleri ve kodlama

Soyut karakterler (harfler, rakamlar, noktalama) alfabelerde gruplanır. Bilgisayarda gösterim için karakterlerle saklanan değerler arasında bir eşleme gerekir: **karakter kümesi**. Sistemlerin haberleşmesi için ortak karakter kümesi şarttır.

- **ASCII** (American Standard Code for Information Interchange): 7 bit, en fazla 128 karakter; 95 yazdırılabilir karakter, 0–31 ve 127 kontrol karakteridir. ISO bunu ISO 646 standardı olarak benimsedi.
- **ISO 8859**: 8 bitlik karakterler, birçok bölüm; her bölümün alt 128 karakteri ASCII ile aynıdır.
- **Unicode**: 1991'de Unicode Standard 1.0; sunum sırasında en son sürüm 6.2 (2012, ISO/IEC 10646:2012 ve Türk lirası simgesi). Dünya dillerinin tümünü kapsamaya çalışır; Çince karakter sayısı 27.484'ten fazladır (öncesinde GB2312-80: 6763 basitleştirilmiş karakter, Big5: 13.053 geleneksel karakter, CNS11643-1992: 48.027, HKSCS: Big5'e 3049 karakter ekler).
- **Kodlama (encoding)**: bir kod değerinin saklama ve iletim için bayt dizisine dönüştürüldüğü bir ek eşleme düzeyidir.

### Yazı tipi ve font

**Typeface (yazı tipi ailesi)**, tutarlı tasarımlı ve çoğu zaman birçok boyut ve stil içeren grafik karakterler ailesidir; **font** ise belirli bir tasarımda, boyutta ve stildeki grafik karakter kümesidir (örneğin yazı tipi "Arial", font "Arial Narrow 24 punto").

Karakter ölçüleri: her karakterin bir sınırlayıcı kutusu (bounding box) vardır; orijin genellikle taban çizgisi üzerindedir ve karakterin genişliği sonraki karakterin orijinini belirler. Orijinle kutunun sol kenarı arasındaki uzaklık **sol yan boşluk (left side bearing)**tur. Küçük harflerin yukarı uzayan (b, h) ve aşağı uzayan (g, p, q) kısımlarına **ascender** ve **descender** denir; bunlar olmayan küçük harflerin yüksekliği **x-yüksekliği**, büyük harflerin yüksekliği **büyük harf yüksekliği (cap-height)**dir.

Bir fontu belirlemek için beş öznitelik kullanılır: **aile** (Times, Helvetica, Courier, Garamond, Univers), **biçim** (dik, eğik, italik, küçük büyük harf), **ağırlık** (ince … kalın), **genişlik**, **boyut** (punto: baskıda 1 inç = 72,27 punto, PostScript sistemlerinde 72 punto).

**Bitmap ve anahatlı (outline) fontlar**: bitmap fontlar belirli boyut ve çözünürlüktedir, ölçeklenince çok kötü görünür; anahatlı fontlar karakter anahatlarını içerir, geniş bir boyut aralığında düzgün ölçeklenir ama ekranda görüntülenmek için rasterleştirme gerekir. Günümüzde anahatlı fontlar yaygındır (iki tür: PostScript ve TrueType).

**Metin yerleşimi**: *leading* iki satır tabanı arasındaki uzaklık (12 punto metin için 14, 10 punto için 12 punto); *tracking* karakterler arası boşluk; *kerning* belirli iki karakter arasındaki ek ayardır (örneğin A ve v).

### Çoklu ortamda metin kullanımı için öneriler

- Küçük yazıda en okunaklı fontu seç; süslü fontlar işe yaramaz.
- Aynı çalışmada mümkün olduğunca az yazı tipi kullan; ağırlık, boyut ve italik/kalın ile çeşitlendir.
- Yazı boyutunu mesajın önemiyle orantılı değiştir.
- Büyük başlıklarda doğru kerning yap.
- Farklı renkleri ve metni farklı zeminlere koymanın etkilerini dene.
