---
baslik: EEM441 Communications I: Communication Theory lecture slides 7–8 (ELK 307, Nihat Kabaoğlu): angle modulation
ozet: Phase and frequency modulation, single-tone and narrowband FM, FM generation, the frequency discriminator, and demodulation with a phase-locked loop.
---

The angle modulation section (Part 5) of the ELK 307 Communication Theory I course: slides for Lectures 7 and 8. The lecture slides belong to the ELK 307 Communication Theory I course and to Nihat Kabaoğlu (the institution is not stated in the document); they were added to this course because they were found in the EEM441 folder. PDF copies of the slides are in the ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes, with the source credited. It will be removed at the request of the rights holder.*

## Lecture 7: Basic definitions, single-tone and narrowband FM

### Contents

Phase-Locked Loop

### Basic Definitions

It is obtained by varying the angle of a carrier signal with the amplitude of the signal m(t). The angle can be varied in two different ways, through frequency or through phase. Therefore, angle modulation is divided into two types, depending on the approach chosen.

θi ( t ) is varied in proportion to the baseband signal m(t). The modulated signal is Note: φc = 0 is assumed.

f i ( t ) is varied linearly in proportion to the baseband signal m(t). The modulated signal is Note: φc = 0 is assumed.

Signal zero crossings are uniform. Signal amplitude is not constant. Signal zero crossings are not uniform. Signal amplitude is constant. An FM signal can be generated with a phase modulator, or a PM signal with a frequency modulator.

### Single-Tone FM

For the analysis of FM signals, the simplest possible case is a single-tone message. Maximum frequency deviation from f c. Note! Δf depends on the amplitude of m(t). f m depends on the amplitude and frequency of m(t).

### Example

A carrier with a frequency of 100 MHz has a peak value of 3 V. A sinusoid with a frequency of 2 kHz modulates the frequency of this carrier, and the maximum deviation in the carrier frequency is 75 kHz. If the value of the modulating signal at t=0 is zero, the expression of the modulated signal is

### Single-Tone FM

Unlike amplitude modulation, FM is a nonlinear modulation. The relationship between the spectrum of an FM signal and m(t) is not simple. The bandwidth of an FM signal is much larger than that of m(t). The spectrum of an FM signal contains a carrier and an infinite number of sidebands placed symmetrically around it. The carrier amplitude of the FM signal is related to the modulation index through J0(β). How do changes in the amplitude and frequency of the modulating sinusoidal signal m(t) affect the spectrum of the FM signal? This must be examined in two separate cases: 1. Frequency constant, amplitude variable 2. Amplitude constant, frequency variable

### Example

In FM, if the amplitude of the modulating signal is doubled and its frequency is halved, the maximum frequency deviation / the spacing between adjacent spectral components, c) decreases/stays the same d) increases/stays the same e) cannot be determined. The carrier signal c (t ) = Ac cos (2π f c t ) is used for both an AM and an FM. Given that the maximum frequency deviation of the FM signal is set to 4 times the bandwidth of the AM signal, what is the modulation index of the FM signal?

### Single-Tone FM

Properties of the Bessel Function

### Narrowband FM

When β  1, the components of the FM spectrum other than J 0 ( β ) and J1 ( β ) are negligible, so the signal consists only of sidebands. In this case, the signal is called narrowband FM. For β  1, only the signal components for n = -1, 0, 1 are significant. The bandwidth is the same as that of

## Lecture 8: FM generation and demodulation

### Contents

Phase-Locked Loop

### Generation of FM Signals

There are two methods for generating FM signals: By applying a narrowband FM signal to the input of a frequency multiplier, a wideband FM signal is obtained indirectly at the multiplier output. The general expression of the FM signal:

Using the identity cos(a+b)= cosa.cosb-sina.sinb, the FM signal can be written as follows: For narrowband FM, when φ ( t ) < 1, approximations can be made. In this way, we can express the narrowband FM signal as follows, or in the following form.

Therefore, a narrowband FM signal can be obtained by modulating the phase of a sinusoidal carrier with the integral of m ( t ). From this narrowband FM signal, it is possible to obtain a wideband FM signal indirectly by increasing the modulation index β. Modulators designed on this principle are called Armstrong FM modulators.

If m ( t ) = Am cos ( 2π f m t ) is chosen, the narrowband FM signal is A frequency multiplier multiplies the instantaneous frequency of the signal at its input by n and passes it to the output. The signal at the output is a wideband FM signal. The value of the factor n is chosen according to the desired value of β.

### Armstrong FM Transmitter

A Typical Armstrong FM Transmitter

Based on the block diagram, let us examine how the calculations in the block diagram are made so that an audio signal m ( t ) with frequency components between fm=50Hz and 15kHz is transmitted within an FM band of ∆f=75kHz at a frequency of fc=91.2MHz. At points 5 and 6, β takes values between. At the phase modulator output (point 2), β1 < 0.5 is required for the signal to be narrowband FM. For the wideband FM signal (at points 5 and 6) to reach the maximum modulation index value, it must be multiplied by n = 1500 0.5 = 3000. This multiplication can be done in two stages ( n = 3000 ≅ 64 × 48 = 3072 ). In this case, the values for the narrowband FM signal at point 2 are found. Multiplying the narrowband FM signal by 3000 raises the carrier frequency from 200kHz to 600MHz. This value is outside the 88-108MHz limits allocated for commercial FM broadcasting. Therefore, frequency multiplication and shifting operations are performed together. The value of f mmin determines the maximum modulation index, and the value of f mmax determines the bandwidth of the FM signal.

### Direct FM Generation

 A method in which the amplitude of the modulating signal directly affects the carrier frequency.  It requires less frequency multiplication than indirect FM systems.  The resonant frequency of a resonant circuit with a high Q factor is varied depending on the amplitude of the modulating signal.  The larger the Q factor, the lower the losses of the resonant circuit and the higher its selectivity.  For a series resonant circuit  For a parallel resonant circuit Q p = R ωc L = ωc RC ωc = 1 LC ⇒ Resonant (carrier) frequency

The capacitance in the resonant circuit C0 is the capacitance when m ( t ) ' is zero. Note: In practice, the VCO is integrated. In the case of C0, the instantaneous frequency, using a power series expansion. This shows that, although the capacitance variation is very small, since the carrier frequency is high, the frequency deviation ∆f reaches the desired values.

### Direct FM Transmitter

Direct FM Transmitter Block Diagram

### Demodulation of FM Signals

 To recover the signal m(t) from the FM signal, the FM signal must be converted into amplitude variations directly proportional to its frequency variations.  The device that converts frequency to voltage is called a discriminator. This device takes the derivative of the phase of the signal applied to its input and passes it to the output.  If the derivative of the FM signal is taken, we obtain. If Ac (t ) is constant, the first term is zero. In practice, a limiter circuit is used to prevent this amplitude from varying with time.

 Since the amplitude of the second term varies in proportion to m(t), this term is not zero in amplitude at all times. In this case, the signal m(t) is obtained with the help of an envelope detector. FM Demodulator Block Diagram

Limiter: A hard limiter and a bandpass filter. Limiter Circuit Characteristic

Differentiator: In practice, the derivative of a signal can be taken in three different ways.  Direct Differentiation  Frequency Domain Differentiation  Time Delay Differentiation. Direct Differentiation Method: Half-Wave Rectifier, Low-Pass Filter. Differentiation is performed using the current-voltage relationship of the capacitor. The capacitor current. If the diode is assumed ideal, during the negative alternations of I ( t ), the current flows through the diode, so ie = 0. During positive alternations, the current passes through the emitter of the transistor, and the emitter current is expressed as follows: Using trigonometric identities, it can be found that ic ( t ) consists of components at baseband and at frequencies fc, 2fc,…. The LPF outputs the baseband and direct-current signals. The capacitor C1 also removes the DC component. As a result, the discriminator output is as follows.

Frequency Domain Differentiation Method: As is known from the properties of the Fourier transform, differentiation in the time domain corresponds to multiplication by jw (or j2π) in the frequency domain. In the frequency band of the FM signal, a system whose transfer function varies linearly with jw can be used for differentiation. For example, the linear region of a resonant circuit has this property.

Balanced Discriminator (Balanced Modulator): By using two slope detectors placed one on top of the other, it is possible to increase the linear region. The balanced discriminator [reduces] the distortion caused by even harmonics and the distortion that would be caused by unwanted amplitude modulation in the FM signal.

In this case, the RL circuit works as a differentiator. Time Delay Differentiation: Time-delay differentiators operate on a principle based on the definition of the derivative. A discriminator operating on this principle is called a time-delay demodulator.

Other Methods Used in the Demodulation of FM Signals: Zero Crossing Detector: The number of zero crossings in an interval is directly proportional to the amplitude of m ( t ) in that interval. Phase-Locked Loop. Phase-Locked Loop. Nonlinear Model of the Phase-Locked Loop

Frequency Demodulator with Feedback. A Typical FM Receiver

*Note: The text was automatically extracted from the slides and edited; equations and figures could not be rendered as text, so the relevant parts have been omitted. For the full version, see the PDF files at the end of the post.*
