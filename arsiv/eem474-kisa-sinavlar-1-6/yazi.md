---
baslik: EEM474 Güç Elektroniği: Kısa sınavlar 1–6 ve cevap notları
ozet: Güç faktörü, anahtarlar, buck/boost, PWM evirici ve DC motorlar üzerine altı kısa sınavın A/B formları.
---

EEM474 Güç Elektroniği dersinin altı kısa sınavı ve üzerlerindeki cevap notları bir araya getirildi. Birçok soruda cevap, ders sunumunun sayfa numarasına yönlendiriyor; bu kısımlar tamamlanmış çözüm olarak sunulmadı. PDF'ler, kişisel bilgi taşıyabilecek üst verileri temizlenmiş olarak yazının sonundaki ZIP'tedir.

## Kısa sınav 1: Temel kavramlar

Sorular dönüştürücü türlerini (AC/DC, DC/DC, DC/AC, AC/AC), AC voltmetrenin RMS değerini, harmonikleri ve güç kalitesini kapsar. Sinüzoidal v(t) = Vm cos(ωt + θ), i(t) = Im cos(ωt + φ) için PF = cos(θ − φ) yazılır. Temeli 100 Hz olan işaretin harmonikleri bu frekansın tam katlarıdır.

DF = I₁,rms / Irms ve THD = √(Irms² − I₁,rms²)/I₁,rms bağıntıları verilerek iyi güç kalitesinde DF'nin 1'e, THD'nin 0'a yaklaşması beklenir. Aynı fazlı sinüs akımı, faz kaymalı sinüs akımı ve darbe biçimli doğrultucu akımı karşılaştırılır.

Periyodik kararlı durumda kondansatörün ortalama akımı sıfırdır. Sigortanın aşırı akım koruması ile aşırı gerilim koruması aynı işlev değildir. Serbest dolaşım diyodunun akımı, yükün direnç veya endüktif olmasına göre incelenir.

*Not: Cevap notunda ideal anahtarın geçiş için “çok az enerji” kullandığı ifadesi doğru işaretlenmiş. Tam ideal modelde anahtarlama kaybı sıfırdır; küçük fakat sıfır olmayan kayıp gerçek anahtara aittir.*

## Kısa sınav 2: Anahtarlar ve kayıplar

Triyak ile GTO'nun farkları, ideal anahtar özellikleri ve anahtar seçiminin gerilim–akım–frekans ölçütleri sorulur. İletim kaybı ile açılma/kapanma kaybı ayrılır. BJT sürme darbesinden baz akımı, kolektör akımı ve VCE dalga biçimleri çizilir; akım–gerilim bölgelerinden uygun anahtar yapısı seçilir.

SCR yalnız iletime geçiş yönünden kapı kontrollüdür. GTO negatif kapı darbesiyle kesime götürülebilir. Triyak iki yönde akım taşıyabilir; GTO'nun çift yönlü akım taşıdığı sonucu çıkarılmamalıdır.

## Kısa sınav 3: DC–DC ve geri besleme

Doğrusal ve anahtarlamalı güç kaynakları boyut, kayıp, çıkış dalgalanması ve kontrol yönünden karşılaştırılır. H-köprüde pozitif/negatif çıkış ve tek yönlü gerilim için hangi anahtarların iletimde olduğu sorulur. Boost'ta anahtar iletimdeyken diL/dt = Vin/L'dir.

Örnek geri beslemeli buck devresinde 20 V kaynak, 150 µH endüktör, 100 µF kapasite ve 32 Ω başlangıç yükü bulunur. Çıkıştan eşit dirençli bölücüyle örnek alınır; 2,5 V referansla 5 V çıkış elde edilir. Kaynaktaki cevapta 6 V hedefi için referansın 3 V yapılması yazılıdır. Hata yükselteci ve karşılaştırıcının görevleri, 3 ms sonra ek yük bağlanmasının etkisi sorulur.

## Kısa sınav 4: Evirici ve harmonikler

THD'nin anlamı açıklanır; temel bileşenin dışındaki RMS bileşenlerin temel RMS'ye oranı kullanılır. Şebekeden ayarlanabilir AC üretimi için üç yapı istenir:

- Kontrollü doğrultucu + kare dalga evirici: genlik doğrultucudan, frekans eviriciden.
- Kontrolsüz doğrultucu + buck + kare dalga evirici: genlik buck'tan, frekans eviriciden.
- Kontrolsüz doğrultucu + SPWM evirici: iki ayar da eviriciden.

100 V DC, R = 10 Ω, L = 25 mH ve 60 Hz kare dalga örneğinde çıkış RMS, tek harmonik akımları ve THD istenir. Son soru kâğıdın yüzey alanının ölçüm aracı kullanmadan tahminidir.

## Kısa sınav 5: PWM ve AC gerilim denetimi

İki kondansatörlü yarım köprüde önce üst veya alt anahtarın kapanmasına göre çıkışın işareti çizilir. H-köprü için bipolar ve unipolar SPWM kapı işaretleri üretilir. Gerilim grafiğinden ma ve mf oranları, normalize spektrumdan anahtarlama yöntemi belirlenir.

DC/DC'nin frekans yükselten veya düşüren bir AC frekans dönüştürücü olmadığı; DC gerilim düzeyi değiştirdiği vurgulanır. Faz kontrollü AC çıkış için RMS integrali yalnız iletim aralıklarında alınır.

## Kısa sınav 6: DC makineler

Motor ve jeneratörde E = KΦω, T = KΦIa ve Pdönüşüm = EIa = Tω ilişkileri kullanılır. Eşdeğer devrede endüvi direnci, endüktansı ve zıt EMK yer alır. Motorun ilk hareketinde E = 0 olduğundan akım sınırlama gerekir.

Sorular 220 V DC motorun şebekeden ayarlanabilir beslenmesi, moment–hız eğrisi, kayıplarla verim, şönt motor kalkış akımı ve sargılı motorlarda hız ayarını kapsar. Birçok cevabın yalnız ders slaytına gönderme yaptığı kaynak düzeni korunmuştur.

*Not: A/B formlarının aynı soruları farklı sırada veren kısımları burada birleştirildi. “Cevap Anahtarı” yazısı öğrenci adı değildir. PDF Title/Author alanları yeniden oluşturularak temizlendi.*
