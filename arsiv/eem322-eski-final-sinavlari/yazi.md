---
baslik: EEM322 Denetim Sistemleri: Eski Final Sınavları 1992–2002 (Hacettepe Üniversitesi, ELE 354)
ozet: Hacettepe Üniversitesi ELE 354 Control Theory / Control Systems dersinin 1992, 1994, 2001 ve 2002 final soruları ve 1992 finalinin çözümü: alan kontrollü DC motorlu konum servosu, durum uzayı ve eşlik (companion) biçimi, ikinci derece sistem yanıtı, kök yer eğrisi, Routh, Bode, Nyquist ve Mason kazanç formülü.
---

Bu yazı, EEM322 Denetim Sistemleri dersine çalışırken öğrenciler arasında dolaşan **eski final sınavlarını** bir araya getiriyor. Sınavlar Başkent Üniversitesi'ne değil, **Hacettepe Üniversitesi Elektrik ve Elektronik Mühendisliği Bölümü**'nün **ELE 354 Control Theory I / Control Systems** dersine ait: 22.06.1992, Haziran 1994, 31.05.2001 ve 04.06.2002 tarihli dört final. 1992 ve 1994 sınavlarının altında "A. Uraz" imzası var. 1992 finalinin el yazısı çözümü de dosyalar arasındaydı; aşağıda sorularla birlikte metne aktarıldı ve hesaplar tek tek kontrol edildi.

Sayfalar kâğıt fotokopilerin fotoğrafları olduğu için görseller yayınlanmadı; fotoğraflanmış sayfalardan metne aktarıldı. Şekilli sorularda (devre, blok diyagram, işaret akış grafiği) şeklin anlatımı verildi. Sorular kaynaktaki gibi İngilizce bırakıldı; açıklamalar ve notlar Türkçe.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## 1992 finali (22.06.1992)

**ELE 354 Control Theory I – Final (2 saat).** Her soru 25 puan.

### Sorular

**1.** Consider the positional servo with a field-controlled dc motor as shown in Fig. Q1. The angular position of the output shaft is compared with a reference input angular position using two rotary potentiometers.

*Şekil:* Giriş potansiyometresi (r) ile çıkış potansiyometresi (c) arasındaki fark e, kazancı K_p olan yükseltecin girişine gider. Yükselteç, alan sargısını (R_f, L_f, akım i_f) sürer; armatür akımı I_a sabittir. Motor miline (θ) bağlı n = N₁/N₂ oranlı dişli kutusu, eylemsizliği J_L ve sürtünmesi B_L olan yükü döndürür; yük mili çıkış potansiyometresine bağlıdır.

- (a) Obtain the transfer function between the applied voltage e_f and the displacement θ on the motor shaft of a field-controlled dc motor which drives a load with a moment of inertia J_L and a viscous friction coefficient B_L through a gear ratio of n = N₁/N₂.
- (b) Determine the mathematical relations for each component and draw a detailed block diagram showing every component with its transfer function and the system variables. Obtain the overall transfer function between the angular displacement c of the output shaft and angular displacement r of the input shaft.

**2.** The state equation of a linear time-invariant system is given as

ẋ = [1 2; −3 −4] x + [1; 1] u

- (a) Transform the state equation into the companion canonical form.
- (b) By assuming a zero input, obtain the transition matrix and find the initial states which yield the state vector x = 2e⁻ᵗ [1 −1]ᵀ at time t.

**3.** The forward transfer function of a unity feedback system is given as G(s) = K / (s(s + 3)).

- (a) Determine the damping ratio ζ and undamped natural frequency ωₙ in terms of K. What are the ranges of K for underdamped, critically damped and overdamped responses?
- (b) For K = 9, obtain the values of peak time T_p, settling time T_s for 2% tb and percent overshoot PO. Calculate the unit step response, draw it against time with all the points of interest indicated on the plot.
- (c) For K = 9, what are the error constants and the steady state errors to unit step, ramp and parabolic inputs?

**4.** A negative feedback system has the open loop transfer function K / (s(s + 2)(s² + 2s + 2)).

- (a) Indicating clearly all the steps involved and calculating all the necessary points and K on the branches, plot a detailed root-locus diagram for the given open loop transfer function.
- (b) It is desired that the dominant closed loop poles should have a damping ratio of ζ = 0.707 and an undamped natural frequency of ωₙ = 0.707. Find all the closed loop poles and the value of K which satisfy the desired specification.

### Çözüm 1: Alan kontrollü DC motorlu konum servosu

**(a)** Alan kontrollü motorda tork alan akımıyla orantılıdır (armatür akımı sabit):

- Tork: T = K₁ i_a K_f i_f = K₂ i_f (K₁, K₂, K_f, i_a sabit)
- Alan devresi: e_f = L_f di_f/dt + R_f i_f
- Mekanik denklem: J d²θ/dt² + B dθ/dt = T = K₂ i_f; burada yük motor miline indirgenmiştir: J = n²J_L, B = n²B_L.

Sıfır başlangıç koşullarıyla Laplace dönüşümü:

- (L_f s + R_f) I_f(s) = E_f(s)
- (Js² + Bs) Θ(s) = K₂ I_f(s)

Buradan:

Θ(s)/E_f(s) = K₂ / (s(L_f s + R_f)(Js + B)) = K_m / (s(T_f s + 1)(T_m s + 1))

- K_m = K₂/(R_f B): motor kazanç sabiti
- T_f = L_f/R_f: alan devresinin zaman sabiti
- T_m = J/B: eylemsizlik/sürtünme (mekanik) zaman sabiti

**(b)** Bileşen denklemleri:

- Hata algılayıcı (potansiyometre çifti): E(s) = K₁[R(s) − C(s)]
- Yükselteç: E_f(s) = K_p E(s)
- Dişli kutusu: C(s) = n Θ(s)

Blok diyagram: R(s) → toplama noktası (−C(s)) → K₁ → K_p → K_m/(s(T_f s + 1)(T_m s + 1)) → n → C(s), çıkıştan girişe birim negatif geri besleme. Kapalı çevrim transfer fonksiyonu:

C(s)/R(s) = K₁K_pK_m n / (T_f T_m s³ + (T_f + T_m)s² + s + K₁K_pK_m n)

### Çözüm 2: Eşlik biçimi ve geçiş matrisi

**(a)** Önce kontrol edilebilirlik matrisi kurulur: S = [B AB] = [1 3; 1 −7], |S| = −10 ≠ 0, yani durum denklemi eşlik biçimine dönüştürülebilir.

- S⁻¹ = (1/10)[7 3; 1 −1], son satırı q = [1/10 −1/10]
- Q = [q; qA] = (1/10)[1 −1; 4 6], Q⁻¹ = [6 1; −4 1]
- w = Qx dönüşümüyle ẇ = QAQ⁻¹w + QBu = A₁w + B₁u:

ẇ = [0 1; −2 −3] w + [0; 1] u

Kâğıdın altında yöntemin genel hâli de not edilmiş: S = [B AB A²B …], q = [0 0 … 1]S⁻¹, Q = [q; qA; …; qAⁿ⁻¹], w = Qx.

**(b)** Rezolvent matris:

(sI − A)⁻¹ = [s−1 −2; 3 s+4]⁻¹ = 1/((s+1)(s+2)) · [s+4 2; −3 s−1]

Ters Laplace ile geçiş matrisi:

Φ(t) = [3e⁻ᵗ − 2e⁻²ᵗ, 2e⁻ᵗ − 2e⁻²ᵗ; −3e⁻ᵗ + 3e⁻²ᵗ, −2e⁻ᵗ + 3e⁻²ᵗ]

Sıfır girişte x(t) = Φ(t)x(0) olduğundan x(0) = Φ⁻¹(t)x(t) = Φ(−t)x(t). x(t) = 2e⁻ᵗ[1 −1]ᵀ yerine konunca:

**x(0) = [2 −2]ᵀ**

Kontrol: [1 −1]ᵀ, A'nın λ = −1 özdeğerine ait özvektörüdür; bu yüzden x(0) = [2 −2]ᵀ'den başlayan çözüm tam olarak 2e⁻ᵗ[1 −1]ᵀ olur. Çözümde aynı sonuç eşlik biçimindeki geçiş matrisi Φ_w(t) = L⁻¹[(sI − A₁)⁻¹] ile x(0) = Q Φ_w(−t) Q⁻¹ x(t) yoluyla da elde edilmiş.

### Çözüm 3: İkinci derece sistemin yanıtı

Kapalı çevrim transfer fonksiyonu C(s)/R(s) = K/(s² + 3s + K) = ωₙ²/(s² + 2ζωₙs + ωₙ²) olduğundan:

**(a)** ωₙ = √K, ζ = 3/(2√K). Karakteristik denklem Δ(s) = s² + 3s + K = 0.

| Yanıt | ζ | K |
|---|---|---|
| Az sönümlü | 0 < ζ < 1 | K > 9/4 |
| Kritik sönümlü | ζ = 1 | K = 9/4 |
| Aşırı sönümlü | ζ > 1 | 0 < K < 9/4 |

**(b)** K = 9 için ζ = 0.5, ωₙ = 3 rad/s:

- Tepe zamanı: T_p = π/(ωₙ√(1−ζ²)) = π/2.598 = **1.21 s**
- Yerleşme zamanı (%2): T_s ≈ 4/(ζωₙ) = 4/1.5 = **2.67 s**
- Yüzde aşım: PO = 100·e^(−ζπ/√(1−ζ²)) = 100·e^(−1.814) = **%16.3**
- Birim basamak yanıtı: c(t) = 1 − (e^(−ζωₙt)/√(1−ζ²)) sin(ωₙ√(1−ζ²) t + tan⁻¹(√(1−ζ²)/ζ)) = **1 − 1.155 e^(−1.5t) sin(2.598t + 60°)**

Çözümdeki grafikte yanıt 1.163 tepe değerine T_p = 1.21 s'de ulaşıyor, %2 bandına T_s = 2.67 s'de giriyor; gecikme zamanı T_d ve yükselme zamanı T_r de eksende işaretlenmiş.

*Not: Kaynakta faz açısının işareti okunaksız; ζ = 0.5 için doğru değer tan⁻¹(√3) = +60°'dir.*

**(c)** K = 9 için G(s) = 9/(s(s + 3)) = 3/(s(0.333s + 1)); sistem **tip 1**:

- K_p = G(0) = ∞, K_v = lim s·G(s) = 3, K_a = lim s²·G(s) = 0
- Birim basamak r(t) = 1: e_ss = 0
- Birim rampa r(t) = t: e_ss = 1/K_v = **1/3**
- Parabolik r(t) = t²: e_ss = ∞

### Çözüm 4: Kök yer eğrisi

Açık çevrim G(s)H(s) = K/(s(s + 2)(s² + 2s + 2)); karakteristik denklem 1 + G(s)H(s) = 0.

**Adım 1 – Kutuplar/sıfırlar:** kutuplar 0, −2, −1 ± j (n = 4); sıfır yok (m = 0). Dört dal var, hepsi sonsuza gider.

**Adım 2 – Asimptotlar:** n − m = 4 asimptot; açılar θ_k = (2k + 1)π/4 = 45°, 135°, 225°, 315°; merkez σ_a = (Σp − Σz)/(n − m) = (−2 − 1 + j − 1 − j)/4 = **−1**.

**Adım 3 – jω ekseni kesişimi:** Δ(s) = s⁴ + 4s³ + 6s² + 4s + K = 0 için Routh tablosu:

| Satır | 1. sütun | 2. sütun | 3. sütun |
|---|---|---|---|
| s⁴ | 1 | 6 | K |
| s³ | 4 | 4 | |
| s² | 5 | K | |
| s¹ | 4(5 − K)/5 | | |
| s⁰ | K | | |

*Not: Kaynakta s¹ satırı (5 − K)/5 olarak yazılmış; doğrusu (5·4 − 4K)/5 = 4(5 − K)/5'tir. Satırın işareti, dolayısıyla kararlılık aralığı değişmez.*

Kararlılık aralığı **0 < K < 5**. K = 5'te yardımcı denklem 5s² + 5 = 0 → s = **±j**. Gerçekten K = 5 için Δ(s) = (s² + 1)(s² + 4s + 5).

**Adım 4 – Ayrılma noktası:** K = −(s⁴ + 4s³ + 6s² + 4s), dK/ds = −(4s³ + 12s² + 12s + 4) = −4(s + 1)³ = 0 → s = −1 (üç katlı kök; Horner tablosuyla bulunmuş). Bu noktada K = −(1 − 4 + 6 − 4) = **1**. K = 1 için Δ(s) = (s + 1)⁴: dört kök birden −1'de buluşur, yani −1 çift ayrılma noktasıdır.

**Adım 5 – Ayrılış açıları (−1 ± j kutuplarından):** θ = 180° − 135° − 45° − 90° = **−90°** (diğer kutup için +90°).

Ortaya çıkan eğride −1 ± j kutuplarından çıkan dallar düşey olarak gerçel eksene iner, 0 ve −2'den çıkan dallar −1'e gelir; K = 1'de dört dal −1'de buluşup 45°, 135°, 225° ve 315° doğrultularında asimptotlar boyunca ayrılır. Sağa giden iki dal sanal ekseni K = 5'te ±j'de keser.

**(b)** İstenen baskın kutuplar: ζ = 0.707, ωₙ = 0.707 → s = −ζωₙ ± jωₙ√(1−ζ²) = **−0.5 ± j0.5**.

Açı koşulu kontrolü (θ₁ = tan⁻¹(0.5/1.5) = 18.4°, θ₂ = tan⁻¹(1.5/0.5) = 71.6°):

−(18.4° + 71.6° + 315° + 135°) = −540° = −3 × 180°

yani −0.5 ± j0.5 kök yer eğrisi üzerindedir. Sentetik bölme: Δ(s)/(s² + s + 0.5) = s² + 3s + 2.5, kalan K − 0.5 × 2.5 = 0. Böylece **K = 1.25** ve kalan kapalı çevrim kutupları **−1.5 ± j0.5**.

Kontrol: (s² + s + 0.5)(s² + 3s + 2.5) = s⁴ + 4s³ + 6s² + 4s + 1.25. Ayrıca Δ(s) = (s + 1)⁴ + (K − 1) olduğundan K > 1 için kökler −1 merkezli dört doğru üzerindedir; −0.5 + j0.5 için (K − 1) = |0.5 + j0.5|⁴ = 0.25, yani K = 1.25 doğrulanır.

## 1994 finali (Haziran 1994)

**ELE 354 Control Theory I – Final (2 saat).** Tarih kısmen okunaklı (16/6/1994 gibi).

**1.** An armature-controlled dc motor is used to deliver a torque T to a load with a moment of inertia J and a rotational viscous friction B. The armature winding has an inductance L_a and a resistance R_a. Write down all the mathematical relations (time-domain) and obtain the transfer function between the angular displacement Θ(s) of the load and the applied input voltage E_a(s) to the armature winding. Draw a detailed block diagram.

**2.** Consider the positional servo with an armature-controlled dc motor as shown. The angular position of the output shaft is compared with a reference input angular position using two rotary potentiometers. Obtain the overall transfer function between the angular displacement c of the output shaft and angular displacement r of the input shaft, and draw the final block diagram. Note that you may use the results which you have obtained in Q.1.

*Şekil:* 1992 finalindeki servonun armatür kontrollü sürümü: potansiyometre farkı e, K_p yükseltecinden geçip armatür devresini (R_a, L_a, i_a) sürer; alan akımı i_f sabittir. Motor mili θ, n = N₁/N₂ dişli kutusu üzerinden J_L, B_L yükünü ve çıkış potansiyometresini döndürür.

**3.** Write only the mathematical equations for the given three tank fluid system and draw an analogous electrical system. (*Şekil:* Q_i girişli, yan yana bağlı üç tank; kesit alanları A₁, A₂, A₃, seviyeleri H₁, H₂, H₃, aradaki ve çıkıştaki dirençler R₁, R₂, R₃, çıkış debisi Q₀; H_i = yükseklik, A_i = kesit alanı, ρ = 1 su yoğunluğu.)

**4.** The dynamic equations of a linear time-invariant system is given as ẋ = [−1 2; −1 −4] x + [0; 1] u and y = [1 0] x. Obtain the zero-input response for x(0) = [1 0]ᵀ, the zero-state response for a unit-step input and the total output response y(t).

**5.** Consider a unity feedback system with an OLTF G(s) = K / (s(s³ + 6s² + 9s + 24)). Obtain the position K_p, velocity K_v and acceleration K_a error constants and indicate the type of input which would yield zero steady-state error. The steady-state error for a ramp input is desired to be less than 0.5. Investigate whether this is achievable under stable operation.

**6.** Consider a feedback control system with the feedforward and feedback transfer functions given, respectively, as G(s) = 10/(s + 3) and H(s) = hs. The nominal value of the parameter h is h = 2. Obtain the sensitivity of CLTF T(s) to parameter variations in h. Determine the percent magnitude change in CLTF T(s) for a 10% change in h at a frequency of ω = 5 rad/sec.

**7.** A unity feedback control system has a plant transfer function of the form G(s) = K(s + 1)(s + 2) / (s(s² + 1)(s + 6)). Determine the range of K for stable operation and indicate the critical value of K and jω-axis crossing.

**8.** Consider the system given in Q.7. Indicating clearly all the steps involved and calculating all the necessary points and angles, plot a detailed root-locus diagram. Note that you may use the results which you have obtained in Q.7.

## 2001 finali (31.05.2001)

**ELE 354 Control Systems – Final (2.5 saat).** İki bölümden oluşuyor; B bölümü farklı bir yazı tipiyle basılmış ayrı bir sayfa.

### A bölümü

**A-1.** Water tank level control is achieved by using a float level sensor and valve as shown. Assume that the float has a negligible mass and the valve is controlled so that a reduction in the flow rate is proportional to an increase in head; Q₁ = r − K₁x_a where the reference signal r is r = 0 for this regulating system. The variables Q₁ and H are the deviations from some nominal values. Write all the relevant mathematical equations, draw a detailed block diagram and obtain the CLTF between H and r by utilizing the block diagram.

*Şekil:* Kesit alanı A olan tanka vana üzerinden Q₁ debisi girer; tank R direncinden Q₂ debisiyle boşalır. Yüzen şamandıra, kolları a ve b olan bir manivelanın b ucuna bağlıdır (yer değiştirme x_b); manivelanın a ucu vanayı x_a kadar hareket ettirir. H = seviye, ρ = 1.

**A-2.** Draw the signal flow graph of the given block diagram and obtain the overall transfer function between C(s) and R(s) using the Mason's gain formula.

*Şekil:* R(s) dış toplama noktasından (−H₃ geri beslemesi) geçer; ardından ikinci toplama noktası (−H₁ geri beslemesi) ve paralel G₃ ile G₁ blokları gelir. Bu iki kolun toplamı bir toplama noktasında birleşir; ilk toplama noktasının çıkışından G₄ ileri besleme kolu son toplama noktasına bağlanır. Son toplama noktasından sonra G₂ bloğu ve −H₂ iç geri beslemesi vardır, çıkış C(s).

**A-3.** The dynamic equations of a linear time-invariant system is given as ẋ = [1 1; −6 −4] x + [0; 1] u, y = [1 0] x. Obtain the zero-input state, zero-state state, zero-input output, zero-state output and total output responses for x(0) = [1 0]ᵀ and a unit-step input u = 1, t ≥ 0.

**A-4.** Consider a unity feedback control system with the plant transfer function G(s) = 50000(s + 2) / (s(s + 10)(s² + 50s + 2500)). Using the straight line approximation technique, obtain the Bode plots. [Use 10 dB/cm in magnitude scale, 45°/cm in phase scale]. Indicate clearly on the plots the gain/phase crossover frequencies, the gain/phase margins and read out their approximate values.

### B bölümü

**B-1.** Consider the following polynomial: s⁸ + s⁷ + 12s⁶ + 22s⁵ + 39s⁴ + 59s³ + 48s² + 38s + 20. Determine how many roots of this polynomial are in the right half plane, the left half plane and on the jω axis. Determine the roots on the jω axis, if any.

**B-2.** Design the values of K₁ and K₂ in the following system, to meet the following specifications; steady state error component due to a unit step disturbance is −0.000012 and the steady state error component due to a unit ramp input is 0.003. (*Şekil:* R(s) → toplama (−C) → K₁(s + 2)/(s + 3) → D(s)'nin eklendiği toplama noktası → K₂/(s(s + 4)) → C(s), birim geri besleme.)

**B-3.** Consider the following system. Draw a detailed root locus diagram. Design the value of K for "good performance". (*Şekil:* birim geri beslemeli; ileri yolda K ve (s + 1.5)/(s(s + 1)(s + 10)).)

**B-4.** Consider the following system. Draw a detailed Nyquist diagram. By using Nyquist criterion; find the range of K for stability and instability, the value of K for marginal stability and determine the frequency of oscillations. If K = 6; determine the gain margin, estimate the phase margin. (*Şekil:* birim geri beslemeli; ileri yolda K ve 1/((s² + 2s + 2)(s + 2)).)

## 2002 finali (04.06.2002)

**ELE 354 Control Systems – Final (2.5 saat).**

### A bölümü

**A-1.** A position control system with G(s) in the forward path and a tachometer feedback H(s) given as G(s) = 4/(s(s + 2)), H(s) = (1 + hs). Determine the value of h so that the damping ratio ζ is 0.6. Obtain steady-state responses for r₁(t) = 2 and r₂(t) = 3 sin 2t inputs and show whether asymptotic tracking is achieved for r₁(t).

**A-2.** Consider a feedback control system with the feedforward and feedback transfer functions given, respectively, as G(s) = 10/(s + 3) and H(s) = hs. The nominal value of the parameter h is h = 2. Obtain the sensitivity of CLTF T(s) to parameter variations in h. Determine the percent magnitude change in CLTF T(s) for a 10% change in h at a frequency of ω = 0.1 rad/sec and find whether this frequency is within the bandwidth?

**A-3.** The characteristic equation of a unity feedback control system is given as Δ(s) = s² + (K − 2)s + 2 = 0. Find the range of K for stable operation. Indicating clearly all the steps involved and calculating all the necessary points and angles; plot a detailed root-locus diagram.

**A-4.** Consider a unity feedback control system with the plant transfer function G(s) = 9000s / ((s + 2)(s + 30)(s² + 5s + 25)). Using the straight line approximation technique, obtain the Bode plots. [Use 10 dB/cm in magnitude scale, 45°/cm in phase scale]. Indicate clearly on the plots the gain/phase crossover frequencies, the gain/phase margins and read out their approximate values.

### B bölümü

**1.** Consider the electro-mechanical system given below. Determine the transfer function from the armature voltage (e) to the shaft position (θ). (*Şekil:* e(t) kaynağı R direnci üzerinden motoru besler; motorun zıt EMK'sı e_m = Kθ̇_m. Motor mili J_m eylemsizliğini ve n₁ dişlisini döndürür; n₂ dişlisi J_L yükünü taşıyan mili θ kadar döndürür.)

**2.** Determine the transfer function G(s) such that the effect of the disturbance (d) is eliminated entirely. (*Şekil:* r → toplama noktası (−y geri beslemesi ve +G(s)·d) → (s + 5)/(s + 10) → 10/(s(s + 5)) → d'nin eklendiği toplama noktası → y.)

**3.** Obtain a state-space representation for the following system. Determine observability and controllability status of your representation. (*Şekil:* u → toplama (−y) → (s + z)/(s + p) → 1/s² → y, birim geri besleme.)

**4.** Consider the following system. Draw the Nyquist plot associated with the open-loop transfer function. Determine gain margin and estimate phase margin of the closed loop system provided K = 0.5. (*Şekil:* birim geri beslemeli; ileri yolda K ve 100/(s(s + 2)(s + 10)).)
