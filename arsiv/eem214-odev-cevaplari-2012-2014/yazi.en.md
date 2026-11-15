---
baslik: EEM214 Electronics I: Homework Answers (2012–2014), Diode Types, Datasheet Reports, Resistor and Capacitor Types
ozet: Student answers to the 2012, 2013 and 2014 homework assignments of EEM214 Electronics I: tunnel, varicap, Schottky, photo and LED diodes; datasheet reports on the 1N4148/1N4448, MJE521, 2N3055, 2N6660, VN2222L and BAR17; resistor color codes and capacitor types.
---

This post collects the answers that students prepared for the homework assignments given in the spring semesters of 2012, 2013 and 2014 in the **EEM214 Electronics I** course at Başkent University. All of them are the work of classmates; names and student numbers have been removed (the numbers in the file names of the 2013 assignments were also removed). The 2013 version of the assignment texts is in the archive post [EEM214 Assignments (2013)](/arsiv/eem214-odevler-2013/); the 2012 assignment list is almost the same (Assignments 2–4, issued 12.04.2012, due 11.05.2012) and is included in the ZIP. The PDFs with personal information redacted can be downloaded as a ZIP at the end of the post.

## 2012 and 2013: Assignment 1 – Diode types

The answers of two students describe the five requested diode types under the headings structure, operating principle, characteristic and application area:

- **Tunnel diode:** Made by adding heavy doping to pure silicon and germanium; the P-N junction is very thin. In its characteristic, the current increases as the voltage increases up to a certain value, then the current drops (negative resistance region, slope −1/R) and rises again. Thanks to this negative resistance, it is used as an amplifier, as an oscillator in the MHz range (the resistance of the resonant circuit must be smaller than the negative resistance, for example 80 Ω), and as a switch in circuits such as multivibrators and flip-flops; it can operate up to 10 000 MHz.
- **Varicap diode:** Operates under reverse bias; as the reverse voltage increases, the neutral (depletion) region widens and the capacitance decreases. It replaces expensive, bulky, manually adjusted variable capacitors; it is used in automatic frequency control in TV and FM receivers, frequency modulators and frequency multipliers.
- **Schottky diode:** A diode that can switch rapidly between conduction and cutoff at very high frequencies; it is used as a mixer, modulator, demodulator and detector in microwave receivers.
- **Photodiode:** Used under reverse bias; it is an insulator until light falls on the junction, and when light falls on it, electron–hole pairs are generated and a current (about 20 µA) flows. It is used in remote control receivers, alarm and counting circuits, and fire alarm systems.
- **LED:** A P-N diode doped with GaAs, GaAsP or GaP; under forward bias, the energy released by the recombination of electrons and holes at the junction is emitted as light. It is used in digital displays, indicator lamps and optocouplers.

*Note: The answers state that the tunnel diode "operates under reverse bias" and that the Schottky diode is made "by coating the P-N junction with platinum". The negative resistance region of a tunnel diode is in the forward direction; the Schottky diode, on the other hand, has a metal–semiconductor (metal–n) junction rather than a P-N junction, which is why its forward voltage drop is small (about 0.2–0.3 V) and its switching speed is high.*

## 2012 and 2013: Datasheet reports (Assignments 2–4)

In these assignments, students examined and commented on the datasheet of a diode, a BJT and a FET/MOSFET of their choice section by section (manufacturer information, package and pin layout, absolute maximum ratings, thermal characteristics, electrical characteristics, typical characteristic curves, package dimensions); the reports also include excerpts taken from the datasheets.

**2013 reports:**

- **Diode – 1N/FDLL 914, 916, 4148, 4448 (Fairchild):** high-conductance fast diode; color bands of the FDLL type, maximum ratings (T_A = 25 °C), thermal characteristics, forward voltage–current, reverse current, capacitance and reverse recovery time curves.
- **BJT – MJE521 (Motorola):** medium-power NPN silicon transistor in a plastic package, 4 A, 40 V, 40 W; recommended for general-purpose amplifier and switching applications, especially 5–10 W audio amplifiers with complementary symmetry, PNP counterpart MJE371; safe operating area and DC current gain curves.
- **MOSFET – 2N6660 and VQ1004J/P (Vishay Siliconix):** single and quad N-channel, 60 V MOSFETs; summary table of V(BR)DSS, r_DS(on), V_GS(th), output and transfer characteristics, variation of r_DS(on) with temperature, capacitances and transient thermal impedance.

**2012 reports:**

- **BJT – 2N3055 (NPN power transistor):** DC current gain β 20–70; V_CE(sat) = 1.1 V (I_C = 4 A, I_B = 400 mA); V_CEO(sus) at least 60 V (I_C = 200 mA), V_CER(sus) at least 70 V (R_BE = 100 Ω); I_CEO at most 0.7 mA (V_CE = 30 V); I_CEX at most 1.0 mA (5 mA at T_C = 150 °C); I_EBO at most 5 mA (V_BE = 7 V); variation of h_FE with current and temperature.
- **MOSFET – VN2222L (N-channel):** body and terminals, absolute maximum ratings, drain–source breakdown voltage (at least 60 V), threshold voltage (0.6–2.5 V), zero-gate-voltage drain current, on-state resistance (r_DS(on) at most 7.5 Ω), forward transconductance, input and output capacitances and typical curves.
- **PIN diode – BAR17:** silicon PIN diode; storage and operating temperatures, power dissipation, reverse voltage, forward current, reverse current, diode capacitance, and curves of forward resistance versus current and capacitance versus reverse voltage.

## 2014: Diode types, resistors and capacitors

The assignments given on 25.04.2014 in the spring semester of 2014, which were stated to be on the final exam, had three topics: diode types (tunnel, varicap, Schottky, photo, LED), resistor types and color codes (carbon, stone, film, integrated, SMD, adjustable and variable resistors; reading 3-, 4- and 5-band resistors) and capacitor types (by dielectric and by capacitance value). In the answer file:

- **Resistor color code:** the first two bands give the first two digits of the value, the third band gives the number of zeros to append (the multiplier), and the fourth band gives the tolerance. As a memory aid, "SoKaKTa SaYaMaM GiBi Ama Görürüm" (black, brown, red, orange, yellow, green, blue, violet, gray, white, gold, silver). Examples: red–yellow–blue–silver = 24 MΩ ± 10%; yellow–violet–brown–gold = 470 Ω ± 5%; blue–gray–black–gold = 68 Ω ± 5%.
- **Capacitors by dielectric:** vacuum (10–1000 pF, up to 10 000 V, radio transmitters), air (adjustable, RF tuning), plastic film (polycarbonate, polyester, polypropylene; signal and filter circuits), mica (50 pF – 20 nF, high voltage and frequency), paper (300 pF – 4 µF, almost no longer used), glass (stable, expensive), ceramic (coupling and filtering, high frequency), aluminum electrolytic (polarized, poor at high frequency), tantalum electrolytic, OS-CON, supercapacitor (carbon aerogel) and "gimmick" capacitor (two wires twisted around each other).
- **By capacitance value:** fixed capacitors and adjustable capacitors (variable, trimmer, varactor).

*Note: The answer file gives "22 kΩ ± 7%" for red–red–orange–gold; the gold band indicates a ± 5% tolerance.*

There is also a short Turkish-language note file from 2009: P- and N-type semiconductors (pulling the valence band up or the conduction band down through doping), the distinction between conductors, semiconductors and insulators, electric current and the convention for current direction, and free electrons in solids.

## Download

The ZIP file contains PDF copies of the homework answers, organized into folders by year, with personal information redacted, as well as the Word file of the 2012 assignment list.
