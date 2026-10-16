---
baslik: EEM214 Elektronik I: Laboratuvar Cihazları Tanıtımı (Osiloskop, Devre Tahtası, Sinyal Üreteci) ve Deney 1 Raporları
ozet: EEM214 Elektronik I laboratuvarının ön çalışma metni olarak verilen cihaz tanıtımı: osiloskopta prob, kanal, AC/DC kuplaj, tetikleme ve ölçüm menüsü, breadboard kullanımı ve kablo hazırlama, sinyal üreteci ve ayarlı güç kaynağı; ayrıca osiloskop, DMM ve potansiyometre deneyinin iki öğrenci raporu.
---

Bu yazı, Başkent Üniversitesi Elektrik-Elektronik Mühendisliği **EEM 214 – Elektronik I** laboratuvarında ilk deneyden önce ön çalışma olarak okunması istenen **Laboratuvar Cihazları Tanıtımı** belgesini (9 sayfa, 2003–2005) ve ilk deneyin ("Oscilloscopes, DMM, Function Generator, Potentiometer") iki öğrenci raporunu bir araya getiriyor. Raporlar arkadaşların çalışması; ad ve öğrenci numaraları kapatıldı. Deneyin 2012 tarihli föyü arşivde "Laboratuvar Deney 1" yazısında bulunuyor. Belge ve raporlar yazının sonunda ZIP olarak indirilebilir.

## Laboratuvar Cihazları Tanıtımı

### Osiloskop

Osiloskop laboratuvarın temel cihazlarından biridir. Prob olarak bilinen uçlarına uygulanan elektriksel sinyalleri ekranında görüntüler; böylece devrenin istenildiği gibi çalışıp çalışmadığı ya da belli noktalardaki sinyaller gözlemlenebilir. Bir sinyalin ekranda anlamlı olarak gözlemlenebilmesi için periyodik olması gerekir; aksi hâlde üst üste binen ya da ekranda dalgalanan görüntüler elde edilir.

Günümüzde birçok osiloskop sayısaldır. Sayısal osiloskoplar problardan aldıkları sinyali örnekleyerek hafızada saklar; bu sayede periyodik olmayan sinyaller de ayarlanan zaman penceresinde gözlemlenebilir ve sinyal üzerinde işlem yapılabilir. En büyük dezavantajları örnekleme frekansının sınırlı olmasıdır; bu, gözlemlenebilecek sinyalin frekans aralığını daraltır. Analog osiloskoplarda da benzer bir sınır vardır, ancak bunu kullanılan malzemelerin çalışma bantları ve gecikme süreleri belirler.

**Prob ayarı:** Problar üzerinde 1X, 10X, 100X gibi çarpanlar bulunur. Prob 10X'e ayarlanırsa giriş sinyalinin genliği onda birine düşer; sinyali bire bir görmek için prob 1X'te olmalıdır. Ayrıca osiloskop menüsündeki (örnek cihazda Storage menüsü) prob çarpanı da 1X'e ayarlanmalıdır. Ekran kenarındaki **Probe Adjust** ucu 0 ile 0.5 V arasında değişen, 0.5 V tepeden tepeye bir kare dalga verir; probun ve kanalın doğru ayarlandığını kontrol etmek için yalnız prob ucunu bu uca takmak yeterlidir.

Probu bir noktaya bağlamadan önce dikkat edilecekler:

- Gözlemlenecek noktadaki gerilim osiloskoba zarar vermeyecek değerde olmalı.
- Probun toprak ucu doğru noktaya bağlanmalı.
- Gözlenecek nokta ile osiloskop kanalının empedansları uyumlu olmalı.
- İki kanal birlikte kullanılacaksa ikisi de aynı toprağa bağlı olmalı.
- Probların her iki ucu da tam oturmalı.

**Kanal ayarı:** Önce kanal girişi topraklanarak eksen (sıfır) ayarı yapılır ve pozisyon düğmesiyle sinyal dikey eksende konumlandırılır; ardından ölçülecek sinyalin niteliğine göre AC ya da DC kipine geçilir. Örneğin yavaş değişen bir bileşenin üzerine binmiş yüksek frekanslı bir sinyal DC kipte doğru okunamaz; AC kipte osiloskop DC (ve DC'ye yakın, yavaş) bileşeni süzer ve yalnız AC kısmı gösterir. Birçok osiloskop kanalları aynı anda gösterebilir, toplayabilir veya çıkarabilir; bu, bir eleman üzerindeki gerilimi ölçmeyi kolaylaştırır.

**Tetikleme ayarı:** Ekrandaki sinyal ile osiloskop senkron olmalıdır. Otomatik tetikleme çoğu durumda durağan bir görüntü sağlar; sinyalde kilitlenilebilecek birden fazla bileşen varsa time/div ve tetikleme menüsü ayarlarıyla senkronizasyon sağlanır. Tetikleme menüsünde **Source** (hangi kanal ya da dış kaynak), **Mode** (otomatik, normal, TV yatay/dikey) ve **Level/Hold-off** ayarları bulunur.

**Ölçüm menüsü:** Ekrandaki kareleri sayarak ölçüm yapmak mümkün olsa da zahmetlidir; osiloskoplardaki ölçüm menüsüyle frekans, genlik, periyot gibi değerler doğrudan okunabilir.

### Devre tahtası (breadboard)

Breadboard, devre elemanlarını lehimsiz bağlamak ve deneysel amaçlı küçük devreler kurmak için kullanılır; özellikle DIP tipi entegrelerle çalışmak için idealdir. Delikler standart entegre bacak aralığında dizilmiştir; belirli gruplar kendi içinde birbirine temas eder, alt ve üstteki yatay sıralar genellikle besleme dağıtım yollarıdır.

Her deliğin içindeki metal yay kabloya yan yüzeyinden temas eder; bu yüzden kablo uçlarını gereğinden uzun soymanın ya da masaya fazla sokmanın anlamı yoktur, hatta sakıncalıdır:

- Pin yapısı bozulur, bir sonraki kullanımda temassızlığa yol açar.
- Uzun tel metal kılıf içinde yatay ilerleyerek komşu pinlere temas edebilir.
- Masanın tabanındaki metal plakaya değerek başka bir uzun telle kısa devre ya da yüksek empedanslı bir yol oluşturabilir.

Kablo uçları yan keski veya kablo açacağıyla açılmalı; hiçbir şekilde ateşle yakılarak açılmamalıdır, bu kablonun kimyasal yapısına zarar verir.

### Sinyal üreteci

Periyodik sinyal üreten cihazlardır. Ortak özellikleri: farklı dalga biçimleri (sinüs, kare, üçgen) ve tersleyici, frekans aralıkları (1 Hz – 1 MHz), frekans çarpanı (0.1–2.0), görev çarpanı (duty), DC kaydırma (offset), genlik ayarı ve düşük empedanslı çıkış; ayrıca kazancı yüksek devrelere uygulamak için dB zayıflatma seçenekleri. Önce dalga biçimi ve frekans seçilir, üreteç devreye bağlanır, genlik **devreye bağlıyken** ayarlanır (üreteç ve devre empedansları yüzünden ayarlanan genlik değişebilir); genellikle genlik sıfıra yakınken bağlanıp yavaşça artırılır.

### Ayarlanabilir güç kaynağı

Simetrik ya da bağımsız modda çalışabilen iki kaynaktan oluşur; seri bağlamak için ana ve bağımsız kaynağın − ve + uçları metal bir parçayla birleştirilir. Ekranlarında gerilim ve çekilen akımı gösterirler; en yüksek akım sınırlanarak kısa devre ya da aşırı akım durumunda devrenin yanması önlenir, kısa devrede kaynak beslemeyi otomatik keser.

## Öğrenci raporları (Deney 1)

### 2006 raporu

- 1 V tepe sinüste osiloskobun ölçüm menüsünden: V_max = 0.98 V, V_min = −0.98 V, V_avg = 0 V, V_rms = 705.7 mV, V_pp = 1.96 V, periyot 10.08 ms, frekans 99.20 Hz.
- Volts/div sinyalin genliğini değil her karenin değerini, time/div frekansı değil zaman ölçeğini değiştirir; pozisyon düğmesi DC gerilim eklemez, yalnız sinyali kaydırır.
- 2 V/div'de ekranda 8 kare olduğu için en fazla 16 V tepeden tepeye okunabilir; tam genlikteki sinyal sığmıyor.
- Üretecin DC offset'i eklendiğinde AC kuplajda fark görülmez, DC kuplajda sinyal ofsetle birlikte görülür.
- Potansiyometreli gerilim bölücü (V_out = V_in·R2/(R1 + R2)):

| Konum | R1 | R2 | V_out (R_L = ∞) | V_out (R_L = 150 Ω) |
|---|---|---|---|---|
| Tam saat yönü | 4.970 kΩ | 1 Ω | 0.6 mV | 0.6 mV |
| Orta | 2.580 kΩ | 2.512 kΩ | 5 V | 0.6 V |
| Tam saat yönü tersi | 1 Ω | 4.888 kΩ | 10 V | 7.2 V |

Tam saat yönünde teorik olarak R2 = 0 ve V_out = 0 olmalı; ölçülen küçük 1 Ω yüzünden 0.6 mV okunuyor. Diğer konumlar beklenen değerlere yakın.

### 2008 raporu

Ölçüm menüsünden V_max = 1.96 V, V_min = −1.08 V, V_pp = 2.04 V, V_avg = −35.2 mV, periyot 10.55 ms, frekans 94.52 Hz. Volts/div'in her karenin gerilim değerini, sec/div'in zaman ölçeğini belirlediği; sinyal ekrana sığmadığında okunamadığı; tetiklemenin görüntüyü sabitlediği ve DC offset'in sinyali kaydırdığı kısaca açıklanmış. Potansiyometre tablosu boş bırakılmış.

## İndirme

ZIP dosyasında Laboratuvar Cihazları Tanıtımı belgesinin Word dosyası ve iki raporun kişisel bilgileri kapatılmış PDF kopyaları bulunuyor.
