---
baslik: EEM322 Control Systems: Exam-Style Practice Problems and Notebook Solutions (2012)
ozet: A five-question exam-style practice set for EEM322 Control Systems and a student's notebook solutions: controllability and solution of the state equation, root locus, error constants and steady-state error, gain and phase margins, full Nyquist plot.
---

This post is a text transcription of eight notebook pages in the "denetim sınav" (control exam) subfolder of the EEM322 Control Systems folder. The pages were photographed on May 30, 2012: the first page has five exam-style questions, and the following pages have a student's pencil solutions to these questions. **Transcribed from the photographed pages**; the photographs were not published. There are a few errors in the solutions; they are pointed out in the notes below.

## Questions

1. ẋ(t) = [−1 1; 0 0]x(t) + [1; 0]u(t), with initial condition x(0) = [7; 2] (the first element is hard to read in the photograph). (a) Is the system controllable? (b) Find the complete solution of the state equation (t ≥ 0).
1. G(s) = K(s + 2)/[(s + 1)(s − 3)]. Examine the closed-loop stability; find the critical K value and the critical points. Give the formulas used for the centroid and angles of the asymptotes; compute the possible breakaway points in the root locus plot; sketch the root locus in full detail for the range 0 ≤ K < ∞.
1. G(s) = K/[s(s + 1)(s + 4)]: for K = 10, find the error constants (Kp, Kv, Ka) and ess for unit step, ramp and parabolic inputs.
1. For the same system with K = 10, the gain crossover frequency is ωg = 1.38 rad/s. Find the phase crossover frequency ωp and the gain and phase margins (gm, pm); discuss the closed-loop stability in terms of gm and pm.
1. Obtain the full Nyquist plot for K = 10.

## Question 1: Controllability and solution of the state equation

1. (a) Controllability matrix U = [B AB] = [1 −1; 0 0] ⇒ det U = 0, rank U = 1 ⇒ the system is **not controllable**.
1. (b) (sI − A)⁻¹ = [s + 1 −1; 0 s]⁻¹ = (1/(s(s + 1)))·[s 1; 0 s + 1] = [1/(s + 1) 1/(s(s + 1)); 0 1/s], where 1/(s(s + 1)) = 1/s − 1/(s + 1).
1. State transition matrix: **e^(At) = [e^(−t) 1 − e^(−t); 0 1]**.
1. X(s) = (sI − A)⁻¹x(0) + (sI − A)⁻¹B·U(s) = (1/(s(s + 1)))·([s 1; 0 s + 1][7; 2] + [s 1; 0 s + 1][1; 0]·(1/s)).

*Note: In the notebook the solution stops at this line. If continued, X₁(s) = (7s + 3)/[s(s + 1)] = 3/s + 4/(s + 1), X₂(s) = 2/s; that is, x₁(t) = 3 + 4e^(−t), x₂(t) = 2 (t ≥ 0).*

## Question 2: Root locus

1. T(s) = G/(1 + G) = K(s + 2)/[s² − 2s − 3 + K(s + 2)].
1. Open-loop poles at −1 and +3 (n = 2), zero at −2 (m = 1). Number of asymptotes n − m = 1; its angle is θk = (2k + 1)π/(n − m) = 180°; centroid σ = (−1 + 3 − (−2))/1 = 4.
1. Δ(s) = s² − 2s − 3 + K(s + 2) = s² + (K − 2)s + 2K − 3. Routh table: s²: 1, 2K − 3; s¹: K − 2; s⁰: 2K − 3. The notebook gives the critical gain as Kcr = 3/2 and writes s(−2 + 3/2) = 0 ⇒ s = 0.
1. Breakaway points: K = −(s² − 2s − 3)/(s + 2); dK/ds = 0 ⇒ (2s − 2)(s + 2) − (s² − 2s − 3) = 0 ⇒ s² + 4s − 1 = 0 ⇒ roots −4.24 and 0.24.
1. Root locus: the branches leaving the poles at +3 and −1 break away from the real axis at 0.24, cross the imaginary axis and trace a circle, and return to the real axis at −4.24; one goes to the zero at −2 and the other to −∞.

*Note: The two Routh conditions must be satisfied together: K − 2 > 0 and 2K − 3 > 0, i.e. the closed loop is stable for **K > 2**. The critical gain is not 3/2 but **Kc = 2**; the auxiliary equation is then s² + 1 = 0 and the critical points are s = ±j (the locus crosses the imaginary axis here). At K = 3/2 one of the poles is at s = 0, but the other is still in the right half-plane (s = 0.5).*

## Question 3: Error constants and steady-state error

G(s) = 10/[s(s + 1)(s + 4)] (type 1):

- Kp = G(0) = ∞, Kv = lim(s→0) sG(s) = 10/4, Ka = lim(s→0) s²G(s) = 0.
- ess = lim(s→0) sR(s)W(s), W(s) = 1/(1 + G(s)) = (s³ + 5s² + 4s)/(s³ + 5s² + 4s + 10).
- R(s) = 1/s ⇒ ess = 0; R(s) = 1/s² ⇒ ess = 4/10; R(s) = 1/s³ ⇒ ess = ∞.

## Question 4: Gain and phase margins

G(jω) = 10/[jω(jω + 1)(jω + 4)] is separated into real and imaginary parts; the notebook finds the frequency at which the imaginary part vanishes as ω(−ω² + 40) = 0 ⇒ ωp = √40 ≈ 6.4 rad/s. The gain margin gm = 1/|G(jωp)| and its conversion to dB with 20 log, and the phase margin pm = 180° + ∠G(jωg) = 180° − 90° − tan⁻¹(1.38) − tan⁻¹(1.38/4), are written out, but the numerical results are not completed.

*Note: An error was made when expanding the denominator. The imaginary part of G(jω) is proportional to ω(4 − ω²), so **ωp = 2 rad/s**. |G(j2)| = 10/(2·√5·√20) = 0.5 ⇒ **gm = 2 (≈ 6 dB)**. At ωg = 1.38, pm = 90° − 54.1° − 19.0° ≈ **17°**. Both margins are positive, so the closed loop is stable (the critical gain for s³ + 5s² + 4s + K is 20).*

## Question 5: Nyquist plot

1. ω part (s = jω): |G(jω)| = 10/(ω√(ω² + 1)√(ω² + 16)), ∠G(jω) = −90° − tan⁻¹ω − tan⁻¹(ω/4). As ω → 0, ∞∠−90°; as ω → ∞, 0∠−270°.
1. Infinite-radius arc (s = Re^(jψ)): G = 10/(R³e^(j3ψ)) → 0∠−3ψ. The small semicircle indenting around the pole at the origin (s → 0) maps G onto an arc of infinite radius; the s and G angles are paired in the table as 90° ↔ −270°, 0° ↔ 0°, −90° ↔ 270°.
1. The closed curve drawn in the notebook encircles the −1 point, and the conclusion N = Z − P ⇒ 2 = Z − 0 ⇒ Z = 2, "unstable", is reached.

*Note: This result contradicts Questions 3–4. For K = 10 the curve crosses the negative real axis at −0.5 at ω = 2 rad/s (gm = 2); the −1 point is not encircled, N = 0, P = 0 ⇒ Z = 0, so the closed loop is **stable**. Z = 2 occurs only for K > 20.*
