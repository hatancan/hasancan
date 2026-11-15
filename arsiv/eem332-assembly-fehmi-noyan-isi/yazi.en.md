---
baslik: EEM332 Microprocessors: Assembly Programming Language (Fehmi Noyan İsi)
ozet: July 2003 notes on 16-bit x86 assembly: registers, flags, instructions, and program examples.
---

This post brings together the related notes and exercises from the Başkent University **EEM332 Microprocessors** course archive (2003–2003). July 2003 notes on 16-bit x86 assembly: registers, flags, instructions, and program examples. Source: a personal lecture note by Fehmi Noyan İsi, affiliated with Gaziantep University, July 2003. PDF archive copies of the documents and, where available, their source code can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes, with the source credited. It will be removed at the request of the rights holder.*

## assembly

Assembly Programming Language, July 2003

Prepared by: Fehmi Noyan İSİ fni18444@gantep.edu.tr – fnoyanisi@yahoo.com http://www2.gantep.edu.tr/~fni18444



This document describes the general structure of 16-bit Assembly programming for the processors that Intel designates as the 80x86 series: the 8086, 80186, 80286, 80386, 80486 and Pentium. For that reason, the document covers assembly language only for the 8086, 80186 and 80286 (Intel's 16-bit processors). The examples are written for the MS-DOS operating system. Assembly programming for the Windows operating system is 32-bit and is not covered in this document. The section "Assembly Language under Linux" describes the use of assembly language under the Linux operating system. Because many of the sources on assembly programming you will come across keep using certain basic terms and expressions in their original English form, I too have not used the Turkish equivalents of many terms and expressions. Although this may in some cases make the text a little plainer, I believe it is more useful to learn the concepts under their widely known names.

Fehmi Noyan İSİ

Table of Contents Introduction                                                7

Chapter 1: Fundamentals                                   8 1.1 Number Systems                               8 1.2 Data Types                                   8 1.2.1 Bit                                      8 1.2.2 Byte                                     8 1.2.3 Word                                     8 1.2.4 Double Word (Long)                       8 1.3 Logical Operations on Bits                   9 1.4 Signed and Unsigned Numbers                  9 1.5 Shift and Rotate Operations                  10

Chapter 2: The Microprocessor (CPU) and Memory      11 2.1 The Microprocessor and Its Structure           11 2.1.1 Data Registers                            11 2.1.2 Pointer and Index Registers               12 2.1.3 Segment Registers                         12 2.1.4 Instruction Pointer                       12 2.1.5 Flag Register                             12 2.1.5.1 Carry Bit                            13 2.1.5.2 Parity Bit                           14 2.1.5.3 Auxiliary Carry Bit                  14 2.1.5.4 Zero Bit                             14 2.1.5.5 Sign Bit                             14 2.1.5.6 Trace Bit                            14 2.1.5.7 Interrupt Bit                        14 2.1.5.8 Direction Bit                        15 2.1.5.9 Overflow Bit                         15 2.2 Memory and Its Structure                       15 2.3 Stack                                          16 2.4 Memory Addressing in 80x86 Processors          18 2.4.1 Direct Addressing                         18 2.4.2 Indirect Addressing                       18 2.4.3 Indexed Addressing                        19 2.4.4 Based Indexed Addressing                  19 2.4.5 Based Indexed + Constant (Disp) Addressing 20

Chapter 3: The 80x86 Instruction Set                 20 3.1 Transfer Instructions                          21 3.1.1 MOV Instruction                           22 3.1.2 XCHG Instruction                          23 3.1.3 LEA Instruction                           23 3.1.4 PUSH Instruction                          24 3.1.5 PUSHF Instruction                         24

3.1.6 POP Instruction                  24 3.1.7 POPF Instruction                 25 3.1.8 LAHF Instruction                 25 3.1.9 SAHF Instruction                 25 3.2 Input/Output Instructions             26 3.2.1 IN Instruction                   26 3.2.2 OUT Instruction                  26 3.3 Arithmetic Instructions               26 3.3.1 ADD Instruction                  27 3.3.2 ADC Instruction                  27 3.3.3 SUB Instruction                  27 3.3.4 SBB Instruction                  28 3.3.5 MUL Instruction                  28 3.3.6 IMUL Instruction                 29 3.3.7 DIV Instruction                  29 3.3.8 IDIV Instruction                 30 3.3.9 INC Instruction                  30 3.3.10 DEC Instruction                 31 3.3.11 CMP Instruction                 31 3.4 Logical Instructions                  32 3.4.1 AND Instruction                  32 3.4.2 TEST Instruction                 32 3.4.3 OR Instruction                   32 3.4.4 XOR Instruction                  32 3.4.5 NOT Instruction                  33 3.5 Shift and Rotate Instructions         33 3.5.1 SHL/SAL Instructions             33 3.5.2 SHR Instruction                  33 3.5.3 SAR Instruction                  33 3.5.4 RCL Instruction                  34 3.5.5 ROL Instruction                  34 3.5.6 RCR Instruction                  34 3.5.7 ROR Instruction                  34 3.6 Branch Instructions                   35 3.6.1 JMP (Unconditional Jump) Instruction 35 3.6.2 JZ/JE Instructions               36 3.6.3 JNZ/JNE Instructions             37 3.6.4 JB/JC/JNAE Instructions          38 3.6.5 JBE/JNA Instructions             38 3.6.6 JNB/JNC/JAE Instructions         38 3.6.7 JG/JNLE Instructions             38 3.6.8 JA/JNBE Instructions             38 3.6.9 JL/JNGE Instructions             38 3.6.10 JLE/JNG Instructions            38 3.6.11 JS and JNS Instructions         38 3.6.12 JO and JNO Instructions         39 3.6.13 JCXZ Instruction                39 3.7 Loop Instructions                     39

3.7.1 LOOP Instruction                               39 3.7.2 LOOPZ/LOOPE Instructions                       40 3.7.3 LOOPNZ/LOOPNE Instructions                     40

Chapter 4: Using Interrupts                                40

Chapter 5: The DEBUG Program                               41

Chapter 6: Using Assembly under the Linux Operating System 44 6.1 Intel and AT&T Syntaxes                             45 6.1.1 Source-Destination Direction                    46 6.1.2 Prefixes                                        46 6.1.3 Suffixes                                        46 6.1.4 Memory Operations                               47 6.1.5 INT 0x80 and Linux System Calls (Syscalls)      47 Examples                                                48

Internet Addresses                                         52

Introduction Assembly is a low-level language and is somewhat harder to understand than high-level programming languages such as C, C++, Pascal and Basic. When writing programs in assembly, the hardware features of the computer being used matter to the programmer. The code written is mostly hardware-dependent, which is a factor that reduces the portability of the program. When programming in assembly, the programmer deals directly with the computer's processor and memory. That is, it is possible to directly modify values in memory (in RAM) and in the processor's registers. Unlike the compilers of high-level languages, programs called an "assembler" and a "linker" are used to turn assembly source files into executable files. In fact, compilers can also be said to be a kind of assembler program. However, unless an extra parameter is used, a compiler first translates the source file into the required object file, and then, if no error is encountered, the resulting object file is turned into an executable file with the help of the linker. All programs run on our computer are first loaded into the computer's RAM. Then execution takes place in RAM. The information loaded into RAM is nothing other than the machine-language equivalent of our program. It would not be very wrong to call assembly language the form of machine language that a user can understand. In fact, the most important characteristics of assembly programs are that their size is much smaller than that of programs written in a high-level language and, accordingly, that they run much faster. The fast execution of programs stems from the simplicity of their code. However, the high-speed processors and large-capacity hard disks in use today make these characteristics of assembly programs unimportant. In the following example, a program that prints the letter "A" on the screen is written first in assembly and then in C and Pascal. Note the large difference between their sizes even though the programs do the same job.

Assembly Program                       C Program                       Pascal Program

#include <stdio.h>

```asm
MOV AH,02                                                              begin
MOV DL,41                           main()                              write('A')
INT 21                              {                                  end.
INT 20                               printf("A");
```

}

Assembler Information              Compiler Information                Compiler Information MS-DOS DEBUG                       Turbo C 2.01 for MS-DOS             FreePascal 0.9 for MS-DOS

Size: 8 bytes                       Size: 8330 bytes                   Size: 95644 bytes

As you can see, the program written in C is more than 1000 times larger than the one written in assembly! I don't think there is even any need to compare the size of the Pascal program with that of the assembly one. This difference may matter for an old computer, but it is not very important for a computer meeting today's standards. For this reason, the assembly programming language is today used mostly by system programmers and inline within other

programming languages. By "inline assembly" what is meant is using assembly code as is within a high-level language. This gives us the ability to easily access any part of the hard disk (for example the MBR), system resources such as the BIOS, or specific memory regions.

Chapter 1: Fundamentals 1.1 Number Systems The system we use in our everyday calculations is the decimal number system, and this system consists of the digits 0,1,2,3,4,5,6,7,8 and 9. Other numbers are obtained using these digits. For the computer we use (it would be better to say for all electronic devices), this is not the case. The computer uses the base-two number system, called the binary number system, in which there are only 0 and 1. For the computer, 0 means "false" (FALSE) and 1 means "true" (TRUE). On the other hand, the number base used when writing assembly programs is the base-sixteen system known as hexadecimal. The first ten digits used in this system are the same as in the decimal system and consist of the digits 0,1,...,9. For 10, 11, 12, 13, 14 and 15, the letters A, B, C, D, E and F are used respectively. When hexadecimal numbers are written, the letter "h" or "H" is placed at the end. The reason hexadecimal is used in assembly language is the difficulty of representing long numbers such as memory addresses in binary. It is clear that as the number base grows, the number of digits needed to represent any number decreases. For instance, if we wanted to write the address of a memory location such as "1BA5:010F" in binary, it would be "0001101110100101:0000000100001111", which is a number that is hard both to remember and to write.

1.2 Data Types 1.2.1 Bit We mentioned that the computer uses the binary number system. Each digit in this system is called a "bit", meaning Binary Digit. That is, a bit can hold one of two pieces of information, 0 or 1. The bit is the smallest unit of information for the computer.

1.2.2 Byte A group of eight bits is called a "byte". A byte can hold 256 different values, ranging from 0 to 255.

(binary) 00000000 = 0 (decimal) (binary) 11111111 = 255 (decimal)

As can be seen, the maximum value a byte can take is 255 and the minimum value is 0.

1.2.3 Word Two bytes (16 bits) of information is called a "Word". The maximum value a word can take is 65535 and the minimum value is 0. This means that 65536 different values can be stored in a word.

1.2.4 Double Word (Long) Combining two separate words yields a "Double Word". A double word is 32 bits long.

Because the amount of information the 8086, 80186 and 80286 processors can process at one time is 16 bits long, these processors are called 16-bit processors. Intel used a 32-bit information-processing system in its 80386 and later processors, and these processors are called 32-bit processors.

1.3 Logical Operations on Bits Processors perform many operations by means of logical comparisons. Four logical instructions are used in the assembly programming language: AND, OR, XOR and NOT. The truth tables of these instructions are given below.

```asm
AND       1      0                                   OR        1       0
```

1        1      0                                    1        1       1 0        0      0                                    0        1       0

```asm
XOR       1      0                                  NOT        1       0
```

1        0      1                                             0       1 0        1      0

Since the bytes used in our computer also consist of 1s and 0s, the CPU operates on the bits separately in every logical operation. I have given a few examples below.

1001 0110 1001 1111                                  1011 0010 1110 1010 1011 1101 0001 1110                                  1011 0000 0000 0000

```asm
AND _______________________________                    OR ____________________________
```

1001 0100 0001 1110                                  1011 0010 1110 1010

1010 1010 1000 1111                                  0010 0000 0000 1111

### 1110 1110 1100 0001                               NOT______________________________

### XOR________________________________                      1101 1111 1111 0000

0100 0100 0100 1110

1.4 Signed and Unsigned Numbers When data types were described earlier, the value range was defined as 0-255 for a byte and 0-65535 for a word. So what should we do if we want to use negative numbers in our operations? In this case, half of the region allocated for the byte, word or long is assigned to negative numbers and the other half to positive numbers. That is, the values a byte can take lie between –128....-1 and 0....127. Likewise, for a word this range is –32,768......+32,767. The leftmost bit of a byte, word or long is called the sign bit. If the value of the sign bit of our signed number is 0, the number is considered positive; if it is 1, negative. That is, 0110 0101 1110 1100 is a positive number (word) 1000 1100 1010 0000 is a negative number (word)

To find the negative of any number, its two's complement is found. For this:

### 1) The number is passed through a NOT operation

### 2) 1 is added to the result obtained

Now, let's try to find –13. +13 = 0000 1101 (byte)

### 1) The number is passed through a NOT operation

0000 1101

### NOT______________

1111 0010

### 2) 1 is added to the result obtained

1111 0010 +------------ 1111 0011      -13

Now let's test the result we obtained. 13+(-13) = 0000 1101 + 1111 0011 The result of the operation above should be zero.

0000 1101 1111 0011 +-------------- 1 0000 0000

If the carried 1 is disregarded, the result is zero, which shows that our operation is correct.

1.5 Shift and Rotate Operations Other logical operations performed on bit strings are shift and rotate operations. These two operations can themselves be divided into subcategories: right shift, left shift, and right rotate, left rotate.

1      0       1       1       1       0       0       1

If a right shift is applied to a byte like the one above, bit 7 takes the place of bit 6,

### bit 6 takes the place of bit 5, bit 5 takes the place of bit 4, .... 0 is written to the vacated bit 7 position, and the 1 value in bit 0

is thrown out of the bit string. The left shift operation is carried out in the same way. This time 0 is written to the vacated

### bit 0 position and bit 7 is left out of the operation.

0       1       0       1       1       1       0       0       After right shift

0       1       1           1       0       0       1       0   After left shift

In the rotate operation, just as in the shift operation, the bits are shifted one place to the right or left, but here, instead of zero, the value of bit 0 is written to the vacated bit 7 position, and the value of bit 7 is written to the vacated

### bit 0 position. That is, if right and left rotate operations are applied respectively to our byte above, results like the following are obtained.

1       1       0       1       1       1       0       0       After right rotate

0       1       1           1       0       0       1       1   After left rotate

Chapter 2: The Microprocessor (CPU) and Memory 2.1 The Microprocessor and Its Structure The part of today's computers that interprets and processes information is the computer's central processing unit. The central processing unit (CPU) communicates with memory and various input/output units using data paths called buses. Processors are classified as 8-bit, 16-bit and 32-bit processors according to the information transfer of their internal and external lines and the maximum amount of information they can process. The assembly language described in this document is for the Intel 8086 series, a 16-bit processor (external and internal data transfer is done in words). The fact that the language is for the 8086 series does not mean that the programs you write will not run on the 8088, 80186, 80286, 80386, 80486, Pentium and Celeron series and on AMD processors. The processor consists of compartments called registers. We can group these registers as Data registers, Pointer and Index registers, Segment registers, the Instruction Pointer, and the Program Status Word (Flag register). The register structure of the 8086 processor is shown simply below.

2.1.1 Data Registers As can be seen in the figure, the 8086 processor has 14 registers of 16-bit capacity. Of these registers, the Data registers (AX, BX, CX and DX) are each divided into two registers of 8-bit capacity. These registers are named AH and AL for AX, BH and BL for BX, CH and CL for CX, and DH and DL for DX. AH is called the 8-bit high part of the 16-bit AX register, and AL is called the 8-bit low part of the 16-bit AX register. When writing our programs, we make use of these 8-bit registers in processing 8-bit data. As we will see in later sections, the data registers are reserved by the CPU in many operations (loops, use of interrupts, mathematical operations...). In these cases we have no chance of changing the value in the register.

In our programs, a change in the value of the BH or BL register will directly change the value of the BX register. The same applies to the other data registers. To give an example: let the value of our BX register be A43F. In this case BH=A4 and BL=3F. Now let us change the value of BL to 05. In the end BX=A405, BH=A4 and BL=05. (The given example will be easier to understand if the figure above is examined)

2.1.2 Pointer and Index Registers Pointer and index registers are used to reach any point in memory. For this, the operation is carried out by assigning the offset and segment addresses of the point to be reached to the required registers. (This subject will be treated in more detail in Section 2.2, Memory and Its Structure.)

2.1.3 Segment Registers The segment registers (CS, DS, SS and ES) hold the starting addresses of the sections (Segments) created in memory when our program is loaded into the computer's memory. That is, these registers can be called a kind of location pointer. CS holds the starting address of the memory region containing the executable code of our program (Code Segment). That is, our machine-language code is at the place indicated by CS. DS is the section where the variables in our program are stored. SS holds the starting address of the stack section allocated in memory for our program. The stack is used, with the PUSH and POP instructions we will see later, to put values into and take values out of memory, to hold the address information that says where programs and functions will go after they terminate, and to store the parameters passed to programs and functions. In UNIX-based systems the stack is also used to specify the parameters required for using interrupts. ES (Extra segment) is used mostly for string operations.

2.1.4 Instruction Pointer The Instruction Pointer register stores the memory address of the next instruction to be processed by the processor. No operation can be performed on this register by the programmer. After each instruction is executed, the CPU automatically assigns the required value to this register according to the instruction used.

2.1.5 Flag Register The Flag Register is in a different situation from the other registers. Unlike the other registers, which are treated as a whole in 16-bit form, each bit of the flag register has a separate meaning for the CPU (only 9 of them are used by the 8086 processor). The special names of these bits are given below. O : Overflow flag D : Direction flag I : Interrupt flag T : Trace flag S : Sign flag Z : Zero flag A : Auxiliary Carry flag P : Parity flag C : Carry flag

Since the computer uses the binary number system, the value in these registers is at any moment either 1 or 0. A bit being 1 is called "Set", and a bit being 0 is called "Reset". The processor makes use of the states of these bits while executing many instructions.

2.1.5.1 Carry Bit The event arising from the number placed in the destination field during any operation performed by the processor not fitting into the destination field is called a "carry" (overflow out of the field). If the CPU encounters a carry as the result of an operation, the value of the carry flag is made 1. Below, two 16-bit numbers are added and a carry occurs in the result. (The carried bit is shown in red)

### 1111 1001 0110 1010            F96A

### 0010 1010 1111 1001            2AF9

+---------------------------- 1 0010 0100 0110 0011            2463        CF=1 The result of adding F96A and 2AF9 is the number 2463, which is smaller than both numbers. Since the numbers we have are positive, it is impossible to obtain a number smaller than the ones we have as a result of an addition. In this case the CPU sets the value of the carry flag to 1 and thereby obtains a 17-bit number.

```
C:\WINDOWS\Desktop>debug
```

-a100

```
1E40:0100 MOV AX,F96A
1E40:0103 MOV BX,2AF9
1E40:0106 ADD AX,BX
1E40:0108
-t
```

```
AX=F96A BX=0000        CX=0000 DX=0000 SP=FFEE           BP=0000 SI=0000 DI=0000
DS=1E40 ES=1E40        SS=1E40 CS=1E40 IP=0103            NV UP EI PL NZ NA PO NC
1E40:0103 BBF92A             MOV    BX,2AF9
-t
```

```
AX=F96A BX=2AF9        CX=0000 DX=0000 SP=FFEE           BP=0000 SI=0000 DI=0000
DS=1E40 ES=1E40        SS=1E40 CS=1E40 IP=0106            NV UP EI PL NZ NA PO NC
1E40:0106 01D8               ADD    AX,BX
-t
```

```
AX=2463 BX=2AF9        CX=0000 DX=0000 SP=FFEE           BP=0000 SI=0000 DI=0000
DS=1E40 ES=1E40        SS=1E40 CS=1E40 IP=0108            NV UP EI PL NZ AC PE CY
1E40:0108 A394D3             MOV    [D394],AX                      DS:D394=A2A2
```

The screen output above was obtained by trying the example I gave under the debug program. First, the value of the AX register was set to F96A with "MOV AX,F96A". We can see this with AX=F96A after the first t command (examine the value of AX in the section after the 1st t command). Then the value of BX was set to 2AF9 with "MOV BX,2AF9" (examine the value of BX in the section after the 2nd t command). Finally, these two values were added with "ADD AX,BX" and assigned to AX. After the last "t" command, AX=2463 and the "NC" expression at the end has turned into "CY", which shows that a carry occurred as the result of the operation.

2.1.5.2 Parity Bit If, as the result of an operation, the low-order byte of the word is divisible by two with no remainder, this bit is set to 1; otherwise it is set to 0. Whether the number in the high-order byte of the result is divisible by two is not important for this flag.

2.1.5.3 Auxiliary Carry Bit If, as a result of an operation performed by the CPU, a carry occurs out of the first four bits of the destination field, the value of this flag is set to 1. In the example given above for the carry flag, the sum of 1010 (hex A), the first four bits of the first number, and 1001 (hex 9), the first four bits of the second number, yielded the number 0011 and a carry was passed to the next bit. The value of the bit, which was NA (0) before the ADD operation, became AC (1) after the operation.

2.1.5.4 Zero Bit If the result of any operation is zero, this flag is set.

-a100

```
1E40:0100 mov ax,12
1E40:0103 xor ax,ax
1E40:0105
-t
```

```
AX=0012 BX=0000         CX=0000 DX=0000 SP=FFEE             BP=0000 SI=0000 DI=0000
DS=1E40 ES=1E40         SS=1E40 CS=1E40 IP=0103              NV UP EI PL NZ NA PO NC
1E40:0103 31C0                XOR    AX,AX
-t
```

```
AX=0000 BX=0000         CX=0000 DX=0000 SP=FFEE             BP=0000 SI=0000 DI=0000
DS=1E40 ES=1E40         SS=1E40 CS=1E40 IP=0105              NV UP EI PL ZR NA PE NC
1E40:0105 F0                  LOCK
1E40:0106 01D8                ADD    AX,BX
```

Above, the value of the AX register is first set to 12. Then this register is XORed with itself. XORing a number with itself yields 0. This situation set the value of the zero flag ( NZ ZR ).

2.1.5.5 Sign Bit In signed numbers, bit 7 of the number for a byte (8 bits) and bit 15 of the number for a word (16 bits) is called the sign bit. As a result of an operation, the sign bit in the destination field is copied into the sign flag. That is, if the value of the sign bit is 0, the result obtained is considered positive; if it is 1, the result obtained is considered negative.

2.1.5.6 Trace Bit It is used to make the CPU execute only one instruction and then wait. The "Trace" operation used by DEBUG is carried out by setting this flag.

2.1.5.7 Interrupt Bit It indicates whether the CPU will take into account interrupt requests coming from various devices. If it is 0, the requests will not be taken into account.

2.1.5.8 Direction Bit The value of this flag is generally used to indicate the direction of the operation in string operations.

2.1.5.9 Overflow Bit It is used to check for overflow in signed numbers. As you will recall, the carry flag was used for unsigned numbers. But the situation is somewhat different for signed numbers. Since an overflow occurring in signed numbers will affect the sign bit of the byte or word, it is possible for a signed number that is positive (sign bit 0) to be perceived as negative (sign bit 1) as a result of the overflow. In this case the overflow flag is set and misinterpretation of the result is prevented.

2.2 Memory and Its Structure When we run a program on our computer, the program is first loaded into RAM and then executed. Loading is done by loading the program's sections such as code and data separately into various memory areas. These areas are called segments. In the 8086 processor, each of these segments is 64 Kb (65535 bytes) long. This value is about 4 Gb in 32-bit processors. Since we are working with the 8086 processor and memory regions 16 bits long, the maximum area we can address is 64 Kb. The 8086 processor provides the programmer with four segments to work on. These are: the CODE, DATA, EXTRA and STACK segments. The starting addresses of these segments are stored in CS for the CODE SEGMENT, in DS for the DATA SEGMENT, in ES for the EXTRA SEGMENT and in SS for the STACK SEGMENT. The 64 Kb segments described above are themselves divided into 1-byte sections. These 1-byte sections within the segments are called OFFSETs. That is, there are 65535 offsets in a segment. Each instruction entered by the programmer advances the offset address by the number of bytes it occupies. The SEGMENT:OFFSET pair is used to reach any point in memory.

```asm
To reach a point within the code segment, the value in CS is used as the segment address and
```

the value in IP is used as the offset address. Likewise, to reach a value within the stack segment, the value in SS is used as the segment address and either SP or BP is used as the offset address. The following example will help you with how memory and data are stored.

### -A100

```
1E40:0100 MOV AH,01
1E40:0102 INT 21
1E40:0104 CMP AL,45
1E40:0106 JNE 0100
1E40:0108 INT 20
1E40:010A
-G
```

### GGHJRE

Program terminated normally

```
-U 100
1E40:0100 B401          MOV     AH,01
1E40:0102 CD21          INT     21
1E40:0104 3C45          CMP     AL,45
1E40:0106 75F8          JNZ     0100
1E40:0108 CD20          INT     20
1E40:010A D3E8          SHR     AX,CL
1E40:010C 94            XCHG    SP,AX
1E40:010D 00726D        ADD     [BP+SI+6D],DH
```

```
1E40:0110 E87000               CALL      0183
1E40:0113 A396D3               MOV       [D396],AX
1E40:0116 8A04                 MOV       AL,[SI]
1E40:0118 3C20                 CMP       AL,20
1E40:011A 740C                 JZ        0128
1E40:011C 3400                 XOR       AL,00
1E40:011E 2F                   DAS
1E40:011F 1E                   PUSH      DS
```

-

The short program above reads every key entered from the keyboard and continues reading until 'E' is entered. (By the way, notice that the program is only 10 bytes long. I wonder how many KB the same program would take in C or Pascal!! ☺ ). First we wrote the program and then ran it with "G". Finally, we did an unassemble operation starting from offset address 100 with "U 100". If you pay attention, at the beginning of each line there are two numbers separated by a colon, like "1E40:0104". These numbers are, in order, the segment and offset addresses of the instruction. That is, segment 1E40 of our computer is our current code segment at that moment, and offset

### 0104 in this segment (actually offsets 0104 and 0105) contains the instruction "CMP AL,45".

On the next line these numbers become "1E40:0106", which shows us that our offset address has increased by 2. That is, the "CMP AL,45" instruction occupies 2 bytes in our computer's memory. The numbers to the right of the segment and offset addresses in the unassemble operation are the hexadecimal equivalents of the instructions you entered as they exist in memory. In fact, the computer stores information in its memory as numbers, and assembly language is the more human-readable form of these numbers. That is, when the CPU encounters "3C45" (0011 1100 0100 0101 = 16 bits) it understands that this is a comparison instruction and acts accordingly. Other instructions are treated in the same way. Whether the information at hand is an instruction or a variable is understood by means of the segment in which the information is located.

2.3 Stack In high-level programming languages, values are stored in areas called variables. In assembly language, on the other hand, the programmer uses the CPU registers and the stack to store values. The stack is a section where information is stored temporarily. The 8086 processor provides the programmer with a 64 Kb stack segment. The starting address of this segment is in SS and the current offset address at that moment is in SP (Stack Pointer). Values such as the return addresses of functions in the program, the arguments passed to functions, and command-line parameters are stored in the stack. In addition, the programmer can temporarily store some values in this area and use them later. Placement within the stack is done in words. That is, in one operation on the stack, two offsets are moved backward or forward each time. The stack provides the programmer with sequential access. Assuming the offset addresses of our stack segment range from 0000 to FFFF and the current value of SP is FFFF, the first value to be put on the stack is written to addresses FFFF and FFFE (two bytes of data can be written and read). Then the value of SP is changed to FFFD to indicate the address of the next value to be written.

Above, the initial value of the stack pointer is FFFF (Figure 1). After the first transfer of information onto the stack, SP=FFFD to indicate the address where the next information will be written (Figure 2). The numbers 89 and 67 have been written to addresses FFFF and FFFE respectively. This shows us that the information written onto the stack is 6789h. In the same way, the value 1234h is then transferred onto the stack (Figure 3) and the value of SP changes to FFFB. In Figure 4, information is taken from the stack. Contrary to the first two operations, this time the value of SP increases by 2 and FFFB+2=FFFD. That is, the first value to be written from then on will be written to addresses FFFD and FFFC. In short, when information is written onto the stack the value of SP decreases, and when information is read it increases. The stack works on the LIFO (Last-In First-Out) principle. That is, the last information written onto the stack is the first information that can be retrieved, and the first information written is the last that can be retrieved. In the example above, first the number 6789h and then the number 1234h were written onto the stack. To reach 6789h, the first value written, 1234h must be read first. Operations on the stack are carried out with the PUSH and POP instructions.

```asm
MOV instruction: In the next section, "Memory Addressing in 80x86 Processors", information
```

transfer between memory and CPU registers will be explained using the MOV instruction.

```asm
MOV destination,source
The usage form of the MOV instruction is as above. This instruction transfers the information in "source" to "destination". That is,
```

```asm
MOV AX, 1234h
MOV BX, AX
```

Above, first the value 1234h was written to the AX register. Then this value was transferred from the AX register to the BX register. That is, at the end of the program AX=1234h and BX=1234h. The most important point to watch for in using the instruction is that the "destination" and "source" fields are of equal size (16 bits in our example).

2.4 Memory Addressing in 80x86 Processors The 8086 processor provides the programmer with 17 kinds of addressing methods for accessing memory. In the assembly programming language, memory addressing and memory access are among the most important subjects and ones that must be well known.

- Displacement-only

- Base

- Displacement + Base

- Base + Indexed

- Displacement + Base + Indexed

The 17 kinds of addressing methods used are derived from the five main categories above.

2.4.1 Direct Addressing This addressing method is the easiest to understand. By this means, a read or write is performed to any memory cell whose address is given. Since the memory we use consists of 16-bit addresses, our address constants must also consist of four-digit hexadecimal numbers.

```asm
MOV AX, [4126]
MOV CX, CS:[4A4C]
MOV DS:[41C8], BX
```

In the first line above, with "MOV AX, [4126]" the values at memory addresses 4126h and 4127h are assigned to the AX register. Since address 4126h is 1 byte and the AX register is 2 bytes, the values at both address 4126h and address 4127h are read. In the second example, the values at addresses 4A4Ch and 4A4Dh within the Code Segment are assigned to the CX register. As you can see, by using an expression such as "CS:[4A4C]" you can reach information in any segment you want. Finally, with the "MOV DS:[41C8], BX" instruction the value in BX is written to addresses 41C8h and 41C9h within the Data Segment.

2.4.2 Indirect Addressing With this method, the operation is performed on the memory location pointed to by the value held in a register. The four registers that can be used for this method are BX (Base), BP (Base Pointer), SI (Source Index) and DI (Destination Index). I have given a few examples of addressing in this way below.

Based

```asm
MOV BX, 1234                    First the value of BX is changed to 1234h.
MOV AX, [BX]                   Then the value at the location in memory pointed to by
```

1234 is assigned to AX. That is, the instruction set at the side

```asm
MOV AX, [1234]
```

does the same job.

Based

```asm
MOV BP, 45C8                     BP = 45C8h
MOV AX, [BP]                     MOV AX, [45C8]
```

Indexed

```asm
MOV DI, 76A7                       DI = 76A7h
MOV AX, [DI]                       MOV AX, [76A7]
```

Indexed

```asm
MOV SI, D78C                       SI = D78Ch
MOV AX, [SI]                      MOV AX, [D78C]
```

In the first two addressing methods, since the Base registers BX and BP are used, this method is called Based. Likewise, in addressing done with DI and SI, since the Index registers are used, it is called Indexed. As in the previous section, in this method too a separate segment can be specified for the offset to be reached. Above, BX, DI and SI use DS (Data Segment) by default. The default segment for BP is SS (the Stack Segment).

2.4.3 Indexed Addressing With this method, both a constant and a register as above are used to reach the desired place. The desired offset address is the sum of the constant used and the value in the register. Again, as above, BX, DI and SI use DS by default and BP uses SS by default as the segment. Of course, it is possible to reach data in different segments if desired.

```asm
MOV BX, 7A82                    BX = 7A82
MOV AL, 78[BX]                  7A82 + 78 = 7AFA
MOV AL, [7AFA]
```

As you can see, with the "MOV AL, 78[BX]" instruction above, the value in offset 7AFAh, which is the sum of the value 7A82h in BX and our constant 78h, is assigned to AL. Of course, since BX is used, the Data Segment is used as the source segment.

2.4.4 Based Indexed Addressing This method resembles the indirect addressing method. The only difference is that here two different registers are used rather than one, one a Base and the other an Index register. The value to be assigned to the destination region is the value in the offset indicated by the sum of the values in these two registers.

```asm
MOV BX, D854                    BX = 7A82
MOV SI, 278C                    SI = 278C
MOV AL, [BX][SI]                D854 + 278C = FFE0
MOV AL, [FFE0]
```

```asm
MOV BP, 54AC                  BP = 54AC
MOV DI, 4444                  DI = 4444
MOV AL, [BP][DI]              54AC + 4444 = 98F0
MOV AL, [98F0]
```

In the first example above the default segment is the Data Segment, and in the second it is the Stack Segment.

2.4.5 Based Indexed + Constant (Disp) Addressing This method covers all the methods above. Its general form is as below, and the operation is performed on the value at the offset address given by the sum of the values in the registers and the constant.

```asm
MOV AL, DISP[BX][SI]
MOV BL, DISP [BX+DI]
MOV BH, [BP+SI+DISP]
MOV AH, [BP][DI][DISP]
```

Chapter 3: The 80x86 Instruction Set In this chapter we will examine some of the assembly instructions used to program Intel's 80x86 series processors.

- Transfer instructions

```asm
MOV
XCHG
LEA
PUSH
PUSHF
POP
POPF
LAHF
SAHF
```

- Input/Output instructions

```asm
IN
OUT
```

- Arithmetic Instructions

```asm
ADD
ADC
SUB
SBB
MUL
IMUL
DIV
```

### IDIV

```asm
INC
DEC
CMP
```

- Logical Instructions

```asm
AND
OR
XOR
NOT
TEST
```

- Shift and Rotate Instructions

```asm
SAL/SHL
SHR
SAR
RCL
ROL
RCR
ROR
```

- Branch Instructions

```asm
JMP
JZ/JE
JNZ/JNE
JB/JC/JNAE
JBE/JNA
JNB/JNC/JAE
JG/JNLE
JA/JNBE
JL/JNGE
JLE/JNG
JS and JNS
JO and JNO
JCXZ
```

- Loop Instructions

```asm
LOOP
LOOPZ/LOOPE
LOOPNZ/LOOPNE
```

3.1 Transfer Instructions The instructions in this group are used to transfer any information between register-register, memory-register and register-memory locations.

3.1.1 MOV Instruction

```asm
The MOV instruction was touched on briefly earlier in the memory addressing section. In this part
```

more detailed information about the use of the instruction will be given. The various forms of use of the mov instruction are as follows.

General Form: mov destination, source

```asm
mov register, register
mov memory, register
mov register, memory
mov memory, constant value
mov register, constant value
```

The various ways of using the mov instruction are shown above. Note that among the forms of use there is no memory-to-memory transfer. The "register" expressions above represent both general-purpose registers and segment registers. However, a constant value absolutely cannot be loaded directly into a segment register. Such an operation is carried out in two steps as below.

```asm
mov ax, 1234
mov cs, ax
```

In the example above, the value 1234h was assigned to CS. Another important point to note is that the values to be transferred must be of the same size. That is, a 16-bit value cannot be assigned to AH. Likewise, a transfer cannot be made from an 8-bit register to a 16-bit register. When any memory region is addressed with indirect addressing and a constant value is to be assigned into it, the length of the value to be assigned must be specified.

```asm
mov [bx], 12            Error!
```

```asm
mov byte ptr [bx], 12
or
mov word ptr [bx], 1234
```

With the "byte ptr" and "word ptr" prefixes, the processor is informed about the size of the information to be transferred.

```asm
NOTE: In 32-bit processors ( 80386 and later ), 32-bit information transfer can be
done with the "dword ptr" prefix.
```

```asm
The MOV instruction makes no change to the flag register.
```

3.1.2 XCHG Instruction

```asm
The XCHG (exchange) instruction is used to swap two values with each other. Of course, again
```

the values to be swapped must be the same size. Its general form is as below.

```asm
xchg register, register
xchg memory, register
```

```asm
In the use of the xchg instruction the positions of the operands do not matter. That is, "xchg memory,
```

register" and "xchg register, memory" do the same job.

```asm
mov ax,1234           AX=1234h
mov bx, 5678          BX=5678h
xchg ax,bx            AX=5678h BX=1234h
```

```asm
The XCHG instruction makes no change to the flag register.
```

3.1.3 LEA Instruction

```asm
Although the use of the LEA instruction resembles the MOV instruction, in some cases
```

it gives the programmer the ability to do with a single instruction an operation that would take two or three instructions. Its general form is as below.

```asm
lea register, memory
```

Giving a few examples of the use of the instruction will make the conveniences it provides to the programmer easier to understand.

```asm
lea ax, [bx]       mov ax, [bx]
lea bx, 3[bx]      BX = BX+3
```

The uses above are cases that could be carried out with a single instruction other than "lea". (Since the assembly equivalent of the expression BX = BX+3 has not yet been explained, an ordinary notation was used) If the examples below are examined, the convenience the instruction provides will be clearly noticed.

```asm
lea ax, 3[bx]          BX = BX+3      mov ax, bx
lea ax, 8[bx+di]
```

```asm
The general purpose of using the LEA instruction is to store a memory address in a register.
```

While the instruction is used it has no effect on the flag registers.

3.1.4 PUSH Instruction

```asm
The PUSH instruction is used to save any information into the section of the computer called the stack.
```

The information to be put on the stack with the PUSH instruction must be 16 bits long. The general form of the instruction is as below.

```asm
PUSH value
```

The part shown as "value" above must, as stated earlier, be 16 bits long. In addition, the part shown as "value" cannot take a constant value. That is, the value to be written onto the stack with PUSH must be either the value in a register or the value in a memory region.

```asm
Because information is written onto the stack with the PUSH instruction, the value of SP changes. Each
```

PUSH instruction executed will decrease the value of SP by 2 (since 2 bytes of information are transferred with PUSH). An example of transferring information onto the stack with the PUSH instruction is given below.

```asm
mov ax,1234          AX = 1234h
push ax              AX > STACK , SP = SP-2
```

Writing information onto the stack is used together with pointers for temporarily saving the necessary values and, in some UNIX systems, for passing the parameters required in using interrupts.

3.1.5 PUSHF Instruction Similarly to the PUSH instruction, the PUSHF instruction transfers information onto the stack. The only difference here is that the information to be transferred with PUSHF is taken not from any register or memory region but from the flag register. The use of the instruction is as follows.

### PUSHF

As can be seen, no register or memory address is used while using the instruction. Instead, the information to be put on the stack is directly the value in the 16-bit flag register. The instruction is used to preserve the current value of the flag register during any operation. Just as with the PUSH instruction, the PUSHF instruction will also decrease the value of SP by 2.

3.1.6 POP Instruction

```asm
The POP instruction reads information from the stack. That is, the information written onto the stack with the PUSH instruction
```

is read back with the POP instruction. The information read must be 16 bits long.

```asm
The information taken with the POP instruction is the last information written onto the stack. When transferring information with the PUSH and POP instructions,
```

the order of the information written and read is important. Making calculation errors in operations on the stack while writing programs is a common occurrence. The general use of the instruction is as below.

```asm
POP destination_field
```

Above, the destination field can be a memory region or a register.

```asm
mov ax,1234         AX = 1234h
push ax             AX > STACK , SP = SP-2
mov ah,01           AH = 01 ,the value of AX changed!
pop ax              AX = 1234h
```

In our example, first a value is assigned to AX and then, by changing the value of AH, the value of AX is indirectly changed as well. In the last operation, with the POP instruction the old value of AX, previously put onto the stack with PUSH, is retrieved.

3.1.7 POPF Instruction

```asm
If POP is paired with PUSH, it would not be wrong to pair the POPF instruction with the PUSHF instruction.
```

With the POPF instruction, 16 bits of information from the stack are written to the flag register. Not all 16 bits taken are taken into account by the processor. The values the bits represent for the processor, according to their order within the word, are given below.

### bit 0    Carry bit

### bit 2    Parity bit

### bit 4    Auxiliary bit

### bit 6    Zero bit

### bit 7    Sign bit

### bit 8    Trap bit

### bit 9    Interrupt bit

### bit 10    Direction bit

### bit 11    Overflow bit

As will be understood, the POPF instruction completely changes the value of the flag register. The instruction is used on its own, just like the PUSHF instruction.

```asm
To fully grasp how the PUSH, PUSHF, POP and POPF instructions operate on the stack,
```

I recommend that you reread the "Stack" section in the earlier parts of the text.

3.1.8 LAHF Instruction The LAHF (Load AH from Flags) instruction copies the low-order byte of the flag register into the AH register. The bits copied are the sign, zero, auxiliary, parity and carry bits. The overflow, direction, interrupt and trace bits outside these have nothing to do with the instruction. The use of the instruction is as follows.

lahf

As can be seen, the instruction is used on its own. No change occurs in the flag register during the execution of the instruction.

3.1.9 SAHF Instruction The SAHF (Store AH into Flags) instruction, like the LAHF instruction, operates on the flag register. The value in AH is copied into the low-order byte of the flag register. Again the bits

affected by the operation are the sign, zero, auxiliary, parity and carry bits. The use of the instruction is on its own, as with the LAHF instruction.

3.2 Input/Output Instructions In 80x86 series processors, the "in" and "out" instructions are used to reach the input and output units. In fact, in a way these instructions work similarly to the MOV instruction. The only difference is that these instructions work specifically with the memory region reserved for the computer's I/O unit.

3.2.1 IN Instruction

```asm
in ax/al, port
in ax/al, dx
```

```asm
The general use of the IN instruction is shown above. With the IN instruction, the information read from the port address specified by "port" or dx
```

is copied into AX or AL according to its size. If the port to be accessed is between 0-255, the port number is used. Otherwise, that is, if the port to be accessed is between 256 and 65535, the maximum port number supported by the 80x86 processor, the desired port number is loaded into DX and then access is made with the IN instruction. The flag register undergoes no change during execution of the instruction.

3.2.2 OUT Instruction

```asm
out port, ax/al
out dx, ax/al
```

```asm
The use of the OUT instruction resembles the IN instruction. The only difference is that in the IN instruction
```

the information in the port is assigned to AX/AL, whereas in the OUT instruction the information in AX/AL is sent to the port. Again, as in the IN instruction, for addresses between 0-255 the port number is entered directly, while for addresses between 256-65535 addressing is done with DX. The flag register undergoes no change during execution of the instruction.

```asm
mov al, 2e       AL = 2Eh
out 70, al       70h. The value 2E is sent to the port
in al,71         In response to the request sent, 71h.
```

the response comes from the port. The incoming value is taken into AL.

Above, information is sent to CMOS port 70h with the OUT instruction. The CMOS responds to the incoming signal from port 71h, and we save the response received into AL with the IN instruction.

3.3 Arithmetic Instructions In addition to the basic arithmetic operations such as addition, subtraction, multiplication and division, the 80x86 gives the programmer the ability to store the results obtained in various forms. The flag register changes during the execution of arithmetic instructions.

3.3.1 ADD Instruction

```asm
The ADD instruction is used to perform addition. Its general form is as below.
```

```asm
add destination, source
```

```asm
With the ADD instruction, the value in "source" is added to "destination" and
```

saved into "destination". The "destination" and "source" fields can be one of the register-register, memory-register, register-memory pairs.

```asm
mov ax, 1234                      AX = 1234h
mov word ptr [4444], 1000         [4444] = 1000h
add word ptr ax, [4444]           AX = AX + [4444]
```

= 1234h + 1000h = 2234h

In the example above, first the value 1234h was assigned to AX. Then the word-length value 1000h was written to the memory cell with address 4444h (two memory cells were used for this operation). Finally, the value in AX was added to the word pointed to by memory cell 4444h and the result was again assigned to AX.

3.3.2 ADC Instruction The ADC instruction is also used for addition, just like the ADD instruction. The only difference is that in the ADC instruction the value of the carry flag is also added in the addition. Its general form is as below.

adc destination, source

To show the operation performed arithmetically, the following notation would not be wrong.

destination = destination + source + value of the carry flag

With the ADC instruction, in consecutive addition operations it is ensured that the carry is not ignored.

3.3.3 SUB Instruction

```asm
The SUB instruction is used for subtraction. Its use is as in the ADD instruction.
```

```asm
sub destination, source
```

The value in "source" is subtracted from "destination" and the result is stored in "destination". The arithmetic representation of the operation is

destination = destination – source

In fact, with the SUB instruction the CPU adds "destination" and "-source". What is actually done is again an addition.

```asm
mov ax, 8da7          AX = 8DA7h
mov bx, 4a43          BX = 4A43h
sub ax, bx            AX = AX – BX
```

= 8DA7h – 4A43h = 4364h

3.3.4 SBB Instruction

sbb destination, source

The relationship between the SBB and SUB instructions is the same as the relationship between the ADD and ADC instructions.

```asm
The same job is done as with the SUB instruction, except that here the value of the carry flag is also subtracted from the value placed in the "destination" field.
```

The arithmetic representation of the operation is

destination = destination – source – value of the carry flag

3.3.5 MUL Instruction

```asm
The MUL instruction is the instruction used to perform multiplication. Although multiplication is arithmetically
```

performed with two values, the MUL instruction takes only one value.

```asm
The value used with the MUL instruction is implicitly multiplied by the value in ax/al.
```

```asm
mov ax,0045        AX = 0045h
mov bx,11ac        BX = 11ACh
mul bx             AX = AX * BX
```

= 0045h * 11Ach = C35Ch

Above, the number 0045h, one of the elements of the multiplication, was loaded into AX. In the next step, after the other number to be used in the operation, 11ACh, is loaded into BX, with the "mul bx" instruction the number in BX is directly multiplied by AL (AH=00) and the product obtained is stored in AX.

```asm
mov ax, 0005                   AX = 0005h
mov word ptr [4000], 1212      [4000] = 12 , [4001] = 12
mul word ptr [4000]            AX = AX*[4001][4000]
```

Above, the second number to be used in the multiplication is read from a memory region. Notice that in my operations I inform the processor about the length of the value I am assigning with "word ptr". When using the MUL instruction, if the number you will operate on is in a memory region, you must inform the processor about the length of the information to be operated on with helper information such as "word ptr" and "byte ptr". Suppose the result you find at the end of the multiplication does not fit in a 16-bit area. In such a case the result found is stored in the DX:AX pair.

```asm
mov ax, 4321             AX = 4321h
mov cx, 4586             CX = 4586h
mul cx                    AX * CX = 4321h * 4586h
```

= 123B0846h (32-bit) = DX = 123Bh , AX = 0846h

3.3.6 IMUL Instruction The IMUL instruction, like the MUL instruction, is used for multiplication; the only difference is that the IMUL instruction is used for operations on signed numbers. As a result of an operation performed with the IMUL instruction, if AH (if the result fits in AX) or DX (if the result does not fit in AX) is nonzero, the result of the multiplication is negative. If an overflow has occurred as a result of the operation and AH or DX contains a value belonging to the result itself rather than the sign of the result, the carry and overflow flags will have been set.

3.3.7 DIV Instruction It is an instruction used for division. The DIV instruction, as with the MUL instruction, takes only one value and implicitly uses the AX register. Its general form is as below.

```asm
div divisor_value
```

In a division operation, the length of the "divisor_value" also determines the length of the dividend to be used in the operation. For instance, if the "divisor_value" is an 8-bit value, the 16-bit AX register will be taken as the dividend. At the end of the operation the quotient is copied into AL and the remainder into AH. Likewise, if the "divisor_value" is a 16-bit value, the DX:AX pair is taken as the dividend. Again at the end of the operation the quotient is placed in AX and the remainder in DX. To divide an 8-bit number by an 8-bit number and a 16-bit number by a 16-bit number, the value 0 is assigned to the AH and DX registers respectively. If a memory region is used as the "divisor_value", the processor must be informed about the length of the value used.

```asm
mov ax, 4a2c
div byte ptr [2155]
```

```asm
One thing to watch out for when using the DIV instruction is not running into a division by zero situation
```

and whether the quotient fits in the destination field. For instance, an error will be encountered at the end of an operation like the one below.

```asm
mov ax, aaaa
div 4
```

The operation above will be erroneous because the number 2AAAh, the result of the operation ( AAAAh / 4H = 2AAAH 16-bit ), will not fit in AL, which is an 8-bit register.

3.3.8 IDIV Instruction The IDIV instruction is used for division like the DIV instruction. Its difference from the DIV instruction is that the IDIV instruction is used for operations on signed numbers. Besides what was described above for the DIV instruction, a point to watch for in using the IDIV instruction is preserving the sign bit of the number while zeroing the AH or DX values. For example, if the divisor to be used is an 8-bit negative number and the dividend is an 8-bit number, the sign bit 1 of the 8-bit negative number in AL must be assigned to all bits of AH.

3.3.9 INC Instruction

```asm
The INC instruction increases the value in the register or memory region given to it by one. It does the same job as the "++" operator
```

in C. Below, I tried to show the use of the instruction as in C.

```asm
mov ax, 000f                  variable = 15 ;
inc ax                        variable++ ;
```

It has the same effect on the flag register as the ADD instruction, except for the carry flag.

```asm
add ax,1
inc ax
```

Both instructions above do the same job. However, the operation performed with the INC instruction is carried out faster by the processor and occupies one third as much space in memory as the first. For these reasons, the "inc ax" instruction is used instead of uses such as "add ax,1".

```asm
inc byte ptr [125a]
inc word ptr [7ad8]
inc byte ptr [bx+di]
```

If the value in a memory region is to be processed with the INC instruction, the length of the information to be operated on must be specified to the processor.

3.3.10 DEC Instruction

```asm
The DEC instruction decreases the value in the register or memory region given to it by one.
```

Again, as with the INC instruction, I would like to give an example from C.

```asm
mov ax, 000f                  variable = 15 ;
dec ax                         variable-- ;
```

As seen above, the DEC instruction corresponds to the "--" operator in C.

```asm
A decrement performed with the DEC instruction could also have been carried out with the "sub ax,1" instruction but
the DEC instruction occupies less space in memory than the SUB instruction and runs faster.
```

```asm
dec word ptr a8[bx+di]
```

```asm
If the value to be decremented with the DEC instruction is in a memory region, the length of the value must be communicated to the processor with "word ptr" or
```

"byte ptr".

3.3.11 CMP Instruction

```asm
The CMP instruction works like the SUB instruction.
```

```asm
cmp value1, value2
```

Above, register-register, register-memory region, memory region-register and register-constant value can be used in place of "value1" and "value2" respectively.

```asm
In short, the CMP instruction subtracts "value2" from "value1". But unlike the SUB instruction,
```

the result is not saved anywhere. Instead, branching in the program is done according to the values of the flag register bits that change as a result of the operation. After the CMP instruction, the flow of the program is generally changed with conditional branch instructions according to the result.

```asm
cmp ax, bx
```

### In short, the instruction has the following effects on the flag register 

- If AX is equal to BX, the result of the operation is zero and the zero flag takes the value 1.

- If the value of AX is smaller than that of BX, the carry flag takes the value 1 at the end of the subtraction.

- If the result is negative, the sign bit takes the value 1; if positive, 0.

3.4 Logical Instructions These instructions are used to perform logical comparisons during any operation. Before examining the instructions in this chapter, it is worthwhile to review the "Logical Operations on Bits" section of the document. While these instructions are executed, the values in the register or memory region used are processed as separate bits.

3.4.1 AND Instruction

```asm
and destination, source
```

In the use of the instruction, one of the pairs register-register, memory region-register, register-memory region, register-constant value and constant value-register can be used in the "destination" and "source" fields. During the operation, the values in the "destination" and "source" regions are subjected to a logical AND operation and the result of the operation is saved to the "destination" field.

```asm
mov ah, a5      AH = A5h = 1010 0101 (binary)
mov al, c1      AL = C1h = 1100 0001 (binary)
and ah, al           AND_________________
```

1000 0001 (binary) = 81h

Above, the values A5h and C1h were assigned to AH and AL, and then the two values were subjected to a "logical AND" operation with the "and ah, al" instruction. The value 81h was obtained as a result of the operation. The value obtained was placed in the AH register.

3.4.2 TEST Instruction

```asm
The TEST instruction works entirely like the AND instruction. The only difference is that the result obtained is not
```

transferred to the destination field; instead, the flow of the program is controlled according to the flag bits that change.

3.4.3 OR Instruction

```asm
or destination, source
```

```asm
The OR instruction is used to perform the "logical OR" operation. The values that can be used in place of the "destination" and "source"
```

fields are the same as for the AND instruction. After the operation is carried out, the result obtained is saved into the destination field.

3.4.4 XOR Instruction

```asm
xor destination, source
```

The values that can be used for the "destination" and "source" fields are the same as for the AND instruction. The value obtained as a result of the operation is saved into the destination field.

```asm
The XOR instruction is frequently used to set the value of any register to zero. The "xor ax, ax"
```

instruction runs faster than the "mov ax, 0" instruction and occupies less space in memory.

3.4.5 NOT Instruction

```asm
not destination
```

```asm
The NOT instruction is, unlike the other logical instructions, the only one that does not affect the flag register.
```

It also differs from the other instructions in its form of use. The bits of the value in the "destination" field are inverted and written back to the same field.

3.5 Shift and Rotate Instructions In this section, carrying out, with assembly instructions, the operations in the previously described section titled "Shift and Rotate Operations" will be explained.

3.5.1 SHL/SAL Instructions

```asm
The SHL (Shift Left) and SAL (Shift Arithmetic Left) instructions are equivalent.
```

```asm
shl destination, count
```

Both instructions shift the bit positions in the "destination" field to the left "count" times. During the shift operation, zero is written to bit position 0 and the value in bit position 7 or 15 is written into the carry flag.

3.5.2 SHR Instruction

```asm
The use of the SHR (Shift Right) instruction is as follows.
```

```asm
shr destination, count
```

```asm
With the SHR instruction, the bit arrangement in the "destination" region is shifted to the right "count" times. In the right
```

shift operation, the value 0 is assigned to the vacated bit position 7 or 15, and the value in bit position 0 is written to the carry flag. The sign bit takes the value of the high-order bit of the result, which is always zero. Arithmetically, subjecting any unsigned number to the operation "SHR number, a" is the same thing as dividing the number by 2^a.

3.5.3 SAR Instruction

```asm
sar destination, count
```

```asm
The SAR (Shift Arithmetic Right) instruction, as with the SHR instruction, shifts the bit arrangement in the "destination" field
```

to the right "count" times. Its difference from the SHR instruction is that the vacated bit position 7 or 15 is filled not with zero but with the value already in bit position 7 or 15. Its effect on the flags, unlike SHR, is that the value in bit position 7 or 15 is written into the sign flag.

3.5.4 RCL Instruction

```asm
rcl destination, count
```

```asm
The RCL (Rotate through Carry Left) instruction puts the bit arrangement in the destination field into a left rotate
```

movement. After the operation, the value in the carry flag is written to bit position 0 and the leftover bit is transferred into the carry flag.

3.5.5 ROL Instruction

```asm
rol destination, count
```

```asm
The ROL (Rotate Left) instruction, like the RCL instruction, is used for the left rotate operation. Its only
```

difference is that the vacated bit position 0 is filled not with the value of the carry flag but with the value of the highest-order bit. In this operation too, the high-order bit value is copied into the carry flag.

3.5.6 RCR Instruction

```asm
rcr destination, count
```

```asm
The RCR (Rotate through Carry Right) instruction works exactly like the RCL instruction.
```

As its name suggests, its only difference is that the rotate operation is done to the right, not the left. Again, the value in the low-order bit position is copied into the carry flag and the value in the carry flag into the high-order bit position.

3.5.7 ROR Instruction

```asm
ror destination, count
```

```asm
We can relate the ROR instruction to the RCR instruction in the same way we related the ROL instruction to the RCL instruction.
```

That is, the ROR instruction also works like the RCR instruction. The only difference is that the value assigned to the high-order bit position by the ROR instruction is not the one in the carry flag but the one in the low-order bit position.

```asm
NOTE: The "count" expression used in the instructions that perform the "shift" and "rotate" operations above
```

is normally used as 1. In 80286 and later processors, the use of any constant value has been introduced. In earlier processors, to use a value other than 1 the following method must be followed.

```asm
mov cl, count
shr ax, count
```

As above, the desired value is assigned to CL and then it is operated with the destination field.

3.6 Branch Instructions Branch instructions are used to redirect the normally top-to-bottom flow of the program to somewhere else, either depending on some condition or unconditionally. These branch instructions can be thought of as the "if" or "goto" statements in high-level languages. The branch instructions used in assembly language have the FAR or NEAR property according to where they jump. Instructions with the NEAR property occupy 2-3 bytes, while those with the FAR property occupy 5 bytes. The difference between the instructions is that those with the FAR property are used for branching to points in a different segment. Although not required, the type of branch can be specified with "FAR PTR" or "NEAR PTR".

3.6.1 JMP (Unconditional Jump) Instruction

```asm
jmp target
```

```asm
The JMP instruction is used to branch unconditionally to any specified point.
```

In programs written using DEBUG, the offset address of the point to be gone to is written in the "target" part. If a branch is made to an address in a different segment, an addressing of the form SEGMENT:OFFSET is used in the "target" part. If a branch is made within the same segment to a point farther than –128 or +127 bytes, this branch also has the FAR property. Its space occupied in memory will be 3 bytes. In fact, all the JMP instruction does is add the value "address_to_go_to - current_address" to the IP value. The value to be added to IP during the execution of the JMP instruction is calculated starting from the address of the instruction following the JMP instruction. When branching, instead of directly writing the address to go to, the operation can also be carried out by way of memory addressing.

```asm
mov bx, 0401
mov si, 0002
mov word ptr [bx+si+04], 1a8c
jmp far ptr [bx+si+04]
```

In the example above, the point to be gone to with the JMP instruction is not the value BX+SI+04 = 0407h but the place indicated by the value within offset number 0407h in the same segment. In our example this value is 1A8Ch. Similarly, branching can also be carried out using any general-purpose 16-bit register.

```asm
mov ax, 1111
jmp ax
```

Above, after the "JMP AX" instruction the flow of the program will continue from offset address 1111h.

To branch into another segment, the SEGMENT:OFFSET pattern is used. That is, to branch to address 4C70:0100, the instruction "JMP 4C70:0100" must be used. The instruction will occupy 5 bytes in memory.

Apart from the JMP instruction discussed above, there are also conditional branch instructions used in assembly language. These instructions affect the flow of the program according to the values of the flag registers as a result of any operation. These instructions can be paired with "if" in C and the "if...then" construct in Pascal. The comparison operation can be any arithmetic operation, or a comparison (CMP) or a rotate. But conditional branch instructions are mostly used after the CMP instruction for comparison purposes.

3.6.2 JZ/JE Instructions

```asm
The JZ/JE (Jump if Zero/Jump if Equal) instructions arrange the flow of the program according to the value of the zero flag after any operation.
```

During execution of the instruction, if the bit value in the zero flag is 1 the program jumps to the place indicated by the JZ instruction; otherwise the processor continues the flow of the program as if the JZ instruction did not exist.

```asm
dec cx
cmp cx,0
jz 010a
jmp 0110
```

In the example above, the value in CX is decreased by one. Then the value obtained is compared with zero, and if the result is zero a jump is made to address 010Ah. If the result is different from zero, the program continues its normal flow and the next instruction, "JMP 0110", is executed. This time an unconditional branch is made to address 0110h. The notation in our example is the notation used inside DEBUG. For programmers who assemble assembly programs through an assembler program, the notation is somewhat different. Programmers who use an assembler use labels that they place at various points in the program instead of offset addresses.

```asm
.model small
.code
org 0100h
basla:
mov dl,41h
mov ah,02h
int 21h
dongu: inc dl
int 21h
cmp dl,5Ah
jnz dongu
```

```asm
mov ah,4Ch
```

```asm
int 21h
end basla
```

Above is seen an assembly program written with MASM. At this stage do not try to understand the program; just pay attention to the label used within the program. The line where the "INC DL" instruction is located is marked with the "dongu" label. With the "JNZ dongu" instruction, no offset address is specified, and the jump to the desired point is made with the help of a label. Above, the value in DL is increased starting from 41h until it reaches 5Ah. In practice, DEBUG is not a suitable environment for writing programs. You assemble the assembly program you write with some assembler software and use it. If the program above is compiled as a COM file it occupies 19 bytes and writes the uppercase letters of the alphabet to the screen.

3.6.3 JNZ/JNE Instructions

```asm
The JNZ/JNE (Jump if Not Zero/Jump if Not Equal) instructions are used as the opposite of the JZ and JE instructions.
```

After any operation, if the value in the zero flag is not zero, the program continues its flow by branching to the place indicated by the instruction. As an example, the MASM program given for JZ can be examined. With the "jnz dongu" instruction the value in the zero flag is checked. If the value is different from zero, the place marked with "dongu" is gone to and the loop is executed again. Finally, when the value in DL reaches 5Ah, the flow of the program passes to the next instruction, the "mov ah, 4ch" line. I have given below the C program that does the same job as the program above. While the size of the COM file written in assembly is 19 bytes, that of the one written in C is 8378 bytes!

#include <stdio.h>

```asm
int main()
```

{

```asm
int ch=65; /* hex 41 */
```

### dongu

if (ch!=90) /* hex 5A */ { printf("%c",ch); ch++;

```asm
goto dongu;
```

}

```asm
return 0;
```

}

In the C example, the operations performed with "cmp" and "jnz" in the first program are carried out with the "if" and "goto" statements.

3.6.4 JB/JC/JNAE Instructions

```asm
The JB/JC/JNAE (Jump if Below/Jump if Carry/Jump if Not Above or Equal) instructions branch according to the value of the carry
```

flag. If there is a 1 in the carry flag after any operation, the flow of the program goes to the place indicated by the JB instruction. Otherwise, the JB instruction is disregarded and the normal flow of the program continues.

3.6.5 JBE/JNA Instructions

```asm
During the execution of the JBE/JNA (Jump if Below or Equal/Jump if Not Above) instructions, the carry and
```

zero flags are checked. If one of the two flags is 1 after an operation, a branch is made to the point indicated by the JBE instruction.

3.6.6 JNB/JNC/JAE Instructions

```asm
When one of the JNB/JNC/JAE (Jump if Not Below/Jump if Not Carry/Jump if Above or Equal)
```

instructions is encountered, the CPU checks the value of the carry flag. If the value in the carry flag is zero, a branch is made to the point indicated by the JNB instruction.

3.6.7 JG/JNLE Instructions

```asm
The condition required for the JG/JNLE (Jump if Greater than/Jump if Not Less than or Equal) instructions to take effect
```

is that the values of the sign and overflow flags are equal and that zero is in the zero flag. If the required conditions are met, a branch will be made to the point indicated by the JG instruction and the flow of the program will continue from that point.

3.6.8 JA/JNBE Instructions

```asm
During the execution of the JA/JNBE (Jump if Above/Jump if Not Below or Equal) instructions, the flags taken into
```

account are the carry and zero flags. If, after any operation, the values of both of these flag bits are zero, the flow of the program continues from the place indicated by the JA instruction. If one of the two flag bits is not zero, the program will continue its normal flow.

3.6.9 JL/JNGE Instructions

```asm
The condition required for the JL/JNGE (Jump if Less than/Jump if Not Greater or Equal) instructions to take effect
```

is that the carry and overflow flag bits carry different values from each other. If the two bits contain different values, the flow of the program is directed to the point indicated by the JL instruction.

3.6.10 JLE/JNG Instructions

```asm
During the execution of the JLE/JNG (Jump if Less than or Equal/Jump if Greater) instructions, the values of the zero,
```

sign and overflow flags are taken into account. To branch to the place indicated by the instruction, there must be a 1 in the zero flag or the values of the sign and overflow flags must be different. If the required condition is met, the flow of the program will be shifted to the point indicated by the JLE instruction.

3.6.11 JS and JNS Instructions

```asm
During the execution of the JS (Jump if Sign) and JNS (Jump if No Sign) instructions, the sign flag is checked.
```

The value in the sign flag being 1 is the required condition for JS, and it being zero is the required condition for JNS.

If the required condition is met, the program will continue its flow from the point indicated by the JS or JNS instruction.

3.6.12 JO and JNO Instructions

```asm
During the execution of the JO (Jump if Overflow) and JNO (Jump if No Overflow) instructions, the value in the overflow
```

flag is looked at. A 1 in the overflow flag is the required condition for the JO instruction and a zero for the JNO instruction.

3.6.13 JCXZ Instruction

```asm
The JCXZ (Jump if CX is Zero) instruction checks the value of the CX register. If the value in CX
```

is zero, the program continues its flow from the place indicated by the JCXZ instruction.

With the conditional branch instructions given above, only a jump of +128/-128 bytes can be made. If a branch to a farther distance is needed within the program, the following method must be followed.

- A branch to the desired point is made with the JMP instruction

- A label is given to the point after the JMP instruction

- The opposite of the instruction to be used is written in front of the JMP instruction, branching to the label after the JMP instruction

For example, while at offset 0100 in DEBUG you cannot give the "JE 184" instruction. What you need to do to execute this instruction is to give, in order,

???? : 0100 jne 105 ???? : 0102 jmp 184 ???? : 0105

these instructions. If examined carefully, it will be seen that the instruction set above does the same thing as the "JE 184" instruction.

3.7 Loop Instructions The instructions in this category are used to repeat any routine a certain number of times. The loop instructions used in assembly language can in a way be paired with the "for" and "while" loops in C.

3.7.1 LOOP Instruction This instruction is used to repeat any situation a certain number of times. The value in the CX register is taken as the counter. In each iteration the value in CX is decreased by one and the operation continues until the value of CX becomes zero. The general usage pattern of the instruction is as below.

```asm
loop target
```

The value specified by "target" must be an offset address for DEBUG, and a label for a program to be assembled using some assembler. The maximum jump that can be made with the LOOP instruction is +128/-128 bytes. Since, by the nature of the instruction's use, the point to be jumped to is one of the addresses before the LOOP instruction, the maximum address we can go to is at a distance of –128 bytes.

```
1E27:0100 XOR AX, AX
1E27:0102 MOV CX,0005
1E27:0105 INC AX
1E27:0106 LOOP 0105
```

At the end of the program above, the value of AX will be 5. The value 5 loaded into CX at the start of the program determines the number of iterations to be carried out with LOOP.

```
1E27:0100 XOR AX, AX
1E27:0102 MOV CX,0005
1E27:0105 INC AX
1E27:0106 DEC CX
1E27:0107 JNZ 0105
```

The program above performs the same operation as the program in the previous example. The only difference is that the "INC CX" and "JNZ 0105" instructions are used in place of the "LOOP 0105" instruction. In fact, what is done with LOOP is nothing other than the work of these two instructions.

3.7.2 LOOPZ/LOOPE Instructions

```asm
The LOOPZ/LOOPE instructions are also used to repeat any situation a certain number of times.
```

The use of the instruction is the same as the LOOP instruction. The only difference is that during execution the LOOPZ instruction checks the zero flag in addition to the value of the CX register. As long as the value of CX is different from zero and the value in the zero flag is 1, a branch is made to the place indicated by the instruction. If either of the two conditions fails to hold, the loop is exited.

3.7.3 LOOPNZ/LOOPNE Instructions

```asm
The LOOPNZ/LOOPNE instructions, like the LOOP instruction, accept the CX register as the counter
```

and are used to repeat a condition a certain number of times. The loop continues while the value of CX is different from zero and the value in the zero flag is not 1.

Chapter 4: Using Interrupts Normally the processor executes the instructions in the code segment in order. In some cases, in order to work with the computer's peripheral devices, to use certain routines in RAM or the BIOS, or when some invalid results arise, routines called interrupts are executed by the processor. What I will briefly touch on here are the interrupts that arise from programs calling subroutines defined in RAM or the BIOS. These subroutines do many jobs in the programmer's place. It would not be wrong to pair these subroutines with the ready-made library functions in high-level languages. Every interrupt that can be used has a predefined number. The interrupt is used by passing this number as a parameter to the "INT" instruction and assigning the necessary values to the required registers. As an example, INT 21, which is used very frequently under DOS, can be given. Let us use function number AH = 01 of INT 21, a DOS interrupt.

For the operation, the value of the AH register must be 01h and then the interrupt must be called with the "INT 21" instruction. When the interrupt is called with the INT 21 instruction, the value in AH is looked at. The subroutine to be executed is loaded into memory according to the value in AH.

```
C:\WINDOWS\Desktop>debug
-a 100
1E27:0100 mov ah,01
1E27:0102 int 21
1E27:0104 cmp al,41
1E27:0106 jnz 100
1E27:0108 mov ah,4c
1E27:010A int 21
1E27:010C
-g
```

ssdfaA

```
C:\WINDOWS\Desktop>
```

After assigning the value 01h to AH, the program above loads the required instructions into memory with the INT 21 instruction. The program reads the keys entered from the keyboard, and the ASCII code of each key value read is written into AL (by virtue of INT 21 AH=01h). With the CMP instruction we make the program keep running until the value of the key read is 41h (A). Then we encounter a new INT 21 subroutine. The AH = 4Ch subroutine exits the program being run and returns control to the DOS operating system. Likewise, in UNIX and similar operating systems, subroutines called system calls are loaded into memory with INT 80 and executed. In this document the functions of the interrupts will not be dealt with one by one. The most detailed source that can be obtained on the subject is the document called "Ralf Brown's Interrupt List". Besides the documents, a helper program called "RBILViewer" will also let you view the long interrupt lists in an orderly way.

Chapter 5: The DEBUG Program DEBUG is a piece of software used under MS-DOS that gives the user the ability to modify executable files in memory and save them. Today there are much more functional and advanced programs on the market that do the same job, but the fact that DEBUG comes with MS-DOS removes the difficulty of obtaining the program. In this chapter I have covered some of the commands used within the DEBUG program with examples. To start the DEBUG program, it is enough to give the "debug" command in MS-DOS mode. After giving the command you encounter a screen like the one below.

Microsoft(R) Windows 98 (C)Copyright Microsoft Corp 1981-1999.

```
C:\WINDOWS\Desktop>debug
```

-

The screen above is the screen you will encounter when you first run the debug program. When the program runs, only a dash appears at the left edge of the screen. At this stage debug is waiting for a command for the next operation. In the table below I have given the most used commands together with their explanations.

A – Assemble      Writing a program starting from a given address G – Go            Running the program in memory L – Load          Loading into memory N – Name          Name of the program to be loaded or written Q – Quit          Exiting DEBUG R – Register      Assigning a register value T – Trace         Step-by-step execution U – Unassemble    Unassembling the loaded program W - Write         Writing from memory to disk ? - Help          List of the commands that can be used

Above I have given only the commands we will use together with their explanations. Now, if you like, let us run debug in MS-DOS mode, write a program and save the program to disk.

```
C:\WINDOWS\Desktop>debug
-A 100
1E27:0100 mov ah,02
1E27:0102 mov dh,07
1E27:0104 mov dl,0c
1E27:0106 int 10
1E27:0108 mov ah,4c
1E27:010A int 21
1E27:010C
```

-N set_curs.com

```
-R CX
```

### CX 0000

### 000C

### -W

0000C bytes being written -

With the program above, the cursor is moved to the point specified by DH and DL. First, the "A" command was used to write the program inside debug. The 100 parameter used with the "A" command indicates the offset address at which the program will start being written. Since the program we will write is a COM file, we set the starting offset as 0100. On the next line we started writing our assembly program. After the writing part of the program was finished, we determined, with the "N" command, the file name to be used when saving the information in memory to disk. With the "R" command, we assign to the value in the CX register the length of our program in bytes (in our example 010C – 0100 = 000C ). Finally, with the "W" command the instructions in memory are saved to disk under the file name "set_curs.com". Now let us unassemble the program we wrote with the help of DEBUG again.

```
C:\WINDOWS\Desktop>debug
```

-N set_curs.com

### -L

```
-U
1E4A:0100 B402          MOV            AH,02
1E4A:0102 B607          MOV            DH,07
1E4A:0104 B20C          MOV            DL,0C
1E4A:0106 CD10          INT            10
1E4A:0108 B44C          MOV            AH,4C
1E4A:010A CD21          INT            21
1E4A:010C D6            DB             D6
1E4A:010D C70619DFAD82 MOV             WORD PTR [DF19],82AD
1E4A:0113 E8C901        CALL           02DF
1E4A:0116 0BC0          OR             AX,AX
1E4A:0118 7478          JZ             0192
1E4A:011A 8BE8          MOV            BP,AX
1E4A:011C BF02D2        MOV            DI,D202
1E4A:011F 8B36C6DB      MOV            SI,[DBC6]
```

### -Q

```
C:\WINDOWS\Desktop>
```

Above, again the DEBUG program is run by giving the "debug" command from the command line. This time the "N" command is used to give not the name of the file to be written to disk but the name of the file to be transferred from disk into memory. Then the file whose name was given is loaded into memory with the "L" command. The program loaded into memory is unassembled with the "U" command. If you examine the code carefully, you will see that the first six lines of the program consist of the assembly code we wrote in the previous example. The numbers to the left of the code are the form in which the assembly instructions exist in memory (machine language). The assembly instructions on lines 010C and after are code that happens to be in memory at that moment

```asm
at random. They have nothing to do with our program. Finally,
```

DEBUG is exited with the "Q" command. Any program in memory can be executed step by step with the "T" command. A simple example of the use of the command is given below.

Microsoft(R) Windows 98 (C)Copyright Microsoft Corp 1981-1999.

```
C:\WINDOWS\Desktop>debug
-A 100
1E2C:0100 mov ax,1234
1E2C:0103 mov bx,4567
1E2C:0106 mov ax,bx
1E2C:0108
-T = 100
```

```
AX=1234 BX=0000       CX=0000 DX=0000 SP=FFEE          BP=0000 SI=0000 DI=0000
DS=1E2C ES=1E2C       SS=1E2C CS=1E2C IP=0103           NV UP EI PL NZ NA PO NC
1E2C:0103 BB6745            MOV    BX,4567
-T
```

```
AX=1234 BX=4567       CX=0000 DX=0000 SP=FFEE          BP=0000 SI=0000 DI=0000
DS=1E2C ES=1E2C       SS=1E2C CS=1E2C IP=0106           NV UP EI PL NZ NA PO NC
1E2C:0106 89D8              MOV    AX,BX
```

```
-T
```

```
AX=4567 BX=4567        CX=0000 DX=0000 SP=FFEE           BP=0000 SI=0000 DI=0000
DS=1E2C ES=1E2C        SS=1E2C CS=1E2C IP=0108            NV UP EI PL NZ NA PO NC
1E2C:0108 107420             ADC    [SI+20],DH                               DS:0020=FF
```

-

As you can see, the program written with DEBUG is executed step by step. You can use the "T" command for error checking of the short pieces of code you write.

Chapter 6: Using Assembly under the Linux Operating System This document will not give information about the use of Linux and the workings of the system. In this chapter it is assumed that the user has previously used Linux or a similar UNIX-derived system. The oldest CPU model on which the Linux operating system can run is the 80386 architecture. That is, Linux cannot be installed on a computer using an 8086, 80186 or 80286. The biggest innovation Intel brought with the 80386 is that it made it possible to use 32-bit registers in place of the 16-bit registers used in the older models (8086, 80186 or 80286). This gives the programmer more addressable memory space. While in models before the 80386 a segment was 64KB in size, this figure is more than 4GB in the 80386 and later. (At the time I was writing this document, Intel was working on new processors with 64-bit capacity!) In the 80386, additions were made to the previously used registers and some new registers were added. In place of the AX, BX, CX, DX, SI, DI, BP and SP registers, each 16 bits, the EAX, EBX, ECX, EDX, ESI, EDI, EBP and ESP registers, each 32 bits, are used respectively. In addition to the 16-bit segment registers CS, DS, ES and SS used in earlier processors, two 16-bit segment registers, FS and GS, were added. The 80386 uses 16-bit segment registers like the earlier models. In addition to all this, the flag register also gained 32-bit capacity. Bit 16 of the extended new flag register is called the "debug resume" (RF) bit and

### bit 17 the "virtual mode" (VM) bit. While the processor is running under virtual mode

it operates with the 8086 architecture. In addition to these, in the 80486 the "alignment check flag" bit was added at bit position 18. When writing 32-bit programs, 16-bit and 8-bit registers can be used. The register scheme used by the 80386 is as below.

All the programs we write under Linux can use the 32-bit capacity registers provided by the 80386. Using assembly language under Linux does not give the programmer as great advantages as under DOS. Since the programs run run under protected mode, the programmer's access to the resources provided by the BIOS is restricted. (Actually this is true of all systems that run in protected mode) Assembly routines to be used under Linux are mostly used inline within languages such as C. The fact that the programs written do not show as large a size difference as between two programs written under DOS in a high-level language and in assembly, and the restrictions in use due to protected mode, have reduced the popularity of the language under Linux (or any UNIX-derived system). But still, at some points there is no other alternative and the use of assembly language becomes mandatory. (The boot files in the Linux Kernel Ver1.0 source, http://www.kernel.org) Assembly files saved under Linux take the .s or .S extension. The program is written using the AT&T or Intel syntax depending on the assembler program used. If NASM (Netwide Assembler), which is used under Linux and DOS, is to be used as the assembler, the program is written using the Intel syntax. The assembly language rules described so far in the document are for the Intel syntax. In contrast, the AT&T syntax is always used in code written with GDB, one of the debugger programs frequently used under Linux, in inline code to be used with C, and in the code in the Linux kernel. In fact, GCC uses an assembler program named "as" during compilation. Since "as" uses the AT&T syntax, the code in C files compiled with GCC must of necessity also be written with the AT&T syntax. In this document the differences between the Intel and AT&T syntaxes will mainly be dwelt on, and some examples of the use of the GNU Assembler will be given.

6.1 Intel and AT&T Syntaxes As I stated above, the syntax used when writing assembly programs under Linux is in accordance with AT&T standards. While the assembler programs used under DOS assemble code written in the Intel syntax, those used under Linux (and UNIX-derived systems) require the AT&T syntax, with one or two exceptions.

Intel                            AT&T

```asm
mov eax, 01h                      movl $0x01, %eax
mov bx,1234h                      movw $0x1234, %bx
```

As can be seen above, the AT&T syntax is somewhat more complicated than Intel's. Now, if you like, let us examine the differences in order.

6.1.1 Source-Destination Direction While in the Intel syntax the general form is "instruction destination, source", in AT&T this ordering is "instruction source, destination". In fact, what looks natural to the eye is the value moving from left to right.

Intel                            AT&T

instruction destination, source     instruction source, destination

```asm
mov ebp ,esp                      movl %esp, %ebp
```

6.1.2 Prefixes In the AT&T syntax, registers take the "%" prefix and constant values take the "$" sign. If the number used as a constant value is written in hexadecimal, an expression like "0xnumber" is used.

Intel                            AT&T

```asm
mov ah, 12h                       movb $0x12, %ah
```

In the example above, the value 12h (18 in decimal) was assigned to AH. Note that in the AT&T syntax the constant value has the "$" sign at its beginning and that we used the notation 0x12 to represent the value 12h. There is a big difference between "movb $0x12, %ah" and "movb $12, %ah". The equivalent of the second instruction in GDB will be "movb $0xC, %ah".

6.1.3 Suffixes Another difference between the syntaxes is the "l", "w" and "b" suffixes placed at the end of instructions in the AT&T syntax. These suffixes are used to give information about the size of the information being operated on. They correspond to the "dword ptr", "word ptr" and "byte ptr" qualifiers used in the Intel syntax. The suffix "l" (long) is used for 32-bit data operations, "w" (word) for 16-bit data operations, and "b" (byte) for 8-bit data operations.

Intel                            AT&T

```asm
mov byte ptr bh, 45h              movb $0x45, %bh
mov eax, dword ptr [ebx]          movl (%ebx), %eax
```

6.1.4 Memory Operations Besides the new registers, the biggest innovation the 80386 provides programmers is in memory addressing methods. You need to have knowledge about memory addressing in the 8086 series before reading this section. While in the 8086 series only the BX register is used when doing indirect addressing, in the 80386 and later processors any general-purpose register (EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP) can be used. That is, the notation below does not work on a processor before the 80386, while on the 80386 and later it works without problems.

```asm
mov al, [edx]
```

Another point to note is that if you run your program in 16-bit real mode on an 80386 processor, the memory region you can address is still 64KB in size and you must use 32-bit registers during access. The 80386 lets you use any register for base or index addressing. The only restriction is that you cannot use ESP as an index value. In addition, in the 80386 the "index" value can be multiplied by one of the constants 1, 2, 4 or 8, providing more efficient memory access. The general Intel and AT&T syntax forms are given below.

INTEL instruction destination, segment_register:[base + index * n + displacement] AT&T instruction %segment_register:displacement(base, index, n ), destination ( n = 1, 2, 4 or 8 )

I think the examples below will clear up any question marks the formulas above may have created in your mind.

Intel                              AT&T

```asm
mov eax, [ecx*8h]                   movl 0x08(%ecx), %eax
mov edx, [ebx+ecx*08h-05h]          movl –0x05(%ebx,%ecx,0x08)
```

At this point, compared to Intel's, the AT&T syntax really is not programmer-friendly at all! In code written for the 80386, when memory addressing is done, the first of the registers used is assumed to be the "base" and the second the "index". The programmer must be careful here. Because the processor determines the segment from which it will take the information according to the "base" register used. Only when ESP or EBP is used as the base is the current segment the Stack Segment. In other cases the Data Segment is used by default.

6.1.5 INT 0x80 and Linux System Calls (Syscalls) Among the routines used a lot when writing assembly programs under Linux are system calls. To use any system call, the number of the system call is loaded into EAX, and if the system call takes at most five arguments, the required arguments are loaded in order into the EBX, ECX, EDX, ESI and EDI registers. For

system calls taking six or more arguments, again the system call number is loaded into EAX. Then the required arguments are pushed onto the stack from last to first and ESP is copied into EBX. System calls are listed in /usr/include/asm/unistd.h. You can also get information about system calls with the command "man 2 system_call_name".

### Examples 

ilk.s

fnoyan@tux:~$ cd asm fnoyan@tux:~/asm$ vi ilk.s

Write the following code into the file "ilk.s".

.text .globl _start

### _start

```asm
movl $12,%eax
movl $0x12, %eax
```

xorl %eax, %eax

```asm
inc %eax
int $0x80
```

fnoyan@tux:~/asm$ as ilk.s –o ilk.obj fnoyan@tux:~/asm$ ld ilk.obj –o ilk fnoyan@tux:~/asm$ ./ilk fnoyan@tux:~/asm$ fnoyan@tux:~/asm$ gdb -q (gdb) file ilk Reading symbols from ilk...(no debugging symbols found)...done. (gdb) disas _start

### Dump of assembler code for function _start

0x8048074 <_start>:     mov    $0xc,%eax 0x8048079 <_start+5>:   mov    $0x12,%eax 0x804807e <_start+10>: xor     %eax,%eax 0x8048080 <_start+12>: inc     %eax 0x8048081 <_start+13>: int     $0x80

```asm
End of assembler dump.
```

(gdb)

Above, the step-by-step assembling of the ilk.s file and the examination of the assembly code inside it with the help of GDB are shown. In our example, the "file" command used with GDB does the same job as the "n" command in debug, and the "disas" command does the same job as the "u" command in debug. In this example you can easily see the difference between the "movl $12,%eax" and "movl $0x12, %eax" instructions I gave above. With the "disas _start" command, GDB unassembles starting from the "_start" point in our program.

iki.s

This example illustrates the use of "chmod", which is a system call. After learning the system call number (15 for chmod) from the /usr/include/asm/unistd.h file, you can learn the required arguments by reading the Linux help files.

fnoyan@tux:~$ man 2 chmod

After learning the required arguments, save the following code as iki.s.

```asm
.data
```

path: .ascii "./dosya" .text .globl _start

### _start

```asm
movl $15, %eax
movl $path, %ebx
```

xorl %ecx, %ecx

```asm
int $0x80
```

xorl %eax, %eax

```asm
incl %eax
int $0x80
```

The program above clears the access permissions of the file named "dosya" in the directory it is in. That is, our program does the same job as the "chmod 000 ./dosya" command.

fnoyan@tux:~/asm$ touch dosya; chmod 777 dosya fnoyan@tux:~/asm$ ls –l dosya fnoyan@tux:~/asm$ as iki.s –o iki.obj fnoyan@tux:~/asm$ ld iki.obj –o iki fnoyan@tux:~/asm$ ./iki fnoyan@tux:~/asm$ ls –l dosya .... .... fnoyan@tux:~/asm$ gdb -q (gdb) file iki Reading symbols from iki...(no debugging symbols found)...done.

(gdb) disas _start

### Dump of assembler code for function _start

0x8048074 <_start>:     mov    $0xf,%eax 0x8048079 <_start+5>:   mov    $0x8049088,%ebx 0x804807e <_start+10>: xor     %ecx,%ecx 0x8048080 <_start+12>: int     $0x80 0x8048082 <_start+14>: xor     %eax,%eax 0x8048084 <_start+16>: inc     %eax 0x8048085 <_start+17>: int     $0x80

```asm
End of assembler dump.
```

(gdb)

We created a file named "dosya" and set its access permissions to –rwxrwxrwx (777). Then, with the program we wrote, we changed the access permissions of the file named "dosya" to ----------(000). According to "man 2 chmod", the function takes two arguments. The first is the path to the file and the second is the new access permissions (zero in our example). If you like, let us examine the program step by step.

```asm
.data
```

path: .ascii "./dosya"

In the piece above, an ascii-type constant is defined within the program. ".data" indicates that we are in the Data Segment.

.text .globl _start

### _start

```asm
We switch to the Code Segment.
```

```asm
movl $15, %eax
movl $path, %ebx
```

xorl %ecx, %ecx

```asm
int $0x80
```

Here the chmod system call is made. After the system call number is loaded into EAX, the required arguments are loaded into the registers. Here, with the "movl $path, %ebx" instruction, what is done is loading the address of our constant into EBX (this is seen in the GDB output of the program.). Then zero is assigned to ECX and finally "int $0x80" is executed.

xorl %eax, %eax

```asm
incl %eax
int $0x80
```

At the end of our program, the _exit() system call (system call number

### 1) is used to end the program. This does the same job as the AH=4Ch INT 21h call under DOS.

uc.s

In our last example, we change the name of the file named "dosya" created above to "yeni_dosya". For this job we again used a system call: rename (system call number 38). Our code is as below.

```asm
.data
```

old_path:     .ascii "./dosya\0" new_path:     .ascii "./dosya_yeni\0" .text .globl _start

### _start

```asm
movl $38, %eax
movl $old_path, %ebx
```

xorl $new_path, %ecx

```asm
int $0x80
```

xorl %eax, %eax

```asm
incl %eax
int $0x80
```

Above, a system call was again used, as in the previous example. This time, in addition to the system call number, two arguments were needed, and the first was written into EBX and the second into ECX. The "old_path" constant specified by the "movl $old_path, %ebx" instruction is replaced with the required offset address during assembly. The GDB output below will help you understand this more easily.

fnoyan@tux:~/asm$ gdb -q (gdb) file uc Reading symbols from uc...(no debugging symbols found)...done. (gdb) disas _start

### Dump of assembler code for function _start

0x8048074 <_start>:     mov    $0x26,%eax 0x8048079 <_start+5>:   mov    $0x804908c,%ebx 0x804807e <_start+10>: xor     $0x8049094,%ecx 0x8048084 <_start+16>: int     $0x80 0x8048086 <_start+18>: xor     %eax,%eax

0x8048088 <_start+20>:       inc       %eax 0x8048089 <_start+21>:       int       $0x80

```asm
End of assembler dump.
```

Note that in the code displayed with GDB the instructions have no suffixes.

### Internet Addresses 

In this final part of the document there are the addresses of some websites for those who want to work with assembly on a broader scale.

http://linuxassembly.org                     A site where you can find resources on assembly language and its use under Linux and other UNIX-based systems.

http://www.janw.easynet.be/eng.html          Another article describing the use of assembly language under Linux.

http://www.geocities.com/SiliconValley       An address where you can find information on the use of inline assembly with GCC under Linux. /Ridge/2544/                               

ftp://www6.software.ibm.com/software/       Another document on inline assembly with GCC. developer/library/l-ia.pdf                 

http://members.lycos.co.uk/kasiasyg/         A site that has Turkish translations of some of the documents whose addresses are given above.

http://www.programmersheaven.com             A site with wide-ranging content where you can find sample code and resources not only on assembly but on many other programming languages.

http://www.web-sites.co.uk/nasm/            The site of NASM, an assembler used under Linux and MS-Windows operating systems.

http://win32asm.cjb.net                      One of the best sites where you can learn 32-bit assembly programming under the Windows operating system.

Besides the above, some useful resources whose addresses I do not know but which you can easily reach by typing the necessary information into a search engine.

The Art Of Assembly Language

PC Assembly Language                              Author: Paul.A Carter

Ralf Brown's Interrupt List                       Author: Ralf Brown



*Note: Since the document was written in July 2003, the first day of the month was used for archive ordering; the exact day is not specified.*
