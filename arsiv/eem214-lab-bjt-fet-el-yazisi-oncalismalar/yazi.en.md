---
baslik: EEM214 Electronics I: Handwritten Pre-Lab Work for the BJT and FET Laboratory
ozet: A transcription, with personal information removed, of the BJT operating regions, biasing, emitter follower, MOSFET calculations, and JFET pre-lab questions.
---

Pre-lab work prepared by different students for the EEM214 laboratory, some of it dated 2013, was photographed, and the scanned pages were transcribed into text. Personal information has been removed; the photographs and the downloadable file are not shared. Different copies of the same assignment were considered together; errors seen in the source are noted under the relevant section.

## BJT: Base Current and Operating Regions

The first pre-lab takes R_B = 100 kΩ, V_BE = 0.6 V, and β = 260. The relations used are:

- I_B = (V_BB − V_BE)/R_B.
- I_C = βI_B.
- V_CE = V_CC − I_C R_C.

For V_BB = 0.6 V, I_B = 0 is written; for 1 V, 4 µA. In the third case the heading says 10 V, but 12 V is used in the calculation; the results 114 µA and 144 µA appear in different copies.

*Note: For 10 V the result is 94 µA, and for 12 V it is 114 µA. The result 144 µA is inconsistent with the given numbers. The relation I_C = βI_B applies to the forward active region.*

For R_C = 1 kΩ, the values I_B = 0, 20, 40, and 60 µA used in the source give I_C = 0, 5.2, 10.4, and 15.6 mA, respectively. The table written by directly applying the forward active region relation is:

| V_CC | I_B | I_C | V_CE |
| --- | --- | --- | --- |
| 15 V | 0 | 0 | 15 V |
| 15 V | 20 µA | 5.2 mA | 9.8 V |
| 15 V | 40 µA | 10.4 mA | 4.6 V |
| 15 V | 60 µA | 15.6 mA | −0.6 V |
| 10 V | 0 | 0 | 10 V |
| 10 V | 20 µA | 5.2 mA | 4.8 V |
| 10 V | 40 µA | 10.4 mA | −0.4 V |
| 5 V | 0 | 0 | 5 V |
| 5 V | 20 µA | 5.2 mA | −0.2 V |
| 1 V | 0 | 0 | 1 V |

The voltage result for the 1 V and 20 µA row is left incomplete in the source. The load lines drawn intersect the V_CE axis at 1, 5, 10, and 15 V.

*Note: Negative V_CE results show that the circuit cannot operate in the forward active region at this current; the real solution must be found again using the saturation model. The unclear voltage entry in the first row of one copy was compared with the 15 V in the other copy.*

For R_C = 2.2 kΩ and I_B = 20 µA, one copy gives 2.56 V at a 15 V supply, 1.44 V at a 10 V supply, −6.44 V at a 5 V supply, and −10.44 V at a 1 V supply. In the other copy, the first result appears as 3.532 V.

*Note: With the assumption I_C = 5.2 mA, the first two algebraic results are 3.56 V and −1.44 V. The value 3.532 V may stem from computing the current with more digits; the source does not explain this. The negative results again require a saturation check.*

In the saturation calculation with V_CE,sat = 0.2 V:

- V_CC = 15 V, R_C = 1 kΩ: I_C = 14.8 mA. One copy gives I_B = 0.56 mA, the other approximately 0.057 mA.
- V_CC = 10 V, R_C = 2.2 kΩ: in the other copy, I_C ≈ 4.45 mA and I_B ≈ 0.017 mA are found. In the first copy, although the heading is 10 V, 15 V is used in the equation, and 6.72 mA and 0.025 mA are written.

*Note: 14.8 mA/260 ≈ 56.9 µA. For 10 V and 2.2 kΩ, the limiting current is 4.455 mA, and the base current computed with β = 260 is 17.13 µA; the forced β in saturation is evaluated separately.*

The pages list the forward active, cutoff, and saturation regions. For forward active, the conditions I_B > 0 and V_CE > 0 are given; for saturation, a small V_CE and positive I_B are shown.

*Note: The V_CE > 0 condition alone does not define the forward active region; the base-emitter junction must be forward biased and the base-collector junction reverse biased.*

## Four BJT Biasing Circuits

In another two-page work, V_CC = 30 V, β = 100, R_C = 4.7 kΩ, R_B = 470 kΩ, and, where needed, R_E = 1.2 kΩ are used.

| Circuit | Base current in the source | V_CE in the source |
| --- | --- | --- |
| Fixed-bias | 62.34 µA | 0.7002 V |
| Bias with emitter resistor | 49.56 µA | 0.7068 V |
| Collector-to-base feedback | 31.17 µA | 15.3501 V |
| Voltage-divider bias | −2.735 µA | 31.61689 V |

The equations used:

- Fixed bias: I_B = (V_CC − V_BE)/R_B.
- With emitter resistor: I_B = (V_CC − V_BE)/[R_B + (β + 1)R_E].
- Feedback approximation: I_B = (V_CC − V_BE)/(R_B + βR_C).
- Divider: V_Th = V_CC R_B2/(R_B1 + R_B2), R_Th = R_B1 || R_B2; I_B = (V_Th − V_BE)/[R_Th + (β + 1)R_E].

In the divider, using 470 kΩ and 5.6 kΩ, V_Th = 0.3532 V and R_Th = 5.59 kΩ are written.

*Note: 470 kΩ || 5.6 kΩ ≈ 5.534 kΩ. Since V_Th < 0.7 V, the negative base current indicates that the forward active model is invalid; in the simplified model the transistor is in cutoff. 31.61689 V is not a physical operating point. In the circuit with the emitter resistor, V_CE with the given I_B is approximately 0.70 V; the small differences are due to rounding. Since the current supplying the base from the collector also flows through R_C, the full equation contains β + 1 instead of β.*

The stability calculation page contains the following results:

- Fixed bias: S(I_CO) = 101 and S(V_BE) = −101/(470 kΩ).
- With emitter resistor: S(V_BE) = −100/[470 kΩ + 101 × 1.2 kΩ] ≈ −0.1691 × 10⁻³ A/V; S(I_CO) ≈ 79.86.
- Feedback: S(V_BE) = −100/[470 kΩ + 101 × 4.7 kΩ]; the result is written as −0.1058. S(I_CO) ≈ 50.75.
- Divider: in the last row, 0.180 is used in place of a resistance, and the results −0.82385 and 0.011369 are written.

*Note: The current with respect to which the stability factor is defined matters. For the derivative of I_C with respect to V_BE, the numerator is −β in fixed bias. The dimension of the feedback row is approximately −0.1059 mA/V. The value 0.180 in the last row is inconsistent with the earlier R_Th calculation; this row is not a verified design result.*

## Common Collector: Emitter Follower

In the work dated 26 April 2013, which has another copy, V_CC = 15 V, R_1 = 47 kΩ, R_2 = 10 kΩ, R_E = 1 kΩ, and β = 100 are used. The sequence of operations in the source:

1. V_Th = [10/(10 + 47)] × 15 = 2.625 V.
2. R_Th = 10 kΩ || 47 kΩ = 8.25; written with the unit Ω.
3. In the equation I_B = (V_Th − V_BE)/[R_Th + (β + 1)R_E], 15 − 0.7 is substituted in the numerator, giving 0.131 mA.
4. I_E = 13.231 mA and r_e = 25 mV/I_E = 1.89 Ω are computed.
5. R_in,base ≈ β(r_e + R_E); the result is written as 101.2 kΩ. In the other copy, the total R_in ≈ 7.63 kΩ appears.
6. The result of the expression R_out = r_e || R_E is written as 0.530 kΩ.
7. A_V ≈ R_E/(r_e + R_E) = 0.998; there is no phase difference in the voltage.
8. A_I ≈ −β(R_1 || R_2)/[(R_1 || R_2) + R_in,base]. The output current arrow is chosen opposite to the emitter current.

*Note: V_Th ≈ 2.632 V and R_Th ≈ 8.246 kΩ. With the correct V_Th, I_B ≈ 17.68 µA, I_E ≈ 1.786 mA, and r_e ≈ 14 Ω are found. Even the source's operation 1.89 Ω || 1 kΩ gives approximately 1.886 Ω, not 0.530 kΩ. The actual output resistance also depends on the resistance of the input source. The negative current gain here results from the chosen arrow direction; the voltage gain of an emitter follower is positive.*

## MOSFET: Ohmic Region and Saturation

The work dated 2 May 2013 and two scanned pages use the same parameters: μ₀C_ox = 166.67 µA/V², W/L = 3, V_T = 1.45 V; in the scanned solution, V_A = 1/λ = 100 V is also given.

- Ohmic region: I_D = μ₀C_ox(W/L)[(V_GS − V_T)V_DS − V_DS²/2].
- Saturation boundary: V_DS,sat = V_GS − V_T.
- Saturation, channel-length modulation neglected: I_D = ½μ₀C_ox(W/L)(V_GS − V_T)².
- Differential resistance in the ohmic region: r = 1/[μ₀C_ox(W/L)(V_GS − V_T − V_DS)].

| V_GS | V_DS | Region in the scanned solution | I_D | Resistance |
| --- | --- | --- | --- | --- |
| 3 V | 0.5 V | Ohmic | 325 µA | 1904.7 Ω |
| 5 V | 0.5 V | Ohmic | 825 µA | 655.7 Ω |
| 2 V | 3 V | Saturation | 75.63 µA | Ohmic relation not applicable |

In the other copy, the first two resistances are written as 1.9047 × 10⁻³ Ω and 6.557 × 10⁻⁴ Ω; the ohmic relation is also applied to the third case, giving a negative resistance and −1425.0285 µA.

*Note: In the first two resistances there is a unit error of a factor of one million due to the µ coefficient. The third case is in saturation; the negative results come from using the wrong region equation. If the V_A = 100 V information is to be used, the saturation current is multiplied by the factor 1 + λV_DS, giving approximately 77.9 µA; the scanned solution neglects this effect.*

For a small-signal resistance of 100 kΩ, V_DS ≈ 0 is taken; one copy finds V_GS = 1.45 V, and the scanned solution finds 1.47 V.

*Note: The 100 kΩ condition gives V_GS − V_T ≈ 0.020 V; the result 1.47 V is consistent.*

In the diode-connected MOSFET example, V_DD = 5 V and I_D = 100 µA:

V_GS = V_T + √[I_D/(½μ₀C_ox W/L)] ≈ 2.082 V.

R = (5 − 2.082)/(100 µA) ≈ 29.18 kΩ. The source also has the rounded result 29.2 kΩ for the same calculation.

## FET Pre-Lab: Biasing and Output Resistance

On the page dated 10 May 2013 and in the second copy, a circuit is drawn with the gate connected to ground through a resistor, R_D = 4.7 kΩ, R_S = 1 kΩ, and V_DD = 15 V. I_G ≈ 0 is written. The loop equation has the form −15 + 4.7k I_D + V_DS + 1k = 0.

*Note: The current is missing in the last term; the dimensionally correct term should be I_D × 1 kΩ.*

In the next line, the saturation decision is made using the condition V_DS ≥ V_GS − V_T and the comparison 3 V ≥ 2 V. The table for r_o ≈ V_A/I_D with V_A = 100 V:

| I_D | r_o |
| --- | --- |
| 1 mA | 100 kΩ |
| 2.5 mA | 40 kΩ |
| 10 mA | 10 kΩ |

In the FET design with a divider, V_DD = 15 V, V_G = 5 V, I_D = 4 mA, V_D = 11 V, I_DSS = 9 mA, and V_P = 3 V are written. Taking the divider current as 0.05 mA, R_G1 = (15 − 5)/0.05 mA = 200 kΩ and R_G2 = 5/0.05 mA = 100 kΩ are found.

*Note: The sign of V_P depends on the channel type; the source does not explain the channel type and sign convention on this line.*

## Unsolved Başkent Laboratory Questions

**Experiment 4 pre-lab:** The first circuit is common-emitter: upper base resistor 100 kΩ, lower base resistor 10 kΩ, input source resistance 10 kΩ, collector resistor 5 kΩ; the emitter is grounded. A_I, A_V, Z_o, and Z_i are requested. V_CC is not specified numerically.

The second circuit is common-base. The base is grounded, the collector is connected to +8 V through 3.6 kΩ, and the emitter is connected to −5 V through 3.9 kΩ. The input is capacitively coupled to the emitter, and the output to the collector. A_V and A_I are requested for β = 75 and r_o = ∞. The source contains no solution.

**Experiment 5 pre-lab:** For the common-source, self-biased JFET circuit, R_D = 12 kΩ, R_G = 1 MΩ, R_S = 470 Ω, V_DD = 30 V, I_DSS = 3 mA, V_P = −2.4 V, and r_d ≫ R_D are given. The source resistor is bypassed for AC by a capacitor. V_GS, I_D, V_DS, and the small-signal voltage gain are asked for; no solution is written.

## Review Notes on the 2N5460 P-Channel JFET

A two-page student report describes the G, S, and D terminals; the distinction between N and P channels; and the P-channel 2N5460 device. The gate, source, and drain terminals are likened, in terms of function, to the base, emitter, and collector terminals of a BJT. The transfer characteristic is the variation of I_D with V_GS at constant V_DS. When V_GS = 0, I_D = I_DSS in the saturation region; at the pinch-off voltage, the current is approximately zero.

The values given in the report:

| Parameter | Value in the source |
| --- | --- |
| I_DSS | −1 mA to −5 mA |
| V_GS(off) | 0.75–6.0 V |
| Forward transfer admittance, magnitude of y_fs | 1000–4000 µmho |
| Output admittance, magnitude of y_os | At most 75 µmho |

g_m expresses the change in drain current with respect to the change in gate voltage. The output admittance is used to find the small-signal output resistance. The report interprets the current curves at different pinch-off voltages and the variation with temperature; it states that the current decreases as temperature rises, and that transconductance increases with current while its slope decreases.

*Note: These are the graph interpretations of the source report; g_m is not a fixed material constant and depends on the operating point. The resistance is obtained from the reciprocal of the output admittance. The negative currents reflect the P-channel sign convention; the magnitude range is 1–5 mA. The temperature behavior of the graphs cannot be generalized to all operating points.*

The switch example uses a +10 V supply and a 2 kΩ drain resistor. When V_GS < −4 V, the device is in cutoff and V_out = +10 V; when V_GS = 0, ohmic operation and approximately V_out = 0.3 V are written. The load line is I_D = (10 V − V_DS)/2 kΩ and intersects the axes at 5 mA and 10 V.

*Note: The V_P = −4 V signs in this last example belong to an N-channel JFET; it should not be taken as a direct continuation of the preceding P-channel 2N5460 section. The manufacturer graphs in the photographs and the datasheet itself were not shared.*
