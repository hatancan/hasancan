---
baslik: EEM301 Signals and Systems I: Fourier Summary and Useful Relations (Alper Uraz)
ozet: A two-page formula summary for EEM301 Signals and Systems I: continuous- and discrete-time convolution, Fourier series and Fourier transform synthesis/analysis equations, useful integrals, finite and infinite geometric sums, rectangular–polar conversion, and powers of j.
---

This post contains the two-page **"Fourier Summary"** (EEM301-UsefulSummary) formula sheet distributed by Prof. Dr. Alper Uraz in the Başkent University course **EEM301 Signals and Systems I**. The document exists in two versions: the first version dated January 2007, and the version corrected in 2010 with a convolution property added. The text below is transcribed from the newer version. Both Word files can be downloaded as a ZIP at the end of the post.

## Convolution

Convolution property (added in the 2010 version):

- y(t) = h(t) ∗ x(t) ⟷ Y(ω) = H(ω) X(ω)
- y(n) = h(n) ∗ x(n) ⟷ Y(e^(jω)) = H(e^(jω)) X(e^(jω))

| | Continuous time (CT) | Discrete time (DT) |
|---|---|---|
| Non-causal x(·), h(·) | y(t) = ∫₋∞^∞ x(τ) h(t − τ) dτ | y(n) = Σ_{k=−∞}^{∞} x(k) h(n − k) |
| Causal x(·), h(·) | y(t) = ∫₀ᵗ x(τ) h(t − τ) dτ | y(n) = Σ_{k=0}^{n} x(k) h(n − k) |

## Fourier series

x(t) ⟷ aₖ and x(n) ⟷ aₖ (FS):

| | CT | DT |
|---|---|---|
| Synthesis equation | x(t) = Σ_{k=−∞}^{∞} aₖ e^(jkω₀t) | x(n) = Σ_{k=⟨N⟩} aₖ e^(jkω₀n) |
| Analysis equation | aₖ = (1/T) ∫_T x(t) e^(−jkω₀t) dt | aₖ = (1/N) Σ_{n=⟨N⟩} x(n) e^(−jkω₀n) |

## Fourier transforms

x(t) ⟷ X(ω), that is, F[x(t)] = X(ω), x(t) = F⁻¹[X(ω)]; in discrete time, x(n) ⟷ X(e^(jω)).

| | CT | DT |
|---|---|---|
| Synthesis equation | x(t) = (1/2π) ∫₋∞^∞ X(ω) e^(jωt) dω | x(n) = (1/2π) ∫_{2π} X(e^(jω)) e^(jωn) dω |
| Analysis equation | X(ω) = ∫₋∞^∞ x(t) e^(−jωt) dt | X(e^(jω)) = Σ_{n=−∞}^{∞} x(n) e^(−jωn) |

## Useful integrals

- ∫ e^(ax) sin nx dx = e^(ax)/(a² + n²) · [a sin nx − n cos nx]
- ∫ e^(ax) cos nx dx = e^(ax)/(a² + n²) · [a cos nx + n sin nx]
- ∫ x sin nx dx = sin nx / n² − x cos nx / n
- ∫ x cos nx dx = cos nx / n² + x sin nx / n
- ∫ x e^(ax) dx = e^(ax) [x/a − 1/a²]
- ∫ p·q dx = p [∫q dx] − ∫ [∫q dx] (dp/dx) dx (integration by parts)

## Useful relations

**Finite sum formula** (for any complex a):

- Σ_{n=0}^{N−1} aⁿ = (1 − a^N)/(1 − a), a ≠ 1; N for a = 1

**Infinite sum formula:**

- Σ_{n=0}^{∞} aⁿ = 1/(1 − a), |a| < 1

**Derivatives:**

- Σ_{n=0}^{N−1} n aⁿ = a(1 − a^N)/(1 − a)² − N a^N/(1 − a)
- Σ_{n=0}^{∞} n aⁿ = a/(1 − a)², |a| < 1

**With different limits** (a ≠ 1, positive/negative M, N and M ≤ N):

- Σ_{n=M}^{N−1} aⁿ = (a^M − a^N)/(1 − a); N − M for a = 1
- Σ_{n=M}^{∞} aⁿ = a^M/(1 − a), |a| < 1
- Σ_{n=1}^{N} n = N(N + 1)/2, Σ_{n=1}^{N} n² = N(N + 1)(2N + 1)/6

*Note: In the first version dated 2007, the sum Σ n aⁿ (n = 0…∞) was written as a/(1 − a); the correct expression is a/(1 − a)², which was fixed in the 2010 version.*

## Rectangular ↔ polar

For positive real a, b and integer n:

- a − jb = r e^(jθ₁) ⇒ r = √(a² + b²), θ₁ = tan⁻¹(−b/a) = −tan⁻¹(b/a)
- −a + jb = r e^(jθ₂) ⇒ r = √(a² + b²), θ₂ = π − tan⁻¹(b/a) = π + θ₁
- e^(±jnπ) = cos(nπ) = (−1)ⁿ, sin(nπ) = 0, e^(±j2πn) = 1, e^(j(2n+1)π/2) = j(−1)ⁿ

**Powers of j:**

- (−j)² = −1, (−j)³ = +j, (−j)⁴ = 1, (−j)⁵ = (−j)⁴(−j)¹ = −j, …
- (+j)² = −1, (+j)³ = −j, (+j)⁴ = 1, (+j)⁵ = (+j)⁴(+j)¹ = +j, …
