---
baslik: EEM202 Circuit Theory II: Experiment, Three-Phase, Transformer and Cooling Circuit Sources
ozet: Proteus source files for the EEM202 experiments, HW3–HW4, and the laptop cooler project.
---

Proteus source files for the experiment, homework, and project work in the EEM202 folder. Eight circuit files that complement the previously archived reports are presented together here. The 2014 experiment and homework files and the 2015 cooler project are in the same package; the 17 April 2015 date from the internal record of the final project was used. The ZIP can be downloaded at the end of the post.

## Experiment 1–3 sources

`deney1.pdsprj`, `deney2.pdsprj`, and `deney3.pdsprj` are the editable circuit sources of the laboratory folders. They contain resistor, capacitor, inductor, signal source, and measuring instrument models. The related preliminary work and recorded measurements can be found in the [laboratory work post](/arsiv/eem202-deney-calismalari/).

*Note: The source projects may represent more than one working version. It was not assumed that the initial values in the files and the report screens represent the same condition; the projects were not run here.*

## HW3: three-phase and single-phase circuits

`HW3.pdsprj` and `TEK FAZLI DEVRE.pdsprj` come from the same homework folder. The files contain sinusoidal sources, resistor/inductor loads, and AC measuring instruments. The HW3 record also contains transformer model references. The questions and results of the homework can be read together with the [PSpice homework](/arsiv/eem202-pspice-odevleri/) and the [HW3–HW4 reports](/arsiv/eem202-pspice-odev-3-4-raporlari/).

In the three-phase work, the relationship between phase voltages, line/phase quantities, and the load connection are decisive. The single-phase file is kept separately for comparison; the file name and source folder show this distinction.

## HW4: transformer study

`HW4.DSN` and `HW4.pdsprj` are two source formats for the same study. Both contain model records related to a sinusoidal source, a transformer, and AC measuring instruments. The DSN schematic file and the PDS project container were kept separate; since the file types differ, one was not counted as an unnecessary copy of the other.

## Laptop cooler project

`devre2proje.pdsprj` is the circuit source of the [cooler project report](/arsiv/eem202-proje-dizustu-bilgisayar-sogutucu/). The internal model references include an NTC, an op-amp, a rectifier bridge, a 7812 regulator, a transformer, an adjustable resistor, and a DC fan. The temperature sensing, comparison, and fan driving sections of the project are associated with these components.

## File format

The PDS project files contain PROJECT.XML, schematic/data records, and auxiliary project components. Only the source projects were included; backups and temporary working files were not taken. The customer ID field in the project XML was zeroed out. The download may require models from older Proteus versions; no simulation results were produced in this round.
