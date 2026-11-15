---
baslik: EEM301 Signals and Systems I: Notes on Signals, Fourier and Laplace Transforms (Texas A&M, Parlos and Parasuram)
ozet: Lecture notes from MEEN 651 (Alexander G. Parlos, 2003) and MEEN 364 example handouts (Parasuram, 2001–2003) from the Texas A&M University Department of Mechanical Engineering: definitions of signals and systems, Fourier series and transform, Laplace transform and its properties, mass-spring-damper transfer function, sampling and aliasing.
---

This post introduces nine PDFs dated 2017 that sit in the EEM301 Signals and Systems I folder. The documents belong to the **Texas A&M University, Department of Mechanical Engineering**: three lecture notes (Fall 2003) prepared by Dr. Alexander G. Parlos for the course **MEEN 651 Control System Design**, and example handouts signed by Parasuram (2001–2003) for the course **MEEN 364**. The texts are in English; their contents are summarized below. All the PDFs can be downloaded as a ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*

## MEEN 651 Lecture 1A: Introduction to Signals and Systems

- Signals are functions of one or more independent variables (most often time) and carry information; systems respond to input signals by producing output signals (e.g., the voltages and currents in an electrical circuit are signals, and the circuit itself is the system).
- Continuous-time and discrete-time signals and systems.
- Use of transforms:

| | Steady-state behavior | Transient behavior |
|---|---|---|
| Continuous time | Continuous Fourier transform | Laplace transform |
| Discrete time | Discrete Fourier transform | z-transform |

## MEEN 651 Lecture 1B: Fourier Analysis and Fourier Transforms

- Basic continuous-time signals: complex exponential x(t) = Ce^(at), periodic e^(jω₀t), sinusoid A cos(ω₀t + φ) = A·Re{e^(j(ω₀t+φ))}, T₀ = 2π/|ω₀|.
- Unit step u(t) and unit impulse δ(t): u(t) = ∫₋∞^t δ(τ)dτ, δ(t) = du(t)/dt.
- Fourier series x(t) = Σ a_k e^(jkω₀t); the coefficients a_k = (1/T₀)∫ x(t)e^(−jkω₀t) dt are derived by multiplying both sides by e^(−jnω₀t) and integrating over one period; letting the period go to infinity leads to the Fourier transform.
- Unit step and unit impulse sequences, complex exponentials and sinusoids in discrete time; comparison of continuous-time and discrete-time e^(jω₀t) and e^(jω₀n) (in discrete time, frequencies differing by multiples of 2π give the same signal, and periodicity requires ω₀/2π to be rational).

## MEEN 651 Lecture 2A: Laplace Transforms

- Definition: F(s) = ∫₀^∞ f(t)e^(−st) dt, s = σ + jω; inverse transform f(t) = (1/2πj)∫ F(s)e^(st) ds (in practice, partial fractions are used).
- Table: δ(t) → 1, u(t) → 1/s, t → 1/s², t² → 2/s³, e^(−at) → 1/(s + a), te^(−at) → 1/(s + a)², sin ωt → ω/(s² + ω²), cos ωt → s/(s² + ω²).
- Properties: linearity, integration (F(s)/s), differentiation (sⁿF(s) − initial-condition terms), time shift e^(−as)F(s), shift in the complex domain F(s + a), and the initial value theorem f(0⁺) = lim_{s→∞} sF(s) and final value theorem lim_{t→∞} f(t) = lim_{s→0} sF(s).
- Example: mass-spring-damper system. From the equations m dv/dt = F(t) − bv(t) − kx(t), dx/dt = v(t), we get X(s)(ms² + bs + k) = F(s) + x(0⁻)(ms + b) + mv(0⁻); with zero initial conditions the transfer function is **T(s) = X(s)/F(s) = 1/(ms² + bs + k)**.

## MEEN 364 example handouts (Parasuram)

- **Handout E.1 – Examples on Signals and Systems:** signal examples, system representation, systems with analog/discrete/digital inputs and outputs, model types, linear and nonlinear systems, time-domain and frequency-domain models.
- **Handout E.2 – Examples on Fourier Transforms:** the continuous Fourier transform of f(x) = U(x)e^(−ax), and computing the Fourier transform of a discrete-time signal using a geometric series.
- **Handout E.3 – Examples on Laplace Transforms:** examples of Laplace transforms and inverse transforms by partial fractions.
- **Examples on Sampling and Aliasing Phenomena (E.4):** when x₁(t) = cos 2π(10)t and x₂(t) = cos 2π(50)t are sampled at F_s = 40 Hz, x₁(n) = cos(πn/2) and x₂(n) = cos(5πn/2) = cos(2πn + πn/2) = cos(πn/2); the two signals are indistinguishable, and 50 Hz is an alias of 10 Hz at this sampling rate. Other examples compute the smallest sampling rate that avoids aliasing and the Nyquist rate for x(t) = 3 cos 100πt.
- **Handout on Fourier Analysis of Dynamic Signals:** elements of a digital signal processing system, classification of signals, Fourier series and transform of continuous-time and discrete-time periodic signals, the fast Fourier transform (FFT) and the use of `fft`/`ifft` in MATLAB.
- **Handout A.2 – Laplace Transforms:** definition, derivation of the transforms of basic functions, verification with MATLAB (transforms should first be done analytically, with MATLAB used only for checking), properties, steady-state value via the final value theorem, inverse transform, solving differential equations, and partial fraction expansion theorems.
