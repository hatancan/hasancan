---
baslik: EEM474 Power Electronics: Final Exam Study Questions on Motors
ozet: Study questions on DC motor direction and speed control, back EMF, induction motor slip, and the stepper motor.
---

Oral study questions on motors, with short answers, compiled to prepare for the EEM474 final. A three-page PDF, undated, can be downloaded at the end of this post. The exam-scope announcement at the beginning of the file applies only to the relevant semester.

## DC Machines

Permanent-magnet, wound-field, and electronically driven motors are compared. For the generator, E = KΦω is used; for motor torque, T = KΦIa is used. Back EMF is produced by the rotor rotating in the field, and it limits the motor current against the supply voltage.

In steady state, U = E + RaIa; at start-up, since E = 0, Ia ≈ U/Ra. A starting resistor or a current-limiting drive limits the starting current. The torque–speed relationship is plotted as a function of the applied voltage and the field flux.

## Reversing Direction

In a permanent-magnet motor, the armature polarity is reversed. In shunt and series-wound motors, only the armature connection or only the field connection must be reversed. If both are reversed, the direction of torque does not change. In a separately excited machine, it is sufficient to change the polarity of one of the independent field/armature sources.

## Speed Control

With the field held constant, the armature voltage is varied; with the armature voltage held constant, the field current is varied. Students are asked to explain the torque–power–speed relationships below and above the base speed. The cause-and-effect chain from a change in field resistance through flux, EMF, current, and speed is also asked separately.

*Note: In one place, the source equates the constant armature voltage case with "the current through the rotor is constant." Since the current also depends on the load torque and the back EMF, keeping only the voltage constant does not fix the current.*

## AC Motor

The transformer and the induction motor are compared. The synchronous speed of the rotating field is ns = 120fs/P; slip is s = (ns − nr)/ns. At standstill s = 1, at synchronous speed s = 0, and in the motoring region generally 0 < s < 1. The rotor electrical frequency is related by fr = sfs.

*Note: For s = 0, the source says "the motor does not rotate." This statement is incorrect: nr = ns; in an ideal induction motor, the relative speed and the induced rotor torque are zero.*

For variable-speed three-phase drive from a single-phase supply, a rectifier–DC link–inverter structure is drawn. For the single-phase motor, creating the starting field with an auxiliary winding is asked; for the three-phase motor, reversing direction by swapping two phases is asked.

## Stepper and Brushless Motors

For full-step and half-step operation, the 1/0 energizing sequences of the windings, the forward/reverse order, and the relationship between the number of pulses and the angle are requested. The position and drive characteristics of the stepper motor and the brushless DC motor with electronic commutation are compared.

*Note: The question numbers in the source skip around; they are grouped here by topic. The "not included in the final" list should not be interpreted as the current exam scope.*
