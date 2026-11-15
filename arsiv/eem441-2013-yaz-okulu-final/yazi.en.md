---
baslik: EEM441 Communications I: Summer School Final Exam (14 August 2013) and Solutions
ozet: Başkent University EEM 441 summer school final: FDM channel filter, FM tone spectrum and phasor, VSB envelope and phase, AM envelope sketches; with handwritten solutions.
---

The summer school final exam of the Başkent University EEM 441 Communication Systems I course dated 14 August 2013 (duration 110 minutes) and its handwritten solutions. The exam paper and solutions were transcribed to text from photographed pages; the photographs have not been published. For this reason, there is no downloadable original file. Personal information (student number, name) has been removed. The three additional photographs in the same folder are repeats of the same pages.

## Questions

1. In a telephone exchange, voice channels are separated at the receiver by bandpass filters with transfer function |H(f)| = 1/√(1 + [2(f − f₀)/B]^(2n)). Assuming that the components of the baseband voice signal outside 300 < |f| < 3300 Hz are negligible, sketch the spectra of three adjacent channels in the group spectrum. Taking |H(f)| ≤ 0.1 outside the desired passband, calculate B, f₀ and n.
2. A tone-modulated FM signal with modulation index β = 2 and a highest information-signal component of f_m = 200 Hz is applied to a BPF with a bandwidth of 750 Hz centered at frequency f_c. Sketch the frequency spectrum and the phasor diagram of the FM signal; calculate the envelope of the output signal and sketch its graph.
3. Unit-amplitude video signals are transmitted using DSB-SC modulation. Sketch the phasor diagram for the tone-modulated DSB-SC signal. If the width of the lower sideband is reduced by half, calculate the envelope A(t) and the phase angle φ(t) of the DSB-SC modulated signal by sketching the phasor diagram.
4. a) Amplitude modulation is performed with the information signal m(t) = cos(2π f_m t) u(t), taking f_m ≪ f_c. For the cases where the modulation is DSB and AM with μ < 1 and μ > 1, sketch the envelopes on the modulated signals; indicate the amplitude values. b) Repeat the same question for the information signal m(t) = 0.5 u(t) − 1.5 u(t − T), taking T ≫ 1/f_c.

A Bessel functions formula sheet was also provided with the exam (graphs of J_n(β); J_n(β) = (−1)ⁿ J₋ₙ(β); for β → 0, J_n ≈ βⁿ/(2ⁿ n!); ΣJ_n² = 1; FM s(t) = A_c Σ J_n(β) cos[2π(f_c + n f_m)t]; SSB s(t) = (A_c/2) m(t) cos ω_c t ∓ (A_c/2) m̂(t) sin ω_c t).

## Solution 1: Channel filter

Each channel is single-sideband (SSB subcarrier): the voice band is 300–3300 Hz, and the carrier line lies below the band. In the figure, adjacent subcarriers are at f_i − 4, f_i, f_i + 4 kHz (4 kHz spacing); below each channel's 3 kHz band a 0.3 kHz gap is left, and a 0.7 kHz gap between it and the second channel (band between f_i − 3.3 kHz and f_i − 0.3 kHz).

Let f_i be the i-th subcarrier. Take B = 3 kHz, and the filter center becomes f₀ = f_i − 0.3 kHz − B/2 = f_i − 1.8 kHz. Required: |H(f)|² ≤ 0.01 for |f − f₀| ≥ B/2 + 1 kHz = 1.5 + 1 = 2.5 kHz.

|H|² = 1/(1 + [2(2.5)/3]^(2n)) ≤ 0.01 ⇒ (5/3)^(2n) ≥ 99 ⇒ 2n log₁₀(5/3) ≥ log₁₀ 99. Since log₁₀(5/3) = 0.222, n × 0.444 ≥ 2 and n ≥ 4.5, that is, n = 5.

Result: B = 3 kHz, f₀ = f_i − 1.8 kHz, n = 5.

## Solution 2: Single-tone FM, BPF output

The solution on the paper was worked with the values tone frequency f_m = 4 kHz and β = 2 (J₀(2) ≈ 0.22, J₁(2) ≈ 0.58); the BPF passes the carrier and the first sidebands (B ≈ 8500 Hz).

- Spectrum: 0.22 A_c at f_c; +0.58 A_c at f_c + 4000 Hz; −0.58 A_c at f_c − 4000 Hz.
- Phasor diagram: the 0.22 A_c horizontal carrier phasor; two 0.58 A_c phasors rotating at ±ω_m t are added to it. Since the sideband phasors are in opposite directions, their sum is 2 × 0.58 = 1.16 A_c with a vertical component.
- Envelope: A_min = 0.22 A_c; A_max = √(0.22² + 1.16²) A_c ≈ 1.18 A_c. A(t) is a curve with period 1/f_m that varies between 0.22 A_c and 1.18 A_c.

*Note: The numerical values on the solution sheet (f_m = 4 kHz, B = 8500 Hz) do not agree with those on the question paper (f_m = 200 Hz, BPF 750 Hz); the solution was written with a different set of values, but the method is the same.*

## Solution 3: DSB-SC and signal with attenuated lower sideband (VSB)

Tone-modulated DSB-SC: x_c(t) = (A_c/2) cos(ω_c − ω_m)t + (A_c/2) cos(ω_c + ω_m)t. In the phasor diagram, two A_c/2 phasors rotate in opposite directions at ±ω_m t; the resultant lies along the horizontal axis with A(t) = A_c cos ω_m t.

Reducing the lower sideband by half (its amplitude to A_c/4): lower sideband phasor is A_c/4, upper sideband phasor is A_c/2.

- V_I = (A_c/2) cos ω_m t + (A_c/4) cos ω_m t = (3/4) A_c cos ω_m t
- V_Q = (A_c/2) sin ω_m t − (A_c/4) sin ω_m t = (A_c/4) sin ω_m t
- A(t) = [(3/4 A_c cos ω_m t)² + (A_c/4 sin ω_m t)²]^½ = (A_c/4) √(9cos²ω_m t + sin²ω_m t) = (A_c/4) √(8cos²ω_m t + 1) = (A_c/4) √(5 + 4cos 2ω_m t)
- φ(t) = arctan[(A_c/4) sin ω_m t / (3A_c/4 cos ω_m t)] = arctan(tan ω_m t / 3)

## Solution 4: AM and DSB envelopes

a) m(t) = cos(2π f_m t) u(t): a signal that jumps to 1 at t = 0, then oscillates like a sinusoid.

- DSB: the carrier amplitude is multiplied by m(t); it starts from A_c at t = 0, the envelope has the shape |cos|, and as m(t) changes sign the carrier reverses phase.
- AM, μ < 1: envelope A_c[1 + μ m(t)]; for t < 0 the amplitude is A_c, for t > 0 it varies between A_c(1 ± μ); the envelope never drops to zero, with no phase reversal.
- AM, μ > 1: the envelope goes negative; at the zero crossings a phase reversal (overmodulation) occurs and the envelope is distorted.

b) m(t) = 0.5 u(t) − 1.5 u(t − T): 0.5 in the interval 0 < t < T, and −1 (0.5 − 1.5) for t > T.

- DSB: amplitude 0.5 A_c between 0 and T, and A_c after T (and the phase rotates by 180°).
- AM, μ < 1: A_c(1 + 0.5μ) between 0 and T, and A_c(1 − μ) after T (the envelope shrinks, the phase is the same); A_c for t < 0.
- AM, μ > 1: since 1 − μ is negative after T, the carrier reverses phase and the envelope is |1 − μ| A_c; A_c(1 + 0.5μ) between 0 and T.
