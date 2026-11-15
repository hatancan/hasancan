---
baslik: EEM441 Communications I: 2010 and 2014 Quizzes (SSB Phase Error, FM Chain, Superheterodyne)
ozet: EEM441 Communications I 2010 quiz, 2014 make-up quiz and August 2014 Quiz 2: SSB with phase discrimination, balanced modulator, frequency multiplier chain and image frequency.
---

Three short exams from the Başkent University EEM 441 Communications I course between 2010 and 2014: the 2 November 2010 quiz, the 29 December 2014 make-up quiz and the 6 August 2014 Quiz 2. The sources are photographs of the exam papers and solutions (some of them screenshots); the content was transcribed from the photographed pages into text, and the photographs have not been published. The student name and number on the make-up exam paper have not been transcribed.

## Quiz, 2 November 2010

**Question 1.** In the SSB generator with phase discrimination shown in the figure, the carrier phase shift is −90° + δ (δ is a small angle error). At the input, x(t) is multiplied by (A_c/2)cos ω_ct in the upper branch; the lower branch contains a Hilbert transformer H_Q(f) and (A_c/2)sin ω_ct; the branches are added or subtracted. a) Find the modulated output s(t) and the envelope A(t). b) For x(t) = cos ω_mt and a quadrature phase shift with |H_Q(f_m)| = 1 − ε and arg H_Q(f_m) = −90° + δ, recompute s(t) as the sum of two sinusoids (ε and δ are small errors).

**Question 2.** When amplitude modulators are unbalanced, they are nonlinear elements, one with V_out = a₁V_in + a₂V_in² + a₃V_in³ and the other with V_out = b₁V_in + b₂V_in² + b₃V_in³ (balanced modulator: the outputs of two AM modulators with inputs ½x(t) and −½x(t) are subtracted; each consists of a nonlinear element + BPF). Calculate the output signal in this case.

*Note: In the photograph of this page, only the questions were legible.*

## Quiz 1 (make-up), 29 December 2014 (duration 30 min)

**Question 1 (50 points).** The information signal is f(t) = cos 2π·2·10³t + ½cos 2π·4·10³t, and the carrier is a 1 MHz cosine (cos 2π·10⁶t). Sketch the frequency spectra of the following signals: a) for the double-sideband (DSB) modulated signal c(t) = f(t)cos 2π·10⁶t, C(jω); b) for the single-sideband (upper sideband) modulated signal c(t) = f(t)cos 2π·10⁶t ± f̂(t)sin 2π·10⁶t, C(jω).

**Question 2 (50 points).** The carrier frequency of a double-sideband signal of the form f(t)cos ω₁t is to be changed from ω₁ to ω₂ (frequency translation). Show that this can be achieved by applying f(t)cos ω₁t and cos(ω₁ + ω₂)t to the inputs of a balanced modulator and using an appropriate filter.

## Quiz 2, 6 August 2014 (duration 1 hour)

**Question 1.** The general expression of a frequency-modulated signal is f_FM(t) = A_c cos[ω_ct + K∫f(t)dt]; the modulating signal is f(t) = A_m cos ω_mt. For A_c = 50 V, A_m = 20 V, K = 2356, ω_c = 2π·200·10³ rad/s, ω_m = 2π·15·10³ rad/s: a) Show that the signal f₁(t) = 50cos(2π·200·10³t + 0.5 sin(2π·15·10³t)) is a narrowband FM signal and find its bandwidth. b) In the block diagram below, obtain the signal f₅(t), state with a reason what it is called, and give its carrier frequency and modulation index. c) Calculate the average power that f₅(t) can produce in a 50 Ω load resistor.

*Block diagram:* f₁(t) → frequency multiplier ×64 → f₂(t) → mixer (f₀(t) = 20cos(2π·10 900·10³t)) → f₃(t) → BPF (passband 1885–1915 kHz) → f₄(t) → frequency multiplier ×48 → f₅(t).

**Question 2.** The frequency-modulated signal applied to the input of the block diagram is f₁(t) = 10cos(2π·200·10³t + 0.5 sin(2π·15·10³t)) V, with the same block diagram given. a) Obtain the signal f₅(t); b) find the maximum power that the signal f₅(t) can deliver to a 50 Ω load resistor; c) for the case where the maximum frequency deviation of the signal f₅(t) is 75 kHz, calculate the bandwidths of the signals f₁(t) and f₅(t).

*Solution.* f₂(t) = 10cos(2π·12 800·10³t + 32 sin(2π·15·10³t)) (×64). Mixer: f₃(t) = f₂f₀ = (10·20/2)[cos(2π·1900·10³t + 32 sin(…)) + cos(2π·23 700·10³t + 32 sin(…))], i.e. two components with amplitude 100. The BPF (1885–1915 kHz) passes only the 1900 kHz one of the sum/difference components: f₄(t) = 100cos(2π·1900·10³t + 32 sin(2π·15·10³t)). ×48: **f₅(t) = 100cos(2π·91 200·10³t + 1536 sin(2π·15·10³t))**, the carrier is 91.2 MHz, and the modulation index is β₅ = 1536 (wideband FM). Receiver/load matching: with a source resistance of 50 Ω and a load of 50 Ω, the maximum power is P = f₅²/(4R_L) = 100²/(4·50) = 50 W. Bandwidths: for f₁(t), since β ≈ 0.5 (narrowband), B₁ = 2f_m = 2·15 kHz = 30 kHz; for f₅(t), Δf = 75 kHz ⇒ β = Δf/f_m = 75/15 = 5, B₅ = 2(1 + β)f_m = 2·6·15 kHz = 180 kHz.

*Note: The same question also appears in the worked-solution sheet with the values A_c = 50 V, A_m = 20 V, K = 2356; β = KA_m/ω_m = 2356·20/(2π·15·10³) = 0.5.*

**Question 3.** A superheterodyne receiver is tuned to listen to a radio station with carrier frequency ω_c; the antenna is simultaneously under the influence of another station with carrier frequency ω_c + 2ω_a (the image frequency). The expression of the incoming signal is f(t) = f₁(t)cos(ω_ct) + f₂(t)cos[(ω_c + 2ω_a)t]; the frequency spectra of the information signals f₁(t) and f₂(t) (rectangular and triangular) and the spectra of the receiver's radio-frequency and intermediate-frequency amplifiers are given in the figure. a) Sketch the first conversion of the receiver; b) show the outputs of the radio-frequency amplifier, the mixer and the intermediate-frequency amplifier with their frequency spectra; c) state the solution that would eliminate the image interference that causes a radio broadcast to be heard at the same time.

*Note: Since Question 3 of the August 2014 quiz is blurry in the photograph, the question text has been transcribed in summarized form; the solution contains only one page concerning the image frequency (choosing the local oscillator below/above the carrier for the lower/upper sideband of SSB, and the inversion of the spectrum).*
