---
baslik: EEM214 Elektronik I: 2014 Laboratuvar Ölçüm ve Dalga Şekli Notları
ozet: Osiloskop kullanımı, 1N4148 diyot ölçümleri, doğrultma, kırpma ve kenetleme deneylerinin fotoğraflardan aktarılan ölçüm notları.
---

25 Şubat, 4 Mart ve 18 Mart 2014 tarihli laboratuvar sayfaları fotoğraflanmış sayfalardan metne aktarıldı. Kişisel bilgiler çıkarıldı. Fotoğraflar paylaşılmıyor ve indirme dosyası bulunmuyor. Bulanık veya kadraj dışında kalan sayılar tahmin edilmedi; aşağıdaki ölçümler yalnız okunabilen kayıtlardır.

## Deney 1: osiloskop ve işaret üreteci

25 Şubat sayfalarında DC kuplajla sinüsün gözlenmesi, prob çarpanının kontrol edilmesi ve gerilim/zaman ölçekleriyle dalga şekli çizilmesi istenir. Sinüs çizimlerinin yanında V_pp = 2 V notu okunur. V_min = −1 V satırı seçilebilmektedir; diğer gerilim ve frekans değerlerinin tamamı güvenilir biçimde okunamıyor.

Başka bir çizimde kare dalga ile aynı periyottaki sinüs üst üste gösterilir. Bir sonraki eksende yatay bir iz çizilmiştir; ölçek notu belirsizdir. Bu grafiklerden kesin frekans veya faz farkı çıkarılmamıştır.

Potansiyometre tablosunda R_1, R_2 ve yüksüz V_out sütunları görülür. Okunabilen kayıtlar:

| Konum | R_1 | R_2 | V_out |
| --- | --- | --- | --- |
| İlk konum | 1,2 Ω olarak görünüyor | Yaklaşık 4,68 kΩ | 0 V |
| Orta konum | Belirsiz | 2,5 kΩ | 3,5 V |
| Son konum | Yaklaşık 4,69 kΩ | 147 Ω olarak görünüyor | Belirsiz |

Föyde yük bağlanarak ölçümün tekrarlanması ve 150 Ω yük ifadesi de vardır; yük altındaki sonuç sütunu kadraj dışındadır.

*Not: Bu bölümdeki sayılar bulanık fotoğraftan okunabildiği ölçüde aktarılmıştır; kesin bir kalibrasyon kaydı olarak kullanılmamalıdır.*

## Deney 2: 1N4148 diyot testi

4 Mart sayfasında multimetre diyot testi için ileri yönde 0,5638 V, ters yönde 0,000 kaydedilmiştir. Föy ileri yöndeki tipik silikon diyot okumasını 0,500–0,900 V aralığında verir.

*Not: Ters yöndeki 0,000, kaynak cihazın gösterim kaydıdır. Multimetreye bağlı olarak açık devre göstergesi OL veya başka bir biçimde olabilir; sıfır gerilim değeri tek başına bütün cihazlar için “sağlam diyot” ölçütü değildir.*

220 Ω seri dirençle ileri i–v karakteristiği için doldurulmuş satırlar:

| Föydeki hedef diyot gerilimi | Ölçülen diyot gerilimi | Yazılan akım |
| --- | --- | --- |
| 0,40 V | Yaklaşık 0,4542 V | 20,61 µA |
| 0,50 V | 0,5212 V | 74,26 µA |
| 0,60 V | Yaklaşık 0,60 V; son basamaklar belirsiz | 138,29 µA |
| 0,70 V | 0,6075 V | 144,84 µA |
| 0,80 V | 0,6257 V olarak okunuyor | 276,33 µA |

0,35; 0,45; 0,55; 0,65; 0,75; 0,85 ve 0,90 V satırları boş veya üzeri çizilidir.

*Not: Hedef gerilim ile ölçülen gerilim farklı sütunlardır. Fotoğraftaki kayıtlar hedeflere tam oturmuyor; ölçüm yerine hedef sayıları geçirilmedi.*

## Ters kutuplama tablosu

Föy, küçük akımlarda doğrudan akım ölçümü yerine 1 MΩ direnç üzerindeki gerilimin ölçülmesini ister. Kaynak sütunlarının okunabilen dökümü:

| Kaynak gerilimi | Dirençte ölçülen gerilim | Kaynakta yazılan diyot gerilimi | Kaynakta yazılan akım |
| --- | --- | --- | --- |
| 0 V | 0 V | 0,3 V | 0 |
| −1 V | 0,0030 V | 1,43 V | 0 |
| −2 V | 0,0040 V | 2,12 V | 0 |
| −3 V | 0,0042 V | 2,88 V olarak okunuyor | 0 |
| −4 V | 0,0040 V | 3,66 V | 0 |
| −5 V | 0,0040 V | 4,62 V | 0 |
| −10 V | 0,0063 V | 9,28 V | 0 |
| −15 V | 0,0064 V | 13,69 V | 0 |
| −20 V | 0,0052 V | 18,13 V | 0 |
| −25 V | 0,0053 V | Yaklaşık 22,98 V; son basamak belirsiz | 0 |

*Not: 1 MΩ üzerinde 3,0–6,4 mV, yaklaşık 3,0–6,4 nA'ya karşılık gelir; kaynak akım sütununu sıfıra yuvarlamıştır. Diyot gerilimi sütunu nominal kaynak ve direnç geriliminin farkıyla tam uyuşmuyor. Bu değerler düzeltilmiş hesap sonucu değil, fotoğraftaki deney kaydıdır.*

## Yarım dalga doğrultma gözlemi

Aynı günün iki fotoğrafı aynı çizimin farklı kadrajlarıdır. Föy, 100 Hz sinüs, 5 V tepeden tepeye giriş ve R_L = 1 kΩ ile giriş/çıkışın çizilmesini ister. Giriş pozitif ve negatif yarım periyotlardan oluşur; ikinci eğri yalnız bir yarım periyotta iletim gösterir. Diğer yarım periyotta çıkış sıfıra yakın çizilmiştir.

*Not: El yazısı okların hangi eğriye ait olduğu yer yer belirsizdir; fotoğraftan kesin tepe değeri veya diyot düşümü hesaplanmadı.*

## Deney 4: kırpıcı devreler

18 Mart sayfalarında ilk deneyin giriş koşulları 100 Hz ve 20 V tepeden tepeye sinüstür. Devre için R = 1 kΩ ve R_L = 47 kΩ verilmiştir. Osiloskopta DC kuplaj kullanılır; kanalların yanında 5 V ölçek notları vardır.

İlk çıkış çiziminde sinüsün üst kısmı düzleşerek kırpılır. Diyot ters çevrilip pozitif DC kaynak negatif kaynakla değiştirildiğinde, ikinci çizimde alt kısım düzleşir. Bu iki çizim kırpma yönünün değiştiğini gösterir.

Ön çalışmada tasarlanan devrenin denenmesi istenen sonraki bölümde giriş 100 Hz ve 10 V tepeden tepeyedir. Çizilen devrede girişte seri 1 kΩ, çıkışta 47 kΩ yük ve zıt yönlü diyot kollarıyla ilişkili 3 V ve 2 V DC kaynaklar bulunur. Bu bölümde giriş/çıkış grafik kutuları boş bırakılmıştır; ölçülmüş bir dalga şekli yoktur.

## Kenetleyici devreler

Föyün sonraki bölümünde 100 Hz, 20 V tepeden tepeye girişle C = 1 µF kullanılır; çıkış sinüsü aşağı doğru kaymış çizilmiştir. İkinci devrede C = 47 µF'tir. Çizimde üst seviyenin yanında 5,3 V, alt seviyenin yanında 14,7 V büyüklüğü yazılıdır. Sıfır çizgisine göre bunlar yaklaşık +5,3 V ve −14,7 V konumundadır.

Diyotun ve DC kaynağın yönü ters çevrilince sonraki çizimin üstünde 14,7 V, altında 5,3 V büyüklükleri bulunur; eksene göre yaklaşık +14,7 V ve −5,3 V olarak gösterilmiştir.

*Not: Kaynak alt seviye yazılarında eksi işaretini açıkça göstermiyor. İşaretler burada grafikteki sıfır çizgisine göre açıklanmıştır; iki durumda da toplam aralık 20 V'tur.*

Son sayfa kondansatör takılı ve takılı olmayan durumların giriş, çıkış ve X–Y aktarım eğrilerini karşılaştırır. DC kaynakların ayrı ayrı değiştirilmesi istenir. Öğrencinin kısa yorumu: “a ile b arasında kapasitör farkı var. b'de iki volt arasındaki fark kadar kenetleyecek.” Çıkış çizimi kaymış ve bir yönde sınırlanmış olarak gösterilir; kesin ölçek okunamadığından sayısal kenetleme seviyesi verilmemiştir.
