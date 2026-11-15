---
baslik: EEM442 Communications II: Quizzes (Pulse Modulations, PCM, Line Codes, TDM-PCM, BPSK, π/4-QPSK) Handwritten Solutions
ozet: Transcription of the handwritten solutions to the EEM442 Communications II quizzes from spring 2017 (Quizzes 1-4): PAM/PDM/PPM sketches and power calculation, PCM quantization, line codes, TDM-PCM bandwidth, BPSK error probability, and π/4-QPSK.
---

These are my handwritten solutions, written after the exams, to the quizzes (Quizzes 1–4) given in the **EEM442 Communications II** course in the spring semester of 2017. They were photographed on 8 June 2017. The questions and solution steps are transcribed below; the photographs have not been published. Because the question texts were reconstructed from the solutions and the note headings, they are brief and inferential; there may be small errors in reading the handwriting.

## Quiz 1: Pulse Modulations (PAM, PDM, PPM)

**Question:** For the message signal x(t) = 2·cos(2πt) V:
- a) Find the Nyquist rate (N.R.),
- b) Sketch the PAM signal with a sampling rate of 10 Hz, pulse duration τ = 20 ms, A = 1 V (sampling at 0.1 s intervals),
- c) Find the PAM power,
- d) Sketch the PDM/PWM for the same sampling rate (τ₀ = 50 ms, t₀ = 15 ms, A = 1),
- e) Find the PDM/PWM power,
- f) Sketch the PPM over the interval 0–0.1 s,
- g) Find the PPM power.

**Solution.**
- a) f_m = 1 Hz ⇒ **N.R. = 2·f_m = 2 Hz**.
- b) C.S.R. (chosen sampling rate) = 10 Hz, T_s = 0.1 s; the sample values at t = 0, 0.1, 0.2, 0.3, 0.4, 0.5, … are 2, 1.62, 0.61, −0.61, −1.62, −2, … (pulses of 0.02 s width start at 0, 0.1, 0.2, … s).
- c) PAM power P = (A²·τ/T_s)·⟨x²(t)⟩, ⟨x²⟩ = 2²/2 = 2 ⇒ P = (1·0.02/0.1)·2 = **0.4 W**.
- d) τ = τ₀ + t₀·x(t) = 50 + 15·x(t) ms: x = 2 → τ = 80 ms; x = 1.62 → τ = 74.3 ms; x = 0.61 → τ = 59.15 ms. In the sketch, the start/end times of the pulses are marked according to these widths, such as 0.08, 0.1, 0.174, 0.2, 0.259 s (the handwriting was not fully legible).
- e) ⟨τ⟩ = τ₀ + t₀·⟨x(t)⟩ = 50 ms (⟨x⟩ = 0); **P = A²·⟨τ⟩/T_s = 1·50 ms/100 ms = 0.5 W**.
- f) PPM: the pulse position (delay) varies with the message: delays d₁, d₂; pulses of constant width τ = 20 ms.
- g) d = τ(t); **P = A²·τ/T_s = 1²·20/100 = 0.2 W**.

## Quiz 2: PCM

**Question:** For the signal x(t) = 3·cos(πt) + 5·cos(5πt) V, sample at the Nyquist rate and quantize with 4 bits (Q = 16); find the PCM code.

**Solution.** The highest frequency is 2.5 Hz ⇒ N.R. = 5 Hz; in the sketch, 2·N.R. = 10 Hz and T_s = 0.1 s are used. Q = 16, n = 4 bits, A_max = 3 + 5 = 8 V, A_min = −8 V ⇒ step size a = (A_max − A_min)/Q = 16/16 = 1 V. Since each sample has n bits, the PCM bit rate is r_b = n·f_s; the bit duration is T_b = T_s/n.

Sample values: t = 0.1 → 2.85 (+0); 0.2 → 2.42 − 5 = −2.58; 0.3 → 1.76; 0.4 → 5.43 (as handwritten); 0.5 → 0; 0.6 → −5.93. Each sample was rounded down to its level and encoded on the 0000 … 1111 code grid (−8 V = 0000, 0 V = 1000, +8 V = 1111); the resulting PCM stream is: **1010 0101 1001 1101 0111 0010**.

*Note: At t = 0.4 s, 3cos(0.4π) + 5cos(2π) = 0.93 + 5 = 5.93 V should be obtained; 5.43 is written on the paper (since the level is 5 in code 1101, the quantization result remains the same).*

## Line Codes and TDM

**Line code sketches.** **Bipolar RZ** is sketched over a bit sequence (1 0 1 0 0 1 0 1 1 0 0 1 1 1 0 1 0 1 1 0 0 1 0 …) (1 → alternating +/− pulse over half the bit duration, 0 → no pulse; "half-bit alternating positive/negative"). Then, for the sequence 1, 0, 1, 1, the following are sketched one by one:
- **Unipolar RZ:** positive only, half-bit pulse;
- **Polar NRZ:** full bit duration; 1 → positive, 0 → negative;
- **Polar RZ:** half bit; 1 positive, 0 negative;
- **Bipolar NRZ:** full bit duration; 1s alternate between positive and negative, 0 → zero level;
- **Bipolar RZ (AMI):** half bit; 1s alternate between positive/negative;
- **Manchester:** the bit duration is divided in two; 1 → first half high, second half low; 0 → first half low, second half high.

**TDM question.** Four message signals (with bandwidths of 10, 15, 20, and 30 kHz) are multiplexed with a commutator, then m₁(t) … m₄(t) are obtained through a PCM encoder (Q = 32), a channel, a PCM decoder, a decommutator, and an LPF in each branch. Solution: f_m (largest signal) = 30 kHz ⇒ f_s ≥ 2·f_m ⇒ **f_s = 60 kHz** (for each channel); 4 channels × 60 kHz = **240 kHz** samples/s; Q = 32 = 2ⁿ ⇒ n = 5 bits ⇒ bit rate 240k × 5 = **1.2 Mbps**.

## Quiz 3: TDM-PCM System and Channel Bandwidth

**Question:** The four channels in the figure (with bandwidths of 45 kHz, 15 kHz, 15 kHz, and 15 kHz) are transmitted by a TDM-PCM communication system (quantizer and encoder Q = 2ⁿ, n = 6). Given that the channel bandwidth is 648 kHz, find the roll-off factor α for the raised-cosine filter.

**Solution.** The 45 kHz channel is counted as 3 channels of 15 kHz ⇒ 6 channels in total. For each, N.R. = 2·15 kHz = 30 kHz. Sample rate r_s = (number of channels) × N.R. = 6 × 30 kHz = 180 kSamples/s; bit rate r_b = n·r_s = 6 × 180 = **1080 kbps**. B.W. = (1 + α)/(2T_b) = (1 + α)·r_b/2 = 648 kHz ⇒ **α = 0.2**.

## Quiz 4: BPSK and π/4-QPSK

**Question 1 (BPSK).** A BPSK signal (s₁(t) = A·cos(ω₀t), s₂(t) = −A·cos(ω₀t), A = 10 mV) in white Gaussian noise with power spectral density N₀ = 10⁻¹¹ is theoretically detected with a matched filter. **What is the maximum bit rate** for the error probability to be less than 8·10⁻⁴?

**Solution.** P_e = Q(√(2E_b/N₀)), E_b = A²·T_b/2 ⇒ P_e = Q(√(A²T_b/N₀)) ≤ 8·10⁻⁴. A = 10⁻² V, N₀ = 10⁻¹¹ ⇒ √(10⁻⁴·T_b/10⁻¹¹) = √(10⁷·T_b); since Q(3.16) ≈ 8·10⁻⁴, 10⁷·T_b ≥ 10 (the paper has "T·10⁷ ≤ 3.16" written, and the final answer found is **r_b ≈ 1 Mbps**).

*Note: For Q(x) ≤ 8·10⁻⁴, x ≥ 3.16 is required; this gives √(10⁷·T_b) ≥ 3.16 ⇒ T_b ≥ 1 µs ⇒ r_b ≤ 1 Mbps. So the direction/scale of the inequality in the intermediate line "T ≤ 3.16·10⁻⁷" on the paper is inconsistent, but the result (1 Mbps) is correct.*

**Question 2 (π/4-QPSK, coherent).**
- a) Draw the block diagram that produces the modulated signal,
- b) find the orthonormal basis functions and the amplitude factors,
- c) draw the constellation diagram,
- d) for the baseband data 10 11 00 10 10 00 10 01, state the symbol phase changes and the transmitted symbols.

**Solution.** b) φ₁(t) = √(2/T) cos(ω_c t), φ₂(t) = √(2/T) sin(ω_c t) (written as √(2/T_b) in the handwriting); the amplitude factors (a, b) ∈ {(√E_b, 0), (0, √E_b), (−√E_b, 0), (0, −√E_b)} and the π/4-rotated set {(±√(E_b/2), ±√(E_b/2))} (an eight-point constellation, alternating between the two QPSK sets). a) Block diagram: baseband → two serial-to-parallel (S/P) converters (even and odd bit branches) → ±√E_b levels for the I and Q branches → multipliers (cos and sin carriers) → summer → x(t); selection between the two symbol sets is made by a switch (2T_b). c) Constellation: four points on the axes (one of the sets) and four points on the diagonals (the π/4-shifted set); radius √E_b. d) The bit pairs are mapped in sequence to the I and Q levels, with different sets for odd and even symbols; the phase changes relative to the previous symbol are written as **135°, 135°, 135°, −45°, −45°, 45°, −135°** (the direction in between is noted as counterclockwise).
