---
baslik: EEM322 Control Systems: Lecture Notebook (March–April 2013) – Steady-State Error, Sinusoidal Response, Routh Table, Axis Shifting and Root Locus
ozet: Worked examples from the 2013 EEM322 Control Systems lecture notebook: steady-state response to polynomial and sinusoidal inputs, converting a non-unity feedback system to an equivalent unity feedback system, zero element and zero row in the Routh table, stability range of K, axis shifting, imaginary-axis crossing on the root locus, breakaway point, departure angle, K for ζ = 0.7, and root finding with Horner/Newton.
---

This post contains examples on steady-state error, stability and the root locus from a friend's **lecture notebook** for the 2013 spring semester of the Başkent University course **EEM322 Control Systems** (pages photographed on 29 March, 14–15 and 19 April 2013). The content was **transcribed to text from the photographed pages**; the photographs themselves were not published. The examples were written in English in class; the Turkish side notes were transcribed as well. The calculations have been checked. The photographs of the textbook pages on Routh and the root locus that the course followed were not transcribed, since they are pages from the book.

For the theory, see the posts [Lecture 6](/arsiv/eem322-ders-06-kararlilik/), [Lecture 7](/arsiv/eem322-ders-07-surekli-hal-hatalari/) and [Lecture 8](/arsiv/eem322-ders-08-kok-yer-egrisi/). Earlier sections of the notebook: [modeling and block diagrams](/arsiv/eem322-defter-modelleme-blok-diyagram/), [state space](/arsiv/eem322-defter-durum-uzayi/).

## Steady-state error

### Example 2(b): Non-unity feedback (b ≠ 1)

In part (a) of the example, which began on the previous page, it was found that the output tracks a ramp input with a finite ess and that the system is type 1. In part (b) the feedback is b ≠ 1:

- W(s) = [s² + 3s + 10(b − 1)]/(s² + 3s + 10b)
- C₀ = W(0) = (b − 1)/b, C₁ = dW(s)/ds (s = 0) = 3/(10b²)
- For R(s) = 1/s: ess = lim(s→0) sR(s)W(s) = W(0) = (b − 1)/b (finite result for a step input)
- For R(s) = 1/s²: ess = lim(s→0) (1/s)W(s) = ∞
- The output tracks a step input with a finite ess; the system is type 0.

### Example 3(a): Polynomial input

Here G(s) is not given; the closed-loop transfer function is given directly (note in the notebook: "G(s) is not given here, pay attention to that!"):

- T(s) = (3s + 2)/(s² + 3s + 2) = (b₁s + b₀)/(s² + a₁s + a₀)
- The steady-state error for both step and ramp inputs is zero if b₀ = a₀ and b₁ = a₁; if only a₀ = b₀, the error is zero for the step input only.

(i) For a step input r(t) = 4:

- css(t) = lim(t→∞) c(t) = T(0)·a = (b₀/a₀)·a = (2/2)·4 = 4

(ii) For r(t) = 2 + t (step and ramp together):

- r₁(t) = 2 ⇒ css₁(t) = 2
- r₂(t) = t ⇒ css₂(t) = T(0)·t + T′(0)·1 = (b₀/a₀)t + [(a₀b₁ − b₀a₁)/a₀²]·1 = t
- By superposition, css(t) = 2 + t

Error expressions:

- Position error: ep(t) = |(a₀ − b₀)/a₀| = |1 − T(0)| = 0
- Velocity error: ev(t) = |(1 − T(0))t − T′(0)| = |[(a₀ − b₀)/a₀]t − (a₀b₁ − b₀a₁)/a₀²| = 0

Thus asymptotic tracking is achieved for both (i) and (ii): css(t) = lim c(t) = r(t).

### Example 4(a): Sinusoidal input

- T(s) = 3/(s + 0.4), r(t) = 5 sin 2t, ω = 2
- T(j2) = 3/(0.4 + j2) = 3/(2.04 e^(j1.37)) = 1.47 e^(−j1.37)
- css(t) = X·|T(jω)|·sin(ωt + φ) = 5 × 1.47 sin(2t − 1.37) = 7.35 sin(2t − 1.37), X = 5, φ = ∠T(jω) = −1.37 rad

### Example 5(a): Non-unity feedback

G(s) = 2/(s² + 3s), H(s) = 5s + 2. First, the equivalent unity-feedback structure:

- G/(1 + GH) = Ge/(1 + Ge) ⇒ Ge = G/[1 + G(H − 1)]
- Ge(s) = [2/(s² + 3s)]/{1 + [2/(s² + 3s)](5s + 2 − 1)} = 2/(s² + 13s + 2)
- No pole at the origin ⇒ type 0
- Kp = Ge(0) = 1, Kv = lim sGe(s) = 0, Ka = lim s²Ge(s) = 0

Steady-state error for r(t) = 1, t, t² (W(s) is the transfer function between the error and the input, W = 1/(1 + Ge) = (s² + 13s + 2)/(s² + 13s + 4)):

- Unit step: ess = lim s·(1/s)·W(s) = 1/2 = 1/(1 + Kp)
- Unit ramp: ess = ∞
- Parabolic (R = 2/s³): ess = ∞

As expected, since the equivalent system is type 0, ess is finite only for r(t) = 1.

At the top of the next page the sensitivity relation is also noted: |ΔT(s)/T(s)| = |S_K^T(s)|·|ΔK/K|, s = jω.

## Chapter 5: Stability (Routh table)

### Example 3a: Zero in the first column

- Δ(s) = s⁵ + 2s⁴ + 2s³ + 4s² + 11s + 10 = 0
- Routh: s⁵: 1, 2, 11; s⁴: 2, 4, 10; s³: ε, 6, 0; s²: c₁, 10; s¹: d₁; s⁰: 10
- c₁ = (4ε − 12)/ε ≅ −12/ε (as ε → 0₊, 4ε goes to zero), d₁ = (6c₁ − 10ε)/c₁ ≅ 6
- Two sign changes in the first column ⇒ two roots in the right half-plane (RHP)

### Example 3b: Entire row of zeros

- Δ(s) = s⁵ + 2s⁴ + 24s³ + 48s² − 25s − 50 = 0
- s⁵: 1, 24, −25; s⁴: 2, 48, −50; s³: 0, 0 (entire row of zeros)
- Auxiliary equation from the row above: A(s) = 2s⁴ + 48s² − 50, dA(s)/ds = 8s³ + 96s ⇒ s³ row: 8, 96
- Continuing: s²: 24, −50; s¹: 112.7, 0; s⁰: −50
- One sign change ⇒ one root in the RHP. Factored form: Δ(s) = (s + 1)(s − 1)(s + j5)(s − j5)(s + 2)

Side note: Stable polynomials are called Hurwitz polynomials; when an entire row of zeros occurs, the auxiliary equation is written down and the table is rebuilt using its derivative.

### Example 4: Range of K for stability

Unity-feedback system, G(s) = K/[s(s + 2)(s² + s + 1)]:

- CLTF: C(s)/R(s) = K/[s(s + 2)(s² + s + 1) + K]
- CLCE: Δ(s) = s⁴ + 3s³ + 3s² + 2s + K = 0
- Routh: s⁴: 1, 3, K; s³: 3, 2; s²: 7/3, K; s¹: 2 − 9K/7; s⁰: K
- For closed-loop stability, 0 < K < 14/9; the critical gain is Kc = 14/9
- Auxiliary equation (7/3)s² + 14/9 = 0 ⇒ s² + 2/3 = 0 ⇒ s₁,₂ = ±j√(2/3) = ±j0.82 ⇒ ωp = 0.82 rad/s

### Example 5: Axis shifting

- Δ(s) = s⁴ + 6s³ + 12s² + 11s + 6 = (s + 2)(s + 3)(s² + s + 1)
- Routh: s⁴: 1, 12, 6; s³: 6, 11; s²: 61/6, 6; s¹: 455/61; s⁰: 6 ⇒ all roots are in the left half-plane (LHP)
- Side note: For second-order polynomials, coefficients of the same sign are a necessary and sufficient condition for stability.

To find out whether there are roots to the right of the line s = −1, p − 1 is substituted for s (the jω axis is shifted to −1, and the new axis is called jν):

- Δ(p) = (p − 1)⁴ + 6(p − 1)³ + 12(p − 1)² + 11(p − 1) + 6 = p⁴ + 2p³ + p + 2
- Routh: p⁴: 1, 0, 2; p³: 2, 1; p²: −1/2, 2; p¹: 9; p⁰: 2
- Two sign changes ⇒ there are two roots to the right of the line s = −1 (−1/2 ± j√3/2). The roots that were at −3 and −2 before the shift are at −2 and −1 after the shift.

## Root locus

### Example 6(a)

- CLCE: Δ(s) = s³ + 7s² + 16s + K + 10 = 0 ⇒ 1 + K/(s³ + 7s² + 16s + 10) = 0
- Equivalent OLTF: K/[(s + 1)(s² + 6s + 10)] = K/[(s + 1)(s + 3 ± j)]
- Open-loop poles: −1, −3 ± j (n = 3), no zeros (m = 0)
- Asymptotes: θk = (2k + 1)π/(n − m) = 60°, 180°, 300°; σa = (−1 − 3 − 3)/3 = −2.33
- jω-axis crossing, Routh: s³: 1, 16; s²: 7, K + 10; s¹: [112 − (K + 10)]/7; s⁰: K + 10 ⇒ Km = 102. Auxiliary equation 7s² + 112 = 0 ⇒ s² + 16 = 0 ⇒ s₁,₂ = ±j4
- Breakaway point: K = −s³ − 7s² − 16s − 10 ⇒ dK/ds = −(3s² + 14s + 16) = 0 ⇒ s₁,₂ = −2, −2.67
- Departure angle (from the pole at −3 + j): θd = 180° − Σθpj + Σθzi = 180° − 90° − 153° = −63°

In the sketch, the two branches leaving the complex poles depart at −63° and come down to the real axis at −2.67 (K ≈ 1.85); one goes to −∞, and the other proceeds to the right and meets the branch coming from −1 at −2 (K = 2). These two branches leave −2 again and cross the imaginary axis at ±j4 for K = 102.

### Example 6(b): K for ζ = 0.7

ζ = 0.7 ⇒ ζ = cos θ, θ = 45°. The closed-loop poles are of the form {−b, −a ± ja}:

- Δ(s) = (s + b)(s² + 2as + 2a²) = s³ + (2a + b)s² + (2a² + 2ab)s + 2a²b = s³ + 7s² + 16s + (K + 10)
- 2a + b = 7, 2a² + 2ab = 16, 2a²b = K + 10 ⇒ b = 7 − 2a, a² − 7a + 8 = 0 ⇒ a = 1.4384 (or 5.5616)
- b = 4.1232, K = 7.06; the closed-loop poles are −4.12 and −1.44 ± j1.44

Once the poles are known, K can also be found with the magnitude condition: 1 + KGH(s) = 0 ⇒ |GH(s)| = 1/|K|, that is,

- K = |(s + 1)(s + 3 + j)(s + 3 − j)| (s = −1.44 + j1.44) = |(−0.44 + j1.44)(1.56 + j2.44)(1.56 + j0.44)| = 1.506 × 2.896 × 1.621 = 7.07

### Example 7: Root loci varying with a parameter

- (i) KG(s) = K/[(s − a)(s² − 2bs + b² + c²)] = K/[(s − a)(s − b + jc)(s − b − jc)]: when a = b + √3c, the three branches meet at a single point (for example, a = −0.54 for b = −4, c = 1); the shape of the locus is sketched for the cases a < b + √3c, a > b + √3c and a = 0.
- (ii) KG(s) = K(s + 1)/[s²(s + a)]: the root loci for a = 3, 7, 9 and 11 are compared; in the sketches for a = 9 and a = 11, the branches form a circle around the zero at −1.
- (iii) KG(s) = K(s + a)/[s(s + 1)(s² + 4s + 8)]: the special case where the branches join, around a = 1.296, is sketched.

### Example 8: Root finding with the Horner array and Newton's method

For p(s) = s³ + 7s² + 15s + 10 with initial guess s₁ = −1:

- Horner (−1): 1, 6, 9, r₁ = 1; second pass: 1, 5, r₂ = 4
- s₂ = s₁ − r₁/r₂ = −1 − 1/4 = −1.25
- Horner (−1.25): 1, 5.75, 7.813, r₃ = 0.234; second pass: 1, 4.5, r₄ = 2.188
- s₃ = s₂ − r₃/r₄ = −1.25 − 0.234/2.188 = −1.357
- The real roots of p(s): −1.382, −2, −3.618

### Example 9: Finding integer roots

For Δ(s) = s⁵ + 2s⁴ + 24s³ + 48s² − 25s − 50 = 0 from Example 3b, the integer real roots must be among the divisors of 50. Using the Horner array:

- s = 1: 1, 3, 27, 75, 50, remainder 0
- s = −1: 1, 2, 25, 50, remainder 0 ⇒ what remains is s³ + 2s² + 25s + 50
- From the auxiliary equation, (s² + 25) is known to be a factor as well: (s³ + 2s² + 25s + 50)/(s² + 25) = s + 2 (or with −2 by Horner: 1, 0, 25, remainder 0)
- Δ(s) = (s + 1)(s − 1)(s² + 25)(s + 2) = 0

*Note: In the notebook, Example 9 begins with "From Exa. 4"; the polynomial is that of Example 3b.*
