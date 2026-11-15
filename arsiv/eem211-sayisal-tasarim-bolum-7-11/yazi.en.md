---
baslik: EEM211 Digital Logic Design: "Digital Design" Lecture Notes, Chapters 6–11 (Combinational Circuits, Multivibrators, Flip-Flops, Counters, Registers, DAC/ADC)
ozet: Chapters 6–11 (2003–2004) of a Turkish "Digital Design / Digital Electronics" lecture note: adders, comparators, decoders, and encoders; monostable, astable, and bistable multivibrators, 74121/74122, and 555; latches and flip-flops; asynchronous and synchronous counters; shift registers, Johnson and ring counters; operational amplifier, D/A and A/D converters.
---

This post presents **Chapters 6–11** of a downloaded Turkish **"Digital Design"** lecture note found in the EEM211 Digital Logic Design course folder. The chapters are separate PDFs (sy-06, sys7–sys11), created from Word in September 2003 and March 2004; the page headers read "SAYISAL TASARIM – Derin" ("DIGITAL DESIGN – Derin"; "SAYISAL ELEKTRONİK – I", i.e. "DIGITAL ELECTRONICS – I", in Chapter 6). The author of the note and the institution it belongs to are not stated explicitly in the documents. The topics and notable examples of each chapter are summarized below; for the details of the formulas and circuit diagrams, all six PDFs can be downloaded as a ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed upon the rights holder's request.*

## Chapter 6: Combinational circuits

- **Arithmetic units:** half adder, full adder, two-bit and four-bit parallel adders.
- **Comparators.**
- **Decoders:** two-bit and three-bit decoders, decoders with enable inputs, the BCD-to-decimal decoder (4028), and the BCD-to-7-segment display decoder.
- **Data distributors (demultiplexers)** and **encoders:** decimal-to-BCD encoder and decimal-to-BCD priority encoder.
- **Parity generators and checkers.**

## Chapter 7: Multivibrators (oscillators)

Circuits that generate the square and rectangular waves used as trigger signals in digital circuits are called multivibrators (oscillators). They are examined in three groups: monostable, astable (free-running), and bistable multivibrators.

- **Monostable (one-shot):** produces a single pulse in response to a trigger at the input; the pulse width depends on the externally connected resistor and capacitor and is independent of the duration of the trigger signal. The transistor circuit, the non-retriggerable **74121** (tw = 0.7·R_EXT·C_EXT; if no external resistor is used, the internal resistance is 2 kΩ, tw ≈ 30 ns), and the retriggerable **74122** (tw = K·R_EXT·C_EXT·(1 + 0.7/R_EXT), K = 0.32) are described.
- **Astable (free-running):** in the transistor circuit the period is T = 0.7·(R1·C1 + R2·C2); in the oscillator built with a Schmitt-trigger gate, the high and low durations are calculated from the threshold voltages (e.g., for Vcc = 5 V, VT+ = 2.75 V, VT− = 1.67 V).
- **Bistable** multivibrators and **integrated timing circuits** (the 555-type timer).

**Example (74121):** For a 10 ms output pulse, if R_EXT = 10 kΩ is chosen, then C_EXT = tw / (0.7·R_EXT).

*Note: The note gives this calculation as 14.285 µF; the correct value is C_EXT = 10×10⁻³ / (0.7 × 10×10³) ≈ 1.43 µF (the exponent in the denominator was written as 10⁻³ instead of 10³, and the result is off by one order of magnitude).*

**Example (74122):** For a 10 µs pulse, if C_EXT = 200 pF is chosen, then R_EXT = tw/(K·C_EXT) − 0.7 = 10×10⁻⁶ / (0.32 × 200×10⁻¹²) − 0.7 ≈ 156.25 kΩ; 160 kΩ is chosen as the standard value.

## Chapter 8: Latches and flip-flops

The output of a combinational circuit depends only on the present inputs; a sequential circuit, on the other hand, consists of a combinational circuit together with memory elements that store information, and its outputs also depend on the stored information. In synchronous sequential circuits, the memory elements are all affected at the same time by a common clock signal, whereas in asynchronous circuits the order in which the inputs change is decisive. The topics of the chapter:

- S-R latch (with NOR and NAND gates), D latch;
- preventing contact bounce with the help of latches;
- S-R, D, J-K, and T flip-flops, the clock pulse, and edge triggering;
- asynchronous inputs in flip-flops (preset, clear);
- master-slave flip-flop;
- flip-flop excitation (transition) tables.

## Chapter 9: Counters

Circuits that repeat a certain sequence of states depending on the input pulses are called counters; they are used in timing circuits (frequency division, etc.) and control circuits (coding, information storage, etc.). Counters are classified as asynchronous and synchronous according to how the clock signal is applied, and as up and down counters according to the counting direction. Topics: the concept of modulus in counters, asynchronous up and down counters, resetting in asynchronous counters (counting in a desired modulus), and synchronous counters.

## Chapter 10: Registers

Circuits that store digital information temporarily are called registers. In the chapter, registers are classified according to data input-output and shift direction:

- left-shift and right-shift registers, the four-bit left-right shift register;
- serial-in serial-out (SISO), serial-in parallel-out (SIPO), parallel-in parallel-out (PIPO), and parallel-in serial-out (PISO) registers;
- shift-register counters: the Johnson counter and the ring counter.

## Chapter 11: Digital-to-analog (DAC) and analog-to-digital (ADC) converters

- Digital and analog signals.
- **Operational amplifiers:** the inverting amplifier (V_OUT = −V_IN·R_F/R_1), the non-inverting amplifier (A_V = 1 + R_F/R_1; in the example, a gain of 6 gives a 12 V output from a 2 V input), and the summing amplifier, with numerical examples.
- **D/A converters:** the binary-weighted resistor D/A converter (step-by-step calculation of the contribution of each input bit to the output) and the R-2R ladder D/A converter.
- **A/D converters:** parallel-comparator (simultaneous, flash), single-ramp (single-slope), and dual-ramp (dual-slope) A/D converters.
