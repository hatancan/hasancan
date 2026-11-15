---
baslik: EEM474 Power Electronics: AC Motors and Variable-Frequency Drives
ozet: Rotating field, synchronous speed, slip, induction and synchronous motors, and V/f speed control.
---

The explanations and formulas from the English-language slides in the EEM474 course folder have been transcribed into text. The author's name is not clearly stated in the documents. Photographs and images taken from books were not transferred, so this post has no download file.

## Rotating Magnetic Field

Three-phase winding currents with a 120° phase difference between them produce a rotating magnetic field. The synchronous speed is given by ns = 120f/P, where f is the electrical frequency and P is the number of poles. The mechanical speed is in rpm. When the frequency or the number of poles changes, the speed of the field changes.

## Induction Motor

The relative motion of the rotor with respect to the field induces voltage and current in the rotor conductors. The interaction of this current with the stator field produces torque. Slip is defined as s = (ns − n)/ns. The rotor frequency is fr = sf. If the rotor were to reach synchronous speed exactly, induction and torque production would, in the ideal case, vanish.

The squirrel-cage and wound-rotor constructions are compared. The simple and robust construction of the squirrel-cage motor, together with a drive, gives it a wide range of applications. In the wound rotor, an external rotor resistance can be used to change the starting and speed behavior.

## Torque–Speed Curve

The starting torque, the maximum (breakdown) torque, and the normal operating region are evaluated separately. As the load torque increases, the operating point moves to a larger slip. The stator voltage, the frequency, and the rotor circuit parameters change the curve. Stable operation under load is analyzed through the intersection of the motor and load torques.

## Synchronous Motor

The rotor field of a synchronous machine rotates at the same speed as the rotating stator field. The rotor field can be produced by a magnet or by a field (excitation) winding. The synchronous speed is determined by the frequency and the number of poles even under load; an increase in torque changes the angular relationship between the rotor field and the stator field.

## Speed Control and V/f

When connected directly to the grid, the frequency is fixed. A rectifier, a DC link, and an inverter provide the motor with a supply of variable frequency and variable amplitude. Below the base speed, keeping the V/f ratio approximately constant is used to preserve the magnetic flux. At low frequency, the voltage drop across the winding resistance becomes more significant.

Increasing the frequency after the voltage limit has been reached corresponds to the field-weakening region. In the slides, the constant-torque and constant-power regions are related to the load requirements of the variable-speed drive.

## Single-Phase Motors

The difference between the field produced by a single-phase supply and the three-phase rotating field is explained. An auxiliary winding and a phase-shifting capacitor are used to establish the starting direction and torque. Depending on the application, capacitor-start and permanent-split (run) capacitor arrangements are distinguished.

*Note: The older version and the 2013 version of the slides were merged using their common content; the photographs of motors and drives were not published.*
