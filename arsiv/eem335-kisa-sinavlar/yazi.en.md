---
baslik: EEM335 Computer Organization: Quizzes and Answers (2003–2009), Hamming Code Questions
ozet: EEM335 Computer Organization quiz questions and answers, 2003-2009: Von Neumann machine, cache mapping (direct, set associative) calculations, DMA, memory types, memory map, CD land-pit, Hamming code.
---

Quiz papers from 2003–2009 for the **EEM335 Computer Organization** course at Başkent University; most come with answer keys, so the questions are worked out. The course is taught by Prof. Dr. Emin Akata. Multiple copies of the same exam were counted only once; the original PDFs are in the ZIP file at the end of the post. Drawings (block diagrams, memory connection diagrams) could not be rendered as text, so the original PDF should be consulted.

## Quiz 1 – 5 November 2003

1. **What significance does the "Von Neumann Machine" have within the concept of computer architecture?** ENIAC's program was supplied externally through hardware connections, and programming it was very difficult. Von Neumann, who was an advisor on the ENIAC project, and his colleagues proposed a new structure called the "IAS Computer," in which the program is also kept in memory and executed from there. This **stored program concept** became the model for all subsequent computer architectures.
2. **How many generations is the evolution of computers classified into?** Although there is no consensus on the definitions after the third, there are 5 generations: (1) vacuum tube, (2) transistor, (3) SSI-MSI integrated circuits, (4) LSI, (5) VLSI.
3. **What does Moore's law predict?** Moore, one of the founders of Intel, observed that the number of transistors that can be placed on an integrated circuit doubles every year.
4. **What is the average read/write time for 2 KByte of data on a disk with an average access time of 2 ms and a transfer rate of 10 Mbit/s?** T_N = T_A + N/R. N = 2·1024·8 = 16384 bits, R = 10·1,048,576 = 10,485,760 bit/s: T = 2·10⁻³ + 16384/10,485,760 = 0.0035625 s = **3.5625 ms**.

## Quiz 2 – 24 December 2003

1. **Why is interrupt-driven DMA more efficient than programmed I/O for multi-word data transfers?** In programmed I/O the CPU takes on the entire operation and cannot do any other work. In interrupt-driven I/O the CPU is freed from the waiting loop, but the data transfer still falls to it. In DMA the CPU delegates the I/O task to the DMA module; the DMA module uses the system bus at moments when the CPU is not using it, or by *cycle stealing*.
2. **What is the difference between memory-mapped I/O and isolated I/O?** Isolated I/O uses IOR/IOW signals and special I/O instructions; I/O units and memory can be connected to the same addresses. Memory-mapped I/O has no special instructions; memory instructions and MEMR/MEMW signals are used, and part of the address space is reserved for I/O. Its advantage is that the powerful memory instructions can also be used for I/O, and its disadvantage is the loss of memory space; for isolated I/O the opposite holds.
3. **How many kinds of scheduling are performed in operating systems?** Long-term (jobs are given process status and enter the short-term queue), medium-term (swap-in/swap-out scheduling), short-term (processes are executed efficiently through time sharing, or suspended).
4. **If one bus cycle is 5 ms, how long does the transfer of one word take in two different DMA configurations?** If there is a separate bus between the DMA and the I/O modules, (a) only the memory access uses the system bus: **5 ms**. If the same bus is shared, (b) one read and one write take 2 bus cycles: **10 ms**.

## Quiz 1 – 17 October 2007

1. The first 4 generations: **1st generation** electronic, vacuum tubes, machine language, stored program; **2nd generation** transistors, core memory, high-level languages; **3rd generation** integrated circuits, semiconductor memory, multiprocessing; **4th generation** VLSI structures, microprocessors, network structures, optical disks.
2. The Von Neumann machine keeps the program and the data together in memory (stored program concept); the instructions in memory are executed through the Arithmetic Logic Unit and the Program Control Unit, and I/O connections are provided by a control unit.
3. CPU registers: **PC** (address of the next instruction), **IR** (instruction being executed), **MAR** (memory address to be read/written), **MBR** (word to be written to memory or read from memory), **I/O AR** and **I/O BR** (the I/O counterparts of MAR/MBR); the **Execution Unit** generates the control signals required by the instruction. (Points: 32 + 32 + 36, duration 25 min.)

## Quiz 2 – 14 November 2007

**Question 1.** A 64-line direct mapped cache is used with a block size of 8 bytes and a total main memory of 2¹⁶ bytes.

- a) Address fields: block 2^w = 8 → w = 3; number of lines 2^r = 64 → r = 6; since the address is 16 bits, tag = 16 − 3 − 6 = **7 bits**.
- b) Which cache line does address `2C96` in main memory map to? 2C96 = 0010110 **010010** 110; the middle 6 bits are the line number: 010010 = **12H** (line 18).
- c) Which bytes are brought along when the byte at address `A043` is loaded into the cache? The block is 8 bytes; the first address with w = 0 is A040; that is, the 8 bytes between **A040–A047**.

**Question 2.** What is the memory hierarchy and what is it used for? As access speed increases, the cost per bit increases; as capacity increases, the cost per bit decreases and access becomes slower. The user wants large capacity, low cost, and performance all at once. The solution is a hierarchy: going from top to bottom, memory is accessed less frequently, and access speed and cost decrease while capacity increases.

## Quiz 1 – 4 July 2008

Questions 1 and 2 (Von Neumann and the generations) and Question 4 (CPU registers) are the same as those in the 2003 and 2007 exams. Question 3: the basic structure of a computer (CPU, memory, I/O interface) is drawn; a **microprocessor** is defined as the form of a Central Processing Unit (CPU) manufactured on a single integrated circuit.

## Quiz 2 – 14 July 2008

64 KByte main memory, 2 KByte cache, 16 words per block (1 byte = 1 word):

- a) At least **16 bits** of address are required (64K = 2¹⁶).
- b) Direct mapping: cache has 2048/16 = **128 lines** → r = 7 bits; within-block w = 4 bits; tag = 16 − (4 + 7) = **5 bits**. On a read, the cache line is first selected with the r-bit line field, and the first 5 bits of the address are compared with the line's tag; if they are equal (hit), the desired word is read with the last 4 bits, otherwise the block is brought from memory into the cache.
- c) The cache has 128 lines, and main memory has 65536/16 = **4096 blocks**. Since i = j mod m, Block-132 maps to 132 mod 128 = **cache line 4**.
- d) 2-way set associative: 128/2 = 64 sets → 6 bits; word 4 bits; tag = 16 − (6 + 4) = **6 bits** (6 + 6 + 4). Block-132 maps to 132 mod 64 = **set 4**.

## Quiz 3 – 30 July 2008

1. Each chip provides 512 × 512 = 256 Kbit (1 bit of data is taken from the chip); with 8 chips, **256 KByte** is obtained.
2. The land-pit transitions corresponding to the bit pattern `001001001010000000010000010000101000001001000` on a CD track segment are drawn (on a CD, 1 bits correspond to land-pit transitions and 0s to intervals without a transition; the drawing is in the PDF).
3. **RAM** is read-write memory (dynamic DRAM and static SRAM; DRAM needs refreshing because charge leaks, and DRAM is slower and cheaper; SRAM is used in cache and DRAM in main memory; both are volatile). **ROM** is programmed once at manufacture and cannot be erased. **PROM** is programmed once by the user with special hardware. **EPROM** is erased with ultraviolet light and can be reprogrammed. **EEPROM** is erased with an electrical signal.
4. DRAM performs reads/writes without clock synchronization, and the CPU has to wait for the access time. **SDRAM** (Synchronous DRAM) is synchronized with the clock; the number of cycles after which the operation will finish is known, and the CPU can do other work during this time.
5. The map of the given memory connection diagram (3-8 decoder, 2K×8 EPROM, two 1K×4 RAMs): **EPROM: C000–C7FF**, **RAM: E400–E7FF** (the address tables are in the PDF).

## Quiz 2 – 10 November 2008

Byte addressing in a direct mapped cache, address fields Tag = 8, Line = 13, Word = 1 bits.

- a) Address 8 + 13 + 1 = 22 bits → main memory 2²² = **4 MByte**.
- b) The cache has 2¹³ = 8K lines, with 2 bytes per line → **16 KByte**.
- c) Main memory has 4M / 2 = **2M blocks**; d) block size is 2¹ = **2 bytes**.
- Question 2: the address `25DB2D` is written as 22 bits: 10 0101 1101 1011 0010 1101; the Line field is 0110110010110 = **0D96H**, w = 1: it is placed in the second word of cache line 0D96H.
- Question 3: the smallest address that can be placed in the same line is **001B2C**, with Tag = 0.
- Question 4: with fully associative mapping, the address structure would be Tag = 21 bits, Word = 1 bit.

## Quiz 2 – 22 July 2009

**Question 1.** 1 byte of data is transmitted using a SEC (Single Error Correcting) Hamming code; with what bit pattern is 211₁₀ transmitted? For an 8-bit word, the condition 2^k ≥ 8 + k + 1 requires k = 4 check bits; these are placed at positions 1, 2, 4, 8. 211₁₀ = 11010011. Positions 12…1: D8 D7 D6 D5 C8 D4 D3 D2 C4 D1 C2 C1. With even parity: C1 = D1⊕D2⊕D4⊕D5⊕D7 = 0, C2 = D1⊕D3⊕D4⊕D6⊕D7 = 0, C4 = D2⊕D3⊕D4⊕D8 = 0, C8 = D5⊕D6⊕D7⊕D8 = 1. The transmitted pattern: **110110010100**.

**Question 2.** Design a total memory of 8 MByte using 1024 × 1024 × 4 memory chips; show the MAR and MBR connections. A chip selects 10 row bits + 10 column bits and provides 4 bits of data; for one byte, 2 chips are selected with the same address → each chip pair is 1 MByte; for 8 MByte, **8 pairs** are required, and 3 bits are needed to select among the pairs: total address 10 + 10 + 3 = **23 bits** (2²³ = 8 MByte). (The drawing is in the PDF.)

## Hamming code exercises

1. Hexadecimal numbers with a Hamming code are transmitted over a channel in which a single-bit error may occur; find the transmitted number from the received word 1000101. Positions 1–7. Positions 4-5-6-7 check: even → C1 = 0; positions 2-3-6-7 check: odd → C2 = 1; positions 1-3-5-7 check: odd → C3 = 1. Error position C1C2C3 = 011 = **3**. The corrected word is 1010101; the message bits (positions 3, 5, 6, 7) = 1101 = **D**.
2. How many check bits are needed for a 6-bit data word? From the condition 2^k ≥ m + k + 1, 2⁴ = 16 ≥ 6 + 4 + 1 → **4 check bits**; they are placed at positions 1, 2, 4, and 8.
