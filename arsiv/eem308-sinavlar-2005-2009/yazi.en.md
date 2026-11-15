---
baslik: EEM308 Signals and Systems II: 2005 Midterm and 2009 Quiz 3 Questions (EEM 302)
ozet: The 2004-2005 spring midterm of EEM 302 Signals and Systems II (steady-state response to sinusoidal input, stability and minimum phase, unit-step response of a difference equation, z-transform via convolution) and the 22 May 2009 quiz 3 question (all-pass system).
---

This post presents two past exams from the **EEM 302 Signals and Systems II** course at Başkent University (the course was later offered under the code EEM 308): the **2004-2005 spring semester midterm** prepared by **Lecturer Mustafa Doğan**, and the question written on the board for **quiz 3** on **22 May 2009**. Both were transcribed from photographed pages; the photographs themselves are kept in the archive and are not published. In the midterm photograph, part of the top of the paper is covered by a sticky note; since it is a blank exam paper, it contains no name or student number.

## 2004-2005 spring midterm

Header: *Başkent University Department of Electrical-Electronics Engineering, EEM 302 Signals and Systems II, Midterm — Lecturer Mustafa Doğan*. Rules:

1. One A4 formula sheet prepared in your own handwriting is allowed in the exam. Formula sheets that are found to be photocopies will be confiscated.
1. Everyone will use their own calculator; shared use will absolutely not be permitted.
1. Students who cheat will be punished in accordance with the "Başkent University Disciplinary Regulations".

Points: Question 1: 20, Question 2: 20, Question 3: 30, Question 4: 30; total 100.

### 1. Steady-state response to sinusoidal inputs (20 points)

The transfer function H(s) of an LTI system is given below. Find the steady-state response to the following input:

x(t) = 3 [cos(4t) − √3 sin(4t)]

x(t) → **H(s) = 1/(s² + 4s + 8)** → y_ss(t) = ?

### 2. Stability and minimum phase (20 points)

Which of the following causal LTI systems are **stable**? Which of them are **minimum-phase**? WHY? Please, explain clearly.

- a) H(s) = (s + 10)(10s + 1) / ((0.01s + 1)(s² + s + 1))
- b) H(s) = (10s² + 5s + 10) / (0.1s + 1)
- c) H(z) = (1 + 2z⁻²) / (1 − 0.5z⁻¹)²
- d) H(z) = 1 / ((1 − 0.25z⁻¹)(1 + 0.75z⁻¹))
- e) H(z) = (1 − 2z⁻¹) / (1 + 0.5z⁻¹)
- f) H(z) = z⁻¹ (1 − 0.3z⁻¹) / (1 − 0.25z⁻²)

*Note: The exponents of z in parts c, d and f are blurry in the photograph; the reading above is the most likely one.*

### 3. Unit-step response of discrete-time LTI systems (30 points)

The difference equation of a causal LTI system is:

2y[n] − 2y[n−1] + y[n−2] = x[n]

- a) H(z) = ?
- b) Find the output y[n] for input x[n] = u[n].

### 4. Convolution and the z-transform (30 points)

The transfer function H(z) of a discrete-time LTI system is given below. Find the output y[n] for input x[n] = (2/3)ⁿ for all n. **Hint:** Use convolution sum in discrete-time and then z-transform properties. Do **not** evaluate X(z)!

x[n] → **H(z) = (1 − 0.25z⁻¹) / (1 + (1/3)z⁻¹)** → y[n] = ?

### Brief solution notes

*Note: The exam had no answer key; we calculated the results below ourselves.*

- **Question 1:** x(t) = 3[cos 4t − √3 sin 4t] = 6 cos(4t + 60°). H(j4) = 1/(8 − 16 + j16) = 1/(−8 + j16); |H(j4)| = 1/√320 ≈ 0.0559, ∠H(j4) = −(180° − 63.43°) = −116.57°. Therefore y_ss(t) = (6/√320) cos(4t + 60° − 116.57°) ≈ **0.335 cos(4t − 56.57°)**.
- **Question 3:** H(z) = 1/(2 − 2z⁻¹ + z⁻²) = 0.5 / (1 − z⁻¹ + 0.5z⁻²); the poles are z = 0.5 ± j0.5 = (1/√2)e^(±jπ/4), inside the unit circle (the system is stable). For a unit-step input, the steady-state value is H(1) = 1/(2 − 2 + 1) = 1.
- **Question 4:** (2/3)ⁿ is an eigenfunction: y[n] = H(z)|_{z=2/3} · (2/3)ⁿ = ((1 − 0.375)/(1 + 0.5)) (2/3)ⁿ = **(5/12)(2/3)ⁿ**.

## 22 May 2009 quiz 3

The question written on the board:

H(z) = (z⁻¹ − 0.2) / (1 − 0.2z⁻¹)

Show that |H(e^{jω})| = 1.

*Note: Brief solution: for z = e^{jω}, the numerator is e^{−jω} − 0.2 = e^{−jω}(1 − 0.2e^{jω}). Since |e^{−jω}| = 1, and 1 − 0.2e^{jω} and the denominator 1 − 0.2e^{−jω} are complex conjugates of each other, their magnitudes are equal; hence |H(e^{jω})| = 1. The system is a first-order all-pass filter with its pole at z = 0.2 and its zero at z = 5 (the 1/p reflection of the pole).*
