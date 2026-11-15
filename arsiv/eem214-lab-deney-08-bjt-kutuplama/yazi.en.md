---
baslik: EEM214 Electronics I: Experiment 8 – BJT Biasing Circuits and Stability Against β (Lab Sheet and Student Reports)
ozet: Experiment 8 lab sheet from the 2006 EEM214 Electronics I laboratory: fixed bias, emitter-resistor bias, collector-feedback bias and voltage-divider bias; resistor design for I_C = 6 mA, β measurement with the 2N3903, 2N3904 and BC238B, and a stability ranking of the circuits based on the percentage variation of I_CQ.
---

This post contains the **Experiment 8: BJT Biasing** lab sheet (February 2006) from the Başkent University **EEM 214 Electronics I** laboratory, along with student reports prepared for this experiment. The reports are the work of classmates; names and student numbers have been blacked out. Since the lab sheet is in English, its text is reproduced in English. A password-free copy of the lab sheet and the reports can be downloaded as a ZIP at the end of the post.

## Lab Sheet: Experiment 8 – BJT Biasing

**Aim:** To examine the different methods of setting the DC operating point (Q-point, quiescent operating point) of a transistor, to determine the most effective configuration for providing good stability with respect to changes in β, and to understand how a change of β in a transistor circuit changes the Q-point.

**Theory:** In order to use a transistor in an amplifying circuit it has to be biased; the purpose of biasing is to set the DC levels of the transistor currents and voltages (I_B, I_C, I_E and V_B, V_C, V_E). For linear applications the bias circuit must keep the transistor in the active state over the required range of input and output signals. An important issue is bias stability: β may vary significantly from transistor to transistor and with temperature, so the Q-point has to be stabilized against β variations.

The four circuits in the lab sheet (all with V_CC = 15 V, R_C = 1 kΩ):

- **Fig. 1 – fixed bias:** the base is connected to V_CC through R_B, the emitter is grounded.
- **Fig. 2 – emitter-resistor bias:** Fig. 1 with R_E = 100 Ω added.
- **Fig. 3 – collector-feedback bias:** the base is connected to the collector through R_F.
- **Fig. 4 – voltage-divider bias:** R2 (upper) and R1 = 2.2 kΩ (lower) form the divider, R_E = 100 Ω.

### Preliminary work

1. Review Section 5.12 of the textbook.
1. Explain why biasing is needed in transistor amplifier circuits.
1. For each circuit of Fig. 1–4: a) obtain the equations for I_B, I_C and V_CE; b) for β = 200 calculate the specified resistor (R_B, R_B, R_F, R2 respectively) to give I_C = 6 mA; c) with this resistor calculate I_C for β = 100 and β = 300.
1. Calculate the range of variation of I_CQ for each circuit as a percentage of the medium-β value, % range = 100·(I_CQ,high − I_CQ,low) / I_CQ,medium, and rate the circuits from most stable to least stable.
1. Read the experimental work.

### Experimental work

1. Measure the actual values of the resistors (1 kΩ, 100 Ω, 2.2 kΩ, 47 kΩ).
1. Build Fig. 1 with R_B = 470 kΩ and use it to find β of each of the three transistors (2N3903, 2N3904, BC238B) from V_CC, V_C and V_B. One should be below 100, one above 300 and one near the middle; the medium-β transistor is used to design the four circuits.
1. With the medium β, calculate the resistors for I_C = 6 mA (V_BE = 0.65 V, I_B = 6 mA/β): Fig. 1: R_B = (V_CC − V_BE)/I_B; Fig. 2: R_B = (V_CC − V_BE − I_C·R_E)/I_B; Fig. 3: R_F = (V_CE − V_BE)/I_B with V_CE = V_C = V_CC − I_C·R_C; Fig. 4: R2 = (V_CC − V_BE − I_C·R_E)/(I_R1 + I_B), where I_R1 = V_B/R1 = (V_BE + I_C·R_E)/R1.
1. For each circuit build it with the medium-β transistor, measure V_C and calculate I_CQ = (V_CC − V_C)/R_C, adjusting the bias resistor until V_C = 9 V ± 0.5 V; then replace the transistor with the low-β and high-β ones and repeat.
1. a) Calculate the % range of I_CQ for each circuit. b) Rate the circuits and discuss how the Q-point varies with β. c) Is there any difference between the theoretical and experimental order? Why?
1. What effect does adding an emitter resistor to the bias circuit have on bias stability? What should its value be to make the collector current less dependent on β?

**Components:** 500 kΩ potentiometer, 1 kΩ, 100 Ω, 2.2 kΩ, 2N3903, 2N3904, BC238B.

## Student Reports

### β measurement (Fig. 1, R_B = 470 kΩ)

| Transistor | V_C (A) | V_B (A) | β (A) | V_C (B) | V_B (B) | β (B) |
|---|---|---|---|---|---|---|
| 2N3903 | 13.242 V | 0.680 V | 54.77 | 12.951 V | 0.669 V | 68.33 |
| 2N3904 | 10.444 V | 0.712 V | 154.45 | 10.29 V | 0.715 V | 157 |
| BC238B | 4.132 V | 0.697 V | 365.7 | 4.2 V | 0.695 V | 360 |

In both reports the medium-β transistor turned out to be the 2N3904 (β ≈ 155).

*Note: In the calculations of Report A the units are mixed up (for example, I_C = 1.88 A and I_B = 34.32 mA are written); the correct values are I_C = (15 − 13.242)/972 Ω ≈ 1.81 mA and I_B = (15 − 0.68)/471.2 kΩ ≈ 30.4 µA, which gives β ≈ 59. The β values of the other two transistors (154, 366) remain the same once the units are corrected.*

### Designed resistors (I_C = 6 mA)

| Circuit | Report A (β = 154.45) | Report B (β = 157) |
|---|---|---|
| Fig. 1, R_B | 369.8 kΩ | 375.5 kΩ |
| Fig. 2, R_B | 354.8 kΩ | 359.8 kΩ |
| Fig. 3, R_F | 368.8 kΩ | 218.5 kΩ |
| Fig. 4, R2 | 27.2 kΩ | 22.7 kΩ |

*Note: In Fig. 3, since V_CE = V_C = 15 − 6 mA × 1 kΩ = 9 V, R_F = (9 − 0.65)/(6 mA/β); for β = 157 this is ≈ 218 kΩ (Report B is correct). In Report A, V_C was mistakenly taken as 14.96 V. In Fig. 4, with I_R1 = (0.65 + 0.6)/2.2 kΩ ≈ 0.568 mA, R2 = 13.75 V / (0.568 + 0.038) mA ≈ 22.7 kΩ.*

### Measured I_CQ and stability

| Circuit | β | V_C (A) | I_CQ (A) | V_C (B) | I_CQ (B) |
|---|---|---|---|---|---|
| Fig. 1 | low | 13.372 V | 2.628 mA | 12.060 V | 2.94 mA |
| Fig. 1 | medium | 8.993 V | 6 mA | 9.148 V | 5.852 mA |
| Fig. 1 | high | 1.400 V | 13.6 mA | 2.146 V | 12.854 mA |
| Fig. 2 | low | 12.411 V | 2.589 mA | 11.922 V | 3.078 mA |
| Fig. 2 | medium | 9.245 V | 5.755 mA | 9.126 V | 5.874 mA |
| Fig. 2 | high | 2.576 V | 12.424 mA | 2.806 V | 12.194 mA |
| Fig. 3 | low | 11.302 V | 3.698 mA | 12.312 V | 2.688 mA |
| Fig. 3 | medium | 9.003 V | 5.997 mA | 9.35 V | 5.65 mA |
| Fig. 3 | high | 5.808 V | 9.192 mA | 6.140 V | 8.86 mA |
| Fig. 4 | low | 9.315 V | 5.685 mA | 9.96 V | 5.14 mA |
| Fig. 4 | medium | 9.297 V | 5.703 mA | 9.074 V | 5.926 mA |
| Fig. 4 | high | 9.016 V | 5.991 mA | 9.09 V | 6.03 mA |

I_CQ percentage variations: in Report A, Fig. 1 is 182%, Fig. 2 171%, Fig. 3 92%, Fig. 4 5%; in Report B, Fig. 1 is 169%, Fig. 2 155%, Fig. 3 109%, Fig. 4 15%. Both reports reach the same result: **the most stable circuit is the voltage-divider bias (Fig. 4)**, followed by collector-feedback bias (Fig. 3), emitter-resistor bias (Fig. 2), and finally the least stable, fixed bias (Fig. 1). The small differences between theory and experiment were attributed to measurement errors and to the potentiometer not being adjustable exactly to the desired value.

*Note: In Report A, the I_CQ calculation for Fig. 1 at low β used V_C = 12.372 V, whereas the table lists 13.372 V; with 13.372 V, I_CQ ≈ 1.63 mA.*

The third report, from 2008 (in Turkish), found β = 101, 75 and 189 for the 2N3903, 2N3904 and BC546, and measured V_C for the four circuits; the I_CQ column is empty. It comments that the emitter resistor improves stability by reducing I_E and therefore the base current.

*Note: In the β table of the 2008 report, I_C = V_C / 1 kΩ was used (for example, I_C = 14 mA for V_C = 14 V); the correct expression is I_C = (V_CC − V_C)/R_C. Also, V_B = 9.7 V is written for the BC546; it should most likely have been 0.7 V.*

## Download

The ZIP file contains the lab sheet PDF with its password removed (Experiment8.pdf) and PDF copies of the 2006 and 2008 reports with personal information blacked out.
