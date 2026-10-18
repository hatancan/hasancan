---
baslik: EEM474 Güç Elektroniği: Tek ve üç fazlı eviriciler, SPWM
ozet: Kare dalga ve kısmi kare dalga eviriciler, RL yük, harmonikler, sinüzoidal PWM ve üç fazlı anahtarlama.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## DC'den AC'ye dönüşüm

Yarım köprü ve tam köprü eviriciler, DC kaynaktan işareti değişen çıkış gerilimi üretir. Tam köprüde çapraz anahtar çiftleri sırayla iletime alınır. Aynı kolun üst ve alt anahtarları aynı anda iletime alınırsa DC kaynak kısa devre olur. Endüktif yükte akımın devamı ters paralel diyotlarla sağlanır.

## Kare dalga ve RL yük

±Vdc tam köprü kare dalgası tek harmoniklerden oluşur. n tek olmak üzere n. gerilim harmoniğinin tepe değeri 4Vdc/(nπ)'dir. RL yükte her harmonik için Zₙ = √[R² + (nωL)²], Iₙ = Vₙ/Zₙ ve φₙ = atan(nωL/R) kullanılır. Endüktans yüksek frekanslı akım bileşenlerini daha fazla sınırlar.

THD, temel dışındaki harmoniklerin toplam etkin değerinin temel bileşenin etkin değerine oranıdır. Gerilim THD'si ile akım THD'si aynı olmak zorunda değildir.

## Kısmi kare dalga

Çıkışın bir bölümünde sıfır gerilim uygulanarak darbe genişliği değiştirilir. Sunum, gecikme açısının harmonikler üzerindeki etkisini ve belirli harmonikleri yok etme seçimini inceler. Gerilimin temel bileşeni ile yük akımının bozulması birlikte değerlendirilir.

R = 10 Ω, L = 25 mH ve f = 60 Hz örneğinde 100 V DC beslemeli kare dalga için temel akımın tepe değeri yaklaşık 9,27 A, akım THD'si %16,7 gösterilir. α = 30° ve Vdc = 116 V olan kısmi kare dalga örneğinde THD yaklaşık %6,6'ya iner.

## Sinüzoidal PWM

Sinüzoidal referans, yüksek frekanslı üçgen taşıyıcıyla karşılaştırılır. Genlik modülasyon oranı ma = Vreferans,tepe / Vtaşıyıcı,tepe; frekans oranı mf = ftaşıyıcı / ftemel olarak tanımlanır. Lineer bölgede tam köprü temel çıkışının tepe değeri ma Vdc ile orantılıdır.

Bipolar PWM'de çıkış iki polarite arasında değişir. Unipolar yöntemde köprünün kolları karşıt referanslarla sürülür; çıkışta sıfır seviyesi de oluşur. Harmoniklerin taşıyıcı çevresine taşınması filtrelemeyi kolaylaştırır. Aşırı modülasyonda lineer genlik ilişkisi geçerliliğini kaybeder.

Sunumdaki Vdc = 100 V, ma = 0,8, mf = 21, f = 60 Hz, R = 10 Ω ve L = 20 mH örneğinde temel gerilim tepesi 80 V, temel akım tepesi yaklaşık 6,39 A, toplam güç yaklaşık 205,5 W ve akım THD'si %8,7 verilir. Son tasarım sorusunda 150 V DC kaynaktan 75 Vrms, 60 Hz çıkış; R = 12 Ω, L = 60 mH ve %10'dan küçük akım THD'si hedeflenir.

## Üç fazlı evirici

Üç kollu köprüde fazlar 120° kaydırılır. 180° iletim düzeninin altı anahtarlama durumu sunumda 123, 234, 345, 456, 561 ve 612 sırasıyla gösterilir. Durumlar 60° aralıklarla değişir. Yıldız ve üçgen yük bağlantılarında faz ve hat gerilimleri ayrı değerlendirilir.

Altı basamaklı çıkışta hat geriliminin etkin değeri √(2/3)Vdc'dir. Üç fazlı SPWM'de 120° kaydırılmış üç sinüs aynı taşıyıcıyla karşılaştırılır; hat gerilimi iki kolun çıkış farkıdır.

*Not: Sayısal THD sonuçları sunumdaki harmonik hesabına ve yuvarlamalara aittir; her anahtarlama yöntemi için değişmez bir oran değildir.*
