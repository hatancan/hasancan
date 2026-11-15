---
baslik: EEM214 Electronics I: Introduction to Laboratory Instruments (Oscilloscope, Breadboard, Signal Generator) and Experiment 1 Reports
ozet: The instrument introduction given as the pre-lab reading for the EEM214 Electronics I laboratory: probes, channels, AC/DC coupling, triggering, and the measurement menu on the oscilloscope, breadboard use and wire preparation, the signal generator, and the adjustable power supply; plus two student reports for the oscilloscope, DMM, and potentiometer experiment.
---

This post brings together the **Introduction to Laboratory Instruments** document (9 pages, 2003–2005), which students in the Başkent University Electrical-Electronics Engineering **EEM 214 – Electronics I** laboratory were asked to read as pre-lab work before the first experiment, and two student reports for the first experiment ("Oscilloscopes, DMM, Function Generator, Potentiometer"). The reports are the work of friends; names and student numbers have been redacted. The 2012 handout for the experiment can be found in the archive in the post "Laboratory Experiment 1". The document and the reports can be downloaded as a ZIP at the end of the post.

## Introduction to Laboratory Instruments

### Oscilloscope

The oscilloscope is one of the basic instruments of the laboratory. It displays on its screen the electrical signals applied to its leads, known as probes; in this way you can check whether a circuit is working as intended or observe the signals at particular points. For a signal to be observed meaningfully on the screen it must be periodic; otherwise you get overlapping or fluctuating traces on the screen.

Today many oscilloscopes are digital. Digital oscilloscopes sample the signal they receive from the probes and store it in memory; this way non-periodic signals can also be observed in the set time window, and operations can be performed on the signal. Their biggest disadvantage is the limited sampling frequency, which narrows the frequency range of signals that can be observed. Analog oscilloscopes have a similar limit, but it is determined by the operating bandwidths and delay times of the components used.

**Probe setting:** Probes carry multipliers such as 1X, 10X, 100X. If the probe is set to 10X, the amplitude of the input signal is reduced to one tenth; to see the signal one-to-one, the probe must be at 1X. In addition, the probe multiplier in the oscilloscope menu (the Storage menu on the example instrument) must also be set to 1X. The **Probe Adjust** terminal at the edge of the screen supplies a 0.5 V peak-to-peak square wave that varies between 0 and 0.5 V; to check that the probe and channel are set correctly, it is enough to connect only the probe tip to this terminal.

Things to watch before connecting the probe to a point:

- The voltage at the point to be observed must be at a level that will not damage the oscilloscope.
- The probe's ground lead must be connected to the correct point.
- The impedances of the point to be observed and of the oscilloscope channel must be compatible.
- If two channels are used together, both must be connected to the same ground.
- Both ends of the probes must be fully seated.

**Channel setting:** First, the axis (zero) is set by grounding the channel input, and the signal is positioned on the vertical axis with the position knob; then, depending on the nature of the signal to be measured, AC or DC mode is selected. For example, a high-frequency signal riding on a slowly varying component cannot be read correctly in DC mode; in AC mode the oscilloscope filters out the DC (and near-DC, slow) component and displays only the AC part. Many oscilloscopes can display, add, or subtract the channels at the same time; this makes it easier to measure the voltage across an element.

**Trigger setting:** The signal on the screen and the oscilloscope must be synchronized. Automatic triggering gives a stable display in most cases; if the signal has more than one component the oscilloscope could lock onto, synchronization is achieved with the time/div and trigger menu settings. The trigger menu contains **Source** (which channel or external source), **Mode** (auto, normal, TV horizontal/vertical), and **Level/Hold-off** settings.

**Measurement menu:** Although it is possible to take measurements by counting the divisions on the screen, this is laborious; with the measurement menu on oscilloscopes, values such as frequency, amplitude, and period can be read directly.

### Breadboard

The breadboard is used to connect circuit components without soldering and to build small experimental circuits; it is especially ideal for working with DIP-type ICs. The holes are arranged at the standard IC pin spacing; certain groups are connected to each other internally, and the horizontal rows at the top and bottom are generally supply distribution rails.

The metal spring inside each hole contacts the wire along its side surface; therefore there is no point in stripping wire ends longer than necessary or pushing them too far into the board, and it is in fact undesirable:

- The pin structure is damaged, which causes poor contact in the next use.
- A long wire can run horizontally inside the metal sheath and touch neighboring pins.
- It can touch the metal plate at the base of the board and form a short circuit with another long wire, or a high-impedance path.

Wire ends should be stripped with side cutters or a wire stripper; they must never be stripped by burning with a flame, as this damages the chemical structure of the wire.

### Signal generator

These are instruments that produce periodic signals. Their common features are: different waveforms (sine, square, triangle) and an inverter, frequency ranges (1 Hz – 1 MHz), a frequency multiplier (0.1–2.0), a duty multiplier (duty), DC shift (offset), amplitude adjustment, and a low-impedance output; also dB attenuation options for applying signals to high-gain circuits. First the waveform and frequency are selected, the generator is connected to the circuit, and the amplitude is adjusted **while connected to the circuit** (the set amplitude may change because of the generator and circuit impedances); generally it is connected with the amplitude near zero and then slowly increased.

### Adjustable power supply

It consists of two sources that can operate in symmetric (tracking) or independent mode; to connect them in series, the − and + terminals of the master and independent sources are joined with a piece of metal. Their displays show the voltage and the current drawn; by limiting the maximum current, burning of the circuit in a short-circuit or overcurrent situation is prevented, and in a short circuit the supply automatically cuts the output.

## Student reports (Experiment 1)

### 2006 report

- For a 1 V peak sine wave, from the oscilloscope's measurement menu: V_max = 0.98 V, V_min = −0.98 V, V_avg = 0 V, V_rms = 705.7 mV, V_pp = 1.96 V, period 10.08 ms, frequency 99.20 Hz.
- Volts/div changes the value of each division, not the amplitude of the signal; time/div changes the time scale, not the frequency; the position knob does not add DC voltage, it only shifts the signal.
- At 2 V/div, since there are 8 divisions on the screen, at most 16 V peak-to-peak can be read; a full-amplitude signal does not fit.
- When the generator's DC offset is added, no difference is seen in AC coupling; in DC coupling the signal is seen together with the offset.
- Voltage divider with a potentiometer (V_out = V_in·R2/(R1 + R2)):

| Position | R1 | R2 | V_out (R_L = ∞) | V_out (R_L = 150 Ω) |
|---|---|---|---|---|
| Fully clockwise | 4.970 kΩ | 1 Ω | 0.6 mV | 0.6 mV |
| Middle | 2.580 kΩ | 2.512 kΩ | 5 V | 0.6 V |
| Fully counterclockwise | 1 Ω | 4.888 kΩ | 10 V | 7.2 V |

Fully clockwise, R2 = 0 and V_out = 0 should theoretically hold; because of the small measured 1 Ω, 0.6 mV is read. The other positions are close to the expected values.

### 2008 report

From the measurement menu: V_max = 1.96 V, V_min = −1.08 V, V_pp = 2.04 V, V_avg = −35.2 mV, period 10.55 ms, frequency 94.52 Hz. It is briefly explained that volts/div sets the voltage value of each division and sec/div sets the time scale; that the signal cannot be read when it does not fit on the screen; that triggering stabilizes the display; and that the DC offset shifts the signal. The potentiometer table was left blank.

## Download

The ZIP file contains the Word file of the Introduction to Laboratory Instruments document and PDF copies of the two reports with personal information redacted.
