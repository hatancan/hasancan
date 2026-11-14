---
baslik: BIL437 Bilgisayarlı Görü: Uzaktan Algılama ve Sayısal Görüntü İşleme (University of South Carolina, John R. Jensen)
ozet: Dr. John R. Jensen'in (University of South Carolina, Coğrafya) Uzaktan Algılama ve Sayısal Görüntü İşleme sunumları: yerinde veri ve uzaktan algılama, süreç, avantajlar ve sınırlar, Landsat, SPOT, AVHRR, MODIS, IKONOS ve AVIRIS gibi sensör sistemleri.
---

BIL437 Bilgisayarlı Görü dersinin son bölümünde (lecture6_1 ve lecture6_2_1 – 6_2_4) dağıtılan beş sunum, **Dr. John R. Jensen** (Department of Geography, University of South Carolina, Columbia) tarafından hazırlanmış "Remote Sensing and Digital Image Processing" ders sunumlarıdır; slaytlardaki kaynak notu "Jensen, 2000/2003/2004" biçimindedir. Aşağıda sunumların metinleri özetlenmiştir; sunumlar ağırlıklı olarak uydu ve hava görüntüleriyle dolu olduğundan görüntüler yazıya alınmamıştır. Beş sunumun orijinali yazının sonunda ZIP olarak indirilebilir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## 1. Uzaktan algılama nedir? (lecture6_1)

**Bilimin amacı** evrensel doğruları keşfetmektir. Bilim insanları fiziksel dünyayı, canlıları ve süreçleri (erozyon, ormansızlaşma, kentsel yayılma) gözlemleyip ölçer.

### Yerinde (in situ) veri

Hipotezi kabul ya da reddetmek için gerekli veri doğrudan sahada toplanabilir; buna *in situ* veri denir. Bu zaman alan, pahalı ve hataya açık bir iştir. Yöntemden kaynaklanan hatalar şunlardan doğabilir: örnekleme tasarımının olgunun uzamsal değişkenliğini yakalayamaması (bazı yerler fazla, bazıları az örneklenir), ölçüm aletlerinin yanlış kullanılması, aletlerin kalibre edilmemiş olması. Yerinde ölçümlere "yer gerçeği (ground truth)" demek yanlıştır; "yer referans verisi" demeliyiz, çünkü o da hata içerir. Örnek yerinde ölçümler: soya fasulyesinde spektroradyometre ölçümü ve yaprak alan indeksi (LAI) ölçümü.

### Uzaktan algılamanın tanımı

ASPRS'nin birleşik tanımı (Colwell, 1997): fotogrametri ve uzaktan algılama, "temassız algılayıcı sistemlerden elde edilen görüntü ve enerji örüntülerinin sayısal gösterimlerinin kaydedilmesi, ölçülmesi ve yorumlanması yoluyla, fiziksel nesneler ve çevre hakkında güvenilir bilgi elde etme sanatı, bilimi ve teknolojisidir". Uzaktan algılama aygıtı, algılayıcının anlık görüş alanı (IFOV) içindeki bir nesne ya da olgu hakkında, onunla doğrudan fiziksel temas olmadan bilgi toplar; algılayıcı hava (suborbital) ya da uydu platformundadır.

### Gözlemler

- Uzaktan algılama bir bilim mi? Sunuma göre uzaktan algılama, matematiğe benzeyen bir araç/tekniktir: bir nesneden ayrılan elektromanyetik ışımanın (EMR) uzaktan ölçülüp matematiksel ve istatistiksel algoritmalarla bilgiye dönüştürülmesi bilimsel bir etkinliktir ve harita bilimlerinin diğer araçlarıyla (kartografya, CBS) uyum içinde çalışır.
- Algılayıcılarla bir nesne (örneğin kavak tepe tacı çapı) ya da bir olgunun coğrafi kapsamı hakkında bilgi alınabilir; yansıyan, yayılan ya da geri saçılan EMR gerçek özelliğin yerine geçen bir göstergedir ve görsel ve/veya sayısal görüntü işlemeyle kalibre edilip bilgiye çevrilmelidir.

### Avantajlar

- Algılayıcı yalnızca yansıyan ya da yayılan EMR'yi kaydediyorsa (pasif) ilgilenilen nesneyi rahatsız etmez.
- Veri sistematik toplanabilir (örneğin 9×9 inç'lik dikey hava fotoğrafı karesi); bu, bazı yerinde çalışmalardaki örnekleme yanlılığını ortadan kaldırabilir.
- Kontrollü koşullarda x, y konumu, z yüksekliği ya da derinliği, biyokütle, sıcaklık, nem içeriği gibi temel biyofiziksel bilgi verebilir.
- Su temini tahmini, ötrofikasyon, noktasal olmayan kirlilik; kentsel kenarda arazi kullanımı değişimi, su talebi ve nüfus tahmini gibi süreçlerin modellenmesi için kritik hâle gelmiştir.

### Sınırlar

- En büyük sınır, çoğu zaman gereğinden fazla övülmesidir; her bilgiyi sağlayan bir çare değil, uzamsal, tayfsal ve zamansal bilgiyi verimli ve ekonomik biçimde sağlama çabasıdır.
- Algılama sistemini, çözünürlükleri, kalibrasyonu, platformu, zamanı ve işleme yöntemini insanlar seçer; bu seçimler hata getirebilir.
- LIDAR, RADAR, SONAR gibi kendi ışımasını gönderen güçlü etkin sistemler incelenen olguyu etkileyebilir.
- Algılayıcılar kalibrasyonlarını yitirebilir; veri toplamak ve işlemek pahalı olabilir.

### Uzaktan algılama süreci

1. Hipotez tanımlanır (tümevarım/tümdengelim; belirlenimci ya da olasılıksal model).
2. Algılayıcı verisini kalibre etmek ve geometrik, radyometrik, tematik özelliklerini değerlendirmek için yerinde ve yardımcı veri toplanır.
3. Uzaktan algılayıcı verisi pasif ya da etkin, analog ya da sayısal aygıtlarla (tercihen yerinde veriyle aynı zamanda) toplanır.
4. Veriler analog/sayısal görüntü işleme, modelleme ve n boyutlu görselleştirmeyle işlenir.
5. Üst veri, işleme geçmişi ve doğruluk bilgisi verilir; sonuçlar görüntü, grafik, istatistik tablo, CBS veritabanı, mekânsal karar destek sistemi gibi biçimlerde iletilir.

Bir optik algılayıcının IFOV'u içinde kaydedilen ışıma L (W m⁻² sr⁻¹), dalga boyu λ, konumun tayfsal yanıtı s(x, y, z), zaman t, kutuplanma, … gibi değişkenlerin bir fonksiyonudur.

## 2. Uzaktan algılama verisi toplama (lecture6_2_1 – 6_2_4)

Sayısal görüntü iki yolla elde edilir: (1) analog (basılı) görüntüyü sayısallaştırmak; (2) Landsat 7 ETM+ gibi zaten sayısal biçimde veri veren algılayıcılar. Analog hava fotoğrafı türleri: siyah-beyaz panokromatik, kızılötesi, normal renkli, yanlış renkli kızılötesi. Sayısallaştırmada doğrusal dizi ya da alan dizisi CCD'li tarayıcılar kullanılır; sayısallaştırıcının anlık görüş alanı (dpi ya da mikrometre) ile fotoğraf ölçeğine göre piksel yer çözünürlüğü arasındaki ilişki gösterilir.

Sunumlar ardından sırayla şu sistemleri tanıtır (sensör özellikleri, bantlar, çözünürlükler ve örnek görüntülerle):

- **Landsat MSS** (Landsat 1–5): Çok Bantlı Tarayıcı, güneşle eşzamanlı yörünge, 79×79 m IFOV; **Landsat 4–5 Thematic Mapper (TM)**: yedi bant, 30×30 m; yaprak yansıması ve nem içeriği; **Landsat 7 ETM+** (30×30 m, ilk görüntü 18 Nisan 1999, Sioux Falls).
- **GOES** (Doğu/Batı kapsama alanı, kızılötesi görüntü), **AVHRR** (veri edinim özellikleri, bant genişlikleri, küresel NDVI bitki örtüsü indeksi görüntüsü).
- Hava platformlu sistemler: **Daedalus AMS**, **ATLAS** (yakın kızılötesi band 6), ölçülü 2,5×2,5 m tarama görüntüleri, Four Mile Creek'in yer sıcaklık haritası (kızılötesi, sıcaklık dilimleme).
- **SPOT** (HRV, CCD doğrusal dizi, 10×10 m pankromatik; Landsat TM ile ayrıntı ve kapsama karşılaştırması; SPOT Vegetation, 10 günlük küresel sentez), **IRS-1D** (5×5 m), **ASTER** (15×15 m), **MODIS** (2.330 km tarama genişliği, Nil Deltası görüntüsü), **MISR**.
- Yüksek çözünürlüklü ticari uydular: **EROS A1** (1,8 m), **IKONOS** (1×1 m pankromatik, 4×4 m çok bantlı, stereo çift, "pan-sharpened" birleşik görüntü).
- **Görüntüleme spektrometresi**: **AVIRIS** veri küpü ve hiperspektral ürün sınıflandırması; sayısal çerçeve kameralar (Positive Systems, Emerge Spatial); 32.000×8.000 dedektörlü sayısal dizi panoramik kamera; SPIN-2.
