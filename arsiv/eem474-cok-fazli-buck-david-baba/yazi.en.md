---
baslik: EEM474 Power Electronics: Multiphase buck converter (David Baba, Texas Instruments)
ozet: A 2012 article covering the phase-shifted buck, input and output ripple, a 40 A application example, and layout principles.
---

David Baba's article "Benefits of a multiphase buck converter," published in the first-quarter 2012 issue of Texas Instruments Analog Applications Journal. The PDF creation date is February 22, 2012; the full article can be downloaded at the end of this post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed at the request of the rights holder.*

## Phase-shifted operation

In a two-phase buck, the switching times of two inductors feeding the same output are shifted relative to each other. With a 40 A load shared equally, the average current of each phase is 20 A. Sharing the current spreads the thermal load across the components; the partial cancellation of the current ripples eases the burden on the input and output capacitors.

## Dependence of ripple on duty cycle

For N phases and duty cycle D, taking k = floor(ND), the normalized output ripple in the article is:

r(D) = N [D − k/N][(k + 1)/N − D] / [D(1 − D)]

For two phases at D = 0.20, r = 0.75, i.e., a 25% reduction. In the D = 0.25 simulation, the single-inductor ripple is 2.2 A, while the total ripple at the output is about 1.5 A. In an ideal two-phase system, the ripples cancel each other completely at D = 0.5.

*Note: The zero-ripple result assumes equal phases and ideal timing; a real circuit has tolerances and parasitics. The formula is not used directly at the endpoints D = 0 and D = 1, since it would involve division by zero.*

## Input capacitor and transient response

The article also compares the RMS current requirement of the input capacitor as a function of duty cycle. Lower energy storage per inductor can improve the response to a load step. Ripple cancellation reduces the ESR-induced voltage ripple at the output.

## Application example

The LM3754 evaluation board uses a 10.8–13.2 V input, 1.2 V output, 40 A maximum load, and 300 kHz switching frequency. A 0.5 µH inductor per phase and a total of 2000 µF of output capacitance are listed. The measurements in the article show a response of about 20 µs to a 10 A load step, with about 27 mV of undershoot/overshoot. The efficiency and power-loss graphs compare the 0.9 V and 1.2 V outputs.

## Layout

High-current paths and gate-drive return paths are kept short. The signal ground and power ground are joined at a suitable point. Small-signal components are placed close to the controller; the copper area of the switching node and its coupling to sensitive traces are limited. The proximity of the input capacitor to the MOSFET pair is particularly emphasized.

*Note: The product names and measurement values belong to the application in the 2012 article; they are not a current product recommendation, nor guaranteed performance for every multiphase circuit.*
