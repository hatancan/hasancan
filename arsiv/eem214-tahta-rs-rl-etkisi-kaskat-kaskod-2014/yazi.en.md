---
baslik: EEM214 Electronics I: Effect of Source and Load Resistance, Cascade and Cascode Connections (Board Notes, 2014)
ozet: What was written on the board in the EEM214 Electronics I lecture of 16 May 2014: the two-port amplifier model using the systems approach, the effect of R_s and R_L on voltage and current gain, a numerical example, an emitter follower + common-base cascade amplifier example, a two-stage common-emitter amplifier problem, and the gain of the cascode connection.
---

This post records what was written on the board in the EEM214 Electronics I lecture of **16 May 2014**. The topics are modeling amplifiers using the **systems approach** (as two-port networks), the effect of the source resistance R_s and the load resistance R_L on gain, and multistage (cascade, cascode) amplifiers. The text was transcribed from phone photographs of the board; the photographs themselves were not published because they show people. The circuit diagrams are described in words. The quiz and final questions from the same period are in the post [2014 Quiz 2 and final answer key](/arsiv/eem214-quiz-2-final-2014/).

## Effect of R_s (source resistance) and R_L (load resistance)

In the systems approach, an amplifier is represented as a two-port block as follows: an input resistance R_i at the input, and at the output a dependent voltage source A_vNL·v_i in series with the output resistance R_o. The source v_s is connected to the input through R_s, and the load R_L is connected to the output. The unloaded (no-load) gain is:

v_o = A_vNL·v_i ⇒ v_o/v_i = A_vNL

**Effect of R_s:** The input voltage is found with a voltage divider:

v_i = v_s·R_i/(R_i + R_s) ⇒ v_i/v_s = R_i/(R_i + R_s)

A_vs (unloaded) = v_o/v_s = (v_o/v_i)·(v_i/v_s) = **A_vNL·R_i/(R_i + R_s)**

The factor R_i/(R_i + R_s) here is the effect of R_s. The input current is I_i = V_i/R_i if there is no R_s; with R_s present, I_s = V_s/(R_s + R_i).

**Effect of R_L:** If R_L is present,

V_oL = (A_vNL·V_i)·R_L/(R_o + R_L) ⇒ V_oL/V_i = A_vL = A_v(loaded) = **A_vNL·R_L/(R_o + R_L)**

The factor R_L/(R_o + R_L) here is the effect of R_L.

**With both R_s and R_L present:**

A_vs(loaded) = V_oL/V_s = (V_oL/V_i)·(V_i/V_s) = **A_vNL·[R_L/(R_o + R_L)]·[R_i/(R_s + R_i)]**

**Current gains:**

- Loaded current gain: **A_iL = −A_vL·R_i/R_L**
- With both the load and R_s present: **A_is = −A_vs·(R_s + R_i)/R_L**

## Example: Effect of R_s and R_L

Amplifier: A_vNL = −480, Z_i = 4 kΩ, Z_o = 2 kΩ; R_s = 0.2 kΩ. Questions: For R_L = 1.2 kΩ, what are A_vL and A_vs(loaded)? For R_L = 5.6 kΩ, what are A_vL and A_i = I_o/I_i = I_o/I_s?

- R_L = 1.2 kΩ: A_vL = A_vNL·R_L/(Z_o + R_L) = −480·1.2k/(2k + 1.2k) = **−180**
- A_vs(loaded) = A_vL·Z_i/(Z_i + R_s) = −180·4k/(4k + 0.2k) = **−171.36**
- R_L = 5.6 kΩ: A_vL = A_vNL·5.6k/(5.6k + 2k) = **−353.76**
- A_iL = −A_vL·Z_i/R_L = −(−353.76)·4k/5.6k = **252.6…** (the last digits are cut off in the photograph)

*Note: A_vs(loaded) = −171.36 is written on the board; the calculation −180·4/4.2 gives −171.43.*

## Example: Two-stage cascaded amplifier

A source with R_s = 1 kΩ, the first stage an **emitter follower** (Z_i = 10 kΩ, Z_o = 12 Ω, A_vNL ≅ 1), the second stage a **common-base** stage (Z_i = 26 Ω, Z_o = 5.1 kΩ, A_vNL = 240), and a load R_L = 8.2 kΩ. Z_i = Z_i1, Z_o2 = Z_o. Questions:

- a) What is the loaded gain of each stage?
- b) What are the overall gains A_vL and A_vsL of the circuit?
- c) What is the overall (loaded) current gain A_iL of the circuit?
- d) If the first stage is removed, what is the overall gain A_vsL of the remaining circuit?

Equivalent circuit: v_s – 1 kΩ – 10 kΩ (input of the 1st stage); the A_vNL1·v_i1 source – 12 Ω – 26 Ω (the input of the 2nd stage is the load of the 1st stage); the A_vNL2·v_i2 source – 5.1 kΩ – R_L = 8.2 kΩ.

- a) A_v1L = A_vNL1·26 Ω/(26 Ω + 12 Ω) = **0.684**; A_v2L = A_vNL2·8.2k/(5.1k + 8.2k) = **147.97**
- b) A_vL = v_o/v_i1 = A_v1L·A_v2L = 0.684·147.97 = **101.2**; A_vsL = v_o/v_s = A_vL·10k/(1k + 10k) = **92**
- c) A_iL = −A_vL·Z_i/R_L = −101.2·… (the photograph was taken before the result was written)
- d) When the first stage is removed, the source (1 kΩ) is connected directly to the 26 Ω input: A_vL = A_vNL2·8.2k/(8.2k + 5.1k) = 147.97; A_vs = A_vL·26 Ω/(26 Ω + 1 kΩ) = 147.97·26/1026 = **3.7**

Conclusion: When a high-input-resistance emitter follower is placed in front of the low-input-resistance common-base stage, the overall gain rises from 3.7 to 92.

## Problem: Two-stage common-emitter amplifier

Circuit: two identical common-emitter stages, V_CC = 20 V; in each stage a voltage divider with R1 = 15 kΩ, R2 = 4.7 kΩ, R_C = 2.2 kΩ, R_E = 1 kΩ (bypassed with C_E = ∞); the stages and the input and output are coupled with C = ∞ capacitors; β₁ = β₂ = 200, r_o = ∞; input v_i = 25 µV.

- a) Perform the DC analysis of the circuit and find the small-signal parameters (r_e, r_π, g_m, …).
- b) Find the overall gain of the circuit. Find V_o.
- c) If a load R_L = 4.7 kΩ is connected to the circuit, find the overall gain. Find V_o.
- d) If the internal resistance of the source is R_s = 1 kΩ, find A_vsL.

AC equivalent circuit drawn on the board: at the input, 15k ∥ 4.7k ∥ βr_e; at the output of the first stage, in parallel with the β·I_b1 current source, 2.2k ∥ 15k ∥ 4.7k ∥ βr_e2, i.e. **R_L1 = R_i2** (the load of the first stage is the input resistance of the second stage); in the second stage, the β·I_b2 current source and 2.2 kΩ. The numerical solution is not in the photographs.

## Cascode connection

Circuit: the first transistor (npn) is common-emitter (R_B1, R_B2 divider, R_C, R_E and C_E), and its collector is connected to the emitter of the second transistor (written as pnp on the board); the second transistor is common-base (its base is at AC ground through R_B and C_B), and the output is taken from the collector across R_L. V_o1 = V_i2.

Small-signal equivalent: at the input, R_B1 ∥ R_B2 and β₁r_e1; at the output of the first stage, the β₁I_b1 current source, R_C and the input resistance of the second stage r_e2 (**R_i2 = R_L1**); in the second stage, the α·I_e current source and R_L.

- A_v1L = −β₁I_b1·(R_C ∥ r_e2) / (I_b1·β₁r_e1) = **−(R_C ∥ r_e2)/r_e1**
- A_v2L = α·I_e·R_L / (I_e·r_e2) = **α·R_L/r_e2**
- A_vTL = **−[(R_C ∥ r_e2)/r_e1]·α·R_L/r_e2**

Since R_C ∥ r_e2 ≈ r_e2, the gain of the first stage is approximately −1; almost all of the gain is provided by the common-base second stage.
