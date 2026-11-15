---
baslik: EEM311 Electronics II: 2008 Laboratory Preliminary Work and Reports, Experiments 5–8 (Current Mirror, Active Load, Differential Amplifier, Frequency Response)
ozet: Student preliminary work and reports from the EEM311 Electronics II laboratory, Fall 2008, Experiments 5–8: CD4007 current mirror Io–Vcc2 measurements and output resistance, CMOS amplifier with active load, 2N3904 differential amplifier (Avdm, Avcm, CMRR), and the frequency response of a common-emitter amplifier.
---

This post contains student work for the last four experiments of the **Fall 2008** laboratory of the **EEM311 Electronics II** course in the Electrical-Electronics Engineering Department at Başkent University: PSpice preliminary work, hand-calculated preliminary work, and lab reports (November–December 2008). For Experiments 7 and 8, there is work from two different students. All of it is **work by classmates; personal information has been removed.** The handwritten preliminary work pages for Experiments 6, 7 and 8 were transcribed to text from photographed pages. The experiment handouts are in separate posts in the archive (Experiments 5–6 and Experiments 7–8). Personal-information-free PDF copies can be downloaded as a ZIP at the end of the post.

## Experiment 5: MOSFET Current Mirror

### Preliminary Work (PSpice)

Bias simulation and hand-calculation comparison for the mirror built with the CD4007 (V_CC1 = V_CC2 = 5 V, R = 1 kΩ):

| | PSpice | Preliminary work (by hand) |
|---|---|---|
| V_D1 | 3.566 V | 3.72 V |
| V_D2 | 5.000 V | 5.000 V |
| V_G1 = V_G2 | 3.566 V | 3.72 V |
| I_D1 = I_REF | 1.434 mA | 1.28 mA |
| I_D2 = I_O | 1.444 mA | 1.29 mA |

A DC sweep of V_CC2 from 0 to 8 V was performed; beyond a few volts, I_O settles at a value close to I_REF.

### Report

Measured values: V_D1 = 3.278 V, V_G1 = 3.277 V, I_D1 = I_REF = 1.79 mA; V_D2 = 5.069 V, V_G2 = 3.277 V, I_D2 = I_O = 1.88 mA. It can be seen that V_G1 = V_G2 and I_REF ≈ I_O.

Output current measured while varying V_CC2 from 0 to 8 V:

| V_CC2 (V) | I_O (mA) | V_CC2 (V) | I_O (mA) |
|---|---|---|---|
| 0.00 | 0.025 | 2.75 | 1.841 |
| 0.25 | 0.745 | 3.00 | 1.845 |
| 0.50 | 1.180 | 3.25 | 1.850 |
| 0.75 | 1.498 | 3.50 | 1.855 |
| 1.00 | 1.665 | 3.75 | 1.860 |
| 1.25 | 1.761 | 4.00 | 1.864 |
| 1.50 | 1.789 | 4.50 | 1.872 |
| 1.75 | 1.811 | 5.00 | 1.880 |
| 2.00 | 1.820 | 6.00 | 1.892 |
| 2.25 | 1.827 | 7.00 | 1.905 |
| 2.50 | 1.833 | 8.00 | 1.915 |

Report's interpretation: I_O begins to level off after 1.5–1.75 V because M2 enters saturation beyond this voltage; at smaller voltages the current drops because the transistor is in the triode region.

Output resistance from the V_CC2 = 4 V and 6 V measurements: R_o = ΔV/ΔI = (6 − 4) V / (1.892 − 1.864) mA; in the preliminary work this value was found to be **81 kΩ**.

*Note: The report does not state a result; with the given values, R_o = 2 V / 0.028 mA ≈ 71.4 kΩ.*

## Experiment 6: CMOS Common-Source Amplifier with Active Load

### Preliminary Work

The handwritten pages (transcribed from photographs) contain the small-signal AC equivalent (Q3–Q2 PMOS mirror with resistances r_o3, r_o2 and g_m·v_gs sources, Q1's g_m1·v_gs1 source, r_o1, R_g and R_L), and the gain was calculated as follows:

- v_out = −g_m1·v_gs1·(r_o1 ∥ R_L), v_in = v_gs1
- g_m1 = 2I_D / (V_GS1 − V_TN) = 2·0.64 mA / (3.03 − 1.45) V ≈ 0.81 mA/V
- A_v = −g_m·R_L = −0.81 mA/V × 100 kΩ ≈ **−81**

*Note: The r_o's were neglected in the last step. With λ = 0.01 V⁻¹, r_o1 ≈ r_o2 ≈ 100 V / 0.6 mA ≈ 167 kΩ; if r_o1 ∥ r_o2 ∥ R_L ≈ 45 kΩ is taken at the output, A_v ≈ −37, which is much closer to the PSpice result (−40).*

PSpice preliminary work (V_CC = 15 V, R_REF = 25.42 kΩ, R_g = 1 MΩ, R_L = 100 kΩ, 25 mV peak input, 5 kHz):

- Bias: source current 1.058 mA, R_REF current 500.5 µA, NMOS current 557.4 µA, V_G = V_D = 2.754 V.
- Transient simulation: v_in = 25 mV (peak), v_out = 1.018 V (peak), **A_v = −40**.
- When R_REF is replaced with the diode-connected NMOS Q4: the current rises to 12.61 mA, V_G = V_D = 7.756 V; v_out = 468 mV (peak), **A_v ≈ 18.7** (in magnitude).

### Report

1. R_REF was adjusted with a potentiometer to I_REF = 0.6 mA: **R_REF = 25.33 kΩ**, I_O = I_D = 0.86 mA, V_A = 13.20 V, V_G = 2.78 V, V_D = 2.79 V.
1. From the oscilloscope measurement, A_v = −2.04 V / 75.2 mV ≈ **−27.2**.
1. The R_in (R_x = 50 kΩ pot) line and the final discussion question were left blank.

## Experiment 7: BJT Differential Amplifier

### Preliminary Work, First Student

Handwritten calculations (transcribed from photographs), for Figure 5 in the handout (V_CC = 15 V, V_EE = −15 V, R_A = R_B = 2.2 kΩ, R_E = 250 Ω, β = 100, V_BE = 0.7 V):

- I_CQA = I_CQB = 2 mA, I_CQ1 = I_CQ2 = 1 mA, target V_CE1 = V_CE2 = 6 V.
- I_CQA·R_REF + V_CEA + I_CQA·R_A = 15 V → 2 mA·R_REF + 0.7 + 4.4 − 15 = 0 → **R_REF = 4.95 kΩ**
- With the inputs grounded, V_E1 = V_E2 = −0.7 V; for V_CE = 6 V, V_C = 5.3 V; 5.3 = 15 − 1 mA·R_C → **R_C = 9.7 kΩ**
- g_m = I_CQ1 / V_T = 1 mA / 25 mV = 0.04 S
- A_vdm-diff = −g_m·R_C / (1 + g_m·R_E) = −0.04·9.7 k / (1 + 0.04·250) = **−35.27**
- A_vdm-se1 = −g_m·R_C / [2(1 + g_m·R_E)] = **−17.64**, A_vdm-se2 = **+17.64**
- V_E = I_CQ1·R_E + I_CQB·R_EE − 15 = −0.7 V gives **R_EE = 7.025 kΩ**
- A_vcm-se1 = −g_m·R_C / (1 + g_m·R_E + 2g_m·R_EE) = **−0.68**
- CMRR = R_EE / (1/g_m + R_E) = 7.025 k / (25 + 250) = **25.6**
- rπ = β·V_T / I_CQ = 2.5 kΩ; R_idm = 2rπ(1 + g_m·R_E) = 2·2.5 k·11 = **55 kΩ**
- R_icm = v_icm / (2i_b) = rπ(1 + g_m·R_E + g_m·R_EE)/2 = **365 kΩ**

*Note: In the R_icm calculation, g_m·R_EE is used in the denominator, as in the first expression in the handout. Since the currents of the two halves flow together through R_EE, the correct term is 2g_m·R_EE; then R_icm = 2.5 k·(1 + 10 + 562)/2 ≈ 716 kΩ.*

With PSpice (R_C = 9.7 kΩ, R_REF = 4.95 kΩ):

- Bias: V_CE1 = V_CE2 = 6.11 V, I_CQ1 = I_CQ2 = 991.3 µA ≈ 1 mA, I_CQA = 1.994 mA, I_CQB = 1.995 mA. The report states that the values are very close to the calculations in the preliminary work and that the design is correct.
- v_in1 = 50 mV, v_in2 = −50 mV (peak), 1 kHz: v_out1 and v_out2 = 3.407 Vp-p (opposite phase), v_odm = 6.813 Vp-p, v_idm = 198.092 mVp-p → **A_vdm-diff = −34.394, A_vdm-se1 = −17.2, A_vdm-se2 = 17.2**.
- 4 V peak, 1 kHz applied to both inputs (common mode): v_out1 = v_out2 = 8.1 mVp-p, v_icm = 7.9238 Vp-p.

*Note: In the document, v_in1 is written as "Vp-p = 99.046 V"; the unit should be mV. The common-mode gain is also given as "7.5153 × 10⁻⁶"; 8.1 mV / 7.9238 V ≈ 1.0 × 10⁻³.*

### Preliminary Work, Second Student (PSpice)

Circuit built with standard resistors (R_C = 10 kΩ, R_REF = 5.1 kΩ) and 100 µF capacitors on the supply rails:

- Bias: V_CE1,2 = 5.359 V − (−0.663 V) = **6.022 V**, I_CQ1,2 = 964.1 µA, I_CQA,B = 1.939 mA.
- With ±50 mV peak inputs: v_out1 = −3.54 Vp-p, v_out2 = 3.54 Vp-p, v_odm = 7.08 Vp-p, v_idm = 200 mVp-p → A_vdm-diff = −35.4, A_vdm-se1 = −17.7, A_vdm-se2 = 17.7.
- With a 4 V peak common-mode input: v_out1 = v_out2 = 8.4 mVp-p, v_icm = 7.96 Vp-p → A_vcm-se ≈ −0.001.

Comparison table with the hand calculations (by hand R_C = 9.7 kΩ, R_REF = 4.88 kΩ):

| | Hand calculation | PSpice |
|---|---|---|
| A_vdm-diff | −36.36 | −35.4 |
| A_vdm-se1 | −18.18 | −17.7 |
| A_vdm-se2 | 18.18 | 17.7 |
| R_EE | 7.025 kΩ | |
| CMRR | 25.5 | |
| A_vcm-se1 | −0.69 | −0.001 |
| R_idm | 55 kΩ | |
| R_icm | 365 kΩ | |

### Report, First Student

The circuit was built with V_CC = 15 V, V_EE = −15 V, R_A = R_B = 2.2 kΩ, C = 100 µF, R_POT = 500 Ω; the standard **10 kΩ** was used for R_C.

1. With the inputs grounded (capacitors not installed): I_CQA = 1.979 mA, I_CQB = 2.005 mA, V_CE1 = 6.042 V, V_CE2 = 6.480 V, I_CQ1 = 1.005 mA, I_CQ2 = 0.938 mA, V_C1 = 4.310 V, V_C2 = 5.780 V.
1. v_in1 = 100 mVp-p, 1 kHz, v_in2 grounded: v_out1 = 1.45 V, v_out2 = 1.52 V → A_vdm-se1 = 14.5, A_vdm-se2 = 15.2.
1. v_in2 = 100 mVp-p, v_in1 grounded: v_out1 = 1.63 V, v_out2 = 1.50 V → A_vdm-se1 = −16.3, A_vdm-se2 = −15.0.
1. Using the oscilloscope's math menu, CH1 − CH2: v_out1 − v_out2 = 2.94 V → **A_vdm-diff = 29.4**.

*Note: In the document, the unit of I_CQA is written as "V" (should be mA). In the calculation for step 3, the numerator is written as 1.45; the result −16.3 is obtained with v_out1 = 1.63 V.*

### Report, Second Student

1. DC (inputs grounded): I_CQA = 1.963 mA, I_CQB = 1.971 mA, V_CE1 = 6.045 V, V_CE2 = 6.042 V, I_CQ1 = 0.965 mA, I_CQ2 = 0.967 mA, V_C1 = 5.412 V, V_C2 = 5.411 V.
1. v_in2 grounded, 100 mVp-p, 1 kHz applied to Q1: v_out1 = −1.83 Vp-p, v_out2 = 1.81 Vp-p → A_vdm-se1 = −18.35, A_vdm-se2 = 18.15.
1. v_in1 grounded, the same signal applied to Q2: v_out1 = 1.83 Vp-p, v_out2 = −1.81 Vp-p → A_vdm-se1 = 18.35, A_vdm-se2 = −18.15.
1. With CH1 − CH2, v_odm = −3.64 V → **A_vdm-diff = −36.4**.
1. 8 Vp-p, 1 kHz applied to both inputs: v_out1 = −4.21 mV, v_out2 = −4.18 mV → A_vcm-se1 = −0.000526, A_vcm-se2 = −0.000522.
1. The student wrote that, while preparing the report, they noticed they had used A_vdm-diff instead of A_vdm-se when calculating CMRR in the lab, and corrected it: **CMRR = A_vdm-se / A_vcm-se = 18.35 / 0.000526 ≈ 34 886**.
1. Reasons why the measured currents and voltages differ slightly from the calculated ones: the β values of the transistors in the simulation and in the experiment differ, and R_E could not be set to exactly 250 Ω on both sides with the potentiometer.

| | Preliminary work (PSpice) | Experiment |
|---|---|---|
| A_vdm-se1 / A_vdm-se2 | −17.7 / 17.7 | −18.35 / 18.15 |
| A_vdm-diff | −35.4 | −36.4 |
| A_vcm-se | −0.001 | −0.000526 |

## Experiment 8: Frequency Response of a Common-Emitter Amplifier

### Preliminary Work, First Student (by hand, transcribed from photographs)

For the circuit in the handout (V_CC = 12 V, R1 = 8.2 kΩ, R2 = 3.9 kΩ, R_C = 6.3 kΩ, R_E = 3.3 kΩ, R_s = 3 kΩ, R_L = 3.9 kΩ, 2N3904, β = 100):

- V_B = 3.9 k / 12.1 k · 12 = 3.9 V; 3.9 = 0.7 + I_E·3.3 k → I_E = 0.967 mA, I_C = β/(β+1)·I_E = **0.957 mA**, I_B = **9.57 µA**
- 12 = I_C·R_C + V_CE + I_E·R_E → **V_CE = 2.67 V**; Q point (0.957 mA, 2.67 V)
- R_B = R1 ∥ R2 = 2.64 kΩ, rπ = β·V_T / I_C = 2.61 kΩ, **R_in = R_B ∥ rπ = 1.31 kΩ**
- r_o = (V_CE + V_A)/I_C = 107.3 kΩ, **R_out = R_C ∥ r_o = 5.95 kΩ**
- A_v-mid = R_in/(R_in + R_s) · (−g_m·(R_C ∥ R_L)) = **−27.3**
- Short-circuit time constants: for C1, R_1s = R_s + (R_B ∥ rπ) = 4.2 kΩ → 23.8 rad/s; for C2, R_2s = R_L + (R_C ∥ r_o) = 7.87 kΩ → 127.1 rad/s; for C_E, R_3s = R_E ∥ [(rπ + R_th)/(β+1)] = 39.5 Ω → 253.2 rad/s. ω_L = 404.1 rad/s → **f_L = 64.4 Hz**
- Open-circuit time constant: R_eq = [(R_s ∥ R_B) + r_x] ∥ rπ = 0.96 kΩ, C = C_π + C_µ(1 − A_v) = 238.7 pF → ω_H = 4.37 × 10⁶ rad/s, **f_H = 695.9 kHz**
- Bandwidth **BW = f_H − f_L ≈ 695.8 kHz**

### Preliminary Work, PSpice Results

The first student's simulation (with C_E = 10 µF, a table value left over from the handout of 2005):

- Bias: V_CE = 2.779 V, I_BQ = 7.078 µA, I_CQ = 958.1 µA.
- 1 kHz transient analysis: v_in = 19.81 mVp-p, v_out = 544.13 mVp-p, A_v = 27.839.
- AC sweep: midband ≈ 27.28 dB; the 3 dB points are **f_L ≈ 41.5 Hz, f_H ≈ 851.1 kHz**.
- With C_E removed: v_out = 6.65 mVp-p, A_v = 0.337; the cursors show 16.1 Hz and 601.174 M(Hz).

Report's interpretation: when C_E is removed, there is a large drop in gain; the lower and upper cutoff frequencies also change.

*Note: 544.13 / 19.81 ≈ 27.47; the 27.839 in the document is slightly different.*

The second student (C_E = 100 µF) found the same bias values; with a 10 mV peak input, v_out = 289.2 mV peak, **A_v = −28.9**. Comparison table:

| | Hand calculation | PSpice (with C_E) | PSpice (without C_E) |
|---|---|---|---|
| I_BQ | 9.29 µA | 7.078 µA | |
| I_CQ | 0.929 mA | 958.1 µA | |
| V_CEQ | 3.06 V | 2.78 V | |
| A_mid | −27.26 | −28.9 | −0.32 |
| f_L | 60.2 Hz | 41.5 Hz | 16.1 Hz |
| f_H | 694 kHz | 851.2 kHz | 601.17 kHz |

### Report

The circuit was built according to Figure 2 in the handout (the report states C_E = 10 µF). Transistor data: V_BE(ON) = 0.7 V, V_A = 100 V, r_x = 100 Ω, C_π = 13.9 pF, C_µ = 8 pF, n = 1, V_T = 25 mV.

1. DC measurements: I_BQ = 0.071 mA, I_CQ = 0.954 mA, V_CEQ = 3.07 V.
1. v_s = 20 mVp-p, 1 kHz: v_in = 18.8 mV, v_out = 432 mV (10 mV/div and 200 mV/div, 500 µs/div) → **A_v-mid = 23.0**. In the subsequent measurements, v_in = 32.8 mV was used for ease of observation.
1. The cutoff frequencies are given as **f_H = 425 kHz**, f_L = 3.87 Hz. Frequency sweep (A_v = v_out / 32.8 mV):

| Frequency | v_out (peak) | A_v |
|---|---|---|
| 30 Hz | 56.0 mV | 1.707 |
| 40 Hz | 72.0 mV | 2.195 |
| 50 Hz | 96.0 mV | 2.927 |
| 80 Hz | 152 mV | 4.634 |
| 150 Hz | 272 mV | 8.293 |
| 200 Hz | 344 mV | 10.488 |
| 250 Hz | 400 mV | 12.195 |
| 300 Hz | 456 mV | 13.902 |
| 20 kHz | 864 mV | 26.341 |
| 60 kHz | 856 mV | 26.097 |
| 120 kHz | 824 mV | 26.122 |
| 200 kHz | 752 mV | 22.927 |
| 500 kHz | 480 mV | 14.634 |
| 750 kHz | 352 mV | 10.732 |
| 1 MHz | 272 mV | 8.293 |
| 1.3 MHz | 208 mV | 6.342 |
| 1.5 MHz | 184 mV | 5.609 |

The graph was plotted in Excel with evenly spaced "logarithmic" sequence numbers on the x-axis.

- **Step 4:** When C_E is removed, the midband gain drops significantly: **A_v-mid = 0.333**, f_H = 722 kHz, f_L = 132 Hz.
- **Step 5:** With a 5 kΩ pot, **R_in = 3.688 kΩ**.
- **Step 6:** With a 10 kΩ pot, **R_out = 6.12 kΩ**.

*Note: 0.954 mA is 954 µA, not 95.4 µA as written in the report. In the 120 kHz row, 824 / 32.8 ≈ 25.12 should be the value. Since the gain in the table is only about half the midband value (≈ 26.3) even at 300 Hz, the lower cutoff frequency is around a few hundred hertz; "3.87 Hz" was most likely meant to be 387 Hz.*

## Unpublished Files

The PSpice project and simulation files in the folder (.opj, .DSN, .DBK, .sim, .out, .dat, etc.) were not included in the post; the photographs of the handwritten preliminary work were only transcribed to text and are not in the download file.
