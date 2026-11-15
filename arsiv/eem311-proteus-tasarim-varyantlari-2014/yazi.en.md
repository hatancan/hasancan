---
baslik: EEM311 Electronics II: Additional Proteus Variants of the 2014 Design Assignment
ozet: Eight additional Proteus DSN files for the band-pass filter, notch filter, narrow-band filter, power supply, and ECG amplifier; different components and test settings in the 2014–2015 assignment.
---

This post contains **eight additional Proteus schematics** prepared by classmates for the 2014 fall design assignment of the **EEM311 Electronics II** course at Başkent University. The dates in the files range from 27 December 2014 to 3 January 2015. The files that passed a personal-information check can be downloaded as a ZIP at the end of the post. Compared with the earlier [Proteus design sets](/arsiv/eem311-odev-2014-proteus-tasarimlari/), these files differ in components, connections, or test settings; copies of identical files were not included in the package again.

The assignment questions and report descriptions are in the [2014 filter and oscillator design assignment post](/arsiv/eem311-odev-2014-filtre-osilator/).

## Band-pass filter: Two separate versions

`311/soru2.DSN` is an early version dated 27 December 2014. Compared with `soru2` in the existing design package, some resistors are **11 kΩ** instead of 22.5 kΩ and some capacitors are **1 µF** instead of 0.2 µF; the source and measurement setup also differ.

`odev/proteus cizimleri/soru2.DSN` is the report version dated 2 January 2015. It contains **1.5 kΩ, 1.8 kΩ, and 0.9 kΩ** resistors and **1 µF** capacitors. The report describes cascading low-pass and high-pass stages to target the **85–1050 Hz** range. The report's resistor and capacitor choices should be read together with this version; the test settings in the file are not, on their own, the filter's measured cutoff frequency.

## Notch filter

`odev/proteus cizimleri/soru3.DSN` is a schematic dated 3 January 2015. Unlike the earlier package's solution using the LM741, this file uses the `OA_3PIN` ideal op-amp model. The saved test source is **5 V, 1 kHz**.

The related report aims to reject the **256–2304 Hz** band for a flute sound; the output of the band-pass stage is subtracted from the input. The choices in the report are: C₁ = 0.1 µF, C₂ = 0.2 µF, R₁ = R₂ = 0.50 kΩ; in the other stage, C₃ = C₄ = 0.5 µF, R₃ = 1.25 kΩ, R₄ = 0.625 kΩ.

## Narrow-band filter

There are two files: `e311/soru4.DSN` (28 December 2014) and `odev/proteus cizimleri/soru4.DSN` (2 January 2015). Their content is not the same as the `50 Hz.DSN` file in the earlier package. In the later version, the measurement setup has been expanded and the source settings have been changed.

The design in the report uses **f_c = 104.2 Hz**, C₁ = C₂ = 0.1 µF, R₁ = R₄ = 15.27 kΩ, R₂ = 0.80 kΩ, and R₃ = 290 kΩ.

*Note: Although the report describes the target as an FM radio channel, the given calculation is for 104.2 Hz. There is a factor of one million between this and 104.2 MHz; the file has not been verified as an RF channel selector.*

## Power supply: Two versions

`311ek/5 (25)+/olan.DSN` is a version dated 30 December 2014. In this file, the amplitude of the 50 Hz source is recorded as **22 V**; the schematic of the same name in the earlier package has **220 V**. There are also differences in the diode and connection layout.

`odev/proteus cizimleri/soru5.DSN` is a version dated 3 January 2015. The source setting is **220 V, 50 Hz**; it contains a transformer, a rectifier, and measurement elements. The report describes the transformer stepping the voltage down, the bridge diode rectifying, and the output capacitor smoothing; the stated targets are 5 V and at most 400 mA.

*Note: In the assignment question the upper limit is 300 mA, whereas the report says 400 mA. Smoothing with resistors and capacitors alone does not provide voltage regulation under a varying load. The presence of model definitions in the files does not, by itself, prove that all of those parts are connected in the final circuit.*

## ECG amplifier

`e311/soru6.DSN` is a version dated 28 December 2014. Compared with the 2 January version in the earlier package, the measurement/recording components and connection records differ. The file contains an **AD624** model and a **2 V, 1 kHz** sine test setting. These settings are the saved trial conditions of the file; they should not be taken as a measurement result showing that the ECG amplitude/frequency requirements of the assignment are met.

## Package contents

| Folder | Files |
| --- | --- |
| 311 | soru2.DSN |
| 311ek/5 (25)+ | olan.DSN |
| odev/proteus cizimleri | soru2.DSN, soru3.DSN, soru4.DSN, soru5.DSN |
| e311 | soru4.DSN, soru6.DSN |

The schematics are in Proteus ISIS format. The circuits were not run during this archiving; the differences were determined by comparing the schematic records, and the descriptions come from the report of the same assignment.
