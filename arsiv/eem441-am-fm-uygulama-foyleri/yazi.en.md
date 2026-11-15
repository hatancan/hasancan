---
baslik: EEM441 Communications I: AM and FM Lab Handouts
ozet: AM and FM experiments on the ANACOM sets: preliminary work, measurement points, the superheterodyne receiver, demodulation, and noise experiments.
---

Başkent University's **EEM441 Communications I** course has two lab handouts that describe amplitude modulation (AM) and frequency modulation (FM) experiments. The author and date are not stated. PDF copies of the handouts can be downloaded as a ZIP at the end of this post.

## Lab 1: Amplitude Modulation

The aim is to study amplitude modulation in practice, and to reinforce the theoretical topics by working on the experiment set with the transmitter and receiver operations.

### Preliminary work

1. For the square wave in the figure, plot the double-sideband AM signal with carrier, using a carrier of f_c = 1 MHz, in the time and frequency domains; perform the MATLAB simulation.
1. For the same message, obtain the double-sideband suppressed-carrier (DSB-SC) AM signal in the time and frequency domains.
1. Research the properties of the superheterodyne receiver and other receiver types.
1. Research the present-day areas of use of amplitude modulation.

The square wave has levels of +1 and −1, and the unit of the horizontal axis is ms. The positive interval is shown as 0–3 ms and the negative interval as 3–6 ms; the signal is periodic.

### Transmitter and receiver

The ANACOM 1/1 transmitter can perform DSB and SSB AM. The audio oscillator provides the modulating signal. The balanced modulator suppresses the carrier. The signal amplified by the output amplifier can be transferred to the receiver by cable or broadcast from the antenna.

The ANACOM 1/2 receiver is a superheterodyne. It has a diode detector for DSB with carrier and a product detector for SSB. The detector output is connected to the audio amplifier and the loudspeaker.

### Measurements at the transmitter

1. Select a tone from the audio oscillator and feed it to the AM DSB modulator. Record the t.p.1 and t.p.9 signals.
1. Using t.p.1 as the trigger signal, display t.p.3. Examine whether the signal is double-sideband AM; test the Balance knob.
1. From the V_max and V_min values of the envelope, find the modulation percentage: m = [(V_max − V_min)/(V_max + V_min)] × 100%.
1. Record the changes at t.p.3 by varying the amplitude and frequency of the tone.

### Transmitter settings

- The audio amplifier amplitude control, the balanced modulator/band-pass filter balance control, and the output amplifier gain must be at maximum.
- The mode switch must be at DSB and the Tx output at ANT.
- The loudspeaker must be on, and the antenna must be fully extended and upright.

### Receiver settings

- The Rx input must be at ANT. and the RF tuning circuit at INT.
- The RF amplifier gain must be at maximum; AGC must be enabled.
- The detector switch must be at Diode.
- The audio amplifier amplitude must be near minimum and the loudspeaker on.
- The Beat Frequency Oscillator must be off; the antenna must be extended and upright.

### Measurements at the receiver

1. Find the transmitted station using the tuning dial.
1. Observe the RF amplifier output with an AC-coupled oscilloscope.
1. The mixer multiplies the local oscillator sinusoid by the RF signal. The local oscillator frequency is 455 kHz above the RF carrier. Calculate the components in the output spectrum: f_LO = f_AM + f_IF, f_IF = 455 kHz.
1. Examine t.p.20 with AC coupling; observe the change in the fundamental component as the frequency setting is varied.
1. Examine the outputs of the IF amplifiers at t.p.24 and t.p.28.
1. Plot the output of the diode detector at t.p.31.
1. Examine the output of the audio amplifier at t.p.39 and prepare the report.

## Lab 2: Frequency Modulation

The aim is to study frequency modulation in practice.

### Preliminary work

1. Explain the operation of the VCO, i.e. the voltage-controlled oscillator, with a figure.
1. Compare the differences between FM and AM.
1. Implement FM in MATLAB with your own code. Choose the message and the carrier, and write their values on the plot.
1. Examine the block diagram of the experiment set.

The handout reminds students to bring a calculator to the experiment. The set includes the following blocks: audio oscillator, reactance and varactor modulators, mixer/amplifier, amplitude limiter, tuned resonant circuit, Foster–Seeley/ratio detector, quadrature detector, PLL detector, and low-pass filter/amplifier.

### FM modulation

1. Connect the audio oscillator output to the modulator input.
1. Set the Reactance–Varactor switch to the Reactance position.
1. Set the Carrier Frequency control to the middle position.
1. Select an audio signal and examine the Mixer/Amplifier output at t.p.34. Set the audio amplitude to minimum; measure the amplitude and frequency of the FM carrier that is seen.
1. Set the audio amplitude to maximum. Observing 10–15 periods on the screen, record how the oscillations change. Discuss the effect of the message amplitude on the FM and how this effect can be observed better.

### FM detection and demodulation

1. Connect a 1 V_pp sinusoid of about 455 kHz to the input of the tuned resonant circuit. Take the external trigger from the input and observe the output.
1. Vary the frequency around 455 kHz and find the maximum of the DC level at t.p.40. Also measure at 435 and 475 kHz, and plot the output voltage versus input frequency.
1. Make all connections except the amplitude limiter. At t.p.40, examine whether there is a positive DC level, a sinusoid similar to the one at t.p.14, and a small-amplitude high-frequency ripple.
1. Compare t.p.73 with t.p.40. Vary the amplitude and frequency of the message and plot the output signal.

### Effect of noise

1. Connect a 100 mV_pp, 2 kHz sinusoid to the noise input. Trigger with t.p.5 and examine whether amplitude modulation appears on top of the FM at t.p.34.
1. Examine the signal at t.p.73.
1. Set the message amplitude to zero and measure the remaining noise amplitude at t.p.73.
1. Enable the amplitude limiter and observe its effect.
1. Repeat the same procedures with the Quadrature Detector block and compare the two demodulators.
1. Prepare the report and submit it.

*Note: Step 7 of the FM handout says to change the frequency of the input by “removing the signal generator”; the connection wording is ambiguous. The subsequent measurements require changing the input frequency. Also, the “7–14” reference in step 14 includes its own step; this is how the source is worded.*
