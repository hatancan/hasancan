---
baslik: EEM211 Digital Logic Design: Ten Experiments for Logic Circuits (Handout of Unspecified Source)
ozet: A 68-page laboratory handout covering everything from TTL and CMOS characteristics to counters and registers.
---

The 2005 document "LOJIK DEVRELER.pdf" is a 68-page handout covering the physical implementation of gate circuits and ten laboratory experiments. The document does not state who prepared it or which institution it comes from; it was archived as third-party course material found in the EEM211 folder. The PDF creation date is 4 February 2005. The complete document can be downloaded at the end of this post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes, with the source credited. It will be removed at the request of the rights holder.*

## Introduction: Implementing Logic Gates

Throughout the handout, positive logic is used: the voltage representing logic 1 is greater than the voltage representing logic 0. Diode AND/OR circuits, bipolar transistors as switches, DTL and TTL gates, and MOS and CMOS structures are covered.

The model used assumes that a diode conducts in the forward direction at a voltage of approximately 0.7 V. For the transistor, the relation IC=βIB is written for the active region; once saturation is reached, the external circuit limits the collector current. In the example with a 5 V supply, IC=(5−VCEsat)/RC, with VCEsat taken as approximately 0.2 V. In the inverter, the output is high when the input is low, and the output is low when the input is high enough to drive the transistor into saturation.

## 1. TTL and CMOS Gate Characteristics

The static and dynamic behavior of the gates is examined. Work is done on input/output voltages, current values, and propagation delays. A ring configuration built from an odd number of NOR gates is used for delay measurement. Before the experiment, students are asked to simulate the circuits in a CAD environment and to examine the characteristics of the integrated circuits to be used.

## 2. Combinational Circuit Analysis

The Boolean function and truth table of the given gate circuit are derived. Input combinations are applied on the experiment board, and the measured outputs are compared with the expected results. In this way, the relationship among the schematic, the algebraic expression, and the table is tested.

## 3. Combinational Circuit Synthesis

A logic function is constructed from the desired input/output behavior, simplified, and implemented with gates. In the preparation, students are asked to examine the functions with tools such as MORP and Espresso and to carry out a CAD simulation. It is essential that the simplification result does not change the truth table.

## 4. MSI Decoders, Multiplexers, and Encoders

Decoder, multiplexer, and encoder integrated circuits are used as blocks. The effect of the select and enable inputs on the output is investigated. The approach of implementing logic functions not only with basic gates but also with ready-made MSI function blocks comes to the fore.

## 5. Addition, Subtraction, and Comparison

Half and full adders, parallel addition, subtraction, and magnitude comparison are covered. The two-bit parallel adder prepared before the experiment is built on the experiment board. The sum and carry outputs are verified with various input combinations; the block connections of wider arithmetic structures are examined.

## 6. Implementation and Analysis of Memory Elements

The idea of storing information with feedback gate circuits is introduced. The inputs, outputs, state-holding and state-changing behaviors of latches and flip-flops are examined. Unlike in combinational circuits, the effect of the previous state on the next output is observed.

## 7. Synchronous Sequential Circuit Analysis

For a given sequential circuit, the flip-flop input functions, next states, and outputs are determined. By following the changes of state with clock pulses, the state table is compared with the experimental results.

## 8. Synchronous Sequential Circuit Synthesis

States and transitions appropriate to the specified behavior are selected. The excitation functions of the memory elements are obtained and simplified. The design is checked in simulation and on the experiment board. The preparation, implementation, and measurement steps are given separately in the handout.

## 9. Asynchronous and Synchronous Counters

In counter circuits, the effects of the state sequence and the clock connections are compared. In the asynchronous structure the stages trigger one another, whereas in the synchronous structure a common clock is used. The experiments aim to observe the counting sequence and the change of the outputs over time.

## 10. Registers

In the final experiment, information storage and shifting operations are covered. The word "yazıcı" used in the handout means register in this context (the Turkish term "yazmaç" is also used for it). Before the experiment, circuit simulation, integrated circuit examination, and testing of the operating states of the built circuit are required.

## References

At the end of the handout, the books by Ahmet Dervişoğlu, Friedman–Menon, Barry Wilkinson, Kuntman–Toker–Özcan, Ercegovac–Lang, M. Morris Mano, and Richard Tinder are listed as sources. These are the handout's own references; they were not used in place of information about the person or institution that prepared the handout.
