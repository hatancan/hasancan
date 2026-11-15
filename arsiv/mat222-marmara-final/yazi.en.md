---
baslik: MAT222 Differential Equations: 2005 Final Exam and Solutions (Marmara University, Faruk Uçar)
ozet: Groups A and B of the Marmara University MAT232 final: Bessel integral, linear systems, Laplace transforms, and an initial value problem.
---

This post contains the questions and solutions of the **7 June 2005** final exam of **MAT232 Differential Equations II** at the **Marmara University Faculty of Arts and Sciences, Department of Mathematics**. The author listed in the PDF metadata is Faruk Uçar. The originals of these two files, kept in the Başkent MAT222 archive, can be downloaded as a ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request by the rights holder.*

## Common question 1: Bessel integral

Let Jₚ be the Bessel function of the first kind of order p. Using the identity d[tⁿJₙ(t)]/dt = tⁿJₙ₋₁(t), prove the following result:

∫₀² tJ₀(λt) dt = 2J₁(2λ)/λ.

In the solution, take n = 1. The chain rule gives d[tJ₁(λt)]/dt = λtJ₀(λt). Applying the limits yields the desired result.

*Note: The expression containing a division is for λ ≠ 0. In the case λ = 0 the integral equals 2; the limit of the right-hand side as λ → 0 is also 2.*

## Group A question 2: linear system

Solve the system x₁′ = x₁ + x₂, x₂′ = 4x₁ − 2x₂.

The coefficient matrix is A = [[1, 1], [4, −2]]. det A = −6, tr A = −1. The characteristic equation is λ² + λ − 6 = (λ + 3)(λ − 2), so the eigenvalues are −3 and 2. From the first equation, x₂ = x₁′ − x₁.

- x₁(t) = K₁e⁻³ᵗ + K₂e²ᵗ
- x₂(t) = −4K₁e⁻³ᵗ + K₂e²ᵗ

## Group B question 2: linear system

Solve the system x₁′ = −x₁ + 4x₂, x₂′ = x₁ + 2x₂.

A = [[−1, 4], [1, 2]], det A = −6, tr A = 1. The characteristic equation is (λ − 3)(λ + 2) = 0. The result given in the source:

- x₁(t) = 4K₁e⁻²ᵗ + K₂e³ᵗ
- x₂(t) = −K₁e⁻²ᵗ + K₂e³ᵗ

*Note: In an intermediate line of the Group B solution, the source writes x₂ = ψ′ − ψ. For this system the correct relation is x₂ = (ψ′ + ψ)/4. The two solution vectors given in the final result, however, do satisfy the system.*

## Group A question 3: sine and hyperbolic sine

L{sin(at)sinh(at)} is computed. Using sinh(at) = (eᵃᵗ − e⁻ᵃᵗ)/2 and F(s) = a/(s² + a²):

L{sin(at)sinh(at)} = [F(s − a) − F(s + a)]/2 = 2a²s/(s⁴ + 4a⁴).

## Group B question 3: cosine and hyperbolic cosine

For L{cos(at)cosh(at)}, take F(s) = s/(s² + a²):

L{cos(at)cosh(at)} = [F(s − a) + F(s + a)]/2.

The source writes the last line as a(s² + 2a²)/(s⁴ + 4a⁴).

*Note: When the fractions are added over a common denominator, the correct numerator is s(s² + 2a²). Hence the result is s(s² + 2a²)/(s⁴ + 4a⁴). For both transforms, real a and s > |a| suffice.*

## Common question 4: initial value problem

Solve y″ − 3y′ + 2y = 4e²ᵗ, y(0) = −3, y′(0) = 5 using the Laplace transform.

(s² − 3s + 2)Y(s) = 4/(s − 2) + 14 − 3s.

Result of the partial fraction decomposition:

Y(s) = −7/(s − 1) + 4/(s − 2) + 4/(s − 2)².

Inverse transform:

y(t) = −7eᵗ + 4e²ᵗ + 4te²ᵗ.

This result satisfies the equation and both initial conditions. The solution vectors of the two linear systems were also checked by differentiation.
