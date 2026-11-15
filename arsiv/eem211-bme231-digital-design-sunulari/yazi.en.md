---
baslik: EEM211 Digital Logic Design: BME 231 Digital Design Lecture Slides (Mehmet Yüksekkaya, 2006)
ozet: Weekly slides from the Fall 2006 BME 231 Digital Design course in the Biomedical Engineering Department at Başkent University: number systems, signed numbers and codes, Boolean algebra, Karnaugh maps, decoders and encoders, sequential circuits, registers and counters, ROM, PAL, PLA, RAM, ADC-DAC, and designing one function in seven different ways.
---

This post introduces the weekly slides that instructor **Mehmet Yüksekkaya** used in the Fall 2006 semester in the **BME 231 Digital Design** course of the Biomedical Engineering Department at Başkent University. The files also include two Turkish-language slide sets from a later semester of the same course (MSI and PLD components; synchronous sequential logic), one of which bears the name of İ. Cengiz Koçum. The course textbook is M. Morris Mano's *Digital Design* (3rd edition, Prentice Hall, 2002); most of the figures in the slides come from this book. The topics of each slide set are summarized below; the thirteen PowerPoint files can be downloaded as a ZIP at the end of the post.

## Course information

| | |
|---|---|
| Class hours | Wednesday 14:00–15:50 |
| Textbook | Digital Design, 3rd edition, M. Morris Mano, Prentice Hall, 2002 |
| Attendance + quizzes + homework | 20% |
| Laboratory (pre-lab + lab quiz + report) | 20% |
| Midterm exam | 25% |
| Final exam | 35% |

## Weekly slides

1. **Week 1 – Course introduction and number systems:** course content, definitions, digital circuits, tips for success; conversions between bases (all directions among binary, octal, hexadecimal, and decimal) and exercises.
1. **Week 2 – Signed numbers, codes, and introduction to Boolean algebra:** unsigned and signed numbers, 2's complement representation and integer ranges, BCD, Gray, and ASCII codes, AND and OR gates, Boolean algebra axioms.
1. **Week 3 – Boolean functions and simplification:** basic theorems, De Morgan's theorems, duality, complements of functions, building other gates from NAND and NOR, XOR and XNOR, minterms-maxterms and canonical forms, going from a truth table to an expression, simplification using Boolean rules.
1. **Week 4 – Simplification with Karnaugh maps.**
1. **Week 5 – Gate-level simplification and combinational circuits:** map simplification with don't-care conditions, NAND-NAND and NOR-NOR implementation, code converter and full subtractor design.
1. **Week 6 – Decoders and encoders:** 2-to-4 and 3-to-8 decoders, implementing functions with decoders, a 4-to-16 decoder from two 3-to-8 decoders, 8-to-3 encoder, adder-subtractor circuit, code conversion.
1. **Week 10 – Synchronous sequential logic, registers, and counters:** S-R and D latches, edge-triggered D, J-K, and T flip-flops, asynchronous inputs, output and state equations, state table and diagram, design examples (e.g., a counter that counts in the sequence 00, 11, …, a 4-bit counter that counts from 0 to 10), register with parallel load, shift registers, serial transfer, universal shift register, synchronous and asynchronous (ripple) counters. The end of the slides defines the term project: a report describing the special characteristics of digital integrated circuits (output range, power dissipation, propagation delay, noise margin, etc.), in which each student examines an IC of their choice from its datasheet; due Wednesday, December 27, with a 25% penalty for each day late.
1. **Week 13 – ROM and programmable logic:** ROM internal structure and memory array, implementing functions with ROM, PAL and PLA.
1. **Week 14 – RAM:** RAM interface signals, size, read and write operations, internal structure of RAM, memory hierarchy, square lookup table with ROM, PLA and PAL design examples.
1. **Week 14 – ADC and DAC:** analog and digital concepts, analog-to-digital and digital-to-analog converters, output levels and resolution, sampling and quantization.
1. **Week 14 – Different design examples:** designing a given truth table in seven different ways: with gates, with a decoder, with a 4x1 MUX, with a 2x1 MUX, with a PROM, with a PAL, and with a PLA.

## Two Turkish slide sets from a later semester

- **MSI and PLD components:** definitions of SSI, MSI, LSI, VLSI, adder-subtractor circuit, decoders and encoders, demultiplexer, priority encoder, multiplexers, programmable logic array (PLA) and PLA program table, code conversion.
- **Synchronous sequential logic (İ. Cengiz Koçum):** RS flip-flop with NOR gates, latches and flip-flops, asynchronous inputs, state equations, table, and diagram; five-step sequential circuit design, design with D flip-flops, counter design, state reduction, state assignment, design with unused states, counters with non-binary sequences, registers, shift registers, and the serial adder.
