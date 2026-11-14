---
baslik: EEM441 Haberleşme I: İletişim Kuramı ders sunumları 1–3 (ELK 307, Nihat Kabaoğlu)
ozet: İletişim sistemlerine genel bakış, sinyaller ve sistemlerin temelleri, Fourier dönüşümü, spektral yoğunluk, Hilbert dönüşümü ve zarflar.
---

ELK 307 İletişim Kuramı-I dersinin ilk üç sunumu (Nihat Kabaoğlu). Önerilen kitap Simon Haykin, *Communication Systems* (4. baskı, Wiley, 2001); diğer kaynaklar arasında Couch ve Ziemer–Tranter'in kitapları ile Haluk Derin–Murat Aşkar'ın Türkçe İletişim Kuramı kitabı anılır. Ders sunumları ELK 307 İletişim Kuramı-I dersine ve Nihat Kabaoğlu'na aittir (kurum belgede yazmıyor); EEM441 klasöründe bulunduğundan bu derse eklendi. Sunumların PDF kopyaları yazının sonundaki ZIP'tedir.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## Ders 1: İletişim sistemlerine genel bakış

### Tavsiye Edilen Kitaplar

Simon Haykin, “Communication Systems”, Fourth Edition, Wiley, 2001, ISBN: 047117869-1 (Derste takip edilecek).  Digital & Analog Communication Systems, (7/E, PEARSON), Leon W. Couch, ISBN-10: 0131424920, ISBN-13:  R.E. Ziemer, W.H. Tranter, “Principles of Communication Systems, Modulation and Noise”, 5th Edition, ISBN:

### Diğer Faydalı Kaynaklar

 Haluk Derin, Murat Aşkar, “İletişim Kuramı Modülasyon Yöntemleri, 2’inci baskı”,  Demir Öner, “İletişim Kuramı-I Ders  J.G.Proakis, M.Salehi, “Fundamentals of Communication Systems”, Prentice-Hall,

### İçerik

İletişim Sistemlerine Genel Bakış İletişim Sisteminin Öğeleri İletişim Sistemlerinin Kısıtlamaları Analog ve Sayısal Mesajlar Modülasyon ve Modülasyonun Gerekliliği Sayısal Haberleşmenin Analog Haberleşmeye Olan Üstünlükleri Sinyaller ve Sistemlerin Temelleri Trigonometrik ve Üstel Fourier Serileri ve Fourier Dönüşümü Sinyallerin Doğrusal Sistemlerden İletimi Enerji ve Güç Spektrumları, Öz ve Çapraz İlinti Fonksiyonları Hilbert Dönüşümü ve Özellikleri, Ön Zarf ve Kompleks Zarf Kavramları Bant Geçiren Sinyal ve Sistemler Faz ve Grup Gecikmesi

Çift Yanbant ve Tek yanbant Modülasyonları Darbantlı Frekans Modülasyonu Genişbantlı Frekans Modülasyonu Frekans Modülasyonlu İşaret Üretimi ve Çözümü Örnekleme ve Darbe Modülasyonları Zaman Bölmeli Çoğullama Frekans Bölmeli Çoğullama Darbe Modülasyonları: PAM, PPM, PWM, PCM Bantgenişliği, Bilgi İletim Hızı, Kanal Kapasitesi

### Giriş

Bir iletişim sisteminin amacı, KAYNAK adı verilen bir noktadan HEDEF adı verilen bir başka noktaya bilgi  Telefon, radyo ve televizyon haberleşme sistemlerine verilebilecek en alışılmış örneklerdir.  Haberleşme sistemleri haberleşmenin türüne göre  Tasarımda, kaynak sayısı, kullanıcı sayısı, uzaklık, kullanıcıların durağan ya da gezgin oluşları, sistemin emniyeti, güvenlik gibi çeşitli faktörler göz önüne alınır.

### İletişim sistemlerinin Öğeleri

 Tipik bir haberleşme sistemi aşağıdaki gibi

### Bir İletişim Sisteminin Öğeleri

Kaynak : İnsan sesi, ışık, ısı gibi mesajları oluşturur.  Giriş Dönüştürücüsü : Elektriksel olmayan giriş mesajını elektriksel dalga formuna dönüştürür. (Temel bant sinyal)  Verici : Verimli iletim için temel bant sinyalde değişiklik  İletim Ortamı (Kanal) : Verici çıkışının gönderildiği ortam (Koaksiyel kablo, dalga klavuzu, fiber optik hat, ya  Alıcı : Vericide ve kanalda yapılan değişikliklerin etkisini ortadan kaldırmak için alınan sinyali işler.  Çıkış Dönüştürücüsü : Elektriksel dalga formunu kullanıcının ihtiyaç duyacağı orijinal yapısına dönüştürür.  Hedef : Mesajın iletileceği birim. İnsan, bilgisayar gibi.

### İletişim Sistemlerinin Kısıtlamaları

İletilen sinyal, iletim ortamının neden olduğu aşağıda sıralanan istenmeyen etkilere maruz kalır : GÜRÜLTÜ : Sistemin dışındaki ya da içindeki doğal süreçler tarafından üretilen, rasgele ve öngörülemeyen Harici Gürültü Kaynakları : Elektrikli cihazların kontrol anahtarları, otomobil ateşleme radyasyonu, floresan ışıkları, güneş ışınları, elektrik fırtınaları gibi. Gerekli önlem alındığında, harici gürültü en aza indirgenebilir hatta yok edilebilir. Dahili Gürültü Kaynakları : İletkenlerdeki elektronların ısıl hareketi (termal gürültü), elektronik aygıtlardaki yüklü taşıyıcıların rasgele emisyonu, difüzyonu ya da yeniden birleşmeleri (çarpma gürültüsü). Gerekli önlem alındığında, dahili gürültü azaltılabilir, ancak asla yok edilemez.

İletişim hızında sınırlama getiren en temel unsurlardan birisi Sinyal Gürültü Oranı (SNR) Vericiden uzaklaştıkça gürültü seviyesi artarken işaretin gücü azalır. Bu nedenle SNR kanal boyunca sürekli azalır. Zayıflamayı önlemek amacıyla alınan sinyali kuvvetlendirmek gürültüyü de kuvvetlendirir. Ayrıca, böyle bir durumda, yükselteç devresinin oluşturacağı gürültü nedeniyle SNR daha da kötüleşecektir. SNR’ ı iyileştirmek için alıcıda bazı özel filtreler kullanılır.

ZAYIFLAMA : Sinyalin iletim ortamında ilerlerken gücünde meydana gelen azalma olarak tanımlanır. İletim kaybı olarak da adlandırılır. Uzaklık ve frekansla doğru orantılıdır. İletim ortamı olarak atmosferin kullanılması durumunda yağmur ve kar da zayıflamayı artıran bir etki yapar. İletim ortamı boyunca repetörler kullanılarak, alıcıda ise kanalın genlik ve faz karakteristiğinin tam tersi genlik ve faz karakteristiğine sahip özel filtreler(equalizer: denkleştirici) kullanılarak zayıflama önlenebilir. DİSTORSİYON : Sistemin kusurlu cevabının neden olduğu dalga şeklindeki değişiklikler olarak tanımlanır. Distorsiyon iletilen sinyalin şeklini bozar. Çıkış Sinyali (Distorsiyona uğramış)

Distorsiyonu önlemek için sistemin bantgenişliği sistem cevap karakteristiğinin sabit olduğu bölgede seçilmelidir ve sistemin bantgenişliği sinyalin bantgenişliğinden büyük olmalıdır. Ancak, pratik uygulamalar için bu koşulları yerine getirmek genelde mümkün değildir. Doğrusal distorsiyon olması durumunda, distorsiyon ortadan kaldırılabilir, ya da alıcıda denkleştirici kullanılarak en aza GİRİŞİM : Aynı frekans bandındaki iki ya da daha fazla sinyalin kombinezonu nedeniyle oluşur. Girişim, eklenmiş iki sinyal sonucu oluşan daha kuvvetli bir sinyal meydana getirebileceği gibi birbirinin gücünü azaltan bir etkileşim sonucunda daha zayıf bir sinyal de meydana getirebilir.

### Analog ve Sayısal Mesajlar

 Analog Mesajlar : Değerleri sürekli bir bölgede değişen veriler ile karakterize edilirler. Analog Mesajlara Örnekler Belli bir bölgenin atmosferik basıncı ya da sıcaklığı, mikrofonun çıkışındaki ses sinyali gibi  Sayısal Mesajlar : Sonlu sayıdaki semboller ile Sayısal Mesajlara Örnekler Morse alfabesi ile kodlanmış telgraf mesajı, bilgisayar Not : İkili Sayısal Mesaj iki sembolden meydana getirilir. M-li Sayısal Mesaj M sembolden meydana getirilir.

Alıcının görevi, kanalın çıkışındaki gürültülü ve bozulmuş olan sinyalden mesajı elde etmesidir.  Sayısal mesajlar sonlu sayıda elektrik sinyal kümesi kullanılarak iletildikleri için sayısal sinyallerden mesajın çıkarılması analog olanlara göre daha kolaydır. Alınan sinyal (Gürültüsüz) Alınan sinyal (Gürültülü) Alıcıda yeniden üretilen sinyal

### Modülasyon

 Çeşitli bilgi kaynaklarından üretilen temel band sinyallerin verilen bir kanal üzerinden her zaman doğrudan iletimi mümkün değildir. Bu yüzden, temel band sinyali yüksek frekanslı taşıyıcı sinyalin bazı parametrelerini değiştirmek için kullanılır. Bu işlem MODÜLASYON olarak bilinir.  Alıcıda ise, temel band sinyali elde edebilmek için DEMODÜLASYON adı verilen vericideki modülasyon işleminin tersi bir işlemden geçer.

Taşıyıcı dalga tipine bağlı olarak iki tür  Sürekli Dalga Modülasyonu : Burada taşıyıcı yüksek frekanslı bir sinüstür. Bu sinüsün parametrelerinden biri (genlik, frekans ya da faz) temel bant sinyalin genliği ile orantılı olarak Analog Sürekli Dalga Modülasyonu : Burada modüle eden sinyal analogtur. Genlik Modülasyonu(AM), Frekans Modülasyonu(FM)1 ve Faz Modülasyonu(PM)1 1 : Bazen FM ve PM birlikte Açı Modülasyonu (Angle Modulation) olarak da adlandırılır.

Modüle edici (temel bant) sinyal Genlik modüleli dalga Frekans ya da Faz modüleli dalga

Sayısal Sürekli Dalga Modülasyonu : Burada modüle eden sinyal sayısaldır ve bu sinyal sinüzoidal taşıyıcının genlik, frekans ve fazını kendi genliğiyle orantılı olarak değiştirir. Modüle edici sinyalin ikili ya da M’ li oluşuna bağlı olarak sayısal sürekli dalga modülasyonu iki türdür.  İkili Modülasyon : Burada, modüle edici sinyal sıfıra dönmeyen (NRZ) dikdörtgen darbelerden oluşur. Modüle edilen parametre bir ayrık değerden diğerine anahtarlanır. Bu sayede aşağıdaki modülasyon yöntemleri elde edilir : Genlik Kaydırmalı Anahtarlama (ASK) ya da On-Off Anahtarlama (OOK) Frekans Kaydırmalı Anahtarlama (FSK) Faz Kaydırmalı Anahtarlama (PSK) ya da Tersine Faz Çevirmeli Anahtarlama (PRK)

Sayısal Modüleli Dalga Şekilleri; (a) Temel bant işaret

Diğer ikili modülasyon türleri şunlardır : Türevsel PSK (DPSK) Minimum Kaydırmalı Anahtarlama (MSK) ya da Hızlı FSK ya da Sürekli Fazlı PSK  Dörtlü Taşıyıcılı Modülasyon : Birbirine dik fazlı iki taşıyıcı kullanan bir modülasyon. Bu modülasyon türü için Dörtlü Genlik Modülasyonu (QAM) tipik bir  M’ li Modülasyon : Haberleşmek için M sembol kullanan modülasyon türü. M sembol şunlardan M farklı genlik seviyesi (Çok genlikli sinyalleşme) M farklı faz (Çok fazlı sinyalleşme) M farklı genlik ve faz kombinasyonu (M’li APK)

4’lü çok genlikli alfabe 4’lü çok genlikli sinyal

 Darbe Modülasyonu : Burada taşıyıcı periyodik darbe trenidir. Darbelerin genlik, genişlik ve pozisyonları temel bant sinyalin genliğiyle orantılı olarak değiştirilerek aşağıdaki modülasyon türleri Darbe Genlik Modülasyonu (PAM) Darbe Genişlik Modülasyonu (PWM) ya da Darbe Süre Modülasyonu (PDM) Darbe Konum Modülasyonu (PPM) PAM sinyalinin uygun bir şekilde kodlanmasıyla  Darbe Kod Modülasyonu (PCM)  Türevsel Darbe Kod Modülasyonu (DPCM)  Uyarlamalı Delta Modülasyonu (ADM)

### Modülasyonun Gerekliliği

Modülasyon Etkin Yayılım Sağlar Elekromanyetik enerjinin etkin bir şekilde yayılabilmesi için verici antenin boyutları yayılacak sinyalin dalga boyunun onda biri mertebelerinde ya da daha fazla λ=c/f (c=3x108 m/sn) eşitliği dikkate alındığında, taşıyıcı frekansı arttıkça anten boyutunun küçüleceği görülebilir. Örneğin, f = 100Hz ile 3000Hz arasındaki bir bantda bulunan ses sinyalinin dalga boyu λ = 3000km ile 100km arasındadır. Eğer bu ses sinyali f = 100MHz’ lik bir taşıyıcıyı modüle ederek iletilirse, dalga boyu λ=3m’ ye Bu nedenle, temel bantlı sinyalin frekans bileşenlerini taşıyıcı sinyalin frekansına kaydırılabilmesi için modülasyona ihtiyaç vardır.

Modülasyon Eşzamanlı İletim Olanağı Sunar Modülasyon aynı iletim ortamı üzerinden aynı anda bir çok temel bant sinyalin iletilebilmesi için gereklidir. Eşzamanlı iletim için aşağıdaki yöntemler kullanılır: Frekans Bölmeli Çoğullama (FDM) Her bir temel bant sinyali modüle etmek için farklı taşıyıcı frekansları kullanılır. Bu yöntemde, taşıyıcı frekansları modüleli sinyallerin spektrumlarının birbiri ile örtüşmesini ve girişmesini engelleyecek kadar uzak seçilir. Alıcıda ise, arzu edilen istasyon ya da sinyali seçmek için ayarlanabilir bant geçiren süzgeçler kullanılır. Bu sayede kanalın bant genişliği herhangi bir örtüşme olmadan çeşitli sinyallerce paylaşılmış olur.

Zaman Bölmeli Çoğullama (TDM) Temel bant sinyaller dar darbelerden oluşan PAM sinyallerine dönüştürülür. Bir sinyalin darbeleri arasındaki boşluk diğer sinyallerin darbeleri için kullanılır. Böylece, çeşitli sinyal darbeleri birbiri arasına sokularak, iletim zamanı belirli bir sayıdaki sinyal tarafından paylaşılmış olur. Alıcıda ise, darbe trenleri yerleştirildikleri sıralamaya uygun bir şekilde birbirinden ayrılır. Modülasyon Gürültü ve Girişimin Etkisini Azaltır Frekans ve faz modülasyonları iletim bandının ve SNR’ ın kontrol edilmesine olanak sağlar.

### Kodlama

Kodlama güvenli sayısal iletim için gerekli olan bir sembol işleme işlemidir. Kodlama(Encoding) sayısal mesajı yeni bir sembol dizisine Kod Çözme(Decoding) kodlanmış diziyi orijinal haline (mesaja) geri dönüştürür. Bu dönüşüm sırasında belki iletim sırasında meydana gelen veri bozulması nedeniyle birkaç hata da Hata Kontrol Kodları kanal gürültüsü ya da bir takım eksiklikler nedeniyle oluşması muhtemel hataların etkisini ortadan kaldırmak için kullanılır. Her bir ikili kod sözcüğüne ekstra “kontrol bitleri” ekleyerek hataların büyük bir çoğunluğunu sezmek hatta düzeltmek mümkündür. Aslında bu yöntemle mesaja bir fazlalık eklenerek sinyal bant genişliği artırılır, ancak bu iletişim emniyetini de artırır. Örnek: 0001 kod sözcüğüne 1’ lerin sayısını çift yapmak için 1 eklenirse, yeni kod sözcüğü 00011 olur. Alıcıdaki kod çözücü birlerin sayısının çift olup olmadığını kontrol eder. Bu sayı çift değilse alıcı iletim esnasında bir hata oluştuğunu anlar ve mesajın yeniden iletilmesini ister. Bu yöntem çift parite kontrolü olarak bilinir.

### Sayısal Haberleşmenin Analog

Haberleşmeye Olan Üstünlükleri Sayısal haberleşme kanal gürültüsü ve distorsiyona karşı daha İletim yolu boyunca kullanılan repetörler sayısal sinyali sezer ve gürültüden arındırılmış olarak sinyali yeniden iletir. Bu sayede, iletim yolu boyunca gürültünün birikmesi önlenir. Bu analog haberleşmede Sayısal devre uygulamaları esnek bir yapıya sahiptir ve mikroişlemcilerin, sayısal anahtarlamanın ve büyük ölçekli entegre devrelerin kullanımına olanak sağlar. Sayısal sinyaller oldukça düşük hata oranıyla, yüksek doğrulukla ve Sayısal sinyallerin çoğullanması oldukça kolay ve daha verimlidir. Sayısal iletişim, bant genişliği ve SNR’ ın kontrol edilmesi bakımından analog haberleşmeye göre oldukça üstündür. Yukarıdaki tüm bu nedenlerden ötürü genellikle sayısal iletişim analog iletişimden daha çok tercih edilir.

## Ders 2: Sinyaller ve sistemlerin temelleri

### İçerik

 Sinyaller ve Sistemlerin Temelleri Trigonometrik ve Üstel Fourier Serileri Fourier Dönüşümü ve Özellikleri Birim Dürtü (Delta Dirac) Fonksiyonu Sinyallerin Doğrusal Sistemlerden İletimi

### Sinyaller

 Sinyal, bilgi ya da veri kümesi olarak tanımlanabilir. Telefon ya da televizyon sinyali. Bir kuruluşun ayın günlerine göre satış tutarları  Ancak, bu derste zamanın fonksiyonu olan sinyaller ile  Bir dalga şeklinin fiziksel olarak gerçeklenebilmesi için Bant genişliği sonlu Aldığı değerler sonlu ve gerçel

### Sinyallerin Sınıflandırılması

 Sürekli zamanlı ve ayrık zamanlı sinyaller  Analog ve sayısal sinyaller  Deterministik ve rasgele sinyaller  Periyodik ve periyodik olmayan sinyaller  Enerji ve güç sinyalleri

### Sürekli ve Ayrık Zamanlı Sinyaller

 Zamanın her anında belirtilen sinyaller sürekli zamanlı sinyaller olarak tanımlanır.  Zamanın belirli anlarında belirtilen sinyaller ayrık zamanlı sinyaller olarak tanımlanır. Sürekli Zamanlı Sinyal Ayrık Zamanlı Sinyal

 Ayrık zamanlı bir sinyal sürekli zamanlı bir sinyalin örneklenmesi ile elde edilebilir.  Bazı durumlarda ise ayrık zamanlı sinyalden tekrar sürekli zamanlı sinyale geri dönmek  Örnekleme Teoremi’ ne uygun yapılan örnekleme sonunda sürekli zamanlı sinyali yeniden elde  Örnekleme teoremi şunu ifade eder: Sinyalin spektrumundaki en yüksek frekans B ise, bu sinyalden saniyede 2B’ den az olmayacak şekilde alınacak örnekler kullanılarak sinyali yeniden oluşturmak mümkündür.

### Analog ve Sayısal Sinyaller

 Genlik değerlerini sürekli bir bölgeden alan sinyallere analog sinyal adı verilir.  Analog ve sayısal sinyal kavramı sürekli zamanlı ve ayrık zamanlı sinyal  Çünkü, bir sinyal sayısal ve sürekli zamanlı olabileceği gibi analog ve ayrık zamanlı da

 Kuvantalayıcı kullanarak analog bir sinyalden sayısal bir sinyal elde etmek mümkündür.  Analog sinyalin genliği L aralığa bölünür.  Her bir örnek değeri orijinal değerin bulunduğu aralığın orta noktasındaki değere yuvarlanır.  Kuvantalama kayıplı bir işlemdir. Dikkat : Öyleyse, sayısal ayrık zamanlı bir sinyal, analog sürekli zamanlı bir sinyalin örneklenip kuvantalanmasıyla elde edilir. (Kodlama da yapıldığı varsayılıyor)

### Deterministik ve Rasgele Sinyaller

 Fiziksel tanımı tamamıyla bilinen bir sinyale deterministik sinyal denir.  Yalnızca istatistiksel özellikleri ile tanımlanan bir sinyale ise rasgele sinyal denir.

### Periyodik ve Periyodik Olmayan

 Bazı sabit pozitif T0 değerleri için eğer sağlanıyorsa f(t) periyodiktir denir.  Eğer bu şartı sağlamıyorsa da o zaman bu sinyal periyodik değildir denir.  Yaygın olarak bilinen bazı periyodik sinyaller

Periyodik Olmayan Sinyal

### Enerji ve Güç Sinyalleri

Gerçel bir f (t ) sinyalinin enerjisi E f olarak tanımlanır. Karmaşık değerli bir sinyal içinse, Eğer, E f < ∞ ise o zaman bu f (t ) sinyali enerji Dikkat! Enerji sinyallerinin ortalama gücü sıfırdır!

Enerjinin sonlu olabilmesi için gerekli koşul zaman sonsuza giderken sinyal genliğinin sıfıra gitmesidir. Sonsuz enerjili sinyaller ile ilgilenildiğinde ise (örneğin periyodik işaretler) sinyalin enerjisi ile değil gücü ile ilgilenmek daha anlamlı Güç sinyalleri fiziksel sonsuza kadar devam eder ya da bir anda sonsuz değer alırlar. şartını sağlıyorsa bu sinyal güç sinyalidir denir.  Bir sinyal aynı anda hem enerji hem güç sinyali olamaz.

Enerji sinyaline örnek Yukarıda grafiği verilen sinyalin enerjisi

Güç sinyaline örnek g (t ) = A cos (ω0t + θ ) ‘ nin gücünü hesaplayalım.

Bir sinyal güç veya enerji sinyali olarak sınıflandırılır. Güç sinyalleri periyodik olabilir veya olmayabilir.  Enerji sinyalleri daima periyodik değildirler.

### Trigonometrik ve Üstel Fourier

Fiziksel olarak gerçeklenebilir T0 ile periyodik bir f(t) sinyali Fourier serisine açılabilir: Trigonometrik Fourier Serisi Üstel Fourier Serisi

Burada, ω0 = 2π f 0 = 2π T0 temel frekansı, nω0 ise n’ inci harmonik frekansını göstermektedir. a0 , an , bn , C0 , Cn , θnve Gn aşağıdaki gibi tanımlanan sabitlerdir:

Fourier Serilerinde Simetri f(t) tek simetri özelliğine sahiptir eğer ise, o zaman tüm n = 0,1, 2, … değerleri için an = 0 olur. Yani, seride yalnızca sinüslü terimler vardır. f(t) çift simetri özelliğine sahiptir eğer ise, o zaman tüm n = 0,1, 2, … değerleri için bn = 0 olur. Yani, seride yalnızca kosinüslü terimler vardır.

### Örnek

Yukarıda verilen sinyali Fourier serisine açınız.

### Örnek (devam)

Bu verileri kullanarak şunları çizebiliriz:  genlik Cn ’ nin ω ile değişimi → Genlik Spektrumu  faz θn’ in ω ile değişimi → Faz Spektrumu Bu iki çizim birlikte f(t)’ nin frekans spektrumu

### Örnek

Faz tek, genlik ise çift simetrik

### Fourier Dönüşümü

Periyodik sinyaller Fourier serisine açılarak temsil edilmişlerdi. Benzer şekilde, periyodik olmayan sinyalleri de Fourier dönüşümü kullanılarak kendi frekans bileşenleriyle ifade etmek mümkündür.  Periyodik olmayan bir f(t) sinyalinin Fourier dönüşümü

Ters Fourier dönüşümü ise

### Örnek

Aşağıda verilen sinyalin Fourier dönüşümünü bulunuz.

f (t ) = A cos (ω0t ) sinyalin Fourier dönüşümünü bulunuz. Frekans spektrumunu çiziniz.

### Örnek(Devam)

Çift taraflı genlik spektrumu Tek taraflı genlik spektrumu Dikkat !!! f(t) çift simetrik fonksiyon olduğu için Faz Spektrumu sıfırdır.

### Fourier Dönüşüm Özellikleri

 Doğrusallık (Süperpozisyon) Özelliği

 Simetri ya da Dualite Özelliği

 Zamanda Öteleme Özelliği  Frekansta Öteleme Özelliği

 Frekansta Öteleme Özelliği

 g(t) ve G(f)’ in Altında Kalan Alan

 Kompleks Eşlenik Özelliği

### Birim Dürtü Fonksiyonu

 Birim Dürtü Fonksiyonunun Fourier Dönüşümü

### δ ( t ) Uygulamaları

 Birim Basamak Sinyali

### Sinyallerin Zamanla Değişmeyen

Doğrusal Sistemlerden İletimi Eğer bir sistem hem doğrusalsa hem de zamanla değişmiyorsa o zaman bu sistemin giriş çıkış ilişkisi şu

Doğrusal Sistemlerden İletimi Bu ifadeye konvolüsyon integrali adı verilir ve çıkış ifadesi konvolüsyonun sembolik gösterimi kullanılarak da Konvolüsyon integrali doğrusal bir sistemin giriş zaman fonksiyonu ve çıkış zaman fonksiyonu arasındaki ilişkiyi sistemin birim dürtü cevabı h (t ) cinsinden tanımlar.

Doğrusal Sistemlerden İletimi Aşağıda şekilleri verilen fonksiyonların konvolüsyon

### Örnek(Devam)

t < −3 ⇒ üst üste çakışma yok, f (t ) = 0 t > 3 ⇒ üst üste çakışma yok, f (t ) = 0

## Ders 3: Enerji ve güç spektral yoğunluğu, doğrusal sistemler

### İçerik

 Sinyaller ve Sistemlerin Temelleri Enerji ve Güç Spektral Yoğunluğu Öz ve Çapraz İlinti Fonksiyonları Hilbert Transformu ve Özellikleri Ön Zarf ve Kompleks Zarf Kavramları Bant Geçiren Sinyal ve Sistemler Faz ve Grup Gecikmesi

### Enerji ve Güç Spektrumları

Hem deterministik hem de periyodik olmayan sinyaller  Periyodik sinyaller ve rasgele sinyaller güç sinyalleridir. Enerji Spektral Yoğunluğu Bu ilişki Parseval teoremi olarak bilinir ve şunu ifade eder: Bir f(t) sinyalinin toplam enerjisi f(t)’ nin tüm frekans bileşenlerinin toplam enerjisine eşittir.

F (ω ) , f (t ) ' nin genlik spektrumu Ψ f (ω ) = F (ω ) enerji spektral yoğunluğu olarak tanımlanır. Enerji Spektral Yoğunluğunun birimi [Joule / Hz]’ dir.

Güç Spektral Yoğunluğu f(t) bir güç sinyali ise (-∞,∞) aralığında sonsuz bir enerjiye sahiptir. Fourier dönüşümünü bulmak için f(t)’ nin kesilmiş hali olan fT(t) sinyali kullanılmalı.

Bu durumda f(t)’ nin güç spektral yoğunluğu Güç Spektral Yoğunluğunun birimi [Watt / Hz]’ dir.

### Özilinti Fonksiyonu

 Özilinti fonksiyonu, bir sinyalin belli bir miktar geciktirilmiş hali ile kendisi arasındaki benzerlik veya uyumun bir ölçüsüdür. Enerji Sinyalleri İçin:

Güç Sinyalleri (Periyodik) için:

### Karşılıklı İlinti Fonksiyonu

 Bir sinyal ile, başka bir sinyalin belli bir miktar geciktirilmiş hali arasındaki benzerlik veya uyumun bir ölçüsüdür.

Güç Sinyalleri (Periyodik) için: Sinyallerin periyodu aynı ve T0 ise,

### Doğrusal Sistemlerden İletim

Birim Dürtü Cevabı Giriş ve Çıkış Arasındaki Enerji Spektral Yoğunluğu İlişkisi

Alçak geçiren sistem Genlik cevabının sıfır frekanstaki değerinin 1 2 ‘ sine düştüğü frekans aralığına 3dB bant genişliği denir.

### Bozulmasız İletim

Daha genel bir ifadeyle, İletimde iki tür bozulma olabilir: 1. Genlik bozulması

### Hilbert Dönüşümü

Ters Hilbert Dönüşümü

### Örnek

Aynı şekilde, g ( t ) = sin ( 2π f c t ) için

### Hilbert Dönüşümünün Özellikleri

gˆ (t ) ‘ nin spektral yoğunlukları aynıdır.  g (t ) ve gˆ (t ) ‘ nin özilinti fonksiyonları aynıdır.  gˆ (t ) ‘ nin Hilbert Dönüşümü −g (t ) ‘ dir. Hilbert Dönüşümü’ nün Fiziksel Anlamı Bu filtre güçlendirme ya da zayıflatma yapmaz, frekans bileşenlerinin genlikleri değişmez. Ancak, bu filtre her frekans bileşeninin fazını 900 kaydırır. Her frekans bileşenine 900 ’lik faz kayması vermek sinyale sabit bir gecikme vermek anlamına gelmez. Çünkü, 900 ’lik faz farkı her frekans bileşeni için farklı sürelerde gecikmelere karşı gelir.

### Kompleks Zarf

Dar bantlı bir g(t) sinyalinin ön zarfının temel bant şekli Kompleks Zarf olarak adlandırılır ve g t ile gösterilir. g s ( t ) : Dik Fazlı Bileşen g ( t ) = g c ( t ) cos ( 2π f c t ) − g s ( t ) sin ( 2π f c t ) Kanonik Yapı

### Zarflara Genel Bakış

- Alçak veya bant geçiren olabilir. - Genellikle kompleks değerlidir. - Alçak geçiren bir sinyaldir. - Ön zarfın ötelenmiş halidir. - Kompleks veya ön zarfın genliğidir. - Her zaman gerçel değerli ve alçak geçirendir.

### Bantgeçiren Sistemler

Bantgeçiren sistemler de, bantgeçiren sinyaller gibi kanonik formda veya kompleks zarf cinsinden temsil edilirler. Birim dürtü cevabı h(t) olan bantgeçiren bir sistem için: Bantgeçiren bir sistemin bantgeçiren bir sinyale cevabı:

Kompleks zarflar yardımıyla daha basit olarak çıkış ifadesine ulaşmak mümkündür.

### Grup ve Faz Gecikmesi

 Fazı β ( f ) olan aşağıdaki doğrusal olmayan sistemi ele alalım.

*Not: Metin, slaytlardan otomatik çıkarılıp düzenlendi; denklemler ve şekiller metne dökülemediğinden ilgili kısımlar atlanmıştır. Tam hâli için yazının sonundaki PDF dosyalarına bakınız.*
