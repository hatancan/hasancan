---
baslik: BIL437 Bilgisayarlı Görü: Sayısal Görüntü İşlemeye Giriş, Görüntü Temelleri, Histogram ve Nokta İşleme
ozet: BIL437 Bilgisayarlı Görü (Computer Vision) dersinin ilk dört sunumu: sayısal görüntü nedir, insan görme sistemi, örnekleme ve nicemleme, histogram eşitleme, logaritmik ve üstel (gamma) dönüşümler.
---

Bu yazı, Başkent Üniversitesi'nde 2015 yaz okulunda aldığım **BIL437 Bilgisayarlı Görü (Computer Vision)** dersinin ilk dört sunumunun (Lecture 1_1 – 1_4) ders notu özetidir. Klasör adı "Bilgisayar Güvenliği" olsa da sunumların başlığı "Bil-437 Computer Vision", laboratuvar föylerinin başlığı ise "İmge İşleme"dir; içerik sayısal görüntü işlemedir. Slaytlardaki görüntülerin kaynağı olarak Gonzalez & Woods, *Digital Image Processing* (2002) belirtiliyor; slaytlarda yazar adı yazmıyor, ama PDF belge özelliklerinde yazar **Brian Mac Namee** olarak kayıtlı. Dört sunumun orijinali yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## 1. Giriş: sayısal görüntü ve görüntü işleme

Derse "bir resim on bin kelimeye bedeldir" sözüyle başlanıyor.

- **Sayısal görüntü**, iki boyutlu bir görüntünün sonlu sayıda sayısal değerle (piksel) gösterimidir. Piksel değerleri gri seviye, renk, yükseklik, saydamlık gibi şeyleri temsil edebilir. Sayısallaştırma, görüntünün gerçek sahnenin bir yaklaşığı olması demektir.
- Yaygın biçimler: nokta başına 1 örnek (siyah-beyaz ya da gri), 3 örnek (R, G, B), 4 örnek (R, G, B ve alfa/saydamlık). Derste çoğunlukla gri seviyeli görüntüler kullanılıyor.
- Görüntü işlemenin iki ana işi: insan yorumu için görüntü bilgisini iyileştirmek; depolama, iletim ve makine algısı için görüntü verisini işlemek.
- İşleme düzeyleri: **alt düzey** (girdi görüntü, çıktı görüntü; gürültü giderme, keskinleştirme), **orta düzey** (girdi görüntü, çıktı öznitelik; nesne bölütleme ve tanıma), **üst düzey** (girdi öznitelik, çıktı anlama; sahne anlama, otonom gezinme).

### Kısa tarihçe

- 1920'ler: gazete sektöründe Bartlane kablo resim iletimi; Londra–New York arası denizaltı kablosuyla görüntüler kodlanıp gönderiliyor, alıcıda telgraf yazıcısıyla yeniden oluşturuluyor. Sonraki iyileştirmelerle ton sayısı 15'e çıkıyor.
- 1960'lar: uzay yarışı ve bilgisayarlar; 1964'te Ranger 7 ay görüntülerinin bilgisayarla iyileştirilmesi.
- 1970'ler: tıpta kullanım; 1979'da Hounsfield ve Cormack bilgisayarlı tomografi (CAT) icadıyla tıp Nobeli'ni paylaşıyor.
- 1980'lerden bugüne: görüntü iyileştirme/onarma, sanatsal efektler, tıbbi görselleştirme, endüstriyel denetim, adli bilişim, insan-bilgisayar arayüzleri.

Sunumdaki uygulama örnekleri: Hubble teleskobunun hatalı aynasından gelen görüntülerin düzeltilmesi, köpek kalbi MR kesitinde kenar bulma, uydu görüntüleri ve CBS (gece ışıkları haritası), baskılı devre kartı (PCB) denetimi, plaka ve parmak izi tanıma, yüz ve hareket tanıma.

### Sayısal görüntü işlemenin temel aşamaları

Görüntü edinme, görüntü iyileştirme, görüntü onarma, morfolojik işleme, bölütleme, nesne tanıma, temsil ve betimleme, görüntü sıkıştırma ve renkli görüntü işleme; hepsi bir "bilgi tabanı" (problem alanı) etrafında toplanıyor.

## 2. Sayısal görüntü temelleri

### İnsan görme sistemi

- Mercek, ışığı retinaya odaklar. Retinada yaklaşık 6–7 milyon **koni** (renge duyarlı, fovea çevresinde yoğun) ve 75–150 milyon **çubuk** (düşük ışığa duyarlı, daha yaygın) bulunur.
- Kör nokta deneyi: kâğıda 6 inç arayla bir nokta ve bir çarpı çizilir, sağ göz kapatılıp sol gözle çarpıya bakılırken kâğıt yüzden yavaşça yaklaştırılınca nokta kaybolur.
- Göz yaklaşık 10^10 farklı ışık şiddetini algılayabilir; ama aynı anda ayırt edebildiği düzey sayısı çok daha azdır (parlaklık uyumu). Algılanan şiddet çevresindeki bölgelere de bağlıdır (Mach bantları, optik yanılsamalar).

### Işık ve elektromanyetik tayf

Işık, elektromanyetik tayfın gözün algılayabildiği dar bir parçasıdır. Algıladığımız renk, nesneden yansıyan ışığın niteliğine bağlıdır: beyaz ışık yeşil bir nesneye düştüğünde çoğu dalga boyu soğurulur, yeşil yansır.

### Görüntü gösterimi ve edinimi

- Görüntü M satır ve N sütunluk piksel dizisidir; gri seviyeler çoğunlukla 0 (siyah) – 255 (beyaz) aralığındadır ve görüntü f(satır, sütun) matrisi olarak ele alınır.
- Görüntü, bir sahnenin aydınlatılıp nesnelerden yansıyan enerjinin emilmesiyle oluşur (röntgen, ultrason, elektron mikroskobu da aynı mantıkta). Gelen enerji sensör malzemesinde gerilim üretir; sensörler tek, şerit (çizgi) ya da dizi (matris) hâlinde düzenlenir.

### Örnekleme, nicemleme ve çözünürlük

- **Örnekleme**: uzayda sınırlı sayıda noktada ölçüm; **nicemleme (quantisation)**: sürekli genlik değerlerinin sınırlı sayıda seviyeye yuvarlanması.
- **Uzamsal çözünürlük**: görüntüde ayırt edilebilen en küçük ayrıntı (piksel boyutu, baskıda DPI).
- **Yoğunluk seviyesi çözünürlüğü**: seviye sayısı 2^k; 1 bit = 2, 4 bit = 16, 8 bit = 256, 16 bit = 65.536 seviye. Seviye sayısı düştükçe (256 → 128 → 64 → 32 → 16 → 8 → 4 → 2) sahte konturlar belirir.
- "Ne kadar çözünürlük yeter?" sorusunun yanıtı, görüntüde ne görmek istendiğine bağlıdır: araç saymak için yeterli bir görüntü plaka okumak için yetmeyebilir.

## 3. Görüntü iyileştirme: histogram işleme

Görüntü iyileştirme, görüntüyü daha kullanışlı yapma işidir: ayrıntıyı vurgulamak, gürültüyü gidermek, daha hoş göstermek. Teknikler iki gruba ayrılır:

- **Uzamsal bölge** teknikleri: pikseller üzerinde doğrudan işlem,
- **Frekans bölgesi** teknikleri: Fourier ya da dalgacık dönüşümü üzerinde işlem.

Bu derste gri seviyeler çoğu işlemde [0, 1] aralığında alınır (0 siyah, 1 beyaz).

**Histogram**, görüntüdeki gri seviyelerin dağılımını gösterir ve özellikle bölütlemede çok işe yarar. Koyu görüntünün histogramı sola, parlak görüntünün sağa yığılır; yüksek kontrastlı görüntünün histogramı en düzgün yayılandır.

**Histogram eşitleme**, frekansları yayarak koyu ya da soluk görüntüleri düzeltir:

- s_k = T(r_k) = Σ (j = 1..k) p_r(r_j) = Σ (j = 1..k) n_j / n
- r_k: girdi şiddeti, s_k: işlenmiş şiddet, n_j: j şiddetinin sıklığı, n: toplam piksel sayısı.

## 4. Nokta işleme ve gri seviye dönüşümleri

Çıktı pikselinin değeri yalnızca aynı yerdeki girdi pikseline bağlıysa s = T(r) biçiminde yazılır.

- **Eşikleme**: r ≤ eşik ise s = 0,0; r > eşik ise s = 1,0.
- **Negatif/özdeşlik** (doğrusal), **logaritmik** ve **üstel** (kuvvet yasası) dönüşümler en yaygın üç gruptur.
- **Logaritmik dönüşüm**: s = c · log(1 + r). Dar bir düşük gri seviye aralığını geniş bir çıktı aralığına açar; değer aralığı çok geniş olan girdiler için yararlıdır (örneğin bir görüntünün Fourier tayfını görünür kılmak). Ters log dönüşümü tersini yapar. Genellikle c = 1 alınır.
- **Kuvvet yasası (gamma)**: s = c · r^γ. γ < 1 koyu girdi aralığını genişletir (örnekte γ = 0,6; 0,4; 0,3 ile kırık omurga MR görüntüsü), γ > 1 görüntüyü koyulaştırır (γ = 3,0; 4,0; 5,0 ile pist havadan fotoğrafı). Monitörlerin tepkisi doğrusal olmadığından **gama düzeltmesi** bu dönüşümle yapılır.
- **Parçalı doğrusal dönüşümler**: kullanıcı tanımlı eğrilerle kontrast germe.
- **Gri seviye dilimleme**: belirli bir gri aralığı vurgulanır, diğer seviyeler bastırılır ya da korunur.

Bir sonraki konu komşuluk işlemleri, süzgeçleme ve evrişimdir; bkz. serinin ikinci yazısı.
