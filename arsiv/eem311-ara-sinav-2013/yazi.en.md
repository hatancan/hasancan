---
baslik: EEM311 Electronics II: 2013 Fall Midterm Exam Questions and Solutions
ozet: Five questions and solutions from the EEM311 Electronics II midterm exam of 18 November 2013: Class A emitter follower (efficiency), current-source-biased differential amplifier, lower cutoff frequency of an emitter follower, design of a bridge-output amplifier with two op-amps, and current gain of a Darlington pair.
---

This post presents the **2013-2014 fall semester midterm exam** (18.11.2013) of the **EEM 311 Electronics II** course in the Electrical-Electronics Engineering department at Başkent University. The source is photos of an exam paper shared by a friend; the paper contains the printed questions and solutions marked with points in red. Personal information has been removed. The questions and the main steps of the solutions were transcribed from the photographed pages into text; the photographs themselves are not published.

The exam lasted 100 minutes, and the point distribution is as follows:

| Question | 1 | 2 | 3 | 4 | 5 | Total |
|---|---|---|---|---|---|---|
| Points | 20 | 20 | 23 | 20 | 17 | 100 |

Instructions at the top of the paper: perform all calculations by showing the derivation of the expression used; use the spaces under the questions and the back of the paper for your answers, and do not ask for extra paper.

## Question 1: Class A emitter follower (20 pts)

In the Class A emitter follower circuit below, the DC supply voltages are V⁺ = +12 V, V⁻ = −12 V and the load resistance is R_L = 100 Ω. The transistor parameters are β = 200, V_BE = 0.7 V. The ac output voltage taken from the circuit is a sinusoidal signal varying between +10 V and −10 V. Accordingly:

- a) What should the minimum value of the current I_Q be, and what value of R provides it? (8 pts)
- b) Find the DC input power the circuit draws from the sources when the output voltage v₀ = 0. (4 pts)
- c) Find the ac output power delivered by the circuit and the circuit's percent efficiency. (8 pts)

*Circuit:* Q₁ is an emitter follower (collector connected to V⁺, input v_I). Its emitter is connected both to the output (v_O, to ground through R_L) and to Q₂, which draws the current I_Q. Q₂ and Q₃ form a current mirror; the reference current flows from ground through resistor R into the diode-connected Q₃, and the emitters are connected to V⁻.

### Solution

**a)** I_Q(min) = v_O(max) / R_L = 10 / 0.1 kΩ ⇒ **I_Q(min) = 100 mA**

R = [0 − 0.7 − (−12)] / 100 mA ⇒ **R = 113 Ω**

**b)** P_Q1 = I_Q · V_CE1 = (100 mA)(12 V) ⇒ P_Q1 = 1.2 W

P(source) = 2 I_Q (12 V) = **2.4 W**

**c)** P̄_L = ½ · V_P² / R_L = (10)² / (2 · 100) = **0.5 W**

P̄_S = 1.2 + 2.4 = 3.6 W

η = P̄_L / P̄_S = 0.5 / 3.6 ⇒ **η = 13.9%**

## Question 2: Current-source-biased differential amplifier (20 pts)

For the transistors in the circuit below, V_A = ∞ (Early voltage) is given. Given that the DC current source I_Q is ideal, draw the ac (small-signal) equivalent circuit of the circuit (6 pts) and derive the expression for the differential-mode gain: A_d = V_o / V_d = ? (V_d = V₁ − V₂) (14 pts)

*Circuit:* The emitters of Q₁ and Q₂ are joined and connected to V⁻ through the current source I_Q. The collector of Q₁ is connected directly to V⁺, and the collector of Q₂ is connected to V⁺ through R_C; the output v_O is taken from the collector of Q₂, and R_L is connected from this node to ground. The inputs are v₁ (base of Q₁) and v₂ (base of Q₂).

### Solution

In the equivalent circuit, each transistor is modeled with r_π and a dependent current source g_m·V_π; the ideal current source is an open circuit in ac, and R_C and R_L are in parallel in ac.

KVL equation: v₁ = V_π1 − V_π2 + v₂, i.e., v₁ − v₂ = V_π1 − V_π2

KCL equation (emitter node):

V_π1 / r_π + g_m V_π1 + g_m V_π2 + V_π2 / r_π = 0 ⇒ (V_π1 + V_π2)(1/r_π + g_m) = 0 ⇒ V_π1 = −V_π2

Hence v₁ − v₂ = −2 V_π2, i.e., V_π2 = −½ (v₁ − v₂).

v_o = −g_m V_π2 (R_C ‖ R_L) = ½ g_m (R_C ‖ R_L)(v₁ − v₂)

For v₁ − v₂ ≡ v_d: **A_d = v_o / v_d = ½ g_m (R_C ‖ R_L)**

## Question 3: Frequency response of an emitter follower (23 pts)

For the amplifier circuit below, β = 100, C_o = 1 µF, r_e = 31 Ω, r_o = 143 kΩ (the "r_e" symbol is not clearly legible in the photo; the solution uses r_π = 3.10 kΩ, which corresponds to (1+β)·31 Ω):

- a) Find the lower cutoff frequency. (7 pts)
- b) Calculate the midband gain A_vmid of the circuit, taking R_S and R_L into account. (6 pts)
- c) Sketch the frequency response with the gain shown in dB. (5 pts)
- d) Calculate the gain of the circuit for an input signal with a frequency of 10 Hz. (5 pts)

*Circuit:* Emitter follower supplied with +10 V and −10 V. The source v_s is connected to the base through R_S = 0.5 kΩ; the base is connected to ground through R_B = 100 kΩ. The emitter is connected to −10 V through R_E = 10 kΩ; the output is taken from the emitter through the coupling capacitor C_o to the load R_L = 10 kΩ.

### Solution

**a)** The resistance seen by the coupling capacitor, looking from the emitter, is the output resistance:

R_o = R_E ‖ r_o ‖ [ (r_π + R_S ‖ R_B) / (1 + β) ]

= 10 ‖ 143 ‖ [ (3.10 + 0.5 ‖ 100) / 101 ] = 10 ‖ 143 ‖ 0.0356 kΩ ⇒ **R_o ≅ 35.5 Ω**

τ_S = (R_o + R_L) C_o = (35.5 + 10⁴)(10⁻⁶) ≅ 1 × 10⁻² s

Accordingly, the 3 dB frequency is: **f_L = 1 / (2π τ_S) = 1 / [2π(10⁻²)] = 15.9 Hz**

**b)** In the midband, the capacitor is assumed to be a short circuit:

A_v = v_o / v_i = (r_o ‖ R_E ‖ R_L) / [r_e + (r_o ‖ R_E ‖ R_L)], where r_o ‖ R_E ‖ R_L = 143 k ‖ 5 k = 4.831 kΩ

A_v = 4.831 k / (0.031 k + 4.831 k) = 4.831 / 4.862 ⇒ A_v ≅ 0.9936

When the source resistance is also taken into account (the divider at the input between R_S and the resistance looking into the base): A_vs = v_o / v_s ≅ 0.9936 × 0.999 ⇒ **A_vmid ≅ 0.992**

**c)** The gain curve is a first-order high-pass characteristic that rolls off at 20 dB/decade below f_L = 15.9 Hz and flattens at ≅ 0.99 (≅ 0 dB) above it (in the solution it is drawn on a logarithmic axis from 1 Hz to 1000 Hz).

**d)** For 10 Hz: A = 0.992 / √(1 + (15.9/10)²)

*Note: The result is not written on the solution sheet; if calculated, √(1 + 1.59²) ≅ 1.88, so the gain is ≅ 0.53.*

## Question 4: Two-op-amp amplifier design (20 pts)

An amplifier circuit using two ideal op-amps is shown below. For the circuit:

- a) Derive the expression for the voltage gain of the circuit (A_v = V_L / V₁). (12 pts)
- b) Design the circuit so that A_v = V_L / V₁ = 15 and at the same time |V_o1| = |V_o2| (how should the required resistor values R₁, R₂, R₃, R₄ be chosen?). (8 pts)

*Circuit:* The first op-amp is a non-inverting amplifier (input v_I, R₂ in the feedback path, R₁ between the inverting input and ground); its output is v_O1. The second op-amp is an inverting amplifier (R₃ at the input, R₄ in the feedback path) that takes v_O1 at its input; its output is v_O2. The load R_L is connected between the two outputs, v_L = v_O1 − v_O2.

### Solution

**a)** v_O1 = (1 + R₂/R₁) v_I

v_O2 = −(R₄/R₃) · v_O1 = −(R₄/R₃)(1 + R₂/R₁) v_I

v_L = v_O1 − v_O2 = (1 + R₂/R₁)(1 + R₄/R₃) v_I

Accordingly: **A_v = (1 + R₂/R₁)(1 + R₄/R₃)**

**b)** |v_O1| = |v_O2| is required ⇒ **R₄ = R₃** must hold.

Then (1 + R₂/R₁)(2) = 15 ⇒ **R₂/R₁ = 6.5**

## Question 5: Current gain of a Darlington pair (17 pts)

For the transistors in the circuit below, β = 100, V_A = ∞, r_e1 = 2.03 kΩ, r_e2 = 20.2 Ω are given. Draw the ac (small-signal) equivalent circuit of the circuit (5 pts) and find the current gain: A_i = I_o / I_i = ? (12 pts)

*Circuit:* V_CC = +10 V. Q₁ and Q₂ are connected as a Darlington pair (the emitter of Q₁ is connected to the base of Q₂, and the two collectors are joined and connected to V_CC through R_C = 2.2 kΩ). Base biasing is R₁ = 335 kΩ (to V_CC) and R₂ = 125 kΩ (to ground); the input v_i is connected to the base through the coupling capacitor C_C. The emitter of Q₂ has R_E = 1 kΩ with a parallel bypass capacitor C_E. The output current I_o is the current flowing through R_C.

### Solution

I_o = g_m1 V_π1 + g_m2 V_π2 = β₁ I_b1 + β₂ I_b2, where I_b2 = (β₁ + 1) I_b1

I_o = I_b1 (β₁ + β₂ + β₁β₂) ⇒ I_o / I_b1 = β₁ + β₂ + β₁β₂ ≅ β₁β₂

Resistance seen from the input: R_ib = β₁ r_e1 + β₁β₂ r_e2 = 100 (2.03 k + 2.02 k) = 100 (4.05 k) ⇒ R_ib = 405 kΩ

R₁ ‖ R₂ = 125 k ‖ 335 k = 91.03 kΩ

Current divider: I_b1 / I_i = (R₁ ‖ R₂) / [(R₁ ‖ R₂) + R_ib] = 91.03 k / (91.03 k + 405 k) ≅ 0.183

A_i = (I_o / I_b1) · (I_b1 / I_i) ≅ β₁β₂ · 0.1835 ⇒ **A_i ≅ 1835**
