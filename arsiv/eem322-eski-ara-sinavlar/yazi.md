---
baslik: EEM322 Denetim Sistemleri: Eski Ara Sınavlar ve Çözümleri 1993–2000 (Hacettepe Üniversitesi, ELE 354)
ozet: Hacettepe Üniversitesi ELE 354 Control Systems dersinin 1993, 1999 ve 2000 ara sınav soruları ve çözümleri: mekanik ve sıvı sistemlerin elektriksel benzerleri, Mason kazanç formülü, durum uzayı modelleri, kaskad ayrıştırma, kontrol edilebilirlik/gözlenebilirlik, geçiş matrisi ve ikinci derece sistem tasarımı.
---

Bu yazı, EEM322 Denetim Sistemleri dersine hazırlanırken öğrenciler arasında dolaşan **eski ara sınavları ve çözümlerini** bir araya getiriyor. Sınavlar **Hacettepe Üniversitesi Elektrik ve Elektronik Mühendisliği Bölümü**'nün **ELE 354 Control Theory I / Control Systems** dersine ait: 13.05.1993, 24.03.1999 ve 13.04.2000 tarihli üç ara sınav. 1993 ve 1999 sınavlarının altında "A. Uraz" imzası var; 2000 sınavının çözüm sayfalarının sonunda "Y. Özkazanç" yazıyor. Her sınavın el yazısı çözümü de dosyalar arasındaydı; aşağıda sorularla birlikte metne aktarıldı ve hesaplar tek tek kontrol edildi.

Sayfalar kâğıt fotokopilerin fotoğrafları olduğu için görseller yayınlanmadı; fotoğraflanmış sayfalardan metne aktarıldı. Şekilli sorularda (mekanik sistem, devre, işaret akış grafiği) şeklin anlatımı verildi. Sorular kaynaktaki gibi İngilizce bırakıldı; açıklamalar ve notlar Türkçe.

*Bu içerik üçüncü taraf bir kaynağa aittir; arşiv ve nostalji amacıyla kaynak belirtilerek paylaşılmıştır. Hak sahibinin talebi hâlinde kaldırılır.*

## 1993 ara sınavı (13.05.1993)

**ELE 354 Control Theory I – Midterm (2 saat).** Her soru 10 puan, toplam 80 puan.

### 1. Mekanik sistem ve elektriksel benzeri

> Write the force equations for the given mechanical system. Find the transfer function between the input f and output x for the considered mechanical system. Obtain the analogous electrical system for velocity-voltage analogy and write the electrical equations.

*Şekil:* Duvara bağlı K yayı, ardından B₂ sönümleyicisi (ara noktanın yer değiştirmesi y), sonra zeminde B₁ sürtünmesiyle kayan M kütlesi; kütleye f kuvveti uygulanıyor, yer değiştirmesi x.

**Çözüm.** Kuvvet denklemleri:

- f = M d²x/dt² + B₁ dx/dt + B₂ d(x − y)/dt
- B₂ d(x − y)/dt = K y

Hız-gerilim (v-v) benzerliğinde: i akım kaynağına paralel C ve R₁, ardından R₂ üzerinden L'ye bağlanan bir devre çıkar (C ≡ M, R₁ ≡ 1/B₁, R₂ ≡ 1/B₂, L ≡ 1/K):

- i = C dv_x/dt + v_x/R₁ + (v_x − v_y)/R₂
- (v_x − v_y)/R₂ = (1/L)∫v_y dt

Transfer fonksiyonu:

X(s)/F(s) = (B₂s + K) / (s[(Ms + B₁)(B₂s + K) + B₂K])

### 2. Mason kazanç formülü

> Obtain the overall gain between the input R(s) and the output C(s) for the given signal flow graph using the Mason's gain formula.

*Grafik:* R(s)'den C(s)'ye ana yol üzerinde G₁, G₂, G₃ dalları; bunlara paralel G₄ ve daha dıştan G₅ dalları; G₂ etrafında −H₂, G₁G₂G₃ zinciri etrafında −H₁ geri besleme dalı.

**Çözüm.**

- İleri yollar: P₁ = G₁G₂G₃, P₂ = G₄, P₃ = G₅
- Çevrimler: L₁ = −G₁G₂G₃H₁, L₂ = −G₂H₂, L₃ = −G₄H₁
- Determinant: Δ = 1 − (L₁ + L₂ + L₃) + L₂L₃
- Kofaktörler: Δ₁ = 1, Δ₂ = 1 − L₂, Δ₃ = Δ

C(s)/R(s) = (P₁Δ₁ + P₂Δ₂ + P₃Δ₃)/Δ = [G₁G₂G₃ + G₄(1 + G₂H₂)] / (1 + G₁G₂G₃H₁ + G₂H₂ + G₄H₁ + G₂H₂G₄H₁) + G₅

### 3. İki tanklı sıvı sistemi

> Write the mathematical equations for the given two tank fluid system and obtain the transfer function between the output flow rate Q₂ and input flow rate Q. Draw an analogous electrical system.

*Şekil:* Q debisiyle beslenen A₁ kesitli üst tank R₁ direncinden Q₁ ile alttaki A₂ kesitli tanka boşalıyor; alt tank R₂ direncinden Q₂ ile boşalıyor (H_i = yükseklik, ρ = 1).

**Çözüm.** P_i = ρH_i ve C_i = A_i/ρ tanımlarıyla:

- Q − Q₁ = C₁ dP₁/dt, P₁/R₁ = Q₁
- Q₁ − Q₂ = C₂ dP₂/dt, P₂/R₂ = Q₂

Q₂(s)/Q(s) = 1 / ((1 + R₁C₁s)(1 + R₂C₂s))

Tanklar birbirini yüklemediği için blok diyagram iki birinci derece bloğun art arda bağlanmasıdır: Q → 1/(1 + R₁C₁s) → Q₁ → 1/(1 + R₂C₂s) → Q₂. Elektriksel benzeri: i akım kaynağı C₁ ∥ R₁ devresini besler; R₁'den geçen i₁ akımı ikinci bir C₂ ∥ R₂ devresine kaynak olur.

### 4. Devre için durum uzayı modeli

> By defining suitable state variables obtain a SSD for the given circuit. You may take the voltage drop across C as the output.

*Devre:* i akım kaynağı ve ona paralel R₁ (düğüm gerilimi v₁); v₁ düğümünden L bobini (akımı i₁) v₂ düğümüne gider; v₂ düğümünde toprağa C kondansatörü, ayrıca R₂ üzerinden v gerilim kaynağı.

**Çözüm.** Dinamik denklemler: i = v₁/R₁ + (1/L)∫(v₁ − v₂)dt ve (1/L)∫(v₁ − v₂)dt = C dv₂/dt + (v₂ − v)/R₂. Durum değişkenleri x₁ = i₁ (bobin akımı), x₂ = v₂ (kondansatör gerilimi) seçilince v₁ = R₁i − R₁x₁ olur ve:

- ẋ₁ = (1/L)(v₁ − v₂) = (1/L)(R₁i − R₁x₁ − x₂)
- ẋ₂ = (1/C)x₁ − x₂/(R₂C) + v/(R₂C)

ẋ = [−R₁/L −1/L; 1/C −1/(R₂C)] x + [R₁/L 0; 0 1/(R₂C)] [i; v], y = [0 1] x

### 5. Kaskad ayrıştırma

> Consider a system described by the transfer function G(s) = 3(s + 5)/(s(s + 1)(s + 2)). Obtain a SSD for G(s) using the cascade decomposition scheme.

**Çözüm.** G(s) = 3 · (1/s) · (1/(s + 1)) · ((s + 5)/(s + 2)) çarpanlarına ayrılıp her biri art arda bağlanır:

- ẋ₃ = 3u
- ẋ₂ = x₃ − x₂
- ẋ₁ = x₂ − 2x₁, y = ẋ₁ + 5x₁ = 3x₁ + x₂

ẋ = [−2 1 0; 0 −1 1; 0 0 0] x + [0; 0; 3] u, y = [3 1 0] x

### 6. Sıfır girişli, sıfır durumlu ve toplam yanıt

> The dynamic equations of a linear time-invariant system is given as ẋ = [1 2; −3 −4] x + [2; −3] u, y = [1 0] x. Obtain the zero-input response for x(0) = [1 −1]ᵀ, the zero-state response for a unit-step input and the total output response y(t).

**Çözüm.** Rezolvent matris: (sI − A)⁻¹ = (1/Δ(s)) [s+4 2; −3 s−1], Δ(s) = (s + 1)(s + 2). Laplace bölgesinde X(s) = (sI − A)⁻¹x(0) + (sI − A)⁻¹BU(s).

- Sıfır girişli yanıt: X(s) = (1/Δ)[s + 2; −(s + 2)] → **x(t) = [e⁻ᵗ; −e⁻ᵗ]**
- Sıfır durumlu yanıt (U = 1/s): X(s) = (1/(s(s + 2)))[2; −3] → **x(t) = [1 − e⁻²ᵗ; −3/2 + (3/2)e⁻²ᵗ]**
- Toplam çıkış: **y(t) = 1 + e⁻ᵗ − e⁻²ᵗ**

### 7–8. İkinci derece sistem ve hata sabitleri

> **7.** Consider a unity feedback system with the feedforward transfer function G(s) = 25/(s(s + 5)). Determine the undamped natural frequency, damping ratio, rise time, percent overshoot (PO), peak time and settling time for 2% t.b. for the unit step cl response.
>
> **8.** For the feedback system given in Q7, find the error constants and the steady-state error e_ss for unit step, unit ramp and parabolic inputs. What is the system type?

**Çözüm 7.** T(s) = 25/(s² + 5s + 25) → ωₙ = 5 rad/s, ζ = 0.5.

- Yükselme zamanı: T_r = (π − θ)/(ωₙ√(1 − ζ²)) = **0.48 s** (θ = cos⁻¹ζ = π/3)
- Tepe zamanı: T_p = π/(ωₙ√(1 − ζ²)) = **0.73 s**
- Yerleşme zamanı (%2): T_s ≈ 4/(ζωₙ) = **1.6 s**
- Yüzde aşım: PO = 100·e^(−π/√3) = **%16.3**

**Çözüm 8.** K_p = G(0) = ∞, K_v = lim s·G(s) = 5, K_a = lim s²·G(s) = 0. Birim basamakta e_ss = 0, birim rampada e_ss = 1/K_v = **0.2**, parabolik girişte e_ss = ∞. Sistem **tip 1**.

## 1999 ara sınavı (24.03.1999)

**ELE 354 Control Systems – Midterm-I (2.5 saat).** Her soru 10 puan.

### 1. İki kütleli mekanik sistem

> Write the force equations for the given mechanical system. Obtain the analogous electrical systems for velocity-voltage (v-v) and force-voltage (f-v) analogies.

*Şekil:* f kuvvetiyle çekilen M₁ kütlesi (x) duvara B₂ sönümleyicisiyle bağlı; M₁, B₁ sönümleyicisiyle M₂ kütlesine (y), M₂ de K yayıyla duvara bağlı.

**Çözüm.** Hızlarla (v_x, v_y) yazılan dinamik denklemler:

- f = M₁ dv_x/dt + B₂v_x + B₁(v_x − v_y)
- B₁(v_x − v_y) = M₂ dv_y/dt + K∫v_y dt

Hız-gerilim (v-v) benzerliğinde: C ≡ M, R ≡ 1/B, L ≡ 1/K; akım kaynağı i ≡ f, düğüm gerilimleri v_x ve v_y. Kuvvet-gerilim (f-v) benzerliğinde: L ≡ M, R ≡ B, C ≡ 1/K; gerilim kaynağı v ≡ f, iki çevre akımı i_x ve i_y.

### 2. Manivela sistemi

> Consider the lever system with the applied force f and the displacement x zero at the reference position as shown. Write the mathematical relations that describe the dynamics of the system and obtain the transfer function between the input f and output x. Draw v-v and f-v electrical analogue circuits.

*Şekil:* Kolları a ve b olan manivelanın a ucuna f uygulanıyor; b ucu yukarıdan K yayıyla, aşağıdan B sönümleyicisiyle sabit noktalara bağlı (yer değiştirme x).

**Çözüm.** Dayanak noktasına göre moment dengesi f·a = f₁·b (f₁: b ucuna iletilen kuvvet) ve f₁ = Kx + B dx/dt. Buradan:

X(s)/F(s) = (a/b)/(Bs + K)

Blok diyagram: F(s) → a/b → F₁(s) → 1/(Bs + K) → X(s). Elektriksel benzerlerde manivela, sarım oranı kol oranından gelen ideal bir transformatörle gösterilmiş.

### 3. Üç tanklı sıvı sistemi

> Write only the mathematical equations for the given three tank fluid system and draw an analogous electrical system.

*Şekil:* Yan yana üç tank; Q_i debisi ortadaki (2.) tanka giriyor; 1. tank R₁, 3. tank R₂ üzerinden 2. tanka bağlı; 3. tank R₃'ten Q₀ ile boşalıyor.

**Çözüm.**

- Q_i = (P₂ − P₁)/R₁ + (P₂ − P₃)/R₂ + C₂ dP₂/dt
- (P₂ − P₁)/R₁ = C₁ dP₁/dt
- (P₂ − P₃)/R₂ = C₃ dP₃/dt + P₃/R₃
- Q₀ = P₃/R₃

Elektriksel benzeri: akım kaynağı v₂ düğümünü besler; bu düğümde C₂ ve R₁ üzerinden C₁ var; R₂ üzerinden v₃ düğümüne geçilir, orada C₃ ve R₃ toprağa bağlıdır.

### 4. Mason kazanç formülü

> Obtain the overall gain between the input R(s) and the output C(s) for the given signal flow graph using the Mason's gain formula.

*Grafik:* İç içe üç yol: en içte G₁, onu saran G₂ ve en dışta G₃ ileri dalları; bunlara karşılık −H₁, −H₂, −H₃ geri besleme dalları.

**Çözüm.**

- İleri yollar: P₁ = G₁, P₂ = G₂, P₃ = G₃
- Çevrimler: L₁ = −G₁H₁, L₂ = −G₂H₂, L₃ = −G₃H₃, L₄ = −G₁H₂, L₅ = −G₁H₃, L₆ = −G₂H₃
- Birbirine değmeyen çevrimler: (L₁, L₂), (L₁, L₃), (L₂, L₃), (L₁, L₆), (L₃, L₄) ve (L₁, L₂, L₃)
- Δ = 1 − (L₁ + … + L₆) + L₁L₂ + L₁L₃ + L₂L₃ + L₁L₆ + L₃L₄ − L₁L₂L₃
- Kofaktörler: Δ₁ = 1, Δ₂ = 1 − L₁, Δ₃ = 1 − L₁ − L₂ − L₄ + L₁L₂

C(s)/R(s) = (P₁Δ₁ + P₂Δ₂ + P₃Δ₃)/Δ

Pay: G₁ + G₂ + G₂G₁H₁ + G₃ + G₃G₁H₁ + G₃G₂H₂ + G₃G₁H₂ + G₃G₁H₁G₂H₂

Payda: 1 + G₁H₁ + G₂H₂ + G₃H₃ + G₁H₂ + G₁H₃ + G₂H₃ + G₁H₁G₂H₂ + G₁H₁G₃H₃ + G₂H₂G₃H₃ + G₁H₁G₂H₃ + G₃H₃G₁H₂ + G₁H₁G₂H₂G₃H₃

### 5. Kontrol edilebilirlik ve gözlenebilirlik

> The dynamic equations of a linear time-invariant system is given as ẋ = [−4 3; −2 1] x + [1; 0] u, y = [1 −1] x. Determine whether the system is controllable and/or observable? Obtain the transfer function and comment on your findings in relation to c/o.

**Çözüm.**

- U = [B AB] = [1 −4; 0 −2], |U| ≠ 0 → (A, B) **kontrol edilebilir**
- V = [C; CA] = [1 −1; −2 2], |V| = 0 → (A, C) **gözlenemez**
- G(s) = C(sI − A)⁻¹B = [1 −1] · (1/((s + 1)(s + 2))) · [s−1 3; −2 s+4] · [1; 0] = (s + 1)/((s + 1)(s + 2)) = **1/(s + 2)**

Sistem gözlenemez olduğu için, beklendiği gibi transfer fonksiyonunda kutup-sıfır sadeleşmesi olur.

### 6. Eşlik biçimi ve geçiş matrisi

> If possible transform the dynamic equations given in Q.5 into the companion canonical form. Obtain the state transition matrix for the transformed matrix A.

**Çözüm.** (A, B) kontrol edilebilir olduğundan dönüşüm mümkündür.

- U⁻¹ = (1/−2)[−2 4; 0 1] = [1 −2; 0 −1/2], q = [0 1]U⁻¹ = [0 −1/2]
- Q = [q; qA] = [0 −1/2; 1 −1/2], Q⁻¹ = [−1 1; −2 0]
- w = Qx ile ẇ = QAQ⁻¹w + QBu = [0 1; −2 −3] w + [0; 1] u, y = CQ⁻¹w = [1 1] w

Geçiş matrisi:

e^(A_c t) = L⁻¹[(sI − A_c)⁻¹] = L⁻¹{(1/((s + 1)(s + 2))) [s+3 1; −2 s]} = [2e⁻ᵗ − e⁻²ᵗ, e⁻ᵗ − e⁻²ᵗ; −2e⁻ᵗ + 2e⁻²ᵗ, −e⁻ᵗ + 2e⁻²ᵗ]

### 7. Kaskad ayrıştırma

> Consider a system described by the transfer function G(s) = (2s + 6)/(s³ + 6s² + 8s). Obtain a SSD for G(s) using the cascade decomposition scheme.

**Çözüm.** G(s) = 2(s + 3)/(s(s + 2)(s + 4)) = (2/s) · (1/(s + 2)) · ((s + 3)/(s + 4)):

- ẋ₃ = 2u, ẋ₂ = x₃ − 2x₂, ẋ₁ = x₂ − 4x₁
- y = ẋ₁ + 3x₁ = −x₁ + x₂

ẋ = [−4 1 0; 0 −2 1; 0 0 0] x + [0; 0; 2] u, y = [−1 1 0] x

### 8. Geri besleme parametrelerinin tasarımı

> Consider a closed loop system with a feedforward transfer function G(s) = 10/s² and a feedback transfer function H(s) = (as + b). For a unit step input, find the values of a and b that give 16% percent overshoot (PO) and 0.4 sec. settling time (2% t.b.).

**Çözüm.** T(s) = G/(1 + GH) = 10/(s² + 10as + 10b).

- T_s = 4/(ζωₙ) = 0.4 s → ζωₙ = 10 → 2ζωₙ = 10a = 20 → **a = 2**
- PO = %16: ln 0.16 = −ζπ/√(1 − ζ²) = −1.83 → ζ²/(1 − ζ²) = (0.583)² = 0.34 → ζ ≈ 0.5 → ωₙ = 20 rad/s
- ωₙ² = 10b = 400 → **b = 40**

## 2000 ara sınavı (13.04.2000)

**Hacettepe University, ELE 354 Control Systems – 1. Midterm Exam, April 13, 2000.**

### 1. Mekanik sistemin diferansiyel denklemleri

> Obtain the differential equations describing the following system. Draw an analogous electrical circuit based on force-current analogy.

*Şekil:* Sol duvara K₁ yayıyla bağlı m₁ kütlesi (x₁, sağa), K₂ yayıyla m₂ kütlesine (x₂, sola) bağlı; m₂ de b sönümleyicisiyle sağ duvara bağlı; F kuvveti m₁'e uygulanıyor.

**Çözüm.**

- m₁ẍ₁ = −F − K₁x₁ − K₂(x₂ + x₁)
- −m₂ẍ₂ = K₂(x₁ + x₂) + bẋ₂

Kuvvet-akım benzerliğinde i = F akım kaynağı; L₁ = 1/K₁, C₁ = m₁ (gerilim v₁ = ẋ₁), L₂ = 1/K₂, C₂ = m₂ ve R = 1/b (gerilim v₂ = −ẋ₂).

### 2. Su seviyesi kontrolü

> The water level, h(t), is controlled by an open loop control system. A dc motor controlled by armature current i turns a shaft, opening a valve. The inductance of the dc motor is neglected. The height of the water in the tank is given by h(t) = ∫(1.6θ(t) − h(t))dt. The motor constant is K_m = 10, and the inertia of the motor shaft and valve is J = 6 × 10⁻³ kg·m². Determine the transfer function from the motor voltage, v(t), to the water level, h(t).

*Şekil:* v(t), kazancı K_a = 50 olan yükseltece girer; yükselteç 10 Ω üzerinden motoru i akımıyla sürer; motor mili vanayı θ(t) kadar açar (vana açıklığı = mil konumu) ve tankın seviyesi h(t) değişir.

**Çözüm.**

- h(t) = ∫(1.6θ − h)dt → H(s) = 1.6Θ(s)/(s + 1)
- ω = θ̇ → Ω(s) = sΘ(s), dolayısıyla H(s) = 1.6Ω(s)/(s(s + 1))
- J dω/dt = K_m i → 6 × 10⁻³ sΩ(s) = 10 I(s)
- 50v = Ri + Kω = 10i + 10ω → 50V(s) = (6 × 10⁻³ s + 10)Ω(s)

H(s)/V(s) = 80 / (s(s + 1)(6 × 10⁻³ s + 10))

### 3. Mason kazanç formülü

> Determine the transfer function from R to C by using Mason's Gain Formula.

*Grafik:* R → 1 → K → G₁ → G₂ → G₃ → 1 → C; G₂ çevresinde −H₂, G₁G₂ çevresinde −H₃, G₂G₃ çevresinde −H₄, G₁G₂G₃ çevresinde −H₁ dalları ve çıkıştan K'nın girişine −1 dalı.

**Çözüm.** L₁ = −G₂H₂, L₂ = −H₁G₁G₂G₃, L₃ = −KG₁G₂G₃, L₄ = −G₁G₂H₃, L₅ = −H₄G₂G₃; tek ileri yol P₁ = KG₁G₂G₃. Bütün çevrimler birbirine değer, Δ₁ = 1:

T = KG₁G₂G₃ / (1 + G₂H₂ + H₁G₁G₂G₃ + KG₁G₂G₃ + G₁G₂H₃ + H₄G₂G₃)

### 4. Köprülü T süzgeci

> Determine the transfer function for the following filter.

*Devre:* Giriş ve çıkış arasında seri iki C kondansatörü, aralarındaki düğümden toprağa R₁; iki kondansatörün üzerinden köprüleyen R₂.

**Çözüm.** Çevre akımları yöntemiyle:

H(s) = (1 + 2R₁Cs + R₁R₂C²s²) / (1 + (2R₁ + R₂)Cs + R₁R₂C²s²)

### 5. Durum değişkeni olarak v ve i

> Develop a state space model for the following system by taking v and i as your state variables. Determine the eigenvalues and eigenvectors of your model.

*Devre:* 1 F'lık kondansatör (v_C1), 1 Ω direnç üzerinden (gerilimi v) 0.5 Ω direnç (akımı i) ile 2 F'lık kondansatörün (v_C2) paralel bağlandığı düğüme bağlı.

**Çözüm.** Önce kondansatör gerilimleriyle: C₁ dv_C1/dt = (v_C2 − v_C1)/1 ve C₂ dv_C2/dt = (v_C1 − v_C2)/1 − v_C2/0.5:

ẋ = [−1 1; 0.5 −1.5] x

v = v_C1 − v_C2 ve i = 2v_C2 olduğundan z = [v; i] = Mx, M = [1 −1; 0 2]; ż = MAM⁻¹z:

d/dt [v; i] = [−1.5 0.5; 1 −1] [v; i]

- Özdeğerler: det(sI − MAM⁻¹) = s² + 2.5s + 1 = 0 → **s₁ = −0.5, s₂ = −2**
- Özvektörler: **z₁ = [−1; −2]**, **z₂ = [−1; 1]**

### 6. Geçiş matrisi ve dürtü yanıtı

> Determine the state transition matrix of the following system. If the input, r(t), is a unit impulse and x₁(0) = 1, x₂(0) = 1; determine x₁(t) for t > 0. ẋ = [−2 −1; 2 −5] x + [0; 1] r(t).

**Çözüm.**

e^(At) = L⁻¹[(sI − A)⁻¹] = [2e⁻³ᵗ − e⁻⁴ᵗ, e⁻⁴ᵗ − e⁻³ᵗ; 2e⁻³ᵗ − 2e⁻⁴ᵗ, 2e⁻⁴ᵗ − e⁻³ᵗ]

x(t) = e^(At)x₀ + ∫₀ᵗ e^(A(t−τ))Br(τ)dτ, x₀ = [1; 1], r(t) = δ(t). Kaynakta sonuç x₁(t) = 2e⁻³ᵗ − e⁻⁴ᵗ olarak verilmiş.

*Not: Bu sonuç hatalı; yalnızca geçiş matrisinin (1,1) elemanıdır. Dürtü girişiyle X(s) = (sI − A)⁻¹(x₀ + B) = (sI − A)⁻¹[1; 2] olur ve X₁(s) = ((s + 5) − 2)/((s + 3)(s + 4)) = 1/(s + 4) çıkar. Doğrusu **x₁(t) = e⁻⁴ᵗ**'dir: sıfır girişli kısım e⁻³ᵗ, dürtü yanıtı e⁻⁴ᵗ − e⁻³ᵗ verir.*

### 7. Blok diyagramdan eşlik biçimi

> Develop a state space model for the following system. Put your state space model in companion form.

*Blok diyagram:* u → toplama (−y) → s → toplama (iç geri besleme) → 1/(2s + 20) → 1/(s + 5) → 1/s → y; iç döngü 1/(s + 5) çıkışından geri beslenir.

**Çözüm.** İç döngü 1/((2s + 20)(s + 5) + 1) = 1/(2s² + 30s + 101) olur; s ve 1/s birbirini götürür:

H(s) = Y(s)/U(s) = 0.5/(s² + 15s + 51)

Eşlik biçimi: ẋ = [0 1; −51 −15] x + [0; 1] u, y = [0.5 0] x

### 8. Kontrol edilemeyen devre

> Develop a state space model for the following circuit. Determine the capacitance, C, such that your model is not controllable.

*Devre:* v(t) gerilim kaynağına paralel iki kol: 2 Ω ile seri 0.5 F (v_C1) ve C ile seri 8 Ω (v_C2).

**Çözüm.**

- 0.5 dv_C1/dt = (v − v_C1)/2 → v̇_C1 = −v_C1 + v
- C dv_C2/dt = (v − v_C2)/8 → v̇_C2 = −v_C2/(8C) + v/(8C)

A = [−1 0; 0 −1/(8C)], B = [1; 1/(8C)]. Kontrol edilebilirlik matrisi [B AB] = [1 −1; 1/(8C) −1/(64C²)]; determinantı −1/(64C²) + 1/(8C) sıfır olduğunda matris tekil olur:

**C = 1/8 F** → model kontrol edilemez. (Bu değerde iki kolun zaman sabiti eşitlenir: 2 Ω × 0.5 F = 8 Ω × 1/8 F = 1 s.)
