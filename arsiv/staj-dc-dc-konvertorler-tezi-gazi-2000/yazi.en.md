---
baslik: INTERNSHIP Summer Internship: DC/DC converters graduation thesis (Gazi University Faculty of Technical Education, 2000)
ozet: A 77-page DC/DC converters thesis prepared in 2000 at Gazi University Faculty of Technical Education: classification by current-voltage direction, buck, boost, buck-boost, CUK and full-bridge converters, flyback and forward converters, and pulse-commutated converters.
---

This post introduces a 77-page thesis titled **"DC/DC Converters"**, prepared in 2000 in the Electronics program of the Electronics-Computer department at Gazi University Faculty of Technical Education, under the supervision of Asst. Prof. Dr. Yılmaz Savaş. The thesis was found among the internship files and gives a compact account of the theory of converter circuits; it is related in subject matter to the converter and inverter circuits examined at TCDD EAM (see [24 V/12 V converter test](/arsiv/staj-tcdd-eam-24v-konvertor-testi-hemzemin-gecit-sema/)). The author's name and student number have not been published, as the cover and jury pages were removed; these two pages are left blank in the downloadable PDF. For the full text, formulas and figures, see the PDF at the end of the post.

*This content belongs to a third-party source (Gazi University Faculty of Technical Education, 2000; supervisor Asst. Prof. Dr. Yılmaz Savaş); it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*

## Abstract

In electrical systems, the electrical power delivered to a load must be controlled. One way of controlling power is to convert power from one voltage level to another. In alternating current (AC), this conversion is done efficiently with transformers; however, transformers cannot be used for direct current (DC/DC) power conversion. The thesis aims to examine DC/DC converters in terms of load current and voltage; the major part of the study is devoted to converter types operating in switching mode, which are divided into five groups according to the function they perform.

Switch-mode converters are needed in order to perform DC/DC power conversion efficiently. Power converters consist of reactive elements and switches; the operating principle is based on adjusting the on and off times of the switches used in the circuit. If the frequency of the voltage feeding the load is high, practically uninterrupted DC power transfer to the load becomes possible. Satisfactory operation of such converters depends on a suitable configuration of the reactive elements and on suitable switching methods.

*(The thesis also includes an abstract in English.)*

## Contents

**Chapter 1: Introduction**

**Chapter 2: Classification of DC-DC converters**

1. Converters by direction of current and voltage flow: Class A, B, C, D and E converters
1. Converters by the operation they perform:
   buck converter (continuous current mode, boundary between continuous and discontinuous conduction, discontinuous conduction, distortions in the output voltage);
   boost converter (continuous conduction, continuous/discontinuous conduction boundary, discontinuous conduction, effect of parasitic elements, output voltage ripple);
   buck-boost converter (same subheadings);
   CUK DC-DC converter;
   full-bridge DC-DC converter (bipolar and unipolar voltage-switching PWM)
1. Comparison of DC-DC converters

**Chapter 3: Magnetically coupled choppers:** flyback converter (circuit analysis, continuous current mode, ripple in the capacitor voltage) and forward converter (circuit analysis, continuous current mode, ripple in the capacitor voltage)

**Chapter 4: Pulse-commutated and resonant converters:** pulse-commutated converter, three-thyristor pulse-commutated converter, pulse-commutated converter independent of charging current, resonant pulse converter

**Chapter 5: Conclusion and evaluation**, **References**

## Comparison of converters (Section 2.3)

According to the comparison section of the thesis, the basic structures of the buck, boost, buck-boost and CUK converters allow only **unidirectional** energy transfer, because they can carry current and voltage in only one direction. In the **full-bridge** converter, the directions of V_o and I_o can be changed independently of each other, so multi-directional power transfer is possible; since it can operate in all four quadrants of the plane whose axes are V_o and I_o, it can also be used as a DC/AC converter. The following conclusions are drawn from the operation of the examined converters:

1. The average current I_o is at its designed maximum value; the ripple in the inductor current is negligible (i_L(t) = I_L), which ensures continuous conduction.
1. The average voltage V_o is at its designed maximum value; if the ripple in V_o is neglected, v_o(t) = V_o.
1. When the input voltage V_d changes, the duty ratio must be controlled so as to keep V_o constant.

According to the switch utilization factor (P_o/P_T) graphs, the switch utilization of the buck and boost converters is good when the input and output voltages are close to each other; in the buck-boost and CUK converters, the switch utilization is 0.25 for D = 0.5 (V_o = V_d).

## Magnetically coupled choppers (Chapter 3)

The basic chopper types are suitable for cases where electrical isolation is not required and the output voltage does not differ much from the input; if one or more of these conditions are needed, magnetically coupled circuits (flyback and forward) are the better choice. The flyback converter has been used for many years to supply high voltage at low power to television screens and other cathode-ray tube applications. The switch is on for DT and off for (1−D)T; while the switch is on, the primary current increases with a slope of (V_d/L1) A/s, and when the switch opens, the stored magnetic energy is transferred to the load through the secondary winding and the diode. In the selection, output power and input voltage are the two main factors; complex circuits are generally suitable for higher powers.

## Conclusion and evaluation

Power converters that obtain DC voltage from AC are called **rectifiers**, those that obtain AC from DC are called **inverters**, and those that obtain DC voltage of a different value from DC are called **converters**. Converters are indispensable in many devices in industry; power transfer in DC systems is done with DC/DC converters. A converter can be thought of as the equivalent DC circuit of an AC transformer with a continuously variable turns ratio: it can increase or decrease the voltage of a DC source. Converters are named buck, boost, buck-boost, CUK and full-bridge according to the proportion of power delivered to the output; since their outputs can be either fixed or adjustable, they have found wide use in practice.

## References (selected)

- Mohan N., Undeland T. M., Robbins W. P., *Power Electronics: Converters, Applications and Design*, John Wiley & Sons, 1989.
- F. F. Mazda, *Electronics Engineer's Reference Book*, 6th edition, Butterworths.
