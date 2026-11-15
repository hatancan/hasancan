---
baslik: EEM335 Computer Organization: Computer System Architecture (Assoc. Prof. Dr. Yalçın Çebi Lecture Slides)
ozet: Computer system architecture lecture slides: von Neumann architecture, 7-layer architecture model, bus types, development of the transistor, PMOS/NMOS/CMOS, logic gates, integrated circuits, processor registers (MDR, MBR, MAR).
---

This post is a summary of the 53-slide presentation **"Computer System Architecture"** found in the EEM335 Computer Organization folder. The name **Assoc. Prof. Dr. Yalçın Çebi** appears on every slide of the presentation; the year of preparation and institution information are not given in the document.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request of the rights holder.*

The full presentation (slide PDF) can be downloaded at the end of the post.

## Computer architecture and von Neumann

Computer architecture is the design and arrangement of all the parts of a computer system. Nearly all computers use similar hardware components, and modern computers are fundamentally based on the **von Neumann architecture**. John von Neumann envisioned and formalized computer organization in the 1950s. The architecture defines three main components:

- **Input/output units:** allow the user to enter commands and see results.
- **Memory:** stores the information to be processed, programs, and statements.
- **Processor (Central Processing Unit):** processes data through pre-programmed steps.

The three units are connected by a **bus**, and all communication takes place via electronic signals. Computers using this architecture are called **stored-program computers**: more than one program and data set can be loaded into memory at the same time, and the processor can switch between them.

## Seven-layer architecture

| Layer | Name | Group |
|---|---|---|
| 7 | Application layer | Software |
| 6 | High-level software layer | Software |
| 5 | Operating system layer | Software |
| 4 | Machine layer | Hardware |
| 3 | Microprogram layer | Hardware |
| 2 | Digital logic layer | Hardware |
| 1 | Physical device layer | Hardware |

- **Physical device:** transistors, capacitors, and resistors; even the most complex computer is made up of combinations of these.
- **Digital logic:** **gates** that store and process data using binary representation; many gates combine on a single chip to form the processor.
- **Microprogram:** interprets statements in machine language; the simple program statements in ROM are called **microcode**, and the resulting program is called a **microprogram**. Manufacturers can execute the same machine layer in different ways to offer processors at different speeds and prices; software can be ported between computers. This layer is absent in first-generation and some small computers.
- **Machine layer:** the lowest layer in which programs can be written; statements are executed directly by the hardware.
- **Operating system:** hides the complexity of the hardware from software and protects the hardware from software errors.
- **High-level software:** the layer of statements that must be translated into machine language.
- **Application:** the topmost layer that the user sees.

## Bus and computer types

A bus is a set of parallel conductors to which various components can be connected; it carries data, address, and control signals as well as power. The **internal bus** is inside the processor; the **external bus** connects separate hardware elements. There are three types of computers by architecture: **single-chip** (for special tasks such as watches and cameras), **single-board** (personal computers and control systems; on a PCB), and **multi-board, bus-based** (minicomputers and mainframes; each board has a separate task). Inserting and removing boards while the system is running is called **hot-swapping**.

In the most basic bus architecture, all components are on a single general-purpose bus (simple, but I/O devices slow down processor-memory transfers); in a **two-bus** architecture, I/O is on a separate bus.

## Development of the transistor

- Pascal's Pascaline (1642) and Babbage's Analytical Engine (1833) are entirely mechanical; modern computers are electrical. The basic device that controls electric current is the **switch**.
- In the 1930s electromagnetic relays, and in the 1950s vacuum tubes, served as switches; tubes got very hot and failed quickly.
- **In 1948, John Bardeen, Walter Brattain, and William Shockley at AT&T Bell Laboratories** produced the first transistor (1956 Nobel Prize in Physics). The first commercial product with a transistor (a hearing aid) came in 1953, the first transistor radio in 1954, and the first fully transistorized computer a year later.
- The first transistor was made of gold and germanium; silicon is used today. Germanium and silicon are **semiconductors**.
- **PMOS:** conductive in its initial state, becomes insulating when current is applied to the control wire. **NMOS:** the opposite; becomes conductive when current is applied. Combining the two gives **CMOS**.
- **NOT**, **AND** (X·Y), and **OR** (X+Y) gates are built with PMOS and NMOS.

## Integrated circuits

Producing circuits by connecting transistors one by one was not suitable for mass production. **In 1958, Jack Kilby of Texas Instruments and Robert Noyce of Fairchild Semiconductor** independently developed the technique of putting all the transistors and connections on a single silicon wafer (microchip, IC). They obtained a patent in 1959 and later exchanged cross-licensing rights. Noyce later founded Intel; Kilby received the Nobel Prize in Physics in 2000.

## Processor and registers

The processor works with a **Control Unit (CU)** and an **Arithmetic Logic Unit (ALU)**; its tasks are memory control, sequencing operations, issuing instructions, and inputting, processing, and outputting data. **Registers** are special-purpose temporary memory locations inside the processor or other components:

- **Memory Data Register (MDR):** located inside the processor; all data and statements going to or coming from the processor pass through it.
- **Memory Buffer Register (MBR):** located in main memory; everything going to or coming from memory passes through it.
- **Memory Address Register (MAR):** holds the address that specifies the location of data in main memory; the address goes to memory over the address bus, and the read/write information is conveyed over the control bus.
