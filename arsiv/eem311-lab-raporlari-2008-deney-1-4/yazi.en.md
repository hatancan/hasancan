---
baslik: EEM311 Electronics II: 2008 Laboratory Preliminary Work and Reports, Experiments 1–4 (BJT, MOSFET, Two-Stage Amplifier)
ozet: Student preliminary work and reports from the fall 2008 EEM311 Electronics II laboratory, Experiments 1–4: BC238B common-emitter amplifier measurements (β, rπ, n, ro, VA), BJT amplifier design, CD4007 MOSFET amplifier PSpice results, and a JFET–BJT two-stage amplifier.
---

This post contains student work from the first four experiments of the **fall 2008** **EEM311 Electronics II** laboratory in the Electrical-Electronics Engineering department at Başkent University: PSpice preliminary work, experiment reports, and the handwritten design calculations for Experiment 2. All of it is **the work of a friend; personal information has been removed.** The reports are in Turkish and were prepared on a computer; the oscilloscope screens were mostly left as blank grids to be drawn by hand. The preliminary work for Experiment 2 was transcribed from photographed pages. The experiment handouts themselves are in separate posts in the archive (Experiments 1–2 and Experiments 3–4). Anonymized PDF copies, with personal information removed, can be downloaded as a ZIP at the end of the post.

## Experiment 1: Single-Stage BJT Amplifier

### Preliminary Work (PSpice)

The circuit from the handout (V_CC = 15 V, R_B1 = 470 kΩ, R_B2 = 1.8 kΩ, R_C = 1 kΩ, R_L = 100 kΩ, C = 10 µF, transistor BC238B) was set up in PSpice. Results of the bias point analysis:

- V_CQ = 15 V − 5.520 V = 9.480 V, V_EQ = 0 V
- I_BQ = 30.310 µA, I_CQ = 9.480 mA, I_EQ = 9.510 mA

*Note: The document gives I_CQ as "9.480 µA"; from the 5.52 V drop across I_C·R_C and the I_E = 9.510 value, it is clear that the current is 9.48 mA.*

Voltage gain found from the time-domain simulation with a 1 kHz sine input, for different peak-to-peak amplitudes:

| Input (p-p) | A_v |
|---|---|
| 2 mV | −96.249 |
| 20 mV | −95.834 |
| 140 mV | −64.501 |
| 500 mV | −18.774 |

As the input grows, the output first becomes distorted and then starts clipping, so the measured gain falls.

### Report

The measured operating point is **I_BQ = 30 µA, I_CQ = 7.966 mA, V_CEQ = 7.010 V**; the DC load line is drawn between 15 mA and 15 V, with the Q point marked on it.

1. β = I_C / I_B = 7.966 mA / 30 µA = **265.53**
1. With a 1 kHz, 40 mV p-p input, v_be = 18.2 mV (p-p) was measured: rπ = v_be / I_BQ = **606.66 Ω**, and from rπ = n·V_T / I_BQ, **n = 0.7279**.
1. With a 20 mV p-p input, v_out = 3.7 V: g_m = I_CQ / (n·V_T) = 0.438 S; from the relation (r_o ∥ R_L ∥ R_C) = v_out / (g_m·v_be), **r_o = 25 kΩ**, and from r_o ≅ V_A / I_CQ, **V_A = 199.15 V**.
1. Oscilloscope settings: 10 mV/div for v_in, 1 V/div for v_out, 500 µs/div.
1. At the point where distortion begins, **v_be = 7.3 mV** (p-p).
1. Largest undistorted output swing **v_out,undistorted = 12.5 V** (p-p).
1. Output waveforms were drawn for 20 mV, 140 mV, and 500 mV p-p inputs; at 500 mV the output is clipped to nearly a square wave.

*Note: A value of n below 1 (0.73) is not physically expected (the handout says 1 ≤ n ≤ 2); an error in the v_be measurement or rounding of I_BQ may have caused this result.*

## Experiment 2: Single-Stage BJT Amplifier Design

The report for this experiment is present in the folder only as blank oscilloscope grids (the report itself was presumably filled in by hand). The handwritten design calculations of the preliminary work, however, are on four photographed pages:

- Required gain range: A_v,min = 22 dB = 10^(22/20) = 12.58, A_v,max = 24 dB = 10^(24/20) = 15.85; the design targets the average, **A_v = (15.85 + 12.58)/2 = 14.35**.
- For an undistorted swing on the AC load line, x = v_out,undistorted,p-p / 2 = 6/2 = 3 V is required; **4 V** was chosen with a safety margin.
- Taking R_C = R_L = 3.3 kΩ, from 4 = I_CQ·(R_C ∥ R_L) = I_CQ·1.65 kΩ, **I_CQ = 2.42 mA**; for β = 250, I_BQ = 2.42 mA / 250 = **9.68 µA**.
- From A_v = (R_C ∥ R_L) / (rπ/(β+1) + R_E1), 14.35 = 1650 Ω / (…) gives **R_E1 = 104.7 Ω**.
- From V_CC = V_CEQ + I_C·R_C + I_C·(R_E1 + R_E2), **R_E2 = 1140 Ω** (R_E = R_E1 + R_E2 ≈ 1244 Ω); base resistor divider **R1 = 39 kΩ, R2 = 13 kΩ**.
- For n = 1.4, rπ = n·V_T / I_BQ = 1.4·0.025 V / 9.68 µA = **3.6 kΩ**.
- With the same I_BQ, for β = 200, I_CQ = 1.9 mA and V_CEQ = 6.01 V; for β = 250, I_CQ = 2.42 mA and V_CEQ = 3.56 V were calculated. The last page shows a drawn small-signal equivalent circuit (R1 ∥ R2, rπ, g_m·v_be = β·i_b, R_E1, R_C, R_L).

*Note: One of the photographed pages gives R_E1 + R_E2 = 1420 Ω and another gives R_E = 1244 Ω; also, since I_CQ changes in proportion to β when I_BQ is held constant (1.9 mA → 2.42 mA, about 27%), the handout's condition that "I_CQ change by at most 3% with β" is not satisfied by this calculation; to meet that condition, the base divider would need to be built with much smaller resistors.*

## Experiment 3: Single-Stage MOSFET Amplifier (PSpice Preliminary Work)

In the common-source amplifier built with the NMOS transistor of the CD4007, the selected resistors are **R1 = 68 kΩ, R2 = 20 kΩ, R_D = 178 kΩ, R_S = 20 kΩ**, C_g = 1 µF, C_S = 10 µF, with a 50 mV, 1 kHz input.

Bias simulation: divider current 170.5 µA, I_D = **74.01 µA**, V_G = 3.409 V, V_D = 1.826 V, total current drawn from the supply 244.5 µA. This is quite close to the handout's target of I_D ≈ 75 µA.

Transient simulation results:

| | With R_L | Without R_L |
|---|---|---|
| Input (Vp-p) | 49.999 mV | 49.999 mV |
| Output (Vp-p) | 188.85 mV | 1.8265 V |
| A_v | −3.777 | −36.53 |

*Note: R_D = 178 kΩ is not a standard resistor value (the handout asks for standard values ≤ 100 kΩ). With V_D = 1.826 V, V_S = 74 µA·20 kΩ ≈ 1.48 V, so V_DS ≈ 0.35 V remains, which is smaller than V_GS − V_t ≈ 1.93 − 1.45 = 0.48 V; that is, the MOSFET is not in saturation but in the triode region. The 1.8265 V in the "Without R_L" column also appears to have been read as the drain DC level rather than as the output swing.*

The report itself is present in the folder only as blank grids and measurement schematics (Figures 6 and 7, R_x = 1 kΩ).

## Experiment 4: Two-Stage JFET–BJT Amplifier

### Preliminary Work (PSpice)

The circuit from the handout (J2N4860 common-source + Q2N3904 common-emitter, V_CC = 12 V, R_g = 1 MΩ, R_d = 1 kΩ, R_s = 330 Ω, R1 = 30 kΩ, R2 = 47 kΩ, R_c = 1 kΩ, R_e = 2.2 kΩ, R_L = 100 kΩ) was set up. Because the handout calls both capacitors "C2", C2 = 22 µF and C3 = 100 µF were used.

| Bias point | Value |
|---|---|
| V_D | 5.865 V |
| V_G | ≈ 0 V (7.884 fV) |
| V_S | 2.024 V |
| V_B | 6.985 V |
| V_C | 9.158 V |
| V_E | 6.292 V |
| I_D | 6.135 mA |
| I_C | 2.842 mA |
| I_E | 2.860 mA |
| I_B | 18.55 µA |

In the transient simulation with a 0.1 mV, 1 kHz input, v_in = 100 µV (p-p), v_out = 963.7 nV, and v_b (p-p) = 6.9851 V were read; from these, the first-stage gain came out as 20.744 k, the second stage as 6.9362 µ, and the total as 496.462 m.

*Note: These gains are not physical: 6.9851 V is the DC level at the base of the second stage (V_B); in the plots, the DC level was measured from the wrong side of the coupling capacitor. The DC values in the preliminary work, however, are consistent with the handout's circuit.*

### Report

Measured voltages: V_G ≈ 0 V (0.007 V), V_D = 4.763 V, V_S = 2.488 V, V_B = 6.981 V, V_C = 9.225 V, V_E = 6.175 V. From these:

- I_C = (V_CC − V_C)/R_c = (15 − 9.225)/1 kΩ = 5.8 mA
- I_D = (V_CC − V_D)/R_D = (15 − 4.763)/1 kΩ = 10.2 mA

*Note: The circuit's supply voltage is 12 V; 15 V was used in the calculations. With 12 V, I_C = 2.78 mA and I_D = 7.24 mA are obtained; I_C agrees with the 2.84 mA in the preliminary work. I_D = V_S/R_s = 2.488/330 ≈ 7.5 mA through the source resistor also confirms the same result.*

The second part of the report contains simulation plots (v_in, v_out, v_b) for a 70 mV, 1 kHz input; the rows for gain, undistorted swing, R_in (R_x = 500 kΩ), and R_out (R_x = 1 kΩ) were left blank.

## Unpublished Files

The PSpice project and simulation files in the folder (.opj, .DSN, .DBK, .sim, .out, .dat, etc.) were not included in this post; the blank report templates for Experiments 2 and 3 are also not in the ZIP.
