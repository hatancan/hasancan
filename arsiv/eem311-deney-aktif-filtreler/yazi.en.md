---
baslik: EEM311 Electronics II: Active Filters Lab Manual (40 dB/decade Low-Pass and High-Pass Filters, 300–3000 Hz Band-Pass)
ozet: The "Experiment 8 – Active Filters" manual of the EEM311 Electronics II laboratory: design and simulation of a 40 dB/decade low-pass active filter with a 3 kHz cutoff and a 40 dB/decade high-pass active filter with a 300 Hz cutoff, and a 300–3000 Hz band-pass filter obtained by cascading the two.
---

This post presents the English-language **"Experiment 8 – Active Filters"** manual of the Başkent University **EEM 311 Electronics II** laboratory (the file name is "Experiment10", but the experiment number in the manual itself is 8). The manual was kept together with the Fall 2014 assignment files; it appears that, instead of experiment 8 in the 2010 manuals (frequency response of a common-emitter amplifier), active filter design was done this semester. The original Word file can be downloaded at the end of the post.

## Objective

The objective of the experiment is to gain experience in active filter design. The warning in the manual:

> IMPORTANT!!! Having all knowledge about active filters is a must! You must also declare the equipment list for your design to the teaching assistant at least one hour before the laboratory experiment.

Every student taking the course (a 1-student workload) designs the low-pass and high-pass active filters defined in the preliminary work; in the laboratory, students are divided into groups of two and test their designs (a 2-student workload), after which the filters of two groups are cascaded to obtain a band-pass active filter, which is tested according to the specifications of the first two designs (a 4-student workload).

**Discussion:** The notes given by the instructor on active filter design, the key points, and the relevant sections of the textbook should be read.

## Preliminary Work

1. Design a **40 dB/decade low-pass** active filter with a cutoff frequency of **3 kHz**. Choose suitable values for the resistors and capacitors that can be found at the laboratory technician's (or you may obtain the components yourself).
1. Design a **40 dB/decade high-pass** active filter with a cutoff frequency of **300 Hz**; the same conditions apply for value selection.
1. Test your designs in an electronic simulation program (Electronics Workbench, PSpice, ADS, etc.). Print out, in report form, your calculations, your schematics, your tests showing that the design meets the specifications above, and your comments on the components you chose and the design method.

A slope of 40 dB/decade means that the filters must be **second-order** (each pole contributes 20 dB/decade).

## Experiment

1. The laboratory assistant divides the class into groups of two. Some groups test the design from preliminary work item 1 (low-pass), and others test the design from preliminary work item 2 (high-pass).
1. Then two sides (one testing design 1 and the other testing design 2) cascade their circuits to form a **300–3000 Hz** band-pass active filter and observe whether it works. If it works, they demonstrate it under all conditions they determine themselves (input voltage range, gain/frequency plots, etc.).

## Summary, Report, and Grading

The experiment summary must be written clearly and must include the numbers and names of all group members; the language of the report is free. The **design part constitutes 75% of the grade**.
