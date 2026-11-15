---
baslik: EEM214 Electronics I: Zener and Diode Small-Signal Preliminary Work Appendices
ozet: Handwritten solutions for Zener regulation, the DC and AC equivalents of a diode, small-signal resistance, and resistor design for a 0.7 voltage transfer ratio.
---

The Zener and diode small-signal preliminary works prepared for the EEM214 laboratory were transcribed to text from photographed and scanned pages. Student names and numbers have been removed; the source images and the download file are not shared. The archive date of the small-signal work is 23 March 2014.

## Zener preliminary work

The same calculation in the two photographs has been transcribed together. The source explanation compares a Zener diode, which conducts current in the reverse direction beyond a certain threshold, with an ordinary diode, which is not used in the reverse direction; it states that an ordinary diode would burn out in reverse conduction.

*Note: Reverse breakdown can also occur in an ordinary diode. Permanent damage depends on current and power limits; "it burns out at any reverse current" is not a general physical rule.*

In the circuit, the source V_s is connected to the output through R_s; the Zener and the load R_L are in parallel at the output. The calculations in the source:

- r_z = ΔV_z/ΔI_z = 20 Ω.
- r_z I_zk = 20 Ω × 0.2 mA = 4 mV; the source calls this V_z.
- With the comparison 10 V − 0.5 kΩ × 5 mA = 7.5 V, the Zener is stated to be conducting and V_out = 6.8 V is written.
- For "V_s + 1", 8.5 V and V_out = 6.8 V; for "V_s − 1", 6.5 V and the Zener is stated not to be conducting.
- R_L = 2 kΩ, V_in = 6.5 V and with the Zener in cutoff, V_out = [R_L/(R_s + R_L)]V_in = (2/2.5) × 6.5 V.
- For R_L = 0.5 kΩ, V_out = [0.5/(0.5 + 0.5)]V_in; with V_in = 10 V this gives 5 V.

*Note: 4 mV is the voltage change calculated with the given dynamic resistance; it is not the nominal 6.8 V of the Zener. For the 2 kΩ load and 6.5 V input, the divider result is 5.2 V. The "V_s ± 1" lines in the source are values centered on 7.5 V; they should not be confused with a direct ±1 V change of the 10 V source. At the loaded regulation limit, the Zener current should also be checked.*

## DC operating point of the diode

The D1N4148 diode is connected to the +5 V supply through 1 kΩ, and its lower terminal is connected to ground through R. The input is coupled to the upper terminal and the output to the 1 kΩ load at the lower terminal through 10 µF capacitors. The input is written as v_i(t) = V_m cos(ωt).

In the source model, the threshold is V_γ = 0.6 V, the series resistance is r = 20 Ω, and the ideality factor is n = 2. At DC, the capacitors are open circuits:

I_DQ = (5 − 0.6)/(1 kΩ + R + 20 Ω).

| R | Total DC resistance | I_DQ |
| --- | --- | --- |
| 3.9 kΩ | 4920 Ω | Approximately 894 µA |
| 56 kΩ | 57020 Ω | Approximately 77.1 µA |

The source curve shows the operating point and the linearization. For AC, the supply is grounded, the coupling capacitors are treated as short circuits, and the diode is replaced by r_d.

## Small-signal resistance and voltage transfer

r_d = nV_T/I_DQ, V_T = 25 mV:

- For 894 µA, r_d ≈ 56 Ω.
- For 77.1 µA, r_d ≈ 650 Ω.

The output load is R_eq = R || 1 kΩ and A_V = V_o/V_in = R_eq/(R_eq + r_d).

| R | Parallel equivalent in the source | r_d | A_V in the source |
| --- | --- | --- | --- |
| 3.9 kΩ | Approximately 800 Ω | 56 Ω | 0.92 |
| 56 kΩ | Approximately 980 Ω | 650 Ω | 0.60 |

*Note: Since 800/(800 + 56) ≈ 0.935, the result 0.92 in the first row does not agree arithmetically. The second ratio is approximately 0.601. The source did not add the 20 Ω series resistance used at DC to r_d at AC; the results are transcribed with this assumption.*

The source writes the small-signal limit as v_d ≪ nV_T = 50 mV.

*Note: This inequality applies to the AC voltage across the diode; it does not have to be the same as the input source amplitude.*

## Resistor design for a 0.7 transfer ratio

The design conditions are 0.67 < A_V < 0.73 and I_DQ < 3 mA. The solution neglects 20 Ω at this stage and uses I_DQ ≈ 4.4 V/(1 kΩ + R). The current condition gives R > 466 Ω.

With resistances expressed in kΩ, r_d ≈ 0.0113(1 + R), R_eq = R/(1 + R), and the target is:

0.7 = R_eq/(R_eq + r_d).

In the source algebra, 7r_d = 3R_eq is written, followed by approximately 8R² − 284R + 8 = 0. The roots are approximately 35.4 kΩ and 28 Ω; the small root is eliminated because of the current limit. 27 kΩ is also written in the first trial line but is not used in the final solution.

Source check for 35.4 kΩ:

- R_eq ≈ 0.972 kΩ.
- r_d ≈ 0.411 kΩ.
- A_V ≈ 0.972/(0.972 + 0.411) = 0.702.

With the standard 33 kΩ, R_eq ≈ 0.970 kΩ, r_d ≈ 0.384 kΩ and A_V ≈ 0.716 are written; it is concluded that 33 kΩ can be used.

*Note: With unrounded nV_T = 50 mV and 4.4 V, the large root is approximately 35.69 kΩ; 35.4 kΩ results from rounding of intermediate coefficients. For 33 kΩ the same model gives approximately 0.715, which is within the required range. With I_DQ ≈ 0.129 mA, the 3 mA limit is also satisfied.*
