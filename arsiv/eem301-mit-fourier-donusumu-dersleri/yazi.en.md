---
baslik: EEM301 Signals and Systems I: Continuous- and Discrete-Time Fourier Transform Lectures (MIT 6.003, Alan Willsky, 2007)
ozet: Summary of lectures 8, 9 and 10 from the Spring 2007 MIT Signals and Systems course: derivation of the continuous-time Fourier transform, examples and properties, the convolution and multiplication properties, frequency response, Parseval's relation, and the discrete-time Fourier transform and its properties.
---

This post presents three PowerPoint lecture decks kept as source material in the EEM301 Signals and Systems I folder: **Lecture #8 (March 6, 2007), #9 (March 8, 2007) and #10 (March 13, 2007)** of the Spring 2007 **MIT Signals and Systems** course; the author of the slides appears to be Alan Willsky. The topics follow Chapters 4 and 5 of the Oppenheim & Willsky textbook. The slides are in English; the headings and main ideas are summarized below. The original slides can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## Lecture 8: Continuous-time Fourier transform (CTFT)

1. Derivation of the Fourier transform pair
1. Examples of Fourier transforms
1. Fourier transform of periodic signals
1. Properties of the CTFT

- **Fourier's derivation:** An aperiodic x(t) is viewed as the limit of a periodic signal whose period T → ∞. The harmonics are spaced ω₀ = 2π/T apart; as T grows, ω₀ → 0, the discrete frequency points become denser, and the Fourier series sum turns into an integral (square wave example).
- **Which signals it applies to:** finite-energy signals (the error signal has zero energy) and signals satisfying the Dirichlet conditions; by allowing impulses in x(t) or X(jω), periodic signals are covered as well.
- **Examples:** the impulse and shifted impulse, exponential functions (even and odd symmetry), the rectangular pulse in time (the inverse relationship between the two widths: the uncertainty principle), and the Gaussian function e^(−at²) (its transform is again a Gaussian; Δt·Δω ~ 1, so both widths cannot be made arbitrarily small at the same time).
- **Periodic signals:** the "line spectrum"; for an impulse train (sampling function), the period is T in time and 2π/T in frequency (again an inverse relationship).
- **Properties:** linearity, time shifting (magnitude unchanged, linear change in phase), conjugate symmetry (if x(t) is real and even, X is real and even; if real and odd, X is imaginary and odd), and time scaling.

## Lecture 9: The convolution property and introduction to the DTFT

1. The convolution property of the CTFT
1. Frequency response and LTI systems
1. The multiplication property and Parseval's relation
1. The discrete-time Fourier transform

- **Convolution property:** y(t) = h(t) ∗ x(t) ⟷ Y(jω) = H(jω)X(jω); a consequence of the eigenfunction property. The frequency response of a continuous-time LTI system is the Fourier transform of its impulse response.
- **Examples:** the differentiator (H(jω) = jω, which amplifies high frequencies and sharpens edges); the impulse response of the ideal lowpass filter (is it causal? what is h(0)? what is the final value of the step response?); cascaded filtering operations; Gaussian ∗ Gaussian = Gaussian.
- **LTI systems described by linear constant-coefficient differential equations:** by the differentiation property, H(jω) is a rational function; h(t) is found by partial fractions. If X(jω) is rational, then Y(jω) is also rational.
- **Parseval's relation** and the **multiplication property:** by duality, multiplication in time corresponds to convolution in frequency; amplitude modulation examples.
- **Derivation of the DTFT:** similar to the continuous-time case, from the Fourier series of a discrete periodic signal whose period goes to infinity.

## Lecture 10: Discrete-time Fourier transform (DTFT)

1. DTFT examples
1. Properties of the DTFT
1. The convolution property and its uses

- **DTFT pair:** analysis equation X(e^(jω)) = Σ x[n]e^(−jωn), synthesis equation x[n] = (1/2π)∫_{2π} X(e^(jω))e^(jωn) dω. Since the synthesis equation integrates over a finite interval, there is no convergence issue; the analysis equation requires finite energy or absolute summability.
- **Examples:** discrete counterparts of the continuous-time examples, the discrete-time rectangular pulse (plotted for N₁ = 2), and sums of complex exponentials: the DTFT of e^(jω₀n) is an impulse of area 2π at ω₀, but since X(e^(jω)) must be 2π-periodic, there are impulses at all the points ω₀ + 2πk. The discrete sinusoid and the discrete periodic impulse train (which is also a periodic impulse train in the frequency domain).
- **Properties:** linearity, shifts, conjugate symmetry, and properties that differ in discrete time because of periodicity; **time expansion:** x[n/2] is undefined and x[2n] misses the odd-indexed values; instead, inserting (k − 1) zeros between successive values gives x_(k)[n]; expansion by a factor of k in time means compression by a factor of k in frequency. Differentiation in frequency and Parseval's relation (the total energy in the time and frequency domains is equal).
- **Convolution property:** y[n] = x[n] ∗ h[n] ⟷ Y(e^(jω)) = X(e^(jω))H(e^(jω)); the examples include the ideal discrete-time lowpass filter.
