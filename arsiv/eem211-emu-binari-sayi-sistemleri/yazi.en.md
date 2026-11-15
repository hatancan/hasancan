---
baslik: EEM211 Digital Logic Design: Binary Number Systems and Logic Circuits (EMU Web Note)
ozet: Digital waveforms, base conversions, gates, Karnaugh maps, and twelve laboratory experiments.
---

Saved from Eastern Mediterranean University (Doğu Akdeniz Üniversitesi) at `sct.emu.edu.tr/ilkan/ex/kitap134.htm`, this is the course text "Binary Number Systems". The page has no explicit author or publication date; the file's archive date of 25 December 2006 was used. It contains theory notes, worked examples, twelve experiments, and practice questions. The text-only HTML version without images can be downloaded at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request by the rights holder.*

## Digital signals and time measurements

The binary system uses 0 and 1. In its example circuits, the source represents these levels with 0 V and 5 V. Rise time is the time between the 10% and 90% levels of the pulse, and fall time is the time between the 90% and 10% levels. Pulse width is measured between the 50% points of the two edges.

The concepts of period T, frequency f=1/T, and duty cycle DC=tw/T are illustrated with examples. A signal with T=10 ms has a frequency of 100 Hz; if tw=1 ms, the duty cycle is 10%. A 10 kHz clock produces 1000 pulses in 100 ms.

## Serial and parallel data transfer

In serial transfer, bits are sent one after another over a single line; in parallel transfer, they are sent together over separate lines. In the source's 100 kHz example, one bit time is 0.01 ms; serial transfer of eight bits is given as 0.08 ms.

*Note: In the parallel transfer row of the same example, the source writes "0.01ms = 10ms". The correct conversion is 0.01 ms = 10 µs.*

## Number systems and conversions

The place weights of binary numbers are 1, 2, 4, 8, and so on. The hexadecimal system uses the characters 0–9 and A–F. Four bits correspond to one hexadecimal digit.

| Conversion in the source | Result |
| --- | --- |
| 77 (decimal) | 1001101 (binary) |
| 0010 0111 (binary) | 27 (hexadecimal), 39 (decimal) |
| 1C (hexadecimal) | 28 (decimal) |
| 650 (decimal) | 28A (hexadecimal) |

The results of these examples were recomputed and verified. In binary addition, 1+1=10, that is, the sum bit is 0 and the carry is 1.

## Logic gates and example designs

The symbols and truth tables of the NOT, AND, NAND, OR, NOR, XOR, and XNOR gates are given. n inputs have 2ⁿ different combinations. XOR produces 1 when its two inputs differ, and XNOR produces 1 when they are the same.

The application problems use the fill levels of two water tanks, the landing-gear sensors of an aircraft, and an equality check of two four-bit numbers. In each design, the physical condition that a sensor output represents with 1 is defined separately.

## Boolean algebra and standard expressions

The commutative, associative, distributive, and De Morgan laws are applied to circuit simplification. A sum of products is SOP, and a product of sums is POS. In a standard term, every variable appears either in its true or complemented form.

In the map method, 4, 8, and 16 cells are used for 2, 3, and 4 variables, respectively. The 1s are grouped into adjacent groups whose sizes are powers of two; the variables that do not change within a group give the resulting term. The adjacency of opposite edges and the fact that the same cell can be used in more than one group are explained.

## Combinational circuits

Examples cover going from a function to a circuit, from a truth table to a function, and from a given circuit to a smaller implementation. The universality of NAND and NOR gates is demonstrated by designing with only a single gate type.

A half adder produces a sum and a carry from two inputs. A full adder also accepts the carry from the previous stage. The comparator, encoder, decoder, and seven-segment display driver topics lead to larger functional blocks. The last theoretical section introduces the concepts of flip-flops, counters, and shift registers.

## Laboratory experiments

| Experiment | Content |
| --- | --- |
| 1 | Integrated circuit connections; 7404, 7408, 7432 |
| 2 | NOT gate with the 7404 |
| 3 | AND gate with the 7408 |
| 4 | OR gate with the 7432 |
| 5 | XOR gate with the 7486 |
| 6 | Comparing four-bit numbers using XOR |
| 7 | Output tables of combinational logic circuits |
| 8 | Obtaining NOT, AND, and OR from NAND |
| 9 | Obtaining NOT, AND, and OR from NOR |
| 10 | Half adder with the 7408 and 7486 |
| 11 | Four-bit addition with the 7483 |
| 12 | 7447 and a common-anode seven-segment display |

Each experiment includes an objective, brief background, a list of equipment, a connection diagram, and a table to fill in. The final practice questions combine number bases, waveforms, gate faults, simplification, Karnaugh maps, and display design.

*Note: Some formulas and overbars in the saved page are given as embedded images. Because these marks were lost in plain-text extraction, ambiguous algebraic examples were not reconstructed here. A sub-caption in the source's NOR experiment also uses the word "NAND"; the context of the section is the NOR experiment.*
