---
baslik: EEM322 Control Systems: Past Midterms and Solutions 1993–2000 (Hacettepe University, ELE 354)
ozet: Midterm questions and solutions for Hacettepe University's ELE 354 Control Systems course from 1993, 1999 and 2000: electrical analogues of mechanical and fluid systems, Mason's gain formula, state-space models, cascade decomposition, controllability/observability, the state transition matrix and second-order system design.
---

This post collects the **past midterms and their solutions** that circulated among students while preparing for EEM322 Control Systems. The exams belong to the **ELE 354 Control Theory I / Control Systems** course of the **Hacettepe University Department of Electrical and Electronics Engineering**: three midterms dated 13.05.1993, 24.03.1999 and 13.04.2000. The 1993 and 1999 exams are signed "A. Uraz" at the bottom; the solution pages of the 2000 exam end with "Y. Özkazanç". The handwritten solution of each exam was also among the files; below, they have been transcribed into text together with the questions, and the calculations were checked one by one.

Since the pages were photographs of paper photocopies, the images were not published; the content was transcribed into text from the photographed pages. For questions with figures (mechanical system, circuit, signal flow graph), a description of the figure is given. The questions were left in English as in the source; the explanations and notes are in English.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## 1993 midterm (13.05.1993)

**ELE 354 Control Theory I – Midterm (2 hours).** Each question is worth 10 points, 80 points in total.

### 1. Mechanical system and its electrical analogue

> Write the force equations for the given mechanical system. Find the transfer function between the input f and output x for the considered mechanical system. Obtain the analogous electrical system for velocity-voltage analogy and write the electrical equations.

*Figure:* A spring K attached to the wall, followed by a damper B₂ (displacement of the intermediate point y), then a mass M sliding on the ground with friction B₁; a force f is applied to the mass, whose displacement is x.

**Solution.** Force equations:

- f = M d²x/dt² + B₁ dx/dt + B₂ d(x − y)/dt
- B₂ d(x − y)/dt = K y

In the velocity-voltage (v-v) analogy, the result is a circuit in which C and R₁ are in parallel with a current source i, followed by an inductor L connected through R₂ (C ≡ M, R₁ ≡ 1/B₁, R₂ ≡ 1/B₂, L ≡ 1/K):

- i = C dv_x/dt + v_x/R₁ + (v_x − v_y)/R₂
- (v_x − v_y)/R₂ = (1/L)∫v_y dt

Transfer function:

X(s)/F(s) = (B₂s + K) / (s[(Ms + B₁)(B₂s + K) + B₂K])

### 2. Mason's gain formula

> Obtain the overall gain between the input R(s) and the output C(s) for the given signal flow graph using the Mason's gain formula.

*Graph:* Branches G₁, G₂, G₃ on the main path from R(s) to C(s); branches G₄ in parallel with them and G₅ further outside; a −H₂ feedback branch around G₂ and a −H₁ feedback branch around the chain G₁G₂G₃.

**Solution.**

- Forward paths: P₁ = G₁G₂G₃, P₂ = G₄, P₃ = G₅
- Loops: L₁ = −G₁G₂G₃H₁, L₂ = −G₂H₂, L₃ = −G₄H₁
- Determinant: Δ = 1 − (L₁ + L₂ + L₃) + L₂L₃
- Cofactors: Δ₁ = 1, Δ₂ = 1 − L₂, Δ₃ = Δ

C(s)/R(s) = (P₁Δ₁ + P₂Δ₂ + P₃Δ₃)/Δ = [G₁G₂G₃ + G₄(1 + G₂H₂)] / (1 + G₁G₂G₃H₁ + G₂H₂ + G₄H₁ + G₂H₂G₄H₁) + G₅

### 3. Two-tank fluid system

> Write the mathematical equations for the given two tank fluid system and obtain the transfer function between the output flow rate Q₂ and input flow rate Q. Draw an analogous electrical system.

*Figure:* The upper tank of cross-section A₁, fed with flow rate Q, discharges through resistance R₁ with flow Q₁ into the lower tank of cross-section A₂; the lower tank discharges through resistance R₂ with flow Q₂ (H_i = height, ρ = 1).

**Solution.** With the definitions P_i = ρH_i and C_i = A_i/ρ:

- Q − Q₁ = C₁ dP₁/dt, P₁/R₁ = Q₁
- Q₁ − Q₂ = C₂ dP₂/dt, P₂/R₂ = Q₂

Q₂(s)/Q(s) = 1 / ((1 + R₁C₁s)(1 + R₂C₂s))

Since the tanks do not load each other, the block diagram is two first-order blocks in cascade: Q → 1/(1 + R₁C₁s) → Q₁ → 1/(1 + R₂C₂s) → Q₂. Electrical analogue: a current source i feeds a C₁ ∥ R₁ circuit; the current i₁ through R₁ becomes the source for a second C₂ ∥ R₂ circuit.

### 4. State-space model for a circuit

> By defining suitable state variables obtain a SSD for the given circuit. You may take the voltage drop across C as the output.

*Circuit:* A current source i with R₁ in parallel (node voltage v₁); an inductor L (current i₁) goes from node v₁ to node v₂; at node v₂ there is a capacitor C to ground, and also a voltage source v through R₂.

**Solution.** Dynamic equations: i = v₁/R₁ + (1/L)∫(v₁ − v₂)dt and (1/L)∫(v₁ − v₂)dt = C dv₂/dt + (v₂ − v)/R₂. Choosing the state variables x₁ = i₁ (inductor current), x₂ = v₂ (capacitor voltage), we get v₁ = R₁i − R₁x₁ and:

- ẋ₁ = (1/L)(v₁ − v₂) = (1/L)(R₁i − R₁x₁ − x₂)
- ẋ₂ = (1/C)x₁ − x₂/(R₂C) + v/(R₂C)

ẋ = [−R₁/L −1/L; 1/C −1/(R₂C)] x + [R₁/L 0; 0 1/(R₂C)] [i; v], y = [0 1] x

### 5. Cascade decomposition

> Consider a system described by the transfer function G(s) = 3(s + 5)/(s(s + 1)(s + 2)). Obtain a SSD for G(s) using the cascade decomposition scheme.

**Solution.** G(s) is factored as G(s) = 3 · (1/s) · (1/(s + 1)) · ((s + 5)/(s + 2)), and the factors are connected in cascade:

- ẋ₃ = 3u
- ẋ₂ = x₃ − x₂
- ẋ₁ = x₂ − 2x₁, y = ẋ₁ + 5x₁ = 3x₁ + x₂

ẋ = [−2 1 0; 0 −1 1; 0 0 0] x + [0; 0; 3] u, y = [3 1 0] x

### 6. Zero-input, zero-state and total response

> The dynamic equations of a linear time-invariant system is given as ẋ = [1 2; −3 −4] x + [2; −3] u, y = [1 0] x. Obtain the zero-input response for x(0) = [1 −1]ᵀ, the zero-state response for a unit-step input and the total output response y(t).

**Solution.** Resolvent matrix: (sI − A)⁻¹ = (1/Δ(s)) [s+4 2; −3 s−1], Δ(s) = (s + 1)(s + 2). In the Laplace domain, X(s) = (sI − A)⁻¹x(0) + (sI − A)⁻¹BU(s).

- Zero-input response: X(s) = (1/Δ)[s + 2; −(s + 2)] → **x(t) = [e⁻ᵗ; −e⁻ᵗ]**
- Zero-state response (U = 1/s): X(s) = (1/(s(s + 2)))[2; −3] → **x(t) = [1 − e⁻²ᵗ; −3/2 + (3/2)e⁻²ᵗ]**
- Total output: **y(t) = 1 + e⁻ᵗ − e⁻²ᵗ**

### 7–8. Second-order system and error constants

> **7.** Consider a unity feedback system with the feedforward transfer function G(s) = 25/(s(s + 5)). Determine the undamped natural frequency, damping ratio, rise time, percent overshoot (PO), peak time and settling time for 2% t.b. for the unit step cl response.
>
> **8.** For the feedback system given in Q7, find the error constants and the steady-state error e_ss for unit step, unit ramp and parabolic inputs. What is the system type?

**Solution 7.** T(s) = 25/(s² + 5s + 25) → ωₙ = 5 rad/s, ζ = 0.5.

- Rise time: T_r = (π − θ)/(ωₙ√(1 − ζ²)) = **0.48 s** (θ = cos⁻¹ζ = π/3)
- Peak time: T_p = π/(ωₙ√(1 − ζ²)) = **0.73 s**
- Settling time (2%): T_s ≈ 4/(ζωₙ) = **1.6 s**
- Percent overshoot: PO = 100·e^(−π/√3) = **16.3%**

**Solution 8.** K_p = G(0) = ∞, K_v = lim s·G(s) = 5, K_a = lim s²·G(s) = 0. For a unit step e_ss = 0, for a unit ramp e_ss = 1/K_v = **0.2**, for a parabolic input e_ss = ∞. The system is **type 1**.

## 1999 midterm (24.03.1999)

**ELE 354 Control Systems – Midterm-I (2.5 hours).** Each question is worth 10 points.

### 1. Two-mass mechanical system

> Write the force equations for the given mechanical system. Obtain the analogous electrical systems for velocity-voltage (v-v) and force-voltage (f-v) analogies.

*Figure:* A mass M₁ (x) pulled by a force f is connected to the wall through a damper B₂; M₁ is connected to a mass M₂ (y) through a damper B₁, and M₂ is connected to the wall by a spring K.

**Solution.** Dynamic equations written in terms of velocities (v_x, v_y):

- f = M₁ dv_x/dt + B₂v_x + B₁(v_x − v_y)
- B₁(v_x − v_y) = M₂ dv_y/dt + K∫v_y dt

In the velocity-voltage (v-v) analogy: C ≡ M, R ≡ 1/B, L ≡ 1/K; current source i ≡ f, node voltages v_x and v_y. In the force-voltage (f-v) analogy: L ≡ M, R ≡ B, C ≡ 1/K; voltage source v ≡ f, two loop currents i_x and i_y.

### 2. Lever system

> Consider the lever system with the applied force f and the displacement x zero at the reference position as shown. Write the mathematical relations that describe the dynamics of the system and obtain the transfer function between the input f and output x. Draw v-v and f-v electrical analogue circuits.

*Figure:* A lever with arms a and b; the force f is applied at end a; end b is connected to fixed points by a spring K from above and a damper B from below (displacement x).

**Solution.** Moment balance about the fulcrum: f·a = f₁·b (f₁: the force transmitted to end b) and f₁ = Kx + B dx/dt. Hence:

X(s)/F(s) = (a/b)/(Bs + K)

Block diagram: F(s) → a/b → F₁(s) → 1/(Bs + K) → X(s). In the electrical analogues the lever is represented by an ideal transformer whose turns ratio comes from the arm ratio.

### 3. Three-tank fluid system

> Write only the mathematical equations for the given three tank fluid system and draw an analogous electrical system.

*Figure:* Three tanks side by side; the flow rate Q_i enters the middle (2nd) tank; the 1st tank is connected to the 2nd tank through R₁ and the 3rd tank through R₂; the 3rd tank discharges through R₃ with Q₀.

**Solution.**

- Q_i = (P₂ − P₁)/R₁ + (P₂ − P₃)/R₂ + C₂ dP₂/dt
- (P₂ − P₁)/R₁ = C₁ dP₁/dt
- (P₂ − P₃)/R₂ = C₃ dP₃/dt + P₃/R₃
- Q₀ = P₃/R₃

Electrical analogue: the current source feeds the v₂ node; at this node there is C₂, and C₁ is reached through R₁; through R₂ one moves to the v₃ node, where C₃ and R₃ are connected to ground.

### 4. Mason's gain formula

> Obtain the overall gain between the input R(s) and the output C(s) for the given signal flow graph using the Mason's gain formula.

*Graph:* Three nested paths: the forward branch G₁ innermost, G₂ surrounding it and G₃ outermost; with corresponding −H₁, −H₂, −H₃ feedback branches.

**Solution.**

- Forward paths: P₁ = G₁, P₂ = G₂, P₃ = G₃
- Loops: L₁ = −G₁H₁, L₂ = −G₂H₂, L₃ = −G₃H₃, L₄ = −G₁H₂, L₅ = −G₁H₃, L₆ = −G₂H₃
- Non-touching loops: (L₁, L₂), (L₁, L₃), (L₂, L₃), (L₁, L₆), (L₃, L₄) and (L₁, L₂, L₃)
- Δ = 1 − (L₁ + … + L₆) + L₁L₂ + L₁L₃ + L₂L₃ + L₁L₆ + L₃L₄ − L₁L₂L₃
- Cofactors: Δ₁ = 1, Δ₂ = 1 − L₁, Δ₃ = 1 − L₁ − L₂ − L₄ + L₁L₂

C(s)/R(s) = (P₁Δ₁ + P₂Δ₂ + P₃Δ₃)/Δ

Numerator: G₁ + G₂ + G₂G₁H₁ + G₃ + G₃G₁H₁ + G₃G₂H₂ + G₃G₁H₂ + G₃G₁H₁G₂H₂

Denominator: 1 + G₁H₁ + G₂H₂ + G₃H₃ + G₁H₂ + G₁H₃ + G₂H₃ + G₁H₁G₂H₂ + G₁H₁G₃H₃ + G₂H₂G₃H₃ + G₁H₁G₂H₃ + G₃H₃G₁H₂ + G₁H₁G₂H₂G₃H₃

### 5. Controllability and observability

> The dynamic equations of a linear time-invariant system is given as ẋ = [−4 3; −2 1] x + [1; 0] u, y = [1 −1] x. Determine whether the system is controllable and/or observable? Obtain the transfer function and comment on your findings in relation to c/o.

**Solution.**

- U = [B AB] = [1 −4; 0 −2], |U| ≠ 0 → (A, B) is **controllable**
- V = [C; CA] = [1 −1; −2 2], |V| = 0 → (A, C) is **unobservable**
- G(s) = C(sI − A)⁻¹B = [1 −1] · (1/((s + 1)(s + 2))) · [s−1 3; −2 s+4] · [1; 0] = (s + 1)/((s + 1)(s + 2)) = **1/(s + 2)**

Since the system is unobservable, a pole-zero cancellation occurs in the transfer function, as expected.

### 6. Companion form and transition matrix

> If possible transform the dynamic equations given in Q.5 into the companion canonical form. Obtain the state transition matrix for the transformed matrix A.

**Solution.** Since (A, B) is controllable, the transformation is possible.

- U⁻¹ = (1/−2)[−2 4; 0 1] = [1 −2; 0 −1/2], q = [0 1]U⁻¹ = [0 −1/2]
- Q = [q; qA] = [0 −1/2; 1 −1/2], Q⁻¹ = [−1 1; −2 0]
- With w = Qx, ẇ = QAQ⁻¹w + QBu = [0 1; −2 −3] w + [0; 1] u, y = CQ⁻¹w = [1 1] w

Transition matrix:

e^(A_c t) = L⁻¹[(sI − A_c)⁻¹] = L⁻¹{(1/((s + 1)(s + 2))) [s+3 1; −2 s]} = [2e⁻ᵗ − e⁻²ᵗ, e⁻ᵗ − e⁻²ᵗ; −2e⁻ᵗ + 2e⁻²ᵗ, −e⁻ᵗ + 2e⁻²ᵗ]

### 7. Cascade decomposition

> Consider a system described by the transfer function G(s) = (2s + 6)/(s³ + 6s² + 8s). Obtain a SSD for G(s) using the cascade decomposition scheme.

**Solution.** G(s) = 2(s + 3)/(s(s + 2)(s + 4)) = (2/s) · (1/(s + 2)) · ((s + 3)/(s + 4)):

- ẋ₃ = 2u, ẋ₂ = x₃ − 2x₂, ẋ₁ = x₂ − 4x₁
- y = ẋ₁ + 3x₁ = −x₁ + x₂

ẋ = [−4 1 0; 0 −2 1; 0 0 0] x + [0; 0; 2] u, y = [−1 1 0] x

### 8. Design of feedback parameters

> Consider a closed loop system with a feedforward transfer function G(s) = 10/s² and a feedback transfer function H(s) = (as + b). For a unit step input, find the values of a and b that give 16% percent overshoot (PO) and 0.4 sec. settling time (2% t.b.).

**Solution.** T(s) = G/(1 + GH) = 10/(s² + 10as + 10b).

- T_s = 4/(ζωₙ) = 0.4 s → ζωₙ = 10 → 2ζωₙ = 10a = 20 → **a = 2**
- PO = 16%: ln 0.16 = −ζπ/√(1 − ζ²) = −1.83 → ζ²/(1 − ζ²) = (0.583)² = 0.34 → ζ ≈ 0.5 → ωₙ = 20 rad/s
- ωₙ² = 10b = 400 → **b = 40**

## 2000 midterm (13.04.2000)

**Hacettepe University, ELE 354 Control Systems – 1. Midterm Exam, April 13, 2000.**

### 1. Differential equations of a mechanical system

> Obtain the differential equations describing the following system. Draw an analogous electrical circuit based on force-current analogy.

*Figure:* A mass m₁ (x₁, to the right) connected to the left wall by a spring K₁, connected by a spring K₂ to a mass m₂ (x₂, to the left); m₂ is connected to the right wall by a damper b; a force F is applied to m₁.

**Solution.**

- m₁ẍ₁ = −F − K₁x₁ − K₂(x₂ + x₁)
- −m₂ẍ₂ = K₂(x₁ + x₂) + bẋ₂

In the force-current analogy, i = F is a current source; L₁ = 1/K₁, C₁ = m₁ (voltage v₁ = ẋ₁), L₂ = 1/K₂, C₂ = m₂ and R = 1/b (voltage v₂ = −ẋ₂).

### 2. Water level control

> The water level, h(t), is controlled by an open loop control system. A dc motor controlled by armature current i turns a shaft, opening a valve. The inductance of the dc motor is neglected. The height of the water in the tank is given by h(t) = ∫(1.6θ(t) − h(t))dt. The motor constant is K_m = 10, and the inertia of the motor shaft and valve is J = 6 × 10⁻³ kg·m². Determine the transfer function from the motor voltage, v(t), to the water level, h(t).

*Figure:* v(t) enters an amplifier with gain K_a = 50; the amplifier drives the motor with current i through 10 Ω; the motor shaft opens the valve by θ(t) (valve opening = shaft position) and the level h(t) of the tank changes.

**Solution.**

- h(t) = ∫(1.6θ − h)dt → H(s) = 1.6Θ(s)/(s + 1)
- ω = θ̇ → Ω(s) = sΘ(s), so H(s) = 1.6Ω(s)/(s(s + 1))
- J dω/dt = K_m i → 6 × 10⁻³ sΩ(s) = 10 I(s)
- 50v = Ri + Kω = 10i + 10ω → 50V(s) = (6 × 10⁻³ s + 10)Ω(s)

H(s)/V(s) = 80 / (s(s + 1)(6 × 10⁻³ s + 10))

### 3. Mason's gain formula

> Determine the transfer function from R to C by using Mason's Gain Formula.

*Graph:* R → 1 → K → G₁ → G₂ → G₃ → 1 → C; with −H₂ branches around G₂, −H₃ around G₁G₂, −H₄ around G₂G₃, −H₁ around G₁G₂G₃, and a −1 branch from the output to the input of K.

**Solution.** L₁ = −G₂H₂, L₂ = −H₁G₁G₂G₃, L₃ = −KG₁G₂G₃, L₄ = −G₁G₂H₃, L₅ = −H₄G₂G₃; a single forward path P₁ = KG₁G₂G₃. All loops touch one another, Δ₁ = 1:

T = KG₁G₂G₃ / (1 + G₂H₂ + H₁G₁G₂G₃ + KG₁G₂G₃ + G₁G₂H₃ + H₄G₂G₃)

### 4. Bridged-T filter

> Determine the transfer function for the following filter.

*Circuit:* Two series C capacitors between input and output, R₁ from the node between them to ground; R₂ bridging across the two capacitors.

**Solution.** Using the loop-current method:

H(s) = (1 + 2R₁Cs + R₁R₂C²s²) / (1 + (2R₁ + R₂)Cs + R₁R₂C²s²)

### 5. v and i as state variables

> Develop a state space model for the following system by taking v and i as your state variables. Determine the eigenvalues and eigenvectors of your model.

*Circuit:* A 1 F capacitor (v_C1) is connected through a 1 Ω resistor (voltage v) to the node where a 0.5 Ω resistor (current i) and a 2 F capacitor (v_C2) are connected in parallel.

**Solution.** First in terms of the capacitor voltages: C₁ dv_C1/dt = (v_C2 − v_C1)/1 and C₂ dv_C2/dt = (v_C1 − v_C2)/1 − v_C2/0.5:

ẋ = [−1 1; 0.5 −1.5] x

Since v = v_C1 − v_C2 and i = 2v_C2, z = [v; i] = Mx, M = [1 −1; 0 2]; ż = MAM⁻¹z:

d/dt [v; i] = [−1.5 0.5; 1 −1] [v; i]

- Eigenvalues: det(sI − MAM⁻¹) = s² + 2.5s + 1 = 0 → **s₁ = −0.5, s₂ = −2**
- Eigenvectors: **z₁ = [−1; −2]**, **z₂ = [−1; 1]**

### 6. Transition matrix and impulse response

> Determine the state transition matrix of the following system. If the input, r(t), is a unit impulse and x₁(0) = 1, x₂(0) = 1; determine x₁(t) for t > 0. ẋ = [−2 −1; 2 −5] x + [0; 1] r(t).

**Solution.**

e^(At) = L⁻¹[(sI − A)⁻¹] = [2e⁻³ᵗ − e⁻⁴ᵗ, e⁻⁴ᵗ − e⁻³ᵗ; 2e⁻³ᵗ − 2e⁻⁴ᵗ, 2e⁻⁴ᵗ − e⁻³ᵗ]

x(t) = e^(At)x₀ + ∫₀ᵗ e^(A(t−τ))Br(τ)dτ, x₀ = [1; 1], r(t) = δ(t). In the source the result is given as x₁(t) = 2e⁻³ᵗ − e⁻⁴ᵗ.

*Note: This result is wrong; it is only the (1,1) element of the transition matrix. With an impulse input, X(s) = (sI − A)⁻¹(x₀ + B) = (sI − A)⁻¹[1; 2], and X₁(s) = ((s + 5) − 2)/((s + 3)(s + 4)) = 1/(s + 4). The correct answer is **x₁(t) = e⁻⁴ᵗ**: the zero-input part gives e⁻³ᵗ, and the impulse response gives e⁻⁴ᵗ − e⁻³ᵗ.*

### 7. Companion form from a block diagram

> Develop a state space model for the following system. Put your state space model in companion form.

*Block diagram:* u → summing junction (−y) → s → summing junction (inner feedback) → 1/(2s + 20) → 1/(s + 5) → 1/s → y; the inner loop is fed back from the output of 1/(s + 5).

**Solution.** The inner loop becomes 1/((2s + 20)(s + 5) + 1) = 1/(2s² + 30s + 101); s and 1/s cancel each other:

H(s) = Y(s)/U(s) = 0.5/(s² + 15s + 51)

Companion form: ẋ = [0 1; −51 −15] x + [0; 1] u, y = [0.5 0] x

### 8. Uncontrollable circuit

> Develop a state space model for the following circuit. Determine the capacitance, C, such that your model is not controllable.

*Circuit:* Two branches in parallel with the voltage source v(t): 2 Ω in series with 0.5 F (v_C1), and C in series with 8 Ω (v_C2).

**Solution.**

- 0.5 dv_C1/dt = (v − v_C1)/2 → v̇_C1 = −v_C1 + v
- C dv_C2/dt = (v − v_C2)/8 → v̇_C2 = −v_C2/(8C) + v/(8C)

A = [−1 0; 0 −1/(8C)], B = [1; 1/(8C)]. Controllability matrix [B AB] = [1 −1; 1/(8C) −1/(64C²)]; the matrix is singular when its determinant −1/(64C²) + 1/(8C) is zero:

**C = 1/8 F** → the model is uncontrollable. (At this value the time constants of the two branches are equal: 2 Ω × 0.5 F = 8 Ω × 1/8 F = 1 s.)
