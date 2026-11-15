---
baslik: EEM211 Digital Logic Design: "Digital Design" Slides, Chapters 1–4 (Metin Artıklar, 2006)
ozet: Assist. Prof. Dr. Metin Artıklar's Digital Design lecture slides: binary number systems, complements, signed numbers and codes; Boolean algebra, canonical forms and logic gates; Karnaugh maps, don't-care conditions, NAND/NOR implementation; combinational circuits (adder, subtractor, BCD adder, multiplier, comparator, decoder, encoder, multiplexer).
---

This post presents the four PDF slide decks in the "ege_notlari" folder of the EEM211 Digital Logic Design course: the first four chapters of the **"Digital Design"** course prepared by **Assist. Prof. Dr. Metin Artıklar** (April 2006). The documents do not state which university the slides were presented at; the order of topics and the examples follow M. Morris Mano's *Digital Design* textbook. There are about 280 slides in total; the headings and scope of each chapter are summarized below. The four PDFs can be downloaded as a ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed upon the request of the rights holder.*

## Chapter 1: Binary Systems

Digital systems are used in almost every field, from communications to healthcare, business, and the internet; their most important characteristic is that they operate on a finite number of data values (e.g., a thermometer displaying temperature using the digits 0–9). The topics of the chapter:

- numbers in binary, base-r numbers, and the radix of numbers;
- conversion of decimal numbers to base r, conversion of fractional numbers;
- conversion of base-2 numbers to base 8 and 16, and of base-8 and base-16 numbers to base 2;
- complements of numbers: (r−1)'s and r's complement, subtraction using complements;
- signed binary numbers: signed-magnitude, 1's complement, and 2's complement methods; addition and subtraction of signed numbers;
- binary codes: BCD and other weighted codes, Gray code, error-detection codes (odd and even parity bits);
- registers (information storage) and introduction to binary logic: AND, OR, NOT (complement) operations.

## Chapter 2: Boolean Algebra and Logic Gates

- Basic definitions: binary operator, axioms, examples of algebraic structures.
- Boolean algebra and two-element Boolean algebra; closure, commutative, identity element, distributive, and complement properties; differences from ordinary algebra.
- Duality principle, basic theorems, De Morgan's law, operator precedence.
- Boolean functions, algebraic simplification, complement of functions (e.g., F1 = x'yz' + x'y'z).
- Canonical and standard forms: minterms and maxterms, writing and implementing functions in terms of minterms and maxterms.
- Other logical operators and logic gates, gates with more than two inputs, positive and negative logic.
- Integrated circuits, IC manufacturing technologies, and computer-aided circuit design.

## Chapter 3: Simplification of Boolean Functions

- Karnaugh map (K-map) method: 2-, 3-, and 4-variable maps.
- Prime implicants.
- Simplification of functions in sum-of-products and product-of-sums forms.
- Don't-care conditions; e.g., F(w, x, y, z) = Σ(1, 3, 7, 11, 15) and don't-care terms.
- NAND and NOR implementation: building AND, OR, and NOT gates from NAND, the two different representations of the NAND gate, two-level and multilevel NAND circuits.
- XOR and XNOR gates, building XOR from NAND, odd and even parity generators and checkers using XOR.

## Chapter 4: Combinational Circuits

- The difference between combinational and synchronous sequential circuits; single-output and multiple-output combinational circuits.
- Analysis of combinational circuits (finding the truth table and output functions) and design steps; as an example, a BCD-to-excess-3 code converter.
- Binary adders and subtractors: synthesis of half and full adders, n-bit adders, anticipating the carries of higher stages (carry lookahead; Sᵢ = Cᵢ ⊕ (Aᵢ ⊕ Bᵢ)), binary subtractors and the overflow flag.
- BCD adders and the carry (C) condition, binary multipliers, magnitude comparator.
- Decoders and implementing functions with decoders, encoders and encoder design.
- Multiplexers (MUX): 2x1 and 4x1 multiplexers, quadruple 2x1 multiplexer, implementing Boolean functions with multiplexers (e.g., F(x, y, z) = Σ(1, 2, 6, 7) and F(A, B, C, D) = Σ(1, 3, 4, 11, 12, 13, 14, 15)).
- High-impedance (three-state) outputs.
