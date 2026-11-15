---
baslik: EEM474 Power Electronics: Buck Converter Simulation Files
ozet: Peak current mode and synchronous buck PSIM schematics with recorded current and voltage data.
---

The peak current mode buck and synchronous buck PSIM schematics from the EEM474 project folder have been archived together with their recorded numerical results. Personal computer paths inside the schematics have been anonymized. The ZIP file can be downloaded at the end of the post; the simulations were not re-run.

## Peak Current Mode and Slope Compensation

The schematic carries the description "Peak Current Mode Control with Slope Compensation". It contains an inductor, capacitor, resistor, IGBT, diode, current sensor, comparator, SR flip-flop, square-wave source, and resettable integrator blocks. The `Ipeak_ref` and `Slope compensation` labels indicate the current threshold and the slope compensation.

Columns of the results file:

```
Time  I(L)  Vo  Vslope  Vm
```

There are 4000 samples with a 0.2 µs time step, covering 0.2 µs–0.8 ms. In the recorded results, the inductor current ranges from 0.01 to 2.66651 A, and the output voltage ranges from approximately 0 to 11.443 V. In the last sample, I(L) = 2.13 A, Vo = 11.4201 V, Vslope = 0, and Vm = 2.1. The largest recorded value of the compensation ramp is 0.5976.

The description of this circuit can be found in the post [Peak Current Mode Project Report](/arsiv/eem474-tepe-akim-modu-raporu/).

## Synchronous Buck

The second schematic contains an inductor, capacitor, resistor, MOSFET switches, a DC source, and gating blocks. The results file:

```
Time  I2  V1
```

Again there are 4000 samples with a 0.2 µs step. I2 ranges from approximately −19.81 µA to 3.11913 A; V1 varies between 10.8581 and 12 V. In the last sample, I2 ≈ −19.59 µA and V1 = 10.8581 V.

*Note: `I2` and `V1` are the probe names in the recording; since the schematic was not reopened and simulated again, they were not automatically renamed as output current/voltage. The long digit strings are scientific-notation measurement data, not student numbers.*
