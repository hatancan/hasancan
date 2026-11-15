---
baslik: EEM301 Signals and Systems I: Friends' Solutions to Homework 1 and Homework 4 (Convolution Sum, System Properties, Differential Equations)
ozet: Friends' solutions to EEM301 Signals and Systems I homework: linearity and time invariance of the system x²[n − 2], discrete-time signal transformations, the convolutions αⁿu[n] ∗ αⁿu[n], (−1/2)ⁿu[n − 4] ∗ 4ⁿu[2 − n], and 2ⁿu[−n] ∗ u[n], and homogeneous differential equations with initial conditions.
---

This post collects the handwritten homework solutions by friends found in the "homework" folder of the EEM301 Signals and Systems I course folder: a **Homework 1** made up of Oppenheim & Willsky problems and a **Homework 4** from summer 2013. Personal information has been removed. The solutions were transcribed from photographed pages; the photos have not been published, so there are no downloadable files.

## Homework 1

### Linearity and time invariance: y[n] = x²[n − 2]

For x₃[n] = a·x₁[n] + b·x₂[n], y₃[n] = (a·x₁[n − 2] + b·x₂[n − 2])² = a²x₁²[n − 2] + 2ab·x₁[n − 2]x₂[n − 2] + b²x₂²[n − 2]; since this is not equal to a·y₁[n] + b·y₂[n], the system is **not linear**. For x₂[n] = x₁[n − n₀], y₂[n] = x₁²[n − 2 − n₀] = y₁[n − n₀], so the system is **time invariant**.

### Discrete-time signal transformations

For a discrete-time signal from the textbook, x[n − 4] (shift right by 4) and x[3 − n] = x[−(n − 3)] (first time-reverse to get x[−n], then shift right by 3) were sketched.

### Convolution: x[n] = h[n] = αⁿu[n]

y[n] = Σ_{k=0}^{n} αᵏ α^(n−k) = αⁿ Σ_{k=0}^{n} 1 = **αⁿ(n + 1)u[n]**.

### Convolution: x[n] = (−1/2)ⁿu[n − 4], h[n] = 4ⁿu[2 − n]

y[n] = Σ_{k ≥ max(4, n−2)} (−1/2)ᵏ 4^(n−k) = 4ⁿ Σ (−1/8)ᵏ:

- n ≤ 6 (n − 2 ≤ 4): y[n] = **(8/9)(−1/8)⁴·4ⁿ**
- n > 6: the lower limit becomes n − 2.

*Note: On the paper, the result for n > 6 is written as (8/9)(−1/2)ⁿ. Since 4ⁿ·(8/9)(−1/8)^(n−2) = (8/9)·64·(−1/2)ⁿ, the correct result is **(512/9)(−1/2)ⁿ**. Check: for n = 7, the direct sum 4⁷·(8/9)(−1/8)⁵ gives −4/9.*

In addition, the convolution of a short rectangular sequence with h[n] was found and sketched as a sum of shifted copies of h[n] (h[n] + h[n − 1] + h[n − 2] + …).

### Homogeneous differential equations

**(a)** d³y/dt³ + d²y/dt² − dy/dt − y(t) = 0, y(0) = 1, y′(0) = 1, y″(0) = −2.

- (p³ + p² − p − 1) = (p + 1)(p² − 1) ⇒ roots 1, −1, −1
- y(t) = Ae^t + Be^(−t) + Cte^(−t)
- A + B = 1, A − B + C = 1, A + B − 2C = −2 ⇒ C = 3/2, B = 3/4, A = 1/4
- **y(t) = ¼e^t + ¾e^(−t) + (3/2)te^(−t)**

**(b)** d²y/dt² + 2 dy/dt + 5y(t) = 0, y(0) = 1, y′(0) = 1.

- p² + 2p + 5 = 0 ⇒ p₁,₂ = −1 ± 2j
- y(t) = Ae^(−t) cos 2t + Be^(−t) sin 2t; y(0) = A = 1, y′(0) = −A + 2B = 1 ⇒ B = 1
- **y(t) = e^(−t)[cos 2t + sin 2t]**

## Homework 4: x[n] = 2ⁿu[−n], h[n] = u[n]

y[n] = Σ x[k]h[n − k] = Σ_{k ≤ min(n, 0)} 2ᵏ.

- n ≥ 0: y[n] = Σ_{k=−∞}^{0} 2ᵏ = 1 + 1/2 + 1/4 + … = 1/(1 − 1/2) = **2**
- n < 0: y[n] = Σ_{k=−∞}^{n} 2ᵏ = **2^(n+1)** (for example, y[−1] = 1, y[−2] = 1/2)

One of the solutions reaches this result using the geometric series formula. On the first trial pages in the same folder, x[k] was assumed to be nonzero for k > 0 as well, giving values such as y[0] = 1, y[1] = 3, y[2] = 7, y[3] = 15; since x[n] = 2ⁿu[−n] is nonzero only for n ≤ 0, this attempt is wrong, and it was corrected on the later pages.
