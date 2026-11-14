---
baslik: EEM441 Haberleşme I: 2009 kısa sınavları (Quiz 1 ve Quiz 3, çözümlü)
ozet: EEM441 Haberleşme I 2009 kısa sınavları: çarpıcı bindirici ve karesel alıcı, genlik bindirimli im ve güç, SSB evre kaydırma, FM sıklık çarpıcı zinciri ve FM çözücüler.
---

Başkent Üniversitesi Elektrik-Elektronik Mühendisliği Bölümü EEM 441 Haberleşme I dersinin 2009'da yapılan üç kısa sınavı: 10 Temmuz 2009 (yaz okulu) Quiz 1, 19 Kasım 2009 Quiz 1 ve 22 Aralık 2009 Quiz 3. Kaynaklar sınav kâğıtlarının ve el yazısı çözümlerin telefon fotoğraflarıdır; fotoğraflanmış sayfalardan metne aktarıldı, fotoğraflar yayınlanmadı. Çözümler bir arkadaşın el yazısı notlarındandır; kişisel bilgi çıkarıldı.

## Quiz 1, 10 Temmuz 2009 (süre 1 saat)

**Soru 1.** Şekildeki öbek gösteriminde e₁(t) = cos ω₁t + cos 2ω₁t, e₂ = A·e₁² olan bir karesel alıcıya ve LPF'ye (kesim 1,5ω₁) paralel gider; toplamdan (e₄) sonra 3,5ω₁–5,5ω₁ bandını geçiren BPF çıkışı e₅'tir. a) e₅'i bulun. b) A = 10 için e₅'in 50 Ω'luk dirençte oluşturacağı ortalama gücü hesaplayın.

*Çözüm.* e₂ = A/2 + (A/2)cos 2ω₁t + A cos ω₁t + A cos 3ω₁t + A/2 + (A/2)cos 4ω₁t; e₃ = cos ω₁t; e₄ = e₂ + e₃. BPF yalnız 4ω₁ bileşenini geçirir: e₅ = (A/2)cos 4ω₁t. P = (A/2)²/(2·50) = A²/400 = 100/400 = 1/4 W.

**Soru 2.** Çarpıcı bindirici (product modulator) öbek gösterimini çizin. Binen im f(t) = 12cos(2π·3×10³t) V, bindirim yüzdesi %80 olan genlik bindirimli im için a) taşıyıcı genliği kaç V olmalıdır; taşıyıcı genliği 12 V'tan küçük olursa ne olur (adı)? b) taşıyıcı sıklığı 30 kHz iken genlik bindirimli imin ifadesi, çift yanlı sıklık görüngesi, bant genişliği. c) 50 Ω'luk dirençte taşıyıcı gücü ve toplam yan bant gücü.

*Çözüm.* m = A_m/A_c = 0,8 ⇒ A_c = 12/0,8 = 15 V. A_c < 12 V olursa m > 1 olur: aşırı bindirim (overmodulation); evre tersliği ve zarf bozukluğu oluşur. s(t) = A_c[1 + m cos(2π·3×10³t)]cos(2π·30×10³t) = 15cos(2π·30k t) + 6cos(2π·27k t) + 6cos(2π·33k t): taşıyıcı 15 V (30 kHz), alt ve üst yan bandın her biri 6 V (27 ve 33 kHz). Bant genişliği 6 kHz. P_c = (15/√2)²/50 = 2,25 W; yan bant gücü 2 × (6/√2)²/50 = 0,72 W.

*Not: El yazısı çözümde yan bant genliği "m·f(t)" ile 0,8×12×15 = 144 alınarak 72 V ve toplam yan bant gücü 103,68 W bulunmuş; çarpım, normalleştirilmemiş mesajla yapıldığı için hatalıdır. Doğru sonuç yan bant başına μA_c/2 = 6 V ve 0,72 W'tır.*

## Quiz 1, 19 Kasım 2009 (süre 1 saat)

**Soru 1.** Şekilde dönemli bir f(t) imi verilmiştir (tepe değeri 5, en küçük değer −2, birkaç ms'lik dönemli sinüs benzeri dalga). a) Genlik bindirimi için taşıyıcı genliğinin en az ne olması gerekir? Taşıyıcı genliği bu değerden küçükse ne gibi bozulmalar olur? Genlik bindirimli imin matematiksel ifadesi nedir? b) Elde edilen GB imini değerler belirterek çizin. c) Taşıyıcı sıklığı 100 kHz alınırsa GB iminin sıklık görüngesini değerler belirterek çizin.

**Soru 2.** SSB imini evre kaydırma yöntemiyle elde eden öbek gösterimde boş kutular var (f₁(t), f₂(t), f₃(t), f₄(t) ve f_SSB(t)). a) Boş kutulara gerekli bilgileri yazın. b) f(t) = Σ cos(ω_i t + θ_i) ve taşıyıcı f_c(t) = cos(ω_c t) ise v(t) = Σ[cos(ω_c t)cos(ω_i t + θ_i) − sin(ω_c t)sin(ω_i t + θ_i)] imini SSB olarak gösterin (ω_c ≫ ω_N); alt mı üst yan bandı mı gösterir? c) Diğer yan band için ifade, d) toplam DSB imi, e) (b) şıkkındaki SSB imi cos(ω_c t) ile çarpılıp alçak geçiren süzgeçten geçirilirse bilgi taşıyan im elde edilir; çarpıcı çıkışındaki imin sıklık görüngesini çizin ve LPF kesim sıklığı f₀'ın aralığını (ω_c, ω₁, … ω_N türünden) belirtin.

*Bu sınavın fotoğraflarında yalnız sorular vardır; çözüm yok.*

## Quiz 3, 22 Aralık 2009 (süre 1 saat)

**Soru 1.** Öbek gösteriminde f₁(t) imi, binen im f(t)'nin f_c1 = 2 MHz taşıyıcılı sıklık bindirimine uğratılmasıyla elde edilmiş dar bant FM imidir; β₁'in en büyük değeri 0,5. Binen im f(t) = cos(2π10³t) + cos(2π·5·10³t) + cos(2π·8·10³t). Sıklık çarpıcılar ×10 ve ×n; arada karıştırıcı (mixer) ve f_LO salıngacı vardır; çıkıştaki f₅(t) taşıyıcı sıklığı f_c5 = 96 MHz ve en büyük sıklık sapması Δf₅ = 80 kHz olan geniş bant FM imi olacak. a) n ve f_LO. b) 1, 2 ve 4 numaralı noktalardaki en büyük sıklık sapmaları (Δf₁, Δf₂, Δf₄). c) 1, 2, 4 ve 5 numaralı noktalardaki bant genişlikleri.

*Çözüm.* f_m,min = 1 kHz, f_m,max = 8 kHz. β₅ = Δf₅/f_m,min = 80 kHz/1 kHz = 80; β₁ = 0,5 olmalı ⇒ 10n = 80/0,5 ⇒ **n = 16**. f_c2 = 10 × 2 = 20 MHz; f_c4 = 96/16 = 6 MHz; f_LO = f_c2 ± f_c4 = 26 MHz veya 14 MHz. Δf₁ = 80 000/160 = 500 Hz, Δf₂ = 10Δf₁ = 5 kHz, Δf₄ = Δf₂ = 5 kHz (Δf₅ = 16 × 5 kHz = 80 kHz). Bant genişlikleri: B₁ = 2f_m,max = 16 kHz; β₂ = 5000/8000 = 0,625 (dar bant) ⇒ B₂ = B₄ = 16 kHz; β₅ = 80 000/8000 = 10 (geniş bant) ⇒ B₅ = 2(1 + 10)·8 kHz = 176 kHz (≈ 2Δf = 160 kHz).

**Soru 2.** a) FM alıcılarında kullanılan sınırlayıcı ve ayırtaçın görevleri; bu devreleri oluşturan öbekler. b) FM imlerinin çözümünde kullanılan i) sıfır geçiş çözücü, ii) evre kilitleyici döngü, iii) geri beslemeli FM çözücü yöntemlerinin öbek gösterimleri.

*Çözüm özeti.* Sınırlayıcı: yüksek kazançlı yükselteç (hard limiter) ve bant geçiren süzgeçten oluşur; ayırtaç girişindeki FM iminin genliğini sabit tutar. Ayırtaç: girişteki imin evresinin türevini alır; bir türev alıcı ve zarf çözücüden oluşur. Sıfır geçiş çözücü: FM im → sınırlayıcı → darbe üreteci → alçak geçiren süzgeç → bilgi imi. Gecikme hatlı çözücü: sınırlayıcı çıkışı ile gecikmiş hâli toplanır, yarım dalga doğrultucu ve alçak geçiren (AGS) zarf çözücüyle bilgi imi elde edilir. (Çözüm sayfasında kaynak olarak Haykin s. 374 ve ODTÜ s. 266 gösterilmiştir.)
