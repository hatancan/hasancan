---
baslik: EEM441 Communications I: Communications Laboratory Handouts (Fırat University and Other Sources)
ozet: AM/FM laboratory handouts: Fırat University amplitude and frequency modulation experiment, AM modulation/demodulation experiment with the MC1496, and an introduction to the oscilloscope.
---

Three supplementary laboratory documents in the EEM441 folder: the Fırat University Faculty of Engineering, Department of Electrical and Electronics Engineering, Communications Laboratory Experiment 1 handout (amplitude and frequency modulation), an "Experiment 2: AM modulation/demodulation" handout whose source is not stated in the document, and a "What is an oscilloscope?" text with no stated source. The original PDFs are in the ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*

## Fırat University, Experiment 1: Amplitude and Frequency Modulation

The handout defines modulation as the process of converting the message signal into a form suitable for transmission, and states that the modulation type is chosen according to noise, bandwidth, and transmitter power. Amplitude modulation is covered in three types:

1. Full amplitude modulation (FAM)
2. Double-sideband suppressed-carrier amplitude modulation (DSBSC AM)
3. Single-sideband amplitude modulation (SSB AM)

For each type, the definition, mathematical expression, and spectrum are given (sections 2.1 – 2.3). Experiments: 2.4 the presence of side frequencies (the receiver's 10.7 MHz IF filter and sidebands), 2.5 double-sideband suppressed-carrier signals of radio broadcasts (shortwave receiver and oscilloscope channels); the cases of 2 kHz and 1 kHz message signals are examined separately. Section 3 defines frequency modulation (3.1), gives the general principles for FM (3.2), and describes the FM experiment with the generator and receiver modules; the experiment set operates with a ±15 V power supply, and a triangular wave is observed on the oscilloscope.

## Experiment 2: AM Modulation and Demodulation

**Objective:** to carry out the theoretical calculations related to amplitude modulation and demodulation; to examine the basic concepts by implementing a modulator and a demodulator.

**Materials:** oscilloscope, +12 V / −8 V power supply, two signal generators, one MC1496 (LM1496) IC, 51 kΩ, 680 Ω, 3.9 kΩ, 1 kΩ, 6.9 kΩ, 11.5 kΩ, and 10 kΩ resistors, 50 kΩ potentiometer, 1 nF and 100 nF capacitors, 1N4148 diode.

**Background.** Converting a baseband signal into a form suitable for transmission is called modulation; after modulation, the information is shifted to a high band and the antenna size is reduced (example: for a 3 kHz tone, an antenna of 1/10 wavelength would be about 10 km long). Carrier AM: sAM(t) = (1 + ma m(t)) Ac cos(ωc t + φ) = Ac cos(ωc t + φ) + Ac ma m(t) cos(ωc t + φ). If the modulation index ma is exceeded, overmodulation occurs and the information cannot be recovered at the receiver without distortion. In the single-tone case, s(t) = Ac cos(ωc t) + (Ac Am ma/2) cos((ωc + ωm)t) + (Ac Am ma/2) cos((ωc − ωm)t); to avoid overlap, fc ≥ 2 fm, and the required bandwidth is B = 2 fm. The envelope detector consists of a nonlinear rectifier and a low-pass filter; the output is of the form y(t) = g c0 (1 + ma m(t)), so the information signal is obtained with a gain and a DC offset.

**Procedure.**

1. The circuit in Figure 1 is built; before applying voltage, the −8 V, +12 V, and ground connections are checked.
2. A 500 kHz, 1 V peak-to-peak sine wave is applied to the modulator carrier input.
3. Information signal: 200 Hz, 0.4 V peak-to-peak sine wave.
4. The modulated signal is observed at pin 6 of the IC, sketched, and the modulation index is calculated.
5. The potentiometer resistance is varied, the change in the output is observed, and the cause is explained.
6. The signals for ma < 1, ma = 1, and ma > 1 are sketched.
7. The demodulator in Figure 2 is built and the modulator output is fed to its input; the information signal and the demodulator output are compared on the oscilloscope.

## What is an oscilloscope?

A device that displays electrical quantities (voltage, frequency, current, phase difference) as luminous lines. It consists of a cathode ray tube (screen, CRT), vertical deflection, horizontal deflection, and an acceleration circuit. When the filament at the back of the tube is heated, it emits electrons; the electrons pass through the electron lens and the accelerating electrode, between the deflection plates, and reach the screen, whose inner surface is coated with phosphor. The document covers the basic concepts at an introductory level, the structure of the oscilloscope, and how to operate it.

*Note: For the detailed experiment steps and figures of the Fırat University handout, see the PDF in the ZIP; only the main headings are summarized here.*
