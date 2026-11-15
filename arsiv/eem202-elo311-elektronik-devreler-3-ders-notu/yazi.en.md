---
baslik: EEM202 Circuit Theory II: ELO-311 Electronic Circuits III Course Notes, Analog Electronics II (Kaplan, 2010-2011)
ozet: "ELO-311 Electronic Circuits III" course notes (2010-2011, with "Analog Electronics - II, Kaplan" in the page headers): introduction to the op-amp and its characteristics, differential amplifier, inverting and non-inverting amplifiers, difference amplifier, voltage follower, differentiator and integrator, comparators, active filters, multivibrators, and voltage-to-current / current-to-voltage converters.
---

This post introduces the 72-page document titled **"ELO-311 Electronic Circuits III – Course Notes – 2010-2011"** kept in the course folder (the PDF dates from October 2010). The page headers read **"Analog Electronics - II"** and the name **"Kaplan"**; the document does not name an institution. The notes cover operational amplifiers (op-amps) and are kept in the folder as an additional resource for the active filter and op-amp work in the EEM202 laboratory. The sections and main points are summarized below; the original PDF can be downloaded at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes, with the source credited. It will be removed at the request of the rights holder.*

## Chapter 1: Operational Amplifiers

### 1.1 Introduction to the Op-Amp

The first integrated circuit produced in the electronics industry was an op-amp: it was manufactured in 1963 by Fairchild under the code µA702. Op-amps are direct-coupled, high-gain voltage amplifiers designed to amplify signals over a wide frequency range; they are used in many areas such as process control, communications, computers, power and signal sources, and measurement systems. This section covers the op-amp symbol and its terminals (inverting "−" and non-inverting "+" inputs, supply connections), typical packages, the manufacturers' coding system, and the properties of ideal and practical op-amps.

### 1.2 Differential Amplifier

The structure, operating characteristics, and differential/common-mode gains of the transistor differential amplifier that forms the input stage of the op-amp.

### 1.3 Op-Amp Characteristics

Parameters such as input offset voltage and current, input bias current, open-loop gain and frequency response, slew rate and full-power bandwidth, and CMRR. From the example problems: "Find the maximum differential input voltage of the op-amp", "Find the full-power bandwidth for an output of V_oSAT = ±12 V".

## Chapter 2: Basic Op-Amp Circuits

- **2.1 Inverting and non-inverting amplifiers:** closed-loop gain A_CL, and problems on output voltage and current drawn from the op-amp in circuits powered by a ±12 V symmetrical supply.
- **2.2 Basic difference amplifier:** a circuit that amplifies the difference between two inputs; load current I_L problems (R1 = R2 = R3 = R_f = 10 kΩ, R_L = 1 kΩ or 10 kΩ).
- **2.3 Voltage follower.**
- **2.4 Differentiator and integrator:** analysis of the output waveform in circuits with a 2 kHz triangular wave and square wave applied to the input.

## Chapter 3: Op-Amp Applications

- **3.1 Voltage comparators:** a reference is applied to one input and the signal to be compared to the other; positive, negative, and zero voltage level detectors depending on the polarity of the reference, and analysis of a detector with a noisy input; in the example circuit R1 = 2 kΩ, R2 = 10 kΩ, R_L = 1 kΩ.
- **3.2 Active filters:** four types of active filter: low-pass, high-pass, band-pass, and band-stop (notch); the band is defined by the gain falling to 0.707 at the cutoff frequency.
- **3.3 Multivibrators:** **astable** (square-wave generator) and **monostable** (one-shot) multivibrators built with op-amps; the stable state, transition state, and return positions of the monostable circuit, along with input and output waveforms.
- **3.4 Voltage-to-current and current-to-voltage converters:** in industry, the outputs of sensors that measure quantities such as pressure, temperature, and flow are converted to standard current or voltage values, and these need to be converted into one another; these functions are performed with op-amp **voltage-to-current** and **current-to-voltage** converters.

## Downloadable File

The original 72-page PDF can be downloaded below.
