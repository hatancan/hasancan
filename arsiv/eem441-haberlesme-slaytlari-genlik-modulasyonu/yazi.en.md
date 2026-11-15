---
baslik: EEM441 Communications I: Amplitude Modulation Lecture Slides (AM-1 … AM-31)
ozet: 33 pages of scanned lecture slides covering amplitude modulation, DSB-SC, SSB, VSB, the superheterodyne receiver, and frequency-division multiplexing.
---

Scans of the English slide printouts numbered AM-1 through AM-31, distributed in EEM441 Communications I; 33 pages. The pages do not state who prepared the slides. All of the scanned pages are in the PDF at the end of the post; the content below is transcribed into text in page order.

## Continuous-wave (CW) modulation and bandpass systems (AM-1, AM-2)

A communication system transmits an information-bearing signal (baseband) over a channel. Efficient use of the channel requires frequency shifting. Modulation is the systematic variation of a property of one waveform (the carrier) in accordance with another waveform (the message, or modulating signal); modulation is performed at the transmitter and demodulation at the receiver. CW modulation is divided into two types:

- Amplitude modulation (AM): the amplitude of a sinusoidal carrier varies with the message.
- Angle modulation: the phase or frequency of the carrier varies with the message.

Long-distance communication systems operate in the bandpass spectrum. As a rule of thumb, the bandwidth is B ≈ 0.02 fc. Example values: long-wave radio ~100 kHz carrier, 2 kHz bandwidth; short-wave radio 5 MHz, 100 kHz; VHF 100 MHz, 2 MHz; microwave 5 GHz, 100 MHz; optical 5·10¹⁴ Hz, 10¹³ Hz.

## Amplitude modulation (AM-3 … AM-8)

The AM wave has the form s(t) = Ac [1 + ka m(t)] cos(2π fc t); ka is the amplitude sensitivity of the modulator. The envelope has the same shape as the baseband signal, provided that |ka m(t)| < 1 (that is, 1 + ka m(t) > 0). Otherwise overmodulation occurs: phase reversals of the carrier and envelope distortion take place. Percentage modulation = 100 × max|ka m(t)|. In addition, fc ≫ W must hold (W: message bandwidth).

For single-tone modulation, m(t) = Am cos(2π fm t), μ = ka Am (modulation index):

s(t) = Ac cos(2π fc t) + ½ μ Ac cos[2π(fc + fm)t] + ½ μ Ac cos[2π(fc − fm)t].

Power distribution (across a 1 Ω resistor): carrier power Ac²/2, upper sideband power μ²Ac²/8, lower sideband power μ²Ac²/8; the ratio of total sideband power to total power is μ²/(2 + μ²).

**Switching modulator.** The diode circuit acts like an ideal switch. With v1(t) = Ac cos(2π fc t) + m(t), |m(t)| ≪ Ac, v2(t) alternates between v1 and zero at rate fc; v2(t) = [Ac cos(2π fc t) + m(t)] gτ(t), and the Fourier expansion of the periodic pulse train gτ(t) is 1/2 + (2/π) Σ (−1)^(n−1)/(2n−1) cos[2π(2n−1)fc t]. With fc ≥ 2W, a bandpass filter centered at fc with bandwidth 2W yields the AM wave: v2(t) ≈ Ac [1 + (4/πAc) m(t)] cos(2π fc t) + unwanted components.

**Nonlinear effects (example).** For an element with input m(t) + Ac cos(2π fc t) and input–output relation y(t) = a1 x + a2 x², a bandpass filter centered at fc ± W at the output yields the AM signal. The modulation index is found as μ = 2a₂/a₁ · Am, and the filter conditions are given by inequalities such as fc > 3W.

**Envelope detector (demodulator).** It operates with a diode, an R-C load, and low-pass behavior. For successful demodulation: the charging time constant of the capacitor must be small relative to the carrier period, while the discharge time constant must be larger than the carrier period and smaller than the period of the message: (rf + Rs)C ≪ 1/fc and 1/fc ≪ Rℓ C ≪ 1/W.

**Limitations of AM.** AM wastes power by transmitting the carrier and wastes bandwidth by transmitting both sidebands (BT = 2W). These are overcome by DSB-SC (carrier suppressed), VSB (one sideband in full, a vestige of the other), and SSB (single sideband, carrier suppressed) modulation, respectively; in return the receiver becomes more complex.

## Double-sideband suppressed-carrier modulation, DSB-SC (AM-9 … AM-13)

s(t) = Ac cos(2π fc t) m(t), S(f) = ½ Ac [M(f − fc) + M(f + fc)]. The envelope is the absolute value of the message; phase reversals occur at its zero crossings. The bandwidth is the same as for AM (2W), but no carrier power is wasted. In a comparison at equal peak envelope power, DSB-SC is more efficient for a fixed peak transmitter power.

**Ring modulator.** A four-diode ring; it is multiplied by the square wave c(t), and the output is s(t) = m(t) c(t). While the outer diodes conduct, the inner diodes are cut off, and vice versa. c(t) = (4/π) Σ ((−1)^(n−1)/(2n−1)) cos[2π(2n−1) fc t]; a bandpass filter selects the region around fc (fc ≫ W, m(t) band-limited).

**Coherent (synchronous) demodulation.** v(t) = Ac' cos(2π fc t + φ) s(t); after the low-pass filter, v0(t) = ½ Ac Ac' m(t) cos φ. The output is largest when the phase error φ = 0 and zero when φ = π/2 (quadrature null effect). If φ varies randomly, distortion results; the local oscillator must be synchronous with the carrier (in both frequency and phase).

**Costas receiver.** A practical synchronous receiver: the local oscillator frequency is set to the previously known fc. The I (in-phase) and Q (quadrature-phase) channel outputs form a feedback system. For small φ, the I channel ≈ ½ Ac m(t) and the Q channel ≈ ½ Ac m(t) φ; the two are multiplied and applied to the VCO, and the phase error is corrected automatically. The sign of φ is used to automatically correct the local phase error.

**Quadrature-carrier multiplexing (QAM).** Two DSB-SC signals sharing the same bandwidth: s(t) = Ac m1(t) cos(2π fc t) + Ac m2(t) sin(2π fc t). At the receiver, the in-phase and quadrature-phase demodulator branches separate the two messages; it is a bandwidth-conserving scheme, and a Costas receiver or a pilot signal can be used for synchronization.

## Filtering of sidebands, VSB (AM-14 … AM-20)

A single sideband (SSB) or vestigial sideband (VSB) signal is obtained from a DSB-SC signal by the frequency-discrimination method: the output of the product modulator u(t) = Ac m(t) cos(2π fc t) is passed through a filter H(f): S(f) = U(f) H(f) = (Ac/2) [M(f − fc) + M(f + fc)] H(f). For distortionless recovery in a coherent detector, H(f − fc) + H(f + fc) = constant (−W ≤ f ≤ W) must hold; the VSB filter satisfies this condition through sideband symmetry in the transition band.

Phase-discrimination method (block diagram): s(t) = sI(t) cos(2π fc t) − sQ(t) sin(2π fc t), with sI(t) = ½ Ac m(t) and sQ(t) = ½ Ac m'(t), where m'(t) is the second component that depends on the filter H(f). The in-phase component is independent of the choice of filter; H(f) affects only sQ(t), and the role of sQ(t) is to reduce or eliminate the power of one sideband.

VSB transmits one sideband and a trace (vestige) of the other sideband; the aim is to reduce the transmission bandwidth. For a VSB signal, s(t) = ½ Ac m(t) cos(2π fc t) ± ½ Ac m'(t) sin(2π fc t).

**Television signals.** The video signal is wideband and carries significant low-frequency content. The demodulation circuit at the receiver must be simple and inexpensive; for this reason an envelope detector is appropriate and a carrier is added to the VSB signal. The VSB shaping filter is applied at the receiver; since sideband filtering at the transmitter would be expensive at high power levels, it is done on the receiver side. In commercial TV broadcasting, the VSB width is approximately 0.75 MHz.

**Distortion with an envelope detector (VSB + carrier).** For s(t) = Ac [1 + ½ ka m(t)] cos(2π fc t) − ½ ka Ac m'(t) sin(2π fc t), the envelope is a(t) = Ac {[1 + ½ ka m(t)]² + [½ ka m'(t)]²}^(1/2). The distortion is due to m'(t). It is reduced in two ways: by reducing the percentage modulation (ka); and by increasing the sideband width of the VSB.

## Single sideband, SSB (AM-21 … AM-24)

To generate SSB, the message spectrum must have an energy gap around the origin; speech signals satisfy this property. For SSB containing the upper sideband, H(f − fc) + H(f + fc) = 1 (−W ≤ f ≤ W) and Ha(f) = −j sgn(f) (quadrature filter, Hilbert transformer). The time-domain expression:

- Upper sideband: s(t) = ½ Ac m(t) cos(2π fc t) − ½ Ac m̂(t) sin(2π fc t)
- Lower sideband: s(t) = ½ Ac m(t) cos(2π fc t) + ½ Ac m̂(t) sin(2π fc t)

In a two-stage SSB modulator, the required frequency separation is more easily achieved; crystal resonators can be used to meet the filters' transition-band requirements.

**SSB demodulation.** A product modulator and a low-pass filter. With a frequency error Δf and a phase error Δφ: with perfect synchronization, v0(t) = ¼ Ac Ac' m(t); for Δf = 0, Δφ ≠ 0, phase distortion results (tolerable for speech, not for data); for Δf ≠ 0, spectral shift and distortion result, and for speech a small shift is acceptable. Spectrum inversion (scrambling) is used in secure speech systems.

## Frequency translation and the superheterodyne receiver (AM-25 … AM-27)

Frequency translation (mixing, heterodyning) is the shifting of the spectrum of a modulated signal to a new carrier frequency; it is done for amplification or other processing. The mixer consists of a product modulator and a bandpass filter. For up-conversion, fℓo = fc + fb is chosen, or for down-conversion, fℓo = fc − fb.

**Example: satellite transponder.** Uplink 6 GHz, downlink 4 GHz: different carriers are used to prevent self-oscillation in a high-gain environment. The frequency converter shifts the amplified uplink spectrum to the downlink passband: 6 − 2 = 4 GHz (local oscillator 2 GHz), and 6 + 2 = 8 GHz is filtered out.

**Superheterodyne AM receiver (550–1600 kHz band).** RF amplifier and mixer, local oscillator (ganged tuning), intermediate-frequency (IF) amplifier with fIF = 455 kHz, bandwidth BIF = 10 kHz, envelope detector, and audio amplifier. fℓo = fc + fIF. After the mixer, interference can occur between the desired signal and the image frequency (fi = fc + 2fIF); image frequencies must be filtered out in the RF section. Image band: 550 + 910 = 1460 to 1600 + 910 = 2510 kHz.

**Example: image rejection in a superheterodyne radio.** A receiver with fc = 1.6–2.6 MHz, BT = 6 kHz; strong unwanted signals around 14–15 MHz and 3.0–5.6 MHz. (A) For fℓo = fc + fIF, the image frequency fi = fc + 2fIF must be made ≥ 5.6 MHz, so fIF ≥ 2 MHz; fℓo = 3.6–4.6 MHz and the local oscillator tuning ratio is ≈ 1.3; the fractional IF bandwidth is about 0.003. (B) For fℓo = fc − fIF, fIF = 0.6 MHz and the tuning ratio is ≈ 2.

## Frequency-division multiplexing, FDM (AM-28 … AM-30)

Multiplexing is the combining of many independent signals into a composite signal to be transmitted over a common channel. Speech signals of 300–3400 Hz must be separated so that they do not interfere with one another; the separation can be done in frequency (FDM) or in time (TDM). In FDM, the most commonly used modulation is SSB, which occupies the least bandwidth.

Telephone hierarchy: the basic group is 12 SSB (lower sideband) channels, each 4 kHz; the supergroup is 5 groups (60 voice channels); the master group; the jumbo group. Forming groups is done for economic reasons.

**Example: demultiplexing.** In the composite signal s(t) = m1(t) cos(2π f1 t) + m2(t) cos(2π f2 t), if m1 and m2 have bandwidths W1 and W2, each channel is separated with a bandpass filter + coherent demodulator + low-pass filter. To avoid interference, f2 − W2 > f1 + W1 (or f2 − f1 > W1 + W2) must hold. Question: what is the difference between multiplexing and demultiplexing?

## Comparison of AM systems (AM-31)

1. AM: two sidebands and the carrier are transmitted; demodulation with an envelope or square-law detector; used in commercial broadcasting.
2. DSB-SC: requires much less transmitter power; cheaper transmitter than AM, more complex receiver; suitable for point-to-point communication.
3. SSB: lowest transmitter power and lowest bandwidth; preferred for long-distance transmission of speech signals over cable; an example of quadrature modulation.
4. VSB: requires a bandwidth between that of SSB and DSB-SC; bandwidth saving is important for signals with large bandwidths, such as TV and wideband data.

*Note: Some of the scanned pages contain small handwritten annotations; only the printed slide content is given in the post. The post summarizes the presentation notes of the time in text form; refer to the page scans for the figures and diagrams.*

*This content belongs to slides distributed as part of the course; since it was distributed without attribution of its source, it is shared for archival and nostalgic purposes. It will be removed at the request of the rights holder.*
