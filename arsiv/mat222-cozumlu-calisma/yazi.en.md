---
baslik: MAT222 Differential Equations: Solved Study Problems 1–2 (Institution Not Specified)
ozet: 22 solved problems from the fall 2006–2007 semester: first-order equations, Bernoulli, Clairaut, Riccati, constant-coefficient equations, and variation of parameters.
---

This post contains the **fall 2006–2007 Differential Equations Study Problems 1 and 2** handouts. The PDF creation dates are 13 and 15 November 2006; the metadata contains only the account name "SerdarB". The document contains no institution or explicit author name; its attribution to Ege University could not be verified. The problems and solution results have been transcribed into the text; the two original PDFs, 17 pages in total, are available for download as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## Study Problems 1

### Linear equations: 1–3

1. y′ + 2y = sin t. Integrating factor e²ᵗ; the result is y = (2 sin t − cos t)/5 + Ce⁻²ᵗ.
2. (4 + t)y′ + y = 6 + 2t. The source takes µ = 1/(4 + t) and writes y = 6t + t² + C(4 + t) in the last line.
3. y′ − 3y = 7, y(0) = 15. The result is y = −7/3 + (52/3)e³ᵗ.

*Note: The correct factor for the second problem is µ = t + 4. Since [(t + 4)y]′ = 6 + 2t, we get y = (t² + 6t + C)/(t + 4), t ≠ −4. In general, the solution in the source does not satisfy the equation.*

### Homogeneous and Bernoulli equations: 4–5

**4.** y′ = (2xy + 3y²)/(2xy + x²). With the substitution y = vx, dx/x = (2v + 1)dv/(v + v²). The source finds x³/(xy + y²) = constant. The solutions y = 0 and y = −x, which are lost in the division, must be checked separately.

**5.** xy − y′ = y³e⁻ˣ². The substitution u = y⁻² gives u′ + 2xu = 2e⁻ˣ². The result is y⁻² = (2x + C)e⁻ˣ².

*Note: In the last line of the alternative solution to the fifth problem, y is written in place of u. The expression (2x + C)e⁻ˣ² that is found is y⁻², not y. Also, the solution y = 0 is lost during the substitution.*

### Exactness and integrating factor: 6–8

**6.** x dy − y dx = x²eˣ dx has an integrating factor depending on x, µ = x⁻². The result is y/x − eˣ = C, or y = Cx + xeˣ.

**7.** sin x cos y dx + cos x sin y dy = 0 is exact; −cos x cos y = C.

**8.** (yeˣ + y) dx + (eˣ + x) dy = 0 is exact; yeˣ + xy = C.

### Clairaut and Riccati: 9–10

**9.** y = xy′ + (y′)³. The general family is y = Cx + C³. For the envelope, x = −3C², y = −2C³; hence y² = −4x³/27.

**10.** y′ = 2 tan x sec x − y² sin x, with known solution y₁ = sec x. The substitution y = sec x + 1/u gives u′ − 2u tan x = sin x. The result in the source:

y = sec x + 3cos²x/(C − cos³x).

This expression satisfies the equation on its interval of definition; the known solution y = sec x is also retained separately.

## Study Problems 2

### Order reduction: 1–2

**1.** (1 + x²)y″ + (y′)² + 1 = 0. The source chooses p = y′ and finds dp/(1 + p²) = −dx/(1 + x²); it then writes p = −x/C and y = −x²/(2C) + C₁.

*Note: Integration gives arctan p = −arctan x + C; the ratio of arctangents cannot be taken. The general expression for p is tan(C − arctan x). The parabola in the source is not a solution for arbitrary C.*

**2.** xy″ = √(1 + (y′)²). With p = y′, ∫dp/√(1 + p²) = ∫dx/x. The source gives the result y = Cx²/4 − ln x/(2C) + C₁ in the region x > 0; because of the condition Cx = p + √(1 + p²) before squaring, C > 0 must be taken here.

### Homogeneous and forced equations: 3–7

**3.** y″ + 6y = 0. The solution is C₁ cos(√6x) + C₂ sin(√6x). The Wronskian is √6 ≠ 0.

**4.** y″ + 3y′ + 2y = 0, y(0) = 2, y′(0) = 1. The solution is 5e⁻ˣ − 3e⁻²ˣ.

**5.** y″ − 7y′ + 10y = 6t + 8e²ᵗ. The source writes C₁e²ᵗ + C₂e⁵ᵗ + 2te²ᵗ + 3t/5 + 21/50.

*Note: Since L{Dte²ᵗ} = −3De²ᵗ, D must be −8/3. The correct particular solution is −(8/3)te²ᵗ + 3t/5 + 21/50.*

**6.** y″ + 7y′ + 12y = sin 2x + e⁻³ˣ + 4. The source's result is C₁e⁻³ˣ + C₂e⁻⁴ˣ − (7/30)cos 2x + (4/30)sin 2x + xe⁻³ˣ + 1/3.

*Note: The trigonometric coefficients were computed incorrectly. The system −14A + 8B = 1, 8A + 14B = 0 gives A = −7/130, B = 2/65. The other particular-solution terms are correct.*

**7.** y″ − 5y′ + 4y = −4(x² + 1)e³ˣ. The source's result is C₁eˣ + C₂e⁴ˣ + (2x² + 2x + 5)e³ˣ; it passes the substitution check.

### Variation of parameters: 8–10

**8.** y″ + y = sin x. The source applies variation of parameters with u₁′ = −sin²x and u₂′ = sin x cos x.

*Note: In the result line, the sign of the sin(2x)cos x term is inconsistent with the preceding integral. The correct simplified general solution is C₁ cos x + C₂ sin x − (x/2)cos x.*

**9.** For (2 − t)y‴ + (2t − 3)y″ − ty + y = 0, y₁ = eᵗ is known; the task is to find another solution by order reduction. The handout repeats this problem and gives no solution. The −ty term in the problem statement is preserved here exactly as written.

**10.** y‴ + y′ = 1/sin x, 0 < x < π. The source's result:

y = C₁ + C₂ cos x + C₃ sin x − ln(csc x + cot x) − cos x ln(sin x) − x sin x.

*Note: The negative logarithm used in the solution is correct. However, the reminder formula at the bottom of the page is missing the minus sign: it should be ∫csc(ax)dx = −ln|csc(ax) + cot(ax)|/a + C.*

### Undetermined coefficients: 11–12

**11.** y‴ − 4y″ + y′ + 6y = sin 4x. The homogeneous roots are −1, 2, 3. The source gives the particular solution as (12/1565)cos 4x + (13/1565)sin 4x.

*Note: Substitution gives 70A − 60B = 0, 60A + 70B = 1. The correct particular solution is (3/425)cos 4x + (7/850)sin 4x.*

**12.** The expression on the problem page is y‴ − 2y″ + 17 = 8 + e²ˣ cos 5x + x²eˣ sin 4x + (x + 1). The solution page, however, treats the equation y‴ − 2y″ + 17y′. According to this second expression, the homogeneous solution is C₁ + eˣ(C₂ cos 4x + C₃ sin 4x).

For the form of the particular solution, the source uses the terms Ax, e²ˣ(B cos 5x + C sin 5x), a resonant trigonometric polynomial, and x(Kx + L).

*Note: On the problem page, the y′ next to 17 is missing. In the solution, the resonant term is missing an x in front of the sine polynomial. The appropriate form is xeˣ[(a₂x² + a₁x + a₀)cos 4x + (b₂x² + b₁x + b₀)sin 4x]. The Ax term can already be represented within x(Kx + L).*
