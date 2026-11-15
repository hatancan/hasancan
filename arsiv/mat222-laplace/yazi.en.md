---
baslik: MAT222 Differential Equations: The Laplace Transform (Ufuk Özerman, institution not stated)
ozet: Ufuk Özerman's 2006 note: the Laplace definition, initial value problems, step and impulse functions, shifting and convolution.
---

This post transcribes the topics, basic relations and worked results of the note "Laplace Transform" signed by **Ufuk Özerman** and dated **29 November 2006**. The document consists of 12 pages, numbered 106–117. It does not state an institution; the name of the `ege_notlari` folder in which it was stored does not, by itself, indicate that the source is Ege University. The original PDF can be downloaded at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## Integral transform and convergence

An integral transform has the form F(s) = ∫_α^β K(s,t)f(t)dt. K is the kernel. For the Laplace transform, K(s,t) = e⁻ˢᵗ and the limits are 0 and ∞:

L{f(t)} = F(s) = ∫₀^∞ e⁻ˢᵗf(t)dt.

This is an improper integral: ∫ₐ^∞ f(t)dt = lim_(A→∞) ∫ₐᴬ f(t)dt. For example, ∫₀^∞ eᶜᵗdt converges for c < 0 and diverges for c ≥ 0. For piecewise continuous functions, the comparison test can be used: if |f| ≤ g and the integral of g converges, then the integral of f converges absolutely.

In the source's existence theorem, after the conditions of piecewise continuity on every finite interval and |f(t)| ≤ Keᵃᵗ for large t are given, it is stated that the transform exists "for s > 0."

*Note: If the exponential growth bound is Keᵃᵗ, the sufficient condition is s > a. The condition s > 0 is not sufficient for a general a.*

## Basic transforms

| f(t) | L{f(t)} |
|---|---|
| 1 | 1/s |
| t | 1/s² |
| t² | 2/s³ |
| t³ | 6/s⁴ |
| eᵃᵗ | 1/(s − a) |
| sin(at) | a/(s² + a²) |
| cos(at) | s/(s² + a²) |
| sinh(at) | a/(s² − a²) |
| cosh(at) | s/(s² − a²) |

For polynomials and trigonometric functions, s > 0 is sufficient; for eᵃᵗ, s > a; for hyperbolic functions with real a, s > |a|. The transform is linear: L{c₁f₁ + c₂f₂} = c₁F₁ + c₂F₂.

## Transforms of derivatives

- L{y′} = sY(s) − y(0).
- L{y″} = s²Y(s) − sy(0) − y′(0).
- L{y⁽ⁿ⁾} = sⁿY(s) − sⁿ⁻¹y(0) − … − y⁽ⁿ⁻¹⁾(0).

Order of application: take the transform of the equation, substitute the initial conditions, solve for Y(s), decompose into partial fractions, and apply the inverse transform.

**Example:** y″ + y = sin 2t, y(0) = 2, y′(0) = 1.

(s² + 1)Y = 2s + 1 + 2/(s² + 4).

Y = 2s/(s² + 1) + (5/3)/(s² + 1) − (2/3)/(s² + 4).

y(t) = 2 cos t + (5/3)sin t − (1/3)sin 2t.

The result satisfies both the equation and the initial conditions.

## Step function and shifting

u_c(t) is 0 for t < c and 1 for t ≥ c. For c ≥ 0, L{u_c} = e⁻ᶜˢ/s.

- L{u_c(t)f(t − c)} = e⁻ᶜˢF(s).
- L{eᶜᵗf(t)} = F(s − c).

**Example:** For f(t) = sin t + u_(π/4)(t)cos(t − π/4), F(s) = [1 + se^(−πs/4)]/(s² + 1).

**Example:** The inverse transform of (1 − e⁻²ˢ)/s² is t − u₂(t)(t − 2). This function equals t for 0 ≤ t < 2 and 2 for t ≥ 2.

**Example:** The inverse transform of 1/(s² − 4s + 5) = 1/[(s − 2)² + 1] is e²ᵗ sin t.

## Discontinuous forcing

2y″ + y′ + 2y = u₅(t) − u₂₀(t), y(0) = y′(0) = 0.

Y(s) = (e⁻⁵ˢ − e⁻²⁰ˢ)H(s), H(s) = 1/[s(2s² + s + 2)].

H(s) = 1/(2s) − (s + 1/2)/(2s² + s + 2).

Accordingly, y(t) = u₅(t)h(t − 5) − u₂₀(t)h(t − 20). The inverse transform in the source:

h(t) = 1/2 − (1/2)e^(−t/4)[cos(√15·t/4) + (1/√15)sin(√15·t/4)].

## Impulse functions

For the Dirac delta, with t₀ > 0, L{δ(t − t₀)} = e⁻ˢᵗ⁰.

For the example g(t) = 2δ(t − 7) + 5δ(t + 3), the source writes 2e⁻⁷ˢ + 5e³ˢ; in an intermediate line δ(t + 2) also appears.

*Note: In the one-sided Laplace transform defined in this note, the impulse at t = −3 lies outside the integration interval. For the given g, the transform is 2e⁻⁷ˢ. The e³ˢ term belongs to the two-sided transform; the δ(t + 2) intermediate line is also inconsistent with the initial expression.*

**Example:** For y″ + y′ + y = δ(t − 2), y(0) = y′(0) = 0, Y(s) = e⁻²ˢ/(s² + s + 1).

Completing the square gives s² + s + 1 = (s + 1/2)² + 3/4.

The impulse response given in the source, once the roots are simplified, is y(t) = u₂(t)(2/√3)e^(−(t−2)/2)sin[√3(t − 2)/2].

As homework, 2y″ + y′ + 2y = δ(t − 5), y(0) = y′(0) = 0 is given.

## Convolution

(f ∗ g)(t) = ∫₀ᵗ f(t − τ)g(τ)dτ = ∫₀ᵗ f(τ)g(t − τ)dτ.

L{f ∗ g} = F(s)G(s).

*Note: The introductory sentence in the source describes F(s)G(s) as the transform of the "product" of f and g. What is meant here is not the pointwise product but the convolution; the integral definition immediately following is correct.*

- For f(t) = cos t, (f ∗ 1)(t) = sin t; the result is not equal to f(t).
- L⁻¹{a/[s²(s² + a²)]} = ∫₀ᵗ (t − τ)sin(aτ)dτ = (at − sin at)/a².
- The source writes L⁻¹{1/[s(s² + 16)]} = (1 − cos 4t)/4.

*Note: In the last integral, a second factor of 1/4 is missing. ∫₀ᵗ (1/4)sin(4τ)dτ = (1 − cos 4t)/16 should hold.*

The final example is the problem y″ + 4y = g(t), y(0) = 3, y′(0) = −1 with a general g(t):

y(t) = 3 cos 2t − (1/2)sin 2t + (1/2)∫₀ᵗ sin[2(t − τ)]g(τ)dτ.
