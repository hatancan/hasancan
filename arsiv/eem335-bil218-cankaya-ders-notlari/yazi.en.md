---
baslik: EEM335 Computer Organization: BİL218 Lecture Notes, Weeks 1.5–9 (Çankaya University, Assoc. Prof. Dr. Ersin Elbaşı)
ozet: Çankaya University BİL218 Computer Organization lecture notes: machine instruction characteristics, instruction cycle and interrupts, bus, memory hierarchy and cache, processor organization and pipeline, RISC/CISC, superscalar, addressing modes, multicycle; syllabus and Homework 2.
---

From the "ersin" subfolder of the EEM335 folder: weekly lecture slides (Weeks 1.5, 2, 3, 5, 6, 7, 8 and 9) for the **Çankaya University, BİL 218 Computer Organization** course, prepared by **Assoc. Prof. Dr. Ersin Elbaşı**, along with the course syllabus and the "Homework 2" sheet. The textbook is Stallings, *Computer Organization and Architecture: Designing for Performance* (8th edition, 2010), and the supplementary book is Tanenbaum, *Structured Computer Organization* (5th edition, 2006). All slide and syllabus PDFs can be downloaded as a ZIP at the end of the post. The grade sheet (student grades) in the same folder has not been published.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## Syllabus (BİL 218)

Topics: computer organization and architecture, evolution of the computer, components, processor/datapath/control, cache, instruction set characteristics, addressing modes, microprocessor organization (CISC) and pipeline, pipeline performance, RISC and pipeline, instruction-level parallelism, IA-64 architecture, control unit, microprogrammed control. Assessment: midterm 30%, attendance 5%, homework 30%, final 35%.

## Week 1.5 – Machine instruction characteristics, operand types, assembly

The set of all instructions of a processor is called the **instruction set**. The components of an instruction are: the **opcode** (operation), source operand(s), result operand(s), and the next instruction. Operands can be in memory, in a CPU register, or in an I/O device. Abbreviations for opcodes are called **mnemonics** (ADD, SUB, MPY, DIV, LOAD, STOR). Instruction types: data processing (arithmetic/logic), data storage, data movement (I/O), and control (test and branch). Number of addresses: 3-address `OP A,B,C` (A ← B OP C), 2-address `OP A,B` (A ← A OP B), 1-address `OP A` (AC ← AC OP A), 0-address (stack).

## Week 2 – Components, instruction cycle, interrupts, bus

Hardwired systems are not flexible; general-purpose hardware performs different tasks depending on control signals. The microprocessor operates in two steps: **fetch** (get the instruction) and **execute** (run it); together these are called the **instruction cycle**. The PC holds the address of the next instruction. Interrupts and bus design criteria are also covered this week.

## Week 3 – Memory and cache

Memory characteristics: location (processor, internal, external), capacity (word size, number of words), unit of transfer (word/block), **access method** (sequential – tape; direct – HDD, CD; random – main memory; associative – cache), performance (access time, cycle time, transfer rate), physical type, volatility, and organization. Next come the memory hierarchy and cache design elements: size, mapping function, replacement algorithms, write policy, line size, and number of caches.

## Week 5 – Processor organization and pipeline

The tasks of the processor: fetch instruction, interpret instruction, fetch data, process data, write data. **User-visible registers:** general-purpose, data, address (segment, index, stack pointer), and condition codes (carry, overflow, sign…). **Control and status registers:** PC, IR, MAR, MBR, and the program status word (PSW; sign, zero, carry, equal, overflow, interrupt enable, supervisor mode). The instruction cycle consists of the fetch, execute, and interrupt stages; the instruction pipeline is covered next.

## Week 6 – RISC

Reasons for the evolution of CISC (the *semantic gap* between high-level languages and hardware); dynamic analysis of programs: assignments dominate execution, conditional branches are used frequently, and procedure calls/returns consume a lot of time; most operands are local scalar variables (an average of 55% in Pascal and C). **RISC** characteristics: a large number of general-purpose registers, a compiler that optimizes register usage, a small number of simple instructions, and better pipeline performance. The section covers the large register file, compiler-based register optimization, the RISC pipeline, and a RISC–CISC comparison.

## Week 7 – Superscalar

In a superscalar architecture, integer and floating-point arithmetic instructions and conditional branches are executed independently and simultaneously (instruction-level parallelism); it is more common in RISC. Topics: superscalar vs. superpipeline comparison, problems in parallel execution, instruction issue policies, **register renaming**, machine parallelism, and **branch prediction**.

## Week 8 – Addressing modes and instruction formats

Basic addressing modes: **immediate, direct, indirect, register, register indirect, displacement, stack**. In addressing design, trade-offs are made among address range, flexibility, number of memory references, and complexity of address computation. Pentium and PowerPC addressing modes and instruction formats are also covered.

## Week 9 – Multicycle and interrupts

In multicycle operation, each instruction is completed in multiple steps; each step finishes in one clock cycle, instructions may use different numbers of cycles, and a functional unit (a single memory, a single ALU) can be shared across multiple cycles within an instruction; data is carried in registers between cycles. Interrupt generation is covered next.

## Homework 2 (BİL 218) questions

1. What is the basic function of computers, and how do they perform it?
2. What is an interrupt, and what are multiple interrupts? What happens if an interrupt occurs while the computer is performing its function? Explain with a diagram.
3. What is a bus, and what are its architecture types?
4. Draw the computer memory hierarchy and explain it with its advantages and disadvantages.
5. Explain the access methods and give a mathematical example for each.
6. What is cache memory, and how does it work?
7. What is cache mapping, and what are its types? Explain each with an example.

(In addition to the lecture notes, the questions are expected to be answered in detail using other sources.)
