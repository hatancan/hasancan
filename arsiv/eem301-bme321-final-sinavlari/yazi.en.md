---
baslik: EEM301 Signals and Systems I: BME 321 Signals and Systems Final Exams and Solutions (2005, 2006)
ozet: Questions and handwritten solutions from the January 2005 and January 2006 final exams of the Başkent University BME 321 Signals and Systems course: linearity, time invariance and causality, convolution, impulse response of cascaded systems, Fourier series of the sin³ signal, filtering of an impulse train, frequency response and superposition.
---

This post was compiled from the "BME Signal Exam" folder in the EEM301 Signals and Systems I folder: the final exams and handwritten solutions of the Başkent University Faculty of Engineering **BME 321 – Signals and Systems** course, dated **13 January 2005** (2004/2005 fall) and **4 January 2006** (2005/2006 fall). The exam papers and solutions were transcribed to text from photographed pages; the photos were not published, so there are no downloadable files. The exams are in English; the questions have been abridged in transcription. Both exams are out of 35 points.

## Final – 4 January 2006

### Question 1 (9 points)

Discrete-time system y[n] = 2x[n] − 5x[n − 1] + 2x[n − 2].

1. Is the system linear, time-invariant and causal?
1. Find the expression for the frequency response.
1. Sketch the magnitude response as a function of frequency.
1. Find the output for the input x₂[n] = 4 + 4 cos(0.5π(n − 1)) (hint: linearity and time invariance).

**Solution:** The system is linear and time-invariant (an input x[n − n₀] gives y[n − n₀]); it is causal because it depends only on x[n], x[n − 1], x[n − 2], that is, on present and past values.

- H(e^(jω)) = Σ b_k e^(−jωk), b_k = {2, −5, 2} ⇒ H(e^(jω)) = 2 − 5e^(−jω) + 2e^(−j2ω) = (2e^(jω) − 5 + 2e^(−jω))e^(−jω) = **(4 cos ω − 5)e^(−jω)**
- |H(e^(jω))| = |4 cos ω − 5|: a curve with period 2π that equals 1 at ω = 0 and 9 at ω = ±π
- H(e^(j0)) = −1, H(e^(jπ/2)) = −5e^(−jπ/2) = 5e^(jπ/2)
- y₂[n] = (−1)(4) + 5·4 cos(0.5π(n − 1) + π/2) = **−4 + 20 cos(0.5πn)**

### Question 2 (8 points)

Input x(t) = u(t) − 2u(t − 4) + u(t − 6) and the given triangular h(t) (1 + t for −1 < t < 0, 1 − t for 0 < t < 1). Find (a) the output y(t), (b) y(0), (c) the regions and points where y(t) = 0.

**Solution:** First find g(t) = h(t) ∗ u(t) = ∫_{−∞}^{t} h(τ)dτ: 0 for t < −1, (t + 1)²/2 for −1 < t < 0, 1/2 + [1/2 − (1 − t)²/2] for 0 < t < 1, and 1 for t > 1. By linearity and time invariance, y(t) = g(t) − 2g(t − 4) + g(t − 6); y(0) = g(0) = 1/2.

### Question 3 (6 + 6 points)

Two LTI systems connected in series.

- (a) The first system is w(t) = ∫_{−∞}^{t} x(τ)dτ, and the impulse response of the second system is h₂(t) = u(t − 5). **Solution:** h₁(t) = u(t), h(t) = u(t) ∗ u(t − 5) = **(t − 5)u(t − 5)** (0 for t < 5, t − 5 for t ≥ 5).
- (b) The first system is w(t) = dx(t)/dt + 3x(t); show that for the total impulse response to be h(t) = δ(t), h₂(t) must be of the form Ae^(−α(t−t₀))u(t − t₀). **Solution:** h(t) = (dδ/dt + 3δ(t)) ∗ e^(αt)u(t) = (3 + α)e^(αt)u(t) + δ(t); for h(t) = δ(t) we need α = −3, that is, **h₂(t) = e^(−3t)u(t)**.

### Question 4 (7 points)

Find all the Fourier series coefficients of the "sine-cubed" signal sin³(3πt) using the Fourier integral.

**Solution:** The period is T₀ = 2π/(3π) = 2/3. Using the expansion of (a + b)³,

sin³(3πt) = (j/8)e^(j9πt) − (3j/8)e^(j3πt) + (3j/8)e^(−j3πt) − (j/8)e^(−j9πt)

Each term is integrated separately; for k ≠ ±1, ±3 the integrals are zero. Result: **a₁ = −3j/8, a₋₁ = 3j/8, a₃ = j/8, a₋₃ = −j/8**, all others 0.

### Question 5 (5 points)

x(t) = Σ δ(t − 50k) = Σ (1/50)e^(j(2π/50)kt) periodic impulse train.

1. Fundamental frequency: **ω₀ = 2π/50 rad/s**.
1. Output (as a real expression) of an LTI system whose frequency response is 1 for |ω| ≤ π/20 and 0 otherwise: The filter passes only the components at ω = 0 and ±2π/50 ⇒ **y(t) = (1/50)(1 + 2 cos(2πt/50))**.

## Final – 13 January 2005

### Question 1 (4.5 points)

Whether the following systems are linear, time-invariant and causal:

| System | Linear | Time-invariant | Causal |
|---|---|---|---|
| y[n] = e^(x[n]) | No | Yes | Yes |
| y[n] = x[n] cos(0.2πn) | Yes | No | Yes |
| y[n] = −x[n + 1] + x[n] − x[n − 1] | Yes | Yes | No (depends on x[n + 1]) |

### Question 2

1. Sketch w(t) = u(t + 2) − u(t − 2).
1. Define and sketch the convolution y(t) = w(t) ∗ w(t).
1. What is the impulse response h(t) of the LTI system that produces the given output y(t) for the input x(t)?

**Solution:** Splitting the convolution integral into four step terms gives

y(t) = (t + 4)u(t + 4) − 2t·u(t) + (t − 4)u(t − 4)

which is a triangle between −4 and 4 with its peak at t = 0. In (c), the output is the sum of three shifted and scaled copies of x(t), shifted by 2, 10 and 18, so **h(t) = δ(t − 2) − δ(t − 10) + ½δ(t − 18)**.

*Note: In the sketch in the solution, the peak value of the triangle is marked as 1; since the width of the rectangle is 4, y(0) = ∫w²(τ)dτ = 4.*

### Question 3

System given by a block diagram: (a) differential equation, (b) frequency response, (c) impulse response. **Solution:** From the block diagram the equation is put into the form d²y/dt² + (5/4)dy/dt + (3/8)y(t) = x(t); H(jω) = 1/((jω)² + (5/4)jω + 3/8) = **1/((jω + 1/2)(jω + 3/4))**, then the impulse response is obtained by partial fractions.

### Question 4

H(e^(jω)) = (1 + e^(−jω))(1 − e^(jπ/3)e^(−jω))(1 − e^(−jπ/3)e^(−jω)).

1. Difference equation: since e^(jπ/3) + e^(−jπ/3) = 2 cos(π/3) = 1, H(e^(jω)) = (1 + e^(−jω))(1 − e^(−jω) + e^(−j2ω)) = 1 + e^(−j3ω) ⇒ **y[n] = x[n] + x[n − 3]**.
1. Impulse response: **h[n] = δ[n] + δ[n − 3]**.
1. The frequencies for which y[n] = 0 for the input x[n] = Ae^(jφ)e^(jωn) are the zeros of H: **ω = π, ω = −π/3, ω = π/3**.
1. For x[n] = 3 + δ[n − 2] + cos(0.5πn + π/4): H(e^(j0)) = 2, H(e^(j0.5π)) = 1 + e^(−j1.5π) = 1 + j = √2e^(jπ/4). By superposition, y[n] = 3·2 + (δ[n − 2] + δ[n − 5]) + √2 cos(0.5πn + π/4 + π/4) = **6 + δ[n − 2] + δ[n − 5] + √2 cos(0.5πn + π/2)**.

### Question 5

The signal x(t) in the figure is to be written as the sum of a rectangular part x₁(t) and a triangular part x₂(t), and its spectrum derived using the derivative and time-shift properties (using δ(t) ⟷ 1). The photographs do not contain the solution to this question.
