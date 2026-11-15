---
baslik: EEM441 Communications I: Worked Study Problems on AM, SSB and FM
ozet: Handwritten worked study problems for EEM441 Communications I covering AM demodulation, the square-law device, envelope detection, SSB and an FM multiplier chain, transcribed into text.
---

Handwritten worked AM, SSB and FM study problems prepared for EEM 441 Communications I. The source is scanned pages (the problem statements and solutions are a student's handwriting); the pages are not published, and the content has been transcribed into text. The solutions are summarized as they appear in the source. It contains no personal information.

## 1. Product Modulator and Amplitude-Modulated Signal (Quiz 1)

For a 80% modulated AM signal with the message f(t) = 12cos(2π·3×10³t) V, the carrier amplitude is A_c = A_m/m = 12/0.8 = 15 V. If A_c < 12 V, then m > 1: overmodulation occurs, producing phase reversal and envelope distortion. For f_c = 30 kHz, f_AM(t) = 15cos(2π·30k·t) + 6cos(2π·27k·t) + 6cos(2π·33k·t), the bandwidth is 6 kHz; in 50 Ω, the carrier power is 2.25 W and the total sideband power is 0.72 W. (The same question also appeared in the July 2009 quiz; the note at the top of the page, "it came up for us in Quiz 3", indicates that this question was repeated later in another exam.)

*Note: The scanned solution also found a sideband amplitude of 72 V and a power of 103.68–109.68 W; this is an error caused by not normalizing the message in the product m·f(t).*

## 2. AM Demodulator with Interfering Carrier

The AM signal A_c[1 + μx(t)]cos ω_ct is added to an unwanted interfering carrier x_i(t) = A_i cos(ω_c + Δω)t, multiplied by cos(ω_ct + φ), and passed through a low-pass filter (ω_c band) (Δf < W). The output is:

V_o(t) = (A_c/2)[1 + μx(t)]cos φ + (A_i/2)cos(Δωt − φ).

To recover the message undistorted, φ ≠ ±π/2 (cos φ ≠ 0) and Δω = 0 are required; in this case V_o = (A_c/2)(1 + μx)cos φ and the interference component becomes a constant DC term.

## 3. Filter and Multiplication by cos 4πt

s(t) passes through the filter H(f) (H = 3, |f| ≤ 2 Hz; 0 otherwise), and is then multiplied by cos 4πt; S(f) is triangular (peak 4, |f| ≤ 4 Hz). For W(f) = S(f)H(f) and r(t) = w(t)cos 4πt, R(f) = ½W(f − 2) + ½W(f + 2): the sum of two half-amplitude copies of W(f), which occupies −2…2 Hz, shifted to ±2 Hz, lying in the range −4…4 Hz.

## 4. Squarer – Low-Pass Filter – Square-Root Device

s(t) = A_c[1 + k_am(t)]cos 2πf_ct, |k_am(t)| < 1, f_c > 2W. V₁ = s² = A_c²[1 + k_am]²cos²(2πf_ct) = (A_c²/2)[1 + 2k_am + k_a²m²][1 + cos 4πf_ct]. The low-pass filter rejects the 4πf_ct component: V₂ = (A_c²/2)[1 + k_am(t)]². Taking the square root gives V₃ = (A_c/√2)[1 + k_am(t)], i.e., m(t) is recovered.

## 5. Envelope Detector and SSB with Carrier (2003 Midterm Question)

s(t) = A_c cos 2πf_ct + m(t)cos 2πf_ct − m̂(t)sin 2πf_ct is an SSB signal with carrier. Envelope: a(t) = √([A_c + m(t)]² + m̂²(t)) = √(A_c² + 2A_cm(t) + m²(t) + m̂²(t)). When A_c ≫ |m(t)|, a(t) ≈ A_c + m(t); the envelope detector recovers the message to a good approximation (the distortion decreases as A_c increases).

## 6. Square-Law Device: y = 6x + 4x²

x(t) = m(t) + cos ω_ct (m has zero mean, and the minimum value of x(t) is M); y(t) = 6x(t) + 4x²(t) = 2 + 6m + 4m² + 6cos ω_ct + 8m cos ω_ct + 2cos 2ω_ct. a) Spectrum: 2δ(f), 6M(f), 4M(f)*M(f) (low frequency), 3δ(f ∓ f_c) and 4M(f ∓ f_c) (around f_c), δ(f ∓ 2f_c). b) For AM, a BPF centered at f_c with bandwidth > 2W is required; f_c − W > 2W, i.e., f_c > 3W must hold. c) g(t) = 6cos ω_ct + 8m(t)cos ω_ct = 6[1 + (4/3)m(t)]cos ω_ct; the modulation index is μ = (4/3)·max|m|, and max x = 1 + max m = M ⇒ for μ = 0.1, M = 1.075 (computed from the problem data).

## 7. FM Multiplier Chain

For A_c = 50 V, A_m = 20 V, K = 2356, ω_c = 2π·200 kHz, ω_m = 2π·15 kHz, β = KA_m/ω_m = 0.5: f₁(t) = 50cos(2π·200·10³t + 0.5 sin(2π·15·10³t)) is a narrowband FM signal (B = 2f_m = 30 kHz). The chain ×64 → mixer (f₀ = 20cos(2π·10 900·10³t)) → BPF (1885–1915 kHz) → ×48: f₅(t) = 100cos(2π·91 200·10³t + 1536 sin(2π·15·10³t)), and the maximum power in 50 Ω is 100²/(4·50) = 50 W. For the detailed solution, see the 2014 Quiz 2 post.

## 8. SSB with Carrier (300 kHz, A_c = 100)

For the SSB signal modulating a 300 kHz carrier (A_c = 100) with x(t) = cos 2000πt + 2sin 2000πt: a) x̂(t) = sin 2000πt − 2cos 2000πt. b) SSB: x_c(t) = (A_c/2)[x(t)cos 2πf_ct ± x̂(t)sin 2πf_ct]; for the lower sideband, x_c(t) = (A_c/2)[cos(ω_c − ω_m)t − 2 sin(ω_c − ω_m)t]. c) Spectrum: X_c(f) = (A_c/4)[(1 + j2)δ(f − f_c + f_m) + (1 − j2)δ(f + f_c − f_m)]; the line magnitude is (A_c/4)√5 ≈ 55.9, at f_c − f_m = 299 kHz.

*Note: Since the last pages of the worksheet are missing, Problem 8 could only be transcribed as far as shown above.*
