---
baslik: EEM322 Control Systems: Course Notebook (March 2013) – State Space, State Transition Matrix, Companion and Modal Forms, Controllability and Observability
ozet: State-space weeks from the 2013 EEM322 Control Systems course notebook: the resolvent matrix (sI−A)⁻¹ and e^(At), state equations of an RLC circuit, transformation to companion form and to modal form via Vandermonde, direct, cascade and parallel decomposition, and controllability and observability with water-tank examples.
---

This post contains the state-space material from a friend's **course notebook** for the 2013 spring semester of Başkent University's **EEM322 Control Systems** course (pages photographed on 7, 14 and 16 March 2013). The content was **transcribed from the photographed pages into text**; the photos have not been published. The examples were written in English in class, and the Turkish margin notes were transcribed as well. The calculations were checked; small typos in the notebook are pointed out in notes. One blurry page could not be read and was skipped.

For the topic explanation, see the post [Lecture 3](/arsiv/eem322-ders-03-durum-uzayi/). The previous and next sections of the notebook: [modeling and block diagrams](/arsiv/eem322-defter-modelleme-blok-diyagram/), [steady-state error, Routh and root locus](/arsiv/eem322-defter-kalici-hata-routh-kok-yer/).

## Verification with Mason's rule

At the top of the page, the result of a block diagram reduction, (G₁ + G₂)/(1 + G₁H), is verified with a signal flow graph: forward paths P₁ = G₁, P₂ = G₂, loop L₁ = −G₁H, Δ = 1 + G₁H, Δ₁ = Δ₂ = 1 ⇒ (P₁Δ₁ + P₂Δ₂)/Δ = (G₁ + G₂)/(1 + G₁H).

## Example 1: Solution of the state equation

Block diagram of the state-space model: u → B → summing junction → ẋ → ∫ → x → C → (summed with D) y, with feedback through A.

- ẋ = [[−1, −3], [1, −5]] x + [1, 0]ᵀ u, y = [1, −1] x, D = 0
- u(t) = 1 (t ≥ 0), x(0) = [1, 0]ᵀ

**(a) Zero-input (homogeneous) solution:** X(s) = (sI − A)⁻¹x(0) or x(t) = e^(At)x(0). Resolvent matrix:

- sI − A = [[s + 1, 3], [−1, s + 5]], det(sI − A) = s² + 6s + 8 = (s + 2)(s + 4)
- (sI − A)⁻¹ = (1/Δ(s))·[[s + 5, −3], [1, s + 1]]
- Partial fractions: [[3/2/(s+2) − 1/2/(s+4), −3/2/(s+2) + 3/2/(s+4)], [1/2/(s+2) − 1/2/(s+4), −1/2/(s+2) + 3/2/(s+4)]]

State transition matrix via inverse Laplace transform:

- Φ(t) = e^(At) = [[(3/2)e^(−2t) − (1/2)e^(−4t), −(3/2)e^(−2t) + (3/2)e^(−4t)], [(1/2)e^(−2t) − (1/2)e^(−4t), −(1/2)e^(−2t) + (3/2)e^(−4t)]]
- Zero-input state response: x(t) = e^(At)[1, 0]ᵀ = [(3/2)e^(−2t) − (1/2)e^(−4t), (1/2)e^(−2t) − (1/2)e^(−4t)]ᵀ

**(b) Output for u(t) = 1 and x(0) = [1, 0]ᵀ:**

- Y(s) = C(sI − A)⁻¹x(0) + C(sI − A)⁻¹B U(s)
- = (1/Δ(s))·{[1, −1][s + 5, 1]ᵀ + [1, −1][(s + 5)/s, 1/s]ᵀ} = (s² + 5s + 4)/[sΔ(s)] = (s + 1)/[s(s + 2)]
- y(t) = 1/2 + (1/2)e^(−2t)

Note from the source: All simplifications and matrix operations should be done in the Laplace domain, and the inverse Laplace transform should be applied at the very end.

## Example 2: State equations of an RLC circuit

A circuit consisting of a source vi, R₁ = 4 kΩ, C₁ = 0.25 mF, L = 2 mH, C₂ = 0.5 mF, R₂ = 1 kΩ, and a current source is. Node equations:

- C₁ dv₁/dt + iL − (vi − v₁)/R₁ = 0 ⇒ 0.00025 dv₁/dt + iL − (vi − v₁)/4000 = 0
- C₂ dv₂/dt − iL + v₂/R₂ − is = 0 ⇒ 0.0005 dv₂/dt − iL + v₂/1000 − is = 0
- L diL/dt + v₂ − v₁ = 0 ⇒ 0.002 diL/dt + v₂ − v₁ = 0

State variables x₁ = v₁, x₂ = v₂, x₃ = iL; inputs u₁ = vi, u₂ = is; output y = v₂:

- ẋ₁ = −x₁ − 4000x₃ + u₁
- ẋ₂ = −2x₂ + 2000x₃ + 2000u₂
- ẋ₃ = 500x₁ − 500x₂
- A = [[−1, 0, −4000], [0, −2, 2000], [500, −500, 0]], B = [[1, 0], [0, 2000], [0, 0]], C = [0, 1, 0]

*Note: In the notebook the first equation is written as "dv₁/dt = v₁ − 4000iL + vi"; the correct sign is −v₁ (the state-variable form is correct: −x₁).*

## Example 3: Transformation to companion form

For the system in Example 1, the characteristic equation is Δ(s) = |sI − A| = s² + 6s + 8 = 0.

- Controllability matrix U = [B, AB] = [[1, −1], [0, 1]], |U| ≠ 0 ⇒ companion form is possible
- U⁻¹ = [[1, 1], [0, 1]], q = [0, 1]U⁻¹ = [0, 1] (last row of U⁻¹)
- Q = [q; qA] = [[0, 1], [1, −5]], Q⁻¹ = [[5, 1], [1, 0]]
- With the transformation w = Qx, ẇ = QAQ⁻¹w + QBu = [[0, 1], [−8, −6]]w + [0, 1]ᵀu
- y = CQ⁻¹w + Du = [4, 1]w

## Example 4: Modal matrix

System in companion form: ẇ = [[0, 1], [−8, −6]]w + [0, 1]ᵀu, y = [4, 1]w, w(0) = Qx(0) = [0, 1]ᵀ.

- Δ(s) = |sI − Ac| = s² + 6s + 8 ⇒ λ₁ = −2, λ₂ = −4
- With the Vandermonde approach, the eigenvectors follow directly: m₁ = [1, λ₁]ᵀ = [1, −2]ᵀ, m₂ = [1, λ₂]ᵀ = [1, −4]ᵀ
- M = [[1, 1], [−2, −4]], M⁻¹ = [[2, 0.5], [−1, −0.5]]
- Λ = M⁻¹AcM = diag(−2, −4), Γ = M⁻¹Bc = [0.5, −0.5]ᵀ, F = CcM = [2, 0]
- ż = Λz + Γu, y = Fz

Transfer function in the three representations:

- G(s) = C(sI − A)⁻¹B = (s + 4)/[(s + 2)(s + 4)] = 1/(s + 2)
- Gc(s) = Cc(sI − Ac)⁻¹Bc = [4, 1]·(1/Δ)[[s + 6, 1], [−8, s]]·[0, 1]ᵀ = 1/(s + 2)
- Gm(s) = F(sI − Λ)⁻¹Γ = 1/(s + 2)

G(s) = Gc(s) = Gm(s) and Δ(s) = |sI − A| = |sI − Ac| = |sI − Λ|, as expected.

**4(b) Modal decomposition (free response):** For ẇ = [[0, 1], [−8, −6]]w, the new initial vector is z(0) = M⁻¹w(0) = [0.5, −0.5]ᵀ.

- w = Mz = M e^(Λt) z(0) = [m₁, m₂]·diag(e^(−2t), e^(−4t))·z(0)
- w(t) = 0.5e^(−2t)[1, −2]ᵀ − 0.5e^(−4t)[1, −4]ᵀ

*Note: At the beginning of Example 4, the notebook writes the companion-form matrix without signs ([[0, 1], [8, 6]]); the correct form is [[0, 1], [−8, −6]]. The second row of M⁻¹ is also written as [−1, 0.5]; the correct form is [−1, −0.5] (Γ was computed with this correct value). In the free response, the coefficient of the second term should be −0.5; this way w(0) = [0, 1]ᵀ is satisfied.*

## Example 5: Transfer function decompositions

G(s) = (3s² + 9s + 6)/(s³ + 7s² + 12s) = 3(s + 1)(s + 2)/[s(s + 3)(s + 4)]

**(i) Direct decomposition:**

- Y/U = (3s⁻¹ + 9s⁻² + 6s⁻³)/(1 + 7s⁻¹ + 12s⁻²)
- X(s) = U(s) − 7s⁻¹X(s) − 12s⁻²X(s), Y(s) = 3s⁻¹X(s) + 9s⁻²X(s) + 6s⁻³X(s)
- Moving to the time domain by choosing the integrator outputs as state variables: ẋ = [[0, 1, 0], [0, 0, 1], [0, −12, −7]]x + [0, 0, 1]ᵀu, y = [6, 9, 3]x

**(ii) Cascade (series) decomposition:** Y/U = (3/s)·[(s + 1)/(s + 3)]·[(s + 2)/(s + 4)]

- (s + z)/(s + p) = (1 + z s⁻¹)/(1 + p s⁻¹) ⇒ X = U − p s⁻¹X, Y = X + z s⁻¹X
- a/s ⇒ X = U, Y = a s⁻¹X
- When the blocks 1/s·3 → (s + 1)/(s + 3) → (s + 2)/(s + 4) are arranged in this order and the integrators are expanded, a triangular-form A matrix results: ẋ = [[−4, −2, 3], [0, −3, 3], [0, 0, 0]]x + [0, 0, 1]ᵀu, y = [2 − 4, 1 − 3, 3]x = [−2, −2, 3]x

*Note: The (2,3) element of the matrix in the notebook looks like −3; since the input of the (s + 1)/(s + 3) block is 3x₃, ẋ₂ = −3x₂ + 3x₃, so the element should be +3.*

**(iii) Parallel decomposition:** The first step is the partial fraction expansion:

- G(s) = (1/2)/s − 2/(s + 3) + (9/2)/(s + 4)
- a/(s + p) = a s⁻¹/(1 + p s⁻¹) ⇒ X = U − p s⁻¹X, Y = a s⁻¹X
- ẋ = [[0, 0, 0], [0, −3, 0], [0, 0, −4]]x + [1, 1, 1]ᵀu, y = [1/2, −2, 9/2]x

## Controllability and observability: water tanks (Example 6, ρ = 1)

**(a)** The upper tank (A₁, R₁) drains into the lower tank (A₂, R₂), the input u goes to the lower tank, and the output is y = x₂/R₂:

- A₁ẋ₁ = −x₁/R₁, A₂ẋ₂ = x₁/R₁ − x₂/R₂ + u
- For A₁ = A₂ = 1, R₁ = R₂ = 1: ẋ = [[−1, 0], [1, −1]]x + [0, 1]ᵀu, y = [0, 1]x
- U = [B, AB] = [[0, 0], [1, −1]] ⇒ rank 1 (determinant 0) ⇒ uncontrollable
- V = [C; CA] = [[0, 1], [1, −1]] ⇒ rank 2 ⇒ observable

*Note: In the notebook the second row of the general matrix is written as [1/(R₁R₂), −1/(R₁A₂)]; according to the equations the correct form is [1/(R₁A₂), −1/(R₂A₂)], with B = [0, 1/A₂]ᵀ.*

**(b)** The input goes to the upper tank, and the output is the flow rate of the upper tank (y = [1, 0]x): ẋ = [[−1, 0], [1, 0]]x + [1, 0]ᵀu ⇒ controllable, unobservable.

**(c)** The input and output are at the first tank, and the second tank is disconnected: ẋ = [[−1, 0], [0, 0]]x + [1, 0]ᵀu, y = [1, 0]x ⇒ uncontrollable, unobservable.

**(d)** Two side-by-side tanks connected through R₁; the input goes to the first tank, and the output is the flow rate of the second tank through R₂:

- A₁ẋ₁ = (x₂ − x₁)/R₁ + u, A₂ẋ₂ = −(x₂ − x₁)/R₁ − x₂/R₂, y = x₂/R₂
- With unit values, ẋ = [[−1, 1], [1, −2]]x + [1, 0]ᵀu, y = [0, 1]x ⇒ controllable and observable

## Example 7: Invariance under similarity transformation

Diagonal form from Example 4: ż = diag(−2, −4)z + [0.5, −0.5]ᵀu, y = [2, 0]z. Since the elements of Λ are negative, the system is stable; because of the 0 in the output matrix, the λ₂ = −4 mode is unobservable.

| Representation | U = [B, AB] | det U | V = [C; CA] | det V | Result |
|---|---|---|---|---|---|
| General (A, B, C) | [[1, −1], [0, 1]] | 1 | [[1, −1], [−2, 2]] | 0 | Controllable, unobservable |
| Companion form (Ac, Bc, Cc) | [[0, 1], [1, −6]] | −1 | [[4, 1], [−8, −2]] | 0 | Controllable, unobservable |
| Diagonal (Λ, Γ, F) | [[0.5, −1], [−0.5, 2]] | 0.5 | [[2, 0], [−4, 0]] | 0 | Controllable, unobservable |

The controllability and observability properties are **invariant** under similarity transformation. The unobservable λ₂ = −4 mode appears as the (s + 4) factor that cancels in the transfer function in Example 4: G(s) = Gc(s) = Gm(s) = (s + 4)/[(s + 2)(s + 4)] = 1/(s + 2).
