---
baslik: EEM332 Microprocessors: Assembly and PIC Educational Website Project
ozet: Technical sections of an educational website project prepared for assembly language, processor architecture, and the PIC16F84.
---

This post brings together the relevant notes and applications from the Başkent University **EEM332 Microprocessors** course archive (2004–2004). The technical sections of an educational website project prepared for assembly language, processor architecture, and the PIC16F84. Source: A student website project with the author anonymized; textbooks and university websites are cited in the references. Work prepared by a friend and course documents have been presented together; student names, numbers, and group information have been removed. PDF archive copies of the documents and, where available, source code can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it has been shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*

## Computer-Related Thesis

### ASSEMBLY LANGUAGE

### WHAT IS ASSEMBLY LANGUAGE?

Many people regard assembly and machine language as equivalent. Machine language is fundamentally quite similar to assembly, but they are not the same thing. Machine language consists entirely of instruction sequences written in the hexadecimal (base-16) system. Assembly, on the other hand, consists of words and abbreviations of words that correspond one-to-one to these instruction sequences.

Example: An instruction sequence written in machine language as B8 01 00 corresponds to the instruction MOV AX,0001 in assembly language.

Now let me say a few words about the terms assembly and assembler. Above, I tried to explain what assembly is by describing the difference between it and machine language. In other words, assembly, like BASIC, Pascal or C, is made up of words. In the end, software is needed to convert these instructions into machine language; we call such software a compiler. The programs that convert prepared assembly instructions into machine language are called assemblers. In other words, the assembly compiler is called an assembler.

### DISADVANTAGES OF ASSEMBLY LANGUAGE

To write a program, one must have detailed knowledge of the hardware of the computer being worked on (such as the registers in the microprocessor and their number, the instruction set it uses, and the addressing modes). It is also inflexible: every microprocessor produced by a manufacturer has its own programming language. Therefore, a program written for one microprocessor may not run on another. Assembly is harder to write than other high-level languages; in other languages the instructions consist of understandable words used in everyday speech, so they are easy to write and interpret.

### ADVANTAGES OF ASSEMBLY LANGUAGE

It gives the programmer fast program execution, operation in a small memory area, and capabilities that high-level languages do not have. It makes it possible to write high-level programs.

- It gives good control when working on special hardware components of the computer.

- Small and compact, working programs can be written.

- It runs faster than programs written in other high-level languages.

### MACHINE LANGUAGE

The language written to perform a specific task in microprocessor-based systems, consisting of logic 0s and 1s, is called machine language. The side-by-side arrangement of these numbers that make up machine language forms a sequence that is incomprehensible to the programmer. A program in machine language written for one computer can be valid for other machines on one condition; otherwise it only runs on its own computer. If the processor used by the machine uses the same instruction set, one can run on the other.

Machine Language Program

### CS:0100           101110000000001000000111000001             MOV AX,0005

### CS:0103           010000011110000011000001100000             ADD AX,0010

### CS:0106           1110001001001111100000001111100            SUB AX,0005

### CS:0109           0111100011001001111101010100101            NOT AX

### CS:010B           1111000000000000001111111000011            MOV BX,AX

### CS:010D           111110010101010111111110000                INT 21H

Figure 1. A program in machine language coded in hexadecimal

The binary instructions here show the actual language that the machine understands and runs. Every processor has its own language. Entering the 0s and 1s that make up binary sequences into the computer's memory leads to errors. For the sake of mutual understanding between machine and human, languages are divided into various categories:

### Languages are divided into various categories for the sake of mutual understanding between machine and human

- High-level languages

- Mid-level languages

- Low-level languages

A program in machine language written for one computer can be valid for other machines on one condition; otherwise it only runs on its own computer. If the processor used by the machine uses the same instruction set, it can run on another.

### HIGH-LEVEL LANGUAGES

English [personal information removed] can be understood by everyone. It is very close to human language and is easy to write. Examples of these languages: Basic, Pascal, C.

### TRANSLATION PROCESSES

The process of translating a source program into an object program using a kind of intermediary program is called translation. Written programs are subjected to different types of translation when being converted to machine language. The programs that do this are interpreters and compilers.

COMPILERS

A compiler is an intermediary program that translates programs written in high-level languages into machine language, assembly language, or some intermediate languages. If the compiler used first produces a program in assembly language, then the assembly language must subsequently be used to produce a program in machine language.

The compiler consists of programs or subroutines located in ROM or on magnetic media. The compiler scans the program and, as its first task, identifies keywords and operators. All details and blanks unrelated to the subject are discarded. The remaining part is turned into a concise program divided into expressions by special markers.

Compiler High-level languages                           Compiler Written                                                 Assembler               Machine Language Programs                                                                       X.EXE Compiler            Interpreter              X.COM

### X.BAS

X.PAS                                                Interpreter

### X.COB

Figure 2. Compiler and interpreter can work separately or together

- Lexical analysis to identify keywords or operators

- Syntactic analysis to identify the type and corrections of each expression

- Flow analysis that finds the relationships between expressions to aid error checking, register assignment and optimization

- Optimization to reduce the total number of instructions

- Generation of code for assembly or machine language

- Generation of the program listing

### ROM

Compiler                                            Object Program

### X.OBJ

Lexical Analysis                                                                        Machine Code RAM                                                 Syntax Corrected       Analysis         Assembly Language       Code Generation     Program X.BAS                                                         Program Program

Source Program

Direct Code Generation

Symbolic and              Interpreter Relative Figure 3. Address Structure of a Simple Compiler

The format of each line in the program consists of a line number, an instruction and an operand. These lines are checked, and if there is any error, the error code is displayed on the screen. The variables in the program are later listed as variables in assembly language. Each variable is given its symbolic address and length. Each instruction is assigned an address in the RAM area reserved for data, and the symbolic address, symbol type and absolute address of the compiled list are stored in RAM. This list is generally called a Dictionary.

INTERPRETERS: The lines in a BASIC program are interpreted one line at a time. That is, the lines are interpreted one by one to arrive at the object program. One does not move on to the next line before a line is completed successfully. The interpreter compiles the library of variables and their addresses and squeezes the absolute address into the places where the translated BASIC line requires it.

### ROM

Corrected Program

### RAM                                       RAM

Translated BASIC line                      Machine Code Subroutine                    Executable Program

### RAM

Absolute Address Next Line Figure 4. Structure of a Simple Interpreter

In debugging, an interpreter is less successful than a compiler. The interpreter cannot translate every expression into machine language codes that will take its place in memory, and therefore it does not produce an object program. While a BASIC line is being translated, the generated machine code is erased as the line's expressions are executed. In an interpreter, one does not move on to another line without correcting an error in a line.

Problem

Develop Algorithm

Write Program

Enter into Computer            Make Correction

Yes Is There an Error?

No Finish

A) Interpreted Program Flow

Problem

Develop Algorithm

Write Program

Enter into Computer             Make Correction

Compile

Yes Is There an Error?

No                     Is It a Syntax Error? Load Object Code                                 No

Start Execution

Yes Is There an Error?

No Finish

B) Compiled Program Flow Figure 5. Example Program Showing the Difference in Operation Between Compiler and Interpreter

### TYPES OF ASSEMBLY LANGUAGE

The intermediary program that translates a source program written in assembly language into the machine language object program is the Assembler. It can reside in ROM, or it can be run from disk or diskette. Those in ROM are resident assemblers.

- 1-) CROSS-ASSEMBLY: Used to run an assembler produced on any computer on another computer.

2-) SELF-ASSEMBLY: Requires memory and peripheral devices. It runs quite slowly.

3-) META-ASSEMBLY: Can handle and use many instruction sets in different ways.

4-) SINGLE-PASS ASSEMBLY: The program is scanned once and converted into the object program.

5-) TWO-PASS ASSEMBLY: The source program is processed twice. In the first pass it collects and defines all symbols. In the second it substitutes the references with their actual definitions. Without backup, it can be quite slow. Most microprocessor-based assemblers need a Two-Pass Assembler.

- If the mini-assembler program is not resident in ROM or a similar place, it is loaded into the computer's RAM.

- A command is given to the computer to run the mini-assembler program.

- The computer converts the source code into machine code and places it in RAM.

- Once the object code has been placed in memory, it is stored on disk or tape, which are magnetic media, for later use.

### TRANSLATORS

A program is written following assembly writing rules and saved as X.ASM, and is converted into an object program by means of the Assembler. The object program forms the program header added to the beginning of the .obj program module. The 256-byte PSP in a COM-type program and the 512-byte program header in an EXE-type program provide information about the completed addresses.

optional                                                X:MAP X.LST             optional

### X.XRF

### TASM                                  LINK

Editor        X.ASM                 MASM                                                       X.COM

### X.EXE

### X.OBR

### X.LIB

Figure 6. Assemble, Link and Execution Steps

The MASM or TASM assembler programs are used to make the program executable. The commas after X.ASM on the command line are for the creation of the LST and XRF files. The program with the XRF (CRF) extension is used in large programs to see which instruction corresponds to which data, and LST is the file in which the numbers of expressions in the program are produced by CRF.

### PROGRAM LOADERS

The loader sets up the processor so that the executable program can be run. The loader also provides the hardware service for resetting the program. If the microprocessor hangs or locks up, the programmer can restart the system using the reset button. The steps for loading an executable program of EXE type into memory for execution are:

### The steps for loading an executable program of EXE type into memory for execution

- Access to the EXE program on disk

- Establishing the boundaries of the 512-byte file header (the 256-byte PSP for COM-type programs) in memory

- Placing the program in the area outside the space reserved for the file header

- Loading the file header address into the DS and ES data segment registers

- Loading the code segment address into the CS register and setting the IP register to the offset address of the first instruction in the code segment (generally 0000H)

- Loading the stack segment into the SS register and setting up the SP register according to the area specified in the program

- Transferring control to the first instruction in the code segment so that the program can be executed

By forming the CS:IP and SS:SP pairs, loaders make the program run starting from the first instruction. Loading the file header address into both DS and ES is not needed except for string operations. In a normal program, loading DS as the data segment is sufficient.

### DEBUGGERS

A debugger is a debugging program that allows examination of register and memory states at a desired point while the program is running. If it finds an error in the program, some debugger programs allow the user to correct the errors and continue running the program from where it stopped. This feature allows examination of the contents of registers and modification of their contents. The operations are carried out by the debugger either through execution of the instructions in the microprocessor, or by execution under the control of a Simulator or an Emulator.

### FLAGS

### FLAGS                      BIT SET (1)                 BIT RESET (0)

Overflow                         OV                            NV

Direction                        DN                            UP

Interrupt                        EI                            DI

### PL

Sign                           NG                            NZ

### ZR                            NA

Zero                                                         PO

### AC

Auxiliary Carry                                                    NC

### PE

Parity

### CY

Trap

Carry

Overflow = Comes into play when an error occurs while operating on signed numbers.

Direction = In character and string operations, makes the index register move forward or backward.

Interrupt = Handles interrupt requests coming from external devices connected to the system.

Sign = This flag comes into play in operations on signed numbers. If the result is negative (-) the flag is 1; if positive (+) the flag is 0.

Zero = If the result of the operation is 0 the flag is 1, otherwise 0.

Auxiliary Carry = Does the same job as the carry flag, but if there is a carry out of bit 3 the flag is 1, otherwise 0.

Parity = If the number of logic ones in the register after the operation is even, the flag is 1, otherwise 0.

Trap = In debugging, makes the data be processed step by step.

Carry = If a carry occurs at the end of an addition, or a borrow in a subtraction,

```asm
the flag is 1, otherwise 0.
```

### DATA TYPES

One of the fundamental characteristics of a programming language is the data types to be used in the language. Here the simplest data types used in assembly language will be discussed.

The length of the information to be used in the assembly programming language depends on the computer's microprocessor. For the 8088 microprocessor, data of at most 16 bits in length can be represented. Since the 80286, 80386 and 80486 microprocessors are more advanced, the data length they use can be greater.

### BYTE

A byte is a unit of information made up of 8 bits. In assembly, a byte can represent both numeric and alphanumeric information.

In BYTE as well as in other data types, numbers fall into two main groups: signed and unsigned. Unsigned numbers represent the case where the entire data field is evaluated as a whole. Whether numbers are signed or unsigned is a relative matter from the machine's point of view.

1 0 0 0 0 0 0 1 Unsigned, represents the number 129.

1 0 0 0 0 0 0 1 Signed, represents the number -127.

In negative numbers the most significant bit is 1.

A byte consists of two main parts. Each part is called a NIBBLE. Each NIBBLE represents one hexadecimal digit.

10000001

----------- -------------

### 2nd NIBBLE 1st NIBBLE

### WORD

A structure formed by 2 bytes. The 8088 and other microprocessors support this 16-bit-long structure. You can process the word structure as a whole, or you can process it as the high byte (HB) or the low byte (LB).

### DOUBLEWORD

A structure two words long, i.e. 32 bits long. It is used both in addressing and in storing large numbers.

### QUADWORD

A structure 64 bits long. It is formed by combining 4 words.

On a machine with an 8088 microprocessor, the BYTE and WORD concepts directly supported by the microprocessor can be used. On 80286, 80386 and higher microprocessors, in addition to the BYTE and WORD concepts, the DOUBLEWORD and QUADWORD concepts can also be used. On 8088 microprocessors, constants and variables longer than a WORD can also be used. However, this use comes with software support rather than direct microprocessor support.

### REGISTERS

8-bit registers: Ah, Al, Bh, Bl, Ch, Cl, Dh, Dl

16-bit registers: Ax, Bx, Cx, Dx, Si, Di, Bp, Cs, Ds, Es, Ss, Sp and Flags

### We can group these registers as follows

Ax : Arithmetic-purpose register, formed by combining the Ah and Al registers. Bx : Base register, formed by combining the Bh and Bl registers. Cx : Counter register, formed by combining the Ch and Cl registers. Dx : Data register, formed by combining the Dh and Dl registers. Si : Source index register, points to the elements of a source array. Di : Destination index register, points to the elements of a destination array. Bp : Base pointer, generally used to point to the base address of an array.

Cs : Register that points to the code segment. Ds : Register that points to the data segment. Es : Register that points to the extra segment. Ss : Register that points to the stack segment. Sp : Stack pointer, points to the active point of the stack.

### BASIC

### MICROPROCESSORS

2.

### CHAPTER

### BASIC MICROPROCESSOR STRUCTURE

Computer systems based on a microprocessor, formed by the combination of a microprocessor, memory and I/O elements, are called microcomputers. Computer architecture refers to the logical structure applied to a computer system and the organization of the hardware elements that make up the system. The microprocessor works like the central processing unit of a microcomputer. The function of the processor is to fetch program instruction codes from memory, decode and execute them, generate the control signals used in input-output operations and provide synchronization, and monitor the results. The functional configuration of this microprocessor includes registers, and timing and control elements such as a clock generator, divider and counter to ensure sequencing in operations.

Microprocessors, called the heart or brain of the computer, are also known as the Central Processing Unit (CPU). The CPU generally performs the following operations:

### The CPU generally performs the following operations

- Provides timing and control signals to all elements and units in the system.

- Fetches instructions from memory.

- Decodes the instruction.

- According to the instruction's operand, transfers data to itself or to the I/O unit.

- Carries out arithmetic and logic operations.

- While the program is being executed, responds to interrupt requests coming from other hardware units.

If the architectural structure of a microprocessor is to be expressed in the simplest way, it consists of a group of registers, an Arithmetic and Logic Unit, and a timing and control unit that supervises what job the system does and when.

### UNITS THAT FORM THE BASIC BUILDING BLOCKS OF THE MICROPROCESSOR

### 1) REGISTERS

One of the elements that determine the architecture of the microprocessor. They have primary responsibility for the manipulation and temporary holding of data. 6502

Data bus Accumulator

X index register Control bus Y index register

Stack register Address bus

flags

Figure 1. Register group of a simple 8-bit processor.

### 2) ARITHMETIC AND LOGIC UNIT (ALU)

All operations that take place in the ALU are synonymous with control signals and are under the supervision of the timing and control unit.

### MEMORY

Accumulator                Temporary register

### ALU

Flags Figure 2. Arithmetic-Logic Unit

### 3) TIMING AND CONTROL UNIT

It is responsible for the entire operation of the system and for operations being performed on time. It generates the control signals required for fetching the instruction code located in the program section of memory, decoding it, processing it by the ALU, and retrieving the result and putting it back into memory. All internal and external elements in the computer system are supervised by these control signals.

Fetch mechanism

Instruction decoder

CPU elements                                                                     IRQ NMI RDY S.O Timing and control unit

### RES R/W SYNC

Flags     Clock signal generator            Q1 Q2 Figure 3. Input-Output Signals of the Timing and Control Unit

### 16-BIT ADVANCED PROCESSORS

The architectural structure has been made suitable for a multitasking environment. 16-bit x86-based processors are grouped into two main sections: the Bus Interface Unit (BIU) and the Execution Unit (EU). The BIU section includes the IP and instruction queues together with the segment registers, and the data fetch units.

General-Purpose Registers              Bus Interface Unit Execution Unit    AL          AH                                   (BIU)

### (EU)         BH          BL

### CH          CL                                    CS

### DH          DL                                    DS

### SI                                         SS

### DI                                         ES

### BP                                         IP

### SP

Data System Bus Data control   Bus and address generation Control Queue

### ALU

Flags

Control Unit

Figure 4. Simple 16-Bit Microprocessor Architecture

### BUS INTERFACE UNIT

The instruction codes and operand information brought from memory or I/O units into the instruction queue are ready to be processed by the execution unit.

### EXECUTION UNIT (EU)

It works together with the BIU. If any data is needed while instructions are being processed and the data is in one of the general-purpose registers, it fetches it; if the needed data is in an external medium (in memory or peripheral devices), it carries out operations such as requesting the data from the BIU. The EU section includes the general-purpose registers, the control unit, and the unit where arithmetic and logic instructions are processed.

Fetch             Fetch             Fetch             Fetch              Fetch Cycle 1

### T

i i Decoder          Decoder          Decoder           Decoder m    Cycle 2

### C

e y Fetch operand      Fetch operand      Fetch operand      Fetch operand Cycle 3 c l                       Execute           Execute            Execute            Execute Cycle 4 e s 5. Cycle    Store result        Store result        Store result        Store result        Store result

Figure 5. Parallel Operation in 16-Bit Processors

### ARITHMETIC AND LOGIC UNIT

After the instruction code is decoded, the ALU (Arithmetic and Logic Unit) performs the mathematical or logic operations.

### REGISTERS

### 1) SEGMENT REGISTERS

The starting address in memory for managing information is held by the segment registers.

32-Bit Names

16-Bit Names

8-Bit Names

EAX                  AH AX AL              Accumulator

EBX                 BH BX BL               Base Address Indexer

ECX                 CH CX CL               Counter

EDX                 DH DX DL               Data

ESI                        SI              Source Indexer

EDI                        DI              Destination Indexer

ESP                        SP              Stack Pointer EBP                        BP              Stack Base Indexer IP              Instruction Pointer / PC Flags         Flags

CS              Code Segment

DS              Data Segment

ES               Extra Segment

SS               Stack Segment

FS              Extra Data Segments (on 386+ processors)

### GS

Figure 7. Register model of 80*86 processors

C) SEGMENT ADDRESS: The expression next to the block name can be defined as the offset address of the class numbers (05) in that block.

```asm
CODE SEGMENT REGISTER: Called CS. The code segment is the section of memory where the instructions to be executed are located in sequence.
```

```asm
DATA SEGMENT REGISTER: Called DS. Indicates the segment part of the full address. The data in the segment is generally stored in the data segment, which is the first data segment.
```

```asm
EXTRA SEGMENT REGISTER: Called ES. This register cannot be used unless defined by the user. In string operations it is called the destination address. While source data is located in the data segment, results are transferred to the extra segment.
```

```asm
STACK SEGMENT REGISTER: Called SS. It is the place where data is temporarily placed, when some data is being processed, because of lack of space or insufficient registers.
```

### CS                            CODE SEGMENT

### DS                            DATA SEGMENT

### SS                            EXTRA SEGMENT

### ES                            STACK SEGMENT

### FS                            OTHER SEGMENTS

### GS

Figure 8. Segment registers and the areas they point to in memory

### GENERAL-PURPOSE REGISTERS

These are electronic elements used in manipulating data during execution of program instructions in the microprocessor, whose structurally smallest section resembles an 8-bit memory cell. They are divided into 2 according to the work they do:

### GROUP 1: EAX,EBX,ECX,EDX,ESI,EDI,EBP

GROUP 2: ESP, EIP and the FLAGS register. Up to the 386 processor, these registers are treated as the 16-bit AX, BX, CX, DX. For processing smaller 8-bit data (bytes), they are defined with even smaller parts, such as AH, AL, BH, BL, CH, CL, DH, DL.

### EAX                                AH       AX       AL

### EBX                                BH       BX       BL

### ECX                                CH        CX      CL

### EDX                                DH        DX      DL

### ESI                                            SI

### EDI                                           DI

### ESP                                           SP

### EBP                                           BP

### EIP                                            IP

### EFLAGS

Figure 9. General-purpose register model in x86-based processors

AX REGISTER: The accumulator is identified by the code AX and is used in the first handling of data; it is called the primary register. It is used in multiplication and division with 8-, 16- and 32-bit data, in some I/O operations and in some string operations.

BX REGISTER: It is the base address register. It acts like an indexer in holding the offset of data groups in memory. It is used in calculations and, in 32-bit processors, in addressing data in memory.

CX REGISTER: It is the counter register. It performs highly valuable duties such as a repetition counter in string operations. The CL register part holds the shift count, particularly in multiple shift and rotate operations. In string operations, with the REPn instruction prefix, together with the LOOP instruction, the operation continues until the value in it becomes zero.

DX REGISTER: It is the data register. It assists the accumulator and acts like a buffer in all operations. In input-output (I/O) operations it holds the port number, while in multiplication and division of large-valued numbers (Word and Doubleword) it is used together with AX.

POINTER AND INDEX REGISTERS: These are registers that point to intermediate addresses in memory. The instruction pointer (IP) helps in finding the offset value for the CS register when determining the location of an instruction in the code segment. In determining the location of data in the stack area, together with the stack segment register, the SP or BP register (Stack Pointer) helps as the offset value.

The Source Index (SI) and Destination Index (DI) registers are used in address indexing operations.

FLAGS REGISTER: Depending on its type, it is an 8-bit, 16-bit or 32-bit memory cell that reflects in its register bits what the result is at the end of an operation. A register bit being logic 1 means the flag is set, and logic 0 means the flag is cleared.

### MEMORY ADDRESSING

LOGICAL MEMORY: All addresses are numbered in bytes. The address numbers of processors with 16 address lines start with 0000H and end with FFFFH. The address space is 1 MB.

The numbers of processors with 32 address lines start with 00000000H and end with FFFFFFFFH. Their addressing capacity is 4 GB.

### EAX

Register                                Memory map        Addresses

### AX

### FFFFFFFFF

### AH         AL

### 0                                              0000A039H

### 25   C3      5A       28

### 0000A038H

### 0000A037H

### 0000A036H

### 0000A035H

### 0000A034H

### 25       C3      5A     28

### 00000000H

### 8-BIT

Figure 11. Placement of 32-bit data in memory

Depending on the memory model definition, a microprocessor can access one or more bytes of data in memory at a time.

### PHYSICAL MEMORY DEFINITION

Since the physical definition of memories is a hardware approach, it depends on processor types and architecture. For the programmer, all memory types or groups are always logically 8-bit.

### MEMORY MAP

### D31-D24                                        D23-D16

### FFFFFFFF                                   FFFFFFFE

### FFFFFFFB                                   FFFFFFFA

### 8-BIT                                      8-BIT

### 0000000F                                   0000000E

### 0000000B                                   0000000A

00000007                                   00000006 00000003                                   00000002

### BANK3                                    BANK2

### D15-D8                                         D7-D8

### FFFFFFFD                                   FFFFFFFC

### FFFFFFF9                                   FFFFFFF8

### 8-BIT                                      8-BIT

### 0000000D                                       0000000C

00000009                                       00000008 00000005                                       00000004 00000001                                       00000000

### BANK1                                 BANK0

Figure 12. Physical memory structure in 32-bit processors

### SEGMENT BOUNDARIES

Segments begin at an address, called the paragraph boundary, whose address is evenly divisible by decimal 16 (decimal 10). Since data loss is to be minimized when data starts in memory from a certain origin point, segment address starts always begin with 0H.

### OFFSET ADDRESS

The address where the data is located is as far as its distance from the starting address pointed to by the segment register.

In a 64 KB memory space, addresses run from 0000H up to FFFFH. In a 4 GB memory space, the 64 KB segment definition is defined similarly even if the number of offset digits increases, that is, it extends from 00000000H up to 0000FFFFH. Segment addresses are assigned automatically by the processor.

Segment registers                              Memory

### CS                               CODE SEGM.

### 045B0

### XX                004CH

### SS

### ES

### STACK SEGM.

### EXTRA SEG.

Ds seg. address     045BOH

Offset address      004CH

Effective address       045ECH

Figure 13. Combination of the offset address and the segment address

### PIC16F84

3.

### CHAPTER

### WHAT IS A PIC?

### MICROCONTROLLER

The PIC is a microcontroller in which the CPU, memory, oscillator, watchdog and I/O are located on a single chip. This saves time and space in design, and also reduces timing and compatibility problems of peripherals. However, in some cases it may limit memory sizes and I/O capacity. The products in the PIC microcontroller family offer a range wide enough in I/O, memory and special functions to meet the needs of most development engineers.

PIC series microprocessors were developed by the MICROCHIP company, and their purpose of manufacture is to meet multifunction logic applications by software with a fast and cheap microprocessor. The literal meaning of PIC is -PERIPHERAL INTERFACE CONTROLLER- an input-output processor. It was first developed in 1994, because a very fast and cheap solution was needed to reduce and control the load on the inputs and outputs of large 16-bit and 32-bit processors. The PIC16C54, the first member of a very wide product family, is the first fruit of this need. PIC processors are referred to as RISC-like processors. The PIC16C54 is an 8-bit CMOS processor with a 12-bit instruction memory width. It has 13 I/O pins in an 18-pin DIP package and can be used at oscillator speeds up to 20 MHz. It contains 33 instructions. It has 512 bytes of program EPROM and 25 bytes of RAM. I think this memory capacity has made many people laugh, but being a RISC processor makes it possible to carry out many jobs with this capacity. For example, the relay control circuit used in the ANTRAK R94 relay contains one PIC16C54. Thanks to this circuit, functions in the R94 such as Time Out Timer, DTMF-coded Control and shutdown, and end-of-speech timing take up 324 bytes in program memory and use 14 bytes of RAM. All PIC series processors can be run without any additional memory or input/output element, with only 2 capacitors, 1 resistor and a crystal. A single pin can sink 40 mA of current, and the chip has a total current sink capacity of 150 mA. The current the chip draws at a 4 MHz oscillator frequency is 2 mA while running and about 20 uA in stand-by. Considering that the price of the PIC 16C54 is around US$2.0, the advantage of this processor is easily understood.

The processor family to which the PIC 16C54 belongs is called the 12-bit core 16C5X. This group is called the base-line group. The other processors that are members of this family are the PIC16C57, PIC16C58, and the 8-pin PIC12C508 and PIC 12C509, which are known as the smallest processors in the world. Interrupt capability is not found in the first processor family, the 12-bit Core 16C5X family. The 14-bit Core 16CXX family, produced later and known as the mid-range class, is a group of processors more capable in many respects. The basic features of this family are interrupt capability and a 14-bit instruction memory. These features

have made the PIC a real processor and suited to use in complex operations. The PIC16CXX family has the widest product range. The most important features of the 16CXX family are that it can be programmed serially even in-circuit (this feature was quite complicated in the PIC16C5x, which was parallel-programmed), that it accepts interrupts, and that its product range includes processors that accept industry-standard inputs and outputs such as 33 I/O, A/D converter, USART, I2C and SPI. The most widely known member of the PIC 16CXX family among amateur electronics enthusiasts, the one on which the most projects have been produced in the world, the darling of the internet, is the PIC16C84, or by its new name PIC16F84.

The popularity of the PIC 16F84 stems less from its being a very good processor than from its program memory being EEPROM (electrically erasable and writable memory). Being programmable serially with four wires is its other important advantage. The biggest trouble for everyone who has ever dealt with a processor as an amateur has been erasing EPROM or EPROM-based processors with an ultraviolet light source after programming them, and programming them again. This has been a very troublesome method that requires equipment for an amateur. A special programmer that is hard to build at home is the other side of the coin. The PIC16F84 is probably the processor for which the most programmers are available on the internet for amateurs. I have so far come across more than 50 PC- and MAC-based programmers that you can build at home. Erasing an EPROM is not even an issue, since the programmer circuit that programs the EEPROM memory can erase the same memory within 1 second.

This feature gives you the advantage of developing programs by trying many times very quickly, which is an invaluable blessing for an amateur electronics enthusiast. While doing these trials you don't even need to remove the processor from your circuit. This type of programming is called ISP (In-System Programming). An amateur electronics enthusiast

### will need the following equipment to develop programs with the PIC16F84

PIC16F84 MS-DOS-based PC ASCII Editor (for example DOS's EDIT) MPASM Assembler Programmer/eraser Software for the programmer I will try to introduce all of these items to you in this article series. In my next article, I will go into the features of the PIC 16F84 in more detail and describe the design of a PC-based programmer/eraser using the RS-232 COM port that is quite complicated!!! (three resistors). For more information about PIC series processors, you can consult the address.

### WHY PIC?

The PIC is an 8-bit microcontroller based on the Harvard architecture. This means there are separate on-chip buses for memory and data. Thus the throughput is increased thanks to simultaneous access to data and program memory. In traditional microcontrollers there is a single on-chip bus carrying both data and program. Compared with the PIC, this slows the processing speed by at least a factor of two. All instructions fit into a 12- or 14-bit program memory word. The software does not need to jump into the DATA part of the program and execute the DATA as instructions. This happens in microcontrollers that use an 8-bit bus and are not based on the Harvard architecture. The PIC is an 8-bit microcontroller based on the Harvard architecture.

This means there are separate on-chip buses for memory and data. Thus the throughput is increased thanks to simultaneous access to data and program memory. In traditional microcontrollers there is a single on-chip bus carrying both data and program. Compared with the PIC, this slows the processing speed by at least a factor of two. All instructions fit into a 12- or 14-bit program memory word. The software does not need to jump into the DATA part of the program and execute the DATA as instructions. This happens in microcontrollers that use an 8-bit bus and are not based on the Harvard architecture.

The PIC is a fully static microprocessor. In other words, when you stop the clock, all register contents are preserved. In practice it is not possible for you to achieve this exactly. When you put the PIC into sleep mode, the clock stops and the PIC sets various flags to remind you what state it was in before the sleep. In sleep mode the PIC draws a standby current of only less than 1 mA.

### PICBASIC

If you are tired of writing pages and pages of code in PICmicro assembly, or are not interested in microcontrollers simply because you hate assembly, PICBasic will offer you significant opportunities. The program segments that you write over pages in PICmicro assembly, and that you have to follow in the debugging process as if counting hairs on a felt, you can write, correct, compile and load into the PIC micro in a total of 8-10 lines with PICBasic. You need to know neither the detailed register structure of the PIC micro nor what will happen in which register at the end of which operation. Whichever ports and features of the PIC micro you intend to use, set up your algorithm, and with any text editor (NOTEPAD, WORD, EDIT, etc.), a sample program with PICBasic instructions that closely resemble the BASIC instructions we know:

### PICBasic Standard

-Supported PIC micros: 12C67x, 16C55x, 12C6x, 14000, 16C62x, 16C71x, 16F8x, 16F87x, 16C9x series... -Compilation capacity: 2K... -Possibility of integration into the MPLAB environment... -Possibility of inserting assembly code...

### PICBasic Professional

-Supported PIC micros: 12C67x, 16C55x, 12C6x, 14000, 16C62x, 16C71x, 16F8x, 16F87x, 16C9x series... -Compilation capacity: Unlimited, in proportion to the program memory of the PIC micro... -Possibility of integration into the MPLAB environment... -Functions specially prepared for writing to and reading from external/internal serial EEPROMs, LCD displays, internal-external AD converters, etc., and for mathematical operations... -Possibility of inserting assembly code...

Both versions come with a user manual in English with plenty of examples...

PICBASIC PRO Application Example: External AD Converters...

Although a group of microcontrollers belonging to the PICmicro family offer an 8-10 bit A/D converter on the chip for our use, sometimes A/D converters with higher resolution are also needed.

Or, if we have a shortage of available ports, using external A/D converters may make more sense. This month's application is about displaying on an LCD the analog information read from 2 separate channels, developed for use with any PICmicro from the 40-pin 16C6x or 16C7x series. Although the PIC16F877 used in the prototype circuit has 8 10-bit A/D converter ports, the main reason for choosing this PICmicro is nothing other than the convenience it provides while developing the application software. As the A/D converter, the LTC1298, a serial A/D converter chip with two channels and 12-bit resolution, was used. You can find the application circuit in the BEGINNERS' PIC PROGRAMMING HANDBOOK. The application software for it, somewhat differently from the PICmicro applications limited to assembly published in earlier issues, was prepared with PicBASIC Pro, which we introduced in our last issue.

PicBASIC Pro program prepared to read the LTC1298 ADC

‘HD44780-compatible LCD connections

Define LCD_DREG PORTD Define LCD_DBIT 4 Define LCD_RSREG PORTE Define LCD_RSBIT 0 Define LCD_EREG PORTE Define LCD EBIT 1

```asm
include "modedefs.bas"
```

’Pin definitions CS var PORTC.5 ' Chip select CK var PORTC.3 ' Clock var DI var PORTA.2 ' Data in var DO var PORTC.1 ' Data out

‘Variable definitions

```asm
addr    var   byte ' Channel address / mode
```

result var word x      var word y      var word z     var word

High CS

'Chip select is not active, i.e. the LTC1298 is not in the circuit.

### ADCON1 = 7

' PORTA, PORTE digital port. On the PIC16F877 at reset, ' PORTA and PORTD are analog inputs. Since we will use the analog ' inputs as digital inputs in this application, this ' definition is necessary.

Low PORTE. 2 ' LCD R/W line low (W).

Pause 100 ' Wait for the LCD's startup routine.

```asm
Goto mainloop
```

' skip the subroutines. ' Subroutine for reading the A/D converter getad

### CS = 0

‘Chip select is active, i.e. the LTC1298 is in the circuit.

'[address / mode - start bit, 3-bit addr, 0 bit] 'send.

ShiftOut DI, CK, MSBFIRST, [l\l, addr\3, 0\1] ’get the 12-bit result Shiftin DO, CK, MSBPRE, [result\l2]

### CS = 1

' Chip select is not active, i.e. the LTC1298 is not in the circuit.

```asm
Return
```

‘Subroutine for reading the x value (channel 0)

### getx 

```asm
addr = $05
```

‘single-ended, channel 0, MSBF high Gosub getad x = result

```asm
Return
```

‘Subroutine for reading the y value (channel 1)

### gety 

```asm
addr = $07
```

single-ended, channel 1, MSBF high Gosub getad y = result

```asm
Return
```

‘Subroutine for reading the z value (difference of channels 0 and 1)

```asm
addr = $01
```

Differential (ch0 = + , ch1 = -), MSBF high

Gosub getad z = result

```asm
Return
```

### mainloop

Gosub getx ‘get the x value Gosub gety ‘get the y value Gosub getz ‘get the z value

‘Send the values to the LCD Lcdout $fe, 1, “x=”,”#x, “y=”,#y,”z=”,#z Pause 100 ‘10 times per second

```asm
Goto mainloop ‘and do it continuously
```

```asm
End
```

If we had written the above program in assembly, it would probably have taken up more than 10 times as much space...

### HARDWARE

To design any system, a complete understanding of the hardware and software is essential. Since the hardware is the interface that provides communication with the outside world,

### it should be examined before the software. This chapter will focus on the following

### Structural Analysis of the Microcontroller

In outline, a microprocessor consists of the basic factors that make it up. These are, in short, MPU, RAM, ROM, IO. Let us briefly touch on these structures;

MPU: The unit also referred to as the Central Processing Unit carries out the main structural operations of our microprocessor: logic operations, arithmetic operations and execution operations; in short, it is the part that processes the data it receives from other units and transfers it on to another unit. It works at a certain clock frequency, i.e. it carries out a certain number of operations per second. Within itself it also has ROM, RAM and IO.

ROM: Called read-only memory, ROM is the piece of memory that is filled once during manufacturing.

RAM: This is the part known as the main memory; it is actively used by the central processing unit, and its smallness or largeness affects the system capacity. It is erased when power is cut.

IO: It is the microcontroller's connection to the outside. It is the protected part that transfers the information received from outside to the MPU, and the data it receives from the MPU to an external port. They are the slowest devices in the system.

Internal structure of the PIC SOFTWARE DESIGN

After understanding the hardware and how the PIC will be connected to the real world, one needs to learn the subject of software in order for the PIC to start doing something.

If you have done previous work related to software, you can skip some of the following information.

· understanding logic functions

· hexadecimal notation

· writing source code

· use of assembler directives

· macros that save time in writing code

· program development

· instruction set

· internal registers

· subroutines,

· lookup tables

· I/O port setup

· Reset vectors

### · RTCC

### · WDT

· interrupts

· stack

· A/D conversion

· E2-based PICs

· which PIC to choose?

· minimum hardware required

· reset circuits, timers

· watchdog

· oscillators

· inputs and outputs

· I/O expansion

· connection to the mains

· analog signal processing

· numbering in PICs

### PIC16F84 ARCHITECTURAL OVERVIEW

The high performance of the PIC16CXX family can be attributed to a number of architectural features commonly found in RISC microprocessors. To begin with, the PIC16CXX uses a Harvard architecture. This architecture has program and data accessed from separate memories. Therefore the device has a program memory bus and a data memory bus. This improves bandwidth over the traditional von Neumann architecture, in which program and data are fetched from the same memory (accesses over the same bus).

Separating program and data memory further allows instructions to be sized differently from the 8-bit-wide data word. PIC16CXX opcodes are 14 bits wide, making single-word instructions possible. The full 14-bit-wide program memory bus fetches a 14-bit instruction in a single cycle. A two-stage pipeline overlaps fetch and execution of instructions (Example 3 – 1). As a result, all instructions except program branches are executed in a single cycle (400 ns @ 10 MHz). The PIC16C84 addresses 1 K x 14 of program memory. All program memory is internal. PIC16CXX devices address the register file or data memory directly or indirectly. All special function registers, including the program counter, are mapped into data memory.

An orthogonal (symmetric) instruction set is arranged so that any operation can be performed on any register using any addressing mode. This symmetrical structure and the lack of "special optimal cases"

make programming with the PIC16CXX simply efficient. In addition, the learning curve is significantly reduced.

The PIC16C84 has 36 x 8 SRAM and 64 x 8 EEPROM data memory. PIC16C XX devices contain an 8-bit ALU and a working register. The ALU is a general-purpose arithmetic unit. It performs arithmetic and Boolean functions between data in the working register and any register file.

The ALU is 8 bits wide and capable of addition, subtraction, shift and logic operations. Unless otherwise stated, arithmetic operations are two's complement in nature. In two-operand instructions, typically one operand is the working register (W register), and the other operand is a file register or an immediate constant. In single-operand instructions, the operand is either the W register or a file register. The W register is an 8-bit working register used for ALU operations. It is not an addressable register.

Depending on the instruction executed, the ALU may affect the values of the Carry (C), Digit Carry (DC) and Zero (Z) bits in the STATUS register. The C and DC bits operate as borrow and digit borrow bits, respectively, in subtraction. See the SUBLW and SUBWF instructions for examples. A simplified block diagram for the PIC16C84 is shown below.

### FIGURE 3-1: PIC16C84 BLOCK DIAGRAM

### FIGURE 3-1: PIC16C84 BLOCK DIAGRAM

3.1 Clocking Scheme / Instruction Cycle

The clock input (from OSC1) is internally divided by four to generate four non-overlapping quadrature clocks, called Q1, Q2, Q3 and Q4. Internally, the program counter (PC) is incremented every Q1, and the instruction is fetched from program memory and latched into the instruction register in Q4. It is decoded and executed during the following Q1 through Q4. The clocks and instruction execution flow are shown in Figure 3 – 2.

3.2 Instruction Flow / Pipelining

An "Instruction Cycle" consists of four Q cycles (Q1, Q2, Q3 and Q4). Instruction fetch and execution form one instruction cycle, while decode and execute form another instruction cycle. However, due to pipelining, each instruction effectively executes in a single cycle. If an instruction causes the program counter to change (e.g. GOTO), then two cycles are required to complete the instruction. A fetch cycle begins with the Program Counter (PC) incrementing in Q1. In the execution cycle, the fetched instruction is latched into the "Instruction Register" in the Q1 cycle. This instruction is then decoded and executed during the Q2, Q3 and Q4 cycles. Data memory is read during Q2 (operand read) and written during Q4 (destination write).

### 3.0 ARCHITECTURAL OVERVIEW

The high performance of the PIC16CXX family can be attributed to a number of architectural features commonly found in RISC microprocessors. To begin with, the PIC16CXX uses a Harvard architecture. This architecture has program and data accessed from separate memories. Therefore the device has a program memory bus and a data memory bus. This improves bandwidth over the traditional von Neumann architecture, in which program and data are fetched from the same memory (accesses over the same bus). Separating program and data memory further allows instructions to be sized differently from the 8-bit-wide data word. PIC16CXX opcodes are 14 bits wide, making single-word instructions possible. The full 14-bit-wide program memory bus fetches a 14-bit instruction in a single cycle. A two-stage pipeline overlaps fetch and execution of instructions. As a result, all instructions except program branches are executed in a single cycle (400 ns @ 10 MHz). The PIC16C84 addresses 1 K x 14 of program memory. All program memory is internal. PIC16CXX devices address the register file or data memory directly or indirectly. All special function registers, including the program counter, are mapped into data memory. An orthogonal (symmetric) instruction set is arranged so that any operation can be performed on any register using any addressing mode. This symmetrical structure and the lack of "special optimal cases" make programming with the PIC16CXX simply efficient. In addition, the learning curve is significantly reduced. The PIC16C84 has 36 x 8 SRAM and 64 x 8 EEPROM data memory. PIC16C XX devices contain an 8-bit ALU and a working register. The ALU is a general-purpose arithmetic unit. It performs arithmetic and Boolean functions between data in the working register and any register file. The ALU is 8 bits wide and capable of addition, subtraction, shift and logic operations. Unless otherwise stated, arithmetic operations are two's complement in nature. In two-operand instructions, typically one operand is the working register (W register), and the other operand is a file register or an immediate constant. In single-operand instructions, the operand is either the W register or a file register. The W register is an 8-bit working register used for ALU operations. It is not an addressable register. Depending on the instruction executed, the ALU may affect the values of the Carry (C), Digit Carry (DC) and Zero (Z) bits in the STATUS register. The C and DC bits operate as borrow and digit borrow bits, respectively, in subtraction. See the SUBLW and SUBWF instructions for examples.

Programmable Control Interface (PIC)

The PIC is a microchip that, unlike the microprocessors produced, is simplified but whose speed and effectiveness have not been reduced. It was produced by the MICROCHIP company for application forms. With its simple chip set, suitable ports and optional functions, the PIC is an unmatched microprocessor for target control. Although structurally reminiscent of RISC processors, thanks to its improved instruction structure it can be programmed much more quickly and easily than its peers. They are 8-16-bit processors. They can go up to 20 MHz. In some types, the ports on them can serve as ADC and DAC through a single word. Compared with their competitors, their speeds and operating environments are more flexible and stable. They can operate between 2.5 V and 6 V, and finally their attractive prices fully meet such needs. (Also, the latest technology always contains more advantages and innovations than the previous one.)

The model below is the PIC 16C series. Since the EEPROM is present inside the chip in the processors of this series, there is no need to connect an extra EPROM and set aside ports to operate it. Below you can see the block diagram of a basic PIC 16C series microchip;

As seen in the diagram, it has external and internal interrupts. In this circuit, to ensure real-time operation of the motor's encoder, pin 5 of port A has been adapted to UART signaling.

Replacing '#' with '$'

```asm
.MODEL SMALL
.STACK 64
.DATA
DIZI DB 'LDA #305A'
.CODE
```

```asm
ANA PROC FAR
MOV AX,@DATA
MOV ES,AX
CLD
MOV AL,'#'
MOV BH,'$'
MOV CX,09
LEA ES:DI,DIZI
REPNE SCASB
JNE CIK
MOV BYTE PTR[DI - L],BH
```

```asm
CIK: MOV AH,4CH
INT 21H
```

### ANA ENDP

```asm
END ANA
```

Displaying the ASCII Character Set on the Screen

Page 60 , 132 TITLE ALLASC (COM) Display ASCII Characters(00FF)

```asm
CODESG SEGMENT PARA 'Code'
```

### ASSUME CS:CODESG , DS:CODESG , SS:CODESG , ES:NOTHING

```asm
ORG 100H
```

### BEGIN JMP SHORT MAIN

```asm
CTR DB 00 , '$'
```

Main Procedure

```asm
MAIN PROC NEAR
CALL B10CLR (Clear Screen)
CALL C10SET (Set Cursor)
CALL C10DISP (Display Characters)
RET
```

### MAIN ENDP

Clear Screen

```asm
B10CLR PROC
MOV AX , 0600H
MOV BH , 07
MOV CX , 0000 (Upper Right Position)
```

```asm
MOV DX , 184FH (Lower Right Position)
INT 10H
RET
```

### B10CLR ENDP

Set Cursor to 0000

```asm
C10SET PROC
MOV AH , 02
MOV BH , 00
MOV DX , 0000
INT 10H
RET
```

### C10SET ENDP

Display ASCII Characters

```asm
D10DISP PROC
MOV CX , 256 (Gives the Initial Value for 256 Repetitions)
LEA CX , CTR (Gives the Initial Value to the Counter's Address)
D20:
MOV AH , 09 (Display ASCII Character)
INT 21H
INC CTR (Increment Counter)
LOOP D20 (Decrement CX, Continue if Not 0)
RET
```

### D10DISP ENDP

### CODESG ENDS

```asm
END BEGIN
```

Program That Adds Two Bytes

### PAGE 60,80

### TITLE MODUL1

### PUBLIC ALTPRO1

### EXTERN SAY1:WORD

### EXTERN SAY2:WORD

### EXTERN TOPSON:WORD

```asm
.MODEL SMALL
.CODE
ALTPRO1 PROC FAR
MOV AX,SAY1
ADD AX,SAY2
MOV TOPSON,AX
RET
```

### ALTPRO1 ENDP

```asm
END
```

Quickly Access the Files on Your Computer with Assembly

model tiny

```asm
NFILES EQU 200 ;Max # files in display
FILESPEC EQU 82h ;Address of filespec in command tail
PATH EQU 81h ;Count of chars in path part of filespec here
NORMAL_FILE EQU 11100001b ;Attribute for a normal file
TAGGED EQU 80h ;Bit to set in attrib to indicate file tagged
DTA_ATTRIB EQU DTA+21 ;Offsets of elements in DTA
DTA_TIME EQU DTA+22
DTA_DATE EQU DTA+24
DTA_SIZE EQU DTA+26
DTA_NAME EQU DTA+30
FILE_TIME EQU bp ;Addrs of elements in 'fileRecords' after name
FILE_DATE EQU bp+2
FILE_SIZE EQU bp+4
INVERSE_VIDEO EQU 70h ;Black on white
NORMAL_VIDEO EQU 17h ;White on blue
COPYVAL EQU 1 ;Keys for Copy/Move/Delete/Rename operations
DELETEVAL EQU 2
MOVEVAL EQU 3
RENAMEVAL EQU 4
codeseg
BOF:
org 100h
Start:
mov sp, OFFSET stackEnd ;Initialize stack
sub ax, ax
push ax
mov [programSeg], cs ;Save current value of CS -> program segment
mov ah, 0Fh ;Find display memory
int 10h
mov di, 0B000h ;If mode 7 (= MDA or Herc), video seg=B000h,
cmp al, 7
je @@L1
mov di, 0B800h ;Otherwise video seg=B800h,
@@L1:
mov es, di ;Unless running under DesqView
mov cx, 'DE'
mov dx, 'SQ'
mov ax, 2B01h
int 21h
cmp al, 0FFh
je @@L2
mov ah, 0FEh
int 10h
mov di, es
@@L2:
mov [displaySegment], di
```

```asm
mov es, [2Ch] ;Find COMSPEC
sub di, di
@@L3:
mov si, OFFSET comspec
mov cx, 8
repe cmpsb
jne @@L3
mov [comspecOff], di
mov [comspecSeg], es
mov es, [programSeg]
NewSpec:
mov si, FILESPEC ;Examine command line filespec
mov di, si
cmp [byte FILESPEC-2], 1 ;If none, use "*.*"
jbe @@L3
@@L1:
lodsb
cmp al, '*' ;Look for wildcard chars
je GetPathLength
cmp al, '?'
je GetPathLength
cmp al, 0Dh
jne @@L1
cmp [byte si-2], '\' ;If none, assume spec is a directory
jne @@L2
dec si ;If last char was not '\', add it
jmp @@L3
@@L2:
mov [byte si-1], '\'
@@L3:
mov ax, si ;Compute length of path minus filename
sub ax, di
mov [PATH], al
mov di, si
NewDir:
mov [keepSorted], 0 ;Directory is initially unsorted
mov si, OFFSET starDotStar ;Append '*.*',0
call CopyString
jmp SHORT Restart
NoRoomError:
mov dx, OFFSET noRoomMsg ;Not enough room to run S
Abort:
call BlankScreen
mov ah, 9
int 21h
mov ax, 4C00h ;Bye
int 21h
GetPathLength:
mov al, [byte FILESPEC-2] ;Null-terminate other filespecs
```

```asm
sub ah, ah
mov si, ax
add si, FILESPEC-1
mov [si], ah
mov cx, ax ;Count chars in path excluding file name:
```

std ;Search backward for last '\' or ':'

### @@L1

```asm
lodsb
cmp al, '\'
je @@L2
cmp al, ':'
loopne @@L1
@@L2:
cld
mov [PATH], cl
Restart:
call HideCursor
mov ax, OFFSET files ;Cursor -> first file
mov [cursor], ax
mov [top], ax
Restart0:
mov bx, (EOF-BOF)/16+1 ;Resize memory to amount needed
mov ah, 4Ah
int 21h
jc NoRoomError
mov ah, 19h ;Get default drive for path/spec display
int 21h
add al, 'A'
mov di, OFFSET pathNSpec ;Store letter, ':\'
stosb
mov ax, '\:'
stosw
mov si, di ;Get path and name of current directory
sub dl, dl
mov ah, 47h
int 21h
sub al, al ;Find end
mov cx, -1
repne scasb
dec di
mov ax, ' '+100h*' ' ;Add two spaces
stosw
mov si, FILESPEC ;Append filespec
call CopyString
;Get all file names matching filespec and set up tables
GetFileRecords:
mov dx, OFFSET DTA ;Set up DTA
mov ah, 1Ah
int 21h
```

```asm
mov dx, FILESPEC ;Get first file name
mov cl, 37h
mov ah, 4Eh
int 21h
jnc FileFound ;No files. Try a different filespec.
mov si, OFFSET NoFilesMsg
call Error
jmp NewFilespec
FileFound:
mov di, OFFSET fileRecords ;DI -> storage for file names
mov bx, OFFSET files ;BX -> array of files
sub bx, 2
StoreFileName:
add bx, 2 ;For all files that will fit,
cmp bx, (OFFSET files) + NFILES*2
jb @@L1
sub bx, 2
mov [last], bx
mov si, OFFSET tooManyMsg
jmp DoError
@@L1:
mov [bx], di ;Store pointer to status/filename in files[]
mov al, [DTA_ATTRIB] ;Store status byte
and al, 3Fh ;Top bit is used to indicate file is Marken
stosb
mov si, OFFSET DTA_NAME ;Copy file name form DTA to filename storage
call CopyString
```

inç di

```asm
mov si, OFFSET DTA_TIME ;Copy time, data and size
mov cx, 4
```

rap movsa

```asm
mov ah, 4Fh ;Neft filename
int 21h
jnc StoreFileName
mov [last], bx ;Save pointer to last file entry
mov al, [keepSorted] ;If returning form EXEC, need to resort files?
or al, al
jz DisplayFiles
jmp Sort0
;Main loop. Display files and wait for command.
DisplayFiles:
call BlankStatus ;Clear status line
mov si, OFFSET helpF1 ;Display help key
call DisplayString
mov bx, [cursor]
mov si, [bx]
lodsb ;Get attributes of file at cursor
mov [attrib], al ;Save attribute byte
call DisplayString ;Display name of highlighted file
```

```asm
mov bp, si ;Save pointer to time, data, size
test [attrib], 10h ;If a directory,
jz @@L7
mov di, 44 ; show '
```

' instead of file size

```asm
mov si, OFFSET dirMsg
call DisplayString
jmp SHORT @@L9
@@L7:
```

std ;File size, right justified

```asm
mov di, 56
mov ax, [FILE_SIZE]
mov dx, [FILE_SIZE + 2]
mov cx, 10000 ;Divide by 10000, show quotient|remainder
div cx
xchg ax, dx
or dx, dx
jz @@L8
mov cl, 4
call WriteDecimal
mov ax, dx
@@L8:
sub cl, cl
call WriteDecimal
@@L9:
std
mov di, 74 ;File data:
sub dx, dx
mov bx, [FILE_DATE] ;Year
mov al, bh
shr al, 1
add al, 80
sub ah, ah
mov cl, 2
call WriteDecimal
mov al, '/'
stosw
mov ax, bx ;Day
and ax, 1Fh
mov cx, 2
call WriteDecimal
mov al, '/'
stosw
mov ax, bx ;Month
mov cl, 5
shr ax, cl
and ax, 0Fh
mov cl, 2
call WriteDecimal
```

```asm
mov di, 86
mov bx, [FILE_TIME] ;File time:
mov ax, bx ;Minutes
mov cl, 5
shr ax, cl
and ax, 3Fh
mov cx, 2
call WriteDecimal
mov al, ':'
stosw
mov al, bh ;Hours
mov cl, 3
shr al, cl
sub ah, ah
sub cl, cl
call WriteDecimal
cld
mov di, 90
mov dl, [attrib] ;Display attribute letters
test dl, 1 ;Read-only
jz @@L3
mov al, 'R'
stosw
@@L3:
test dl, 2 ;Hidden
jz @@L4
mov al, 'H'
stosw
@@L4:
test dl, 4 ;System
jz @@L5
mov al, 'S'
stosw
@@L5:
test dl, 20h ;Archive
jz @@L6
mov al, 'A'
stosw
@@L6:
mov di, 100 ;Display path and filespec
mov si, OFFSET pathNSpec
```

```asm
call DisplayString
mov bx, [top]
mov di, 160
DisplayNext:
mov ah, NORMAL_VIDEO ;Set to inverse video if cursor line
cmp bx, [cursor]
jne @@L0
```

```asm
mov ah, INVERSE_VIDEO
@@L0:
cmp bx, [last] ;If done with files,
jle @@L0a
mov cx, 16 ;Blank out name area
jmp @@L7
@@L0a:
mov si, [bx] ;Get table entry for a file
lodsb ;Get status byte
test al, TAGGED ;If file has been tagged, display '>'
mov al, '>'
jnz @@L1
mov al, ' '
@@L1:
stosw
mov cx, 9 ;In field of 9,
@@L2:
lodsb ;Display filename up to extension
cmp al, '.'
je @@L3
or al, al
jz @@L6
@@L2a:
stosw
loop @@L2
@@L3:
cmp cx, 9 ;Check for special cases of '.', '..'
je @@L2a
cmp [byte si-2], '.'
je @@L2a
mov al, ' ' ;Else pad with spaces out to 9 chars
```

### rap stosw@@L4

```asm
mov cx, 6 ;Display extension in field of 6
@@L5:
lodsb
or al, al
jz @@L7
stosw
loop @@L5
jmp SHORT @@L7
@@L6:
add cx, 6 ;Just pad with blanks if no extension
@@L7:
mov al, ' '
```

rap stosw

```asm
cmp di, 4000 ;Stop at screenful
je GetCommand
cmp di, 3872
jb @@L8
```

```asm
sub di, 3808 ;Neft column
@@L8:
add di, 128 ;Neft row
add bx, 2
jmp DisplayNext
;Get command
GetCommand:
mov es, [programSeg]
mov ah, 8 ;Get keypress
sub ch, ch
@@L1:
```

inç ch

```asm
int 21h
or al, al
jz @@L1
mov ah, ch ;AH = 2 if aux code, 1 if plain ASCII
call ToUpper
mov di, OFFSET CommandKeys ;Look it up, get pointer to routine
mov cx, NCOMMANDS
repne scasw
jne InvalidCommand
add di, CommandAddrs-CommandKeys-2
mov bx, [cursor] ;SI -> file record for highlighted file
mov si, [bx]
jmp [word di] ;Jump to routine
InvalidCommand:
call Beep
jmp GetCommand
; Commands
Up:
sub bx, 2
jmp SHORT NewLine
Down:
add bx, 2
jmp SHORT NewLine
Left:
sub bx, 48
jmp SHORT NewLine
Right:
add bx, 48
jmp SHORT NewLine
PageUp:
sub bx, 238
jmp SHORT NewLine
PageDown:
add bx, 238
NewLine:
cmp bx, [last] ;Make sure cursor is still within bounds
jbe @@L1
```

```asm
mov bx, [last]
@@L1:
cmp bx, OFFSET files
jae @@L2
mov bx, OFFSET files
@@L2:
cmp bx, [top] ;Slide window if off screen
jae @@L3
mov [top], bx
jmp SHORT @@L4
@@L3:
mov ax, bx
sub ax, 238
cmp ax, [top]
jb @@L4
mov [top], ax
@@L4:
mov [cursor], bx
jmp DisplayFiles
Tag:
test [byte si], NOT NORMAL_FILE ;Only allow marking of normal files
jnz @@L1
xor [byte si], TAGGED
@@L1:
jmp DisplayFiles
Go:
mov [byte inputString], 0 ;Initialize to no user-entered command tail
Go0:
lodsb ;Get attribute byte
mov dx, si ;Join path and file name
mov si, PATH
mov di, OFFSET buffer
call Join
test al, 10h ;If a directory,
jz DoExec
ChangeDir:
mov dx, OFFSET buffer
mov ah, 3Bh ;Change to it
int 21h
mov [byte PATH], 0 ;No path now
mov di, FILESPEC ;Read in contents of new directory
jmp NewDir
DoExec:
mov si, dx ;Find extension
@@L1:
lodsb
cmp al, '.'
je @@L2
or al, al
```

```asm
jne @@L1
jmp SHORT @@L4
@@L2:
mov di, OFFSET extensions ;If .EXE, .COM or .BAT, execute it
mov dx, si
@@L3:
mov si, dx
mov cx, 3
repe cmpsb
je @@L5
sub al, al
repne scasb
cmp [byte di], 0
jne @@L3
@@L4:
mov si, OFFSET notExecMsg ;Else error, not an executable file
jmp DoError
@@L5:
call BlankScreen
mov dx, OFFSET buffer ;If .BAT, need COMMAND.COM, otherwise don't
cmp [byte di], 0
jne @@L6
mov si, OFFSET CC
```

label DoEdit near ;Edit function enters here

```asm
mov di, OFFSET EXECCmdLine+1
call CopyString ;Store '/c ' or '/c ' to command tail
mov dl, cl
mov si, OFFSET buffer ;Append path\file
call CopyString
add dl, cl
mov [EXECCmdLine], dl ;Store length, append CR
mov [byte di], 13
mov dx, [comspecOff]
mov ds, [comspecSeg]
@@L6:
cmp [byte cs:inputString], 0 ;If a command tail was entered,
jz DoDOS
push ds
mov ds, [cs:programSeg]
mov di, OFFSET EXECCmdLine+1
mov al, ' ' ;Add a space
stosb
mov si, OFFSET inputString ;Add command tail
call CopyString
```

inç cl

```asm
add [EXECCmdLine], cl
mov [byte di], 13
pop ds
DoDOS:
```

```asm
mov cx, bx
mov bx, (inputString-BOF)/16+1 ;Release unneeded memory
mov ah, 4Ah
int 21h
jc SysErr
call BlankScreen
push cx
mov [cs:temp], sp ;Do EXEC
mov bx, OFFSET EXECParams
mov ax, 4B00h
int 21h
mov bx, cs ;Restore critical registers
mov ds, bx
mov es, bx
mov ss, bx
mov sp, [temp]
pop bx
jnc @@L2
mov si, OFFSET sysErrMsg ;EXEC error
cmp al, 8 ;If return code = 8, no room
jne @@L1
mov si, OFFSET noExecRoomMsg
@@L1:
jmp DoError
@@L2:
mov [byte EXECCmdLine], 0 ;Tidy up
call HideCursor
jmp Restart0
SysErr:
mov si, OFFSET sysErrMsg
DoError:
call Error
jmp DisplayFiles
GoCL:
mov si, OFFSET commandTailMsg ;Prompt for command tail
call Query
mov si, [bx]
jmp Go0
DOS:
call BlankScreen
mov dx, [comspecOff]
mov ds, [comspecSeg]
jmp DoDOS
Edit:
lea dx, [si+1] ;Join path and file name
mov si, PATH
mov di, OFFSET buffer
call Join
mov si, OFFSET editor ;Invoke editor
```

```asm
mov [byte inputString],0
jmp DoEdit
Copy:
mov [byte CMDR], COPYVAL ;Set Copy/Move/Delete/Remove key to Copy
jmp SHORT DoCopy
Delete:
mov [byte CMDR], DELETEVAL ;Set Copy/Move/Delete/Remove key to Delete
jmp SHORT DoCMDR
Move:
mov [byte CMDR], MOVEVAL ;Set Copy/Move/Delete/Rename key to Move
DoCopy:
mov si, OFFSET DestMsg ;If Copy or Move, prompt for destination
call Query
mov di, si
mov [byte si], '\' ;Append '\'
```

inç si

```asm
mov [temp], si
cmp [byte CMDR], MOVEVAL
jne DoCMDR
mov ax, [word FILESPEC] ;If Move to same drive,
mov dx, [word inputString]
cmp ah, ':'
je @@L1
cmp dh, ':'
jne @@L2
@@L1:
cmp ax, dx
jne DoCMDR
@@L2:
mov [byte CMDR], RENAMEVAL ; do Rename instead (much faster)
DoCMDR:
mov bp, OFFSET files - 2 ;For each file
CMDRNext:
add bp, 2
cmp bp, [last]
jbe @@L0
jmp GetFileRecords
@@L0:
mov si, [bp] ;Skip if not tagged
lodsb
test al, TAGGED
jz CMDRNext
xor [byte si-1], TAGGED ;Else untag
mov dx, si
mov si, PATH ;Source path\filename -> sourceFileSpec
mov di, OFFSET sourceFileSpec
call Join
cmp [byte CMDR], DELETEVAL ;If not Deleting
je @@L4
```

```asm
mov si, dx ;Append current file's name to destination path
mov di, [temp]
call CopyString
cmp [byte CMDR], RENAMEVAL ;If Rename, do it
jne @@L2
```

label DoRename near

```asm
mov dx, OFFSET sourceFileSpec
mov di, OFFSET inputString
mov ah, 56h
int 21h
jc CantOpen
@@L1:
jmp CMDRNext
@@L2:
mov dx, OFFSET sourceFileSpec ;Copy or Move: open source, dest files
mov ax, 3D00h
int 21h
jc CantOpen
mov [sourceHandle], ax
sub cx, cx
mov dx, OFFSET inputString
mov ax, 3C00h
int 21h
jc CantRename
mov [destHandle], ax
@@L3:
mov bx, [sourceHandle] ;Read a bufferful
mov cx, 1024
mov dx, OFFSET buffer
mov ah, 3Fh
int 21h
jc ReadError
mov bx, [destHandle] ;Write it
mov cx, ax
mov ah, 40h
int 21h
jc WriteError
cmp cx, 1024 ;Loop until done
je @@L3
mov ah, 3Eh ;Close files
mov bx, [sourceHandle]
int 21h
mov bx, [destHandle]
int 21h
cmp [CMDR], MOVEVAL ;If Move, now do Delete
jne @@L1
@@L4:
mov bx, OFFSET sourceFileSpec ;Delete file
mov ah, 41h
```

```asm
int 21h
jnc @@L1
CantOpen:
mov si, OFFSET cantOpenMsg
jmp DoError
CantRename:
mov si, OFFSET cantRenameMsg
jmp DoError
ReadError:
mov si, OFFSET readMsg
jmp DoError
WriteError:
mov si, OFFSET writeMsg
jmp DoError
NewFilespec:
mov si, OFFSET newSpecMsg ;Prompt for new filespec
call Query
```

inç al

```asm
mov [FILESPEC-2], al ;Store count of chars
mov si, OFFSET inputString
mov di, FILESPEC
call CopyString ;Copy new filespec to command tail area
mov [byte di], 0Dh ;Append CR
jmp NewSpec ;Process new filespec
Rename:
lea dx, [si + 1] ;Join path and current name
mov si, PATH
mov di, OFFSET sourceFileSpec
call Join
mov si, OFFSET newNameMsg ;Prompt for new name of file or directory
call Query
jmp DoRename
Drive:
mov si, OFFSET newDriveMsg ;Prompt for letter of drive to change to
call QueryChar
sub al, 'A'
mov dl, al
mov ah, 0Eh
int 21h
cmp dl, al ;Try again if that drive doesn't exist
jb @@L1
mov si, OFFSET badDriveMsg
jmp DoError
@@L1:
jmp Restart
Sort:
;Sort algorithm:
; 1) make up array of records {pointer to field to sort | tag},
;one for each
```

```asm
; file, in 'buffer'.
; 2) bubble-sort these records
; 3) copy file record pointers in 'files' to 'buffer' in
;order of sorted tags
; 4) copy file record pointers back to 'files' in new order
mov si, OFFSET sortMsg ;Prompt for sort field
call QueryChar
cmp al, 'N' ;Check for legal sort field option
je Sort0
cmp al, 'E'
je Sort0
cmp al, 'D'
je Sort0
mov si, OFFSET genErrorMsg
jmp DoError
Sort0:
mov [keepSorted], al ;Remember for later resorting after EXEC
mov dl, al
sub dh, dh < ;DH = tag (position of file in current order)
mov di, OFFSET buffer
mov bx, OFFSET files
@@L1:
mov si, [bx] ;Find field to sort: get pointer to record
@@L1a:
```

inç si

```asm
mov cx, si
cmp dl, 'N' ;If Name, already pointing at it
je @@L4
sub ah, ah ;If data, find null at end of name
cmp dl, 'E' ;If Ext find '.' or end of name
jne @@L2
cmp [byte si], '.' ;'.' and '..' are special cases
je @@L1a
mov ah, '.'
@@L2:
lodsb
or al, al
je @@L3
cmp al, ah
jne @@L2
@@L3:
dec si ;If Ext, back up to '.' or null
cmp dl, 'E'
je @@L4
add si, 3 ;If data, advance to data field
@@L4:
mov ax, si ;Store pointer to field to sort
stosw
mov al, dh ;Store tag
```

```asm
stosb
```

inç dh ;Bump tag

```asm
add bx, 2 ;Loop until no more files
cmp bx, [last]
jbe @@L1
DoSort:
lea bp, [di-3] ;BP -> last
push bp
@@L0:
mov bx, OFFSET buffer ;Do bubble sort
@@L1:
mov si, [bx]
cmp [word si-1], '.' ;Leave '.' and '..' alone
je @@L4
mov di, [bx+3]
cmp dl, 'D' ;If sorting Dates, compare one word
jne @@L2
cmpsw
jmp SHORT @@L3
@@L2:
mov cx, -1 ;Else compare bytes until not equal
repe cmpsb
@@L3:
jbe @@L4 ;If first field > second
mov ax, [bx] ;Exchange field pointers and tags
xchg ax, [bx+3]
mov [bx], ax
mov al, [bx+2]
xchg al, [bx+5]
mov [bx+2], al
@@L4:
add bx, 3 ;Loop until no more files this pass
cmp bx, bp
jb @@L1
sub bp, 3
cmp bp, OFFSET buffer ;Loop until no more passes
jne @@L0
OrderByTags:
mov di, OFFSET buffer ;Arrange file pointers in order of tags
mov si, OFFSET files
pop bp
@@L1:
mov bl, [di+2] ;Get tag
sub bh, bh
add bx, bx
mov ax, [bx+si] ;Get file ptr associated with that tag
stosw ;Store in place of field pointer in sort buffer
```

inç di

```asm
cmp di, bp
```

```asm
jbe @@L1
mov si, OFFSET buffer
mov di, OFFSET files
@@L2:
movsa ;Copy file pointers back in new order
```

inç si

```asm
cmp di, [last]
jbe @@L2
jmp DisplayFiles
Help:
call BlankStatus ;Display help on status line
mov si, OFFSET helpMsg
call DisplayString
mov ah, 8
int 21h
jmp DisplayFiles
Exit:
call BlankScreen
mov ax, 4C00h ;Bye
int 21h
; Subroutines
WriteDecimal:
;Display a decimal number in inverse video, writing digits
;backwards form right.
; IN: AX = number, CL = field width with leading 0s (no leading
;0s if CL = 0)
; ES:DI -> Video RAM where rightmost digit will go
; OUT: AH = INVERSE_VIDEO
;USED: AL, CX
push bx
push dx
mov bx, 10
sub ch, ch
@@L1:
sub dx, dx ;Get a digit
div bx
xchg ax, dx ;Write it to display, right to left
add ax, '0' + INVERSE_VIDEO*100h
stosw
xchg ax, dx
cmp cx, 0 ;If CX > 0, loop even if AX = 0
jg @@L2
or ax, ax ;Else loop only if AX > 0 (more digits left)
jz @@L3
@@L2:
loop @@L1
@@L3:
pop dx
pop bx
```

```asm
mov ah, INVERSE_VIDEO
Ret1:
ret
DisplayString:
;Display string on status line.
; IN: SI -> string (null-terminated),
;ES:DI -> status line, AH = attribute
; OUT: DI is advanced past end of string
;USES: AL SI
@@L1:
lodsb
or al, al
jz Ret1
stosw
jmp @@L1
Error:
;Beep, display string on status line and wait for keypress (any key)
; IN: SI -> string
; OUT: ES -> program segment
;USED: AX
call Beep
call BlankStatus
call DisplayString ;Display error string
mov si, OFFSET ErrorMsg ;Display 'Press any key' message
call DisplayString
mov ah, 8
int 21h
mov es, [programSeg]
ret
Query:
;
;Prompt for string input on status line
; IN: SI -> message
; OUT: SI -> null at end of ASCIIZ string input,
;AX = length (excluding null)
;USED: none
push bx
push cx
push dx
push di
push es
call BlankStatus
call DisplayString
mov dx, di ;Set cursor to end of printed string
add dx, 2
shr dl, 1
sub dh, dh
mov ah, 2
sub bx, bx
```

```asm
int 10h
mov cx, 80 ;Get input
mov dx, OFFSET inputString
mov si, dx
mov ah, 3Fh
int 21h
sub ax, 2
add si, ax
mov [byte si], 0 ;Null-terminate it
call HideCursor ;Hide cursor
pop es
pop di
pop dx
pop cx
pop bx
ret
QueryChar:
;
;Prompt for single character input
; IN: SI -> message
; OUT: AL = character (lower case converted to upper)
;USED: AH
push es
call BlankStatus
call DisplayString ;Display string
mov ah, 8 ;Get char
int 21h
call ToUpper
pop es
ret
BlankStatus:
;
;Clear top line of display to inverse video
; IN: none
; OUT: ES = video segment, DI = 0
;USED: AX CX
mov ax, [displaySegment]
mov es, ax
sub di, di
mov ax, ' ' + INVERSE_VIDEO*100h
mov cx, 80
```

rap stosw

```asm
sub di, di
ret
Join:
;
;Copy counted path, then ASCIIZ file name to buffer and null-terminate
; IN: SI -> path, DX -> file, DI -> destination
; OUT: DI -> null at end of copied string,
```

```asm
;CX = total chars excluding null
;USED: none
push ax
push si
lodsb ;Get count of chars in path (a counted string)
sub ah, ah
mov cx, ax
```

rap movsb ;Copy it to destination

```asm
mov cx, ax
mov si, dx ;Now copy file name (null-terminated)
call CopyString
add cx, ax ;Sum string counts -> CX
mov [byte di], 0 ;Null-terminate the result
pop si
pop ax
ret
CopyString:
;
;Copy null-terminated string.
; IN: SI -> string, DI -> destination
; OUT: CX = length (excluding null), DI -> terminating
;null of copied string
;USED: AL
mov cx, -1
@@L1:
lodsb ;Copy string
stosb
or al, al ;Until null at end is encountered
loopnz @@L1 ;Accumulate count of chars
```

neg cx ;Adjust count

```asm
sub cx, 2
dec di ;DI -> terminating null
ret
HideCursor:
;
;Move cursor off bottom of screen
; IN: none
; OUT: none
;USED: AH BH DX
mov dx, 1900h
sub bh, bh
mov ah, 2
int 10h
ret
Beep:
;
;Output a bell char
; IN: none
; OUT: none
```

```asm
;USED: AH DL
mov dl, 7
mov ah, 2
int 21h
ret
BlankScreen:
;
;Clear screen and home cursor
; IN: none
; OUT: none
;USED: AX
push bx
push cx
push dx
push es
push di
mov es, [cs:displaySegment] ;Blank screen
sub di, di
mov ax, ' '+NORMAL_VIDEO*100h
mov cx, 25 * 80
```

rap stosw

```asm
sub dx, dx ;Put cursor at upper L hand corner
sub bh, bh
mov ah, 2
int 10h
pop di
pop es
pop dx
pop cx
pop bx
ret
ToUpper:
;
;Convert lower to upper case
; IN: AL = char
; OUT: AL = char
;USED: none
cmp al, 'a'
jb @@L1
cmp al, 'z'
ja @@L1
add al, 'A'-'a'
@@L1:
ret
;Data
;Command dispatch table: aux,2 or ASCII,1 paired to
;command routine addresses
commandKeys db 72,2, 80,2, 75,2, 77,2, 73,2, 81,2, 'T',1, 13,1, 'C',1
```

db 'D',1, 'M',1, 'R',1, 'E',1, 'F',1, 'V',1, 'S',1

db 60,2, 10,1, 59,2, 27,1

```asm
commandAddrs dw Up, Down, Left, Right, PageUp, PageDown, Tag, Go, Copy
```

dw Delete, Move, Rename, Edit, NewFilespec, Drive, Sort dw DOS, GoCL, Help, Exit

```asm
NCOMMANDS EQU (commandAddrs-commandKeys)/2
;Strings
helpMsg db 'Copy Delete Edit Filespec Move Ren Sort '
```

db 'Tag driVe Enter=cd/run F2=DOS Esc=exit',0

```asm
helpF1 db 'Help F1',186,0
noFilesMsg db 'No matching files or invalid path',0
noRoomMsg db 'Out of room$'
cantRenameMsg db "Can't rename to that",0
badPathMsg db 'Bad path',0
sysErrMsg db 'System error',0
cantOpenMsg db "Can't open file",0
writeMsg db 'Write error',0
readMsg db 'Read error',0
notExecMsg db 'Not a directory or executable file',0
badDriveMsg db "Drive doesn't exist",0
genErrorMsg db 'Error',0
tooManyMsg db 'Too many files',0
noExecRoomMsg db 'Not enough memory',0
ErrorMsg db '. Press any key.',0
destMsg db 'Where to?',0
newSpecMsg db 'New filespec:',0
newDriveMsg db 'New drive:',0
sortMsg db 'Sort on: Name Ext data',0
newNameMsg db 'New name:',0
commandTailMsg db 'Command tail:',0
dirMsg db '
```

',0

```asm
extensions db 'EXECOMBAT',0
starDotStar db '*.*',0
editor db '/C E ', 12 dup (0)
cc db '/C ',0
comspec db 'COMSPEC='
;EXEC function parameter block
EXECParams dw 0
EXECCmdLineOff dw OFFSET EXECCmdLine
programSeg dw 0
```

dw -1, -1 , -1 , -1

```asm
EXECCmdLine db 0, 80 dup (?)
sourceFileSpec EQU EXECCmdLine ;Second use for this space during Copy etc.
;Variables, buffers
```

dw 128 dup (?) ;Stack (here for protection during EXEC)

### stackEnd

```asm
keepSorted db ? ;Holds sort subcommand char if this dir sorted
CMDR db ? ;Key for Copy/Move/Delete/Rename actions
attrib db ? ;File attribute byte
```

```asm
sourceHandle dw ? ;Source handle for Copy, etc.
destHandle dw ? ;Destination handle for Copy etc.
cursor dw ? ;Position in 'files' of highlighted file
last dw ? ;Position in 'files' of last file in directory
top dw ? ;Position in 'files' of file at top of screen
temp dw ? ;Holds SP during EXEC, other uses
comspecSeg dw ? ;Segment of environment
comspecOff dw ? ;Offset of 'C:\COMMAND.COM' in environment
displaySegment dw ? ;Segment of display RAM
pathNSpec db 80 dup (?) ;Default path and current filespec for display
DTA db 64 dup (?) ;Disk Transfer Area
inputString db 80 dup (?) ;String returned by 'Query', other uses
files dw NFILES dup (?) ;Array of pointers to file records
fileRecords db 80*NFILES dup (?) ;File records: attrib/name/time/data
buffer db 1024 dup (?) ;Buffer for Copy, etc., other uses
EOF:
end Start
```

Finding the Largest and Smallest in an Unsorted List

### PAGE 60 , 80

### TITLE MAX MIN BUL

```asm
.MODEL SMALL
.CODE
ORG 100H
BAS: JMP SHORT ANA
LISTE DW 2245,4425,40008,22012,34209,36377
ANA PROC NEAR
CLD (LOOK FROM LEFT TO RIGHT)
PUSH CX
PUSH DI
MOV CX , 06
MOV DI , OFFSET LISTE
MOV BX , ES : [DI]
MOV AX , BX
```

### ARA ADD DI , 2

```asm
CMP ES : [DI] , BX
JAE MAKSI
MOV BX,ES:[DI]
JMP TARA
MAKSI: CMP ES,[DI],AX
JBE TARA MOV AX,ES:[DI]
TARA: LOOP ARA
POP DI
POP CX
MOV AH,4CH
INT 21H
```

### ANA ENDP

```asm
END BAS
```

### REFERENCES

- Nurettin Topaloğlu, Mikroişlemci mimarisi ve

Assembly Dili Seçkin yayıncılık 2001

- Abel Peter, IBM PC Assembly Language and

porgramming, international 5th edition, prentice hall, 2000

- GümüşKaya Haluk, Mikroişlemciler ve bilgisayar

intel ailesi ve IBM PC, alfa yayınları 2000

- Scanlo leo, 8086-8088-80286 Assembly Language,

Brady book, 1988

- Dreiver George, introduction to programming in

Assembly language (IBM PC) west puclishing co.1993

- Hyde randal, the art of Assembly language and HLA,

1996

- www.sdu.com.tr

- www.selcuk.com.tr

- www.afyon.com.tr

*Note: The résumé, contact, and personal-information pages have been removed from the download copy. Program-writing and translation errors in the source text have been preserved.*
