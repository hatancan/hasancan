---
baslik: EEM311 Electronics II: BJT Amplifier Design and Output Resistance, 2010 Notebook Notes
ozet: Design of a common-emitter BJT amplifier with a gain of −10 and an input resistance of 500 kΩ; derivation of output resistance using a test source for common-base and emitter-resistor amplifiers.
---

This post contains a friend's notebook notes from the **EEM311 Electronics II** course at Başkent University. The pages were **transcribed to text from photographed pages**; personal information has been removed. The photographs were taken on 6 October and 11 November 2010. Two shots of the same page were read together. This post has no downloadable file.

## Operating point and thermal stability

The notes treat the power dissipated in the transistor as P = V_CE·I_C. The operating point is required not to exceed the maximum power hyperbola and to be kept stable against variations in β and temperature. The emitter resistor and feedback are marked as the tools used to keep the operating point stable.

## Common-emitter amplifier design

Given for Example 14.11: **β = 75, A_v = −10, R_in = 500 kΩ**, with source resistance R_s = 100 Ω. R_E is present in the emitter; in the small-signal equivalent, r_π lies between base and emitter, and a dependent current source β·i_b lies in the collector. The load at the output is shown as R_L.

Base voltage and input resistance:

v_b = i_b r_π + (β + 1)i_b R_E

R_in = v_b/i_b = r_π + (β + 1)R_E

The notes use r_π = βr_e and the approximation (β + 1)R_E ≫ βr_e:

R_in ≈ (β + 1)R_E ⇒ R_E ≈ 500 kΩ / 76 = **6.58 kΩ**

Voltage gain:

A_v = −βR_L / [r_π + (β + 1)R_E] = −βR_L / R_in

−10 = −75R_L / 500 kΩ ⇒ **R_L ≈ 66.7 kΩ**

Here the gain's input voltage is defined as v_i at the transistor base; it is not the same node as v_s ahead of the source resistance.

## Output resistance of the common-base circuit

In Example 14.34, the input is connected to the emitter and the output to the collector; the base is at AC ground. The notes state that the T model is used for the gain calculation and the hybrid-π model for the output resistance derivation.

Finite output resistance of the transistor:

r_o = (V_A + V_CE)/I_CQ

For the output resistance calculation, the input voltage source is short-circuited, the load R_L is removed, and a test source v_x is connected to the collector. The current of the test source is i_x; **R_out = v_x/i_x**.

Equivalent resistance from the emitter to ground:

R_eq = r_π ∥ R_4 ∥ R_I

In the notes, R_I denotes the resistance in series with the input source, and R_4 denotes the other resistor at the emitter. Relations:

v_e = −v_be = i_x R_eq

i_ro = i_x − g_m v_be = i_x(1 + g_m R_eq)

v_x = i_ro r_o − v_be

Substituting:

v_x = i_x(1 + g_m R_eq)r_o + i_x R_eq

**R_out = (1 + g_m R_eq)r_o + R_eq**

The result is the resistance found by looking into the transistor stage after the output load has been removed.

## Output resistance of the common-emitter stage with emitter resistor

In the continuation of Example 14.11, the input source is zeroed; the base is connected to ground through R_s, and the emitter is connected to ground through R_E. v_x is applied to the collector. In the notes, the base current is denoted i, and the test current entering the collector is denoted i_x.

R_T = r_π + R_s + R_E

v_e = (i_x + i)R_E = −i(r_π + R_s)

−i = (R_E/R_T)i_x

Thus:

v_e = [R_E ∥ (r_π + R_s)]i_x

i_ro = i_x − βi = i_x[1 + βR_E/R_T]

v_x = i_ro r_o + v_e

**R_out = [1 + βR_E/(r_π + R_s + R_E)]r_o + [R_E ∥ (r_π + R_s)]**

The resistance symbol inside the parentheses on the last line, which is written a second time in the notebook, is unclear; the explicit derivation above was taken as the basis here. The page gives no numerical result for this output resistance.
