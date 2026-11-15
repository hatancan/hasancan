---
baslik: EEM441 Communications I: 2006–2007 Quizzes, Midterm and Final Exam Questions
ozet: Exams from the 2006–2007 fall semester of EEM441 Communications Systems I: SSB/DSB/AM/FM power and bandwidth, envelope detection, superheterodyne image frequencies, FM transmitter frequency error.
---

Exams from the 2006–2007 fall semester of the EEM 441 Communications Systems I course in the Department of Electrical and Electronics Engineering at Başkent University: Quiz 2 on 16 November 2006, the midterm exam on 18 November 2006, Quiz 3 on 19 December 2006, and the final exam on 12 January 2007 (questions in English). The sources are phone/camera photographs of the exam papers and handwritten solutions; the content was transcribed from the photographed pages into text, and the photographs have not been published.

## Quiz 2, 16 November 2006 (duration 45 min)

**Question 1.** The normalized signal m(t) has a bandwidth of 10 kHz and a power content of 0.5 W; the carrier A cos(2πf₀t) has a power content of 200 W. If m(t) modulates the carrier using a) SSB amplitude modulation, b) DSB-SC, c) AM with a modulation index of 0.6, d) FM with k_f = 50 000 (B_T = 2(Δf + W)), what are the bandwidth and power content of the modulated signal?

*Solution.* A_c = 20, P_c = 200 W, P_m = 0.5 W.

| Modulation | Bandwidth | Power |
|---|---|---|
| SSB | W = 10 kHz | 2P_cP_m = 200 W |
| DSB-SC | 2W = 20 kHz | P_cP_m = 100 W |
| AM (μ = 0.6) | 2W = 20 kHz | P_c(1 + μ²P_m) = 200(1 + 0.36×0.5) = 236 W |
| FM (k_f = 50 000) | 2(50 + 10) = 120 kHz | A²/2 = P_c = 200 W |

**Question 2.** The output of an SSB-L transmitter modulated by f(t) = cos(2000πt) is, in complex representation, s(t) = Re{A[1 + m f(t) + j m f̂(t)]e^(jω_c t)}. a) Compute f̂(t). b) Write the envelope detector output; for which values of m is envelope detection possible? c) If the unmodulated power across 50 Ω is 500 W and the average power increases by 50% when modulation is applied, find A and m. d) For the cases in part c), find the peak envelope power (PEP).

*Solution.* f̂(t) = cos(2000πt − π/2) = sin(2000πt). The envelope is r(t) = A√((1 + m cos ω_m t)² + (m sin ω_m t)²) = A√(1 + m²)·√(1 + (2m/(1 + m²))cos ω_m t) ≈ A(1 + m cos ω_m t) (m² ≪ 1). The distortion increases with modulation index; with a 0.1% THD criterion, m < 0.126 is required. c) P_c = A²/(2R) = 500 W ⇒ A = 100√5 ≈ 223.6 V; P_t = 500 + m²·500 = 750 W ⇒ m² = 1/2, m = 0.707. d) Unmodulated PEP = 500 W; modulated PEP = 500(1 + m)² ≈ 1457 W.

## Midterm 1, 18 November 2006 (duration 100 min)

1. Examine the performance of envelope detection versus synchronous detection of AM under multipath propagation: the receiver input is x(t) = s(t) + αs(t − τ), α < 1, where s(t) is an AM wave. Write the outputs of the envelope and synchronous detectors; compare the special cases ω_cτ = π/2 and ω_cτ = π.
2. A tone-modulated FM signal with β = 1 and f_m = 200 Hz is applied to an ideal B = 500 Hz BPF centered at f_c. Sketch the line spectrum, phasor diagram, and envelope of the output. (J₀(1) = 0.77; J₁(1) = 0.44.)
3. A DSB-SC modulated signal is demodulated with a coherent detector. a) The effect of a frequency error Δf in the local carrier frequency of the detector; b) for a sinusoidal message, show that this error produces a beat at the error frequency, and sketch the demodulated signal.
4. In the system shown in the figure, the nonlinear elements are half-square-law (v₁ > 0, v₂ > 0; outputs aV₁² and bV₂²). Show that with a suitable choice of K and v(t), AM is produced without output filtering (μ < 1).

## Quiz 3, 19 December 2006 (duration 90 min)

**Question 1.** In superheterodyne TV receivers, if the local oscillator generates a second harmonic, this harmonic can bring the picture content of an unwanted channel into the intermediate frequency band. If the video intermediate-frequency carrier in the receiver is 45.75 MHz, find the channel that causes this kind of interference when the receiver is tuned to a) channel 5, b) channel 6. (A VHF TV channel table is given: channel 2: 55.25; 3: 61.25; 4: 67.25; 5: 77.25; 6: 83.25; 7: 175.25; 8: 181.25; 9: 187.25; 10: 193.25; 11: 199.25; 12: 205.25; 13: 211.25 MHz video carrier.)

**Question 2.** In an FM transmitter with the structure NBFM → ×n₁ → mixer (oscillator at f₂(1 ± δ₂)) → ×n₂ → f_c, the NBFM carrier has frequency f₁(1 ± δ₁); the oscillators are not derived from a common source. a) Find the output carrier frequency in terms of n₁, n₂, f₁, f₂, δ₁, δ₂. b) The largest frequency error at f_c. c) For n₁ = 64, n₂ = 48, f₁ = 0.2 MHz, f₂ = 10.8 MHz, δ₁ = δ₂ = 10⁻⁸, find the largest frequency error and f_c.

*Solution (computed from the question data; the photograph contains only intermediate steps).* f_c = n₂(n₁f₁ − f₂); the error is at most n₂(n₁f₁δ₁ + f₂δ₂). Numerically: f_c = 48(12.8 − 10.8) MHz = 96 MHz; error ≈ 48 × (12.8 + 10.8)×10⁶ × 10⁻⁸ ≈ 11.3 Hz.

**Question 3.** In a double-conversion receiver designed for f_c = 300 MHz with f_IF,1 = 30 MHz and f_IF,2 = 3 MHz, each local oscillator is set to the higher of its two possible values. Inadequate filtering in the RF and first IF stages causes interference from three image frequencies; what are they? (Handwritten intermediate steps: LO₁ = 330 MHz, LO₂ = 33 MHz.)

**Question 4.** In SSB generation by the phase-discrimination method, if the carrier phase shift is actually −90° + δ (δ a small angle error), find approximate expressions for the output x_c(t) and the envelope A(t).

## Final, 12 January 2007 (duration 120 min)

1. A narrowband FM signal s(t) = A_c cos(2πf_ct) − βA_c sin(2πf_ct)sin(2πf_mt). a) The envelope and the maximum/minimum envelope ratio (plot versus β for 0 ≤ β ≤ 0.3); b) the average power as a percentage of the unmodulated carrier power (plot for 0 ≤ β ≤ 0.3); c) by expanding the angle θ_i(t) in a power series, show that for β ≤ 0.3, θ_i(t) = 2πf_ct + β sin(2πf_mt) − (β³/3)sin³(2πf_mt); for β = 0.3, what is the ratio of the third-harmonic power to the fundamental component?
2. For an SSB superheterodyne system with f_LO = f_c + f_IF, show the sideband inversion effect by sketching the spectrum of x_c(t)cos(2πf_LO t).
3. (The following pages of the paper are not in the photograph.)

*Note: For the midterm and final, the photographs contain only the question pages and a few handwritten intermediate steps; the full solutions could not be transcribed.*
