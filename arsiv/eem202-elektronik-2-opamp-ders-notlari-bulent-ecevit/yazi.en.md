---
baslik: EEM202 Circuit Theory II: Operational Amplifiers (Op-Amp) Lecture Notes (Bülent Ecevit University, İsmail Şahin)
ozet: Bülent Ecevit University Alaplı Vocational School Electronics II lecture notes (Lecturer İsmail Şahin): ideal and real op-amp characteristics, inverting and non-inverting amplifiers, voltage follower, summing amplifier, difference amplifier, comparator, integrator and differentiator, active filters, and oscillators; with examples and test questions.
---

This post presents the **"Electronics II Lecture Notes"** prepared by **Lecturer İsmail Şahin** at **Bülent Ecevit University Alaplı Vocational School** (58 pages, PDF dated December 2012). The notes are devoted entirely to operational amplifiers (op-amps); they were kept in the course folder as a reference for the active filter experiments in the EEM202 laboratory. Below, the topics, main definitions, and formulas are summarized; the complete notes (the original PDF) can be downloaded at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request by the rights holder.*

## Introduction to the Op-Amp

Op-amps are directly coupled, high-gain circuit elements; their gain can be adjusted without making many changes to the circuit (example: the 741 IC). Their applications include: phase inverter, voltage follower, non-inverting amplifier, summing amplifier, difference amplifier, comparator, integrator and differentiator circuits, filters, D/A converters, and oscillators.

**Characteristics of an ideal op-amp:**

1. The open-loop voltage gain is infinite.
1. When V1 = V2, V0 = 0.
1. The input resistance is infinite and the input currents are zero.
1. The output resistance is zero.
1. The bandwidth is infinite.
1. Its characteristics do not change with temperature or time.

## Real (Non-Ideal) Characteristics

- **Input offset voltage:** Since the transistor pairs in the input stage are not perfectly matched, the output is nonzero when V1 = V2 = 0. The input offset voltage is the differential input voltage that makes the output zero (approximately 1 mV for the LM741); it is adjusted with a 10 kΩ potentiometer.
- **Input bias current (I_B):** Approximately 80 nA for the LM741, and on the order of 50 pA for FET-input types.
- **Open-loop gain and frequency characteristics:** K = 20 log[V0/(V2 − V1)] dB. At high frequencies the gain-bandwidth product (GBW) is constant; for the LM741, **GBW = 1 MHz** (unity-gain bandwidth). If the closed-loop gain is K_n, the bandwidth is B_n = GBW/K_n.
- **Rise time:** t_r·B_n = 0.35 (for the LM741, t_r = 0.3 µs with a 200 mV input).
- **Output voltage limit:** the output cannot reach the supply voltages; in the LM741 with a ±15 V supply, it clips at approximately ±13 V.
- **Large-signal slew rate:** S = 2V_k/T_SR.
- **Common-mode rejection ratio (CMRR):** the ratio of the differential gain to the common-mode gain; approximately 90 dB for the LM741.
- **Output resistance (R_O).**

*Note: The document gives the LM741's input offset current as "approximately 21 mA", its temperature drift as "0–5 mA/°C", and its slew rate as "S = 0.5 V/msec"; the typical values for the 741 are approximately 20 nA for the offset current and **0.5 V/µs** for the slew rate. The input resistance is also approximately 2 MΩ for the 741.*

## Basic Circuits

- **Inverting amplifier:** V0 = −(R_f/R_1)·V_i.
- **Non-inverting amplifier:** V0 = (1 + R_f/R_1)·V_i. Example: for V1 = 2 V, R_f = 500 kΩ, R_1 = 100 kΩ, V0 = 6·2 = 12 V.
- **Voltage follower:** the output is connected to the inverting input; from e3 = A0(e2 − e1) and e1 = e3, when A0 is very large, e2 = e1 = e3. The gain is 1, the effective input impedance is Z_et = (1 + 1/A0)/(1/A0), that is, magnified approximately A0 times, and the output impedance is very low. For this reason it is used as a "buffer" to connect a circuit with a high output impedance to a circuit with a low input impedance.
- **Summing amplifier:** V0 = −R_f(V1/R1 + V2/R2 + … + Vn/Rn). If R_f = R1 = R2 = … is chosen, the inputs are summed without amplification: for example, for V1 = 5 V, V2 = 5 V, Vn = −1 V, V0 = −9 V.
- **Difference amplifier:** amplifies the difference between the two inputs; if R1 = R2 and R3 = R_f, then V0 = (R_f/R1)(V2 − V1). Example: for R1 = R2 = 20 kΩ, R3 = R_f = 40 kΩ, V1 = 2 V, V2 = 8 V, V0 = 2·(8 − 2) = 12 V.
- **Comparator:** even a small difference between the inputs is multiplied by the open-loop gain (approximately 200,000); if Vi > Vref, V0 ≈ +V, and if Vi < Vref, V0 ≈ −V. If a TTL circuit is to be driven, a diode is added to the output.

## Integrator and Differentiator Circuits

- **Integrator:** a capacitor in the feedback path and a resistor at the input: V0 = −(1/RC)∫V_i dt. The reactance of the capacitor is X_C = 1/(2πfC).
- **Differentiator:** the positions of the resistor and capacitor in the integrator circuit are swapped: V0 = −RC·dV_i/dt. The transfer function and applications (including circuits with diodes) are given.

## Op-Amp Filters

- **Low-pass filter:** upper cutoff frequency f_OH = 1/(2πRC) (condition R = X_C).
- **High-pass filter:** lower cutoff frequency f_OL = 1/(2πRC).
- **Band-pass filter:** by cascading high-pass and low-pass sections. Example: for R1 = R3 = 10 kΩ, C1 = 0.01 µF, C2 = 0.001 µF, the lower cutoff frequency is 1/(2π·10 kΩ·0.01 µF) ≈ 1.59 kHz, and the upper cutoff frequency is 1/(2π·10 kΩ·0.001 µF) ≈ 15.9 kHz.

## Oscillators

Op-amp phase-shift RC oscillator, Wien bridge oscillator, and crystal-controlled oscillator circuits, and their operating frequencies.

## Questions

At the end of each section there are example questions, three sets of test questions (with answer keys), 10 solved problems, and questions on the cutoff frequencies of filters.

## Downloadable File

The original 58-page PDF can be downloaded below.
