---
baslik: EEM311 Electronics II: January 2016 Final Exam and Other Exam Questions, with Solutions
ozet: The January 4, 2016 final exam of EEM311 Electronics II (op-amp bridge load driver, transconductance feedback amplifier, BJT frequency response, differential amplifier, ECG filter), plus questions from undated exams on a phase detector filter, waveform generator, common-gate amplifier and MOSFET frequency response, with solutions.
---

This post presents the **final exam of the 2015-2016 fall semester** (04.01.2016) of the Başkent University Electrical-Electronics Engineering course **EEM 311 Electronics II**, along with other exam questions from the same photo group whose exam is not stated on the paper. The source is photographs of exam papers shared and organized topic by topic by friends (photocopied answer keys, student solutions, and graded papers). Personal information has been removed. The questions and the main steps of the solutions were transcribed from the photographed pages into text; the photographs themselves are not published.

## January 4, 2016 final exam

The score table and date (04.01.2016) at the top of the paper appear only on the page of Question 1. The exam lasted 150 minutes:

| Question | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|
| Points | 20 | 25 | 20 | 20 | 15 | 100 |

Questions 2–5 below were attributed to this exam because their question numbers and points match this table exactly and because they appear in the photographs of the same stack of papers; their pages carry no date.

### Question 1: Bridge load driver with two op-amps (20 pts)

In the circuit below:

- a) Derive the expression for the voltage gain (A_v = V_L / V_I). (10 pts)
- b) Taking R₁ = 50 kΩ, design the circuit so that |V_O1| = |V_O2| and A_v = 10 (determine the unknown resistor values). (5 pts)
- c) If R_L = 20 Ω and the power dissipated in this load resistor is 10 W, find the peak value of the voltages |V_O1| = |V_O2| and the peak value of the current through the load. (5 pts)

*Circuit:* v_I is applied to the non-inverting input of the first op-amp; its output is v_O1. From v_O1, R₂ is connected to the inverting input of the first op-amp; from this node, R₁ goes to the inverting input of the second op-amp (virtual ground). The non-inverting input of the second op-amp is grounded, it has R₃ in its feedback, and its output is v_O2. The load R_L is connected between the two outputs, v_L = v_O1 − v_O2.

**Solution (answer key):**

**a)** The current through R₁ is i = v_I / R₁ (the inverting input of the second op-amp is a virtual ground).

v_O1 = i R₂ + v_I = v_I (1 + R₂/R₁)

v_O2 = −i R₃ = −v_I (R₃/R₁)

v_L = v_O1 − v_O2 = v_I (1 + R₂/R₁) + v_I (R₃/R₁) ⇒ **A_v = v_L / v_I = 1 + R₂/R₁ + R₃/R₁**

**b)** A_v = 10 ⇒ R₂/R₁ + R₃/R₁ = 9. For |v_O1| = |v_O2|, 1 + R₂/R₁ = R₃/R₁. From these two, R₂/R₁ = 4 and R₃/R₁ = 5. With R₁ = 50 kΩ ⇒ **R₂ = 200 kΩ, R₃ = 250 kΩ**.

**c)** P̄ = ½ V_P² / R_L ⇒ V_P = √(2 R_L P̄) = √(2 · 20 · 10) = 20 V

|v_O1| = |v_O2| = **10 V** (peak); the peak value of the load current = 20 V / 20 Ω = **1 A**.

### Question 2: Transconductance feedback amplifier (25 pts)

The ac equivalent of a feedback amplifier, without transistor modeling, is given below. The collector currents obtained from the DC analysis of the circuit are I_C1 = 0.5 mA, I_C2 = 1 mA, and I_C3 = 2 mA. Given β = 120, V_T = 26 mV, and r_o = ∞ for all transistors, find the transconductance transfer function of the circuit: A_gf = I_o / V_s. (25 pts)

*Circuit:* Three cascaded BJTs. V_s is applied to the base of Q₁; R_C1 = 5 kΩ, with R_E1 = 0.1 kΩ in its emitter. The base of Q₂ is connected to the collector of Q₁, its emitter is grounded, R_C2 = 2 kΩ. The base of Q₃ is connected to the collector of Q₂, R_C3 = 1 kΩ (I_o is the output current flowing through this resistor), with R_E3 = 0.1 kΩ in its emitter. The feedback resistor R_F = 0.8 kΩ is between the emitters of Q₁ and Q₃ (series-series feedback).

**Solution (answer key, printed English solution):**

Small-signal parameters: g_m = I_C / V_T and r_π = β / g_m

- g_m1 = 19.23 mA/V, g_m2 = 38.46 mA/V, g_m3 = 76.92 mA/V
- r_π1 = 6.24 kΩ, r_π2 = 3.12 kΩ, r_π3 = 1.56 kΩ

Node equations (V_e1 and V_e3 are the voltages of the two emitter nodes):

1. V_s = V_π1 + V_e1
1. V_π1 / r_π1 + g_m1 V_π1 = V_e1 / R_E1 + (V_e1 − V_e3) / R_F
1. V_π2 = −g_m1 V_π1 (R_C1 ‖ r_π2)
1. g_m2 V_π2 + (V_π3 + V_e3) / R_C2 + V_π3 / r_π3 = 0
1. V_π3 / r_π3 + g_m3 V_π3 = V_e3 / R_E3 + (V_e3 − V_e1) / R_F

When the numerical values are substituted and V_π1, V_π2 and the V_e's are eliminated, one obtains −V_s(517.5) + V_π3(405.95) = 0. The output current is I_o = g_m3 V_π3 = 76.92 V_π3, i.e., V_π3 = I_o(0.0130):

−V_s(517.5) + I_o(0.0130)(405.95) = 0 ⇒ **A_gf = I_o / V_s ≅ 98.05 mA/V**

The same circuit is also covered as an example question in the 2016 summer school notes.

### Question 3: Frequency response of a BJT amplifier (20 pts)

In the amplifier circuit below, which uses a transistor with parameters β = 120, r_o = ∞, g_m = 29.2 mA/V, r_π = 4.12 kΩ, and C = 165 pF (the symbol of the capacitor cannot be made out in the photograph), the values of the capacitors C_C2 and C_E are very large (assume infinite). Find:

- a) The lower and upper cutoff frequencies of the circuit. (10 pts)
- b) The midband gain (A_v = V_o / V_s), and sketch the overall frequency response. (10 pts)

*Circuit:* Common-emitter amplifier with a +10 V supply. The source is connected to the base through R_S = 0.5 kΩ and C_C1 = 4.7 µF; base bias R₁ = 40 kΩ and R₂ = 5 kΩ. R_C = 5 kΩ; in the emitter R_E = 0.5 kΩ, bypassed by C_E. The output goes through C_C2 to R_L = 2.5 kΩ.

**Solution (answer key, printed English solution):**

**a)** For the upper cutoff frequency:

τ_H = R_eq (C_π + C_M), R_eq = r_π ‖ R₁ ‖ R₂ ‖ R_S = 4.12 ‖ 40 ‖ 5 ‖ 0.5 ⇒ R_eq = 0.405 kΩ

τ_H = (0.405 × 10³)(15.6 + 149) × 10⁻¹² = 6.67 × 10⁻⁸ s ⇒ **f_H = 1 / (2π τ_H) = 2.39 MHz**

For the lower cutoff frequency:

τ_L = R_eq C_C1, R_eq = R_S + R₁ ‖ R₂ ‖ r_π = 0.5 + 40 ‖ 5 ‖ 4.12 ⇒ R_eq = 2.64 kΩ

τ_L = (2.64 × 10³)(4.7 × 10⁻⁶) = 1.24 × 10⁻² s ⇒ **f_L = 12.8 Hz**

**b)** V_o = −g_m V_π (R_C ‖ R_L)

V_π = [ (R₁ ‖ R₂ ‖ r_π) / (R₁ ‖ R₂ ‖ r_π + R_S) ] V_s = [ 2.14 / (2.14 + 0.5) ] V_s = 0.8106 V_s

|A_v| = (29.2)(0.8106)(5 ‖ 2.5) ⇒ **|A_v| = 39.4**

Frequency response: between f_L = 12.8 Hz and f_H = 2.39 MHz, |A_v| ≅ 39.4 is flat; a trapezoid-shaped curve falling off at both ends.

*Note: The 149 pF in the solution is the Miller capacitance: C_M = C_μ (1 + g_m R_L′); for R_L′ = R_C ‖ R_L = 1.67 kΩ, 1 + g_m R_L′ ≅ 49.7, so this corresponds to C_μ ≅ 3 pF.*

### Question 4: Differential amplifier with emitter resistors (20 pts)

The transistors in the circuit below are identical, with β = 100, r_o = ∞, and |V_BE| = 0.7 V.

- a) For v₁ = v₂ = 0, find I_E, I_C1, I_C2, V_CE1, and V_CE2. (7 pts)
- b) When the circuit is operated in differential mode so as to amplify the difference of the two inputs, i.e., when a differential ac input signal v_d = v₁ − v₂ is applied, draw the ac equivalent circuit and derive the expression for the differential-mode gain (A_d = v_o2 / v_d) for the output taken from the collector of transistor Q₂, and calculate it. (13 pts)

*Circuit:* Differential amplifier with ±5 V supplies. Collector resistors R_C = 100 kΩ; one 2 kΩ resistor in each of the two emitters, and from the common node R_E = 85 kΩ to −5 V.

**Solution (answer key):**

**a)** 0 = 0.7 + (I_E/2)(2) + I_E(85) − 5 ⇒ I_E = (5 − 0.7) / (85 + 1) ⇒ **I_E = 0.050 mA**

I_C1 = I_C2 = (β / (1+β)) (I_E / 2) = (100/101)(0.050/2) ⇒ **I_C1 = I_C2 = 0.0248 mA**

V_CE1 = V_CE2 = 5 − I_C1(100) − (−0.7) ⇒ **V_CE1 = V_CE2 = 3.22 V**

**b)** In differential mode the common emitter node behaves as an ac ground; for the half circuit:

−v_d/2 = V_π + (V_π / r_π + g_m V_π) R_E = V_π [1 + (1+β) R_E / r_π] (here R_E = 2 kΩ is the emitter resistor)

V_π = −(v_d/2) / [1 + (1+β) R_E / r_π]

v_o = −g_m V_π R_C ⇒ A_d = ½ · β R_C / [r_π + (1+β) R_E]

r_π = β V_T / I_CQ = (100)(0.026) / 0.0248 = 105 kΩ

A_d = ½ · (100)(100) / [105 + (101)(2)] ⇒ **A_d ≅ 16.3**

### Question 5: Filter design for an ECG signal (15 pts)

In an ECG measurement system, the components of the ECG signals at the output of the instrumentation amplifier in the 1 Hz – 150 Hz range are to be obtained with a second-order wideband filter circuit, while the components of the 50 Hz mains frequency are also to be suppressed in the 48 Hz – 52 Hz range with a first-order filter. Draw the required circuits and design them by finding the necessary component values. (15 pts)

**A graded student solution:**

- Band-pass filter (BPF): cascade connection of a second-order Butterworth low-pass filter (LPF, f_LPF = 150 Hz, R₁ = R₂ = 1 / (2π√2 · 150 Hz · C)) with a second-order high-pass filter (HPF, f_HPF = 1 Hz, R = 1 / (2π√2 · 1 Hz · C)); the value of C is to be chosen.
- Band-stop (notch) filter: the outputs of a first-order LPF (R_a, C_a) and a first-order HPF (C_b, R_b) are summed in an inverting summer (equal R's); the solution takes f_LPF = 52 Hz (R_a = 1 / (2π · 52 Hz · C_a)) and f_HPF = 48 Hz (R_b = 1 / (2π · 48 Hz · C_b)).
- Scores are marked in red on the paper; 2 points were deducted because the connection of the two filters to each other was found to be missing.

*Note: When building a band-stop filter by summing a parallel LPF + HPF, the cutoff frequency of the LPF must be below the band (48 Hz) and that of the HPF above it (52 Hz). If the LPF is chosen as 52 Hz and the HPF as 48 Hz as in the solution, the passbands of the two filters overlap and 50 Hz is not suppressed.*

## Questions from undated exams

The questions below are in the same photo group but their pages carry no exam name or date. Since the question numbers overlap (there are two separate "4." questions), it is understood that they belong to at least two different exams.

### Question 2: Amplifier design with two op-amps (20 pts)

Same as Question 4 of the 2013 fall midterm: for the circuit with two ideal op-amps, a) derive the expression A_v = V_L / V₁ (12 pts), b) design the circuit so that A_v = 15 and |V_o1| = |V_o2| (8 pts).

**Student solution:** In the first op-amp V₊ = V₋ = V₁ ⇒ A_f1 = v_o1 / v₁ = 1 + R₂/R₁. In the second op-amp V₋ = V₊ = 0 ⇒ v_o1/R₃ = −v_o2/R₄ ⇒ A_f2 = v_o2 / v_o1 = −R₄/R₃.

A_f = (v_o1 − v_o2) / v₁ = (1 + R₂/R₁)(1 + R₄/R₃)

b) |v_o1| = |v_o2| and A_f = 15 ⇒ v_o1 − v_o2 = 15 v₁, each being 7.5 v₁. R₄/R₃ = 1 is required (R₃ = R₄ = 10 kΩ); 1 + R₂/R₁ = 7.5 ⇒ R₂/R₁ = 6.5 ⇒ R₂ = 13 kΩ, R₁ = 2 kΩ.

### Question 3: Filter for the phase detector output (20 pts)

The phase detector multiplies the signals at its two inputs; the signal at its output has components at the sum and difference frequencies of these input signals. Therefore, one of the frequency components of the signal at the phase detector output is (f_in + f_osc) and the other is (f_in − f_osc).

In the circuit below:

- The signal at the input of the phase detector varies between V_in(t) = 5 sin 34540t and V_in(t) = 5 sin 62800t (its amplitude does not change but its frequency varies within this range).
- The oscillator generates a signal at a constant frequency and is V_osc(t) = 1 sin 31400t.

Since it is required that the output of the circuit (V_out(t)) take the difference-frequency signal component (f_in − f_osc) at the phase detector output and attenuate signals at other frequencies by a factor of 1/100, design the appropriate circuit for the place indicated by the question mark in the circuit (take π = 3.14). (20 pts)

*Block diagram:* V_in(t) → Phase Detector (oscillator output V_osc(t) at the second input) → (f_in − f_osc), (f_in + f_osc) → [?] → (f_in − f_osc) → V_out(t)

**Graded solution:**

- f_in1 = 34540 / 2π = 5500 Hz, f_in2 = 62800 / 6.28 = 10 000 Hz, f_osc = 31400 / 2π = 5000 Hz
- f_in1 − f_osc = 500 Hz, f_in2 − f_osc = 5000 Hz: the range 500 Hz – 5000 Hz must pass, and the sum frequencies (10.5–15 kHz) must not pass.
- 20 log(1/100) = −40 dB ⇒ second-order filter ⇒ a second-order band-pass filter design is required.
- HPF (f_HPF = 500 Hz): C₁ = C₂ = C = 5 nF, R₁ = R, R₂ = 2R. 500 Hz = 1 / (2π · 5 nF · √(R₁R₂)) ⇒ R = 1 / (2π · 5 nF · √2 · 500 Hz) = 45.173 kΩ ⇒ R₁ = 45.173 kΩ, R₂ = 90.346 kΩ
- LPF (f_LPF = 5000 Hz): C₄ = C = 1 µF, C₃ = 2C = 2 µF, R₃ = R₄ = R. R = 1 / (2π · 1 µF · √2 · 5000 Hz) ⇒ R₃ = R₄ = 22.5 Ω

### Question 4: High-frequency analysis of a MOSFET amplifier (15 pts)

A version of Question 1 of the January 2014 final with different values: A_vmid = −40; R_D = 40 kΩ, R_S = 2 kΩ, C_gd = 0.5 pF, C_gs = 1 pF, g_m = 1 mS, r_o = r_ds = ∞.

- a) Draw the high-frequency ac equivalent circuit and find the cutoff frequencies. (7 pts)
- b) Draw the overall frequency response of the circuit (Bode plot) and indicate the upper cutoff frequency. (3 pts)
- c) If a signal with a frequency of 1 kHz and an amplitude of 100 mV_pp is applied to the circuit, what is the amplitude V_opp of the signal at the output? (2 pts)
- d) If a signal with a frequency of 5 MHz and an amplitude of 100 mV_pp is applied to the circuit, what is the amplitude V_opp of the signal at the output? (3 pts)

**Graded student solution:**

- a) C_Mi = 41 · 0.5 pF = 20.5 pF, C_Mo ≅ 0.5 pF; f_input = 1 / [2π (C_Mi + C_gs) R_S] = 3.7 MHz, f_output = 1 / [2π C_Mo R_D] = 7.96 MHz
- b) In the midband ≅ 32 dB; after 3.7 MHz −20 dB/decade, after 7.96 MHz −40 dB/decade. f_upper = 3.7 MHz.
- c) At 1 kHz in the midband: A_v = −40 ⇒ V_opp = 40 · 100 mV_pp = 4 V_pp
- d) A_v(5 MHz) = 40 / √(1 + (5/3.7)²) = 23.79 ⇒ V_opp = 23.79 · 100 mV_pp ≅ 2.3 V_pp

### Question 4: High-frequency response of a common-gate amplifier (15 pts)

For the common-gate amplifier circuit below, which uses a transistor with parameters g_m = 2.1 mA/V, C_gs = 15 pF, C_gd = 4 pF, r_o = ∞:

- a) Find the midband gain (A_vmid). (5 pts)
- b) Draw the high-frequency equivalent circuit, find the dominant upper cutoff frequency, and sketch the high-frequency response with the gain shown in dB. (10 pts)

*Circuit:* The source V_i is connected to the source terminal of the MOSFET through R_i = 2 kΩ and C_C1 = 1 µF; the source terminal goes through R_S = 10 kΩ to V⁻ = −5 V. The gate is grounded. The drain goes through R_D = 5 kΩ to V⁺ = +5 V; the output goes through C_C2 = 2 µF to R_L = 4 kΩ.

**A student's solution:**

- a) A_vmid = V_o / V_gs = g_m (5 k ‖ 4 k) ≅ 4.66
- b) Output pole: R_eq = 5 k ‖ 4 k = 2.2 kΩ, C = C_gd = 4 pF ⇒ f = 1 / (2π · 2.2 k · 4 pF) ≅ 18 MHz. Input pole: R_eq = 2 k ‖ 10 k = 1.66 kΩ, C = C_gs = 15 pF ⇒ f ≅ "63 MHz".

*Note: 1 / (2π · 1.66 kΩ · 15 pF) ≅ 6.4 MHz, not 63 MHz. Also, in a common-gate circuit the resistance looking into the source terminal is 1/g_m ≅ 0.48 kΩ and must be taken in parallel with R_i ‖ R_S: R_eq ≅ 0.37 kΩ ⇒ f_input ≅ 28.7 MHz. In this case the dominant upper cutoff frequency is the ≅ 17.9 MHz pole at the output.*

### Question 5: Design of a waveform-generating system (20 pts)

From a system with the input signal V_in = 20 sin 100πt and ±30 volt DC supplies, the two output signals described below are to be obtained:

- V_out1 = 6 + 5 sin 100πt − 30 sin 100πt
- V_out2 = a square wave with f = 50 Hz, 30 volts peak-to-peak, and T_positive = T_negative

Design the system that will give the desired outputs. Show all calculations in your designs. Obtain the DC voltages required for the operation of the circuits or components you use from the given DC sources.

**Graded solution:**

- V_in = 20 sin 100πt ⇒ 2πf = 100π ⇒ f = 50 Hz
- (a) Inverting amplifier, 2 kΩ input / 3 kΩ feedback: A_v = −3/2 = −1.5 ⇒ V_a = −1.5 · 20 sin 100πt = −30 sin 100πt
- (b) Inverting amplifier, 8 kΩ input / 2 kΩ feedback: A_v = −2/8 = −0.25 ⇒ V_b = −0.25 · 20 sin 100πt = −5 sin 100πt
- (c) Inverting amplifier, 1 kΩ / 1 kΩ: A_v = −1 ⇒ V_c = 5 sin 100πt
- (d) 4 kΩ – 1 kΩ voltage divider from +30 V: V_d = 30 · 1k / 5k = 6 V
- These voltages are summed to obtain V_out1 (the details of the summing connection cannot be fully made out in the photograph).
- For V_out2, a zero-reference comparator: V_in > V_REF = 0 ⇒ V_o = +15 V, V_in < 0 ⇒ V_o = −15 V. The comparator's ±15 V supply is obtained from ±30 V with 10 kΩ – 10 kΩ voltage dividers. The output is a square wave with 50 Hz, 30 V_pp, T₁ = T₂.

### Question 6: Voltage regulator with an op-amp (20 pts)

The same question as Question 5 of the January 2014 final (20 points in this exam; with the added warning "NOTE: Use the ideal op-amp equivalent circuit."): V_Z = 6.3 V, A_OL = 1000, R₁ = 4 kΩ, 10 kΩ – 10 kΩ feedback, R_o = 0.5 kΩ, I_ONL = 1 mA, I_OFL = 100 mA; find the % load regulation.

**Solution (answer key):** V₁ = V_o/2; from the output node V_o(1002.05) + I_o = 12 600 ⇒ V_o(NL) = 12.5732 V, V_o(FL) = 12.4744 V ⇒ **load regulation ≅ 0.79%**.
