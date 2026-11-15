---
baslik: EEM322 Control Systems: Lecture Notebook (February 2013) – Op-Amp Circuits, Mechanical Systems, Electrical Analogies and Block Diagrams
ozet: The first weeks of the EEM322 Control Systems spring 2013 lecture notebook: transfer functions of inverting, integrating and differentiating op-amp circuits, the dynamic equations of a two-mass mechanical system and its f-i and f-v analogies, a field-controlled motor, the loading effect in RC circuits, a system with a disturbance input, and the block diagram of a temperature control system.
---

This post contains the first weeks of a **lecture notebook** from the Başkent University **EEM322 Control Systems** course, spring 2013 (pages photographed on 17 and 25 February 2013). The notebook belongs to a friend. The pages were **transcribed to text from photographs**; the photographs were not published. The examples covered in lecture were largely written in English, with Turkish explanations interspersed. Below, the headings, main formulas and results are transcribed. The photographs of the block diagram rules table (Table 2.3, pp. 40–41) of the textbook followed in class were not transcribed because they are pages of the book; only the notebook owner's margin notes are summarized.

The lecture-note counterparts of the same topics are in the posts [Lecture 2](/arsiv/eem322-ders-02-modelleme/) and [Lecture 4](/arsiv/eem322-ders-04-blok-diyagram/). Continuation of the notebook: [state space](/arsiv/eem322-defter-durum-uzayi/) and [steady-state error, Routh and root locus](/arsiv/eem322-defter-kalici-hata-routh-kok-yer/).

## Example 1(a): Electronic systems, op-amp circuit

An op-amp circuit with Z₁ (R₁ ∥ C₁) connected to the inverting input and Z₂ (R₂ ∥ C₂) in the feedback path. Since the voltage at the inverting input of the op-amp is E′(s) ≅ 0:

- [Ei(s) − E′(s)]/Z₁(s) = [E′(s) − Eo(s)]/Z₂(s) ⇒ Eo(s)/Ei(s) = −Z₂(s)/Z₁(s)

Complex impedances:

- Z₁(s) = 1/(C₁s + 1/R₁) = R₁/(R₁C₁s + 1)
- Z₂(s) = 1/(C₂s + 1/R₂) = R₂/(R₂C₂s + 1)
- Eo(s)/Ei(s) = −(R₂/R₁)·(R₁C₁s + 1)/(R₂C₂s + 1) = −(C₁/C₂)·(s + 1/(R₁C₁))/(s + 1/(R₂C₂))

The notebook points out that the transfer function has a negative sign, i.e. the circuit is an inverting amplifier. For a positive sign, a second inverting stage (R₃ at the input, R₄ in the feedback path) can be added at the output: E′o(s)/Eo(s) = −R₄/R₃.

Special cases:

- Z₁ = R, Z₂ = 1/(Cs): integrating circuit, Eo/Ei = −1/(RCs)
- Z₁ = 1/(Cs), Z₂ = R: differentiating circuit, Eo/Ei = −RCs
- Z₂ = R₂, Z₁ = R₁/(R₁C₁s + 1): another differentiating circuit, Eo/Ei = −R₂(R₁C₁s + 1)/R₁

## Example 2(a): Two-mass mechanical system (Pr. 2.2(e))

Taken from the problems at the back of the textbook: mass M₂ is connected to the wall by spring K, and is connected to mass M₁ by damper B₂; there is a damper B₁ between M₁ and the wall, and a force f is applied to M₁. There are two displacements: x (output, M₁) and y (M₂). The mechanical circuit is set up with a force source; the masses lie between a node and the reference (the fixed support point).

Dynamic equations:

- M₁ d²x/dt² + B₁ dx/dt + B₂ d(x − y)/dt = f
- M₂ d²y/dt² + Ky = B₂ d(x − y)/dt

Analogous circuits:

- **f-i (force-current) analogy:** current source i, two node voltages v₁ and v₂; C = M, R = 1/B, L = 1/K. C₁ and R₁ at node v₁, R₂ between the nodes, C₂ and L at node v₂.
- **f-v (force-voltage) analogy:** the two nodes become two loops, and the current source becomes a voltage source. L₁ and R₁ in the first loop, R₂ in the common branch, L₂ and C in the second loop. R = B, C = 1/K, L = M. Note in the notebook: "The displacement difference sits between the variables."

## Field-controlled motor and gearbox

The block chain set up from the defining equations in the Laplace domain: Vf → 1/(Lfs + Rf) → If → Kg → Vg → 1/(Leq s + Req) → Ig → Km → T → 1/(Jeq s² + Beq s) → θ → n → θL. Transfer function:

- θL(s)/Vf(s) = Kg Km n / [(Lfs + Rf)(Leq s + Req)(Jeq s² + Beq s)]

## Block diagram algebra (margin notes)

Notes added to the "Rules of Block Diagram Algebra" table in the textbook:

- In successive summing points, the positions of the signs (+ or −) can be interchanged.
- Series blocks are multiplied; however, this holds only if there is **no loading** between the blocks ("if the blocks can be drawn this way when there is no loading, then there is no loading").
- Parallel (feedforward path) blocks are added; at a takeoff point a signal of the same value is passed on.
- When a summing point is moved in front of a block, 1/G must be added to the other input.
- The positions of a takeoff point and a summing point can be interchanged; a structure with G₂ in the feedback path can be converted to unity feedback: [G₁G₂/(1 + G₁G₂)]·(1/G₂) = G₁/(1 + G₁G₂).

## Example 3(a): Loading effect and block diagram

First, a single RC circuit (series R, parallel C):

1. Time domain: i = (vi − vo)/R, vo = (1/C)∫i dt
1. Laplace transform with zero initial conditions: I(s) = [Vi(s) − Vo(s)]/R, Vo(s) = I(s)/(Cs)
1. Sub-blocks are drawn according to the cause-and-effect relationships.
1. Combining them gives a unity-feedback structure: Vo(s)/Vi(s) = 1/(RCs + 1)

Then two RC circuits in cascade (R₁, C₁, R₂, C₂):

- V₁ + R₁i₁ = vi, (1/C₁)∫(i₁ − i₂)dt = v₁, vo + R₂i₂ = v₁, (1/C₂)∫i₂ dt = vo
- I₁(s) = [Vi(s) − V₁(s)]/R₁, V₁(s) = [I₁(s) − I₂(s)]/(C₁s), I₂(s) = [V₁(s) − Vo(s)]/R₂, Vo(s) = I₂(s)/(C₂s)
- Vo(s)/Vi(s) = 1/[R₁C₁R₂C₂s² + (R₁C₁ + R₂C₂ + R₁C₂)s + 1]

The result is **not equal** to the product of two first-order blocks, i.e. [1/(R₁C₁s + 1)]·[1/(R₂C₂s + 1)]: the second circuit loads the first (the R₁C₂ term).

## Example 4(a): Disturbance input

R(s) → P(s) → summing point → C(s) → summing point (disturbance D(s)) → G(s) → Y(s), with H(s) in the feedback path. Since there are two inputs, the effects are found one at a time and summed:

- For D(s) = 0: Y_R(s) = [C(s)G(s)/(1 + C(s)G(s)H(s))]·P(s)R(s)
- For R(s) = 0: Y_D(s) = [G(s)/(1 + C(s)G(s)H(s))]·D(s)
- Total: Y(s) = C(s)G(s)P(s)R(s)/(1 + CGH) + G(s)D(s)/(1 + CGH)

## Example 5(a): Temperature control system

A system consisting of an amplifier (K₁), a solenoid (L, R; with negligible mass, and with B and K), a valve opened by the solenoid with steam flow rate q, and a thermocouple (Kt) measuring the temperature at the heating wire, with feedback of gain K₂. Valve opening q = Ks x; there is a relation dT/dt = −CT + Kc q between temperature and steam flow rate.

System equations and their Laplace counterparts:

- K₁e = L di/dt + Ri ⇒ K₁E(s) = (Ls + R)I(s)
- f = Kf i = B dx/dt + Kx ⇒ Kf I(s) = (Bs + K)X(s)
- q = Ks x ⇒ Q(s) = Ks X(s)
- dT/dt = −CT + Kc q ⇒ (s + C)T(s) = Kc Q(s)
- et = Kt T ⇒ Et(s) = Kt T(s)
- e = r − K₂et ⇒ E(s) = R(s) − K₂Et(s)

Closed-loop transfer function:

- T(s)/R(s) = K₁KfKsKc / [(Ls + R)(Bs + K)(s + C) + K₁KfKsKcKtK₂]

*Note: In the notebook's block diagram, the thermocouple block is labeled "Kf"; according to the equations, this block should be Kt. The transfer function is correctly written with Kt.*
