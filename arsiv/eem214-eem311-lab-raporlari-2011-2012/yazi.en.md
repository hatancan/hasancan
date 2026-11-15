---
baslik: EEM214 Electronics I: Student Reports and Preliminary Work for the EEM311 Laboratory (2011–2012)
ozet: EEM311 Electronics II laboratory work kept in the EEM214 Electronics I folder: eight Proteus reports from fall 2011 (BJT and FET amplifiers, two-stage amplifier, current mirror, active load, differential amplifier, frequency response) and PSpice preliminary work from fall 2012 (differential amplifier, op-amp, active filter).
---

This post brings together student work that was kept in the laboratory folder of the EEM214 Electronics I course but was actually prepared for the laboratory of the next semester's course, **EEM311 Electronics II**. The eight reports from fall 2011 are Turkish-language reports in which measurements made in the laboratory are compared with Proteus simulations; the files from fall 2012 are mostly PSpice preliminary work. All of it is the work of friends; names and student numbers have been redacted. The lab handouts for the experiments are in the EEM311 posts in the archive: [Experiments 1–2](/arsiv/eem311-deney-1-2-bjt-yukselteci/), [Experiments 3–4](/arsiv/eem311-deney-3-4-mosfet-iki-katli/), [Experiments 5–6](/arsiv/eem311-deney-5-6-akim-aynasi-aktif-yuk/), [Experiments 7–8](/arsiv/eem311-deney-7-8-fark-frekans-cevabi/). PDF copies with personal information redacted can be downloaded as a ZIP at the end of the post.

## Fall 2011 reports

### Report 1: Common-emitter BJT amplifier, small-signal parameters

In the DC analysis I_BQ = 31 µA, I_CQ = 8.396 mA, V_CEQ = 6.24 V; **β = 8.396 mA / 31 µA ≈ 270.6**. From v_be measured with a 1 kHz, 40 mV(pp) input, r_π = 606.66 Ω and n = 0.7279 were calculated; with the measured V_out = 4.48 V, g_m = 0.288 S, r_o ≈ 25 kΩ and V_A ≈ 199 V were found. In Proteus, with a 2 mV(pp) input, v_be = 7.3 mV(pp), and the largest undistorted output is 12.8 V(pp); clipping of the output is shown for 20, 140 and 500 mV(pp) inputs.

### Report 2: Gain, clipping and input resistance in a BJT amplifier

I_CQ = 3.00 mA, V_CEQ = 1.80 V. With a 5 kHz, 100 mV(pp) input, A_v = 1489.4 mV / 100 mV ≈ **14.9**. With a 1 V(pp) input the output clips at 3.25 V and −4.75 V, and with a 6 V(pp) input at 2.25 V and −8.00 V; clipping begins at an input of about 150 mV(pp) (since Proteus has no triangle wave, a sine was used). With a 10 kΩ series resistor at the input, V_out = 44 mV gives **R_in ≈ 7.86 kΩ**.

### Report 3: Common-source FET amplifier

V_G = 3.72 V, V_D = 8.61 V, V_S = 1.70 V. With a 1 kHz, 6 mV(pp) input, V_out = 480 mV, **A_v = 80**; how the gain changes when C_d and R_L are removed, and when C_S is removed, was simulated (the required FET is not available in Proteus, so the values came out different). At a 20 mV(pp) input the output clips. With a 20 kΩ potentiometer, R_in ≈ 26.15 kΩ and R_out ≈ 60 kΩ were calculated.

### Report 4: Two-stage (FET + BJT) amplifier

At 12 V, V_G = 0 V, V_D = 5.87 V, V_S = 2.02 V; V_B = 6.98 V, V_C = 9.16 V, V_E = 6.29 V; I_C = 2.84 mA, I_D = 6.13 mA. With a 1 kHz input, the first-stage gain is 8, the second-stage gain 88.75, and the **total gain 710**. Clipping occurs at a 360 mV(pp) input; with a 500 kΩ series resistor, **R_in ≈ 0.97 MΩ ≈ 1 MΩ**, and with 1 kΩ at the output, **R_out ≈ 0.96 kΩ ≈ 1 kΩ**.

### Report 5: MOSFET current mirror

V_CC1 = V_CC2 = 5 V, R = 1 kΩ. Since the CD4007 is not available in Proteus, a BUK445 was used: in simulation I_REF = I_O = 2.89 mA, in measurement I_REF = 1.86 mA, I_O = 1.68 mA. In the V_CC2 sweep, I_O is 1.18 mA at V_CC2 = 25 mV, 2.87 mA at 100 mV, and constant at 2.89 mA beyond 110 mV; the output resistance was evaluated.

### Report 6: Current-mirror-loaded (active-load) amplifier

For I_REF = 0.6 mA, R_REF = 22 kΩ (measured I_REF = 0.67 mA). It is reported that in simulation, with a 50 mV(pp), 5 kHz input, no gain could be obtained in the first circuit, while in the modified circuit V_out = 920 mV, giving **A_v = 18.4**. R_in ≈ 28 kΩ (50 kΩ in the experiment).

### Report 7: BJT differential amplifier

R_REF = 4.70 kΩ, R_POT = 310 Ω. In the measurement I_CQA = I_CQB = 2 mA, V_CE1 = 4.58 V, V_CE2 = 6.252 V, I_CQ1 = 1.213 mA, I_CQ2 = 0.916 mA; in simulation the two sides are balanced (I_CQ1,2 = 1.03 mA, V_CE1,2 = 5.39 V).

| | Experiment | Simulation |
|---|---|---|
| v_in1 = 100 mV(pp): A_vdm-se1 / A_vdm-se2 | 27.0 / 121.0 | 15.2 / 0 |
| v_in2 = 100 mV(pp): A_vdm-se1 / A_vdm-se2 | 120.0 / 26.0 | 0 / 15.2 |
| A_vdm-diff | 96.3 | 29 |
| Common-mode outputs | 9.46 V | 7.19 V |

The report states CMRR = ∞ in simulation and CMRR = 0.092 in the experiment.

*Note: The report writes A_vdm-diff = 9.3 V / 100 mV = "96.3"; 9.3 V / 0.1 V is 93. The common-mode gain is also computed with an incorrect expression such as "vout1·vout2/((vout1 + vout2)/2)"; the single-ended common-mode gain is A_vcm-se = v_out / v_icm, and the ratio CMRR = A_vdm-se / A_vcm-se should be greater than 1.*

### Report 8: Frequency response of the common-emitter amplifier

Circuit: V_CC = 12 V, R1 = 8.2 kΩ, R2 = 3.9 kΩ, R_C = 6.3 kΩ, R_E = 3.3 kΩ, R_S = 3 kΩ, R_L = 3.9 kΩ, C1 = 10 µF, C2 = 1 µF, C_E = 10 µF, 2N3904. In the experiment I_CQ = 0.81 mA, V_CEQ = 3.06 V (0.96 mA, 2.76 V in simulation). With a 20 mV(pp), 1 kHz input, the midband gain is **25.81** in the experiment and **31** in simulation. In the frequency sweep (30 Hz – 1.5 MHz), **f_L = 3.87 Hz, f_H = 425 kHz** were found; in simulation the gain is 15 at 30 Hz, about 31 between 300 Hz and 20 kHz, 18.5 at 500 kHz, and 7.25 at 1.5 MHz.

## Fall 2012 preliminary work

- **Experiment 3 preliminary work:** PSpice plots of the two-stage circuit with a JFET and a BJT (I_C, I_B, I_D, I_E waveforms).
- **Experiment 5 preliminary work:** DC and AC analysis of the MOSFET current-mirror circuit (PSpice).
- **Experiment 6 preliminary work:** PSpice bias-point values and waveforms for the active-load amplifier with 2N3904/2N3906 (the same file had two copies; one was kept).
- **Experiment 7:** frequency sweep of the common-emitter amplifier (for example, V_out = 288.6 mV at 30 Hz).
- **Experiment 8 – "Introduction to Opamps" (03.12.2012):** simulation of the BJT differential amplifier.
- **Experiment 9 – Operational Amplifiers:** simulations with a 100 mV, 1 kHz sine for an inverting amplifier with a 1 kΩ input resistor and R_f = 4.7 kΩ, 10 kΩ and 1 MΩ; comments that the circuit is an "inverting amplifier" because the input signal is applied to the (−) input of the op-amp, and that the integral of a square wave is a triangle wave.
- **Experiment 8 – Active Filters preliminary work:** schematics of a 3 kHz low-pass and a 300 Hz high-pass filter; with C = 10 µF, R = 375.131 kΩ was calculated for 3 kHz and R = 53.05 Ω for 300 Hz.
- **RC oscillator:** Multisim schematic and oscilloscope screen of an RC phase-shift oscillator with a 741 op-amp (about 2.19 kHz).

*Note: With f = 1/(2πRC), R ≈ 53 Ω at 300 Hz for C = 10 µF is correct, but at 3 kHz R should be ≈ 5.3 Ω (not 375 kΩ). Since such small resistances are impractical, capacitors in the nF range are usually chosen.*

## Download

The ZIP file contains PDF copies, with personal information redacted, of the eight reports from 2011 and the nine preliminary works/reports from 2012.
