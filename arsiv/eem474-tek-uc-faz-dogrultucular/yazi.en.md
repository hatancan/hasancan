---
baslik: EEM474 Power Electronics: Single-Phase and Three-Phase Rectifiers
ozet: Diode and controlled rectifiers, resistive and inductive loads, freewheeling, ripple, and firing angle.
---

The explanations and formulas from the English-language presentations in the EEM474 course folder have been transcribed into this text. The name of the preparer is not stated in the documents. Photographs and images taken from books were not transferred, so this post has no download file.

## Single-Phase Uncontrolled Rectifiers

In a half-wave rectifier, the diode conducts during the appropriate half-cycle of the source sinusoid. With a resistive load, the current follows the voltage. If the source peak value is Vm, the ideal half-wave output is Vavg = Vm/π and Vrms = Vm/2.

Full-wave rectification is implemented with a center-tapped transformer and two diodes, or with a four-diode bridge. In the bridge, two diodes are in each conduction path. For an ideal resistive load, Vavg = 2Vm/π and Vrms = Vm/√2. The fundamental ripple frequency of the full-wave output is twice the line frequency.

## RL Load and Freewheeling

The inductor delays changes in current. Even when the source voltage crosses zero, the load current may not drop to zero immediately. The extinction angle β of the current depends on the R/L ratio of the load and on the firing condition. A freewheeling diode provides a path through which the inductive current can circulate when the source is disconnected from the load.

For the load current, the equation L di/dt + Ri = v(t) is set up separately for each conduction interval. The continuity of the current is distinguished from the fact that the voltage may change through switching.

## Controlled Rectification

The average value of the output is adjusted by the SCR firing angle α. In a single-phase half-wave circuit with a resistive load, Vavg = Vm(1 + cosα)/(2π); in a full-wave controlled circuit, Vavg = Vm(1 + cosα)/π. In a fully controlled bridge, under the assumption of **continuous current**, Vavg = 2Vm cosα/π is obtained.

*Note: The continuous-current bridge relation should not be used in place of the discontinuous-current relation for a resistive load. For this reason, the average voltages of the different waveforms shown in the presentations differ.*

Source inductance makes commutation non-instantaneous. The commutation overlap, during which two conduction groups carry current simultaneously for a short time, affects the average DC output.

## Three-Phase Rectifiers

In a three-phase half-wave connection, the diode connected to the highest phase voltage conducts. In the bridge, the positive bus is connected to the highest phase and the negative bus to the lowest phase. The output is thus composed of segments of the line-to-line voltages. In the six-pulse bridge, the conducting pair changes at 60° intervals; each diode conducts for 120° under the ideal continuous-current condition.

For an ideal diode bridge, the average output is approximately Vdc = 1.35 VLL,rms. For a fully controlled three-phase bridge, under the assumption of continuous current and commutation without overlap, Vdc = 1.35 VLL,rms cosα is used. The ripple frequency of the six-pulse output is 6f.

## Filter and Evaluation

A capacitor filter charges around the peak and supplies the load while the diode is off. While a smaller output ripple is achieved, the input current can become narrow, high pulses. For this reason, the smoothness of the DC output, the input power factor, and the diode peak current are examined together.

The three drawings in the project folder complement the same topics: single-phase diode connections, a filtered output, and a three-phase bridge. The circuits are described in the text; the image files have not been published separately.
