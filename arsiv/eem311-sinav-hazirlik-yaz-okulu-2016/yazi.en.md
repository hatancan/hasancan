---
baslik: EEM311 Electronics II: 2016 Summer School Exam Preparation Notes, Active Filters, Oscillators and Feedback
ozet: Handwritten notes from the EEM311 Electronics II 2016 summer school: Butterworth high-pass and band-pass filter design, quality factor and narrow-band BPF, Hartley, Colpitts, Clapp and crystal oscillators, feedback types and impedance changes, and current and transconductance feedback amplifier examples.
---

This post presents the handwritten lecture notes taken by a friend during the **2016 summer school** (27 July – 9 August 2016) of Başkent University's **EEM 311 Electronics II** course, together with the example problems written on the board in class. The notes were compiled together with past exam questions in preparation for the final exam. Personal information has been removed. The content was transcribed from photographed pages into text; the photographs themselves are not published. Places where the handwriting could not be read are indicated.

## Butterworth high-pass filters (27.07.2016)

### Second-order high-pass filter (HPF)

Circuit: two series capacitors at the input (C₁ = C₂ = C); from the node between them, R₁ = R goes to the op-amp output; from the op-amp's non-inverting input, R₂ = 2R goes to ground; the op-amp is connected as a voltage follower.

f_c = 1 / (2π √(R₁ R₂ C₁ C₂)) = 1 / (2π R C √2)

Gain curve: at f_c the gain is 0.707 (−3 dB), and at f_c/10 it is 0.01 (−40 dB); the slope in the transition region is **−40 dB/decade** (as frequency decreases).

**Example:** Design a circuit that attenuates the output by a factor of 1/100 at 1 kHz and passes 10 kHz and above. Let C = 1 nF.

R = 1 / (2π · 10⁻⁹ · 10 · 10³ · √2) = …

*Note: The result is not written in the notes; if calculated, R ≅ 11.25 kΩ (R₂ = 2R ≅ 22.5 kΩ) is obtained.*

### Third-order HPF

A first-order HPF stage (C₃ = C, R₃ = R, voltage follower) is added after the second-order HPF stage. At f_c/10 the gain is 0.001 (−60 dB); the slope is **−60 dB/decade**.

**Examples:**

- Design a circuit that attenuates signals below 2 kHz with a slope of −60 dB/decade (C = 0.1 µF): of the form R = 1 / (2π · f_c · C) (no value is written in the notes).
- Design a 3-pole filter circuit that passes frequencies above 5 kHz.

## Band-pass filters

A band-pass filter (BPF) is obtained by cascading a low-pass filter (LPF) with an HPF. The lower cutoff frequency f_L is the cutoff frequency of the HPF; the upper cutoff frequency f_H is the cutoff frequency of the LPF. The bandwidth is BW = f_H − f_L.

### First-order BPF

A first-order LPF (series R, shunt C to ground, voltage follower) followed by a first-order HPF (series C, shunt R to ground, voltage follower). The slope is −20 dB/decade on both sides.

**Example:** Design a first-order BPF that passes 1 kHz – 10 kHz (C = 0.1 µF). 1 kHz is for the HPF, 10 kHz for the LPF:

- For the LPF: f_c = 1 / (2π · 10 · 10³ · 0.1 · 10⁻⁶ · R)
- For the HPF: f_c = 1 / (2π · 10³ · 0.1 · 10⁻⁶ · R)

*Note: From this, R ≅ 159 Ω for the LPF and R ≅ 1.59 kΩ for the HPF (no numerical value in the notes).*

### Second-order BPF

A second-order HPF (C₁ = C₂ = C, R₁ = R, R₂ = 2R) followed by a second-order LPF (R₃ = R₄ = R*, C₃ = 2C*, C₄ = C*).

**Example:** Design a filter that passes 300 Hz – 3 kHz.

- For the HPF f_c = 300 Hz = 1 / (2π R C √2), C = 0.01 µF
- For the LPF f_c = 3 kHz = 1 / (2π R C √2), C* = 0.1 µF

### Quality factor

- Center frequency: f_m = f_L + BW/2 = f_H − BW/2
- Resonant frequency: f_r = √(f_L f_H)
- Quality factor: Q = f_r / BW. The notes state narrow-band for Q ≥ 10 and wide-band for Q < 10; next to it, a separate criterion has also been added: Q ≥ 0.5 narrow band, Q < 0.5 wide band.

**Example:** f_r = √(300 · 3000) = 948.68 Hz, BW = 3000 − 300 = 2700 Hz, Q = 948.68 / 2700 ≅ 0.35 (0.3 in the notes) ⇒ wide-band.

### Narrow-band BPF (multiple feedback)

The circuit marked "memorize" in the notes: the input goes through R₁ to a node; from this node, R₃ goes to ground, C₁ to the op-amp output, and C₂ to the op-amp's inverting input; R₂ is between the inverting input and the output.

- f_r = 1 / (2π C √((R₁ ‖ R₃) R₂))
- R₁ = Q / (2π f_r C A_f)
- R₂ = Q / (π f_r C)
- R₃ = Q / (2π f_r C (2Q² − A_f))
- Q = f_r / BW = 2π f_r A_f C R₁ = π f_r C R₂

*Note: The gain expression in the notes reads like "A_f = R₂/R₁"; dividing the R₁ and R₂ formulas above gives R₂/R₁ = 2A_f, i.e. A_f = R₂/(2R₁).*

**Example:** A 10-channel equalizer has resonant frequencies of 1 kHz, 2 kHz, …, 10 kHz. Design the 6th band filter of the equalizer for Q = 10. f_r = 6 kHz, BW = f_r / Q = 6 kHz / 10 = 600 Hz.

## Oscillators (1.8.2016)

In LC oscillators, according to the types of the three impedances in the amplifier's feedback network:

| Oscillator | Z₁ | Z₂ | Z₃ |
|---|---|---|---|
| Hartley | L | L | C |
| Colpitts | C | C | L |
| Clapp | C | C | L and C (series) |
| Crystal | C | C | X_TAL (crystal) |

- **Hartley oscillator (with op-amp):** Block A is an inverting amplifier built with R₁ and R₂; block β is two inductors with a grounded center tap (Z₂, Z₁) and a capacitor between their ends (Z₃).
- **Transistor Hartley oscillator:** a common-emitter BJT with a parallel Z₃ capacitor and a center-tapped Z₁–Z₂ inductor at the collector; the output is taken from a second winding on the inductor (transformer coupled).
- **JFET Hartley oscillator:** the same feedback network connected to the input of a JFET amplifier.
- **Crystal oscillator (with op-amp):** in block β, two capacitors with a grounded midpoint and a crystal (X_TAL) in parallel with them.

## Feedback amplifiers (2.8.2016)

Advantages of feedback:

- The larger the input impedance, the better: R_i ↑, R_o ↓
- It improves the amplifier's frequency response (BW ↑)
- It gives more linear operation

In a single-transistor common-emitter circuit, an unbypassed R_E is also feedback for the circuit.

### Feedback types

| Sampling / mixing | Amplifier type | A | β |
|---|---|---|---|
| Voltage-voltage (series mixing, shunt sampling) | Voltage amplifier | V_o / V_i | V_f / V_o |
| Current-voltage (shunt mixing, shunt sampling) | Transresistance amplifier | V_o / I_i | I_f / V_o |
| Voltage-current (series mixing, series sampling) | Transconductance amplifier | I_o / V_i | V_f / I_o |
| Current-current (shunt mixing, series sampling) | Current amplifier | I_o / I_i | I_f / I_o |

In brief in the notes: if the feedback is connected in series at the input and in parallel at the output, it is a voltage amplifier.

*Note: In the notes, the output side for the voltage-current and current-current types is written as "parallel sampled"; in these two types the output current is sampled in series, so it is given that way in the table.*

### Input-output impedance changes

| | Voltage-series (series-shunt) | Current-series (series-series) | Voltage-shunt (shunt-shunt) | Current-shunt (shunt-series) |
|---|---|---|---|---|
| Z_if | Z_i (1 + βA) | Z_i (1 + βA) | Z_i / (1 + βA) | Z_i / (1 + βA) |
| Z_of | Z_o / (1 + βA) | Z_o (1 + βA) | Z_o / (1 + βA) | Z_o (1 + βA) |

Rule: if the input is series, multiply by (1 + βA); if the input is shunt, divide by (1 + βA); at the output, divide for voltage sampling and multiply for current sampling.

**Example (series-shunt):** In a non-inverting op-amp amplifier with A = 100,000, R₁ = 1.8 kΩ, R₂ = 200 Ω, find the closed-loop gain of the circuit.

β = V_f / V_o = R₂ / (R₁ + R₂) = 0.1

Since A ≫ 1, 1 + Aβ ≅ Aβ ⇒ A_v = A / (Aβ) = 1/β = **10**

## Sampling-mixing and exam question (5.8.2016)

Summarized again in the notes:

- Series mixing – series sampling → transconductance amplifier
- Series mixing – shunt sampling → voltage amplifier
- Shunt mixing – shunt sampling → transresistance amplifier
- Shunt mixing – series sampling → current amplifier
- When finding the loading effect of the feedback circuit: open-circuit on the series side, short-circuit on the shunt side.

### Exam question (25 points): feedback current gain

The question written on the board: β = 100, r_o = ∞, r_π1 = 13.1 kΩ (= (β+1) r_e), r_π2 = 1.9 kΩ, g_m1 = 7.62 mS, g_m2 = 52.7 mS. Find the closed-loop current gain of the circuit: A_if = I_o / I_s = ?

*Circuit:* V⁺ = +10 V. The input current source I_s, in parallel with R_S = 10 kΩ, is connected to the base of Q₁. The collector of Q₁ is connected to V⁺ through R_C1 = 40 kΩ, and its emitter to ground. The base of Q₂ is connected to the collector of Q₁; R_C2 = 2 kΩ, and the output goes through C → ∞ to R_L = 0.5 kΩ (I_o is the load current); R_E = 1 kΩ at the emitter of Q₂. The feedback resistor R_F = 10 kΩ (in series with C → ∞) is connected from the emitter of Q₂ (node V_e) to the base of Q₁ (shunt-series, current amplifier).

**Solution (node equations, on the board and in the notes):**

1. I_s = V_π1 (1/10 + 1/13.1 + 1/10) − V_e (1/10) ⇒ I_s = V_π1 (0.2763) − V_e (0.1)
1. (7.62) V_π1 + V_π2 (1/40 + 1/1.9) + V_e (1/40) = 0 ⇒ (7.62) V_π1 + V_π2 (0.5513) + V_e (0.025) = 0
1. V_π2 (1/1.9 + 52.7) = V_e (1/1 + 1/10) − V_π1 (1/10) ⇒ V_π2 (53.23) = V_e (1.1) − V_π1 (0.1)

From (3): V_e = V_π2 (48.39) + V_π1 (0.0909). Substituting into (1):

I_s = V_π1 (0.2763) − (0.1)[V_π2 (48.39) + V_π1 (0.0909)] ⇒ I_s = V_π1 (0.2672) − V_π2 (4.839)

Substituting into (2): (7.622) V_π1 + V_π2 (1.761) = 0 ⇒ V_π1 = −V_π2 (0.2310)

From this, I_s = (0.2672)(−V_π2)(0.2310) − V_π2 (4.839) ⇒ I_s = −V_π2 (4.901)

I_o = −g_m2 V_π2 [R_C2 / (R_C2 + R_L)] = (−52.7)(2 / 2.5) V_π2 = −42.16 V_π2

I_o = −(42.16)(−I_s / 4.901) ⇒ **A_if = I_o / I_s ≅ 8.60**

## Transconductance feedback amplifier (9.8.2016)

A three-transistor circuit whose title ("… Question") cannot be fully read in the notes: r_o = ∞, β = 120, V_T = 26 mV, I_C1 = 0.5 mA, I_C2 = 1 mA, I_C3 = 2 mA. Find the transconductance transfer function of the circuit: A_gf = I_o / V_s = ?

- Feedback circuit: the resistor (R_E) between the emitters of Q₁ and Q₃, and the two emitter resistors (R_E1, R_E2).
- The resistance reflected to the input is R₁₁ = R_E1 (in the notes), and the resistance reflected to the output is R₂₂ = R_E + R_E1.
- In the ac equivalent circuit, each transistor is modeled with a β r_e resistance and a β I_b current source; I_o = β I_b3.
- First equation for the emitter node of Q₁: I_b1 + β I_b1 = V_e1 / R_E1 + (V_e1 − V_e2) / R_E

The solution in the notes is left at this point. (This question is question 2 of the January 2016 final; the result in the answer key is A_gf ≅ 98 mA/V.)

On another page, the loading resistances of the feedback network are calculated in the ac equivalent of a three-stage amplifier: R₁₁ = 9 kΩ ‖ 1 kΩ = 0.9 kΩ, R₂₂ = 9 kΩ + 1 kΩ = 10 kΩ, R_i3 = β r_e3 + β[(9 k + 1 k) ‖ R_L].

## High-frequency response

The high-frequency response is determined by the transistor's internal (hidden) capacitances: C_be, C_bc and C_ce. External capacitances (C_i, C_o coupling capacitors) are not taken into account at high frequencies.

- C_bc is reflected to both sides using Miller's theorem: C_Miller,input = C_bc (1 + |A_v|), C_Miller,output = C_bc (1 + 1/|A_v|)
- Parallel capacitances are summed.

**Frequency response questions (example):** On the low-frequency side, three break frequencies are given as 500 Hz, 700 Hz and 1 kHz; assuming the gain after the highest break is 100, the gains at the break points are calculated in order: A_V(700 Hz) = 100 / √(1 + (1 kHz / 700 Hz)²). On the graph, the gain values are marked as 100, 70.7 and 65. The general rule in the notes is "A_V = previous gain / √(1 + (ratio)²)", written separately for the low-frequency and high-frequency sides; the numerator and denominator of the ratio cannot be made out exactly in the handwriting.
