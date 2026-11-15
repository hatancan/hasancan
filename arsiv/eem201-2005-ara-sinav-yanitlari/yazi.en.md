---
baslik: EEM201 Circuit Theory I: 2005–2006 Fall Midterm Exam and Answers
ozet: Solutions to the fall 2005 exam on Thevenin equivalents, maximum power transfer, and two-stage ideal operational amplifier circuits.
---

This post contains two questions and four answer pages from the **2005–2006 fall midterm exam** of Başkent University's **EEM201 Circuit Theory I** course. The question sheet carries the names of Prof. Dr. Turhan Çiftçibaşı and Lecturer Mustafa Doğan. It was transcribed from photographed pages stored in the EEM202 folder. The exam does not state its day and month; the archive date is 30 November 2005, the date of the source files. The photographs and the download file are not published.

## Question 1: Thevenin equivalent of a circuit with a dependent source

V₁ = 0.3 V is given. Find the Thevenin equivalent seen from terminals a–b; calculate the current i₀ when 1 Ω is connected between a and b. The circuit contains two 1 Ω resistors, a dependent voltage source of value 4V₁, and a current-controlled voltage source of value i₁.

In the open-circuit calculation:

- Vₐ = V_oc + 4V₁ = V_oc + 1.2.
- Vₐ = −i₁·1 + 0.3 = −i₁ + i₁ = 0.
- **V_oc = −1.2 V.**

In the short-circuit calculation, Vₐ = 1.2 V and i₁ = −0.9 A are found. By KCL, **I_sc = −1.2 A**; therefore **R_Th = V_oc/I_sc = 1 Ω**.

When a 1 Ω load is connected, i₀ = V_oc/(R_Th + 1) = **−0.6 A**.

## Question 2: Maximum power transfer

The a–b equivalent of a circuit containing independent sources of 2 A and 4 V and a dependent current source 2Vₓ is requested, along with the load R for maximum power. The resistors are 1 Ω, 2 Ω, 0.5 Ω and 1 Ω; there is a 1 V source between d–c. Vₓ is the load terminal voltage.

In the open-circuit case, nodes d and c form a supernode. The equations on the page are:

- 2 + V_d − (Vₐ − V_d)/2 + 2V_oc − (Vₐ − V_c)/0.5 = 0
- (Vₐ − V_c)/0.5 + (Vₐ − V_d)/2 + Vₐ − 4 = 0
- V_d − V_c = 1 and Vₐ = V_oc.

The first working lines on the solution page are corrected in red; the result is **V_oc = 7/11 V**. In the short-circuit case, Vₐ = 0, V_c = −1 V and V_d = 0; **I_sc = 2 A** is found.

**R_Th = 7/22 Ω.** For maximum power, R = R_Th is chosen. The load current is 1 A and **P_max = 7/22 W**.

*Note: A check calculation confirms the result P_max = V_oc²/(4R_Th) = 7/22 W. The corrected results were used; intermediate steps that were crossed out were not reproduced.*

## Question 3: Two-stage op-amp

All op-amps are ideal and their supplies are ±5 V. In each stage the input resistors are 1 kΩ and the feedback resistor is 3 kΩ. V₂/2 is applied to the non-inverting input of the first stage, and V₃/2 to that of the second stage.

Node equations:

- (V₁ − V₂/2)/1k + (V_o1 − V₂/2)/3k = 0
- **V_o1 = 2V₂ − 3V₁**
- (V_o1 − V₃/2)/1k + (V_o − V₃/2)/3k = 0
- **V_o = 2V₃ − 3V_o1 = 2V₃ − 6V₂ + 9V₁**

| Inputs | First stage | Second stage |
|---|---|---|
| V₁ = 1 V, V₂ = 2 V, V₃ = 3 V | V_o1 = 1 V | V_o = 3 V |
| V₁ = −2 V, V₂ = 3 V, V₃ = 4 V | Calculated 12 V; 5 V due to supply | Calculated −7 V; −5 V due to supply |

*Note: The linear op-amp relations are valid only when saturation does not occur. The saturation limits in the second row were applied as in the solution page.*

## Question 4: Output voltage and output current

A 1.1 V source is connected through 3 kΩ to the inverting input of the first op-amp; the first feedback is 18 kΩ, and the feedback from the second output to the same node is 24 kΩ. The second op-amp has a 3 kΩ/27 kΩ feedback divider at its negative input and a 1.6 kΩ load at its output.

- (−1.1)/3k − V_o1/18k − V_o/24k = 0 ⇒ −4V_o1 − 3V_o = 26.4
- V_o1/27k + (V_o1 − V_o)/3k = 0 ⇒ V_o1 = 0.9V_o
- **V_o = −4 V**, V_o1 = −3.6 V.

Currents at the output node: i_24k = −1/6 mA; i_1.6k = −2.5 mA; in the feedback branch i_30k = −2/15 mA. From KCL, **i₀ = 2.8 mA**.
