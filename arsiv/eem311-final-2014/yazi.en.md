---
baslik: EEM311 Electronics II: January 2014 Final (End-of-Semester) Exam Questions and Answer Key
ozet: The January 6, 2014 final exam and answer key for EEM311 Electronics II: high-frequency analysis of a MOSFET amplifier using the Miller effect, a three-transistor series-shunt feedback amplifier, a bridge and instrumentation amplifier, a band-pass filter for a phase detector, and the load regulation of an op-amp regulator.
---

This post presents the **final exam (end-of-semester exam) of the 2013-2014 fall semester** (06.01.2014) for the Başkent University Electrical-Electronics Engineering course **EEM 311 Electronics II**. The source is photographs shared by a friend: "CEVAP ANAHTARI" (ANSWER KEY) is handwritten across the top of the first page; some of the solutions are printed (in English), some handwritten, with scores in red beside them. For Question 2, only the result of the answer key could be read, so the intermediate steps were taken from a student's handwritten work. Personal information has been removed. The questions and the main steps of the solutions were transcribed into text from the photographed pages; the photographs themselves are not published.

The exam lasted 120 minutes, and the point distribution is as follows:

| Question | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|
| Points | 22 | 28 | 16 | 19 | 15 | 100 |

## Question 1: High-frequency analysis of a MOSFET amplifier (22p)

The midband gain of the amplifier below is given as A_vmid = −40. By performing the high-frequency analysis of the circuit:

- a) Draw the high-frequency ac equivalent circuit and find the cutoff frequencies. (12p)
- b) Draw the overall frequency response (Bode plot) of the circuit and indicate the upper cutoff frequency. (4p)
- c) If a signal with a frequency of 2 MHz and an amplitude of 10 mV_pp is applied to the circuit, what is the amplitude V_opp of the output signal? (2p)
- d) If a signal with a frequency of 8 MHz and an amplitude of 10 mV_pp is applied to the circuit, what is the amplitude V_opp of the output signal? (4p)

Take R_D = 40 kΩ, R_S = 2 kΩ, C_gd = 0.5 pF, C_gs = 1 pF, g_m = 1 mS, r_o = r_ds = ∞.

*Circuit:* Common-source n-channel MOSFET amplifier with +5 V / −5 V supplies. The source (signal) is connected to the gate through R_S; the drain is connected to +5 V through R_D, and the source terminal is connected to −5 V; the output is taken from the drain.

### Solution (answer key)

C_gd is split in two using Miller's theorem:

C_Mi = (|A_v| + 1) C_gd = 41 · 0.5 pF = 20.5 pF

C_Mo = ((|A_v| + 1) / |A_v|) C_gd = (41/40) · 0.5 pF ≅ 0.5 pF

Input pole: f_input = 1 / [2π (C_Mi + C_gs) R_S] = **3.7 MHz**

Output pole: f_output = 1 / [2π C_Mo R_D] = **7.96 MHz**

In the equivalent circuit, there is R_S at the input followed by C_gs in parallel with C_Mi; at the output there is the g_m·v_gs dependent current source, C_Mo, and R_D = 40 kΩ.

**b)** Bode magnitude plot: the midband gain is 20 log 40 ≅ 32 dB; it rolls off at −20 dB/decade after 3.7 MHz and at −40 dB/decade after 7.96 MHz. The upper cutoff frequency (dominant pole) is **f_H ≅ 3.7 MHz**.

**c)** The key notes that 2 MHz lies below the dominant cutoff frequency, so the gain can be taken as its midband value: V_opp = 40 · V_ipp = **400 mV_pp**.

*Note: With the exact calculation, |A_v| = 40 / √(1 + (2/3.7)²) ≅ 35.2 and V_opp ≅ 352 mV_pp; the key uses the midband approximation.*

**d)** In the key, the gain is calculated in two steps:

A_v(7.96 MHz) = 40 / √(1 + (7.96/3.7)²)

A_v(8 MHz) = A_v(7.96 MHz) / √(1 + (8/7.96)²)

*Note: The numerical result is not visible in the photograph of the key; evaluating these expressions gives A_v(7.96 MHz) ≅ 16.9, A_v(8 MHz) ≅ 11.9, and V_opp ≅ 119 mV_pp.*

## Question 2: Three-transistor feedback amplifier (28p)

In the feedback amplifier circuit below, β = 120 and r_o = ∞ are given for all transistors. In addition, the small-signal parameters of transistors Q₁, Q₂ and Q₃ are r_π1 = 3.66 kΩ, r_π2 = 6.28 kΩ, r_π3 = 1.54 kΩ, g_m1 = 32.81 mS, g_m2 = 19.12 mS and g_m3 = 78.08 mS. Find the small-signal voltage gain of the circuit with feedback: A_vf = v_o / v_i. (28p)

(The question text is blurry in the photograph; the r_π values were taken from the student's solution and are consistent with r_π = β/g_m.)

*Circuit:* V_CC = 10 V. Q₁ is common-emitter; base bias R₁ = 400 kΩ and R₂ = 75 kΩ, input v_i through C_C → ∞; collector resistor R_C1 = 8.8 kΩ, emitter resistor R_E1 = 0.5 kΩ (unbypassed). Q₂ is common-emitter; R_C2 = 13 kΩ, R_E2 = 3.6 kΩ (bypassed with C_E → ∞). Q₃ is an emitter follower; emitter resistor R_E3 = 1.4 kΩ, and the output v_o is taken from the emitter of Q₃. Feedback resistor R_F = 10 kΩ (in series with C_F → ∞) connects the output to the emitter of Q₁.

### Student solution

The feedback type is **series-shunt** (voltage sampling, series mixing). For the loading effect of the feedback network: the output is short-circuited when finding the resistance reflected to the input, and the input side is open-circuited when finding the resistance reflected to the output:

- R₁₁ = R_E1 ‖ R_F (seen at the emitter of Q₁)
- R₂₂ = R_F + R_E1 (at the output, in parallel with R_E3)

The gain without feedback (loaded) is written as the product of the gains of the three stages:

A′ = [−β I_b1 (R_C1 ‖ β r_e2) / (I_b1 (β r_e1 + β R₁₁))] · [−β I_b2 (R_C2 ‖ β(r_e3 + R_E3 ‖ R₂₂)) / (I_b2 β r_e2)] · [β I_b3 (R₂₂ ‖ R_E3) / (I_b3 β(r_e3 + R_E3 ‖ R₂₂))]

A′ = (−7.23) · (−228.55) · 0.98

Feedback ratio: β_f = R_E1 / (R_E1 + R_F) = 0.5 k / 10.5 k = 1/21

A_vf = A′ / (1 + A′β_f)

The student's solution leaves it at "substitute"; since A′ ≅ 1619, A_vf = 1619 / (1 + 1619/21) ≅ 20.7.

**Answer key** (printed English solution, very blurry in the photograph): the circuit is drawn with transistor models and solved by writing five node equations; the result is **v_o / v_i = 20.73**. Since the loop gain is large, the result is very close to the ideal value 1/β_f = 21.

## Question 3: Bridge and instrumentation amplifier design (16p)

The op-amps in the circuit below are powered with ±10 V. The output voltage of the bridge in the circuit is given by v_O1 = (δ/4) V⁺, and for δ = 0.01 the circuit output is required to be v_O = +5 V. Accordingly, design the circuit by finding the unknown resistor values (R₁, R₂, R₃, R₄). (16p)

*Circuit:* The bridge supply voltage V⁺ is obtained by amplifying, with a non-inverting op-amp (200 kΩ and 67.86 kΩ resistors), a reference built from V_S = 18 V with a zener diode (V_Z = 5.6 V, I_Z = 0.25 mA). Three arms of the bridge are 200 kΩ, and the fourth arm is 200(1+δ) kΩ. The bridge output is applied to a three-op-amp instrumentation amplifier (R₁ and R₂ in the input stage, R₃ and R₄ in the difference stage).

### Solution (answer key)

V⁺ = 5.6 V · (1 + 67.86/200) ≅ 7.5 V. For V⁺ = 7.5 V and δ = 0.01, the maximum bridge output is:

v_O1 = (δ/4) V⁺ = 0.01875 V

For the amplifier output to be +5 V, the gain of the instrumentation amplifier must be 5 / 0.01875 = **266.7**. The output of the instrumentation amplifier is:

v_O / v_O1 = (R₄/R₃)(1 + 2R₂/R₁) = 266.7

The ratios R₄/R₃ and R₂/R₁ are desired to be of the same order of magnitude. If R₃ = 15.0 kΩ and R₄ = 187.0 kΩ are chosen, then R₄/R₃ = 12.467 and R₂/R₁ = 10.195. If R₂ = 200.0 kΩ is chosen, then **R₁ = 19.62 kΩ**.

Check: 12.467 × (1 + 2 × 10.195) = 12.467 × 21.39 ≅ 266.7.

## Question 4: Phase detector and RC phase-shift oscillator (19p)

A phase detector multiplies the signals at its two inputs and gives at its output a signal containing the sum- and difference-frequency components of these signals. For the circuit below, the frequency of one of these components at the phase detector output is (f_in + f_osc), and that of the other is (f_in − f_osc).

In the circuit below:

- The signal at the input of the phase detector is V_in(t) = 5 sin 37680t.
- The signal generated by the oscillator varies between V_osc(t) = 1 sin 9420t and 1 sin 32028t (its amplitude does not change but its frequency varies).

Given that the difference-frequency component (f_in − f_osc) of the phase detector output is to be taken at the circuit output (V_out(t)), and signals at frequencies other than these are to be attenuated at a rate of −40 dB/decade:

- a) Design the circuit appropriate for the place marked with a question mark in the circuit (take π = 3.14). (15p)
- b) Find the range of variation of R so that the oscillator generates a signal in the specified range. (4p)

*Circuit:* V_in(t) → Phase Detector → (f_in − f_osc), (f_in + f_osc) → [?] → (f_in − f_osc) → V_out(t). The oscillator is an op-amp RC phase-shift oscillator: 30 kΩ in the feedback of the inverting amplifier, a three-stage C–R network at the input (C = 0.1 µF, three adjustable R); f_osc = 1 / (2π R C √6).

### Solution (answer key)

**a)** f_in = 37680 / 2π = 6000 Hz; f_osc1 = 9420 / 2π = 1500 Hz, f_osc2 = 32028 / 2π = 5100 Hz

f_in − f_osc1 = 6000 − 1500 = 4500 Hz, f_in − f_osc2 = 6000 − 5100 = 900 Hz ⇒ the filter must pass 900 Hz – 4500 Hz: a **second-order band-pass filter** (−40 dB/decade).

- Second-order HPF (f_c = 900 Hz): two 5 nF capacitors, 25 kΩ and 50 kΩ resistors
- Second-order LPF (f_c = 4500 Hz): two 5 kΩ resistors, 10 nF and 5 nF capacitors

Check: 1 / (2π · 25 kΩ · 5 nF · √2) ≅ 900 Hz; 1 / (2π · 5 kΩ · 5 nF · √2) ≅ 4500 Hz.

**b)** The solution to this part is not visible in the photograph.

*Note: With f_osc = 1 / (2π R C √6) and C = 0.1 µF, R ≅ 433 Ω for 1500 Hz and R ≅ 127 Ω for 5100 Hz; R must vary between approximately 127 Ω and 433 Ω.*

## Question 5: Voltage regulator with an op-amp (15p)

In the voltage regulator circuit below, the zener diode and the op-amp are assumed to be ideal. The zener voltage is V_Z = 6.3 V, and the open-loop voltage gain of the op-amp is given as A_OL = V_o/V_d = 1000 (V_d = V₊ − V₋). The output current of the circuit is 1 mA when the circuit is unloaded and 100 mA at full load. Calculate the % load regulation of the circuit. (15p)

*Circuit:* The zener diode is supplied from V⁺ through R₁ = 4 kΩ and applies V_Z to the non-inverting input of the op-amp. A 10 kΩ resistor connects the inverting input to ground, and a 10 kΩ feedback resistor connects it to the output node. The op-amp's output resistance is R_o = 0.5 kΩ; the output V_o delivers current I_o to the load R_L.

### Solution (answer key)

The op-amp is modeled as a dependent voltage source of value A_OL(V_Z − V₁) in series with R_o.

Inverting input node: V₁/10 = (V_o − V₁)/10 ⇒ V₁(1/10 + 1/10) = V_o/10 ⇒ V_o = 2V₁, i.e., V₁ = V_o/2

Output node: (V_o − V₁)/10 + V_o/R_L + [V_o − A_OL(V_Z − V₁)]/R_o = 0

Writing I_o = V_o/R_L and substituting V₁ = V_o/2 (currents in mA, resistances in kΩ):

V_o/20 + I_o + V_o/0.5 − 1000(6.3)/0.5 + 1000 V_o/(2 · 0.5) = 0

V_o(0.05 + 2 + 1000) + I_o = 12 600 ⇒ V_o(1002.05) + I_o = 12 600

- I_o = 1 mA (no load) ⇒ V_o = 12.5732 V
- I_o = 100 mA (full load) ⇒ V_o = 12.4744 V

Load regulation = [V_o(NL) − V_o(FL)] / V_o(FL) × 100% = (12.5732 − 12.4744) / 12.4744 × 100% ⇒ **Load regulation ≅ 0.79%**
