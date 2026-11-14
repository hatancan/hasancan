---
baslik: EEM441 Haberleşme I: İletişim Kuramı ders sunumları 7–8 (ELK 307, Nihat Kabaoğlu): açı modülasyonu
ozet: Faz ve frekans modülasyonu, tek tonlu ve dar bantlı FM, FM üretimi ile frekans diskriminatörü ve faz kilitlemeli çevrimle demodülasyon.
---

ELK 307 İletişim Kuramı-I dersinin açı modülasyonu bölümü (Kısım-5): Ders 7 ve 8 sunumları. Ders sunumları ELK 307 İletişim Kuramı-I dersine ve Nihat Kabaoğlu'na aittir (kurum belgede yazmıyor); EEM441 klasöründe bulunduğundan bu derse eklendi. Sunumların PDF kopyaları yazının sonundaki ZIP'tedir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Ders 7: Temel tanımlar, tek tonlu ve dar bantlı FM

### İçerik

Faz Kilitlemeli Çevrim

### Temel Tanımlar

Bir taşıyıcı sinyalin açısının m(t) sinyalinin genliğiyle değiştirilmesi ile elde edilir. Açı, frekans veya faz vasıtasıyla iki ayrı yolla değiştirilebilir. Bu yüzden, açı modülasyonu, seçilen yaklaşıma göre

θi ( t ) , m ( t ) temel bant sinyaliyle orantılı olarak değiştirilir. Modüle edilmiş sinyal Not: φc = 0 kabul edilmiştir.

f i ( t ) , m ( t ) temel bant sinyaliyle doğrusal orantılı olarak değiştirilir. Modüle edilmiş sinyal Not: φc = 0 kabul edilmiştir.

Sinyal sıfır geçişleri düzgün Sinyal genliği sabit değil Sinyal sıfır geçişleri düzgün değil Sinyal genliği sabit FM sinyali Faz Mödülatörü ile veya PM sinyali Frekans Modülatörü ile üretilebilir.

### Tek Tonlu FM

FM sinyallerinin analizi için, mümkün olan en basit durum tek tonlu mesaj f c ‘ den maksimum sapma frekansı Dikkat! Δf, m(t) nin genliğine bağlı. f m m(t) nin genliğine ve frekansına bağlı.

### Örnek

Frekansı 100 MHz olan bir taşıyıcının tepe değeri 3V’ tur. Frekansı 2kHz olan bir sinüsoidal, bu taşıyıcının frekansını modüle etmekte ve taşıyıcı frekansındaki max. sapma 75 KHz olmaktadır. t=0 anında modüle eden sinyalin değeri sıfır ise, modüle edilmiş sinyalin ifadesi

### Tek Tonlu FM

Genlik Modülasyonunun tersine FM doğrusal olmayan bir modülasyondur. FM sinyallerinin spektrumunun m(t) ile bağlantısı basit değildir. FM sinyalinin bant genişliği, m(t)’ ninkinden çok büyüktür. FM sinyallerinin spektrumu, bir taşıyıcı ve etrafına simetrik olarak yerleşmiş sonsuz sayıda yan frekanslar içerir. FM sinyalinin taşıyıcı genliği J0(β) ile modülasyon indeksine Modüle eden sinuzoidal sinyal m(t) nin genlik ve frekansındaki değişmeler FM sinyalinin spektrumunu nasıl etkiler? Bunu iki ayrı durumda incelemek gerekir: 1. Frekans sabit, Genlik değişken 2. Genlik sabit, Frekans değişken

### Örnek

FM’de modüle eden sinyalin genliği 2 katına çıkar ve frekansı da yarıya düşerse, maksimum frekans sapması / komşu spektral bileşenler arasındaki mesafe, c) azalır/aynı kalır d) artar/aynı kalır e) bir şey söylenemez c (t ) = Ac cos (2π f c t ) taşıyıcı sinyalini bir AM bir de FM yapmaktadır. FM sinyalinin maksimum frekans sapması, AM sinyalinin bant genişliğinin 4 katı olacak şekilde ayarlandığına göre, FM sinyalinin modülasyon indeksi nedir?

### Tek Tonlu FM

Bessel Fonksiyonunun Özellikleri

### Dar Bantlı FM

β  1 olduğunda FM spektrumunun J 0 ( β ) ve J1 ( β ) haricindeki bileşenleri ihmal edilebilir değerde olduğundan, sinyal sadece yan frekanslarından oluşmaktadır. Bu durumda sinyal, Darbant FM olarak β  1 için sinyal bileşenlerinden sadece n= -1, 0, 1 için olanları anlamlıdır. genişliği ile aynıdır.

## Ders 8: FM üretimi ve demodülasyonu

### İçerik

Faz Kilitlemeli Çevrim

### FM Sinyallerinin Üretilmesi

FM sinyallerinin üretilmesi için iki yöntem vardır: Darbantlı FM işaretinin bir frekans çarpıcının girişine uygulanması ile çarpıcı çıkışında genişbantlı FM işareti dolaylı olarak elde edilmiş olur. FM sinyalinin genel ifadesi:

cos(a+b)= cosa.cosb-sina.sinb eşitliğinden yararlanarak FM sinyali aşağıdaki gibi yazılabilir: Darbantlı FM için φ ( t ) < 1 olduğunda, yaklaşıklıkları yapılabilir. Bu sayede, darbantlı FM sinyali şeklinde ya da aşağıdaki gibi ifade edebiliriz.

Öyleyse, darbantlı FM sinyali bir sinüzoidal taşıyıcının fazının m ( t ) ‘ nin integrali ile modüle edilmesi sonucu elde edilebilir. Elde edilen bu darbantlı FM sinyali, modülasyon indeksi β ‘ yı artırmak suretiyle geniş bantlı FM sinyalini dolaylı olarak elde etmek mümkündür. Bu esasa uygun olarak tasarlanmış modülatörlere Armstrong FM Modülatörü adı verilir.

m ( t ) = Am cos ( 2π f m t ) olarak seçilirse, darbantlı FM sinyali Frekans çarpıcı, girişindeki işaretin ansal frekansını n ile çarparak çıkışa iletir. Çıkıştaki bu sinyal genişbantlı FM sinyalidir. n çarpanının değeri, elde edilmek istenen β değerine göre seçilir.

### Armstrong FM Vericisi

Tipik bir Armstrong FM Vericisi

Blok diyagrama göre, frekans bileşenleri fm=50Hz ile 15kHz arasındaki ses işareti m ( t ) ‘ nin ∆f=75kHz’ lik bir FM bandı içinde ve fc=91.2MHz frekansında yayınlanması için blok diyagramdaki hesaplamaların nasıl yapıldığını inceleyelim. 5 ve 6 numaralı noktalarda β arasında değerler alır. Faz modülatörü çıkışında (2 numaralı noktada) darbantlı FM sinyali olabilmesi için β1 < 0.5 olmalı. Genişbantlı FM sinyalinin (5 ve 6 numaralı noktalarda) maksimum modülasyon göstergesi değerini alabilmesi için n = 1500 0.5 = 3000 ile çarpılması gerekir. Bu çarpma iki aşamada yapılabilir ( n = 3000 ≅ 64 × 48 = 3072 ). Bu durumda, 2 numaralı noktadaki dar bantlı FM işaretine ait değerler bulunur. Darbantlı FM sinyalinin 3000 ile çarpılması taşıyıcı frekansını 200kHz’ den 600MHz’ e çıkarır. Bu değer ticari FM yayınları için ayrılan 88-108MHz sınırlarının dışındadır. Bu nedenle, frekans çarpma ve kaydırma işlemleri beraber yapılır. Maksimum modülasyon göstergesini f mmin değeri, FM sinyalinin bantgenişliğini ise f mmax değeri belirler.

### Doğrudan FM Üretimi

 Modüle eden işaretin genlik değerinin taşıyıcı frekansını doğrudan etkilediği bir yöntemdir.  Dolaylı FM sistemlerine göre daha az frekans çarpması gerektirir.  Q çarpanı yüksek olan rezonans devresinin rezonans frekansı, modüle eden işaretin genliğine bağlı olarak değiştirilir.  Q çarpanı ne kadar büyükse rezonans devresinin kayıpları o kadar az, seçiciliği ise o oranda fazladır.  Seri rezonans devresi için  Paralel rezonans devresi için Q p = R ωc L = ωc RC ωc = 1 LC ⇒ Rezonans (taşıyıcı) frekansı

Rezonans devresindeki kapasitans C0 , m ( t ) ' nin sıfır olduğu durumdaki kapasitans Not: Uygulamada VCO tümleşik C0 durumunda ansal frekans Güç serisi açınımı kullanılarak Bu da gösteriyor ki, kapasitans değişmesi çok küçük değerde olmasına rağmen, taşıyıcı frekansı yüksek olduğu için frekans sapması ∆f istenilen değerlere

### Doğrudan FM Vericisi

Doğrudan FM Vericisi Blok Şeması

### FM Sinyallerinin Demodülasyonu

 FM sinyalinden m(t) işaretinin yeniden elde edilebilmesi için, FM sinyalinin frekans değişimiyle doğru orantılı olarak genlik değişimine dönüştürülmesi  Frekansı gerilime çevirme işlemini yapan aygıta ayırtaç (discriminator) denir. Bu aygıt, girişine uygulanan işaretin fazının türevini alıp çıkışa iletir.  FM sinyalinin türevi alınırsa elde edilir. Eğer Ac (t ) sabit ise birinci terim sıfır olur. Uygulamada bu genliğin zamanla değişimini önlemek için bir sınırlayıcı (limiter) devre

 İkinci terimin genliği m(t) ile orantılı değiştiğinden, bu terim genlik zaman sıfır olmaz. Bu durumda, m(t) sinyalini zarf çözücü yardımıyla elde FM Çözücü Blok Diyagramı

Sınırlayıcı (Limiter): Bir keskin sınırlayıcı (hard limiter) ve bir bantgeçiren Sınırlayıcı Devre Özeğrisi

Türev Alıcı: Uygulamada bir sinyalin türevi üç farklı yöntemle alınabilir.  Doğrudan Türev Alma (Direct Differentiation)  Frekans Alanında Türev Alma (Frequency Domain Differentiation)  Zaman Gecikmeli Türev Alma (Time Delay Differentiation) Doğrudan Türev Alma Yöntemi Yarım Dalga Doğrultucu Alçak Geçiren Filtre Türev alma işlemi, kapasitörün akım gerilim ilişkisinden yararlanılarak yapılmaktadır. Kapasitaörün akımı Diyot ideal kabul edilirse, I ( t )‘ nin negatif alternanslarında akım diyot üzerinden akacağı için ie = 0 olur. Pozitif alternanslarda ise akım transistörün emetöründen geçer ve emetör akımı aşağıdaki gibi ifade edilir: Trigonometrik özdeşlikler kullanılarak, ic ( t ) ‘ nin temel bantta ve fc, 2fc,… frekanslarında bileşenlerden oluştuğu bulunabilir. AGF temelbant ve doğru akım sinyallerini çıkış olarak verir. C1 kapasitörü de DC bileşeni eler. Sonuçta, diskriminatör çıkışı aşağıdaki gibi olur.

Frekans Alanında Türev Alma Yöntemi Fourier dönüşümü özelliklerinden bilindiği üzere, zaman alanında türev alma, frekans alanında jw (ya da j2π) ile çarpma işlemine karşılık gelir. FM işaretinin frekans bandında, aktarım işlevi jw ile doğrusal olarak değişen bir sistem türev alma amacıyla kullanılabilir. Örneğin, rezonans devresinin doğrusal bölgesi bu özelliğe sahiptir.

Dengeli Diskriminatör (Balanced Modulator) Üst üste konulmuş iki eğim çözücü kullanılarak doğrusal bölgenin artırılması mümkün. Dengeli ayırtaç çift harmoniklerin neden olduğu bozulmayı ve FM sinyalindeki istenmeyen genlik modülasyonunun neden olacağı

Bu durumda RL devresi türev alıcı gibi çalışır. Zaman Gecikmeli Türev Alma Zaman gecikmeli türev alıcılar türevin tanımını esas alan bir çalışma prensibine sahiptirler. Bu esasa göre çalışan diskriminatör, zaman gecikmeli demodülatör olarak adlandırılır.

FM Sinyallerinin Çözümünde Kullanılan Diğer Yöntemler Sıfır Geçiş Çözücü (Zero Crossing Detector) Bir aralıktaki sıfır geçiş sayısı m ( t ) ‘ nin o aralıktaki genliği ile doğru orantılıdır. Faz Kilitlemeli Döngü (Phase Locked Loop) Faz Kilitlemeli Döngü Faz Kilitlemeli Döngü Doğrusal Olmayan Modeli

Geri Beslemeli FM Çözücü (Frequency Demodulator with Feedback) Tipik Bir FM Alıcısı

*Not: Metin, slaytlardan otomatik çıkarılıp düzenlendi; denklemler ve şekiller metne dökülemediğinden ilgili kısımlar atlanmıştır. Tam hâli için yazının sonundaki PDF dosyalarına bakınız.*
