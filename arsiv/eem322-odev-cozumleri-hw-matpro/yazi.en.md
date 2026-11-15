---
baslik: EEM322 Control Systems: HW+MATPRO Assignment and Handwritten Solutions (HW 18, 35, 36) with Ogata B-5-15
ozet: Prof. Dr. Alper Uraz's EEM322 HW+MATPRO assignment sheet (G(s) = K(s+a)/[sⁿ(s+b)(s²+cs+d)], 50 parameter sets) and three handwritten solutions from spring 2012: percent overshoot and settling time, direct and cascade state diagrams, static error constants, root locus; plus a comparative-system solution for Ogata B-5-15.
---

This post brings together the **HW+MATPRO** assignment of the Başkent University course **EEM322 Control Systems** and the handwritten solutions to it. The assignment sheet is a Word document prepared by the course instructor **Prof. Dr. Alper Uraz** (first version 2005, last revised January 2012). The solutions were **transcribed into text** from notebook and paper pages photographed on 30 April 2012. The photographs were not published. The pages carry no name indicating who wrote them. At the end there is also an **Ogata B-5-15** solution, made up of scanned pages found in the same folder. The assignment sheet and the B-5-15 scans can be downloaded as a ZIP at the end of the post.

The course's classical assignment list (B-problems from the Ogata and Uraz textbooks) is in the [syllabus post](/arsiv/eem322-izlence/). The HW+MATPRO here, by contrast, is an assignment given to each student with their own parameters, proceeding through a single system.

## Assignment sheet: HW+MATPRO

Open-loop transfer function (OLTF):

- G(s) = K(s + a) / [sⁿ (s + b)(s² + cs + d)]

The {n, a, b, c, d} parameters are given in a table for each HW number. K = 1 may be taken when needed. The problems:

1. For a unit step input, compute Ts and PO (percent overshoot), and sketch the unit step response.
1. Draw the state diagrams and obtain the state-space description (SSD) using direct and cascade decomposition.
1. With G(s) in a unity-feedback configuration, find Kp, Kv, Ka; compute ess for unit step, unit ramp and parabolic inputs.
1. Sketch the root locus for 0 ≤ K < ∞; show all important points such as breakaway points, jω-axis crossings, the asymptote centroid, the asymptotes, and the departure/arrival angles.
1. Sketch the Bode diagrams; read off ωg, ωp, the gain margin (gm) and the phase margin (pm).
1. Sketch the complete Nyquist plot step by step as in the worked examples, and determine closed-loop stability using the Nyquist criterion.

Submission rules: Problems 1–4 are due on the Friday of week 11, and problems 5–6 on the Friday of week 14. All time responses, root loci, Bode and Nyquist plots are drawn **by hand**. The **MATLAB project** part requires MATLAB code and appropriate MATLAB plots for every step of problems 4–6 (due: Friday of week 14).

### Parameter table

| HW | n | a | b | c | d | HW | n | a | b | c | d |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 2 | 0.6 | 1 | 26 | 0 | 2 | 3 | 0.6 | 1 |
| 2 | 0 | 1 | 3 | 1.2 | 4 | 27 | 0 | 2 | 4 | 1.2 | 4 |
| 3 | 0 | 1 | 4 | 1.8 | 9 | 28 | 0 | 2 | 5 | 1.8 | 9 |
| 4 | 0 | 1 | 5 | 2.4 | 16 | 29 | 0 | 2 | 6 | 2.4 | 16 |
| 5 | 0 | 1 | 6 | 0.8 | 1 | 30 | 0 | 2 | 7 | 0.8 | 1 |
| 6 | 0 | −1 | 2 | 1.6 | 4 | 31 | 1 | 0.5 | 1 | 4 | 7.0 |
| 7 | 0 | −1 | 3 | 2.4 | 9 | 32 | 1 | 1.0 | 1 | 4 | 7.5 |
| 8 | 0 | −1 | 4 | 3.2 | 16 | 33 | 1 | 1.5 | 1 | 4 | 8.0 |
| 9 | 0 | −1 | 5 | 1 | 1 | 34 | 1 | 2.0 | 1 | 4 | 8.5 |
| 10 | 0 | −1 | 6 | 2 | 4 | 35 | 1 | 2.5 | 1 | 4 | 9.0 |
| 11 | 1 | 1 | 2 | 3 | 9 | 36 | 1 | 1.0 | 1.5 | 5 | 8.0 |
| 12 | 1 | 1 | 3 | 4 | 16 | 37 | 1 | 1.5 | 1.5 | 5 | 8.5 |
| 13 | 1 | 1 | 4 | 1.2 | 1 | 38 | 1 | 2.0 | 1.5 | 5 | 9.0 |
| 14 | 1 | 1 | 5 | 2.4 | 4 | 39 | 1 | 2.5 | 1.5 | 5 | 9.5 |
| 15 | 1 | 1 | 6 | 3.6 | 9 | 40 | 1 | 3.0 | 1.5 | 5 | 10.0 |
| 16 | 1 | −1 | 2 | 4.8 | 16 | 41 | 0 | −2 | 2 | 1.6 | 4 |
| 17 | 1 | −1 | 3 | 1.4 | 1 | 42 | 0 | −2 | 3 | 2.4 | 9 |
| 18 | 1 | −1 | 4 | 2.8 | 4 | 43 | 0 | −2 | 4 | 3.2 | 16 |
| 19 | 1 | −1 | 5 | 4.2 | 9 | 44 | 0 | −2 | 5 | 1 | 1 |
| 20 | 1 | −1 | 6 | 5.6 | 16 | 45 | 0 | −2 | 6 | 2 | 4 |
| 21 | 0 | 1 | 7 | 0 | 0 | 46 | 0 | 2 | 7 | 3 | 9 |
| 22 | 0 | 1 | 8 | 0 | 0 | 47 | 0 | 2 | 8 | 4 | 16 |
| 23 | 0 | 1 | 9 | 0 | 0 | 48 | 0 | 2 | 9 | 1.2 | 1 |
| 24 | 0 | 1 | 10 | 0 | 0 | 49 | 0 | 2 | 10 | 2.4 | 4 |
| 25 | 0 | 1 | 11 | 0 | 0 | 50 | 0 | 2 | 11 | 3.6 | 9 |

## Solution 1: HW 35, G(s) = (s + 2.5) / [s(s + 1)(s² + 4s + 9)]

This solution, written on graph-paper notebook pages, uses the parameters of HW 35 (n = 1, a = 2.5, b = 1, c = 4, d = 9). The top of the page also shows traces of another exercise: for Δ(s) = s³ + 4s² + 9s + K, K = 36 was found from the Routh table, and s = ±j3 was obtained from the auxiliary equation 4s² + 36 = 0. There is also a root locus starting point written for K(s + 1)/(s + 2) (s₁ = −2 at K = 0).

### Problem 2: Direct decomposition

Once the denominator is expanded, G(s) = (s + 2.5)/(s⁴ + 5s³ + 13s² + 9s). The numerator and denominator are divided by s⁴:

- Y(s)/U(s) = (s⁻³ + 2.5s⁻⁴)/(1 + 5s⁻¹ + 13s⁻² + 9s⁻³)
- X(s) = U(s) − 5s⁻¹X(s) − 13s⁻²X(s) − 9s⁻³X(s)
- Y(s) = s⁻³X(s) + 2.5s⁻⁴X(s)

In the signal flow graph with four integrators, the feedback gains are −5, −13, −9 and the forward-path gains are 1 and 2.5. When the state variables x₁…x₄ are assigned to the integrator outputs from right to left:

- ẋ = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, −9, −13, −5]] x + [0, 0, 0, 1]ᵀ u
- y = [2.5, 1, 0, 0] x

### Problem 2: Cascade decomposition

G(s) is split into three parts: (s + 2.5)/(s + 1) · (1/s) · 1/(s² + 4s + 9). For the first-order block the general pattern is:

- (s + z)/(s + p) = (1 + z s⁻¹)/(1 + p s⁻¹) ⇒ X(s) = U(s) − p s⁻¹X(s), Y(s) = X(s) + z s⁻¹X(s)

For the second-order block, 1/(s² + 4s + 9) = s⁻²/(1 + 4s⁻¹ + 9s⁻²) ⇒ X(s) = U(s) − 4s⁻¹X(s) − 9s⁻²X(s), Y(s) = s⁻²X(s). The cascade SSD obtained in the notebook:

- ẋ = [[0, 1, 0, 0], [−9, −4, 1, 0], [0, 0, 0, 2.5], [0, 0, 0, −1]] x + [0, 0, 1, 0]ᵀ u, y = [1, 0, 0, 0] x

*Note: In the notebook's cascade matrix, the connection between the 1/s block and the (s + 2.5)/(s + 1) block is set up incorrectly: as written, u never drives x₄. Since (s + 2.5)/(s + 1) = 1 + 1.5/(s + 1), the correct form is ẋ₄ = −x₄ + u, ẋ₃ = 1.5x₄ + u, ẋ₂ = −9x₁ − 4x₂ + x₃, ẋ₁ = x₂, y = x₁; that is, the third row of A should be [0, 0, 0, 1.5] and B = [0, 0, 1, 1]ᵀ.*

At the bottom of the page there is also a reminder for the first problem: ζωn = α and Ts = 4/(ζωn).

## Solution 2: HW 18, G(s) = (s − 1) / [s(s + 4)(s² + 2.8s + 4)]

Below this solution, written on plain paper, it says "Note: The questions were solved according to number 18." The parameters of HW 18 are: n = 1, a = −1, b = 4, c = 2.8, d = 4.

### Problem 1: PO and Ts

In the solution, the second-order factor s² + 2.8s + 4 is compared with s² + 2ζωn s + ωn²:

- 2ζωn = 2.8 ⇒ ζωn = 1.4; ωn² = 4 ⇒ ωn = 2 ⇒ ζ = 0.7
- Ts = 2/α, α = ζωn = 1.4 ⇒ Ts = 2/1.4 = 10/7
- PO = 100·e^(−ζπ/√(1−ζ²)) = 100·e^(−0.99π) = 100·e^(−3.11) ≈ 4.46

*Note: If √(1 − 0.49) = 0.714 is used for e^(−ζπ/√(1−ζ²)), the exponent is −3.08 and PO ≈ 4.6%. More importantly, this calculation uses the complex pole pair of the open loop. The closed-loop denominator is s⁴ + 6.8s³ + 15.2s² + 17s − 1, and its constant term is negative (−K for every K > 0, since a = −1). The closed loop is unstable, with a pole at s ≈ +0.056, so PO and Ts are not defined for the step response. In some rows the coefficients 1.2 and 7.2 are read in place of 2.8; the correct expansion of the open-loop denominator is s⁴ + 6.8s³ + 15.2s² + 16s.*

### Problem 3: Error constants

- Kp = lim(s→0) G(s) = ∞
- Kv = lim(s→0) sG(s): the solution writes "−1/0 = ∞"
- Ka = lim(s→0) s²G(s): the solution gives ∞
- W(s) = 1/(1 + G), ess = lim(s→0) sR(s)W(s)
- Unit step: ess = 0; unit ramp: ess = −16; parabolic input (R = 2/s³): ess = ∞

*Note: Since G(s) has a single pole at the origin, the system is type 1: Kv = lim sG(s) = −1/16 (finite), Ka = 0. The ramp result ess = −16 = 1/Kv is consistent with this, but the Kv and Ka lines are wrong. In any case, since the closed loop is unstable, these steady-state errors do not actually occur.*

### Problem 4: Root locus

- Open-loop poles: 0, −4, −1.4 ± j1.43 (n = 4); zero: +1 (m = 1)
- Number of asymptotes n − m = 3, angles 60°, 180°, 300°
- Asymptote centroid: the solution gives σa = (−4 − 1.4 − 1.4)/3 = −6.8/3 ≈ −2.2
- The Routh table for the jω crossing (Kc) and the dK/ds = 0 steps for the breakaway point are left as headings; the pole-zero placement is drawn.

*Note: The centroid formula is σa = (Σ poles − Σ zeros)/(n − m). Subtracting the zero at +1 gives σa = (−6.8 − 1)/3 = −2.6.*

## Solution 3: HW 36, G(s) = K(s + 1) / [s(s + 1.5)(s² + 5s + 8)]

A solution written in English in a spiral notebook, headed "HW No: 36" (n = 1, a = 1, b = 1.5, c = 5, d = 8).

### Problem 1

From the hand-drawn step response, PO = 11.3% and Ts = 2.94 were read.

*Note: For K = 1, the closed-loop denominator is s⁴ + 6.5s³ + 15.5s² + 13s + 1, with poles at approximately −2.38 ± j1.19, −1.66 and −0.085. The response has no overshoot and is very slow (Ts ≈ 43 s). The 11.3% and 2.94 s values in the plot are obtained only around K ≈ 14; the plot was most likely drawn with a different K.*

### Problem 2: Direct and cascade SSD

- G(s) = (s + 1)/(s⁴ + 6.5s³ + 15.5s² + 12s) = (s⁻³ + s⁻⁴)/(1 + 6.5s⁻¹ + 15.5s⁻² + 12s⁻³)
- X(s) = U(s) − (6.5s⁻¹ + 15.5s⁻² + 12s⁻³)X(s), Y(s) = (s⁻³ + s⁻⁴)X(s)
- Direct decomposition: ẋ = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, −12, −15.5, −6.5]] x + [0, 0, 0, 1]ᵀ u, y = [1, 1, 0, 0] x

For the cascade decomposition, G(s) is written as (1/s) · (s + 1)/(s + 1.5) · 1/(s + 2.5 − j1.32) · 1/(s + 2.5 + j1.32), and the complex poles and first-order blocks are arranged in sequence.

### Problem 3: Error constants

- Kp = G(0) = ∞, Kv = lim sG(s) = 1/12, Ka = 0 ⇒ the system is type 1
- Unit step: ess = 0; unit ramp: ess = 12 = 1/Kv; parabolic input: ess = ∞
- As a note: for unity feedback, W(s) = 1/(1 + G(s)), ess = lim(s→0) sR(s)W(s)

### Problem 4: Root locus

- Open-loop poles: 0, −1.5, −2.5 ± j1.32 (n = 4); zero: −1 (m = 1)
- Asymptotes: θk = (2k + 1)π/(n − m) = 60°, 180°, 300°; σa = (0 − 1.5 − 2.5 − 2.5 − (−1))/3 = −1.83
- Routh table for Δ(s) = s⁴ + 6.5s³ + 15.5s² + 12s + K(s + 1) = 0: s⁴: 1, 15.5, K; s³: 6.5, 12 + K; s²: X = (15.5·6.5 − 12 − K)/6.5, K
- It is stated that there is no breakaway point on the real axis ("does not cross the real axis"); the dK/ds = 0 derivative is set up.
- Departure angle (from the −2.5 + j1.32 pole): θd = 180° − (152.2° + 127.2° + 90°) + 138.6° ≈ −50°
- In the drawn locus, two branches leave the complex poles at −50° and cross the imaginary axis, while the others remain on the real axis.

*Note: Completing the Routh table and setting the s¹ row to zero gives K² − 34.5K − 1065 = 0 ⇒ Kc ≈ 54.2. From the auxiliary equation, the jω crossing is around ±j3.19; in the plot this point is marked as approximately "3.1j".*

## Appendix: Ogata B-5-15, comparison of three systems

This solution, consisting of three scanned pages (pages 11–13), addresses Ogata's problem B-5-15. The problem compares the unit ramp error and time response criteria for three unity-feedback systems.

| | G(s) | Type | Ramp ess | ζ | Mp | Tr | Ts |
|---|---|---|---|---|---|---|---|
| System I | 5/[s(5s + 1)] | 1 | 1/5 | 0.1 | 1.72 | 1.67 | 40 |
| System II | 5(1 + 0.8s)/[s(5s + 1)] | 1 | 1/5 | 0.5 | 1.16 | 2.42 | 8 |
| System III | 1/[s(s + 1)] | 1 | 1 | 0.5 | 1.16 | 2.42 | 8 |

Sample calculations:

- System I: Δ(s) = 5s² + s + 5 ⇒ s² + 0.2s + 1 ⇒ ωn = 1, ζ = 0.1; θ = cos⁻¹(0.1) = 1.47, Tr = (π − θ)/ωd; Ts = 4/(ζωn) = 40
- System II: T(s) = (1 + 0.8s)/(s² + s + 1), W(s) = 1 − T(s) = s(s + 0.2)/(s² + s + 1) ⇒ ess = 0.2 for the ramp
- System III: T(s) = 1/(s² + s + 1), E(s) = R(s)·s(s + 1)/(s² + s + 1) ⇒ ess = 1 for the ramp
- In all three systems, ess = 0 for the unit impulse and unit step

Commentary (from the solution): System 1 has the smallest damping ratio and responds the fastest, but its overshoot and settling time are very large; therefore it should not be chosen. Systems 2 and 3 have the same damping ratio and equal Mp, Tr, Ts values; System 2 has the smaller steady-state error. Consequently, the best system is System 2.

*Note: The closed loop of System II has a zero at −1.25, and this zero speeds up the response and increases the overshoot. In simulation, Mp ≈ 1.25 and the 0–100% rise time ≈ 1.43 s are obtained for System II (Ts ≈ 7.6 s). That is, the Mp and Tr values of Systems II and III are actually not equal. Even so, the conclusion "System 2 is best" does not change.*
