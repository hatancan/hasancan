---
baslik: EEM441 Communications I: EEM442 Communications II Exams from 2009 and 2010 (Questions and Solutions)
ozet: The EEM442 Communications II final exam of 25 May 2009, the midterm of 3 August 2010, and the final exam of 14 August 2010: TFM, PCM, matched filter, timing error, and ternary signal questions.
---

Başkent University EEM 442 Communications II final exam of 25 May 2009, midterm of 3 August 2010, and final exam of 14 August 2010. The sources are phone photographs of the exam papers and handwritten solutions (since they were kept in the EEM441 folder, they appear here under EEM441); the content was transcribed to text from the photographed pages, and the photographs were not published. The solutions were read from a friend's handwritten notes; personal information was removed.

## Final exam, 25 May 2009 (duration 2 hours)

1. An analog speech signal band-limited to W = 4000 Hz will first be transmitted as binary PCM and then through an M-PAM modulator; the signal-to-quantization-noise power ratio must be higher than 50 dB. a) Block diagram of the transmitter, b) minimum number of bits and the actual value of the ratio, c) required sampling frequency and data rate, d) if bipolar NRZ with a pulse duration of 62.5 µs is used, the transmission bandwidth and symbol rate (bandwidth between f = 0 and the first null of the PSD), e) the value of M, f) spectral efficiency.
2. Coherent BPSK over an AWGN channel at a rate of 100 kbit/s with P_b = 10⁻³ is required. With a passband channel bandwidth of 50 kHz, an α = 1 raised cosine filter, and Gray bit mapping: a) M, b) the E_s/N₀ that achieves P_b, c) E_b/N₀.
3. Ternary signal configuration: s₋₁, s₀, s₁ are at −d, 0, d volts at the receiver; p(s₀) = 0.5 and p(s₁) = p(s₋₁) = 0.25. The error probability and decision regions of the optimum receiver (AWGN).
4. A system with transmit filter h_t(t), channel h_c(t), and receiver matched filter h_r(t); α = 0.2 square-root raised cosine filters are used, and the channel transfer function is also given. (The remainder of the question is cut off in the photograph.)

The formula section of the exam paper gives the following: P_b = p₁Q((A − λ)/σ) + (1 − p₁)Q((A + λ)/σ); Q(3.09023) = 10⁻³; Q(√20) = 3.87×10⁻⁶; B_T = (R_b/2)(1 + α); SNR₀ = 3·2²ᴺ/α (α = peak power/average power); P(s₁→s₂) = Q(d₁₂/√(2N₀)); P_b = Q(√((E_b/N₀)(1 − ρ))); P_s = 2Q(√(2E_s/N₀)·sin(π/M)); P_E(M) = (2(M−1)/M)Q(√(6E_s,avg/((M²−1)N₀))). The 16-PAM line driver question for this exam's question 4 (10 dBm average power, 30 dBm peak power, 12 Msymbol/s) appears on a separate page; the same question was also asked in the 2011 final.

## Midterm exam, 3 August 2010 (duration 2 hours)

**Question 1.** In a tamed frequency modulation (TFM) transmitter, the pre-modulation filter consists of a delay line with branches delayed by T, 0, and −T with coefficients 1/4, 1/2, 1/4, followed by a low-pass filter H₀(f) = πfT/sin(πfT), 0 ≤ |f| ≤ 1/(2T), and it feeds a VCO. Find the impulse response and the overall transfer function of the pre-modulation filter.

*Solution.* h(t) = (1/4)h₀(t − T) + (1/2)h₀(t) + (1/4)h₀(t + T). H(f) = [(1/4)e^(−jωT) + 1/2 + (1/4)e^(jωT)]H₀(f) = (1/2 + (1/2)cos ωT)H₀(f) = cos²(πfT)·H₀(f) = (πfT/sin(πfT))·cos²(πfT), 0 ≤ |f| ≤ 1/(2T); 0 elsewhere.

**Question 2.** A speech signal band-limited to W = 4000 Hz will be transmitted using binary PCM + M-PAM, SNR₀ > 50 dB. a) Transmitter block diagram, b) bits/sample and actual SNR, c) minimum sampling rate and bit rate, d) bipolar NRZ, pulse duration 62.5 µs: transmission bandwidth and symbol rate, e) M, f) spectral efficiency.

*Solution.* SNR₀ = 3L² > 10⁵ ⇒ L ≥ 182, L = 2ᴿ ⇒ R = 8, L = 256, actual SNR₀ = 3·256² ≈ 1.97×10⁵ ≈ 53 dB. f_s ≥ 8 kHz, R_b = 8 × 8 = 64 kbit/s. T_s = 62.5 µs ⇒ R_s = 16 ksymbol/s, B = 1/T_s = 16 kHz. k = R_b/R_s = 4 ⇒ M = 16. Spectral efficiency R_b/B = 4 bit/s/Hz. Block diagram: sampler (f_s ≥ 8 kHz) → quantizer (L = 256) → encoder (R = 8) → M-PAM modulator.

**Question 3.** In a binary system, s(t) (energy E) is sent for 1 and −s(t)/2 for 0, 0 ≤ t ≤ T; the two symbols are equiprobable, AWGN, two-sided power spectral density N₀/2. a) Block diagram of the receiver with matched filter; show that the signal level at the sampling instant is αE (α = 1 or −1/2) and the noise variance is EN₀/2. b) Decision rule and optimum threshold. c) Transmission error probability. d) Are s(t) and −s(t)/2 a good choice, and how can the error probability be reduced?

*Solution.* The receiver consists of a filter h(t) = s(T − t), a sampler at time T, and a comparator with threshold λ. y(T) = αE + n, σ² = EN₀/2. λ_opt = (E − E/2)/2 = E/4. P_e = Q((λ + E/2)/σ) = Q((3/4)√(2E/N₀)). Since the average energy is low, the error probability is high; if s₀ = −s(t) is chosen, λ = 0 and P_e = Q(√(2E/N₀)) is smaller, but the average transmitted power increases.

**Question 4.** In a narrowband (ISI-free) system, a symbol r(t) of duration T is received with L + 1 samples (r_k, k = 0…L), and the impulse response of the matched filter also has L + 1 samples (h_k). a) For h(t) = r(T − t), show that the matched filter output sampled at t = T is Z = Σ h_k r_(L−k). b) Representation of the discrete-time matched filter as a transversal FIR filter and its block diagram. c) If the filter samples are matched to the input samples, find Z in terms of r_k.

*Solution.* Taking T = LΔ, τ = kΔ gives Z = z(LΔ) = Σ r(kΔ)h(LΔ − kΔ) = Σ r_k h_(L−k) = Σ h_k r_(L−k). FIR filter: z⁻¹ delay line, h₀…h_L coefficient multipliers, and an adder. If h_k = r*_(L−k) is chosen, Z = Σ|r_k|², i.e., the energy of the signal.

## Final exam, 14 August 2010 (duration 2 hours)

1. In a telemetry system, eight message signals, each with a bandwidth of 2 kHz, are time-division multiplexed as binary uniformly quantized PCM. The error in the sample amplitude must not exceed 1% of the peak amplitude; if α = 0.2 raised cosine pulses are used, what is the minimum required transmission bandwidth? The sampling rate must be at least 20% above the Nyquist rate.
2. A timing synchronization error pT (0 ≤ p ≤ 1) in a coherent BPSK demodulator: the symbol starts and ends late by pT. a) Find the bit error probability as a function of p. b) For E_b/N₀ = 9.6 dB and p = 0.2, by what factor does the error probability increase? c) If the timing error cannot be eliminated, by how many dB must E_b/N₀ increase to return to the p = 0 error probability?
3. For x(t) band-limited to W, x(t) = Σ x_n·sin[2πW(t − n/2W)]/[2πW(t − n/2W)]. a) X(f) for x₋₁ = −1, x₀ = 2, x₁ = −1 (others 0). b) If these samples are transmitted by a binary system, the levels received at the sampling instants and their probabilities (bits equiprobable).
4. Ternary signal configuration: s₋₁, s₀, s₁ are at −d, 0, d at the receiver; p(s₀) = 0.5, p(s₁) = p(s₋₁) = 0.25. The error probability and decision regions of the optimum receiver (AWGN). Useful formula: for raised cosine, W = (1/2T)(1 + α) (baseband), (1/T)(1 + α) (passband).

*Summary of solutions (2, 3, 4).*

2. If a bit and the bit following it have opposite signs, the correlator output is √E_b(1 − 2p); if they have the same sign, it is √E_b; hence P_b = ½Q(√(2E_b/N₀)) + ½Q(√(2E_b/N₀)·(1 − 2p)). At E_b/N₀ = 9.6 dB, for p = 0, P_b = Q(4.27) ≈ 10⁻⁵; for p = 0.2, P_b ≈ 2.6×10⁻³ (about 260 times). To obtain P_b = 10⁻⁵ again at p = 0.2, trial and error gives E_b/N₀ = 23.56 (13.7 dB); that is, an increase of 13.7 − 9.6 = 4.1 dB is required.
3. x(t) = 2·sinc₀(t) − sinc(t + 1/2W) − sinc(t − 1/2W) and, using sinc(2Wt) ↔ (1/2W)Π(f/2W), X(f) = (1/2W)[2 − e^(−jπf/W) − e^(jπf/W)] = (1/W)[1 − cos(πf/W)] = (2/W)sin²(πf/2W), |f| ≤ W. The received levels are B_n = 2I_n − I_(n−1) − I_(n+1), I_n = ±1: B_n = 0 (probability 1/4), ±2 (1/4 each), ±4 (1/8 each).
4. MAP rule: λ = d/2 − (σ²/d)ln[p(s₁)/p(s₀)] = d/2 + (N₀/2d)ln 2. Decision regions: r < −λ ⇒ s₋₁; |r| < λ ⇒ s₀; r > λ ⇒ s₁. P_e = Q(λ/σ) + ½Q((d − λ)/σ) + ½Q((d + λ)/σ); for λ = d/2, P_e = (3/2)Q(d/2σ) + ½Q(3d/2σ).

*Note: Since no solution was found in the photographs for question 1 of the 14 August 2010 exam, only the question was transcribed. The same ternary signal question also appeared in the 2009 and 2013 exams.*
