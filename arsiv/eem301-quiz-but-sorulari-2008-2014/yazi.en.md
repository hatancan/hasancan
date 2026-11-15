---
baslik: EEM301 Signals and Systems I: Solutions to 2008–2016 Quiz, Makeup Exam, and Exam Questions
ozet: Solutions to the EEM301 Signals and Systems I course's 2008 blackboard quiz questions, 2013–2014 Quiz 1 and 2, the 27.01.2014 makeup exam, and two exam questions from January 2016: convolution, the q- and p-operators, Fourier series, frequency response, and the Fourier transform.
---

This post brings together quiz and makeup exam questions from different years of Başkent University's **EEM301 Signals and Systems I** course: two quizzes written on the blackboard in fall 2008, Quiz 1 and 2 of the 2013–2014 fall semester (Prof. Dr. Alper Uraz), the 27 January 2014 makeup exam, and the solutions to two Fourier transform questions from January 2016. The questions and solutions were transcribed into text from photographed pages (blackboard, exam paper, and solution sheets); the photographs were not published, so there are no downloadable files. Personal information on student papers was not transcribed.

## Quiz 2 (13 November 2008)

The question written on the blackboard:

- x[n] = u[n + 10] − 2u[n] + u[n − 4], h[n] = u[n − 2]
- y[n] = x[n] ∗ h[n] = ?

*Note: No solution was written on the blackboard along with the question. Since h[n] = u[n − 2], y[n] = Σ_{k=−∞}^{n−2} x[k], i.e., the cumulative sum of x up to n − 2: 0 for n < −8, n + 9 for −8 ≤ n ≤ 1, 10 − (n − 1) = 11 − n for 2 ≤ n ≤ 5, and 6 for n ≥ 6.*

## Quiz 3 (4 December 2008)

1. A continuous-time causal LTI system dy(t)/dt + 4y(t) = x(t). For x(t) = cos 2πt, y(t) = ? (Hint: y(t) = Σ a_k H(jkω₀) e^(jkω₀t).)
1. For the signals x(t) = cos 4πt, y(t) = sin 4πt, and z(t) = x(t)y(t) with period T = 1/2: (a) x(t) ⟷ a_k = ?, (b) y(t) ⟷ b_k = ?, (c) using the multiplication property, z(t) ⟷ c_k = ?

*Note: There is no solution on the blackboard. In question 1, since H(jω) = 1/(jω + 4) and a₁ = a₋₁ = 1/2, y(t) = |H(j2π)| cos(2πt + ∠H(j2π)) = cos(2πt − tan⁻¹(π/2)) / √(16 + 4π²). In question 2, a₁ = a₋₁ = 1/2, b₁ = 1/(2j), b₋₁ = −1/(2j); c_k = Σ a_l b_(k−l) ⇒ c₂ = 1/(4j), c₋₂ = −1/(4j), all others 0 (z(t) = ½ sin 8πt).*

## 2013–2014 Quiz 1 (25.10.2013)

Using the q-operator approach, obtain the complementary, particular, and complete solutions of the equation y(n + 2) − 5y(n + 1) + 6y(n) = 15(0.5)ⁿ for the initial values y(0) = 1, y(1) = 0.

**Solution (answer key):**

- D(q) = q² − 5q + 6 = (q − 2)(q − 3) = 0 ⇒ q₁ = 2, q₂ = 3
- Complementary solution: y_c(n) = A(2)ⁿ + B(3)ⁿ
- Particular solution: y_p(n) = 1/D(q)|_(q=0.5) × 15(0.5)ⁿ = (1/3.75) × 15(0.5)ⁿ = 4(0.5)ⁿ
- Complete solution: y(n) = A(2)ⁿ + B(3)ⁿ + 4(0.5)ⁿ; y(0) = A + B + 4 = 1, y(1) = 2A + 3B + 2 = 0 ⇒ A = −7, B = 4
- **y(n) = −7(2)ⁿ + 4(3)ⁿ + 4(0.5)ⁿ**

## 2013–2014 Quiz 2 (08.11.2013)

An LTI system is defined by y″(t) + 3y′(t) + 2y(t) = 5x′(t) + 2x(t). Obtain the impulse response h(t).

**Solution (answer key):**

- (p² + 3p + 2)z(t) = δ(t), y(t) = (5p + 2)z(t); roots p₁,₂ = −1, −2; z′(0) = 1, z(0) = 0
- z_c(t) = Ae^(−t) + Be^(−2t); A + B = 0, −A − 2B = 1 ⇒ A = 1, B = −1 ⇒ z(t) = e^(−t) − e^(−2t)
- h(t) = 5z′(t) + 2z(t) = 5[−e^(−t) + 2e^(−2t)] + 2e^(−t) − 2e^(−2t) = **−3e^(−t) + 8e^(−2t)** (t ≥ 0)

## 2013–2014 Makeup Exam (27.01.2014)

100 minutes, 10 points per question.

### Question 1

For x(t) = u(t + 1) − u(t − 1), h(t) = δ(t) + δ(t − 1) + δ(t + 1), compute y(t) = x(t) ∗ h(t) and sketch it with the intermediate steps.

**Solution:** y(t) = x(t) + x(t − 1) + x(t + 1). Summing the three overlapping rectangles gives a stepped signal: 1 for −2 < t < −1, 2 for −1 < t < 1, 1 for 1 < t < 2, and 0 elsewhere.

### Question 2

A periodic x(t) with period T = 2 (t for 0 ≤ t ≤ 1, 2 − t for 1 ≤ t ≤ 2; a triangular wave) and g(t) = dx(t)/dt (a square wave between ±1). x(t) ⟷ a_k and g(t) ⟷ b_k. Find a₀ directly; then find b_k and obtain the remaining a_k using the FS properties.

**Solution:**

- a₀ = ½∫₀² x(t) dt = 1/2
- b₀ = 0; b_k = (1/2)[∫₀¹ e^(−jπkt) dt − ∫₁² e^(−jπkt) dt] = (1 − e^(−jπk))²/(2jπk): 2/(jπk) for odd k, 0 for even k
- g(t) = dx/dt ⇒ b_k = jkπ a_k ⇒ **a_k = b_k/(jkπ) = −(1/(π²k²))[1 − e^(−jπk)]**, i.e., −2/(π²k²) for odd k, 0 for even k (k ≠ 0)

### Question 3

Compute the convolution sum y[n] = x[n] ∗ h[n] for x[n] = (1/2)ⁿu[n] and h[n] = u[n − 2].

**Solution:** y[n] = 0 for n − 2 < 0; for n ≥ 2, y[n] = Σ_{k=0}^{n−2} (1/2)^k = (1 − (1/2)^(n−1))/(1 − 1/2) = **2 − 4(1/2)ⁿ**.

### Question 4

A causal LTI system y[n] + ½y[n − 1] = x[n].

1. Frequency response H(e^(jω)), |H(e^(jω))|, and ∠H(e^(jω))?
1. Output y[n] for the input x[n] = δ[n] + ½δ[n − 1]?

**Solution:**

- H(e^(jω)) = 1/(1 + ½e^(−jω)) = 1/(1 + ½cos ω − j½sin ω)
- |H(e^(jω))| = 1/√((1 + ½cos ω)² + (½ sin ω)²)
- ∠H(e^(jω)) = tan⁻¹(½ sin ω / (1 + ½ cos ω))
- X(e^(jω)) = 1 + ½e^(−jω) ⇒ Y(e^(jω)) = X(e^(jω))H(e^(jω)) = 1 ⇒ **y[n] = δ[n]**

### Question 5

Using the definitions of the Fourier transform:

1. If x(t) = e^(−|t|), then X(jω) = ? **Solution:** X(jω) = 1/(1 − jω) + 1/(1 + jω) = **2/(1 + ω²)**
1. If X(jω) = 2πδ(ω − 2), then x(t) = ? **Solution:** x(t) = (1/2π)∫2πδ(ω − 2)e^(jωt) dω = **e^(j2t)**
1. Using (b), the Fourier transform of x(t) = cos²(t): cos²t = ½ + ¼e^(j2t) + ¼e^(−j2t) ⟷ **πδ(ω) + (π/2)δ(ω − 2) + (π/2)δ(ω + 2)**

## January 2016: Solutions to Fourier transform questions

Two solution sheets dated January 2016 (transcribed from photographs) solve continuous-time Fourier transform questions:

**1.** h(t) is a rectangle of amplitude 1 between −1 and 1 ⇒ H(jω) = 2 sin ω / ω. The input is X(jω) = δ(ω) + δ(ω − π) + δ(ω − π/6) + δ(ω − 7π). By the convolution property, Y(jω) = H(jω)X(jω); since f(ω)δ(ω − ω₀) = f(ω₀)δ(ω − ω₀), the terms with sin π = sin 7π = 0 vanish, lim_{ω→0} 2 sin ω/ω = 2, and 2 sin(π/6)/(π/6) = 6/π:

- Y(jω) = 2δ(ω) + (6/π)δ(ω − π/6)
- **y(t) = 1/π + (3/π²)e^(jπt/6)**

**2.** For x₁(t) = αe^(−βt)u(t) and x₂(t) = sin(ω₀t), the transform of x(t) = x₁(t)x₂(t) via the multiplication property: X₁(jω) = α/(β + jω), X₂(jω) = (π/j)[δ(ω − ω₀) − δ(ω + ω₀)],

- X(jω) = (1/2π) X₁ ∗ X₂ = (α/2j)[1/(β + j(ω − ω₀)) − 1/(β + j(ω + ω₀))]
- **X(jω) = αω₀ / ((β + jω)² + ω₀²)**
