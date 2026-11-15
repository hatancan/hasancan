---
baslik: MAT222 Differential Equations: Photographed Midterm and Final Study Notes
ozet: Text transcribed from 2006–2007 study sheets: Laplace table, integrating factor, homogeneous and Riccati equations, final exam preparation questions.
---

This post was **transcribed to text from photographed pages**. One of the pages bears the title "Midterm questions and solutions" dated 22 November 2006; the shooting dates are 12 January 2007 according to the EXIF data and the stamp on the image. The name of the preparer and the institution are not given. The photographs are kept in a private archive; there is no downloadable file for this post.

## Laplace transform table

The photograph uses p as the transform variable. In the table below, α and β are constants and n is a non-negative integer; the region of p in which the transform integral converges is assumed.

| f(t) | L{f(t)} |
|---|---|
| 1 | 1/p |
| tⁿ | n!/pⁿ⁺¹ |
| eᵅᵗ | 1/(p − α) |
| cos βt | p/(p² + β²) |
| sin βt | β/(p² + β²) |
| cosh βt | p/(p² − β²) |
| sinh βt | β/(p² − β²) |
| tⁿeᵅᵗ | n!/(p − α)ⁿ⁺¹ |
| eᵅᵗ cos βt | (p − α)/[(p − α)² + β²] |
| eᵅᵗ sin βt | β/[(p − α)² + β²] |
| eᵅᵗ cosh βt | (p − α)/[(p − α)² − β²] |
| eᵅᵗ sinh βt | β/[(p − α)² − β²] |
| t cos βt | (p² − β²)/(p² + β²)² |
| t sin βt | 2βp/(p² + β²)² |
| t cosh βt | (p² + β²)/(p² − β²)² |
| t sinh βt | 2βp/(p² − β²)² |
| teᵅᵗ cos βt | [(p − α)² − β²]/[(p − α)² + β²]² |
| teᵅᵗ sin βt | 2β(p − α)/[(p − α)² + β²]² |

The last six rows were checked by applying −d/dp to the corresponding basic transform.

## Final exam preparation questions

Under the heading "Final Questions" on the handwritten page there are six questions; the first abbreviation in the heading is not clearly legible.

1. Solve the equation (1 + y²) dx = (√(1 + y²) sin y − xy) dy.
2. Solve the equation y″ + y = eˣ.
3. Solve the equation x⁴y⁽⁴⁾ + 6x³y‴ + 7x²y″ + xy′ − y = 0.
4. Find the Laplace transform of the function f(t) = t sinh(βt).
5. Solve the problem y′ + 5y = e⁻²ᵗ, y(0) = 1 using the Laplace transform.
6. Find f(t) for F(p) = 1/[(p − 1)(p − 2)²].

## Handwritten solution of the first question

On a separate page, a = √(1 + y²), da = y dy/√(1 + y²) has been chosen. The equation takes the form a dx + x da = sin y dy. In the photograph, when integrating, a and x are treated as if they were constants, and "ax + xa = −cos y" is written, followed by "2x√(1 + y²) = −cos y".

*Note: The left-hand side is d(ax); it cannot be integrated as if it were two independent constants. The correct result is x√(1 + y²) = −cos y + C. The source also omits the constant of integration.*

## 22 November 2006: midterm questions and solutions

### Differential equation from a family of curves

3x + y − 2 = Ce^(x + 3y).

Differentiating: 3 + y′ = (1 + 3y′)(3x + y − 2). The result on the last line:

y′ = (−3x − y + 5)/(9x + 3y − 7).

This expression was checked by re-deriving it from the first equation.

### Separation of variables

(x²y² − x²y) dy − xy² dx = 0.

Dividing by x²y², (1 − 1/y)dy = dx/x is obtained. The result in the source is y − ln y = ln x + C.

In the regions where it is defined, the form with absolute values is y − ln|y| = ln|x| + C. The solution y = 0, which was lost in the division, is a separate solution.

### Riccati transformation

y′ + xy + x = y², with known solution y₁ = x + 1. In the photograph, y = y₁ + 1/z is chosen and the equation is reduced to a linear one. In the note, the intermediate line is written as z′ + (x + 2)z = 1; in the subsequent integral, however, there is a minus sign in front of e^(x²/2 + 2x).

*Note: Substitution gives z′ + (x + 2)z = −1. The minus sign in the final integral is consistent with this correct equation: z = e^(−x²/2−2x)[C − ∫e^(x²/2+2x)dx].*

### Homogeneous equation

(x² + y²) dx − 2xy dy = 0. With y = ux and dy = u dx + x du, (1 − u²)dx − 2xu du = 0 is obtained.

dx/x = 2u du/(1 − u²).

ln|x| + ln|1 − u²| = C. On the last line of the photograph, (x² + y²)/x = C is written, with C = 5 next to it.

*Note: The previous integral gives (x² − y²)/x = C; the plus sign on the last line is wrong. Since no initial condition determining C = 5 is visible in the photograph, this number could not be verified.*

Two shots and one close-up of the same page were read together and transcribed once. Expressions that were illegible or fell outside the frame were not completed.
