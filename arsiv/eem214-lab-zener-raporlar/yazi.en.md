---
baslik: EEM214 Electronics I: Zener Diode Characteristics and the Zener Regulator, Student Reports (2006–2012)
ozet: Student pre-lab and lab reports for the EEM214 Electronics I Zener diode experiment: forward- and reverse-bias measurement tables for the BZX55C (6.2 V), Zener resistance, and output voltages and Zener currents of a Zener regulator with 15 V and 8 V supplies and different series and load resistors.
---

This post collects student pre-lab and lab reports prepared in different years for the **Zener Diode Characteristics** experiment of the Başkent University **EEM 214 Electronics I** laboratory. All of them are the work of friends; names and student numbers have been redacted. The experiment covers testing a Zener diode with a DMM, the forward- and reverse-bias characteristics of the BZX55C Zener diode, and the behavior of a Zener regulator at different series resistor (R_s) and load (R_L) values. PDF copies with personal information redacted can be downloaded as a ZIP at the end of the post.

## Pre-lab work

- **2009 pre-lab:** The circuit was set up in PSpice and the Zener's i–v characteristic was plotted with a DC sweep of V_in from −10 V to 6 V. The Zener diode is described as follows: in the forward direction it conducts like an ordinary diode (about 0.6 V drop in silicon); in the reverse direction it conducts once the voltage exceeds the breakdown (Zener) voltage and holds the voltage across it at that value. In a heavily doped p-n junction, electrons tunnel from the valence band of the p region to the conduction band of the n region; the breakdown voltage can be set precisely through doping (common tolerances are 5% and 10%). It is used as a voltage stabilizer for generating reference voltages and in low-current applications.
- **2008 pre-lab:** V(D1) – I(D1) curve with PSpice (−20 V to 10 V); the Zener diode is defined as "a diode that, when connected in reverse, passes voltages exceeding the voltage written on it and holds the voltage across it constant at that value"; the i–v characteristics of the ordinary diode and the Zener were compared (for the ordinary diode the slope is 0 when off and infinite when conducting; the Zener additionally conducts in the reverse direction at −V_Z).
- **2012 pre-lab:** PSpice simulations with a 10 V source, 1 kΩ, and a D1N750 Zener.

## Zener diode test

On the DMM diode range, 0.7615 V and 0.7756 V were read in the forward direction and "1" (out of range) in the reverse direction; the diodes are good. One report found 710.2 Ω in the forward direction with the ohmmeter, and a resistance too large to measure in the reverse direction.

## Forward and reverse characteristics (BZX55C)

**Forward bias:**

| v_D (V) | 2006 report A | 2006 report B |
|---|---|---|
| 0.35 | 0.25 µA | 0.25 µA |
| 0.45 | 2.18 µA | 1.9 µA |
| 0.55 | 20.94 µA | 19.9 µA |
| 0.60 | 52.21 µA | 63.6 µA |
| 0.65 | 143.2 µA | 248 µA |
| 0.70 | 1.016 mA | 0.969 mA |
| 0.75 | 5.654 mA | 5.291 mA |
| 0.80 | 31.01 mA | 31.44 mA |
| 0.85 | – | 69.72 mA |

In the forward direction the Zener diode behaves like an ordinary silicon diode; it begins to conduct after about 0.7 V.

**Reverse bias:**

| V_applied (V) | V_Z (A) | I_Z (A) | V_Z (B) | I_Z (B) | V_Z (2008) | I_Z (2008) |
|---|---|---|---|---|---|---|
| 2 | 2.064 V | ≈ 0 | 2.07 V | ≈ 0 | – | – |
| 4 | 4.079 V | 1.8 µA | 4.10 V | 0.85 µA | – | – |
| 6 | 5.83 V | 373 µA | 5.80 V | 0.75 mA | 5.998 V | 1.763 mA |
| 8 | 5.95 V | 6.46 mA | 5.94 V | 6.34 mA | 6.071 V | 5.655 mA |
| 10 | 5.99 V | 12.33 mA | 5.95 V | 12.62 mA | 6.109 V | 11.50 mA |
| 12 | 6.00 V | 18.34 mA | 5.96 V | 18.85 mA | 6.150 V | 17.31 mA |
| 14 | 6.00 V | 24.26 mA | 5.97 V | 24.92 mA | 6.200 V | 24.11 mA |

The Zener voltage is about **6 V**; beyond this value the voltage stays almost constant while the current rises rapidly. Another 2008 report (in Turkish) found a Zener voltage of around 6.3 V.

One of the reports calculated the Zener impedance as Z_Z = V_Z / I_Z: 5.95 V / 6.46 mA = 921 Ω for 8 V, and 6.00 V / 18.34 mA = 327 Ω for 12 V.

*Note: V_Z / I_Z is a "static" ratio. What matters in regulation is the dynamic resistance r_Z = ΔV_Z / ΔI_Z; from the same measurements, (6.00 − 5.95) V / (18.34 − 6.46) mA ≈ 4.2 Ω.*

## Zener regulator

Output voltage V_out (2006 report A):

| R_s | V_s = 15 V, R_L = 1.8 kΩ | V_s = 15 V, R_L = 470 Ω | V_s = 8 V, R_L = 1.8 kΩ | V_s = 8 V, R_L = 470 Ω |
|---|---|---|---|---|
| 390 Ω | 5.98 V | 5.97 V | 5.92 V | 4.30 V |
| 220 Ω | 6.01 V | 6.01 V | 5.94 V | 5.42 V |
| 150 Ω | 6.05 V | 6.02 V | 5.96 V | 5.91 V |
| 100 Ω | 6.13 V | 6.07 V | 5.97 V | 5.98 V |

The currents were calculated as I_L = V_out / R_L, I_s = (V_s − V_out) / R_s, and I_Z = I_s − I_L. For example, for V_s = 15 V, R_L = 1.8 kΩ, R_s = 390 Ω: I_L = 3.32 mA, I_s = 23.1 mA, I_Z = 19.78 mA; for V_s = 8 V, R_L = 470 Ω, R_s = 390 Ω: I_L = 9.14 mA, I_s = 9.49 mA, and I_Z is only 0.35 mA, so the output drops to 4.30 V (it has left the Zener regulation region). The values in report B are very similar (for example, 5.99 V for 15 V / 1.8 kΩ / 390 Ω, and 4.40 V for 8 V / 470 Ω / 390 Ω).

*Note: In the report, for the row V_s = 8 V, R_L = 1.8 kΩ, R_s = 100 Ω, the calculation of the previous row (150 Ω) was written again. The correct values should be I_s = (8 − 5.97) / 0.1 = 20.3 mA, I_L = 3.32 mA, I_Z ≈ 17.0 mA.*

In the 2008 report, measurements were made with 12 V and 8 V sources, R_L = 820 Ω and 330 Ω, and R_s = 620, 390, 100 Ω: for example, at 12 V with R_s = 620 Ω the output stays at 3.84 V, while with R_s = 100 Ω it rises to 6.41 V; at 8 V the output stays between 3.5 and 4.3 V in all cases.

## Download

The ZIP file contains PDF copies, with personal information redacted, of the seven pre-lab and lab reports, organized in folders by year.
