---
baslik: EEM322 Control Systems: Past Final Exams 1992–2002 (Hacettepe University, ELE 354)
ozet: Final exam questions from the Hacettepe University ELE 354 Control Theory / Control Systems course for 1992, 1994, 2001 and 2002, and the solution to the 1992 final: a position servo with a field-controlled DC motor, state space and companion form, second-order system response, root locus, Routh, Bode, Nyquist and Mason's gain formula.
---

This post collects the **past final exams** that circulated among students while studying for EEM322 Control Systems. The exams do not belong to Başkent University; they are from the **ELE 354 Control Theory I / Control Systems** course of the **Department of Electrical and Electronics Engineering at Hacettepe University**: four finals dated 22.06.1992, June 1994, 31.05.2001 and 04.06.2002. The 1992 and 1994 exams are signed "A. Uraz" at the bottom. A handwritten solution to the 1992 final was also among the files; it has been transcribed below together with the questions, and the calculations were checked one by one.

Because the pages were photographs of paper photocopies, the images have not been published; the content was transcribed to text from the photographed pages. For questions with figures (circuits, block diagrams, signal flow graphs), a description of the figure is given. The questions were left in English as in the source; the explanations and notes are in Turkish.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## 1992 final (22.06.1992)

**ELE 354 Control Theory I – Final (2 hours).** Each question is worth 25 points.

### Questions

**1.** Consider the positional servo with a field-controlled dc motor as shown in Fig. Q1. The angular position of the output shaft is compared with a reference input angular position using two rotary potentiometers.

*Figure:* The difference e between the input potentiometer (r) and the output potentiometer (c) goes to the input of an amplifier with gain K_p. The amplifier drives the field winding (R_f, L_f, current i_f); the armature current I_a is constant. A gearbox with ratio n = N₁/N₂, connected to the motor shaft (θ), rotates a load with inertia J_L and friction B_L; the load shaft is connected to the output potentiometer.

- (a) Obtain the transfer function between the applied voltage e_f and the displacement θ on the motor shaft of a field-controlled dc motor which drives a load with a moment of inertia J_L and a viscous friction coefficient B_L through a gear ratio of n = N₁/N₂.
- (b) Determine the mathematical relations for each component and draw a detailed block diagram showing every component with its transfer function and the system variables. Obtain the overall transfer function between the angular displacement c of the output shaft and angular displacement r of the input shaft.

**2.** The state equation of a linear time-invariant system is given as

ẋ = [1 2; −3 −4] x + [1; 1] u

- (a) Transform the state equation into the companion canonical form.
- (b) By assuming a zero input, obtain the transition matrix and find the initial states which yield the state vector x = 2e⁻ᵗ [1 −1]ᵀ at time t.

**3.** The forward transfer function of a unity feedback system is given as G(s) = K / (s(s + 3)).

- (a) Determine the damping ratio ζ and undamped natural frequency ωₙ in terms of K. What are the ranges of K for underdamped, critically damped and overdamped responses?
- (b) For K = 9, obtain the values of peak time T_p, settling time T_s for 2% tb and percent overshoot PO. Calculate the unit step response, draw it against time with all the points of interest indicated on the plot.
- (c) For K = 9, what are the error constants and the steady state errors to unit step, ramp and parabolic inputs?

**4.** A negative feedback system has the open loop transfer function K / (s(s + 2)(s² + 2s + 2)).

- (a) Indicating clearly all the steps involved and calculating all the necessary points and K on the branches, plot a detailed root-locus diagram for the given open loop transfer function.
- (b) It is desired that the dominant closed loop poles should have a damping ratio of ζ = 0.707 and an undamped natural frequency of ωₙ = 0.707. Find all the closed loop poles and the value of K which satisfy the desired specification.

### Solution 1: Position servo with a field-controlled DC motor

**(a)** In a field-controlled motor the torque is proportional to the field current (the armature current is constant):

- Torque: T = K₁ i_a K_f i_f = K₂ i_f (K₁, K₂, K_f, i_a constant)
- Field circuit: e_f = L_f di_f/dt + R_f i_f
- Mechanical equation: J d²θ/dt² + B dθ/dt = T = K₂ i_f; here the load is referred to the motor shaft: J = n²J_L, B = n²B_L.

Laplace transform with zero initial conditions:

- (L_f s + R_f) I_f(s) = E_f(s)
- (Js² + Bs) Θ(s) = K₂ I_f(s)

From these:

Θ(s)/E_f(s) = K₂ / (s(L_f s + R_f)(Js + B)) = K_m / (s(T_f s + 1)(T_m s + 1))

- K_m = K₂/(R_f B): motor gain constant
- T_f = L_f/R_f: time constant of the field circuit
- T_m = J/B: inertia/friction (mechanical) time constant

**(b)** Component equations:

- Error detector (potentiometer pair): E(s) = K₁[R(s) − C(s)]
- Amplifier: E_f(s) = K_p E(s)
- Gearbox: C(s) = n Θ(s)

Block diagram: R(s) → summing junction (−C(s)) → K₁ → K_p → K_m/(s(T_f s + 1)(T_m s + 1)) → n → C(s), with unity negative feedback from the output to the input. The closed-loop transfer function is:

C(s)/R(s) = K₁K_pK_m n / (T_f T_m s³ + (T_f + T_m)s² + s + K₁K_pK_m n)

### Solution 2: Companion form and transition matrix

**(a)** First the controllability matrix is formed: S = [B AB] = [1 3; 1 −7], |S| = −10 ≠ 0, so the state equation can be transformed into companion form.

- S⁻¹ = (1/10)[7 3; 1 −1], its last row is q = [1/10 −1/10]
- Q = [q; qA] = (1/10)[1 −1; 4 6], Q⁻¹ = [6 1; −4 1]
- With the transformation w = Qx, ẇ = QAQ⁻¹w + QBu = A₁w + B₁u:

ẇ = [0 1; −2 −3] w + [0; 1] u

The general form of the method is also noted at the bottom of the page: S = [B AB A²B …], q = [0 0 … 1]S⁻¹, Q = [q; qA; …; qAⁿ⁻¹], w = Qx.

**(b)** Resolvent matrix:

(sI − A)⁻¹ = [s−1 −2; 3 s+4]⁻¹ = 1/((s+1)(s+2)) · [s+4 2; −3 s−1]

The transition matrix by inverse Laplace transform:

Φ(t) = [3e⁻ᵗ − 2e⁻²ᵗ, 2e⁻ᵗ − 2e⁻²ᵗ; −3e⁻ᵗ + 3e⁻²ᵗ, −2e⁻ᵗ + 3e⁻²ᵗ]

With zero input x(t) = Φ(t)x(0), so x(0) = Φ⁻¹(t)x(t) = Φ(−t)x(t). Substituting x(t) = 2e⁻ᵗ[1 −1]ᵀ:

**x(0) = [2 −2]ᵀ**

Check: [1 −1]ᵀ is the eigenvector of A for the eigenvalue λ = −1; therefore the solution starting from x(0) = [2 −2]ᵀ is exactly 2e⁻ᵗ[1 −1]ᵀ. In the solution the same result was also obtained via the transition matrix in companion form, Φ_w(t) = L⁻¹[(sI − A₁)⁻¹], using x(0) = Q Φ_w(−t) Q⁻¹ x(t).

### Solution 3: Response of the second-order system

The closed-loop transfer function is C(s)/R(s) = K/(s² + 3s + K) = ωₙ²/(s² + 2ζωₙs + ωₙ²), so:

**(a)** ωₙ = √K, ζ = 3/(2√K). Characteristic equation Δ(s) = s² + 3s + K = 0.

| Response | ζ | K |
|---|---|---|
| Underdamped | 0 < ζ < 1 | K > 9/4 |
| Critically damped | ζ = 1 | K = 9/4 |
| Overdamped | ζ > 1 | 0 < K < 9/4 |

**(b)** For K = 9, ζ = 0.5, ωₙ = 3 rad/s:

- Peak time: T_p = π/(ωₙ√(1−ζ²)) = π/2.598 = **1.21 s**
- Settling time (2%): T_s ≈ 4/(ζωₙ) = 4/1.5 = **2.67 s**
- Percent overshoot: PO = 100·e^(−ζπ/√(1−ζ²)) = 100·e^(−1.814) = **16.3%**
- Unit step response: c(t) = 1 − (e^(−ζωₙt)/√(1−ζ²)) sin(ωₙ√(1−ζ²) t + tan⁻¹(√(1−ζ²)/ζ)) = **1 − 1.155 e^(−1.5t) sin(2.598t + 60°)**

In the graph in the solution, the response reaches the peak value of 1.163 at T_p = 1.21 s and enters the 2% band at T_s = 2.67 s; the delay time T_d and rise time T_r are also marked on the axis.

*Note: The sign of the phase angle is illegible in the source; for ζ = 0.5 the correct value is tan⁻¹(√3) = +60°.*

**(c)** For K = 9, G(s) = 9/(s(s + 3)) = 3/(s(0.333s + 1)); the system is **type 1**:

- K_p = G(0) = ∞, K_v = lim s·G(s) = 3, K_a = lim s²·G(s) = 0
- Unit step r(t) = 1: e_ss = 0
- Unit ramp r(t) = t: e_ss = 1/K_v = **1/3**
- Parabolic r(t) = t²: e_ss = ∞

### Solution 4: Root locus

Open loop G(s)H(s) = K/(s(s + 2)(s² + 2s + 2)); characteristic equation 1 + G(s)H(s) = 0.

**Step 1 – Poles/zeros:** poles at 0, −2, −1 ± j (n = 4); no zeros (m = 0). There are four branches, all going to infinity.

**Step 2 – Asymptotes:** n − m = 4 asymptotes; angles θ_k = (2k + 1)π/4 = 45°, 135°, 225°, 315°; centroid σ_a = (Σp − Σz)/(n − m) = (−2 − 1 + j − 1 − j)/4 = **−1**.

**Step 3 – jω-axis crossing:** Routh table for Δ(s) = s⁴ + 4s³ + 6s² + 4s + K = 0:

| Row | 1st column | 2nd column | 3rd column |
|---|---|---|---|
| s⁴ | 1 | 6 | K |
| s³ | 4 | 4 | |
| s² | 5 | K | |
| s¹ | 4(5 − K)/5 | | |
| s⁰ | K | | |

*Note: In the source the s¹ row is written as (5 − K)/5; the correct form is (5·4 − 4K)/5 = 4(5 − K)/5. The sign of the row, and therefore the stability range, does not change.*

Stability range: **0 < K < 5**. At K = 5 the auxiliary equation is 5s² + 5 = 0 → s = **±j**. Indeed for K = 5, Δ(s) = (s² + 1)(s² + 4s + 5).

**Step 4 – Breakaway point:** K = −(s⁴ + 4s³ + 6s² + 4s), dK/ds = −(4s³ + 12s² + 12s + 4) = −4(s + 1)³ = 0 → s = −1 (triple root; found with a Horner table). At this point K = −(1 − 4 + 6 − 4) = **1**. For K = 1, Δ(s) = (s + 1)⁴: all four roots meet at −1, that is, −1 is a quadruple breakaway point.

**Step 5 – Departure angles (from the poles at −1 ± j):** θ = 180° − 135° − 45° − 90° = **−90°** (+90° for the other pole).

In the resulting locus, the branches leaving the −1 ± j poles descend vertically to the real axis, the branches leaving 0 and −2 arrive at −1; at K = 1 the four branches meet at −1 and depart along the asymptotes in the directions 45°, 135°, 225° and 315°. The two branches going to the right cross the imaginary axis at ±j at K = 5.

**(b)** Desired dominant poles: ζ = 0.707, ωₙ = 0.707 → s = −ζωₙ ± jωₙ√(1−ζ²) = **−0.5 ± j0.5**.

Angle condition check (θ₁ = tan⁻¹(0.5/1.5) = 18.4°, θ₂ = tan⁻¹(1.5/0.5) = 71.6°):

−(18.4° + 71.6° + 315° + 135°) = −540° = −3 × 180°

so −0.5 ± j0.5 lies on the root locus. Synthetic division: Δ(s)/(s² + s + 0.5) = s² + 3s + 2.5, remainder K − 0.5 × 2.5 = 0. Thus **K = 1.25** and the remaining closed-loop poles are **−1.5 ± j0.5**.

Check: (s² + s + 0.5)(s² + 3s + 2.5) = s⁴ + 4s³ + 6s² + 4s + 1.25. Also, since Δ(s) = (s + 1)⁴ + (K − 1), for K > 1 the roots lie on four straight lines centered at −1; for −0.5 + j0.5, (K − 1) = |0.5 + j0.5|⁴ = 0.25, so K = 1.25 is confirmed.

## 1994 final (June 1994)

**ELE 354 Control Theory I – Final (2 hours).** The date is partly legible (something like 16/6/1994).

**1.** An armature-controlled dc motor is used to deliver a torque T to a load with a moment of inertia J and a rotational viscous friction B. The armature winding has an inductance L_a and a resistance R_a. Write down all the mathematical relations (time-domain) and obtain the transfer function between the angular displacement Θ(s) of the load and the applied input voltage E_a(s) to the armature winding. Draw a detailed block diagram.

**2.** Consider the positional servo with an armature-controlled dc motor as shown. The angular position of the output shaft is compared with a reference input angular position using two rotary potentiometers. Obtain the overall transfer function between the angular displacement c of the output shaft and angular displacement r of the input shaft, and draw the final block diagram. Note that you may use the results which you have obtained in Q.1.

*Figure:* The armature-controlled version of the servo in the 1992 final: the potentiometer difference e passes through the amplifier K_p and drives the armature circuit (R_a, L_a, i_a); the field current i_f is constant. The motor shaft θ rotates, through an n = N₁/N₂ gearbox, the load J_L, B_L and the output potentiometer.

**3.** Write only the mathematical equations for the given three tank fluid system and draw an analogous electrical system. (*Figure:* three tanks connected side by side with input Q_i; cross-sectional areas A₁, A₂, A₃, levels H₁, H₂, H₃, resistances between tanks and at the outlet R₁, R₂, R₃, output flow Q₀; H_i = height, A_i = cross-sectional area, ρ = 1 density of water.)

**4.** The dynamic equations of a linear time-invariant system is given as ẋ = [−1 2; −1 −4] x + [0; 1] u and y = [1 0] x. Obtain the zero-input response for x(0) = [1 0]ᵀ, the zero-state response for a unit-step input and the total output response y(t).

**5.** Consider a unity feedback system with an OLTF G(s) = K / (s(s³ + 6s² + 9s + 24)). Obtain the position K_p, velocity K_v and acceleration K_a error constants and indicate the type of input which would yield zero steady-state error. The steady-state error for a ramp input is desired to be less than 0.5. Investigate whether this is achievable under stable operation.

**6.** Consider a feedback control system with the feedforward and feedback transfer functions given, respectively, as G(s) = 10/(s + 3) and H(s) = hs. The nominal value of the parameter h is h = 2. Obtain the sensitivity of CLTF T(s) to parameter variations in h. Determine the percent magnitude change in CLTF T(s) for a 10% change in h at a frequency of ω = 5 rad/sec.

**7.** A unity feedback control system has a plant transfer function of the form G(s) = K(s + 1)(s + 2) / (s(s² + 1)(s + 6)). Determine the range of K for stable operation and indicate the critical value of K and jω-axis crossing.

**8.** Consider the system given in Q.7. Indicating clearly all the steps involved and calculating all the necessary points and angles, plot a detailed root-locus diagram. Note that you may use the results which you have obtained in Q.7.

## 2001 final (31.05.2001)

**ELE 354 Control Systems – Final (2.5 hours).** It consists of two parts; Part B is a separate page printed in a different typeface.

### Part A

**A-1.** Water tank level control is achieved by using a float level sensor and valve as shown. Assume that the float has a negligible mass and the valve is controlled so that a reduction in the flow rate is proportional to an increase in head; Q₁ = r − K₁x_a where the reference signal r is r = 0 for this regulating system. The variables Q₁ and H are the deviations from some nominal values. Write all the relevant mathematical equations, draw a detailed block diagram and obtain the CLTF between H and r by utilizing the block diagram.

*Figure:* Flow Q₁ enters a tank with cross-sectional area A through a valve; the tank drains through resistance R with flow Q₂. The floating float is connected to end b of a lever with arms a and b (displacement x_b); end a of the lever moves the valve by x_a. H = level, ρ = 1.

**A-2.** Draw the signal flow graph of the given block diagram and obtain the overall transfer function between C(s) and R(s) using the Mason's gain formula.

*Figure:* R(s) passes through the outer summing junction (−H₃ feedback); then come the second summing junction (−H₁ feedback) and the parallel G₃ and G₁ blocks. The sum of these two branches is combined at a summing junction; from the output of the first summing junction a G₄ feedforward path is connected to the last summing junction. After the last summing junction there is the G₂ block with the −H₂ inner feedback, and the output is C(s).

**A-3.** The dynamic equations of a linear time-invariant system is given as ẋ = [1 1; −6 −4] x + [0; 1] u, y = [1 0] x. Obtain the zero-input state, zero-state state, zero-input output, zero-state output and total output responses for x(0) = [1 0]ᵀ and a unit-step input u = 1, t ≥ 0.

**A-4.** Consider a unity feedback control system with the plant transfer function G(s) = 50000(s + 2) / (s(s + 10)(s² + 50s + 2500)). Using the straight line approximation technique, obtain the Bode plots. [Use 10 dB/cm in magnitude scale, 45°/cm in phase scale]. Indicate clearly on the plots the gain/phase crossover frequencies, the gain/phase margins and read out their approximate values.

### Part B

**B-1.** Consider the following polynomial: s⁸ + s⁷ + 12s⁶ + 22s⁵ + 39s⁴ + 59s³ + 48s² + 38s + 20. Determine how many roots of this polynomial are in the right half plane, the left half plane and on the jω axis. Determine the roots on the jω axis, if any.

**B-2.** Design the values of K₁ and K₂ in the following system, to meet the following specifications; steady state error component due to a unit step disturbance is −0.000012 and the steady state error component due to a unit ramp input is 0.003. (*Figure:* R(s) → summing junction (−C) → K₁(s + 2)/(s + 3) → summing junction where D(s) is added → K₂/(s(s + 4)) → C(s), unity feedback.)

**B-3.** Consider the following system. Draw a detailed root locus diagram. Design the value of K for "good performance". (*Figure:* unity feedback; forward path with K and (s + 1.5)/(s(s + 1)(s + 10)).)

**B-4.** Consider the following system. Draw a detailed Nyquist diagram. By using Nyquist criterion; find the range of K for stability and instability, the value of K for marginal stability and determine the frequency of oscillations. If K = 6; determine the gain margin, estimate the phase margin. (*Figure:* unity feedback; forward path with K and 1/((s² + 2s + 2)(s + 2)).)

## 2002 final (04.06.2002)

**ELE 354 Control Systems – Final (2.5 hours).**

### Part A

**A-1.** A position control system with G(s) in the forward path and a tachometer feedback H(s) given as G(s) = 4/(s(s + 2)), H(s) = (1 + hs). Determine the value of h so that the damping ratio ζ is 0.6. Obtain steady-state responses for r₁(t) = 2 and r₂(t) = 3 sin 2t inputs and show whether asymptotic tracking is achieved for r₁(t).

**A-2.** Consider a feedback control system with the feedforward and feedback transfer functions given, respectively, as G(s) = 10/(s + 3) and H(s) = hs. The nominal value of the parameter h is h = 2. Obtain the sensitivity of CLTF T(s) to parameter variations in h. Determine the percent magnitude change in CLTF T(s) for a 10% change in h at a frequency of ω = 0.1 rad/sec and find whether this frequency is within the bandwidth?

**A-3.** The characteristic equation of a unity feedback control system is given as Δ(s) = s² + (K − 2)s + 2 = 0. Find the range of K for stable operation. Indicating clearly all the steps involved and calculating all the necessary points and angles; plot a detailed root-locus diagram.

**A-4.** Consider a unity feedback control system with the plant transfer function G(s) = 9000s / ((s + 2)(s + 30)(s² + 5s + 25)). Using the straight line approximation technique, obtain the Bode plots. [Use 10 dB/cm in magnitude scale, 45°/cm in phase scale]. Indicate clearly on the plots the gain/phase crossover frequencies, the gain/phase margins and read out their approximate values.

### Part B

**1.** Consider the electro-mechanical system given below. Determine the transfer function from the armature voltage (e) to the shaft position (θ). (*Figure:* source e(t) feeds the motor through resistance R; the motor back-EMF is e_m = Kθ̇_m. The motor shaft rotates the inertia J_m and gear n₁; gear n₂ rotates the shaft carrying the load J_L by θ.)

**2.** Determine the transfer function G(s) such that the effect of the disturbance (d) is eliminated entirely. (*Figure:* r → summing junction (−y feedback and +G(s)·d) → (s + 5)/(s + 10) → 10/(s(s + 5)) → summing junction where d is added → y.)

**3.** Obtain a state-space representation for the following system. Determine observability and controllability status of your representation. (*Figure:* u → summing junction (−y) → (s + z)/(s + p) → 1/s² → y, unity feedback.)

**4.** Consider the following system. Draw the Nyquist plot associated with the open-loop transfer function. Determine gain margin and estimate phase margin of the closed loop system provided K = 0.5. (*Figure:* unity feedback; forward path with K and 100/(s(s + 2)(s + 10)).)
