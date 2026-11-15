---
baslik: EEM322 Control Systems: Quiz Preparation Notebook Notes (Summer 2013 and Spring 2015)
ozet: Quiz preparation notebook notes for EEM322 Control Systems: state model of a mass-spring-damper, stability questions, transfer function and time response from a differential equation and from state space, frequency response, similarity transformation and an eigenvalue quiz question, second-order response design with a PI controller.
---

This post is a text transcription of the notebook photos found at the root of the EEM322 Control Systems folder. There are two groups: worked problems and lecture-note pages kept while preparing for quizzes and exams during the **2013 summer school** (July–August 2013); and notes from the **2015 spring semester** (8 April 2015) notebook on similarity transformation, a "quiz question", and second-order systems. **Transcribed from photographed pages to text**; the photos were not published. The photos of textbook pages in the same folder were not published either.

## 2013: Definitions from Lecture Notes

- A system is modeled once it is converted from a visual form into a mathematical form. Points to watch: input, output, disturbance, and system variables; whether the parameters change or not.
- **Linear system:** homogeneity F(au) = aF(u) and superposition F(u + ũ) = F(u) + F(ũ) are satisfied.
- **Time-varying / time-invariant:** the distinction is made through the parameters; if the parameters change, the system is time-varying.
- **Dynamic / static:** a dynamic system has energy-storing elements and initial values, and its output evolves over time; a static system has no initial values, and its output appears immediately.
- **Open-loop** control has no measurement; **closed-loop** control has measurement (sensors and transducers). Block diagram: reference → comparator → controller → actuator → process → output, with feedback from the measuring element. Disturbances are external effects.
- In terms of the physical quantity being controlled: **servomechanism** (the input is tracked) and **regulator** systems; analog and digital control systems.
- Time response criteria: **peak time Tp** (time for the response to reach its peak), **overshoot %OS** (ratio of the difference between the peak value and the steady-state value to the steady-state value), **rise time Tr** (time for the response to go from 10% to 90%), **settling time Ts** (time for the response to settle within 98% of the steady-state value). In proportional control with Gp = K/(τs + 1), the error is E(s) = R(s)/(1 + K).

## 2013: Worked Problems

### State model for a mass-spring-damper

State-space model of a mass m driven by a force F, with damping D and spring K (position x₁, velocity x₂): mÿ = F − Dẏ − Ky ⇒ ẋ₁ = x₂, ẋ₂ = (1/m)(−Dx₂ − Kx₁ + u).

> A = [0 1; −K/m −D/m], B = [0; 1/m], C = [1 0], D = 0

### Which one is stable?

- (s − 1)/(s + 1): pole −1 ⇒ stable.
- (s² − 1)/(s² + 2s + 2): Δ = 4 − 8 = −4 ⇒ poles −1 ± j ⇒ stable.
- (s − 1)/(s² − 1) = 1/(s + 1): pole −1 after cancellation ⇒ stable (note the cancelled s = 1 pole with regard to internal stability).
- A block with gain 2 and −1/(s − 1) in a system with positive feedback: TF = (−2/(s − 1)) / (1 + 2/(s − 1)) = −2/(s + 1) ⇒ pole −1, stable.

### Block diagram reduction

The positive feedback loop formed by G₂ and G₃ is reduced to G₅ = G₂/(1 − G₂G₃); together with G₄, the inner loop is written as G₈ = G₄G₅/(1 + G₄G₅). The problem is left at this point in the notebook ("no continuation").

### Transfer function from a differential equation

y″ + 3y′ + 2y = 3u′ − u ⇒ s²Y + 3sY + 2Y = 3sU − U ⇒ **Y(s)/U(s) = (3s − 1)/(s² + 3s + 2)**.

### Transfer function and time response from state space

ẋ = [−6 −3.5; 6 4]x + [−1; 1]u, y = [4 5]x, x(0) = (−2, 1).

1. Y(s) = C(sI − A)⁻¹x(0) (zero-input response) + [C(sI − A)⁻¹B + D]U(s) (zero-state response).
1. det(sI − A) = (s + 6)(s − 4) + 21 = s² + 2s − 3; (sI − A)⁻¹ = [s − 4 −3.5; 6 s + 6]/(s² + 2s − 3).
1. **G(s) = C(sI − A)⁻¹B = (s + 2)/(s² + 2s − 3)**.
1. With U(s) = 1/s, Y(s) = (−3s − 12)/(s² + 2s − 3) + (s + 2)/[(s² + 2s − 3)s] = (−3s² − 11s + 2)/[(s − 1)(s + 3)s].
1. Partial fractions: −3/(s − 1) + (2/3)/(s + 3) − (2/3)/s ⇒ **y(t) = −3eᵗ + (2/3)e^(−3t) − 2/3**. Because of the s = 1 pole, the response grows unbounded (the system is unstable).

### Frequency response

G(s) = 0.5/(s + 0.5) ⇒ |G(jω)| = 0.5/√(ω² + 0.25), ∠G(jω) = −tan⁻¹(ω/0.5).

| ω (rad/s) | \|G(jω)\| | ∠G(jω) |
|---|---|---|
| 0.2 | 0.928 | −0.385 rad = −21.8° |
| 1.8 | 0.268 | −1.300 rad = −74.5° |

### Intuitive explanation of gain/phase margin and stability

At the phase crossover frequency, the process has |G(jωx)| = K and ∠G(jωx) = −180°. If a 2 sin 5t signal is applied to the closed loop and the loop is cut open, the signal at point Q becomes −K × (the signal at P):

- K = 0.5: at P, 2 sin 5t, 1 sin 5t, 0.5 sin 5t … the signal halves on each pass ⇒ **stable**.
- K = 1: the signal stays 2 sin 5t ⇒ **marginally stable** (conditionally stable).
- K = 3: 2, 6, 18 sin 5t … the signal grows ⇒ **unstable**.

Rule: if the gain at the phase crossover frequency is below 0 dB (gain margin > 0) and the phase at the gain crossover frequency is above −180° (phase margin > 0), that is, if both hold, the system is stable.

## 2015: Similarity Transformation and Quiz Question

### Similarity transformation

With the transformation x = Mz, the system ẋ = Ax + Bu is brought into the form ż = Λz + Γu: Λ = M⁻¹AM, Γ = M⁻¹B, z(0) = M⁻¹x(0). The columns of M are the eigenvectors of A; Λ becomes diagonal (the eigenvalues) and e^(Λt) = diag(e^(λ₁t), …, e^(λₙt)). The solution decomposes into modes as x(t) = M·e^(Λt)·z(0) = z₁(0)e^(λ₁t)m₁ + … + zₙ(0)e^(λₙt)mₙ (modal decomposition; the same as parallel decomposition). In discrete time, Z⁻¹{z(zI − A)⁻¹} = Aᵏ; in continuous time, L⁻¹{(sI − A)⁻¹} = e^(At).

Example: A = [0 1; −2 −3] ⇒ Λ = [−1 0; 0 −2], M = [1 1; −1 −2].

### Quiz question

ẋ = [0 1; −3 −4]x + [0; 1]u, x(0) = [1 1]ᵀ. M = ? ż = Λz + Γu, z(0) = ?

1. |λI − A| = λ² + 4λ + 3 = (λ + 3)(λ + 1) = 0 ⇒ λ₁ = −1, λ₂ = −3.
1. (λ₂I − A)v₂ = 0 ⇒ [−3 −1; 3 1]v₂ = 0 ⇒ v₂ = [1; −3]. Similarly, v₁ = [1; −1].
1. **M = [1 1; −1 −3]**.

*Note: In the notebook the solution ends at M. Continuation: M⁻¹ = [1.5 0.5; −0.5 −0.5], Λ = diag(−1, −3), Γ = M⁻¹B = [0.5; −0.5], z(0) = M⁻¹x(0) = [2; −1].*

### Third-order example

ẋ = [0 1 −1; −6 −11 6; −6 −11 5]x. |λI − A| = λ³ + 6λ² + 11λ + 6 ⇒ λ₁ = −1, λ₂ = −2, λ₃ = −3. Eigenvectors v₁ = [1; 0; 1], v₂ = [1; 2; 4], v₃ = [1; 6; 9] (checked with Av = λv). The note states that the form will differ if one of the roots is complex.

## 2015: Second-Order Systems

- T(s) = ωn²/(s² + 2ζωn s + ωn²); 0 < ζ < 1 is underdamped, ζ = 0 is undamped (ωn is the natural frequency). Roots are −ζωn ± jωd; ωd is the damped natural frequency.
- Overshoot PO = 100·exp(−ζπ/√(1 − ζ²)), settling time ts(2%) = 4/(ζωn); the peak time Tp and settling time Ts are shown on the plot.
- Example state model: A = [0 1; −3 −4], B = [0; 1], y = 10x₁ ⇒ ẋ₁ = x₂, ẋ₂ = −3x₁ − 4x₂ + u.

### Design with a PI controller

In a unity-feedback loop with C(s) = Kp + Ki/s and G(s) = 10/(s + 2); desired ess → 0, PO ≤ 20%, ts(2%) ≤ 2 s.

1. T(s) = C(s)G(s)/[1 + C(s)G(s)] = 10(Kp·s + Ki)/[s² + (2 + 10Kp)s + 10Ki].
1. PO = 20 ⇒ ζ = 0.455; ts = 4/(ζωn) = 2 ⇒ ζωn = 2 ⇒ ωn = 4.396, ωn² = 19.325.
1. s² + (2 + 10Kp)s + 10Ki = s² + 4s + 19.325 ⇒ **Kp = 0.2**, **Ki ≈ 1.93**.

### Question

G(s) = 1/[s(s + 1)], unity feedback: T(s) = 1/(s² + s + 1) ⇒ ωn = 1, 2ζωn = 1 ⇒ ζ = 0.5. PO = 100·e^(−π/√3) = 16.3%, ts(2%) = 4/(ζωn) = 8 s, for a step input (type 1) ess = 0.
