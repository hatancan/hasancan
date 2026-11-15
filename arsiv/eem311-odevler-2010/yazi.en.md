---
baslik: EEM311 Electronics II: Fall 2010 Homework, Multistage BJT Amplifier and Two-Stage Differential Amplifier Design
ozet: Two homework assignments from the Fall 2010 semester of EEM311 Electronics II: the input/output impedance, gain, and unclipped swing of a multistage amplifier with 2N2222A transistors; the design of an amplifier with |Av| = 200 and a two-stage differential amplifier with a differential-mode gain of 100–150, together with the CMRR calculation.
---

This post contains two homework assignments given in the Fall 2010 semester of the **EEM311 Electronics II** course in the Electrical-Electronics Engineering Department at Başkent University: **Homework I** (October 26, 2010) and **Homework II** (November 28, 2010). The homework sheets contain only the questions and circuit schematics; there are no solutions. The text of the questions is given below, with the circuit schematics shown as images taken from the assignments. The original PDFs of both assignments can be downloaded as a ZIP at the end of the post.

## Homework I

**1)** For the circuit below, find:

- a) the input and output impedances,
- b) the voltage gain A_v,
- c) the zero-to-peak unclipped swing.

![Homework I circuit: Vcc = 10 V; Q1, Q2 and Q3 are 2N2222A/ZTX; Q1 base biased with RRB = 730k and RB = 270k, input from source V2 through C2 = 100u; RE = 10k at the Q1 emitter, with RG = 230 Ω through C3 = 100u; Q2 base biased with RB3 = 730k and RB4 = 270k and grounded through C4 = 100u; RC = 10k; Q3 output stage fed by a 5 mA IQ current source, output through C1 = 100u to a load RL = 1k](odev1-devre.jpg "Homework I, Question 1: three-transistor amplifier circuit")

Component values in the circuit:

| Component | Value |
|---|---|
| V_CC | 10 V |
| Q1, Q2, Q3 | 2N2222A/ZTX |
| RRB, RB3 | 730 kΩ |
| RB, RB4 | 270 kΩ |
| RE | 10 kΩ |
| RG | 230 Ω |
| RC | 10 kΩ |
| C1, C2, C3, C4 | 100 µF |
| IQ (Q3 emitter current source) | 5 mA |
| RL | 1 kΩ |

**2)** Calculate the resistor and current values required for a circuit that satisfies the following conditions without distorting the signal:

- V_CC = 10 V
- R_L = 1 kΩ
- |A_v| = 200
- R_in ≥ 3 kΩ
- Unclipped swing at V_out ≥ 2.5 V
- V_E1 ≥ 1 V

## Homework II

![Homework II circuit: two-stage differential amplifier with a 5 V supply; first stage Q1–Q2 (load resistors R1, R2, inputs IN1 and IN2), tail current provided by a Q3–Q4 current mirror and R3; second stage Q5–Q6 (R4, R5), tail current provided by a Q7–Q8 current mirror; Q9 emitter follower, R6, C1 and RL at the output; negative supplies V2 and V3 of 5 V](odev2-devre.jpg "Homework II: two-stage differential amplifier")

1. Design the two-stage differential amplifier above so that its differential-mode gain is between 100 and 150 (C1 = 100 µF and R_L = 10 kΩ).
1. Calculate the DC bias points of the transistors, and explain the function of each resistor and transistor.
1. Calculate the CMRR.

In the schematic, the two collector outputs of the first stage (Q1–Q2) drive the bases of the second stage (Q5–Q6); the tail current of each stage is provided by a BJT current mirror (Q3–Q4 and Q7–Q8), and Q9 is an emitter-follower stage that passes the single-ended output to the load R_L. For the gain and CMRR relations of differential amplifiers, see the differential amplifier lab handout in the archived post "EEM311 Electronics II: Experiments 7–8".
