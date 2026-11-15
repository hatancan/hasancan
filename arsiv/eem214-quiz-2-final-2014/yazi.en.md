---
baslik: EEM214 Electronics I: 2014 Quiz 2 Questions and Final Exam Answer Key (BJT/MOSFET Amplifiers)
ozet: Quiz 2 questions (BJT small-signal gains, MOSFET biasing, MOSFET amplifier) from the 2013–2014 spring semester of EEM214 Electronics I, and the answer key of the 29 May 2014 final exam: Zener regulator, two-stage MOSFET amplifier with a source-follower stage, MOSFET bias design, cascaded BJT amplifier, and an amplifier model using the systems approach.
---

This post presents two exam documents from the **2013–2014 spring** semester of EEM214 Electronics I: the **Quiz 2** question sheet dated 12 May 2014 and the **answer key of the end-of-semester (final) exam** dated 29 May 2014. The text was transcribed from pages photographed with a phone; the photographs themselves are not published. Because the first page of the answer key was photographed blurry, only the legible part was transcribed. For the theory behind these topics, see the archived posts [Lecture 5 – BJT](/arsiv/eem214-ders-05-bjt/) and [Lecture 6 – FET and MOSFET](/arsiv/eem214-ders-06-fet/).

## Quiz 2 (12.05.2014)

**1. (45 points)** For the BJT in the circuit, β = 80 and V_A = 150 V. Perform the AC analysis (small-signal analysis) of the circuit and find the voltage gain A_v = v_o/v_s and the current gain A_i = i_o/i_s. Circuit: a current source of I_CQ = 0.5 mA from V⁺ = +5 V to the collector, the emitter at V⁻ = −5 V, the base connected to ground through R_B = 10 kΩ and to v_s through a coupling capacitor, and the output taken from the collector through a coupling capacitor to R_L = 0.5 kΩ.

**2. (30 points)** n-channel MOSFET: V_TN = 2 V, k_n′ = 80 µA/V², W/L = 4, λ = 0. V_DD = +5 V, R_D = 10 kΩ, R_S = 2 kΩ, the source returned to −5 V; the gate is biased from a divider formed by R1 (to V_DD) and R2 (to −5 V). It is required that I_D = 0.5 mA and that the bias current through R1–R2 be one tenth of I_D. Find R1 and R2 and the operating region of the transistor.

**3. (25 points)** For the n-channel MOSFET amplifier (+9 V supply, R_S = 1.2 kΩ bypassed with C_S, R_D = 1 kΩ to −9 V, R_G = 100 kΩ, input through C_C1), draw the small-signal equivalent circuit and find the input resistance R_i, the output resistance R_o, and the voltage gain A_vs = v_o/v_i; g_m = 6.04 mS.

## Final Exam Answer Key (29.05.2014)

Point distribution: Question 1: 13, Question 2: 32, Question 3: 25, Question 4: 20, Question 5: 13 (total 100, as far as can be read from the blurry page).

### 1. Zener Voltage Regulator

In a Zener regulator with a series resistor, the currents I₁ (series resistor current), I_L (load current), and I_Z = I₁ − I_L are found; in the second part, the smallest value the load resistance can take so that the power dissipated in the Zener does not exceed P_Zmax = 400 mW is computed using the relations I_Z(max) = P_Zmax / V_Z and I_L(min) = I₁ − I_Z(max). Since the photograph is blurry, the numerical values could not be read.

### 2. Two-Stage MOSFET Amplifier

In the amplifier with transistors M1 (p-channel, source-follower input) and M2 (n-channel, source-follower output) (V⁺ = 5 V, V⁻ = −5 V, R1 = 35 kΩ, R2 = 5 kΩ), the bias currents I₁ and I₂ are such that the DC output is 0 V. K₁ = 0.2 mA/V², K₂ = 0.5 mA/V², V_T1 = −0.8 V, V_T2 = +0.8 V, r_o1 = 485 kΩ, r_o2 = 100 kΩ, λ = 0.01 V⁻¹.

- a) **I₂ = 5 V / 5 kΩ = 1 mA**; V_GS2 = √(1/0.5) + 0.8 = 2.21 V; **I₁ = (2.21 − (−5))/35 kΩ = 0.206 mA**; g_m2 = 2√(K₂I_D2) = **1.414 mA/V**, g_m1 = 2√(K₁I_D1) = **0.406 mA/V**.
- b) Small-signal equivalent circuit: for M1, a g_m1·v_gs1 current source with r_o1 and R1 in parallel; for M2, a g_m2·v_gs2 current source with r_o2 and R2.
- c) V_o = g_m2·v_gs2·(R2 ∥ r_o2), v_gs2 = −(g_m1·v_in)(r_o1 ∥ R1) − V_o ⇒ **A_v = −g_m2(R2 ∥ r_o2)·g_m1(r_o1 ∥ R1) / [1 + g_m2(R2 ∥ r_o2)]**. With R2 ∥ r_o2 = 5 ∥ 100 = 4.76 kΩ and R1 ∥ r_o1 = 35 ∥ 485 = 32.6 kΩ, A_v = −(1.414)(4.76)(0.406)(32.6) / [1 + (1.414)(4.76)] **≅ −11.5**.
- d) **R_o = (1/g_m2) ∥ R2 ∥ r_o2 = 0.707 ∥ 4.76 ≅ 0.616 kΩ**.

### 3. MOSFET Bias Design

The transistor is in saturation; I_DQ = 6 mA, V_GSQ = 2.8 V, V_DSQ = 10 V, V_DD = 18 V, g_m = 2.2 mS, R_L = 1 kΩ, loaded gain A_v = −1, R_in = 100 kΩ. R1, R2, R_S, R_D = ?

- I_DQ = K_n(V_GSQ − V_TN)², g_m = 2√(K_nI_DQ) ⇒ 2.2 = 2√(6K_n) ⇒ **K_n = 0.202 mA/V²**; 6 = 0.202(2.8 − V_TN)² ⇒ **V_TN = −2.65 V**.
- V_DSQ = 18 − I_DQ(R_S + R_D) ⇒ R_S + R_D = (18 − 10)/6 = 1.33 kΩ.
- A_v = −g_m(R_D ∥ R_L)/(1 + g_m·R_S) = −1 ⇒ 2.2R_D² + 0.47R_D − 3.93 = 0 ⇒ **R_D = 1.23 kΩ, R_S = 0.10 kΩ**.
- V_G = V_GS + V_S = 2.8 + 6 × 0.1 = 3.4 V; V_G = (R_in/R1)·V_DD ⇒ **R1 = 100 × 18 / 3.4 ≅ 529 kΩ**; 529·R2/(529 + R2) = 100 ⇒ **R2 ≅ 123 kΩ**.

### 4. Cascaded BJT Amplifier

Q1 (npn, R1 = 100 kΩ, R2 = 50 kΩ, R_C1 = 5 kΩ, R_E1 = 2 kΩ bypassed) and Q2 (pnp, R_E2 = 2 kΩ bypassed, R_C2 = 1.5 kΩ), V± = ±5 V, R_S = 0.5 kΩ, R_L = 5 kΩ; β₁ ≠ β₂, r_e1 ≠ r_e2, g_m1 ≠ g_m2, r_o1 ≠ r_o2 (r_o is to be taken into account).

- a) Small-signal equivalent circuit: R_S, R1 ∥ R2, β₁r_e1; β₁I_b1 current source, R_C1, r_o1, β₂r_e2; β₂I_b2 current source, r_o2, R_C2, R_L.
- b) A_vs = [R_i/(R_i + R_s)] · [−(R_C1 ∥ r_o1 ∥ β₂r_e2)·β₁I_b1 / (β₁r_e1·I_b1)] · [(r_o2 ∥ R_C2 ∥ R_L)·β₂I_b2 / (−I_b2·β₂r_e2)]; with the values, **A_vs = [(33.33k ∥ β₁r_e1) / (0.5k + 33.33k ∥ β₁r_e1)] · [(5k ∥ r_o1 ∥ β₂r_e2)/r_e1] · [(r_o2 ∥ 1.15k)/r_e2]** (100k ∥ 50k = 33.33 kΩ, 1.5k ∥ 5k ≅ 1.15 kΩ).

### 5. Amplifier Model Using the Systems Approach

When V_s = 0.1 V is applied to the amplifier input (through R_s = 5 kΩ), V_i = 80 mV is measured; with R_L = 5 kΩ connected, V_o = 5 V, and when the load is removed, V_o = 8 V. Find the input and output resistances and the unloaded gain.

- 80 mV = 100 mV·R_i/(5k + R_i) ⇒ **R_i = 20 kΩ**.
- Unloaded gain **A_vo = 8 V / 80 mV = 100**; unloaded overall gain A_vs = 8 V / 100 mV = 80.
- Loaded gain 5/0.08 = 62.5 = 100 × 5k/(R_o + 5k) ⇒ **R_o = 3 kΩ**.
- Equivalent circuit: 20 kΩ at the input, and at the output a dependent voltage source 100·v_i in series with 3 kΩ.
