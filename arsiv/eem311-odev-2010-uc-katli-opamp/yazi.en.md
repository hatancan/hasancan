---
baslik: EEM311 Electronics II: 2010 Homework Solution Drafts, Three-Stage Amplifier and Transistor Op-amp
ozet: DC operating points and small-signal analysis of an amplifier with three BJTs; handwritten solution draft for a nine-transistor op-amp design consisting of two differential stages and an output stage.
---

This post contains two handwritten solution drafts prepared by classmates for the **EEM311 Electronics II** course at Başkent University. Personal information has been removed; **the content was transcribed from photographed pages**. The photographs were taken on 9–10 November and 17 December 2010. Repeated shots of the same pages were merged. This post has no downloadable file. The semester's homework questions can also be found in the [2010 homework post](/arsiv/eem311-odevler-2010/).

## Homework I: Three-transistor amplifier

The circuit is given with V_CC = 10 V, β = 100 and V_BE(on) = 0.7 V. The base divider of the first npn transistor is 730 kΩ and 270 kΩ; the emitter resistor is 10 kΩ, and in parallel with it there is an AC branch with 100 µF and 230 Ω. The second transistor is pnp; a 270 kΩ resistor to ground and a 100 µF bypass capacitor are connected at its base node. The resistor on the emitter side of the second stage is 730 kΩ. The third transistor is an emitter follower; its collector is connected to the supply and its emitter to a 5 mA current source. The output goes through 100 µF to a 1 kΩ load. The collector resistor of the second stage is 10 kΩ.

### DC solution of the first stage

Equivalent of the base divider:

V_BB1 = (270/1000)·10 = 2.7 V

R_B1 = 270 kΩ ∥ 730 kΩ = 197.1 kΩ

2.7 = 0.7 + (β + 1)I_B1·10 kΩ + I_B1·197.1 kΩ

2 V = (1207.1 kΩ)I_B1

**I_B1 = 1.657 µA**, **I_C1 = 0.1657 mA**

### DC solution of the output stage

I_B3 + I_C3 = 5 mA

(β + 1)I_B3 = 5 mA

**I_B3 = 0.04950 mA**, **I_C3 = 4.9504 mA**

### Node equations of the second stage

With respect to node B₂, the note establishes the following two relations:

I_T + I_E2 = I_C1 + I₁

I₁ = I_B2 + I

In an intermediate step, I₁ ≈ 13.7 µA is found, and:

βI_B2 − I = 0.152 mA

0 = (730 kΩ)I_B2 − 0.7 + (270 kΩ)I

Next to the joint solution, **I_B2 = 1.566 µA** and **I = 0.0346 mA** are written. On another line, I_C2 ≈ 0.1566 mA is shown.

The operating point list in the photograph:

| Transistor | Q(I_C, V_CE) as written in the list |
| --- | --- |
| Q₁ | (0.1657 mA, 7.73 V) |
| Q₂ | (3.46 mA, 6.339 V) |
| Q₃ | (4.9504 mA, 2.321 V) |

*Note: The 3.46 mA for Q₂ in the results list is inconsistent with I_B2 = 1.566 µA and β = 100 on the same page; these two give I_C2 = 0.1566 mA. Since 3.46 mA is used in the subsequent small-signal calculations, the inconsistency carries through. The list was transcribed without correction.*

### Small-signal parameters

Using V_A = 100 V, the relations r_o = (V_A + V_CE)/I_C and r_π = βV_T/I_C are written. The values used in the draft:

| Parameter | Value |
| --- | --- |
| r_o1 | approximately 650 kΩ |
| r_o2 | approximately 30.73 kΩ |
| r_o3 | approximately 20.68 kΩ |
| r_π1 | 15.08 kΩ |
| r_π2 | 722.54 Ω |
| r_π3 | 505.0097 Ω |

Input resistance:

R_in = 730 kΩ ∥ 270 kΩ ∥ 15.08 kΩ = **14.0142 kΩ**

The overall gain is written as the product of the stage ratios:

A_v = (v_out1/v_in1)(v_out2/v_in2)(v_out3/v_in3)

The last numerical line gives **A_v = −10.4923**.

In the output resistance calculation, the input is zeroed and a test voltage is applied at the output. At the end of the page, **R_out = r_o3/2** is written; the algebra in between is missing in places.

*Note: The physical connection of the third stage is an emitter follower; the AC equivalent in the photograph, however, is drawn as if the emitter were grounded. Therefore the gain of −10.4923 and the output resistance of r_o3/2 are not verified results for the original circuit. The input resistance calculation, the parallel combination, is consistent at approximately 14.01 kΩ.*

## Nine-transistor op-amp design with two differential stages

The circuit in the second draft is divided into three blocks: the **first differential amplifier**, the **second differential amplifier**, and the **output stage**. The first differential pair is Q₁–Q₂; its current source is Q₃–Q₄. The second differential pair is Q₅–Q₆; its current source is Q₇–Q₈. Q₉ drives the output as an emitter follower. The inputs are marked as terminals 1 and 2, and the output as terminal 3.

The supplies are +5 V and −5 V. In the note, the collector resistors are R₁ = R₂ = 5 kΩ, R₄ = R₅ = 5 kΩ; the output stage has R₆ = 10 kΩ. In the base current calculation, R_B3 = 1 MΩ is used. It is stated that the resistors were chosen according to the circuit and the gain calculation.

### DC analysis

For the first current source, I_B3 = 4.3 µA was found from the calculation 4.3 V/1 MΩ. The base current of the second stage is written as I_B5 = 0.36 mA/β = 3.6 µA. On the next line:

I_B7 = I_B4 − I_B5 = 5.26 µA − 3.6 µA = 1.66 µA

I_C7 = **0.166 mA**

I_C8 = 0.720 − 0.166 = **0.554 mA**

The following Q points appear in the results list:

| Transistors | Q(I_C, V_CE) as written in the source |
| --- | --- |
| Q₁, Q₂ | (0.298 mA, 4.05 V) |
| Q₃ | (0.43 mA, 0.7 V) |
| Q₄ | (0.596 mA, 5.7 V) |
| Q₅, Q₆ | (0.360 mA, 3.90 V) |
| Q₇ | (0.166 mA, 5 V) |
| Q₈ | (0.554 mA, 4.7 V) |
| Q₉ | (0.306 mA, 1.94 V) |

Steps used for Q₉:

I_E9 ≈ I_C9 = 0.306 mA

V_E9 = 0.306 mA·10 kΩ = 3.06 V

V_CE9 = 5 − 3.06 = **1.94 V**

### AC analysis

The small-signal emitter resistances are calculated with the relation r_e = 26 mV/I_E. The input resistance of the following stage is taken into account as the load of the preceding stage; at the top of the page there is the note **"half of the input resistance of the next stage"**.

For the single-ended output of the differential stage, the gain form used, with the loaded collector resistance shown as R_C ∥ R_in,next, is:

A_v ≈ −(R_C ∥ R_in,next)/(2r_e)

For the output follower, r_e9 ≈ 84.97 Ω is written. There is a gain calculation for the output stage through R_L ∥ R₆, the product of the gains of the two differential stages and the output stage, and also a **CMRR_dB = 20 log₁₀|A_d/A_cm|** calculation. The final figures for the total gain and the CMRR cannot be read clearly enough in the photographs; they were not guessed.

*Note: This section is a design draft. The operating point list and the formulas preserve the lines that could be read; since not all node voltages and current directions could be read clearly, no independent verification could be made for the circuit as a whole.*
