---
baslik: EEM474 Power Electronics: Stepper Motors and Brushless DC Motors
ozet: Full-step and half-step drive, step angle and pulse frequency calculations; commutation of a brushless motor with Hall sensors.
---

The explanations and formulas from the English-language slides in the EEM474 course folder have been transcribed into text. The author's name is not clearly stated in the documents. Photographs and images taken from books have not been transferred, so this post has no download file.

## Stepper Motor Motion

A stepper motor produces discrete angular motion by energizing its windings in a specific sequence. Position is related to the number of pulses; speed is related to the pulse frequency. The rotor and stator arrangements of variable-reluctance, permanent-magnet, and hybrid designs are shown.

For N steps per revolution, the step angle is β = 360°/N. After q pulses, the rotation angle is θ = qβ; for a pulse frequency fp, the speed is n = 60fp/N rev/min.

## Full Step and Half Step

Full-step sequences, in which the windings are energized one at a time or two at a time, are compared. In half-step drive, single-winding and two-winding states are applied in alternation; the mechanical step becomes smaller and the number of pulses required for one revolution doubles. When the sequence is reversed, the direction of rotation changes.

Holding torque is the ability of the energized windings to maintain position while the motor is at rest. As speed increases, the time available for the winding current to rise decreases; therefore, the torque falls, depending on the drive and supply conditions. If the load and acceleration requirements are exceeded, missed steps may occur.

## Calculations in the Slides

| Data | Result |
| --- | --- |
| β = 1.8° | N = 200 steps/rev |
| N = 200, fp = 6000 pulses/s | 30 rev/s = 1800 rev/min |
| β = 1.8°, θ = 46.8° | 26 pulses |
| N = 500, n = 3600 rev/min | fp = 30,000 pulses/s |

These calculations assume that no steps are missed and that the specified step mode is maintained.

## Brushless DC Motor

Electronic switching takes over the function of the mechanical brush and commutator. The rotor position can be determined with Hall sensors or optical sensing. The control circuit energizes the appropriate stator windings according to the position. For the motor to rotate, the commutation sequence must be consistent with the rotor position.

The slides show the operating principle of the Hall sensor, the generation of switching signals from the sensor states, and the sequence of the phase currents. Laser printers and similar motion systems are examples of applications.

*Note: The two copies of the source were merged into a single post. In place of photographs and product images, the operating principle and numerical examples were transcribed into the text.*
