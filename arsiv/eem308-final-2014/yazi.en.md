---
baslik: EEM308 Signals and Systems II: June 2014 Exam (Final) Questions and Solutions
ozet: June 2014 exam questions for EEM308 Signals and Systems II and a student's graded solutions: two-sided z-transform, the G(s) = H(1/s) transformation and filter type, impulse response of an ideal band-pass filter, Bode magnitude plot, changing the sampling rate, and the shift property of the one-sided z-transform.
---

This post presents the five-question exam (apparently the end-of-term exam) of the Başkent University course **EEM 308 Signals and Systems II**, prepared by **Asst. Prof. Dr. Selda Güney** and preserved as photographs, dated 12 June 2014, together with a student's **graded solution sheet**. No name or student number appears on the solution pages. The red numbers in circles show the points awarded. The questions and solutions are transcribed as text; the photographs themselves are kept in the archive and are not published.

## Questions

**1.** Using the information given below, find X(z) and x[n].

1. x[n] is two-sided and stable.
1. One of the two poles of X(z) is at z = 1/8.
1. X(1) = 19/7
1. x[−3] = −3/8, x[−5] = −3/32

**2.** If the relationship between H(s) and G(s) is G(s) = H(1/s):

- a) For H(s) = 1/(s + ½), compute and plot |H(jω)| and |G(jω)|, and determine the filter type for the transfer function.
- b) Show that the value obtained at ω = 2 from the algebraically computed magnitude functions is the same as the value obtained by vector calculation from the pole-zero diagram.
- c) Determine the linear constant-coefficient differential equation associated with H(s) and G(s).

**3.** The frequency response H(jω) of an ideal band-pass filter is as given in the figure: magnitude 1 for ω₀ − W/2 < |ω| < ω₀ + W/2, and 0 at other frequencies.

- a) What is the impulse response h(t) of this filter? (Hint: the impulse response of an ideal low-pass filter is h_c(t) = sin(ω_c t)/(πt))
- b) An ideal band-pass filter can be obtained by connecting a first-order low-pass filter and a first-order high-pass filter in series. Plot the Bode magnitude diagram of the transfer function obtained by connecting the transfer functions H₁ = 10³/(10³ + jω) and H₂ = jω/(100 + jω) in series.

**4.** The real-valued discrete-time signal x[n] has a Fourier transform X(e^{jω}) whose value is zero over 3π/14 ≤ |ω| ≤ π. What kind of system must x[n] be passed through so that the nonzero part of one period of the Fourier transform fills the range |ω| ≤ π? Explain with a block diagram; also show the shape of the Fourier transform of the signal at each stage of the system by sketching it.

**5.** If X(z) denotes the one-sided z-transform of x[n], find the one-sided z-transforms of the following in terms of X(z): a) x[n + 3], b) x[n − 3].

## Student solution

### Question 1: Two-sided z-transform

Form for a two-sided, stable sequence: x[n] = A(1/8)ⁿ u[n] − B·Cⁿ u[−n − 1].

- x[−3] = −B·C⁻³ = −3/8 ⇒ B = (3/8)C³
- x[−5] = −B·C⁻⁵ = −3/32 ⇒ (3/8)C⁻² = 3/32 ⇒ C² = 4 ⇒ **C = 2**, **B = 3**
- X(z) = A/(1 − ⅛z⁻¹) + 3/(1 − 2z⁻¹) ⇒ X(1) = 8A/7 − 3 = 19/7 ⇒ 8A/7 = 40/7 ⇒ **A = 5**

**X(z) = 5/(1 − ⅛z⁻¹) + 3/(1 − 2z⁻¹)**, 1/8 < |z| < 2

**x[n] = 5(1/8)ⁿ u[n] − 3·2ⁿ u[−n − 1]**

### Question 2: G(s) = H(1/s)

**a)** G(s) = H(1/s) = 1/(1/s + ½) = 2s/(s + 2).

- H(jω) = 1/(jω + ½), |H(jω)| = 1/√(ω² + ¼): **low-pass** (pole at −½).
- G(jω) = 2jω/(jω + 2), |G(jω)| = 2|ω|/√(ω² + 4): **high-pass** (zero at the origin, pole at −2).

**b)** Algebraic calculation at ω = 2: |H(j2)| = 1/√(4 + ¼) ≈ 0.485, |G(j2)| = 4/√(4 + 4) ≈ 1.414. With vectors drawn to the point j2 on the pole-zero diagram: for H, the pole vector |r| = √((½)² + 4), K = 1 ⇒ |H(j2)| = 1/|r| ≈ 0.485; for G, the zero vector |s| = 2, the pole vector |r| = √(4 + 4), K = 2 ⇒ |G(j2)| = 2·2/√8 ≈ 1.414. The two methods give the same result.

**c)** Differential equations:

- H(s) = Y(s)/X(s) = 1/(s + ½) ⇒ **dy/dt + ½y(t) = x(t)**
- G(s) = 2s/(s + 2) ⇒ **dy/dt + 2y(t) = 2 dx/dt**

### Question 3: Band-pass filter

**a)** The band-pass filter is a low-pass filter with cutoff frequency ω_c = W/2 shifted to ±ω₀: H(jω) = H₁(j(ω − ω₀)) + H₁(j(ω + ω₀)), h₁(t) = sin(Wt/2)/(πt). The solution gives the result as h(t) = [sin(Wt/2)/(πt)]·cos ω₀t (10 points).

*Note: Since a frequency shift of ±ω₀ corresponds in time to multiplication by e^{jω₀t} + e^{−jω₀t} = 2cos ω₀t, the correct answer is h(t) = 2 sin(Wt/2) cos(ω₀t)/(πt); the solution is missing the factor 2.*

**b)** H₁(jω) = 1/(1 + jω/10³), H₂(jω) = (jω/10²)/(1 + jω/10²). For H = H₁H₂:

20 log|H(jω)| = −20 log|1 + jω/10³| − 40 + 20 log|ω| − 20 log|1 + jω/10²|

The corner frequencies are ω₁ = 10³ and ω₂ = 10². Asymptotic values:

| ω (rad/s) | 10 | 10² | 10³ | 10⁴ | 10⁵ | 10⁶ |
|---|---|---|---|---|---|---|
| Constant | −40 | −40 | −40 | −40 | −40 | −40 |
| LP pole (10³) | 0 | 0 | 0 | −20 | −40 | −60 |
| Zero at origin | 20 | 40 | 60 | 80 | 100 | 120 |
| HP pole (10²) | 0 | 0 | −20 | −40 | −60 | −80 |
| **Total (dB)** | −20 | 0 | 0 | −20 | −40 | −60 |

The magnitude is a curve that is 0 dB between 10² and 10³ rad/s, rises at +20 dB/decade below that range, and falls at −20 dB/decade above it.

*Note: "Band-stop filter" is written in the margin of the solution; as the table shows, the system is a **band-pass** filter that passes the 100–1000 rad/s band.*

### Question 4: Spreading the spectrum to |ω| ≤ π

The bandwidth of X(e^{jω}) is 3π/14; to expand it to π, the sampling rate must be reduced by a factor of 14/3. Since the ratio is not an integer, interpolation by 3 is performed first, followed by decimation by 14:

x[n] → **zero insertion** → w[n] → **low-pass filter** (cutoff ±π/14) → p[n] → **decimation** → y[n]

- Zero insertion: w[n] = x[n/3] (n = 0, ±3, ±6, …), otherwise 0. W(e^{jω}) = X(e^{j3ω}): the main band narrows to ±π/14, and replicas appear around ±2π/3 (25π/42–31π/42).
- The filter removes the replicas; P(e^{jω}) contains only the |ω| ≤ π/14 band.
- Decimation: y[n] = p[14n]; the spectrum expands by a factor of 14 and Y(e^{jω}) fills the entire (−π, π) interval.

*Note: The solution writes w[n] = x[n/2]; the expression consistent with the samples n = 0, ±3, ±6 is x[n/3].*

### Question 5: Shift property of the one-sided z-transform

**a)** y[n] = x[n + 3]:

Y(z) = Σₙ₌₀^∞ x[n + 3] z⁻ⁿ = z³ Σₙ₌₃^∞ x[n] z⁻ⁿ

**Y(z) = z³X(z) − x[0]z³ − x[1]z² − x[2]z**

**b)** y[n] = x[n − 3]:

Y(z) = Σₙ₌₀^∞ x[n − 3] z⁻ⁿ = z⁻³X(z) + (the terms x[−3], x[−2], x[−1] arising for n = 0, 1, 2)

**Y(z) = z⁻³X(z) + x[−1]z⁻² + x[−2]z⁻¹ + x[−3]**

## Solution pages
