---
baslik: EEM474 Güç Elektroniği: el yazısı ders notları (anahtarlardan motorlara)
ozet: Anahtarlama elemanları, doğrultucular, DC/DC çeviriciler, SPWM, AC gerilim denetimi, UPS ve DC motorlar üzerine 53 sayfalık el yazısı ders notları ve sayısal örnekler.
---

Bir arkadaşın kareli deftere el yazısıyla tuttuğu EEM474 Güç Elektroniği ders notlarının (53 sayfa) taranmış hâli. Kişisel bilgiler çıkarıldı. Aşağıda sayfaların başlıkları, formülleri ve çözülen örnekler metne aktarılmıştır; tüm sayfalar yazının sonundaki PDF'te el yazısı hâliyle bulunur. Notlar, dersin sunumlarındaki sırayı izler: anahtarlar, doğrultucular, DC/DC çeviriciler, evirici, AC gerilim denetimi, UPS ve motorlar.

## Anahtarlama elemanları (sayfa 1–9)

**Enerji geri kazanımı.** Anahtar iletimdeyken bobinde enerji depolanır (vL = L·di/dt). Anahtar açıldığında bobindeki enerji diyotlar üzerinden kaynağa geri verilir.

**İdeal güç anahtarı.** İletimdeyken iç direnç 0 olmalı, kesimdeyken akım 0 olmalı; ton = 0 ve toff = 0 beklenir; iletimden kesime geçerken enerji gerekmemelidir. Gerçek anahtar ideal değildir.

**Anahtarlar (kontrol açısından).** 1) Kontrolsüz anahtarlar (diyot). 2) Yarı kontrollü anahtarlar: yalnız iletime geçmesi ya da kesime geçmesi kontrol edilebilir (tristör). 3) Tam kontrollü anahtarlar (transistör). Yarı iletken anahtarlar: sürekli kapı sinyali ister (BJT, MOSFET: gerilim kontrollü), darbe (pulse) kapı sinyali ister (anlık darbe gelince iletimde kalır), bipolar gerilim, unipolar gerilim, çift yönlü akım, tek yönlü akım gibi sınıflara ayrılır.

- **Tristör:** yarı kontrollüdür, yalnız iletime geçmesini kontrol eder. Triyak: iki tristörün paralel (ters) bağlanmasıyla oluşur, çift yönlü akım geçirir. GTO: hem iletime hem kesime geçmesini kontrol eder.
- **Diyot karakteristiği** ve **tristör karakteristiği:** diyot ile ortak yön: tristörün iletime geçmesi için ileri yönde polarite (anoda göre katot) gerekir; diyottan farkı: iletime geçmesi için gate'ten katoda belli bir süre akım geçmesi gerekir.

**Anahtarların karşılaştırılması.** Gerilim, akım ve frekansa göre eleman seçilir. Tristörler en yüksek gerilim ve akımda çalışır; en hızlı çalışanlar MOSFET'lerdir (en yüksek frekans). Frekans ile çalışma hızı doğru orantılıdır. Tristör ve GTO darbe kontrollüdür: tristör gate'ine uygulanan darbeyle iletime geçer, yük gerilimi darbeden sonra devam eder; bu nedenle yalnız iletimi kontrol eder. GTO hem iletimi hem kesimi kontrol eder ve enerji tasarrufu vardır. Transistör ve MOSFET sürekli kontrol ister. IGBT, tristör, transistör ve MOSFET'in iyi özelliklerinin birleştirilmesiyle yapılmıştır. Bir transistör iki yönlü akım çeksin denirse yanına ters paralel diyot bağlanır.

**Anahtarların çalışma bölgesi (i–v düzleminde).** Diyot: iletimde yalnız i ekseninin pozitif yarısı, kesimde v ekseninin negatif yarısı. BJT: iletimde i ekseninde, kesimde pozitif v ekseninde. Transistör ile ters paralel diyot: iletimde (transistör) pozitif i, (diyot) negatif i; kesimde v ekseni. İkisi seri bağlanırsa yalnız kesim durumunda gerilim her iki yönde görülür.

## Harmonik güç örnekleri (sayfa 10–12)

**Örnek 1.** v(t) = 4 + 8 sin(ω₁t + 10°) + 5 sin(ω₂t + 50°); Vrms = √(4² + (8/√2)² + (5/√2)²) = 7,78 V.

**Örnek 2.** v(t) = 100 cos(377t) V; i(t) = 8 + 15 cos(377t + 30°) + 6 cos(2·377t + 45°) + 2 cos(3·377t + 60°) A.

- a) Yükün çektiği güç: P = 0·8 + (100/√2)(15/√2) cos30° + 0 + 0 = 650 W (doğru bileşen 0 olduğundan DC güç yok).
- b) PF: Vrms = 100/√2 = 70,7 V; Irms = √(8² + (15/√2)² + (6/√2)² + (2/√2)²) = 14 A; PF = P/S = 650/(70,7·14) ≈ 0,66.
- c) DF = I₁,rms/Irms = (15/√2)/14 ≈ 0,76.
- d) THD = √((Irms² − I₁,rms²)/I₁,rms²) = √((14² − (15/√2)²)/(15/√2)²) ≈ 0,86 (%86). THD'nin 0'a, DF'nin 1'e yaklaşması beklenir.

*Not: 650 W, 100·15/2·cos 30° = 649,5 W değerinin yuvarlanmışıdır. Irms² = 8² + 112,5 + 18 + 2 = 196,5 olduğundan Irms ≈ 14,02 A, PF = 649,5/(70,71·14,02) ≈ 0,655 ve THD ≈ 0,86 bulunur; kâğıttaki sonuçlar doğrudur.*

## Yarım ve tam dalga doğrultucu (sayfa 12–17)

- Tristör kullanılırsa tetikleme noktası α'dır (π'den önceki noktada tetiklenmesi gerekir). İki diyot kullanılırsa transformatör (orta uçlu) gerekir; dört diyot (köprü) kullanılırsa transformatöre gerek yoktur. İki diyotlu devrede ters (inverse) gerilimler farklıdır.
- RF, FF, η hesaplarına bak: verim η = Pdc/Pac (yarım dalga: tek diyot, tam dalga: 2 veya 4 diyot; verim artar). FF = Vrms/Vdc (form faktörü), RF = Vac/Vdc (ripple faktörü); tam dalga doğrultucuda yarım dalgaya göre daha az salınım vardır, bu nedenle RF düşer.
- **Tam dalga köprü:** yarım dalgadaki gibi diyot yerine tristör kullanılabilir; çapraz tristörlerin aynı anda tetiklenmesi gerekir. 90° ve 150° tetiklenirse hangisi geç tetikleniyorsa o baskın olur (çıkış 150°–180° arasında).
- **RL yüklü yarım dalga doğrultucu.** Yük R ve L ise diyot iletimdeyken L enerji depolar: vL = L·di/dt. Akım azaldığında polarite değişir; yani bobin akım yolu ya da gerilim kaynağı gibi davranmaya başlar. Bu etki bobinin depoladığı enerjidir ve akım π'den sonra da akmaya devam eder (π + β'ya kadar). α'nın değeri L'nin büyüklüğüne göre değişir; L büyüdükçe ya da kaynak frekansı arttıkça süreklilik artar. Bu kısmi negatif gerilim bölümünü yok etmek için R-L'ye paralel bir serbest dolaşım diyotu bağlanır; bağlanırsa devre doğrudan R'ye bağlıymış gibi çalışır ve yükün gerilimi her zaman pozitif kalır, akım ise sürekli hâle gelir.
- Özet: AC'yi DC'ye dönüştürürken R-L yük varsa üzerinde enerji toplanır; bunun kaynağa aktarılmasını engellemek için paralel diyot bağlanır.
- DC motor matematiksel olarak R, L ve E'den oluşur: motor dönmediği sürece yalnız R ve L vardır, motor dönmeye başladıkça E (zıt EMK) gelir. Dört tristörlü doğrultucu RLE (DC motor) devresinde çıkış α ve α + π arasında akım taşır.

## Üç fazlı doğrultucular (sayfa 18–20)

Tek fazlı alternatörden farklı olarak üç fazda sinüs üretilir ve fazlar arasında 120° fark vardır. Özellikleri: 1) tek fazlı doğrultulduğunda dalgalanma çoktur; 2) tek fazda güç faktörü düşüktür; 3) üç fazda daha yüksek güç alınır.

- **Yarım dalga üç fazlı doğrultucu:** her faza bir diyot bağlanır; kaynaktaki fazlar birbirini izler. 1. diyot iletimdeyken 2 ve 3 kesimdedir; sonra 2. diyot, 1 ve 3 kesimde; tekrar başa döner. Bir periyodu üç diyot paylaşır, her diyot 120° iletimde kalır. Çıkış DC'ye daha çok benzer.
- **Üç fazlı tam dalga doğrultucu:** her faz için iki diyot, toplam altı diyot; her diyotun iletim süresi 60°; her anda iki diyot iletimdedir. Çıkış DC'ye daha da yakındır.

## DC'den DC'ye çeviriciler (sayfa 21–31)

**Doğrusal (lineer) ve anahtarlamalı.** Doğrusal çevirici: transistör ya da MOSFET lineer bölgede çalışır (seri veya paralel); gerilim düşürme, ör. LM7805 (12 V'tan 5 V'a). Hat regülasyonu (line regulation): giriş gerilimi belli sınırlar içinde değişse de çıkış gerilimi sabit kalır; yük regülasyonu (load regulation): yük değişse de çıkış sabit kalır. Regülasyon olan yerde bir geri besleme (feedback) sözkonusudur.

**Anahtarlama usulü (SMPS).** Lineerde boşta transformatör yoktur, ama anahtarlamada boşta transformatör vardır: AC → DC → AC (yüksek frekans) → DC. Yükseltme/alçaltma yapılabilir; hacim ve boyut küçüktür (transformatörün boyutundan dolayı), kapasitörlerin boyutu küçüktür; frekans değeri 25 kHz civarındadır (lineerde 50 Hz). Dalgalanma ΔV = 1/(2·e·f·C) biçiminde yazılmıştır.

**Chopper DC/DC.** Lineer: değişken direnç gibi, anlık olarak gerilim kontrol edilir. Anahtarlamalı: anlık olarak bakılmaz, ortalama değere bakılır; chopper ile DC/DC dönüştürücüde gerilim değiştirilebilir. Vavg = K·Vs, K = ton/(ton + toff) = ton/T (duty cycle ya da darbeleme oranı); Vrms = √K·Vs. Vavg ve Vrms K'ya bağlıdır; çıkış gerilimi K ile değişir. K'yı değiştirmenin iki yolu vardır: 1) PWM: ton değiştirilir, T sabittir; 2) frekans modülasyonu: ton sabit, T artar ya da azalır.

**Örnek.** 48 V kaynak, 25 kHz anahtarlama, 24 Ω yük, ton = 1 ms (kâğıtta bu değer verilmiş): T = 1/f = 4 ms (kâğıtta "T = 1 ms" yazmıştır) ve K = 1/4 olarak alınmış; Vo = (1/4)·48 = 12 V, Vrms = √(1/4)·48 = 24 V.

*Not: Kâğıtta frekans "25 kHz" olarak yazılmış ancak hesap T = 4 ms'e (250 Hz) göre yapılmıştır; ton = 1 ms ve K = 1/4 için T = 4 ms gerekir. 25 kHz'de T = 40 µs'dir. Sonuçlar (12 V ve 24 V) K = 1/4 için doğrudur.*

**Buck (azaltan) çevirici.** Anahtar kapalıyken bobin gerilimi VL = Vd − Vo = Vin − Vo; anahtar açıkken VL = −Vo. RL yük olursa akım üsteldir; ΔImax = Vs/(4fL); anahtarlama frekansının yüksek olması istenir; Vo = K·Vin, 0 ≤ K ≤ 1, Vo ≤ Vin.

**Boost (yükselten) çevirici ("Principle of step-up operation").** Anahtar kapalıyken (iletimde) VL = Vs, ΔiL = Vs·DT/L; anahtar açıkken (iletimde değil) bobin polarite değiştirir, Vo = Vs + VL: Vo = Vs[1 + t1/t2] = Vs/(1 − K). K = 0,5 için Vo = 2Vs; K → 1 için Vo → ∞ (gerilim yükseltmenin yolu). ΔiL(kapalı) + ΔiL(açık) = 0 ile Vo = Vd/(1 − D); Vo ≥ Vd. Giriş gücü = çıkış gücü: Vd·Id = Vo²/R. Bobin akımı üçgen biçimli: Imax = IL + ΔiL/2, Imin = IL − ΔiL/2.

**Konverter sınıflandırması.** 1. bölge chopper (Vo–Io düzleminde yalnız 1. bölge; asolton converter); 2. bölge chopper (motor; diyotlu); 1. ve 2. bölge chopper.

**Sürekli iletim sınırı.** Imin ≥ 0 için Lmin = D(1 − D)²·T·R/2; "okimin sıfıra düşmemesi için Lmin". Ripple = ΔVo/Vo, ΔVo/Vo = D/(R·C·f); anahtarlama frekansı arttıkça dalgalanma azalır. ΔiL(on) + ΔiL(off) = 0 ve VL ortalaması 0; tüm çeviricilerde Vo/Vd'yi bulmak için bu iki koşul kullanılır.

**Örnek (boost).** Vo = 30 V, Vin = 12 V, ripple %1, R = 50 Ω, f = 25 kHz. D = 1 − Vs/Vo = 1 − 12/30 = 0,6. Lmin = D(1 − D)²R/(2f) = 0,6·(0,4)²·50/(2·25000) = 96 µH. IL = Vs/((1 − D)²R) = 12/(0,16·50) = 1,5 A; ΔiL/2 = Vs·DT/(2L) = 1,2 A; Imax = 2,7 A, Imin = 0,3 A. C > D/(R·f·(ΔVo/Vo)) = 0,6/(50·25·10³·0,01) = 48 µF.

**Buck-boost çevirici.** D > 0 için boost (Vo > Vs) ve buck'a dönüşebilir; çıkış geriliminin polaritesi girişin tersidir. Anahtar iletimde VL = Vd, ΔiL(on) = Vd·DT/L; anahtar kesimdeyken VL = Vo (büyüklükçe), ΔiL(off) = Vo(1 − D)T/L; sonuç Vo = −Vs·D/(1 − D) (D = 0,5 için Vo = −Vs: yalnız polarite değişir; D = 0'da Vo = 0, D → 1'de Vo → ∞). Seçim: gerilim düşüyor ve polarite değişiyorsa buck-boost; yalnız gerilim düşüyorsa buck; gerilim artıyor ve polarite aynıysa boost; yalnız polarite değişimi isteniyorsa buck-boost.

**Ćuk çevirici.** Aynen buck-boost gibi çalışır: Vo = −Vs·D/(1 − D). (Buck-boost, buck, boost çeviricilerin şekillerine bak; sınavda sorulabilir.)

## DC/DC çeviricilerin kontrolü (sayfa 32–36)

Kaynak → güç elektroniği devresi → yük; çıkıştan geri besleme ile kontrol bloğu (referans ile karşılaştırma, regülatör). Line regulation: girişin belli sınırlar içinde değişmesine rağmen X gerilimi sabit; load regulation: yük değişse de gerilim sabit. Voltaj modu kontrol (VL'ye bakılır) ve akım modu kontrol (iL'ye bakılır). Vo'yu artırmak için D artırılır: Vo = D·Vs (buck). D'yi değiştirmek için PWM kullanılır: testere dişi sinyal ile Vc (V₂) karşılaştırılır; V₂ artarsa darbe genişliği artar, azalırsa daralır; D = ton/T, Vo = D·Vs.

Kontrol döngüsü: Vo artar ya da azalırsa V₂ değişir → V₃ değişir → D değişir → Vo = D·Vs. Anahtar yerine transistör kullanılırsa BE ve CE'yi değiştirir. Voltaj modunda Vo üzerindeki gerilimden, akım modunda akımdan örnek alınır (akım örneği için küçük değerli direnç kullanılır; watt'ı yüksek, direnç değeri küçük).

**Örnek (buck).** L = 100 µH, Vin = 40 V, D = 0,3, Po = 24 W, fs = 100 kHz, Ts = 10 µs. Vo = D·Vin = 12 V; Io = Po/Vo = 2 A; R = Vo/Io = 6 Ω; IL = Io = 2 A; ΔiL = (Vin − Vo)/L · D·Ts = 0,84 A (tepeden tepeye); Imax = IL + Δi/2 = 2,42 A, Imin = 1,58 A. Bobin gerilimi 3 µs boyunca +28 V, 7 µs boyunca −12 V.

**Örnek (boost).** L = 100 µH, Vin = 12 V, D = 0,4, Po = 30 W, fs = 100 kHz. Vo = Vin/(1 − D) = 20 V; Io = 30/20 = 1,5 A; IL = Iin = 30/12 = 2,5 A; ΔiL = Vs·DT/L = (12/100 µ)·4 µ = 0,48 A; Imax = 2,74 A, Imin = 2,26 A; bobin gerilimi 4 µs boyunca +12 V, 6 µs boyunca −8 V.

**Örnek (buck-boost).** L = 100 µH, Vin = 12 V, D = 0,6, Po = 36 W, fs = 100 kHz. Bobin gerilimi 0,6T boyunca +12 V, 0,4T boyunca −18 V; ortalama bobin akımı 5 A (ΔiL = 0,72 A; Imax = 5,36 A, Imin = 4,64 A).

**PWM ve geri besleme çevrimi.** D = ton/Ts = Vcontrol/Vst; Vcontrol = D·Vst. Çıkıştan gerilim bölücü ile Vo'nun bir kısmı (R2/(R1 + R2) = K) alınır, Vref ile karşılaştırılıp hata yükselteci (A·(Vref − Vin·D·K)) PWM'e verilir; Vo değişimi D değişimidir (frekans sabit, duty cycle değişir). Vo'nun olduğu yerde yük R değişirse Vo değişir. **Kullanılabilecek programlar:** PSPICE, PSIM, MATLAB, PSCAD; PSIM'de "run simulation" ile kolemanlar (bağlantılar) yapılır.

## Evirici ve SPWM (sayfa 37–39)

Tek fazlı tam köprü (S1–S4 anahtarları, Vdc kaynağı, AC yük), SPWM bloğuna ma, mf ve fsine girişleri verilir. V₁ = ma·Vdc: 1) sinüsün genliği, 2) frekansı kontrol edilebilir, 3) var olan harmonikler. ma = Vsin/Vtri (modülasyon indeksi, 0–1 arasında); mf = ftri/fsin ≫ 1 (frekans indeksi). ma değişimi Vsin'in değişimiyle ilgilidir.

SPWM bipolar ve unipolar olarak ikiye ayrılır; kontrol bölümlerine göre farklılık gösterirler ama filtreden sonra çıkışları aynıdır. Bipolar SPWM: üçgen dalga ve sinüs bir karşılaştırıcıya verilir; çıkış Q1, Q4'e doğrudan, Q2, Q3'e terslenerek uygulanır. Unipolar SPWM: iki karşılaştırıcı, sinüs 180° faz farkıyla gönderilir; Q1, Q2 ve Q3, Q4 çiftleri. Bu iki devrenin temel farkı oluşan harmoniklerdir.

## AC–AC dönüşüm ve gerilim denetimi (sayfa 39–47)

AC'den AC'ye iki şekilde yapılır: 1) evirici kullanmadan (genlik ayarı: AC gerilimin RMS değeri değiştirilir, on-off ve phase control; frekans ayarı), 2) evirici kullanarak (AC/DC → DC/AC). Genlik ayarı isteniyorsa transformatör kullanılır.

**RMS kontrol: 1) On-off.** İki antiparalel tristör (TR1, TR2); m ve n katsayıları: n saykıl ON (α = 0'da tetiklenir, diyot gibi çalışır), m saykıl OFF. Vrms = Vs·√(n/(m + n)) = Vs·√k. Kesim süresi (m) azaldıkça PF iyileşir.

**2) Phase control.** α değeri değişkendir. Tek yönlü (tristör + diyot) devrede tristör α'da tetiklenir; π anında tetiklenirse... Çıkışta max değer kaynağın değeridir (α = 0'da tetikleme); min değer tristörün π'de tetiklendiği anda, yani negatif sinüs değeri (diyot) için −Vm/2 (kâğıttaki yazım). Tristörün üzerindeki dalga şekli: π'den sonrasını göremeyiz, çünkü diyot olduğu için göremeyiz. İki tristör paralel bağlanırsa (SCR1, SCR2) çıkışın ortalama değeri 0'dır ve aynı dalga şekli iki diyotlu köprüyle de elde edilir: tristörden tek yönlü, R'den çift yönlü akım geçer. RL devrelerinde L'nin etkisiyle tristör π'den daha fazla süre iletimde kalır (π + β). R olduğu zaman 1 kere tetikleniyordu; R + L olduğunda birkaç kere tetiklenmesi gerekir.

**Cycle converter.** İki anti-paralel doğrultucu grubu (1 ve 2) ile AC/AC; bu işlemi 1. grup, sonra 2. grup yaparsak periyodik +'dan −'ye bir dalga oluşur; frekans kaynak frekansının altında kalmış olur. Dezavantajı harmoniklerin artmasıdır.

**Triyak.** En büyük avantajı çift yönlü akım geçirmesidir. Dimmer: triyak (A1, A2, G) ile yük (lamba); α tetikleme açısını değiştirerek Vrms ayarlanır, α arttıkça 220 V yerine daha az voltaj elde edilir ve lamba daha düşük ışıkta yanar. Diyak, zener diyot gibi davranır (AC için), belli bir değere kadar geçişe izin vermez. Tristörün çalışma bölgesi (i–v düzleminde) ile triyakın çalışma bölgesi çizilmiştir (triyak 1. ve 3. bölge).

**Soru.** Yarım köprü (tristör + diyotlu iki farklı devre; D1–D4 ve T1) için a) iki devrenin çıkışı aynıdır; b) Vout = Vm/π (α = 90° için cos90° = 0); Vo = (1/π)∫α→π Vm sin(ωt) dωt = (Vm/π)(1 + cos α). 1. devrede T1 için akım sürekli aynı yöndedir; 2. devrede triyak için çift yönlü akım geçirdiği için akım iki yönde akar.

## UPS (sayfa 49)

DC'den AC'ye dönüştürücü kullanılır. UPS iki gruba ayrılır: 1) online (evirici sürekli çalışır), 2) offline (evirici sürekli çalışmaz). Şehir şebekesi varken bataryaya şarj olur; şehir şebekesi yokken bataryadan enerji verilir.

## Motorlar (sayfa 50–53)

**Motor seçimi:** 1) maliyet, 2) termal kapasite, 3) verim, 4) tork-hız profili. AC motorlar: indüksiyon, senkron, üniversal. DC motorlar: sargılı DC motorlar, sabit mıknatıslı, fırçasız (çalışması için elektronik devre bulunması gerekir).

**Makine verimi:** η = Po/Pin; üç biçimde ifade edilir: η = Po/Pi × 100 %, η = Po/(Po + Ploss) × 100 %, η = (Pi − Ploss)/Pi × 100 %.

**Motor ve jeneratör.** Elektrik enerjisi ↔ mekanik enerji. Mekanik → elektrik: E = K·Φ·ω (ω açısal hız, Φ manyetik akı). Elektrik → mekanik: T = K·Φ·I (I akım). Aynı makine verilen enerjiye göre hem motor hem jeneratör olarak çalışabilir. P = E·IA = T·ω. Motorda U > EA, jeneratörde EA > U. Motor dönmezse E = 0'dır. Devre: V = Ia·Ra + Ea, Ea = KΦω; DC gerilimde L kısa devre olur.

**Sabit mıknatıslı DC motor.** Açısal hız 0 iken tork maksimumdur, açısal hız maksimum iken tork 0'dır (ters orantı vardır). U = E + Ia·Ra, I = T/(KΦ). ω = Vs/(KΦ) − Ra·T/(KΦ)² (eğim negatif); Vs değiştikçe eğim değişmez, fakat karakteristik paralel kayar.

**Sargılı DC motor — şönt motor.** Alan sargısı rotora paralel bağlıdır; U'nun yönünü değiştirsek de alan ve rotorun yönü değişeceğinden motorun yönü değişmez. Yüke göre hız değişimi düşüktür. **Yabancı (ayrılmış) motor:** ya U_E'yi ya da U_A'yı değiştirdiğimizde motorun yönü değişir. **Seri motor:** rotor ve sargı seri bağlanmıştır; motorun yönü değişmez, torku çok yüksektir. **Compound-wound motor:** motorun yönü değişir. Üzerinde harcanan kayıp sargılı DC motorda daha fazladır (iç dirençler yüzünden).
