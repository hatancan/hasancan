---
baslik: EEM322 Denetim Sistemleri: Ders Defteri (Şubat 2013) – Op-Amp Devreleri, Mekanik Sistemler, Elektriksel Benzeşim ve Blok Diyagramları
ozet: EEM322 Denetim Sistemleri 2013 bahar dönemi ders defterinden ilk haftalar: op-amp ile tersleyen, integral alan ve türev alan devrelerin aktarım işlevleri, iki kütleli mekanik sistemin dinamik denklemleri ve f-i, f-v benzeşimleri, alan kontrollü motor, RC devrelerinde yükleme etkisi, bozucu girişli sistem ve sıcaklık denetim sisteminin blok diyagramı.
---

Bu yazı, Başkent Üniversitesi **EEM322 Denetim Sistemleri** dersinin 2013 bahar dönemine ait bir **ders defterinin** ilk haftalarını içeriyor (17 ve 25 Şubat 2013'te çekilmiş sayfalar). Defter bir arkadaşa ait. Sayfalar **fotoğraflanmış sayfalardan metne aktarıldı**; fotoğraflar yayınlanmadı. Derste anlatılan örnekler büyük ölçüde İngilizce yazılmış, araya Türkçe açıklamalar eklenmiş. Aşağıda başlıklar, ana formüller ve sonuçlar aktarıldı. Derste izlenen kitabın blok diyagramı kuralları tablosunun (Tablo 2.3, s. 40–41) fotoğrafları kitap sayfası olduğu için aktarılmadı; yalnız defter sahibinin kenar notları özetlendi.

Aynı konuların ders notu karşılığı [Ders 2](/arsiv/eem322-ders-02-modelleme/) ve [Ders 4](/arsiv/eem322-ders-04-blok-diyagram/) yazılarında. Defterin devamı: [durum uzayı](/arsiv/eem322-defter-durum-uzayi/) ve [kalıcı durum hatası, Routh ve kök yer eğrisi](/arsiv/eem322-defter-kalici-hata-routh-kok-yer/).

## Örnek 1(a): Elektronik sistemler, op-amp devresi

Tersleyen girişe Z₁ (R₁ ∥ C₁), geri beslemeye Z₂ (R₂ ∥ C₂) bağlanmış op-amp devresi. Op-ampın eviren girişindeki gerilim E′(s) ≅ 0 olduğundan:

- [Ei(s) − E′(s)]/Z₁(s) = [E′(s) − Eo(s)]/Z₂(s) ⇒ Eo(s)/Ei(s) = −Z₂(s)/Z₁(s)

Karmaşık empedanslar:

- Z₁(s) = 1/(C₁s + 1/R₁) = R₁/(R₁C₁s + 1)
- Z₂(s) = 1/(C₂s + 1/R₂) = R₂/(R₂C₂s + 1)
- Eo(s)/Ei(s) = −(R₂/R₁)·(R₁C₁s + 1)/(R₂C₂s + 1) = −(C₁/C₂)·(s + 1/(R₁C₁))/(s + 1/(R₂C₂))

Aktarım işlevinin eksi işaretli olduğuna, yani devrenin tersleyen yükselteç olduğuna dikkat çekiliyor. Pozitif işaret için çıkışa ikinci bir tersleyen kat (R₃ girişte, R₄ geri beslemede) eklenebilir: E′o(s)/Eo(s) = −R₄/R₃.

Özel durumlar:

- Z₁ = R, Z₂ = 1/(Cs): integral alan devre, Eo/Ei = −1/(RCs)
- Z₁ = 1/(Cs), Z₂ = R: türev alan devre, Eo/Ei = −RCs
- Z₂ = R₂, Z₁ = R₁/(R₁C₁s + 1): başka bir türev alan devre, Eo/Ei = −R₂(R₁C₁s + 1)/R₁

## Örnek 2(a): İki kütleli mekanik sistem (Pr. 2.2(e))

Kitabın arkasındaki problemlerden alınmış: duvara K yayı ile bağlı M₂ kütlesi, B₂ sönümleyicisiyle M₁ kütlesine bağlı; M₁ ile duvar arasında B₁ sönümleyicisi var, M₁'e f kuvveti uygulanıyor. İki yer değiştirme var: x (çıkış, M₁) ve y (M₂). Mekanik devre kuvvet kaynağıyla kuruluyor; kütleler düğüm ile referans (dayanak noktası) arasında oluyor.

Dinamik denklemler:

- M₁ d²x/dt² + B₁ dx/dt + B₂ d(x − y)/dt = f
- M₂ d²y/dt² + Ky = B₂ d(x − y)/dt

Benzer (analog) devreler:

- **f-i (kuvvet-akım) benzeşimi:** akım kaynağı i, iki düğüm gerilimi v₁ ve v₂; C = M, R = 1/B, L = 1/K. v₁ düğümünde C₁ ve R₁, düğümler arasında R₂, v₂ düğümünde C₂ ve L.
- **f-v (kuvvet-gerilim) benzeşimi:** iki düğüm iki çevreye dönüşüyor, akım kaynağı gerilim kaynağı oluyor. Birinci çevrede L₁ ve R₁, ortak kolda R₂, ikinci çevrede L₂ ve C. R = B, C = 1/K, L = M. Defterdeki not: "Yer değiştirme farkı, değişkenler arasına yerleşir."

## Alan kontrollü motor ve dişli kutusu

Laplace tanım denklemleriyle kurulan blok zinciri: Vf → 1/(Lfs + Rf) → If → Kg → Vg → 1/(Leq s + Req) → Ig → Km → T → 1/(Jeq s² + Beq s) → θ → n → θL. Aktarım işlevi:

- θL(s)/Vf(s) = Kg Km n / [(Lfs + Rf)(Leq s + Req)(Jeq s² + Beq s)]

## Blok diyagramı cebiri (kenar notları)

Kitaptaki "Rules of Block Diagram Algebra" tablosuna düşülen notlar:

- Art arda gelen toplama noktalarında işaretlerin (+ ya da −) yeri değişebilir.
- Seri bloklar çarpılır; ancak bu, bloklar arasında **yükleme yoksa** geçerlidir ("yükleme yoksa öbekler böyle çizilebiliyorsa yükleme yok demektir").
- Paralel (ileri yol beslemeli) bloklar toplanır; ayrılma noktasında aynı değerde sinyal gider.
- Toplama noktası bir bloğun önüne alınırken diğer girişe mutlaka 1/G eklenmelidir.
- Ayrılma noktası ile toplama noktasının yeri değiştirilebilir; G₂ geri beslemeli yapı birim geri beslemeye çevrilebilir: [G₁G₂/(1 + G₁G₂)]·(1/G₂) = G₁/(1 + G₁G₂).

## Örnek 3(a): Yükleme etkisi ve blok diyagramı

Önce tek RC devresi (seri R, paralel C):

1. Zaman bölgesi: i = (vi − vo)/R, vo = (1/C)∫i dt
1. Sıfır başlangıç koşullarıyla Laplace: I(s) = [Vi(s) − Vo(s)]/R, Vo(s) = I(s)/(Cs)
1. Neden-sonuç ilişkisine göre alt bloklar çiziliyor.
1. Birleştirince birim geri beslemeli yapı: Vo(s)/Vi(s) = 1/(RCs + 1)

Sonra iki RC devresi art arda (R₁, C₁, R₂, C₂):

- V₁ + R₁i₁ = vi, (1/C₁)∫(i₁ − i₂)dt = v₁, vo + R₂i₂ = v₁, (1/C₂)∫i₂ dt = vo
- I₁(s) = [Vi(s) − V₁(s)]/R₁, V₁(s) = [I₁(s) − I₂(s)]/(C₁s), I₂(s) = [V₁(s) − Vo(s)]/R₂, Vo(s) = I₂(s)/(C₂s)
- Vo(s)/Vi(s) = 1/[R₁C₁R₂C₂s² + (R₁C₁ + R₂C₂ + R₁C₂)s + 1]

Sonuç, iki birinci dereceden bloğun çarpımına, yani [1/(R₁C₁s + 1)]·[1/(R₂C₂s + 1)]'e **eşit değil**: ikinci devre birincisini yüklüyor (R₁C₂ terimi).

## Örnek 4(a): Bozucu giriş

R(s) → P(s) → toplama → C(s) → toplama (D(s) bozucusu) → G(s) → Y(s), geri beslemede H(s). İki giriş olduğundan etkiler tek tek bulunup toplanıyor:

- D(s) = 0 için: Y_R(s) = [C(s)G(s)/(1 + C(s)G(s)H(s))]·P(s)R(s)
- R(s) = 0 için: Y_D(s) = [G(s)/(1 + C(s)G(s)H(s))]·D(s)
- Toplam: Y(s) = C(s)G(s)P(s)R(s)/(1 + CGH) + G(s)D(s)/(1 + CGH)

## Örnek 5(a): Sıcaklık denetim sistemi

Bir yükselteç (K₁), solenoid (L, R; kütlesi ihmal edilen, B ve K'lı), solenoidin açtığı vana ile buhar debisi q ve ısıtıcı teldeki sıcaklığı ölçen termokupl (Kt) ile K₂ kazançlı geri beslemeden oluşan sistem. Vana açıklığı q = Ks x; sıcaklık ile buhar debisi arasında dT/dt = −CT + Kc q ilişkisi var.

Sistem denklemleri ve Laplace karşılıkları:

- K₁e = L di/dt + Ri ⇒ K₁E(s) = (Ls + R)I(s)
- f = Kf i = B dx/dt + Kx ⇒ Kf I(s) = (Bs + K)X(s)
- q = Ks x ⇒ Q(s) = Ks X(s)
- dT/dt = −CT + Kc q ⇒ (s + C)T(s) = Kc Q(s)
- et = Kt T ⇒ Et(s) = Kt T(s)
- e = r − K₂et ⇒ E(s) = R(s) − K₂Et(s)

Kapalı çevrim aktarım işlevi:

- T(s)/R(s) = K₁KfKsKc / [(Ls + R)(Bs + K)(s + C) + K₁KfKsKcKtK₂]

*Not: Defterdeki blok diyagramında termokupl bloğu "Kf" diye etiketlenmiş; denklemlere göre bu blok Kt olmalı. Aktarım işlevi Kt ile doğru yazılmış.*
