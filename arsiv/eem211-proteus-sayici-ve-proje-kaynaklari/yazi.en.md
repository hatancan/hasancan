---
baslik: EEM211 Digital Logic Design: Counter, Display, and Logic Project Sources (Elektrotekno PCB Attachment)
ozet: Proteus and ARES source files for traffic light, CMOS logic, and seven-segment display projects.
---

Four Proteus circuits and two ARES PCB source files from the circuit projects of classmates in the EEM211 folder. Personal file names have been neutralized. The traffic file is dated 26 December 2007; the other two DSN files appear in the 2015 archive record, and the last PDS project dates from January 2016. The internal modification record of the last project is 11 January 2016. The ZIP can be downloaded at the end of the post.

## Traffic circuit

The `trafik.DSN` file contains a 4013 D flip-flop, a 4514 decoder, a 74XX191 counter, AND/OR gates, and LED models. It is a project that combines a counter, decoding, and light outputs. The information here was derived from the model records readable in the file; the light durations and operating sequence were not simulated.

## Two CMOS logic project versions

`lojik-proje-1.DSN` and `lojik-proje-2.DSN` are located in different project folders in the source. They contain 4013 flip-flops, NAND gates, LEDs, resistors, and capacitors. The first version also has a reference to a variable resistor model. Since the files are not identical, both have been preserved.

The file names of these two sources contained personal information; these were not used in the download file and ZIP paths. The text records inside them were also checked separately.

## Digital logic project

`sayisal-mantik.pdsprj` contains model references to a 74XX74 D flip-flop, AND, OR, inverter, 4511 decoder, and common-cathode seven-segment display. It is a source record belonging to digital design work that connects flip-flop outputs to a display driver.

## Scope of review

This publication preserves the editable sources. The circuits were not run; no conclusion was drawn from the model names inside about the correctness of all connections or that the circuit produces a particular counting sequence. Manufacturer libraries, datasheets, and program installers were not added to the package. The XML customer ID field of the PDS project was zeroed out.


## ARES PCB attachments

`lojik-proje-pcb.LYT` is the printed circuit board design in the project folder. Personal names stored as text on the board have also been removed.

`trafik-isigi-pcb.LYT` is the ARES drawing stored in the source folder together with the elektrotekno.com schematics. The source context of this attachment is explained in the [traffic light schematics post](/arsiv/eem211-trafik-isigi-devreleri/). Since the layout file could not be opened in this environment, it was not verified which schematic version it matches exactly.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*
