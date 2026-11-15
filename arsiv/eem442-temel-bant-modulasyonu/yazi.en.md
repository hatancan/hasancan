---
baslik: EEM442 Communications II: Baseband Modulation (PAM, PDM/PWM, PPM, PCM, Line Codes, Delta Modulation)
ozet: Presentations 02 and 03 of the EEM442 Communications II course (Spring 2017): sampling and Nyquist, bandpass sampling, natural and flat-top sampling, pulse modulations, PCM, quantization SNR, line codes, mu-law and A-law, delta modulation.
---

Two presentations from the **EEM 442 Communications II** course taught at Başkent University in the spring semester of 2017: *02 – Baseband Modulation (PAM-PDM-PPM)* and *03 – Baseband Modulation (PCM-DM)* (28 March 2017). The slides are in English and the explanations here are in English as well; the formulas are faithful to the slide content, and the figures on the slides have been described in text. I am confirming the course name from the file names and the slide title (the folder says "Haberleşme II", the presentation title says "EEM 442 Communications II"). The author of the presentations is not stated in the files (they are the course instructor's own presentations). The originals of both presentations can be downloaded as a ZIP at the end of the post.

## 02 – Baseband modulation: sampling and pulse modulations

### Ideal sampling

The message m(t) is multiplied by the impulse train p(t) = Σδ(t − kT_s): m_s(t) = m(t)·p(t) (impulse sampling); the sample values are m_s[k] = m_s(t)|_{t = kT_s} (point sampling). In the frequency domain, multiplication becomes convolution: M_s(f) = M(f) * P(f), P(f) = (1/T_s)·Σδ(f − n/T_s) and

M_s(f) = (1/T_s)·Σ M(f − n/T_s),

that is, the message spectrum is repeated at intervals of f_s.

**Aliasing and the Nyquist criterion:** when f_s − f_m < f_m, aliasing occurs in the frequency domain; to avoid aliasing, **f_s ≥ 2·f_m** must hold (Nyquist criterion).

*Example:* Find the minimum sampling rate for the following signals: a) x(t) = sinc(6000t), b) x(t) = rect(3000t), c) x(t) = cos(2π·10⁴t) + sin(2π·10⁵t).

### Bandpass sampling

- Simple case f_H = k·B: if k is odd, F_s = 2B (f_H = 3B, 5B, …); if k is even, F_s = 2B as well (f_H = 6B, …).
- General case f_H ≠ k·B: (k − 1)F_s ≤ 2F_L and 2F_H ≤ k·F_s, that is, 2F_H/k ≤ F_s ≤ 2F_L/(k − 1); k_max ≤ F_H/B. A graph is given for choosing F_s.
- Practical approach: with n = ⌊(2f_c − B)/B⌋ = ⌊2f_L/B⌋, (2f_c − B)/n ≥ f_s ≥ (2f_c + B)/(n + 1), that is, 2f_L/n ≥ f_s ≥ 2f_H/(n + 1).
- *Examples:* (a) a signal in the band −100…−75 and 75…100 MHz; (b) minimum sampling rate for x(t) = sinc(600t)·cos(2π·20·10³t).

### Natural sampling

s(t) = Σ c_n·e^{j2πnf_s t} = c_0 + Σ c_n·cos(2πnf_s t); c_n = (τ/T_s)·sinc(nτ/T_s). For x_s(t) = x(t)·s(t), X_s(f) = c_0·X(f) + Σ c_n·X(f − nf_s) + Σ c_n·X(f + nf_s): the spectrum is copied to multiples of f_s with weights c_n.

*Example:* If x(t) = 10000·sinc(2000t) is sampled at the Nyquist rate, the spectrum of the sampled signal has the form above, with c_n = (τ/T_s)·sinc(nτ/T_s), τ/T_s = 0.1: (a) find the Nyquist rate, (b) sketch the spectrum of the signal sampled at the Nyquist rate, (c) sketch the spectrum when a 50 Hz guard band is used.

### Sample-and-hold (flat-top) sampling and pulse modulations

- **PAM (pulse amplitude modulation):** the sampling impulses are modulated by x(t); the pulse amplitude corresponds to the sample value, and the pulse width τ is constant. Average power P_avg = (A²·τ/T_s)·⟨x²(t)⟩.
- **PDM/PWM (pulse duration/width modulation):** the pulse duration varies with the message, τ(t) = τ_0 + t_0·x(t) (τ_3 > τ_2 > τ_1); P_avg = (A²/T_s)·⟨τ(t)⟩.
- **PPM (pulse position modulation):** the pulse has constant amplitude and width, and its position (delay d) varies with the message; P_avg = A²·τ/T_s = A²·τ·f_s.

## 03 – PCM and delta modulation

### Pulse code modulation (PCM)

**Quantization:** the number of levels is Q = 2ⁿ (n: number of bits); the step size is a = (A_max − A_min)/Q. Example: 8-level, 3-bit quantization (000 … 111); the PCM output is the sequence of level codes at the sampling instants, one after another (example: PCM = 111101010110).

**Quantization distortion:** e(t) = x(t) − x_q(t); if e is uniformly distributed, ⟨e²⟩ = ∫ e²·P_e(e) de = a²/12. SNR = ⟨x²(t)⟩/⟨e²(t)⟩. For x(t) = A·cos(2πft) and a = 2A/2ⁿ, since ⟨x²⟩ = A²/2,

**SNR = (3/2)·2^{2n}**, **SNR_dB = 10·log10((3/2)·2^{2n}) = 1.76 + 6.02n.**

Dynamic range and SNR: SNR = 1.76 + 6.02n; (S/N)_q = 10·log10(3Q²). *Example:* A digitization system specifies a 55 dB dynamic range; how many bits are required, and what are the system's SNR and (S/N)_q?

**Time-division multiplexing (TDM):** multiple messages are sampled in turn by a switch (commutator) and sent over a single PCM channel (an example problem is given).

### Line codes

| Code | Rule | Advantages | Disadvantages |
|---|---|---|---|
| **Unipolar NRZ** | 1 → +V, 0 → 0 | simple implementation, low bandwidth | DC level, low-frequency components, no error correction, difficult synchronization |
| **Unipolar RZ** | 1 → +V for half a bit, then 0 | simple, spectral line at the symbol rate | DC level, low-frequency components, no error correction, twice the bandwidth of unipolar NRZ |
| **Polar NRZ** | 1 → +V, 0 → −V | simple, no DC component | no error correction, difficult synchronization |
| **Polar RZ** | 1 → +V for half a bit, 0 → −V for half a bit | simple, no DC | no error correction, twice the bandwidth of polar NRZ |
| **Bipolar (AMI)** | 0 → no pulse; 1 → alternating +V and −V (three levels: +V, 0, −V) | no DC, less bandwidth than unipolar and polar NRZ, error detection capability | difficult synchronization |
| **Manchester** | bit period is split in two; 0 → first half +, second half −; 1 → first half −, second half + | no DC, easy synchronization | requires very wide bandwidth, no error detection |

The slides also show the power spectral densities of the line codes and a comparison table.

### Non-uniform quantization and companding

Uniform and non-uniform quantization are compared; non-uniform quantization is implemented with a compressor + uniform quantizer + expander. Two standards:
- **µ-law**: has a larger dynamic range; distortion is worse for small signals; used in North America and Japan.
- **A-law**: common in Europe.

### Delta modulation (DM)

Encodes by sending the sign (1 bit) of the difference between two consecutive samples; the block diagram consists of a comparator, a sampler, and an integrator in the feedback path. Problems: **slope overload**, when the signal changes faster than the step size; **granular noise**, when the step is too large for a slowly varying signal. For the laboratory application of these topics, see "Communications laboratory: quantization, µ-law, delta modulation".
