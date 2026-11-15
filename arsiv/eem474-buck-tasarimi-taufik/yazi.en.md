---
baslik: EEM474 Power Electronics: Practical Buck Converter Design (Dr. Taufik, Cal Poly)
ozet: Buck component sizing, loss calculation, synchronous rectification, soft switching, and multiphase operation from the PECON 2008 presentation.
---

The content of 97 pages of the PECON 2008 tutorial presentation titled "Practical Design of Buck Converter" by Dr. Taufik of California Polytechnic State University was reviewed and transferred into text. The PDF is dated November 16, 2008. Since the laboratory photographs and datasheet excerpts were not transferred, there is no download file.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request by the rights holder.*

## Operation and Sizing

For an ideal continuous-conduction buck converter, Vo = DVs. While the switch is on, the slope of the inductor current is (Vs − Vo)/L, and while it is off, it is −Vo/L. The relations ΔIL = Vo(1 − D)/(Lf); IL,avg = Io; IL,max/min = Io ± ΔIL/2 are used.

At the continuous-current boundary, IL,min = 0. The critical inductance is Lcrit = (1 − D)R/(2f). The presentation explains that the design should leave a margin above this boundary and that the condition should also be checked at minimum load. The current/voltage stresses on the switch and diode are calculated under worst-case input and load conditions.

## Capacitors

For an ideal output capacitor, ΔVo = ΔIL/(8fC), and the RMS value of the triangular current is IC,rms = ΔIL/(2√3). The voltage ripple due to ESR is added separately. The input capacitor supplies the pulsed current of the switch; the RMS current rating matters as much as the voltage rating.

## 12 V → 2.5 V, 1 A Example

For 50 kHz switching and a 0.1 A continuous-conduction boundary, D ≈ 0.208 is calculated. The critical inductance is approximately 198 µH; 200 µH is selected. At full load, the current varies between approximately 0.901 and 1.099 A. With a 1% output ripple target, the ideal capacitance is found to be approximately 19.8 µF; with the 50 µF selection, the ideal ripple is approximately 0.396%. The subsequent simulations show the start-up transient and the steady-state waveforms.

## Losses

MOSFET conduction loss is evaluated as Isw,rms² RDS(on); the dependence of RDS(on) on gate voltage and temperature is shown. The voltage–current overlap during transitions causes switching loss. Gate drive loss is treated as Qg Vgate f; the energy loss associated with the output capacitance is treated as approximately ½Coss Vin² f.

For the diode, forward drop, dynamic resistance, reverse leakage, turn-on, and reverse recovery losses are separate topics. In the inductor, copper loss is IL,rms²RL; core loss depends on frequency, flux swing, and material parameters. In the capacitor, the loss is IC,rms²ESR. After the total loss is calculated, the efficiency is found.

## Improving Efficiency

Low on-resistance, appropriate gate charge, Schottky diode, low ESR, low winding resistance, and reduced ripple are compared. Increasing the frequency allows smaller filter components but may increase switching and magnetic losses.

In the synchronous buck, a controlled MOSFET is used in place of the freewheeling diode. During dead time, the body diode conduction and reverse recovery effects remain significant. Zero-current turn-off and zero-voltage turn-on examples are introduced to reduce the voltage–current overlap during the transition.

## PWM Controller and PCB

In current-mode control, the current sense resistor, RC filter, error amplifier, and compensation network are examined. The UC184x/ML38xx family is used as a historical example. The timing resistor/capacitor, maximum duty cycle, and dead-time selection are interrelated. In the Type II compensation example, the crossover frequency, the LC pole, and the ESR zero are taken into account.

High di/dt paths are kept short. Input decoupling is placed close to the switches, and controller decoupling close to the supply pin. The switching node is kept away from sensitive feedback and current-sense paths; the ground layout should reduce common-impedance coupling.

## Multiphase Buck

Phase-shifted parallel legs share the current, reduce ripple, and distribute heat. In the simulations comparing two phases with a single phase, the inductor currents, total output, and input pulses are shown together. Dynamic response and the use of smaller components are evaluated together with the control and current-sharing requirements.

*Note: The calculations follow the ideal model and the roundings in the source. Because of the ESR, semiconductor drops, and switching losses added later, the result of the initial ideal calculation will not match the real circuit.*
