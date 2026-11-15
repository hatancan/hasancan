---
baslik: EEM311 Electronics II: 2010 Laboratory Preliminary Work and Reports, Experiments 5–7 (Current Mirror, Active Load, Differential Amplifier)
ozet: Student preliminary work and reports from the fall 2010 EEM311 Electronics II laboratory, Experiments 5–7: I_o–V_CC2 measurement and 80 kΩ output resistance of a CD4007 current mirror, gain of a CMOS amplifier with active load, and 2N3904 differential amplifier measurements (CMRR ≈ 41,400).
---

This post contains student work for Experiments 5, 6, and 7 of the **fall 2010** laboratory of **EEM311 Electronics II** in the Electrical-Electronics Engineering Department at Başkent University (December 2010): PSpice preliminary work and experiment reports. **This is a friend's work; personal information has been removed.** In the 2010 schedule, Experiment 8 (frequency response) was not performed. The experiment handouts are in the archive as separate posts (Experiments 5–6 and Experiments 7–8). Personal-information-free PDF copies can be downloaded as a ZIP at the end of the post.

## Experiment 5: MOSFET Current Mirror

### Preliminary Work (PSpice)

In the DC analysis, I_REF = 1.434 mA, I_O = 1.444 mA, V_GS1 = V_DS1 = V_GS2 = 3.566 V, V_DS2 = 5 V; the student noted that these values are very close to the hand calculations in the preliminary work. In the 0–8 V sweep of V_CC2, I_O settles at around 1.4 mA after about 1.5 V.

### Report

The report describes the current mirror as follows: a circuit that copies the reference current applied to its input to the other branches, either identically or in certain ratios; in theory it is regarded as a current source, but in practice it is not always one. The **CD4007** used (Dual Complementary Pair Plus Inverter) contains three n-channel and three p-channel enhancement-mode MOS transistors and has 14 pins; its inputs are protected against static charge by diodes. The circuit was built with the CD4007, a 1 kΩ resistor, and thin wires, and both supplies were set to 5 V.

1. V_D1 = 3.450 V, V_G1 = 3.408 V, I_D1 = 1.630 mA, I_REF = 1.617 mA; V_D2 = 5.085 V, V_G2 = 3.420 V, I_D2 = 1.650 mA, I_O = 1.623 mA.
1. I_O was measured while V_CC2 was varied from 0 to 8 V; after 1.25 V the current approaches a constant value:

| V_CC2 | I_O | V_CC2 | I_O |
|---|---|---|---|
| 0 V | 0 mA | 3.25 V | 1.689 mA |
| 0.25 V | 0.570 mA | 3.5 V | 1.692 mA |
| 0.5 V | 1.041 mA | 3.75 V | 1.697 mA |
| 0.75 V | 1.270 mA | 4 V | 1.698 mA |
| 1 V | 1.550 mA | 4.5 V | 1.706 mA |
| 1.25 V | 1.594 mA | 5 V | 1.712 mA |
| 1.5 V | 1.640 mA | 5.5 V | 1.718 mA |
| 1.75 V | 1.650 mA | 6 V | 1.723 mA |
| 2 V | 1.660 mA | 6.5 V | 1.727 mA |
| 2.25 V | 1.665 mA | 7 V | 1.732 mA |
| 2.5 V | 1.674 mA | 8 V | 1.741 mA |
| 2.75 V | 1.680 mA | | |
| 3 V | 1.685 mA | | |

- **Item 3:** Output resistance: R_O = (6 − 4) V / [(1.723 − 1.698) mA] = **80 kΩ**. Because the output current varies with V_DS, the current source behaves as if it had a resistive element in parallel.

*Note: Item 2 of the report states that the MOSFET operates "in the triode (linear) region" in this measurement; this is correct only for the small voltages (up to ≈ 1.25 V) where the current rises rapidly; in the region where the current levels off, M2 operates in saturation.*

## Experiment 6: CMOS Common-Source Amplifier with Active Load

### Preliminary Work (PSpice)

With R_REF = 25 kΩ: the transistor currents are 0.566 mA, 0.566 mA, and 0.509 mA; the corresponding V_DS values are 2.764 V, −12.236 V, and −2.29 V; in the transient simulation the gain is **−41.456**. When R_REF is replaced by an NMOS (Q4), 12.61 mA flows through all branches, the V_DS values are 7.756 V, −7.244 V, −7.244 V; the gain is **−19.632**. In each case, which transistor is in triode and which is in saturation has been marked.

*Note: Part e of the preliminary work states "an increase in gain was observed when R_REF was replaced by an NMOS"; according to the results, the gain drops from −41.5 to −19.6.*

### Report

The circuit was built with the CD4007, 1 MΩ and 100 kΩ resistors, a 100 kΩ pot, and two 10 µF capacitors; the supply is 15 V, the signal is 5 kHz, 50 mV.

1. R_REF was adjusted with the pot: **R_REF = 25 kΩ**, I_O = I_D = 0.82 mA, V_A = 13.01 V, V_G = 2.67 V, V_D = 2.80 V. Very close to the preliminary work; the differences are due to resistor tolerance and measurement precision.
1. Oscilloscope measurement: A_v = v_out / v_in = 1.47 V / 48.4 mV ≈ **−29.7** (the input could not be set to exactly 50 mV; input and output are out of phase).
1. With the pot method, **R_in = 58.3 kΩ**.
1. Advantage of the active load: since the output resistance is high, a larger gain is obtained; also, since no resistor is used, the area that large resistors would occupy in integrated circuits is saved.

*Note: 1.47 V / 48.4 mV ≈ 30.4; the report states 29.7.*

## Experiment 7: BJT Differential Amplifier

### Preliminary Work (PSpice)

R_REF = 5 kΩ, R_C = 9.7 kΩ, R_E = 250 Ω, R_A = R_B = 2.2 kΩ, V_CC = 15 V, V_EE = −15 V:

| Quantity | Value |
|---|---|
| I_CQ1,2 | 0.978 mA |
| I_CQA,B | 1.980 mA |
| V_CE1,2 | 6.181 V |
| A_vdm-diff | −34.372 |
| A_vdm-se1 / A_vdm-se2 | −18.226 / 18.226 |
| v_idm (p-p) | 99.046 mV |
| A_vcm-se1 = A_vcm-se2 | −3.8495 |

*Note: In the PSpice expression used for the common-mode gain, the two outputs were multiplied (V(RC1:1)*V(RC2:1)); the result of −3.85 is therefore meaningless, and the value measured in the experiment is around 0.0005. Also, the document reads 7.2055 Vp-p for v_out1,2 and 3.3976 Vp-p for v_odm; with A_vdm-diff = −34.4 and v_idm ≈ 99 mV, v_odm ≈ 3.40 V, and the single-ended outputs should be half of that (≈ 1.7 Vp-p), so the 7.2055 V value is inconsistent.*

### Report

The report describes the differential amplifier as follows: it has two inputs and two outputs; the input signals are applied to the bases of the two transistors, and the outputs are taken from the collectors. R_E is the common emitter resistor of both transistors; R_C1 and R_C2 are the collector load resistors, and without them +V_CC would always be taken from the collector instead of the amplified signal. If PNP transistors were used, the signs of +V_CC and −V_EE would be swapped. The circuit was built with four 2N3904s, two 100 µF capacitors, two 2.2 kΩ resistors, and 500 Ω and 10 kΩ pots; 10 kΩ was used for R_C, and the supplies are ±15 V.

1. DC (inputs grounded, capacitors removed; R_POT adjusted so that V_CE1,2 ≈ 6 V): I_CQA = I_CQB = 2.01 mA, V_CE1 = 5.651 V, V_CE2 = 5.652 V, I_CQ1 = 1.05 mA, I_CQ2 = 1.03 mA, V_C1 = 4.973 V, V_C2 = 4.974 V.
1. With v_in2 grounded and 100 mVp-p, 1 kHz applied to Q1: v_out1 = −2.07 V, v_out2 = 2.07 V → A_vdm-se1 = **−20.7**, A_vdm-se2 = **20.7**.
1. With v_in1 grounded and the same signal applied to Q2: v_out1 = 2.07 V, v_out2 = −2.07 V → A_vdm-se1 = 20.7, A_vdm-se2 = −20.7.
1. Using the oscilloscope's Math menu, CH1 − CH2: v_odm = −4.09 V → **A_vdm-diff = −40.9**.
1. With 8 Vp-p, 1 kHz applied to both inputs: v_out1 = v_out2 = 4 mV → A_vcm-se1 = A_vcm-se2 = 4 mV / 8 V = **0.0005**.
1. **CMRR = A_vdm-se / A_vcm-se = 20.7 / 0.0005 = 41.4 k** (≈ 41,400).
1. The reasons for the differences between measurements and calculations: the β of the transistors in the experiment differs from that in the simulation, and R_E could not be set to exactly 250 Ω on both sides with the potentiometer (one of the transistors invariably carries more current).

| | Preliminary work | Experiment |
|---|---|---|
| A_vdm-se1 / A_vdm-se2 | −18.226 / 18.226 | −20.7 / 20.7 |
| A_vdm-diff | −34.372 | −40.9 |
| A_vcm-se | −3.8495 | 0.0005 |

## Unpublished Files

The PSpice project files for this term were not in the folder; there were only Word documents.
