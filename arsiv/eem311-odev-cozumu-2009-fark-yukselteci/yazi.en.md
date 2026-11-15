---
baslik: EEM311 Electronics II: 2009 Homework Questions and Solution Draft, Differential Amplifier and MOSFET–BJT Multistage Amplifier
ozet: Handwritten homework questions and a solution draft for EEM311 Electronics II (December 2009): Q-points of a differential amplifier with current sources and a PNP active-loaded output stage, operating points of an NMOS–PNP–PMOS three-stage amplifier, and the AC equivalent circuit.
---

This post contains a three-question homework or practice problem set, handwritten on paper, along with an unfinished solution draft for the **EEM311 Electronics II** course (December 2009; it was found in the archive among the laboratory notes). **It is a friend's work; personal information has been removed.** The pages were **transcribed to text from photographed pages**; the circuit diagrams are described in words. This post has no downloadable file.

## Question 1: Differential amplifier

The differential amplifier circuit shown in the figure uses balanced circuit elements. The circuit: Q1–Q2 is an npn differential pair (collector resistors R_C1, emitters tied to −V_EE through current source I1, inputs V_A and V_B); the collector of Q2 is connected to the base of the pnp differential pair Q3–Q4 (the emitters of Q3–Q4 are fed by current source I2, and the collector resistors R_C2 go to −V_EE); the collector of Q4 drives the base of the pnp output transistor Q5, the emitter of Q5 is fed by source I3, and the output V_o is delivered to the load R_L.

- For npn transistors: β = 100, V_A = 50 V, V_BE = 0.7 V
- For pnp transistors: β = 50, V_A = 70 V, V_EB = 0.7 V
- V_T = 25 mV, V_CC = V_EE = 3 V
- R_C1 = 300 kΩ, R_C2 = 78 kΩ, R_L = 7 kΩ
- I1 = 10 µA, I2 = 50 µA, I3 = 250 µA, V_o = 0 at DC

a) Find the Q-points of the transistors: Q(I_CQ, V_CEQ).

b) Draw the small-signal AC equivalent of the circuit; calculate the gain: A_v = V_o / (V_A − V_B), R_in = ?, R_out = ?

### Solution draft

- Output stage: I_C5 + I_B5 = 250 µA → 51·I_B5 = 250 µA → I_B5 = 4.9 µA, I_C5 = 2.45 × 10⁻⁴ A.
- Q3–Q4 stage: I_C4 + I_B4 = 25 µA → 51·I_B4 = 25 µA → I_B4 = 0.47 µA, I_C4 = 50·0.47 µA = **23.5 µA**; likewise I_B3 = 0.47 µA, I_C3 = 23.5 µA. The R_C2 current was taken as I_C4 + I_B5 ≈ 23.5 µA.
- Input stage: I_C2 + I_B4 = 5 µA → I_C2 = 5 µA − 0.47 µA = **4.53 µA**, I_C1 = 4.53 µA.
- V_CE1 = 6 − I_C1·R_C1 = 6 − 4.53 µA·300 kΩ = 4.64 V; V_CE2 = 4.64 V.
- V_CE3 = −6 + I_C3·78 kΩ = −6 + 1.833 = −4.167 V; V_CE4 = −4.167 V; V_CE5 was not found.
- Result: Q1(4.53 µA, 4.64 V), Q2(4.53 µA, 4.64 V), Q3(23.5 µA, −4.167 V), Q4(23.5 µA, −4.167 V).

*Note: The V_CE calculations used the total supply (V_CC + V_EE = 6 V) but did not account for the emitter voltages. With the inputs at ground, the emitters of Q1 and Q2 are at ≈ −0.7 V, so V_CE1 = 3 − 4.53 µA·300 kΩ + 0.7 ≈ 2.34 V.*

## Question 2: Three-stage MOSFET–BJT amplifier

V_CC = 10 V. M1 (NMOS) is a common-source stage: the gate is biased through a 20 kΩ–80 kΩ voltage divider, with a 2 kΩ resistor in the drain and a 5 kΩ resistor in the source. The drain of M1 is connected to the base of the transistor Q1 (PNP); Q1 has 150 Ω in the emitter (to V_CC) and 700 Ω in the collector (to ground). The collector of Q1 drives the gate of the transistor M2 (PMOS); one terminal of M2 is connected to V_CC and the other terminal is connected to ground through a 50 Ω resistor; the output V_o is taken across this resistor.

- β = 100, V_EB = 0.7 V, V_TN = 2 V, V_TP = −1 V
- K_n = 8.8 mA/V², K_p = 50 mA/V², λ = 0

a) Find the operating points of the amplifier; find the voltages at the nodes V_G, V_S, V_B, V_E, V_C, V_O.

b) Check whether the FETs are in saturation.

### Solution draft

- V_G = 80 k / 100 k · 10 V = **8 V**
- I_D = (K_n/2)(V_GS − V_TN)²; −V_G + V_GS + I_D·5 kΩ = 0 was written, and with K_n/2 = 4.4 the equation 4.4·V_GS² − 16.6·V_GS + 9.6 = 0 was solved: V_GS = 3.059 V (the other root is 0.713 V), I_D = 4.4 × 10⁻³·(1.059)² = **4.93 mA**; Q1(4.93 mA, 3.059 V).
- Equations such as V_DS = 10 − I_D(R_S + R_D), V_B = V_DS + I_D·5 kΩ, V_S = I_D·5 kΩ, and −10 + 150·I_E − V_CE + 700·I_C = 0 for Q1 were then set up; for M2, I_D = (K_p/2)(V_GS − V_TP) ² = 25 × 10⁻³(V_GS + 1)² and V_DS = 10 − I_D·50 were written. The numerical results were not completed.

*Note: Since K_n/2 = 4.4 mA/V², the I_D·5 kΩ term in the equation should give a coefficient of 4.4 mA·5 kΩ = 22 V/V²: 8 = V_GS + 22(V_GS − 2)². This equation gives V_GS = 2.5 V, I_D = 4.4 mA/V²·(0.5 V)² = **1.1 mA** and V_S = 5.5 V. The 4.93 mA result in the draft is not possible, since it would make the source voltage (4.93 mA·5 kΩ ≈ 24.7 V) larger than the supply.*

## Question 3: AC equivalent and gain

a) Draw the AC equivalent of the circuit given in Question 2.

b) Find the gain of each stage separately; using these gains, find the overall gain: A_vT = V_o / V_G = ?

### Solution draft

In the AC equivalent, the input resistance is 20 kΩ ∥ 80 kΩ = **16 kΩ**. The first stage (M1, 5 kΩ in the source) with the 2 kΩ drain resistor at node A; the second stage (Q1: rπ, β·i_b source, 150 Ω in the emitter, 700 Ω in the collector), node B; and the third stage (M2, 50 Ω in the source, output node C) were drawn. The overall gain was written as the product of the stage gains:

A_v = (A / v_i)·(B / A)·(v_o / B) = v_o / v_i

The numerical gains were not calculated.
