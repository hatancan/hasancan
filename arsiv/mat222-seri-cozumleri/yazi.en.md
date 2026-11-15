---
baslik: MAT222 Differential Equations: Power Series and Frobenius Solutions (Ufuk Özerman, institution not stated)
ozet: Notes from 2006 on series solutions and a worked-solutions sheet with nine problems: convergence, ordinary and singular points, Euler equations, the Frobenius method, and Bessel functions.
---

This post brings together the 27-page note "Series Solution of Second-Order Equations" signed by **Ufuk Özerman** and the 10-page solutions sheet dated **12 December 2006**. The first file is dated 29 November 2006; its printed page numbers are 79–105. The university name does not appear in the documents, so the affiliation with Ege University has not been verified. The topics, basic relations, and worked results have been transcribed into the text; the two original PDFs can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## Power series and convergence

y = Σ_(n=0)^∞ aₙ(x − x₀)ⁿ.

The series converges if the limit of its partial sums exists. For a radius of convergence ρ, the series converges absolutely in the region |x − x₀| < ρ and diverges in the region |x − x₀| > ρ. The endpoints are examined separately. If the series converges only at the center, ρ = 0; if it converges for every x, ρ = ∞.

In the ratio test, take L = lim |aₙ₊₁/aₙ|·|x − x₀|. L < 1 gives convergence and L > 1 gives divergence; L = 1 is inconclusive.

- Σ_(n=1)^∞ (−1)ⁿ⁺¹n(x − 2)ⁿ: convergent for 1 < x < 3; divergent at both endpoints because the general term does not tend to zero.
- Σ (x + 1)ⁿ/(n2ⁿ): absolutely convergent within −3 < x < 1; at x = −3 it is conditionally convergent as the alternating harmonic series, and at x = 1 it diverges.

*Note: In the first writing of the second example, the sum starts from n = 0; since n appears in the denominator, the start should be n = 1. In the definition of absolute convergence on the first page, the absolute value signs are missing: absolute convergence means that the sum of the absolute values of the terms converges.*

## Series operations and the Taylor expansion

Within the common region of convergence, addition, subtraction, and multiplication are carried out; for division, the denominator must be nonzero. Derivatives are taken term by term:

- y′ = Σ_(n=1)^∞ naₙ(x − x₀)ⁿ⁻¹.
- y″ = Σ_(n=2)^∞ n(n − 1)aₙ(x − x₀)ⁿ⁻².
- Index shift: Σ_(n=2)^∞ aₙxⁿ = Σ_(n=0)^∞ aₙ₊₂xⁿ⁺².

A power series that yields the zero function has all its coefficients equal to zero. This allows a recurrence relation to be derived from the differential equation.

*Note: In the note the Taylor coefficient is printed as f⁽ⁿ⁾(x₀)/n; the correct denominator is n!. That a power series can be differentiated term by term in its interior does not mean that an ordinary continuous function has derivatives of all orders.*

## Ordinary points and singular points

For P(x)y″ + Q(x)y′ + R(x)y = 0, define p = Q/P and q = R/P. In examples with polynomial coefficients, x₀ is an ordinary point if P(x₀) ≠ 0. At a singular point, if (x − x₀)p(x) and (x − x₀)²q(x) can be extended analytically, the point is a regular singular point. In the note's examples with rational coefficients, this condition is checked by requiring the relevant limits to be finite.

Examples:

- (x² − 4)y″ + 2xy′ + ay = 0: singular points ±2.
- x²y″ + xy′ + (x² − 1)y = 0: singular point 0.
- Legendre: (1 − x²)y″ − 2xy′ + α(α + 1)y = 0.
- Airy form: y″ − λxy = 0.
- Hermite: y″ − 2xy′ + 2ny = 0.
- Bessel: x²y″ + xy′ + (x² − ν²)y = 0.

## Solutions around an ordinary point

**y″ + y = 0:** aₙ₊₂ = −aₙ/[(n + 2)(n + 1)]. The even coefficients give the cosine series and the odd coefficients give the sine series:

y = a₀ cos x + a₁ sin x.

**y″ − xy = 0:** a₂ = 0 and aₙ₊₂ = aₙ₋₁/[(n + 2)(n + 1)] (n ≥ 1). Result:

y = a₀(1 + x³/6 + x⁶/180 + …) + a₁(x + x⁴/12 + x⁷/504 + …).

For analytic p and q, a lower bound for the radius of convergence is given by the distance from the center to the nearest coefficient singularity in the complex plane. For example, for (1 + x²)y″ + 2xy′ + 4x²y = 0, the distance to the points ±i is 1 at x₀ = 0 and √5/2 at x₀ = 1/2.

## Euler equations

For x²y″ + αxy′ + βy = 0, the choice y = xʳ gives r(r − 1) + αr + β = 0.

- Distinct real roots: C₁xʳ¹ + C₂xʳ².
- Repeated root: xʳ(C₁ + C₂ ln x), x > 0.
- r = λ ± iµ: x^λ[C₁ cos(µ ln x) + C₂ sin(µ ln x)], x > 0.

Example results from the note:

- x²y″ + xy′ − 4y = 0 → C₁x⁻² + C₂x².
- 2x²y″ + 3xy′ − y = 0 → C₁√x + C₂/x.
- x²y″ + xy′ + 2y = 0 → C₁ cos(√2 ln x) + C₂ sin(√2 ln x).

## The Frobenius method

Around the regular singular point x = 0, a solution is sought in the form y = xʳΣ_(n=0)^∞ aₙxⁿ, a₀ ≠ 0. For p₀ = lim xp(x) and q₀ = lim x²q(x), the indicial equation is:

F(r) = r(r − 1) + p₀r + q₀ = 0.

The coefficient of the lowest power gives the indicial equation; the subsequent powers give the recurrence relation. If the difference between the distinct roots is not an integer, two Frobenius series are obtained. For a repeated root, a ln x term appears in the second solution. When the difference is a positive integer, the second solution may contain a logarithmic term; its coefficient may also be zero.

**Example:** For 2x²y″ − xy′ + (1 + x)y = 0, F(r) = 2r(r − 1) − r + 1; the roots are 1 and 1/2. The recurrence relation is aₙ = −aₙ₋₁/[2(r + n)(r + n − 1) − (r + n) + 1].

## Bessel's equation of order one-half

For x²y″ + xy′ + (x² − 1/4)y = 0, the indicial roots are ±1/2. The two solutions are expressed through sin x/√x and cos x/√x:

- J_(1/2)(x) = √(2/(πx)) sin x.
- J_(−1/2)(x) = √(2/(πx)) cos x.

Although the root difference is 1, no logarithm is needed in the independent solutions of this example.

## Solutions sheet: nine problems

### 1. y″ − xy′ − y = 0

aₙ₊₂ = aₙ/(n + 2).

y = a₀(1 + x²/2 + x⁴/8 + …) + a₁(x + x³/3 + x⁵/15 + …).

### 2. 2y″ + xy′ + 3y = 0

aₙ₊₂ = −(n + 3)aₙ/[2(n + 1)(n + 2)].

y = a₀(1 − 3x²/4 + 15x⁴/96 + …) + a₁(x − x³/3 + x⁵/20 + …).

### 3. (1 − x)y″ + xy′ − y = 0

aₙ₊₂ = [n(n + 1)aₙ₊₁ − (n − 1)aₙ]/[(n + 1)(n + 2)].

y = a₀(1 + x²/2! + x³/3! + …) + a₁x. The first series is eˣ − x.

### 4. (1 + x²)y″ − 4xy′ + 6y = 0

aₙ₊₂ = −(n² − 5n + 6)aₙ/[(n + 1)(n + 2)]. The series terminate:

y = a₀(1 − 3x²) + a₁(x − x³/3).

### 5. x²(1 − x²)y″ − 2xy′ + 4y = 0

The singular points are 0, 1, and −1; all three are regular singular points. For 0 the limits are −2 and 4; for ±1 they are 1 and 0.

### 6. 2x²y″ + 3xy′ − y = 0

The indicial equation is 2r² + r − 1 = 0; the solution is C₁√x + C₂/x.

### 7. x²y″ − 2xy′ + 2y = 2x ln x

The homogeneous solution is C₁x² + C₂x. Using variation of parameters, the result given in the source is:

y = K₁x² + K₂x − x(ln x)² − 2x ln x.

*Note: The result is correct; however, the intermediate integral lines are incomplete/erroneous. They should be ∫2 ln x/x² dx = −2(ln x + 1)/x + C and ∫−2 ln x/x dx = −(ln x)² + C. The extra −2x term in the first integral is absorbed into the homogeneous constant in the final solution.*

### 8. x²y″ + xy′ + (x − 2)y = 0

p₀ = 1, q₀ = −2; the indicial roots are ±√2. The coefficients are found from aₙ = −aₙ₋₁/[(r + n)² − 2]. For both values of r, y_r = xʳ[1 − x/(1 + 2r) + x²/((1 + 2r)(4 + 4r)) + …].

*Note: In the sheet, the sentence after the limit computation states q₀ = 0; the limit on the same page and the indicial equation used show that q₀ = −2.*

### 9. x²y″ + xy′ + x²y = 0

r² = 0 is a repeated indicial root, a₁ = 0, aₙ = −aₙ₋₂/(r + n)².

y₁ = 1 − x²/4 + x⁴/64 − x⁶/2304 + … = J₀(x).

The second solution is obtained by differentiating with respect to r, in the form y₂ = y₁ ln x + x²/4 − 3x⁴/128 + …. The general solution is C₁y₁ + C₂y₂.

The first coefficients of the recurrence relations and the terminating polynomial solutions were checked by substituting them into the equations.
