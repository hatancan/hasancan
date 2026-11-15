---
baslik: MAT222 Differential Equations: 30 Practice Problems (Marmara University, Faruk Uçar)
ozet: Marmara MAT232 practice sheet: Cauchy–Euler, Taylor and Frobenius series, singular points, and Bessel relations, with the given answers.
---

This post contains the **Marmara University Faculty of Arts and Sciences, Department of Mathematics, MAT232 Differential Equations II** practice sheet. The PDF metadata lists the author as **Faruk Uçar** and the date as **8 April 2005**. The 30 main questions and the basic answers from the six-page document have been transcribed here. The original PDF is available for download at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## Cauchy–Euler problems: 1–9

**1.** Solve the equation t²y″ + 3ty′ + 5y = 0 using the substitution t = eˣ and by trying y = tʳ. Answer: y = |t|⁻¹[C₁ cos(2 ln|t|) + C₂ sin(2 ln|t|)].

**2.** Solve the following equations for t > 0:

| Equation | Solution given in the source |
|---|---|
| t²y″ + 2ty′ − 6y = 0 | C₁t⁻³ + C₂t² |
| t²y″ + 9ty′ + 2y = 0 | C₁t^(−4−√14) + C₂t^(−4+√14) |
| t²y″ − 5ty′ + 25y = 0 | t³[C₁ cos(4 ln t) + C₂ sin(4 ln t)] |
| 2t²y″ − ty′ + y = 0 | C₁√t + C₂t |
| t²y″ + 5ty′ + 4y = 0 | t⁻²(C₁ + C₂ ln t) |
| 2t²y″ + ty′ − y = 0 | C₁t⁻¹ᐟ² + C₂t |


**3.** t²y″ − ty′ + y = t ln t. Answer: t[C₁ + C₂ ln t + (ln t)³/6].

**4.** For t³y‴ − 2t²y″ + 8ty′ − 8y = 0: C₁t + t²[C₂ cos(2 ln t) + C₃ sin(2 ln t)]; for t³y‴ + ty′ − y = 0: C₁t + C₂t ln t + C₃t(ln t)².

**5.** (t − 1)²y″ + 8(t − 1)y′ + 12y = 0. Answer: C₁/(t − 1)³ + C₂/(t − 1)⁴.

**6.** t²y″ − 3ty′ + 4y = t + t² ln t. Answer: C₁t² + C₂t² ln t + t + t²(ln t)³/6.

**7.** t²y″ − 2ty′ + 2y = (ln t)² − ln(t²). Answer: C₁t + C₂t² + 1/4 + [(ln t) + (ln t)²]/2.

**8.** t²y″ − ty′ + 4y = cos(ln t) + t sin(ln t). Answer: C₁t cos(√3 ln t) + C₂t sin(√3 ln t) + t sin(ln t)/2 + [3 cos(ln t) − 2 sin(ln t)]/13.

**9.** t²y″ + 5ty′ + 5y = t⁻³. Answer: t⁻²[C₁ cos(ln t) + C₂ sin(ln t)] + 1/(2t³).

## Taylor series: 10–19

**10.** For y′ = 2ty, y(0) = 1, find the series about t = 0 and show that y = eᵗ².

**11.** For y″ − ty′ = 0, y(1) = 0, y′(1) = 1, find the series about t = 1. The source writes y = (t − 1) + (t − 1)³/6 + (t − 1)⁴/12 + ….

*Note: The initial conditions give y″(1) = 1, so the second-order term cannot be missing. The correct beginning is y = s + s²/2 + s³/3 + s⁴/6 + …, where s = t − 1.*

**12.** y″ + 4y = 0 → a₀ cos 2t + (a₁/2)sin 2t.

**13.** y″ − 2ty = 0 → a₀(1 + t³/3 + t⁶/45 + …) + a₁(t + t⁴/6 + t⁷/126 + …).

**14.** Find the Taylor series for y″ − 2ty′ + y = 0. Equating coefficients gives (n + 2)(n + 1)aₙ₊₂ = (2n − 1)aₙ. The source writes the even series as 1 − t²/2! − … and the odd series as t + ….

*Note: Because the source's odd series sum starts at n = 2, the t³/6 term has been dropped. The odd series should begin t + t³/6 + t⁵/24 + ….*

**15.** y″ + 2ty′ + 2y = 0 → a₀(1 − t² + t⁴/2 − t⁶/6 + …) + a₁(t − 2t³/3 + 4t⁵/15 − …). The source writes |t| < 1 on this line.

*Note: In this equation the coefficients are analytic everywhere; both solution series converge for all t. Although |t| < 1 is a valid subregion, the actual radius of convergence is ∞.*

**16.** (1 − t)y″ + y = 0 → a₀(1 − t²/2 − t³/6 − t⁴/24 − …) + a₁(t − t³/6 − t⁴/12 − …).

**17.** Show that the function J₀(t) = Σ_(n=0)^∞ (−1)ⁿt²ⁿ/[2²ⁿ(n!)²] satisfies the equation ty″ + y′ + ty = 0.

**18.** t³y‴ − 2t²y″ + 4ty′ − 4y = 0 → C₁t + C₂t² + C₃t² ln t.

**19.** y″ − ty′ − y = 0 → a₀Σ t²ⁿ/(2ⁿn!) + a₁Σ [2ⁿn!/(2n + 1)!]t²ⁿ⁺¹. Radius of convergence ∞.

## Singular points: 20–23

**20.** Classify all singular points:

- (1 − t²)y″ − 2ty′ + α(α + 1)y = 0: ±1 regular singular.
- 2(t − 2)²ty″ + 2ty′ + (t − 2)y = 0: 0 regular singular, 2 irregular singular.
- (t − π/2)²y″ + cos(t)y′ + sin(t)y = 0: π/2 regular singular.

**21.** Classify all singular points:

- t²y″ + sin(t)y = 0.
- y″ + ln(t)y = 0.
- (t² − 1)y″ + 2ty′ + 6y = 0.
- (t² + 1)y″ + 2ty′ + 6y = 0.
- t²(t + 1)²y″ + (t² − 1)y′ + 2y = 0.
- (t² − 4)²y″ + (t − 2)y′ + y = 0.

For the first equation the source gives 0 as regular singular; for the fifth, −1 as regular and 0 as irregular singular. For the fourth it says "all points are ordinary."

*Note: The fourth answer holds for the real axis; in the complex plane ±i are singular. In the equation containing ln t, the region t ≤ 0 lies outside the domain of the real-coefficient equation; it is not appropriate to classify every point of this region as a singular point of the same type.*

**22.** Determine the type of the given point:

- t(t − 2)²y″ + ty′ + y = 0: t = 0 and t = 2.
- sin(t)y″ + cos(t)y′ + t⁻¹y = 0: t = 0.
- (eᵗ − 1)y″ + ty′ + y = 0: t = 0.
- (1 − t²)y″ + y′/sin(t + 1) + y = 0: t = −1.
- t³y″ + sin(t²)y′ + ty = 0: t = 0.

**23.** Determine the singular points together with their types:

- (t⁵ − t⁴ − 6t³)y″ + t²y′ + (t − 2)y = 0.
- (t² − 3t)y″ + (t + 2)y′ + y = 0.
- (t³ + t²)y″ + (t² − 2t)y′ + 4y = 0.
- (t⁴ − 2t³ + t²)y″ + 2(t − 1)y′ + t²y = 0.

## Frobenius problems: 24–29

**24.** For t²y″ + 4ty′ + (t − 4)y = 0 the indicial roots are 1 and −4. The source gives the structure y₁ = t(1 + Σ aₙtⁿ), y₂ = ay₁ ln t + t⁻⁴(1 + Σ bₙtⁿ).

**25.** For 2ty″ − y′ + 2y = 0, show the regular singularity and solve by the Frobenius method. The given series are t³ᐟ²(1 − 2t/5 + 2t²/35 − 4t³/945 + …) and 1 + 2t − 2t² + 4t³/9 − ….

**26.** ty″ + 2y′ − ty = 0 → (K₁ sinh t + K₂ cosh t)/t.

**27.** 4ty″ + 2y′ + y = 0 → sin√t and cos√t.

**28.** Solve about t = 0 by the Frobenius method:

- t²y″ − ty′ + (2t² + 5/9)y = 0.
- 2t²y″ + ty′ + (2t² − 3)y = 0.
- t²y″ − ty′ + (t² − 3)y = 0.
- ty″ + y′ + 2y = 0.
- t²y″ + (t³ − t)y′ − 3y = 0.

**29.** Equations and fundamental solution pairs given in the source:

| Equation | Solution pair |
|---|---|
| 2ty″ + y′ + 2y = 0 | cos(2√t), sin(2√t) |
| ty″ − y′ + 64t³y = 0 | cos(4t²), sin(4t²) |
| 4ty″ + 2y′ − y = 0 | cosh√t, sinh√t |
| 4t²y″ − 4ty′ + (3 − 4t²)y = 0 | √t cosh t, √t sinh t |
| t²y″ + 6ty′ − (t² − 6)y = 0 | cosh t/t³, sinh t/t³ |

## Bessel relation: 30

From the relations d[tᵖJₚ(t)]/dt = tᵖJₚ₋₁(t) and d[t⁻ᵖJₚ(t)]/dt = −t⁻ᵖJₚ₊₁(t), obtain Jₚ₊₁(t) = (2p/t)Jₚ(t) − Jₚ₋₁(t). Write J₃(2t) in terms of J₀(2t) and J₁(2t).

Check: applying the recurrence twice gives J₃(2t) = (2/t² − 1)J₁(2t) − (2/t)J₀(2t), t ≠ 0.
