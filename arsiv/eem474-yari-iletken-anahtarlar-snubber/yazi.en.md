---
baslik: EEM474 Power Electronics: Power Semiconductors and Snubber Circuits
ozet: The operating principles of diode, thyristor, BJT, MOSFET, and IGBT switches, together with switching losses and protection circuits.
---

The explanations and formulas from the English-language presentations in the EEM474 course folder have been transferred into text. The preparer's name is not stated explicitly in the documents. Since photographs and images taken from books were not transferred, there is no download file for this post.

## Comparison of power switches

A diode turns on depending on the voltage across its terminals and the circuit current; it has no independent control terminal. A thyristor can be switched on with a gate pulse, but a normal SCR cannot be turned off via the gate. The main current must fall below the holding current. The GTO is treated as the type of thyristor that can be turned off via the gate.

The BJT is compared as a current-driven device, while the MOSFET and IGBT are compared as devices driven by gate voltage. The insulated gate of a MOSFET requires a small input current in the static state; during switching, the gate capacitances are charged and discharged. The IGBT combines insulated-gate drive with bipolar conduction characteristics.

## Operating regions of the thyristor

The forward blocking, forward conduction, and reverse blocking regions are distinguished. Once the thyristor has turned on, the gate signal can be removed. Latching current and holding current are not the same concept: the former concerns the sustained conduction after triggering, the latter the continuation of conduction that is already under way. In AC circuits, the natural current zero assists commutation; in DC circuits, an additional commutation arrangement may be required.

## Conduction and switching losses

Conduction loss is calculated as the product of the voltage across the switch and the current. For a suitable MOSFET, using the resistance model, Pcond ≈ Irms² RDS(on). During switching, since the voltage and current are nonzero at the same time, transition energy is produced:

Etransition = ∫ v(t)i(t) dt

Pswitching = fs (Eon + Eoff)

In the presentations, the turn-on and turn-off waveforms are examined in terms of delay, rise, fall, and storage times. The reverse recovery of the diode also affects the current and losses of the other switch.

## Switch selection

Blocking voltage, average/RMS/peak current, operating frequency, conduction loss, switching time, safe operating area, and cooling are evaluated together. The nominal current rating alone is not sufficient. The gate or base driver must provide the voltage, current, and isolation conditions that the switch requires.

## Snubber and inductive load

Because inductor current cannot change instantaneously, turning off the switch can produce an overvoltage. A freewheeling diode provides an alternative path for the current. RC and RCD snubber arrangements are shown for limiting the rate of voltage rise or for absorbing the energy of the parasitic inductance. A series inductive element can limit the di/dt change.

For a capacitor, i = C dv/dt, and for an inductor, v = L di/dt; these relations explain the effect of the protection elements. If the snubber energy is dissipated in a resistor, this is also added to the total loss. Keeping the switching trajectory within the safe operating area is a broader design matter than merely limiting the peak voltage.
