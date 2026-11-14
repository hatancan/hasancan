---
baslik: EEM441 Haberleşme I: 2010 ve 2014 kısa sınavları (SSB evre hatası, FM zinciri, süperheterodin)
ozet: EEM441 Haberleşme I 2010 quizi, 2014 telafi kısa sınavı ve Ağustos 2014 Quiz 2: evre ayrıştırmalı SSB, dengeli modülatör, sıklık çarpıcı zinciri ve görüntü sıklığı.
---

Başkent Üniversitesi EEM 441 Haberleşme I dersinin 2010–2014 arasındaki üç kısa sınavı: 2 Kasım 2010 quizi, 29 Aralık 2014 telafi kısa sınavı ve 6 Ağustos 2014 Quiz 2. Kaynaklar sınav kâğıdı ve çözümlerin (bir kısmı ekran) fotoğraflarıdır; fotoğraflanmış sayfalardan metne aktarıldı, fotoğraflar yayınlanmadı. Telafi sınavının kâğıdındaki öğrenci adı ve numarası aktarılmamıştır.

## Quiz, 2 Kasım 2010

**Soru 1.** Şekildeki evre ayrıştırmalı SSB üretecinde taşıyıcı evre kayması −90° + δ'dır (δ küçük açı hatası). Girişte x(t), üst kolda (A_c/2)cos ω_ct ile çarpılır; alt kolda Hilbert dönüştürücü H_Q(f) ve (A_c/2)sin ω_ct vardır; kollar toplanır veya çıkarılır. a) Çıkıştaki modüleli s(t) ve zarf A(t). b) x(t) = cos ω_mt ve dikey evre kayması için |H_Q(f_m)| = 1 − ε, arg H_Q(f_m) = −90° + δ iken s(t)'yi iki sinüsoidin toplamı olarak yeniden hesaplayın (ε, δ küçük hatalar).

**Soru 2.** Genlik modülatörleri dengesiz olduğunda biri V_out = a₁V_in + a₂V_in² + a₃V_in³, diğeri V_out = b₁V_in + b₂V_in² + b₃V_in³ olan eğrisel elemanlardır (dengeli modülatör: ½x(t) ve −½x(t) girişli iki AM modülatörün çıkışları çıkarılır; her biri doğrusal olmayan eleman + BPF'dir). Bu durumda çıkış sinyalini hesaplayın.

*Bu sayfanın fotoğrafında yalnız sorular okunabilmiştir.*

## Kısa sınav 1 (telafi), 29 Aralık 2014 (süre 30 dak)

**Soru 1 (50 puan).** Bilgi işareti f(t) = cos 2π·2·10³t + ½cos 2π·4·10³t, taşıyıcı 1 MHz'lik kosinüs (cos 2π·10⁶t). Aşağıdaki sinyallerin sıklık görüngelerini çizin: a) çift yan bant (ÇYB) modüleli c(t) = f(t)cos 2π·10⁶t için C(jω); b) tek yan band (üst yan band) modüleli c(t) = f(t)cos 2π·10⁶t ± f̂(t)sin 2π·10⁶t için C(jω).

**Soru 2 (50 puan).** f(t)cos ω₁t biçimindeki bir çift yan bant işaretinin taşıyıcı sıklığı ω₁'den ω₂'ye değiştirilecek (sıklık çevirme). Dengeli modülatörün girişlerine f(t)cos ω₁t ve cos(ω₁ + ω₂)t uygulanıp uygun süzgeçle bunun gerçekleştirilebildiğini gösterin.

## Quiz 2, 6 Ağustos 2014 (süre 1 saat)

**Soru 1.** Sıklık bindirimli imin genel ifadesi f_FM(t) = A_c cos[ω_ct + K∫f(t)dt]; binen im f(t) = A_m cos ω_mt. A_c = 50 V, A_m = 20 V, K = 2356, ω_c = 2π·200·10³ rad/s, ω_m = 2π·15·10³ rad/s için: a) f₁(t) = 50cos(2π·200·10³t + 0,5 sin(2π·15·10³t)) iminin dar bant FM olduğunu gösterin ve bant genişliğini bulun. b) Aşağıdaki öbek gösteriminde f₅(t) imini elde edin, ona ne ad verildiğini nedeniyle yazın; taşıyıcı sıklığını ve bindirim göstergesini belirtin. c) f₅(t)'nin 50 Ω'luk yük direncinde oluşturabileceği ortalama gücü hesaplayın.

*Öbek gösterim:* f₁(t) → sıklık çarpıcı ×64 → f₂(t) → karıştırıcı (f₀(t) = 20cos(2π·10 900·10³t)) → f₃(t) → BGS (geçiş bandı 1885–1915 kHz) → f₄(t) → sıklık çarpıcı ×48 → f₅(t).

**Soru 2.** Öbek gösteriminin girişine uygulanan sıklık bindirimli im f₁(t) = 10cos(2π·200·10³t + 0,5 sin(2π·15·10³t)) V ve aynı öbek gösterimi veriliyor. a) f₅(t) imini elde edin; b) f₅(t) iminin 50 Ω'luk yük direncine aktarabileceği en büyük gücü; c) f₅(t) iminin en büyük sıklık sapması 75 kHz olması durumunda f₁(t) ve f₅(t) imlerinin bant genişliklerini hesaplayın.

*Çözüm.* f₂(t) = 10cos(2π·12 800·10³t + 32 sin(2π·15·10³t)) (×64). Karıştırıcı: f₃(t) = f₂f₀ = (10·20/2)[cos(2π·1900·10³t + 32 sin(…)) + cos(2π·23 700·10³t + 32 sin(…))], yani 100 genlikli iki bileşen. BGS (1885–1915 kHz) yalnız toplam/fark bileşenlerinden 1900 kHz'lik olanı geçirir: f₄(t) = 100cos(2π·1900·10³t + 32 sin(2π·15·10³t)). ×48: **f₅(t) = 100cos(2π·91 200·10³t + 1536 sin(2π·15·10³t))**, taşıyıcı 91,2 MHz, bindirim göstergesi β₅ = 1536 (geniş bant FM). Alıcı/yük eşleşmesi: kaynak direnci 50 Ω, yük 50 Ω olduğunda en büyük güç P = f₅²/(4R_L) = 100²/(4·50) = 50 W. Bant genişlikleri: f₁(t) için β ≈ 0,5 olduğundan (dar bant) B₁ = 2f_m = 2·15 kHz = 30 kHz; f₅(t) için Δf = 75 kHz ⇒ β = Δf/f_m = 75/15 = 5, B₅ = 2(1 + β)f_m = 2·6·15 kHz = 180 kHz.

*Not: Aynı soru çözümlü çalışma kâğıdında A_c = 50 V, A_m = 20 V, K = 2356 değerleriyle de çıkar; β = KA_m/ω_m = 2356·20/(2π·15·10³) = 0,5.*

**Soru 3.** Bir süperheterodin alıcı, taşıyıcı sıklığı ω_c olan bir radyo istasyonunu dinlemek için ayarlanıyor; anten aynı anda taşıyıcı sıklığı ω_c + 2ω_a olan başka bir istasyonun etkisi altında (görüntü sıklığı). Gelen imin ifadesi f(t) = f₁(t)cos(ω_ct) + f₂(t)cos[(ω_c + 2ω_a)t]; f₁(t) ve f₂(t) bilgi imlerinin sıklık görüngeleri (dikdörtgen ve üçgen) ve alıcının radyo sıklığı ile ara sıklık yükselteçlerinin görüngeleri şekilde verilmiş. a) Alıcının ilk dönüşümünü çizin; b) radyo sıklığı yükselteci, karıştırıcı ve ara sıklık yükselteci çıkışlarını sıklık görüngeleriyle gösterin; c) bir radyo yayınının aynı anda duyulmasına neden olan görüntü girişimini ortadan kaldıracak çözümü belirtin.

*Not: Ağustos 2014 quizinin 3. sorusu fotoğrafta bulanık olduğundan soru metni özetlenerek aktarılmıştır; çözümde yalnız görüntü sıklığı ile ilgili bir sayfa vardır (SSB'nin alt/üst yan bandı için yerel salıngacın taşıyıcının altında/üstünde seçilmesi ve izgenin ters dönmesi).*
