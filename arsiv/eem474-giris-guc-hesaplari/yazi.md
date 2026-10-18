---
baslik: EEM474 Güç Elektroniği: Güç dönüşümü, RMS ve güç faktörü
ozet: Güç elektroniğinin dönüşüm türleri; ortalama ve etkin değer, harmonikler, güç faktörü ve enerji depolama bağıntıları.
---

EEM474 ders klasöründeki İngilizce sunumların anlatımı ve formülleri metne aktarıldı. Hazırlayanın adı belgelerde açıkça belirtilmiyor. Fotoğraflar ve kitaplardan alınmış görseller aktarılmadığından bu yazıda indirme dosyası bulunmuyor.

## Güç elektroniğinin konusu

Elektrik enerjisi, yarı iletken anahtarlar kullanılarak yükün gerektirdiği biçime dönüştürülür. Sunumlarda endüstriyel sürücüler, güç kaynakları, ev aletleri, ulaşım ve enerji sistemleri uygulamaları sıralanır. Kontrol devresi, güç devresindeki anahtarların iletim zamanlarını belirler.

| Dönüşüm | Devre |
| --- | --- |
| AC → DC | Doğrultucu |
| DC → DC | Kıyıcı / DC dönüştürücü |
| DC → AC | Evirici |
| AC → AC | AC gerilim veya frekans dönüştürücü |

İdeal anahtar kesimdeyken akımı, iletimdeyken gerilimi sıfır kabul edilir. Gerçek anahtarda iletim gerilimi ve geçiş süreleri kayıp oluşturur. Verim η = Pçıkış / Pgiriş biçimindedir.

## Ortalama, etkin değer ve güç

Periyodu T olan gerilimin ortalama değeri Vort = (1/T) ∫₀ᵀ v(t) dt; etkin değeri Vrms = √[(1/T) ∫₀ᵀ v²(t) dt] olarak tanımlanır. Akım için aynı işlemler uygulanır. Etkin değer, bir dirençte aynı ısıyı üreten DC değerdir.

Anlık güç p(t) = v(t)i(t), ortalama aktif güç P = (1/T) ∫₀ᵀ v(t)i(t) dt olur. Direnç yükünde P = Irms²R = Vrms²/R kullanılır. Ortalama akımın karesini kullanmak, dalgalı akımda aynı sonucu vermez.

Sinüzoidal gerilim ve akımda P = Vrms Irms cosφ; görünür güç S = Vrms Irms; güç faktörü PF = P/S'dir. Reaktif güç Q = Vrms Irms sinφ olarak yazılır.

## Harmonikli dalga biçimleri

Fourier açılımı DC bileşen ile temel frekansın tam katlarındaki bileşenlerden oluşur. Birbirine dik harmoniklerin etkin değerleri için Irms² = I₀² + Σ Iₙ,rms² bağıntısı kullanılır. Gerilim sinüzoidal, akım bozulmuşsa yalnız temel akım bileşeni ortalama aktif güce katkı verir:

P = Vrms I₁,rms cosφ₁

PF = (I₁,rms / Irms) cosφ₁

THDᵢ = √[Σₙ≥₂ Iₙ,rms²] / I₁,rms

Böylece faz kaymasının düzeltilmesi, harmoniklerden kaynaklanan güç faktörü kaybını tek başına ortadan kaldırmaz. Sunumdaki hesaplarda önce dalga biçiminin iletim aralıkları, ardından ortalama ve RMS integralleri kurulmaktadır.

## Endüktör ve kondansatör

Endüktörde vL = L di/dt, depolanan enerji WL = ½Li²; kondansatörde iC = C dv/dt, enerji WC = ½Cv²'dir. Periyodik kararlı durumda bir periyot sonunda depolanan enerji başlangıç değerine döner. Bu nedenle ideal endüktörün ortalama gerilimi ve ideal kondansatörün ortalama akımı sıfırdır.

*Not: Sunumların farklı düzenlenmiş kopyaları tek yazıda birleştirildi. İdeal anahtar ve kayıpsız eleman varsayımları gerçek bir devrenin yüzde yüz verimli olduğu anlamına gelmez.*
