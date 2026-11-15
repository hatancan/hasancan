---
baslik: EEM441 Communications I: 2013 Summer School Midterm Exam (2 August 2013) and Solutions
ozet: Başkent University EEM 441 Communication Systems I summer school midterm exam: SSB envelope receiver, envelope and phase of a bandpass signal, FM spectrum, and frequency multiplier design; with handwritten solutions.
---

Midterm exam of the Başkent University Department of Electrical and Electronics Engineering course EEM 441 Communication Systems I, summer school, dated 2 August 2013 (duration 2 hours). The exam paper, the Bessel function formula sheet distributed with the exam, and the handwritten solutions are transcribed below. The exam paper and solutions were transcribed from photographed pages; the photographs have not been published. For this reason, there is no downloadable original file. Personal information (student number, name) has been removed.

## Questions

1. In an SSB receiver system, the signal A_LO cos(ω_c t) is added to the tone-modulated SSB signal and the sum is applied to the input of an envelope detector circuit. Assume that there is no frequency error in the local oscillator, only a phase error φ′. Taking A_LO ≫ A_c A_m, calculate the signal at the envelope detector output and draw the phasor diagram. (Figure: s(t) SSB → adder (+ A_LO cos(ω_c t + φ′)) → envelope detector → A(t).)
2. In a bandpass communication system, let the in-phase component of the signal at the transmitter output be s_i(t), the quadrature component s_q(t), the envelope A(t) and the phase φ(t). For the signal s_bp(t) = s₁(t) cos(ω_c − 3ω₀)t + s₂(t) cos(ω_c + 3ω₀)t, calculate these using the phasor diagram.
3. In a radio transmitter, the parameters of the FM-modulated signal are taken as f_m = 20 kHz, β = 1, A_c = 100, f_c = 40 kHz. Derive the formula for s(t), draw the frequency spectrum, show that S_T > A_c²/2, and calculate the bandwidth of the system.
4. An FM radio transmitter with f_c ≫ f_m is designed with parameters f_m = 4 kHz, β = 3, f_c1 = 100 kHz, Δf₁ = 16.5 Hz and f_c = 10 MHz. The frequency multiplier system consists only of triplers; all bandpass filters satisfy the condition 0.01 < B/f_c < 0.1. Calculate all Δf and f_LO values, the filter bandwidths and center frequencies, and draw the system diagram; place the frequency down-converter so that no frequency exceeds 13.5 MHz.

## Bessel function formula sheet

The sheet distributed with the exam contains graphs of the first-kind Bessel functions J_n(β) (n = 0…4, β = 0…18) and the following relations:

- J_n(β) = (1/2π) ∫ exp[j(β sin x − n x)] dx (−π…π)
- J_n(β) = (−1)ⁿ J₋ₙ(β)
- For β → 0, J_n(β) ≈ βⁿ / (2ⁿ n!); J₀ → 1, J₁ → β/2, J₂ → β²/8
- For β → ∞, J_n(β) ≈ √(2/(πβ)) cos(β − π/4 − nπ/2)
- Σ J_n²(β) = 1 (n = −∞…∞)
- J_n(jβ) = jⁿ I_n(β), I_n(β) = (1/2π) ∫ exp[β cos θ] cos(nθ) dθ
- s(t) = A_c Re[Σ J_n(β) exp(j2π(f_c + n f_m)t)] = A_c Σ J_n(β) cos[2π(f_c + n f_m)t]
- SSB: s(t) = (A_c/2) m(t) cos ω_c t ∓ (A_c/2) m̂(t) sin ω_c t
- FM: s(t) = A_c cos[2π f_c t + β sin(2π f_m t)]

## Solution 1: Adding a carrier to the SSB signal

Tone-modulated SSB: s(t) = (A_c/2)(A_m cos ω_m t) cos ω_c t ∓ (A_c/2)(A_m sin ω_m t) sin ω_c t; here x(t) = A_m cos ω_m t, x̂(t) = A_m sin ω_m t. This is a single line at f_c ± f_m with amplitude a = ½ A_c A_m. A_LO cos(ω_c t + φ′) is added at the adder. In the phasor diagram, the A_LO phasor is at angle φ′; the phasor of amplitude a rotating at ±ω_m t is added to it, and the resultant is A(t).

A²(t) = (A_LO cos φ′ + a cos ω_m t)² + (A_LO sin φ′ ± a sin ω_m t)²
= A_LO² + a² + 2 A_LO a (cos ω_m t cos φ′ ± sin ω_m t sin φ′)
= A_LO² + a² + 2 A_LO a cos(ω_m t ∓ φ′)

A(t) = A_LO [1 + (a/A_LO)² + (2a/A_LO) cos(ω_m t ∓ φ′)]^½ ≈ A_LO + ½ A_c A_m cos(ω_m t ∓ φ′).

That is, when A_LO ≫ a, the envelope detector output is a DC term plus ½ A_c A_m cos(ω_m t ∓ φ′): the information signal is recovered, carrying only a phase shift of φ′ (a delay, not distortion).

## Solution 2: Envelope and phase of a bandpass signal

The solution on the paper writes the two components with a shift of ω₀ (worked with ω₀ in the source):

- v_i(t) = [v₁(t) + v₂(t)] cos ω₀ t
- v_q(t) = [v₂(t) − v₁(t)] sin ω₀ t
- A(t) = √(v₁²(t) + 2 v₁(t) v₂(t) cos 2ω₀ t + v₂²(t))
- φ(t) = arctan{[v₂(t) − v₁(t)] sin ω₀ t / ([v₁(t) + v₂(t)] cos ω₀ t)}

In the phasor diagram, v₁ and v₂ are two phasors rotating in opposite directions with ω₀ t; when v₁ ≫ v₂, A(t) ≈ v₁(t) + v₂(t) cos 2ω₀ t and φ(t) ≈ −ω₀ t.

*Note: In the exam paper the shift is written as 3ω₀, whereas the solution sheet works with ω₀; the expressions in the solution should be read with 3ω₀ substituted for ω₀ according to the question. In the approximate A(t) expression on the paper, the factor in the second term is illegible; it is written here as v₂(t).*

## Solution 3: FM, β = 1, f_m = 20 kHz, A_c = 100, f_c = 40 kHz

s(t) = A_c cos[2π f_c t + β sin 2π f_m t] = 100 cos[2π·40·10³ t + 1·sin(2π·20·10³ t)].

a) Instantaneous frequency: f_i(t) = (1/2π) dθ_i/dt = f_c + β f_m cos ω_m t = 40 + 20 cos ω_m t kHz.

b) Bessel table J_n(1): J₀ = 0.7652 (≈ 0.77), J₁ = 0.4401 (≈ 0.44), J₂ = 0.1149 (≈ 0.11), J₃ = 0.0196 (≈ 0.02), J₄ ≈ 0.

Line amplitudes A_c J_n: n = 0 → 77 (40 kHz), n = 1 → 44 (60 kHz), n = 2 → 11 (80 kHz), n = 3 → 2 (100 kHz). Lower sidebands: n = −1 → −44 (20 kHz), n = −2 → +11 (0 Hz, i.e. DC), n = −3 → −2 (−20 kHz). The component falling at negative frequency folds over to 20 kHz: −44 − 2 = −46. The folded components are at |f_c − 3f_m| = 20 kHz and |f_c − 2f_m| = 0.

Total power (DC component 11² and AC components ½ amplitude²): S_T = 11² + ½[(−46)² + 77² + 44² + 11² + 2²] ≈ 5170 > A_c²/2 = 100²/2 = 5000. Because the folded (aliased) components are added to the total power, S_T comes out larger than the true signal power A_c²/2; this is the inequality shown on the paper. From the spectrum, the bandwidth is read as 2·3·f_m = 120 kHz.

*Note: In the source table, J₃(1) is written as "0.196 ≈ 0.2"; the correct value is 0.0196 (consistent with the line amplitude 100×0.0196 ≈ 2). On the paper there is a correction note for the bandwidth reading "read 100 kHz instead of 120 kHz"; by Carson's rule B ≈ 2(β + 1)f_m = 80 kHz, and since lines up to the 3rd sideband were included in the calculation, 120 kHz is written.*

## Solution 4: Frequency multiplier chain

n = 3⁶ = 729, Δf = β f_m = 3×4 kHz = 12 kHz. Initial deviation Δf₀ = Δf/n = 12 kHz / 729 = 16.461 Hz (close to the given 16.5 Hz; n = 12 kHz/16.5 Hz ≈ 727 → 729 = 3⁶).

Filter condition: B_Tk ≤ B_k < (5/3)f_ck − (1/3)f_ck = (4/3) f_ck; that is, 10 B_k ≤ f_ck ≤ 100 B_k. For B/f_c = 0.1, at f_c = 300 kHz, B = 30 kHz, and B_k = 15 kHz is taken.

| k | Δf_k | β_k = Δf_k/f_m | B_Tk | f_ck | B_k |
|---|---|---|---|---|---|
| 0 | 16.461 Hz | ≪ 1 | 8 kHz | 100 kHz | — |
| 1 | 49.383 Hz (3×Δf₀) | 0.0123 ≪ 1 | 8 kHz | 300 kHz | 15 kHz |
| 2 | 148.15 Hz (3²×Δf₀) | 0.037 ≪ 1 | 8 kHz | 900 kHz | 45 (≈ 50) kHz |
| 3 | 444.45 Hz (3³×Δf₀) | 0.11 | ≈ 9 kHz | 2.7 MHz | 135 (≈ 140) kHz |
| 4 | 1333.4 Hz (3⁴×Δf₀) | 0.33 | ≈ 13 kHz | 8.1 MHz | 405 (≈ 400) kHz |
| 5 | 4000.2 Hz (3⁵×Δf₀) | 1.0 | 20 kHz | 3.333 MHz | 166 (≈ 150) kHz |
| 6 | 12 kHz (3⁶×Δf₀) | 3.0 | 40 kHz | 10 MHz | 500 kHz |

After the fourth multiplier, f_c4 = 8.1 MHz; since one more tripler would give 24.3 MHz and exceed the 13.5 MHz limit, a frequency down-converter is placed between the 4th and 5th multipliers: f_LO = 8.1 MHz − 10 MHz/(3×3) = 8.1 − 1.111 = 6.988 MHz. After the mixer, the BPF output is at 1.111 MHz; then two triplers (5 and 6) give 3.333 MHz and 10 MHz.

System diagram: m(t) → narrowband FM (f_c0 = 100 kHz, β₀ = 16.461/4000 = 0.004 ≪ 1, B_T0 = 2f_m = 8 kHz) → ×3 → ×3 → ×3 → ×3 (8.1 MHz) → mixer (f_LO = 6.988 MHz) → BPF (1.111 MHz) → ×3 → ×3 → output f_c = 10 MHz, Δf = 12 kHz, β = 3. Output bandwidth B_T6 = 2f_m(1 + β) = 2×4×(1 + 3) = 32 kHz ≈ 40 kHz.
