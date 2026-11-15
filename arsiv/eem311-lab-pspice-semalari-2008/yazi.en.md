---
baslik: EEM311 Electronics II: PSpice Schematics and Resistor Values Table from the 2008 Laboratory
ozet: Ten OrCAD Capture schematics for the MOSFET, JFET–BJT, current mirror, active load, differential amplifier, and frequency response experiments; the standard resistor list used in the laboratory.
---

This post collects **ten OrCAD Capture/PSpice circuit schematics** prepared by classmates during the 2008 term of the Başkent University **EEM311 Electronics II** laboratory. Personal user paths have been cleaned out. Alongside them is the **Standard Resistor Values** table dated 7 September 2005, which was distributed in the experiment folder; the PDF's author metadata has been removed. The files can be downloaded as a ZIP at the end of the post.

The preliminary work and report texts were published earlier in the posts [Experiments 1–4](/arsiv/eem311-lab-raporlari-2008-deney-1-4/) and [Experiments 5–8](/arsiv/eem311-lab-raporlari-2008-deney-5-8/). This package contains editable schematic sources that were not included in those posts.

## Experiment 3: Common-Source MOSFET

`deney3/O.C.DSN` is a common-source amplifier using `nnMOS` from the CD4007 model. The file records a 15 V supply, a 178 kΩ drain resistor, a 50 mV, 1 kHz sine source, and a 10 µF bypass capacitor.

Bias point values saved in the schematic: I_D = 74.01 µA, V_G = 3.409 V, V_D = 1.826 V, V_S = 1.480 V. The resistor divider current is 170.5 µA; the total current drawn from the supply is 244.5 µA. These are old results stored in the file.

## Experiment 4: Two-Stage JFET–BJT Amplifier

There are three schematics:

- `deney4/on-calisma/BIAS.DSN`: DC bias point circuit.
- `deney4/on-calisma/O.C.4.DSN`: transient analysis circuit with coupling and bypass capacitors.
- `deney4/rapor/O.C.4.DSN`: the version saved for the report; the file also contains a 70 mV input setting.

The JFET is **J2N4860** and the BJT is **Q2N3904**. The supply is 12 V, the load is 100 kΩ, and the emitter resistor is 2.2 kΩ. The schematic records show a 0.1 mV, 1 kHz input setting; 10 µF, 22 µF, and 100 µF capacitors are present.

Saved DC values: I_D = 6.135 mA, I_C = 2.842 mA, I_B = 18.55 µA; V_D = 5.865 V, V_S = 2.024 V, V_B = 6.985 V, V_E = 6.292 V, V_C = 9.158 V.

## Experiment 5: MOSFET Current Mirror

`deney5/ONCALISMA.DSN` is a current mirror built with CD4007 MOSFET models. It contains two 5 V sources and a branch with a reference resistor. Among the final saved values are **I_REF = 1.434 mA**, **I_OUT = 1.444 mA**, and a node voltage of **3.566 V**.

The same file also retains numerical records from earlier trials and a `NET0075` error record. For this reason, it should not be assumed that every bias value it contains belongs to a single final run.

## Experiment 6: CMOS Amplifier with Active Load

`deney6/AAAAAAA.DSN` contains `nnMOS` and `ppMOS` models, a 15 V supply, 10 µF coupling capacitors, and 1 MΩ and 100 kΩ resistors. The input setting is 25 mV, 5 kHz. Among the reference resistor trials, 20.16 kΩ and 25.42 kΩ appear.

The file contains bias values left over from multiple trials. The last group of records includes branch currents of approximately 500.5 µA and 557.4 µA, and node voltages of 2.754 V and 12.72 V. The theory of the circuit is explained in the [active-load CMOS experiment handout](/arsiv/eem311-deney-5-6-akim-aynasi-aktif-yuk/).

## Experiment 7: BJT Differential Amplifier

`deney7/OC.DSN` is a differential amplifier with a current source, using four Q2N3904 transistors. It records ±15 V supplies, 9.7 kΩ collector resistors, 2.2 kΩ resistors, and a 4.95 kΩ reference resistor. The two inputs are set as +50 mV and −50 mV sine waves at 1 kHz.

The bias point records include differential pair currents of approximately 984–991 µA, current source branch currents on the order of 1.98 mA, a common emitter voltage of −663.5 mV, and a collector node of approximately 5.452 V.

## Experiment 8: Frequency Response of the Common-Emitter Amplifier

- `deney8/DC ANALIZ.DSN`: DC bias point.
- `deney8/ONCALISMA8.DSN`: preliminary work with coupling and bypass capacitors.
- `deney8/PART D.DSN`: schematic for the part of the experiment with C_E removed.

The model is Q2N3904; R₁ = 8.2 kΩ, R₂ = 3.9 kΩ, R_C = 6.3 kΩ, R_E = 3.3 kΩ, and the supply is 12 V. The files store 10 mV and 20 mV settings for a 1 kHz input.

DC records: I_C = 958.1 µA, I_B = 7.078 µA, I_E = 965.2 µA; V_B = 3.849 V, V_E = 3.185 V, V_C = 5.964 V. From these, V_CE = **2.779 V**.

## The Laboratory's Resistor Values Table

**Standard Resistor Values** is a one-page list with a revision date of 07.09.2005. At the bottom are the addresses of the `~kocaturk` and `~hhatip` course pages at Başkent University. The values it contains:

| Range | Resistors listed in the document |
| --- | --- |
| Below 1 Ω | 0.68 Ω |
| 1–100 Ω | 1.6; 2.2; 2.7; 3; 3.6; 3.9; 4.7; 7.6; 8.2; 10; 15; 20; 25; 27; 33; 43; 47; 51; 56; 68; 75; 91; 100 Ω |
| 100 Ω–1 kΩ | 120; 150; 180; 220; 270; 330; 390; 430; 470; 560; 620; 680; 820; 910 Ω |
| 1–10 kΩ | 1; 1.2; 1.5; 1.8; 2.2; 2.7; 3; 3.3; 3.6; 3.9; 4.7; 5.1; 5.6; 6.2; 6.8; 7.5; 8.2; 10 kΩ |
| 10–100 kΩ | 12; 15; 18; 20; 22; 27; 30; 33; 39; 47; 56; 62; 68; 75; 82 kΩ |
| 100 kΩ and above | 100; 120; 150; 180; 220; 270; 300 kΩ |

*Note: The 7.6 Ω, 25 Ω, and other unusual values in the document have been preserved as they are. This list should not be regarded as a complete E-series standard.*

## About the Schematic Files

The `.DSN` files are OrCAD Capture schematics; they are not in the same format as Proteus schematics, which use the same extension. They contain old model/library paths and simulation records. The CD4007 and JFET models need to be present at the locations referenced in the files; the package does not include all the libraries by itself.

The files were not run here; the numbers in the post are transcribed from the saved schematic properties and the reports of the period. The download package contains ten schematics and one resistor table PDF.
