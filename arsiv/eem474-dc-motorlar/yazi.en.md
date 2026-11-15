---
baslik: EEM474 Power Electronics: DC Motors, Torque–Speed Relationship, and Drives
ozet: Permanent-magnet, shunt, series, and compound DC machines; electromechanical conversion, losses, and speed control.
---

The explanations and formulas from the English-language slides in the EEM474 course folder were transferred into text. The name of the preparer is not clearly stated in the documents. Since photographs and images taken from books were not transferred, there is no download file for this post.

## Energy Conversion

A motor converts electrical energy into mechanical energy; a generator converts mechanical energy into electrical energy. The basic relationships are E = KΦω, T = KΦI, and Pconversion = EI = Tω. For a conductor in a field, the force is F = BℓI sinα; the voltage induced by motion, under the appropriate perpendicularity condition, is given as e = Bℓv.

The presentation addresses motor selection in terms of cost, thermal capacity, efficiency, torque–speed curve, acceleration, power density, and peak torque. Automotive, household appliances, industry, printers, and disk drives are application examples.

## Permanent-Magnet DC Motor

The stator provides the constant magnetic field, and the rotor provides the current-carrying armature windings. The brushes and commutator change the connection of the winding current during rotation. In steady state, Vs = Eg + RaIa; Eg = Keω; T = KtIa. Therefore:

ω = Vs/Ke − RaT/(KeKt)

At start-up, since ω = 0, there is no back EMF; the current is limited by the armature resistance and the drive. The ideal no-load speed is Vs/Ke, and the locked-rotor torque is KtVs/Ra. When the voltage is changed, the position of the torque–speed line shifts.

*Note: In one line of the speed equation in the source, the Ke and Kt labels are mixed up. The relationship above was written from the equations Vs = Keω + RaIa and T = KtIa given on the same page. In some models using SI units, the numerical values of these two constants may be the same.*

## Wound-Field Machines

In a separately excited machine, the field winding is supplied from a separate source. In the shunt connection, the field winding is parallel to the armature; when the field current is kept approximately constant, the speed varies little with load. In a series motor, the field current equals the armature current; a high starting torque is obtained, but the speed can increase greatly when the load decreases. In a compound machine, series and shunt fields are present together.

For a generator, the terminal voltage is written as U = Ea − RaIa; for a motor, Ea = U − RaIa. The intersection of the motor and load torque–speed curves is the operating point.

## Losses and Efficiency

The armature copper loss is Ia²Ra, and the field copper loss is If²Rf. Friction, windage, hysteresis, and eddy-current losses are also taken into account. Efficiency is the ratio of useful output power to input power. The electromechanical conversion power and the useful shaft power are not the same, because of losses.

*Note: The source uses an idealized description in which the no-load torque and output power are zero. In a real motor, there is a no-load current that supplies friction and other losses. The statement "change the field polarity" regarding reversing a permanent-magnet motor should likewise be read as reversing the armature supply polarity for this motor.*

## Speed and Direction Control

Armature voltage, field flux, and circuit resistance influence speed. The average armature voltage is adjusted with a chopper. An H-bridge provides motion in both directions by reversing the polarity; freewheeling paths maintain the continuity of the inductive current. In regenerative operation, energy coming from the mechanical side is fed back to the electrical source.
