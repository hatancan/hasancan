---
baslik: MAT222 Differential Equations: 2005 Midterm Exam and Solutions (Marmara compilation, Faruk Uçar)
ozet: Group A and B questions dated 28 April 2005: Cauchy–Euler equations, Taylor series, radius of convergence, and classification of singular points.
---

This post contains Groups A and B of the **28 April 2005 Differential Equations II** midterm exam, together with their solutions. The PDF metadata lists **Faruk Uçar** as the author. It was kept together with Marmara University MAT232 documents by the same author; since the pages of these two exams do not carry an institution name, the Marmara connection rests on the compilation context. The two original PDFs can be downloaded as a ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed upon the rights holder's request.*

## Exam format

The duration is 100 minutes in both groups; question 1 is worth 30 points, question 2 is worth 40 points, and question 3 is worth 30 points. The independent variable in the source is t.

## Group A: Cauchy–Euler equation

**Question:** Solve the equation t²y″ + 5ty′ + 4y = 0, t > 0, using the substitution t = eˣ.

Letting Y(x) = y(eˣ), we get y′ = Y′/t and y″ = (Y″ − Y′)/t². Thus Y″ + 4Y′ + 4Y = 0 is obtained. Since the characteristic polynomial is (λ + 2)²:

y(t) = C₁t⁻² + C₂t⁻² ln t.

## Group A: Taylor series

**Question:** Solve the equation (t² − 1)y″ + ty′ − y = 0 using a Taylor series about t = 0; find the radius of convergence.

Write y = Σ_(n=0)^∞ cₙtⁿ. Equating coefficients gives c₂ = −c₀/2, c₃ = 0 and cₙ₊₂ = (n − 1)cₙ/(n + 2).

y(t) = c₀(1 − t²/2 − t⁴/8 − t⁶/16 − …) + c₁t.

The source gives the result as R = 1.

*Note: In the same paragraph, the source describes the series as "convergent for every t"; this contradicts R = 1. The Taylor series of the non-polynomial solution converges within |t| < 1. In the n = 5 line, in the expression c₅ = (4/7)c₅, the left-hand subscript should be c₇.*

## Group A: singular points

| Equation | Regular singular point | Irregular singular point |
|---|---|---|
| t²(t − 5)²y″ + 4ty′ + (t² − 25)y = 0 | t = 0 | t = 5 |
| t²(t + 1)²y″ + (t² − 1)y′ + 2y = 0 | t = −1 | t = 0 |

For checking, the equation is put into the form y″ + p(t)y′ + q(t)y = 0. Around t₀, (t − t₀)p(t) and (t − t₀)²q(t) are examined. For the first equation, the limits at t = 0 are 4/25 and −1; for the second equation, at t = −1, they are −2 and 2.

## Group B: Cauchy–Euler equation

**Question:** Solve the equation t²y″ − 3ty′ + 4y = 0, t > 0, using the substitution t = eˣ.

The substitution gives Y″ − 4Y′ + 4Y = 0. The characteristic polynomial is (λ − 2)² and the solution is:

y(t) = C₁t² + C₂t² ln t.

## Group B: Taylor series

**Question:** Solve the equation (t² + 1)y″ + ty′ − y = 0 using a Taylor series about t = 0 and find the radius of convergence.

c₂ = c₀/2, c₃ = 0, cₙ₊₂ = −(n − 1)cₙ/(n + 2).

The source begins the coefficient sequence with c₄ = −c₀/8, c₆ = c₀/16. R = 1 is given.

*Note: In Group B, the sign (−1)ᵏ written in the general c₂ₖ formula contradicts the values of c₄ and c₆ directly above it; the correct sign is (−1)ᵏ⁻¹. Accordingly, the series is c₀(1 + t²/2 − t⁴/8 + t⁶/16 − …) + c₁t. The statement "convergent for every t" is also wrong here; since the complex singular points are ±i, the Taylor radius of convergence is 1. In the n = 5 line, the left-hand c₅ should be c₇.*

## Group B: singular points

| Equation | Regular singular point | Irregular singular point |
|---|---|---|
| t²(t − 2)²y″ + 5ty′ + (t² − 4)y = 0 | t = 0 | t = 2 |
| (t² − 9)²y″ + (t + 3)y′ + 2y = 0 | t = −3 | t = 3 |

In the first equation, the limits at t = 0 are 5/4 and −1; in the second equation, at t = −3, they are 1/36 and 1/18. The Euler solutions were checked by substitution, and the series coefficients through the recurrence relation.
