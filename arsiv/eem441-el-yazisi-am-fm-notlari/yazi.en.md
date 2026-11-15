---
baslik: EEM441 Communications I: Handwritten Lecture Notes – AM, DSB-SC, SSB and FM
ozet: Frequency and phase error in coherent demodulation, frequency modulation, the narrowband FM approximation, and a formula summary for AM/DSB-SC/SSB/FM; transcribed to text from photographed handwritten notes.
---

Two separate sets of handwritten notes taken by classmates (21 photos) were transcribed to text from the photographed pages; personal information was removed. The photos themselves have not been published. Some of the notes are written on squared notebook paper (coherent demodulation and FM derivations), and some as single-page formula summaries (AM, DSB-SC, SSB, FM).

## Formula summary: AM, DSB-SC, SSB and FM

**AM.** s(t) = Ac (1 + ka m(t)) cos(ωc t), ωc = 2π fc. If |ka m(t)| < 1 (i.e., 1 + ka m(t) > 0), the envelope is not distorted (no overlap); if ka m(t) > 1, the envelope crosses over (overmodulation). Spectrum: S(f) = (Ac/2)[δ(f − fc) + δ(f + fc)] + ka (Ac/2)[M(f − fc) + M(f + fc)]. The carrier power is Ac²/2; for μ = ka Am, the upper sideband power is μ²Ac²/8 and the lower sideband power is μ²Ac²/8. For a single tone, s(t) = Ac (1 + μ cos ωm t) cos ωc t; the bandwidth is BW = 2 fm. Reading from the envelope: Ac = (Amax + Amin)/2, μ = (Amax − Amin)/(Amax + Amin).

**DSB-SC.** s(t) = Ac cos ωc t · m(t); S(f) = ½ Ac [M(f − fc) + M(f + fc)]. In a coherent detector, with v(t) = Ac cos(ωc t + φ) s(t): v(t) is maximum when φ = 0 and minimum when φ = π/2. Quadrature-carrier multiplexing: s(t) = Ac cos ωc t m1(t) + Ac sin ωc t m2(t); the sum of two DSB-SC signals with a 90° phase difference. Vestigial sideband: s(t) = ½ Ac cos ωc t m(t) + ½ Ac m'(t) sin ωc t.

**SSB.** s(t) = (Ac/2) m(t) cos ωc t ∓ (Ac/2) m̂(t) sin ωc t; m̂(t) is the Hilbert transform of the message (for m(t) = Am cos ωm t, m̂(t) = Am sin ωm t).

**FM.** s(t) = Ac cos(ωc t + 2π kf ∫ m(t)dt); for a single tone, s(t) = Ac cos(ωc t + β sin ωm t), β = Δf/fm. β ≫ 1 is wideband, β ≪ 1 is narrowband. Deviation ratio D = Δf/W, W = fm. Instantaneous frequency fi(t) = fc + kf Am cos ωm t and kf Am = Δf = β fm. Spectrum: for β ≪ 1, J0(β) and J1(β) are significant; for β ≫ 1, n_max is found from the condition Jn(β) > 0.01.

## Frequency and phase error in coherent demodulation

The signal c(t) = f(t) cos ω0 t is multiplied by the local oscillator cos[(ω0 + Δω)t + θ] (followed by a low-pass filter, LPF):

c1(t) = f(t) cos ω0 t · cos[(ω0 + Δω)t + θ] = ½ f(t) [cos((2ω0 + Δω)t + θ) + cos(Δω t + θ)].

The output after the LPF is e0(t) = ½ f(t) cos(Δω t + θ). Cases:

- If Δω = 0, θ = 0, then e0(t) = ½ f(t): no distortion at all.
- If Δω = 0, θ ≠ 0, then e0(t) = ½ f(t) cos θ = k f(t): unless θ varies with time, only the amplitude is reduced or increased. θ should be kept as constant as possible and θ ≠ 90°; if θ = π/2, then e0(t) = 0. If θ varies with time (θ(t)), the output is distorted in a way that requires attention.
- If Δω ≠ 0, θ = 0, then e0(t) = ½ f(t) cos(Δω t): there is serious distortion (the envelope of the output oscillates according to Δω t). In the spectrum, E0(ω) = ¼ [F(ω − Δω) + F(ω + Δω)]; if Δω is small, the two copies are very close to each other.

If a single-sideband (SSB) signal c(t) = f(t) cos ω0 t − f̂(t) sin ω0 t is demodulated in the same way, the LPF output is e0(t) = ½ f(t) cos(Δω t + θ) + ½ f̂(t) sin(Δω t + θ). For Δω = 0, θ = 0, e0 = ½ f(t) (the information signal); for Δω = 0, θ ≠ 0, e0 = (f(t)/2) cos θ + (f̂(t)/2) sin θ: for upper or lower SSB, θ yields a mixture of f(t) and its Hilbert transform (phase distortion).

## Frequency modulation

With amplitude A and angle θ(t), c(t) = A cos θ(t); the instantaneous angular frequency is ωa(t) = dθ(t)/dt. The angle of the carrier varies with the message; in these notes the instantaneous frequency is used.

- c(t) = A cos θ(t) = A cos(ω0 t + θ0 + k f(t)): phase (angle) modulation.
- c(t) = A cos[ω0 t + k ∫ f(t) dt]: frequency modulation; ωa(t) = ω0 + k f(t), Δω ≈ k |f(t)|max.

Example: for f(t) = a cos ωm t, ωa(t) = ω0 + k a cos ωm t, Δω = k a and c(t) = A cos[ω0 t + (k a/ωm) sin ωm t] = A cos[ω0 t + (Δω/ωm) sin ωm t]. The modulation index is β = Δω/ωm. For β ≪ π/2, narrowband FM: cos(β sin ωm t) ≈ 1, sin(β sin ωm t) ≈ β sin ωm t and

c(t) ≈ A [cos ω0 t − β sin ω0 t sin ωm t] = A [cos ω0 t − (β/2) cos(ω0 − ωm)t + (β/2) cos(ω0 + ωm)t].

Numerical check (condition β ≪ 1.57 rad/s): for β = 0.2, cos β = 0.9801 ≈ 1 and sin β = 0.19867 ≈ 0.2; for β = 0.5, cos β = 0.8776 ≈ 1.0 and sin β = 0.4794 ≈ 0.5.

A better approximation using a series expansion (cos Q = 1 − Q²/2! + Q⁴/4! − …, sin Q = Q − Q³/3! + …) is obtained by increasing β somewhat: cos(β sin ωm t) ≈ 1 − (β sin ωm t)²/2 and sin(β sin ωm t) ≈ β sin ωm t. The result is

c(t) = (1 − β²/4) cos ω0 t + (β²/8) cos(ω0 − 2ωm)t + (β²/8) cos(ω0 + 2ωm)t − (β/2) cos(ω0 − ωm)t + (β/2) cos(ω0 + ωm)t,

valid for β ≪ 1. In the spectrum, lines with amplitudes π(1 − β²/4) at ω0, ±πβ/2 at ω0 ± ωm, and πβ²/8 at ω0 ± 2ωm are seen; in this approximation the bandwidth is 4ωm (shown in the drawing on the board). In narrowband FM the sidebands lie on either side of the carrier, whereas in the wideband case the actual FM signal is written as c(t) = cos ω0 t − kg(t) sin ω0 t: here g(t) = ∫ f(t)dt, and when k g(t) ≪ π/2 rad/s, cos[k ∫ f dt] ≈ 1 and sin[k ∫ f dt] ≈ k g(t). The sidebands resemble the form of g(t); in AM the sidebands are proportional to f(t). In narrowband FM the bandwidth is twice the highest frequency of g(t), and the highest frequency components of f(t) and g(t) are the same.

*Note: The squared-notebook pages were photographed in poor light, so some equations were ambiguous; the unclear parts were written in a way consistent with the standard FM/AM derivations, and since the photos are not published, verification exists only in the private archive.*
