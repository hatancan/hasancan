---
baslik: EEM332 Microprocessors: DEBUG Notes and Source Compilation (Fran Golden and Course Archive)
ozet: Examining registers and memory with DEBUG, tracing instructions step by step, and the x86 instruction table.
---

This post brings together the related notes and exercises from the Başkent University **EEM332 Microprocessors** course archive (2002–2010). Examining registers and memory with DEBUG, tracing instructions step by step, and the x86 instruction table. Source: Course compilation; the Introduction to DEBUG document credits Fran Golden and the original educational sources. PDF archive copies of the documents and, where available, their source code can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request from the rights holder.*

## Debug Commands

Debug Commands: To see experimentally how Assembly instructions work, to understand whether the programs we write behave as intended, and to correct any errors, DOS's DEBUG.COM program is used. Although there are more advanced, user-friendly debuggers, DEBUG is preferred because it is easy to find and convenient for simple applications. To use the DEBUG program, one must know its commands. Here we will try to explain some of the DEBUG commands with the help of simple examples.

```
C:\>DEBUG
```

-

The dash sign indicates that the debug program is now ready to accept commands.

- R (Register): This command is used to determine the current register values and the state of the flags.

```
-R
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 8B24   MOV   SP,[SI]           DS:0000=20CD
```

-

With this command, the desired values (provided they are hexadecimal) can be assigned to registers.

```
-R AX
```

### AX 0000

### 

If we type the value we want for the AX register after the ':' sign and press Enter;

### 12AF

```
-R
AX=12AF BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 8B24   MOV   SP,[SI]           DS:0000=20CD
```

- We set the value of the AX register to 12AF.

The values NV UP EI PL NZ NA PO NC that follow the registers indicate the state of the flags.

```
-R F
```

### NV UP EI PL NZ AC PO CY -

With this command, only the state of the flags can be viewed and changed as needed. If a flag value is not to be changed, you can press the space bar to move on to the next flag value.

Flag Name                          Set(1)                      Clear (0) Overflow - OF                  OV (overflow)              NV (not overflow) Direction - DF              DN (decrement - down)         UP (increment - up) Interrupt - IF                   EI (enable)                 DI (disable) Sign - SF                       NG (negative)                  PL (plus) Zero - ZF                         ZR (zero)                  NZ (not zero) Auxilary Carry- AF           AC (auxilary carry)           NA (not auxilary) Parity - PF                   PE (even parity)              PO (odd parity) Carry - CF                     CY (carry yes)               NC (not carry) Table 18-1 Flag abbreviations used in the debugger

- D (Dump / Display): With this command we can view the contents of any segment of memory starting from any offset. We can also limit the area we want to view.

```
-D DS:0
2AF2:0000 CD 20 FF 9F 00 9A EE FE-1D F0 4F 03 5A 25 8A 03 . ........O.Z%..
2AF2:0010 5A 25 17 03 5A 25 14 24-01 01 01 00 02 FF FF FF Z%..Z%.$........
2AF2:0020 FF FF FF FF FF FF FF FF-FF FF FF FF 3B 25 4E 01 ............;%N.
2AF2:0030 16 2A 14 00 18 00 F2 2A-FF FF FF FF 00 00 CE 0B .*.....*........
2AF2:0040 06 1E 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
2AF2:0050 CD 21 CB 00 00 00 00 00-00 00 00 00 00 20 20 20 .!...........
2AF2:0060 20 20 20 20 20 20 20 20-00 00 00 00 00 20 20 20             .....
2AF2:0070 20 20 20 20 20 20 20 20-00 00 00 00 00 00 00 00             ........
```

-

Here the portion of the Data segment starting from offset 0000H is shown. If no range is given, it displays 128 bytes. After giving the memory dump in hexadecimal, the corresponding displayable ASCII characters are shown alongside.

```
-D DS:100,115
2AF2:0100 8B 24 17 5A 18 BA 4A 29-A2 4F F6 C9 07 AE 07 09 .$.Z..J).O......
2AF2:0110 20 8C 07 BA 4F 80                    ...O.
```

-

As can be seen, if the address of the range to be displayed is given next to the D command, only the values within the specified address range are displayed on the screen.

- A (Assembly): This command allows simple programs to be written with the help of Debug. Programs written inside Debug start at offset address 100H, as in COM programs. For this reason, when the program is to be run, the value of the IP register must be set to 100H with the R command.

```
-A
2AF2:0100 MOV AX,5
2AF2:0103 ADD AX,4
2AF2:0106 SHR AX,1
2AF2:0108 ^C
```

- After the A command is given, you can write an assembly program starting from address 100H of CS. All numbers given here must be in hexadecimal form. When you finish entering instructions, you can end the process by pressing Ctrl-C.

- T (Trace): This runs the written assembly instructions one by one and displays the values taken by the registers and flags at the end of each operation. The T command starts running from the point IP indicates and stops after each instruction is executed.

```
-R
AX=12AF BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 B80500  MOV   AX,0005
```

```
-T
```

```
AX=0005 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0103 NV UP EI PL NZ NA PO NC
2AF2:0103 050400  ADD   AX,0004
-T
```

```
AX=0009 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0106 NV UP EI PL NZ NA PE NC
2AF2:0106 D1E8   SHR   AX,1
-T
```

```
AX=0004 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0108 NV UP EI PL NZ AC PO CY
2AF2:0108 A24FF6  MOV   [F64F],AL           DS:F64F=11
```

-

As seen in this example, we have run the assembly code we just wrote. This is a command designed so that we can easily follow the changes in the registers and flags after each operation.

If the user wishes, a number can also be given next to the T command. In this case, that many instruction lines are executed back to back, and the register and flag values are printed to the screen each time. Example:

### -T5

Or the user can also specify how many instructions to execute starting from an offset (address) of their choice. Example:

```
-T=200,5
```

This command means execute 5 instructions back to back starting from offset 200H.

- U (Unassemble): This is a command used to convert the machine code written in CS into mnemonics in a form the user can understand. Each time it is invoked, it shows the user the mnemonics of 32 bytes of machine code.

```
-U CS:112
2AF2:0112 07      POP   ES
2AF2:0113 BA4F80    MOV    DX,804F
2AF2:0116 FC      CLD
2AF2:0117 807463BA    XOR   BYTE PTR [SI+63],BA
2AF2:011B C6418208    MOV   BYTE PTR [BX+DI-7E],08
2AF2:011F 83745BBA    XOR   WORD PTR [SI+5B],-46
2AF2:0123 D208     ROR    BYTE PTR [BX+SI],CL
2AF2:0125 847453    TEST DH,[SI+53]
2AF2:0128 BADE04    MOV    DX,04DE
2AF2:012B 0908     OR    [BX+SI],CX
2AF2:012D 85744B    TEST SI,[SI+4B]
2AF2:0130 BAEA08    MOV    DX,08EA
```

-

With this command, 32 bytes of machine code starting from address CS:112 are unassembled and their mnemonic equivalents are shown.

If desired, the starting address and the number of bytes to be unassembled can also be given as parameters.

```
-U CS:100L8
```

This command will unassemble 8 bytes starting from address CS:100H.

- E (Edit): This is a command used to change the values at any location in memory.

-

```
-E DS:10
2AF2:0010 5A.
```

The command waits for the user to enter a hexadecimal value to change the value of the byte at address DS:10H. If the value is not to be changed, you can move on to the next byte with the space bar and change its value. To finish this process, press ENTER.

- F (Fill): This is used to fill a memory area whose start and end addresses are specified with a specified number.

-

```
-F DS:100,120,AB
```

Using the F command, the portion of DS between 100H and 120H will be filled with the value ABH. If we then examine from address DS:100H with the D command, we verify that the operation was carried out as intended.

```
-D DS:100
2AF2:0100 AB AB AB AB AB AB AB AB-AB AB AB AB AB AB AB AB ................
2AF2:0110 AB AB AB AB AB AB AB AB-AB AB AB AB AB AB AB AB ................
2AF2:0120 AB 5B BA D2 08 84 74 53-BA DE 04 09 08 85 74 4B .[....tS......tK
2AF2:0130 BA EA 08 86 74 43 12 28-BA F6 08 87 74 3B BA 02 ....tC.(....t;..
2AF2:0140 50 08 90 20 88 74 33 BA-0E 08 89 74 2B BA 1A 41 P.. .t3....t+..A
2AF2:0150 82 08 8A 74 23 BA 26 08-8B 74 1B BA 32 54 24 08 ...t#.&..t..2T$.
2AF2:0160 8D A2 BA 3E 08 8E 48 00-74 0B BA 86 08 FF 74 03 ...>..H.t.....t.
2AF2:0170 BA 4A 50 E9 1D A0 C0 C9-BA 56 50 E8 17 75 E8 AB .JP......VP..u..
```

-

- C (Compare): This is a command used to compare the contents of specified ranges.

### -C 100,110,10

```
2AF2:0100 AB 5A 2AF2:0010
2AF2:0101 AB 25 2AF2:0011
2AF2:0102 AB 17 2AF2:0012
2AF2:0103 AB 03 2AF2:0013
2AF2:0104 AB 5A 2AF2:0014
2AF2:0105 AB 25 2AF2:0015
2AF2:0106 AB 14 2AF2:0016
2AF2:0107 AB 24 2AF2:0017
2AF2:0108 AB 01 2AF2:0018
2AF2:0109 AB 01 2AF2:0019
2AF2:010A AB 01 2AF2:001A
2AF2:010B AB 00 2AF2:001B
2AF2:010C AB 02 2AF2:001C
2AF2:010D AB FF 2AF2:001D
2AF2:010E AB FF 2AF2:001E
2AF2:010F AB FF 2AF2:001F
2AF2:0110 AB FF 2AF2:0020
```

This command compares the contents at addresses 100H-110H with the contents starting at address 10H and lists those that differ.

### -C 100,110,100

-

This compares the contents at 100H-110H with the contents at 100H again. Since no difference is found, nothing appears on the screen.

### -C DS:100,110,CS:300

```
2AF2:0100 AB 25 2AF2:0300
2AF2:0101 AB 44 2AF2:0301
2AF2:0102 AB 68 2AF2:0302
2AF2:0103 AB 20 2AF2:0303
2AF2:0104 AB DD 2AF2:0304
2AF2:0105 AB 20 2AF2:0305
2AF2:0106 AB 91 2AF2:0306
2AF2:0107 AB CF 2AF2:0307
2AF2:0108 AB 3A 2AF2:0308
2AF2:0109 AB 1C 2AF2:0309
2AF2:010A AB 04 2AF2:030A
2AF2:010B AB 1C 2AF2:030B
2AF2:010C AB 6B 2AF2:030C
2AF2:010D AB 82 2AF2:030D
2AF2:010E AB 04 2AF2:030E
2AF2:010F AB 1C 2AF2:030F
2AF2:0110 AB 04 2AF2:0310
```

As can be seen, contents in different segments can also be compared.

```
-G (Go): Programın verilen bir adrese kadar ya da bitene kadar çalışmasını sağlamak amacıyla kullanılır.
```

Hmm — the line above is inside a code block and must stay as in the source except for translating Turkish text; here it is:

```
-G (Go): Used to run the program up to a given address or until it finishes.
```

```
-G
```

Program terminated normally

If the program ran correctly, the above message will appear on the screen. If there is an error in the program's return addresses or a logic error in the program, the program never terminates. In this case, the machine will need to be reset.

- H (Hex): Used to calculate the hexadecimal sum and difference of two given numbers.

### -H2E,3

### 0031 002B

-

The first value shown is the sum of the two hexadecimal numbers, and the other is their difference.

- L (Load): Used to load the program into memory again.

- M (Move): Used to move a block of data from one place to another.

### - M DS:100,110,CS:500

With this command, the data between DS:100H and DS:110H will be placed starting from address CS:500H.

- P (Proceed): This command has features similar to the T command. After executing instructions, it displays the register and flag values on the screen. However, its biggest difference from the T command is in the handling of instructions such as LOOP, CALL, and INT. If any of these instructions is executed with the P command, it produces the result without going into the details of that operation. (If it is a LOOP, it shows the state of the registers and flags once the loop completes; if it is a CALL, once the operations are carried out and control returns; or if it is an INT, once all the operations the interrupt handler must perform have been done.)

- Q (Quit): A command used to exit the debugger.

### -Q

```
C:\>
```

## calisma-685

### 8086 REGISTERS and SEGMENTS

The microprocessor contains 14 special locations called registers. We can think of these locations, each 16 bits wide, as special memory units. Registers are used by the microprocessor for special purposes. They are also used to temporarily store various data and to perform operations on that data. Since registers reside on the CPU chip, operations performed with registers are much faster than operations performed on memory locations.

The registers of the 8086/8088 microprocessor can be grouped as follows:

1. General-purpose registers

a) Data registers (4)

b) Pointer and index registers (4)

2. Instruction pointer register (1)

3. Program status word register (1)

4. Segment registers (4)

Of the 14 registers listed above, 4 are the CS, DS, SS and ES registers, which hold the starting addresses of the CODE, DATA, STACK and EXTRA segments. These four registers are generally called segment registers. Of the remaining ones, 8 are general-purpose registers, 1 is the instruction pointer register, and the last is known as the program status word register. We will call the program status word register the flag register. General-purpose registers are divided into two groups, each consisting of 4 registers. The first four are called data registers, and the other 4 are called pointer and index registers.

### 1. General-purpose registers

### a) Data Registers

The DATA registers, used mostly for arithmetic operations, are AX, BX, CX and DX. Unlike the other registers, each DATA register can be used as a whole or as two parts. A DATA register can be divided into two sub-fields, so that the register can be used either as a single 16-bit register or as two separate 8-bit registers. This feature is shown in the figure. For example, we treat the AX register as 16-bit for 16-bit operations, and AH and AL, which make up AX, for 8-bit operations. The high-order part of any 16-bit data register is denoted by the register name and the first letter of the word 'High', and the low-order part by the register name and the first letter of the word 'Low'. Thus the 8-bit registers named AH and AL for AX, BH and BL for BX, CH and CL for CX, and DH and DL for DX are obtained. It is clear that changing the value of one of these 8-bit registers also changes the value of the 16-bit register containing it, and vice versa. However, an operation performed on either half of a 16-bit register does not change the other half. The figure also shows that registers other than the data registers cannot be divided into sub-fields in this way. For the flag register, however, there is an even different kind of use.

The AX register, which can be called the accumulator, is used as a word-length register in multiplication, division, input, output, and some string operations. The AL register is byte-length and is used as the counter register of some operations or as the transfer area (destination register) in decimal-oriented arithmetic operations. The AH register is used in byte-length division and multiplication. BX, which can be called the base register, is used mostly for addressing data in memory. CX is the counter register; it is used as the counter register of LOOP instructions or repeated string operations. The CL register can be used as a shift and rotate counter. DX, called the data register, is used in word-length multiplication and division operations.

### b) Pointer and Index Registers

As shown in the figure above, the pointer and index registers are SP, BP, SI and DI. However, it is possible to regard the IP and BX registers as pointer or index registers as well. Pointer and index registers, like data registers, can be used for arithmetic operations. However, the main purpose of using these registers is that they are treated as address pointers for accessing data in various memory regions. To indicate the address of a location in memory, two separate address values are used. The first value is the address of the segment containing the location pointed to; segment registers are used at this point. The second address value, which indicates the location's position within the segment, is known as the offset address. Pointer and index registers are used to indicate offset addresses.

The microprocessor uses the CS and IP registers to access locations within the code segment.

```asm
Stack segment içinde bulunan bir veriye ulaşmak için SS registerı ile birlikte SP ya da BP
```

To access data in the stack segment, one of the SP or BP registers must be used together with the SS register. To access locations within the data segment, the DS register, which is the start of the data segment, is used, together with BX, SI or DI to indicate the offset address of the location. To access locations within the extra segment or an arbitrarily selected segment, we can use CS, DS or SS.

### 2. Instruction Pointer Register:

The IP register, which can be called the instruction pointer, contains the offset address of the next instruction to be executed by the execution unit of the 8088. The memory region indicated by the offset address in IP is within the code segment, because the instructions that make up programs reside in this segment. Since the IP register is a special-purpose register, it cannot be used directly by the programmer. However, it is possible to change the value of this register indirectly using information on the stack.

### 3. Program Status Word Register:

We can abbreviate the program status word register as PSW. We will call this register the flag register. The flag register is quite different from the other registers. First of all, the notation 'PSW' is not an operand; it is just an abbreviation used to refer to this register. The flag register cannot be considered as a whole, or as a 16-bit or 8-bit number. This is because what matters is not the numerical value of the flag register but the value of each of the bits that make it up. However, there is a restriction here too: of the 16 bits that make up the register, only 9 are used. The current value of each of these 9 bits affects how various control instructions are executed or gives information about the result of arithmetic or logical operations.

### 4. Segment Registers:

Computers using the 8088 and 8086 processors place programs and data in two separate areas of memory. These program and data areas are at most 64 K in size and are called segments. The 8088 processor can have 4 separate segments at the same time. These segments are called the CODE, DATA, STACK and EXTRA segments. Four separate registers are used to indicate the first byte of these segments, in other words the starting address of the segment. These are, in order, CS, DS, SS and ES, and they are called segment registers. The code segment register CS indicates the starting address of the segment containing the program being executed. In other words, machine language instructions reside in the segment addressed by CS. The stack segment register SS contains the starting address of the current stack segment. The stack segment is a block of memory in which various data are temporarily stored.

```asm
Data segment registeri olan DS ,geçerli data segmentinin başlangıç adresidir. Bu segment genel olarak
```

The data segment register DS holds the starting address of the current data segment. This segment is generally used by program variables. In other words, the data subjected to information processing operations reside in locations within the data segment. The extra segment register ES contains the starting address of the current extra segment. The extra segment is generally used for string operations. In systems with sufficient memory, these 4 segments are different parts of memory. In systems without large memory, these segments may overlap.

### 8086 SEGMENTS

*While discussing the registers above, the 8086 segments were also covered in detail. However, if we summarize the segments again

### ...

```asm
Code Segment:
This segment indicates the address of the segment containing the running program. In other words, machine language instructions reside in the segment addressed by CS. Execution of the program begins from the first byte of the segment.
```

Data Segment:

The data segment register DS contains the starting address of the current data segment. This segment is generally used by program variables. In other words, the data subjected to information processing operations reside in locations (sections) within the data segment.

```asm
Stack Segment:
This segment is used to store return addresses when going to subroutines and the regions needed to return to the operating system at the end of the program.
```

Extra Segment:

Generally used for string operations.

### DEBUG COMMANDS

To see experimentally how Assembly instructions work, to understand whether the programs we write behave as intended, and to correct any errors, DOS's DEBUG.COM program is used. Although there are more advanced, user-friendly debuggers, DEBUG is preferred because it is easy to find and convenient for simple applications. To use the DEBUG program, one must know its commands. Here we will try to explain some of the DEBUG commands with the help of simple examples.

```
C:\>DEBUG
```

- The dash sign indicates that the debug program is now ready to accept commands.

- R (Register): This command is used to determine the current register values and the state of the flags. With the help of this command, the desired values (provided they are hexadecimal) can be assigned to registers. The values NV UP EI PL NZ NA PO NC that follow the registers indicate the state of the flags.

```
-R F
```

### NV UP EI PL NZ AC PO CY -

With this command, only the state of the flags can be viewed and changed as needed. If a flag value is not to be changed, you can press the space bar to move on to the next flag value.

Flag Name                        Set(1)                  Clear (0)

Overflow - OF               OV (overflow)          NV (not overflow) Direction - DF             DN (decrement -         UP (increment - up) down) Interrupt - IF               EI (enable)              DI (disable) Sign - SF                   NG (negative)              PL (plus) Zero - ZF                     ZR (zero)               NZ (not zero) Auxilary Carry- AF        AC (auxilary carry)       NA (not auxilary) Parity - PF                PE (even parity)          PO (odd parity) Carry - CF                  CY (carry yes)           NC (not carry) Flag abbreviations used in the debugger - D (Dump / Display): With this command we can view the contents of any segment of memory starting from any offset. We can also limit the area we want to view. If the address of the range to be displayed is given next to the D command, only the values within the specified address range are displayed on the screen.

- A (Assembly): This command allows simple programs to be written with the help of Debug. Programs written inside Debug start at offset address 100H, as in COM programs. For this reason, when the program is to be run, the value of the IP register must be set to 100H with the R command.

```
-A
2AF2:0100 MOV AX,5
2AF2:0103 ADD AX,4
2AF2:0106 SHR AX,1
2AF2:0108 ^C
```

- After the A command is given, you can write an assembly program starting from address 100H of CS. All numbers given here must be in hexadecimal form. When you finish entering instructions, you can end the process by pressing Ctrl-C.

- T (Trace): This runs the written assembly instructions one by one and displays the values taken by the registers and flags at the end of each operation. The T command starts running from the point IP indicates and stops after each instruction is executed.

If the user wishes, a number can also be given next to the T command. In this case, that many instruction lines are executed back to back, and the register and flag values are printed to the screen each time.

- U (Unassemble): This is a command used to convert the machine code written in CS into mnemonics in a form the user can understand. Each time it is invoked, it shows the user the mnemonics of 32 bytes of machine code.

- E (Edit): This is a command used to change the values at any location in memory.

- F (Fill): This is used to fill a memory area whose start and end addresses are specified with a specified number.

- C (Compare): This is a command used to compare the contents of specified ranges. This command compares the contents at addresses 100H-110H with the contents starting at address 10H and lists those that differ.

```
-G (Go): Used to run the program up to a given address or until it finishes.
```

- H (Hex): Used to calculate the hexadecimal sum and difference of two given numbers.

- L (Load): Used to load the program into memory again.

- M (Move): Used to move a block of data from one place to another.

- P (Proceed): This command has features similar to the T command. After executing instructions, it displays the register and flag values on the screen. However, its biggest difference from the T command is in the handling of instructions such as

```asm
LOOP, CALL, INT. If any of these instructions is executed with the P command, it produces the result without going into the details of that operation.
```

- Q (Quit): A command used to exit the debugger.

### -Q

```
C:\>
```

## homework

8086 Registers and DEBUG Commands;

8086 REGISTERS: The central processing unit, i.e. the CPU, can be described as the brain of the computer. Just as the brain directs all of the body's activities in the human body, the CPU does this job in a computer. A microprocessor takes the form of an integrated circuit or chip made up of millions of transistors and the logic circuits built from them. The CPU manages all of the computer's processing steps. It is connected to all the components on the motherboard. To carry out its tasks, the processor is equipped with address, memory and control buses. The overall performance of the computer varies in direct proportion to the processor used. Intel released the 16-bit 8086 processor in 1978. The 8086, the first processor with high-level programming languages and more efficient operating systems, formed the basis of IBM-compatible systems. With the 8088 processor that followed, IBM released the first personal computer (PC). This first PC had 16K of memory, a display with no graphics capability and a tape drive. This first processor supported 8 bits as its external data bus and ran at a 4.77 MHz clock speed.

Pin Connections AD15-AD7 (8086) Address/Data Bus: These lines contain the multiplexed upper part (the high-order 8 bits) of the address/data bus on the 8086. These lines carry the address bits A15-A8 when the ALE pin is logic 1 and the data bus bits D15-D8 when it is logic 0. These pins show high impedance while the microprocessor is in the hold state. For the 8086/8088 microprocessors, minimum mode is selected by connecting MN/MX directly to +5V. The pin cannot be connected to +5V through a pull-up resistor.

### 1. IO/M (8088), M/IO (8086) Memory Input/Output; It is a pin on the microprocessor address bus that indicates whether the address bus holds a memory address or an I/O address.

It shows high impedance while the microprocessor is in the hold state.

### 2. WR-Write; It is a strobe on the 8086/8088 that indicates data output for memory or I/O devices.

This pin goes to the high-impedance state while the microprocessor is in the hold state.

### 3. INTA-Interrupt Acknowledge; It is responsible for the INTR input pin. The INTA pin is generally used as a gate to the interrupt vector,

which handles the interrupt requests on the data bus.

### 4. ALE-Address Latch Enable; It indicates that the 8086/8088 address/data bus contains address information.

This address may be a memory address or an I/O port number. Note that this pin gives no signal while the microprocessor is in the hold state.

### 5. DT/R Data Transmit/Receive; It indicates whether the microprocessor is receiving

or sending data. This signal is used to enable the external data bus buffers.

### 6. DEN-Data Bus Enable; It is used to enable the external data bus buffers.

### 7. HOLD-Hold; It is a direct memory access request. If HOLD is logic 1, the microprocessor stops executing software

and the address, data and control bus lines go to the high-impedance state. If HOLD is at logic 0, the microprocessor executes its software normally.

### 8. HLDA-Hold Acknowledge (hold request accepted); It indicates that the 8086/8088 has entered the HOLD

state.

### 9. SS0 (8088); It is equivalent to S0, which is used when the microprocessor is operating in max mode. This signal

is combined with IO/M and DT/R to decode the function being performed by the current bus cycle.

### DEBUG COMMANDS

DOS's DEBUG.COM program is used to see by experiment how Assembly instructions work, to check whether the programs written do what they are intended to do, and to fix any errors. Although there are more advanced, user-friendly debuggers, DEBUG is preferred because it is easy to find and convenient for simple applications. To use the DEBUG program, you need to know its commands.

```
C:\>DEBUG;
```

- The dash now indicates that the debug program is ready to accept commands. - R (Register): This command is used to display the current register values and the state of the flags. With the help of this command, desired values (provided they are in hexadecimal) can be assigned to the registers. Flag Name                    Set (1)                Clear (0) Overflow - OF           OV (overflow)         NV (not overflow) Direction - DF         DN (decrement -        UP (increment - up) down) Interrupt - IF            EI (enable)            DI (disable) Sign - SF               NG (negative)              PL (plus) Zero - ZF                  ZR (zero)             NZ (not zero) Auxiliary Carry - AF AC (auxiliary carry)         NA (not auxiliary) Parity - PF            PE (even parity)         PO (odd parity) Carry - CF              CY (carry yes)          NC (not carry) Table 18-1 Flag abbreviations used in the debugger - D (Dump / Display): With this command we can view the contents of any segment of memory starting from any offset we want. We can also limit the area we want to see. If the address of the desired range is given next to the D command, only the values within the specified address range are displayed on the screen. A (Assembly): This command makes it possible to write simple programs with the help of Debug. Programs written inside Debug start at offset address 100H, as in programs with the COM extension. For this reason, when the program is to be run, the value of the IP register must be set to 100H with the R command. - T (Trace): It executes the written assembly instructions one by one and shows the values taken by the registers and flags on the screen at the end of the operation. The T command starts running from the point IP indicates and stops after each instruction is executed. If the user wishes, a number can be given next to the T command. In this case, as many instruction lines as the given number are executed back to back, and the register and flag values are written to the screen each time. - U (Unassemble): It is a command used to convert the machine code at CS into mnemonics in a form the user can understand. Each time it is called, it shows the user the mnemonics of 32 bytes of machine code.

- E (Edit): It is a command used to change the values at any location in memory. - F (Fill): It is used to fill an area whose memory start and end addresses are specified with a specified number. C (Compare): It is a command used to compare the data in specified ranges.

```asm
data in different segments can also be compared.
```

```
-G (Go): It is used to make the program run up to a given address or until it ends
```

.

```
-G
```

Program terminated normally

If the program ran properly, the message above will appear on the screen. If there is an error in the program's return addresses or a logic error was made in the program, the program never ends. In this case the machine will need to be reset. - H (Hex): It is used to compute the hexadecimal sum and difference of two given numbers. - L (Load): It is used to load the program into memory again. - M (Move): It is used to move a block of data from one place to another.

### - M DS:100,110,CS:500

With this command, the data between DS:100H and DS:110H will be placed starting at address CS:500H. - P (Proceed): This command has properties similar to the T command. After executing the instructions, it shows the register and flag values on the screen. However, its biggest difference from the T command is in how it handles instructions such as LOOP, CALL and INT. If any of these instructions is executed with the P command, it produces the result without going into the details of that operation. (If it is a LOOP, it shows the states of the registers and flags once the loop has completed; if it is a CALL, once the operations have been carried out and control has returned; or if it is an INT, once all the operations the interrupt handler needs to perform have been done.) - Q (Quit): It is a command used to exit the debugger.

### -Q

```
C:\>
```

### REFERENCES

- Assembly codes, Faculty of Engineering and Architecture, Department of Computer Engineering

- Microprocessors, Yıldız University publications

- www.gencbilim.com

## appendix-2

### DEBUG COMMANDS (APPENDIX 2)

Command                     A Meaning                    Assembly Usage format          A [Address] Function                Entry into writing a program in assembly language. Example                     A100 (for writing a program starting from offset address 0100) Explanation                  Press ENTER to exit from writing a program in assembly language. Command                     C Meaning                    Compare 1- C [1st address start] [1st address end] [second address start] Usage format 2- C [1st addressLnumber] [second address] Compares two different regions of memory. If these regions are the same, no message Function                is displayed; if there are different bytes within the compared regions, these are shown on the screen. C 0010 0015 0020 (the address locations 0010-0015 are compared with 0020-0025) Example                     C 0010L5 0020 (5 locations starting at address 0010 are compared with 5 locations starting at address 0020) Explanation                  If large address limits are given, all of the desired regions may not be visible on the screen. Command                     D Meaning                    Dump (take a memory dump to the screen) Usage format          D [memory area] Function                Shows any desired part of memory on the screen. D200 (shows 128 one-byte memory locations starting at offset address 0200 on the screen) Example                     D 0010,0050 (shows the memory region between offset addresses 0010 and 0050 on the screen) D100L20 (the first 20h bytes starting from 0100 are shown) If only D is typed and ENTER is pressed, it shows a dump on the screen starting at offset 0100. Explanation                  The command can also be used in a format such as D cs:0250. Command                     E Meaning                    Enter (entering data into memory) Usage format          E [ADDRESS] list Function                Used to quickly enter the desired data into memory. 1- E 0230 'abcdef12345' (enters the data abcdef12345 starting at address 0230; each character takes up 1 byte) Example                     2- If used in the form E 0230, it shows the contents of 0230; this location can be changed if desired, or you can move on without making a change by pressing ENTER. Explanation                  The "D" command can be used to see the entered characters. Command                     F Meaning                    Fill

www.mikroislemciler.com Lect. Eren ERENER

Usage format          F [start address] [end address] character to fill with Function                Used to fill any desired memory region with a hexadecimal value. 1- F 0100 0120 AA (fills the region from address 0100 to address 0120 with the value AAh) 2- F 100L100 22 (fills 100h locations starting at address 0100 with the value 22h) Example                     3- F 100L34 12 AB F1 C4 (fills 34 locations starting at address 0100 with the data sequence 12 AB F1 C4) Explanation                  You can view the filled regions with the D command. Command                     G Meaning                    GO (go, run) Usage format          G [ADDRESS] Function                Used to run the written Assembly program (to have the microprocessor execute it). 1- G (runs the program starting from CS:IP until it is interrupted) Example                     G 0200 (the microprocessor starts executing the data in memory from cs:ip up to offset address 0200, until interrupted) The programmer must know well between which memory limits the written program lies, Explanation                  and cs:ip must be set up before the program is run. If your program is faulty and you are not in protected mode, your system may lock up. Command                     H Meaning                    Hexadecimal add and subtract Usage format          H value1 value2 Function                Shows the sum and difference of two hexadecimal numbers on the screen. Example                     H 9 3 (the sum is 000C and the difference is 0006) Explanation                  The limit is a doubleword. Command                     I (input) Meaning                    Read a value from a port Usage format          i port address Function                Reads 1 byte of data from any port Example                     i 2F8 (reads data from the serial port) Explanation                  None Command                     L Meaning                    Load (load from disk into memory) 1- For parametric usage; L [offset address to load to] [drive no] [start sector] [number of sectors to read from the start sector] Usage format          2- For non-parametric usage; - n file name; first the name of the file to be loaded is typed in this way, then L is typed and enter is pressed. The program is thus loaded into memory starting at CS:0100. The length of the program is placed in BX:CX. Function                Load a program or sector(s) into memory

### 1) L 0100 0 1 2 (loads the 1st and 2nd sectors on drive A to CS:0100

 

### 2) With Debug open;

Example                         – n mer.com (a file named mer.com)

### –L

(loads the mer.com file into memory starting at CS:0100; the space occupied by the program can be seen in BX:CX) For parametric usage, drive no

### 0 = A, 1 = B, 2 = C, 3 = D ……

Explanation In Windows XP, parametric usage is limited. It can only be used for MS-DOS-compatible files. Command                     M (move) Meaning                    Move a memory region. Usage format          M [start address][end address][start address of the destination] Function                Moves any block of memory to another place. Example                     M 0100 010F 0200 Explanation                  None

www.mikroislemciler.com Lect. Eren ERENER

Command                     N (name) Meaning                    Choose a name for the program file Usage format          N file name It has two tasks: the first is to choose a name for the L and W commands, the second is to Function                assign file parameters to the program being test-executed in memory by debug Example                     N dosya1.com Explanation                  None Command                     O (output) Meaning                    Send a value to a port Usage format          O port address Function                Sends 1 byte of data to the output port Example                     O 2F8 Explanation                  None Command                     P (proceed) Meaning                    Execute a subroutine or loop Usage format          P or P = [offset address] Function                Instead of executing the subroutines, loops and interrupts in the program line by line, it executes them in one go. Example                     P (while the program is loaded in memory) Explanation                  After loading any program into memory, have the same program executed first with the T command and then with the P command. Command                     Q (quit) Meaning                    Exit Debug and return to the operating system. Usage format          Q Function                Return to the command prompt Example                     Q Explanation                  Give this command to exit Debug Command                     R (register) Meaning                    View or change the contents of registers Usage format          R or R [register name] Function                View the contents of registers, or view and change them rax ; the 16-bit value of the AX register is shown on the screen and the cursor blinks at the : part; if enter is pressed the contents do not change; to change the contents, a value must be entered before enter (the value must not exceed two bytes). Example r ; when used alone, it shows the 16-bit values of all registers

rf ; used to change the contents of the flag registers

### Flag register states

Flag Flag                 State 1                 State 0 Overflow                       OV                       NV Direction                      DN                       UP Explanation                             Interrupt                       EI                      DI Sign                         NG                       PL Zero                         ZR                       NZ Aux. Carry                      AC                       NA Parity                       PE                       PO Carry                        CY                       NC Command                     S (search) Meaning                    Search in a memory region Usage format          S area list Function                Searches memory for the specified byte sequence and gives the address as the result when found. Example                     S CS:100 110 65 ; searches for the data 65 between offsets 0100 and 0110. Explanation                  None Command                     T (trace, step by step) Meaning                    Make the CPU execute the program's instruction lines step by step Usage format           T [address][value] Function                Runs the program step by step

www.mikroislemciler.com Lect. Eren ERENER

T ; when used alone, executes 1 instruction line starting from CS:0100, Example                     T3 ; executes 3 instruction lines starting from cs:0100, T=0101 8 ; executes 8 instruction lines starting from address CS:0101. Explanation                  None Command                     U (Unassemble) Meaning                    View Assembly instructions in machine code Usage format          U [address] or U [address] L [value] Function                Shows Assembly code in machine language format on the screen U100 ; shows 20h bytes starting from address CS:0100 Example U100L10; shows 10h bytes starting from address CS:0100 Explanation                  If a large value is entered, all of the desired lines may not be visible on the screen at once. Command                     W (write to disk) Meaning                    Write the program in memory to disk

### 1-W

Usage format 2-W [address][drive no][sector][number of bytes] Function                Writes the data in memory to a disk or floppy Example                     W If the W command is used alone, the number of bytes to be written must be written to BX:CX and the file name must be set with the n command before the w command is issued. Explanation

www.mikroislemciler.com Lect. Eren ERENER

## Debug Intro

EEM 332 - Microprocessors Introduction to DEBUG

Notes are taken from; *DEBUG/ASSEMBLY TUTORIAL by Fran Golden http://www.datainstitute.com/debug1.htm **A Guide to DEBUG by Daniel B. Sedory http://www.geocities.com/thestarman3/asm/debug/debug.htm

COM Extensions

### 1. COM programs are very small and compact programs that cannot be larger than 65K bytes

```asm
in size.
```

### 2. The PSP of a COM program is located in the first 100 Hex (256 Dec) locations of the

program.

### 3. The first instruction of the COM program must start at offset 100 in memory.

### 4. DOS creates the PSP for the COM program, which means we don't have to be concerned

with this when we assemble a program.

### 5. All the data, code, and the stack area are in the same segment of memory. (1 segment is

### 65K)

EXE Extensions

### 1. The EXE programs can be any size from (200 bytes-640k bytes)

### 2. The PSP must be setup by the programmer, when the program is assembled.

### 3. The programmer determines where the first instruction is in the program.

### 4. The EXE program uses separate segments for the data, code and stack area in memory.

From the above comparison you can see it is much more difficult to assemble an EXE program than it is a COM program. The debug utility program was designed to work only with a COM program by setting up the PSP area each time we enter debug. Once in debug, we can start assembly of a program at offset 100 and not be concerned with PSP or where the data, code, and stack is located. It is possible to look at an EXE program with debug if we rename the program with a different extension before we load it into memory.

Assembly language ---------------------- Programming in the early days of computing had to be written using the machine code of the microprocessor and as a result required specialized people who had this ability. The use of computers was restricted to the companies and corporations with the finances to support such a specialized operation. It didn't take long for the programmers to write the code to do most of the hard work in binary. One of the most important programs written was the Assembler, which was a conversion type program that allowed the use of English words to represent the instruction set of the CPU, that was compiled into machine code after they were written. One such program is Debug.com that is supplied by the MicroSoft corp. in most versions of DOS.

Debug, which is a small but powerful assembler, converts English sounding words called mnemonics into the machine code. All instructions for the 8088 have a mnemonic word to

```asm
represent them in debug. For example, in the program above, the code can be written in an
```

assembler language that is much easier to write and understand.

The mnemonic form of that program is shown below.

mnemonic form----------machine code

```asm
MOV AX,0005------------B80500
ADD BX,AX---------------01C3
MOV [120],AX------------891E2001
```

Details of Each Command

Assemble: A [address] Creates machine executable code in memory beginning at CS:0100 (or the specified address) from the 8086/8088 (and 8087) Assembly Language instructions which are entered. Although no Macro instructions nor labels are recognized, you can use the pseudo-instructions 'DB' and 'DW' (so you can use the DB opcode to enter ASCII data like this: DB 'This is a string',0D,0A                                                                               ). The 'A' command remembers the last location where any data was assembled, so successive 'A' commands (when no address is specified) will always begin at the next address in the chain of assembled instructions. This aspect of the command is similar to the Dump command which remembers the location of its last dump (if no new address is specified).

The    assembly     process    will   stop    after   you     ENTER      an    empty     line.

### Example (you enter the characters in bold type)

```
-a
```

xxxx:0100 jmp 126 xxxx:0102 db 0d,0a,'This is my first DEBUG program!' xxxx:0123 db 0d,0a,'$' xxxx:0126 xor ax,ax xxxx:0128 mov ah,9 xxxx:012A mov dx,102 xxxx:012D int 21 xxxx:012F mov ax,4c xxxx:0132 int 21 xxxx:0134

```
-g =100
```

This is my first DEBUG program!

Program terminated normally -

NOTE: You can pipe simple 8086/8088 Assembly Language scripts into DEBUG (which can even include a semi-colon ';' followed by comments on any of its lines!).

- DEBUG uses the convention of enclosing operands which refer to Memory locations

```asm
in square brackets '[ ]' (as opposed to an immediate value as an operand).
```

- DEBUG may require you to explicitly tell it whether or not an operand refers to a

word or byte in Memory! In such cases, the data type must be stated using the prefixes 'WORD PTR' or 'BYTE PTR'

- For all 8087 opcodes, the WAIT or FWAIT prefix must be explicitly specified.

Compare: C range address

Compares two blocks of memory. If there are no differences, then DEBUG simply displays

### another prompt (-). Here's an example of what happens when there are differences

-c 140 148 340

```
127D:0143 30 6D       127D:0343
127D:0146 10 63       127D:0346
127D:0148 49 30       127D:0348
```

The bytes at locations 140 through 148 are being compared to those at 340 (through 348, implied); the bytes are displayed side by side for those which are different (with their exact locations on either side of them).

Dump: D [range] D [address] [length] Displays the contents of a block of memory.

### Example

```
-d 100 133
```

xxxx:0100 EB 24 0D 0A 54 68 69 73-20 69 73 20 6D 79 20 66                .$..This is my f xxxx:0110 69 72 73 74 20 44 45 42-55 47 20 70 72 6F 67 72                irst DEBUG progr xxxx:0120 61 6D 21 0D 0A 24 31 C0-B4 09 BA 02 01 CD 21 B8                am!..$1.......!. xxxx:0130 4C 00 CD 21                                                    L..! - This next example uses the option [length]; the 'l24' means a length of 24 hexadecimal

### bytes (that's 36 in decimal)

```
-d 102 l24
```

xxxx:0100       0D 0A 54 68 69 73-20 69 73 20 6D 79 20 66                  ..This is my f xxxx:0110 69 72 73 74 20 44 45 42-55 47 20 70 72 6F 67 72                irst DEBUG progr xxxx:0120 61 6D 21 0D 0A 24                                              am!..$ -

Enter: E address [list] Used to enter data or instructions (as machine code) directly into Memory locations. Example: First we'll change a single byte at location CS:FFCB from whatever it was before to D2

```
-e ffcb d2
```

The next two examples show that either single(') or double(") quote marks are acceptable for entering ASCII data. By allowing both forms, you can include the other type of quote mark

### within your entry string

```
-e 200 'An "ASCII-Z string" is always followed by '
-e 22a "a zero-byte ('00h')." 00
```

Now let's examine a string of 14 hex bytes entered into Memory at location CS:0100 and

### following

```
-e 100 31 C0 B4 09 BA 0E 01 CD 21 B8 4C 00 CD 21
```

This is actually machine code for a program that will display whatever it finds at location CS:010E       until   it   encounters     a    byte      of    24h     (a     '$'    sign).

Here's something a bit more interesting for you to try out: It's essentially the same program, but the data includes all of the bytes from 00h through FFh; except for 24h which was placed at the end of the last line. The DEBUG prompt '-' is purposely left out here so you can copy

```asm
and paste the whole block all at once into DEBUG using a DOS-Window (You'll find Help on
```

### using DOS-Window controls here)

e 100 31 C0 B4 09 BA 0E 01 CD 21 B8 4C 00 CD 21 0D 0A 0D 0A e 112 00 01 02 03 04 05 06 07 08 09 20 0B 0C 20 0E 0F 10 11 e 124 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 e 136 20 25 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35 e 148 36 37 38 39 3A 3B 3C 3D 3E 3F 0D 0A 0D 0A 40 41 42 43 e 15a 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52 53 54 55 e 16c 56 57 58 59 5A 5B 5C 5D 5E 5F 60 61 62 63 64 65 66 67 e 17e 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 78 79 e 190 7A 7B 7C 7D 7E 7F 0D 0A 0D 0A 80 81 82 83 84 85 86 87 e 1a2 88 89 8A 8B 8C 8D 8E 8F 90 91 92 93 94 95 96 97 98 99 e 1b4 9A 9B 9C 9D 9E 9F a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aA aB e 1c6 aC aD aE aF b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 bA bB bC bD e 1d8 bE bF 0D 0A 0D 0A c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 cA cB e 1ea cC cD cE cF d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 dA dB dC dD e 1fc dE dF e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 eA eB eC eD eE eF e 20e f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 fA fB fC fD fE fF 0D 0A e 220 0D 0A 24 The bytes 0Dh and 0Ah produce a Carriage Return and Linefeed on the display, so they were

```asm
replaced by a 20h (a space) in the listing above. The 24h byte was, of course, moved to the
end of the listing and its original location also turned into a space. A blank line was placed at
```

the beginning and after every 64 bytes in the listing using the sequence '0D 0A 0D 0A.' So, we should see four separate lines of 64 characters each (a few of those being blank spaces in the first line of course) when the program is run, right? Start DEBUG in a DOS-Window, copy and paste the lines above into DEBUG at the '-' prompt, then enter the following

### command

g =100 ( 'g' followed by a SPACE, then '=100') This will run* the program in DEBUG... displaying the lines we mentioned and another stating: "Program terminated normally." [ If possible, do NOT close the DOS-Window or exit DEBUG as we'll be making a 'patch' to the code later.] If you were surprised to find more than four spaces on the first line, or that there appear to be some missing characters at the end of that line, then you might want to study about the Control Characters at the beginning of an ASCII chart. You'll also need to learn about Interrupts and what effect different BIOS and DOS Video Functions have on how the ASCII Characters are displayed. ( *Refer to: The 'G' Gocommand.)

OK, I'll save you the time and tell you what happened: First, the Zero byte displays as a blank space here. The 07h byte sounds a BEEP (but does not display anything), 08h performs a BACKSPACE (erasing the 06h byte character) and 09h is a TAB -- which may jump up to eight columns to the right before reaching the next 'Tab Stop.' But since it just happens to begin in column seven, it only moves one column to the right where our program places the blank space we substituted for 0Ah. Lastly, for some reason, when using Function 09 of INT 21 ("Display a string of characters until a '$' sign is encountered"), the ESC character (1Bh; 27 decimal) doesn't display or do anything either. So, upon reaching the end of the first line, it appears      as     if    five      of    the      characters    were      never     displayed.

If you enter the following two lines into DEBUG ( with more blank-space substitutions inserted ) and run the program again, you'll see all of the displayable characters output on the

### first line in their correct positions

e 112 00 01 02 03 04 05 06 20 20 20 20 0B 0C 20 e 120 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 20 All four rows should come out even now, including the last one, because the FFh (255

```asm
decimal) displays as a blank space! You can prove this by inserting another byte such as 2Eh
```

(a period '.') right after the FFh byte. Since DEBUG has no 'Insert' command, here's another

### 'patch' for you which effectively moves the remaining program bytes up one location

e            21e             2e          0d        0a            0d          0a           24

### Here's how the program output should now look when run again

You can save this program to your hard drive, by first giving it a path and filename (such as,

```
C:\TEMP\ASCIIDSP.COM; see 'N' Name command) and writing the bytes (see 'W' Write
```

### command) to a file like this

-n c:\temp\asciidsp.com -rcx

### CX0000

:124       [ Program Length = 223h - 100h + 1 = 124h ] -w

Fill: F range list This command can also be used to clear large areas of Memory as well as filling smaller

### areas with a continuously repeating phrase or single byte. Examples

```
-f 100 12f 'BUFFER'
-d 100 12f
```

xxxx:0100 42 55 46 46 45 52 42 55-46 46 45 52 42 55 46 46 BUFFERBUFFERBUFF xxxx:0110 45 52 42 55 46 46 45 52-42 55 46 46 45 52 42 55 ERBUFFERBUFFERBU xxxx:0120 46 46 45 52 42 55 46 46-45 52 42 55 46 46 45 52 FFERBUFFERBUFFER

```
-f 0 ffff 0
```

This last example fills all of the assigned Segment with bytes of zeros ( which could also be thought of as clearing the whole Segment ). I use this command whenever I want to be sure that the bytes I'm looking at are those I'm concerned about and not just random bits of code lost in memory!

If you want to examine a file from disk in a 'clean' Segment, then you would first have to start DEBUG without the filename on the command line, clear the Segment using -f 0 ffff 0, and then finally load the file with the Name (n) and Load (L) commands.

Go: G [=address] [addresses] Go is used to run a program and set breakpoints in the program's code.

As we saw in an Example for the ENTER command, the '=address' option is used to tell DEBUG a starting location. If you use 'g' all by itself, execution will begin at whatever location is pointed to by the CS:IP registers. Optional breakpoints ( meaning the program will HALT before executing the code at any of these locations) of up to any ten addresses may be      set      by      simply      listing     them      on      the     command       line.

Requirements: Breakpoints can only be set at an address containing the first byte of a valid 8088/8086 Opcode. So don't be surprised if picking some arbitrary address never halts the program; especially if you're trying to DEBUG a program containing opcodes DEBUG can't understand    (that's    anything     'requiring' a   CPU     above     an     8088/8086)!

CAUTION: DEBUG replaces the original instructions of any listed breakpoint addresses with CCh (an INT 3). The instructions at these locations are restored to their originals ONLY if one of the breakpoints is encountered... If DEBUG does not HALT on any breakpoint, then all your breakpoints are still enabled! So, don't ever save the code as is, unless you're sure that DEBUG has hit one of your breakpoints! ( Saving to a backup copy before using breakpoints is often a better way. )

Hex: H value1 value2 A very simple (add and subtract only) hex calculator. Enter two Hex values (only up to four hex digits each), and DEBUG shows first the SUM and then the DIFFERENCE (no carries

### past the fourth digit). Examples

-h 123 100                    -h 100 123                    -h ffff 1

### 0223 0023                     0223 FFDD                     0000 FFFE

-                             -                             - Input: I port

The use of I/O commands while running Windows may be unreliable! This is especially true when trying to directly access hard disks through I/O commands! Long ago (when DOS was the only OS for PCs), there were dozens of BASIC programs that used I/O commands for all sorts of tasks through the parallel and serial ports (e.g., to change fonts on a printer or values in a modem's control registers). They can also be used for direct communications with your          keyboard         or         floppy          drive's         control        chips. Here's an example of how to read the hours and minutes from your computer's "real time

```asm
clock":
```

-o 70 04 <-- Check the hours. -i 71 18 <----- 18 hours (or 6 p.m.)

-o 70 02 <-- Check the minutes. -i 71 52 <----- 52 minutes The first space wasn't necessary under my version of DEBUG; so you might be able to get away with "o70" and "i71" instead. Here's a page of more complex examples dealing with hard drives and the ATA commands for reading info from the disk controllers!

### Load

L [address] [drive] [firstsector] [number] This command will LOAD the selected number of sectors from any disk's Logical Drive under the control of MS-DOS/Windows into Memory. The address is a location in Memory (use only 4 hex digits to keep it within the memory allocated to DEBUG) the data will be copied to, the drive number is mapped as: 0=A:, 1=B:, 2=C:, etc., firstsector counts from ZERO to the largest sector in the disk volume and number specifies in hexadecimal the total number        of     sectors       that     will    be      copied      into     Memory.

The terminology 'Disk Volume' or 'Logical Drive' means that you can not use L[oad] to load or examine the MBR, for example, or any other sectors outside of the Logical Drive Letters           or           Volumes            assigned            by          DOS/Windows. For example, if you enter the command: L 100 2 0 1 in DEBUG, instead of seeing the very first sector on a hard disk (the MBR), you'll see the first sector of the Boot Record for the Logical drive C: of the first hard disk partition that can accessed by a compatible MS-DOS or Windows                                                                                       OS.

Load can be useful in examining a Floppy Disk, but, unfortunately, only if the disk can be read by MS-DOS/Windows. Unlike hard disks, the very first sector on a floppy disk is an OS Boot sector. Here's what you might see from a Logical disk sector and some dumps from a couple                                    floppy                                      disks.

### Examples

-l 100 2 0 1  [ the C: drive. ]

```
-d 100 10f
```

xxxx:0100 EB 58 90 4D 53 57 49 4E-34 2E 31 00 02 08 20 00 .X.MSWIN4.1... .

```
-d 280 2ff
```

xxxx:0280 01 27 0D 0A 49 6E 76 61-6C 69 64 20 73 79 73 74 .'..Invalid syst xxxx:0290 65 6D 20 64 69 73 6B FF-0D 0A 44 69 73 6B 20 49 em disk...Disk I xxxx:02A0 2F 4F 20 65 72 72 6F 72-FF 0D 0A 52 65 70 6C 61 /O error...Repla xxxx:02B0 63 65 20 74 68 65 20 64-69 73 6B 2C 20 61 6E 64 ce the disk, and xxxx:02C0 20 74 68 65 6E 20 70 72-65 73 73 20 61 6E 79 20 then press any xxxx:02D0 6B 65 79 0D 0A 00 00 00-49 4F 20 20 20 20 20 20 key.....IO xxxx:02E0 53 59 53 4D 53 44 4F 53-20 20 20 53 59 53 7E 01 SYSMSDOS    SYS~. xxxx:02F0 00 57 49 4E 42 4F 4F 54-20 53 59 53 00 00 55 AA .WINBOOT SYS..U. - -l 100 0 0 1  [ a floppy in the >A: drive. ]

```
-d 100 13d
```

xxxx:0100 EB 3C 90 29 47 38 71 33-49 48 43 00 02 01 01 00 .<.)G8q3IHC..... xxxx:0110 02 E0 00 40 0B F0 09 00-12 00 02 00 00 00 00 00 ...@............ xxxx:0120 00 00 00 00 00 00 29 40-16 D8 13 4E 4F 20 4E 41 ......)@...NO NA xxxx:0130 4D 45 20 20 20 20 46 41-54 31 32 20 20 20       ME    FAT12 - -l 100 0 0 1  [ a different floppy in the A: drive. ]

```
-d 100 13d
```

xxxx:0100 EB 3C 90 53 59 53 4C 49-4E 55 58 00 02 01 01 00 .<.SYSLINUX..... xxxx:0110 02 E0 00 40 0B F0 09 00-12 00 02 00 00 00 00 00 ...@............ xxxx:0120 00 00 00 00 00 00 29 7E-CF 55 3C 20 20 20 20 20 ......)~.U<

xxxx:0130 20 20 20 20 20 20 46 41-54 31 32 20 20 20             FAT12 -

```
-d 2d0 2ff
```

xxxx:02D0 42 3B 16 1A 7C 72 03 40-31 D2 29 F1 EB A7 42 6F B;..|r.@1.)...Bo xxxx:02E0 6F 74 20 66 61 69 6C 65-64 0D 0A 00 00 00 00 4C ot failed......L xxxx:02F0 44 4C 49 4E 55 58 20 53-59 53 F4 3C 82 3A 55 AA DLINUX SYS.<.:U. Note that the Linux Boot disk above is the kind formatted as an MS-DOS diskette and not as a true Linux floppy. If it had been a floppy formatted for some other OS or with a faulty boot sector, then MS-DEBUG would not be able to read it. Instead you'd see that old "General failure reading drive A / Abort, Retry, Fail?" error message, and then DEBUG's "Disk error reading drive A" message after having cleared the first error message. This makes DEBUG almost worthless as far as trying to fix an error in a floppy disk's boot sector! However, if you keep a binary copy of a good floppy disk Boot Sector somewhere, you could use DEBUG to overwrite whatever's on a faulty floppy disk's first sector (see Write command). But if you really want to see what's in such a Boot sector (that keeps DEBUG from recognizing it as valid), you'll need to use a disk editor that will allow you to do so; such as Symantec's Norton DiskEdit          (ONLY            in         Physical         Disk         Mode        though).

```asm
NOTE: Just because a floppy disk can't be read by DOS or opened in DEBUG does NOT
```

necessarily mean it's defective. It might simply have been formatted with a different OS (such as Linux) and could easily boot-up on its own; a very good reason for labeling your disks! (CAUTION: Never try booting your system with a disk you're not 100% sure of; unless you disconnect all hard disks and don't have any flash BIOS, because it might contain a nasty boot virus!                                                                                            ) [ Many floppy disks have the letters IHC in their OEM ID field. What kind of OEM Name is that? None. Someone at Microsoft decided that this was where they'd place a new pseudo-random type of identification to make sure that any information cached by 'Windows 9x' from one disk wouldn't be mixed up with info from a different one if you swapped disks. The whole string begins with five pseudo-random hex bytes, and always ends with the characters IHC. All floppy diskettes that are not write-protected will have any original OEM ID overwritten. Once Windows has written this string, it will remain the same for any future disk reads or writes. However, performing even a quick format under Windows, will change the               five               hex               bytes              every             time. Some have concluded that the characters 'IHC' are the first three letters of the word "Chicago" in reverse order, since Chicago was the 'code name' for Windows 95™ before it was ever released (it would have appeared as ' OGACIHC' on the hypothetical disk). Although certainly a possibility, I have no proof of that. Due to my interest in some very old Greek Manuscripts, I still can't help seeing the 3 characters 'IHC' as an Iota, Eta and old style Sigma since this combination of letters was often used as an abbreviation for the Greek word IHSUS.         Just     another        one      of       those      coincidences     of       life. REMEMBER: If you really want to preserve all of the contents of an important diskette, you can't even perform a simple Directory read under a Windows OS, UNLESS it is 'write- protected' and you know the drive's write-protect system is functioning correctly! ]

```asm
Move: M range address
```

This command should really be called: COPY (not Move) as it actually copies all the bytes from      within     the       specified    range      to       a       new        address.

### Examples

### 1) -m 7c00 7cff 600

Copies all the bytes between Offset 7C00 and 7CFF (inclusive) to Offset 0600 and following...

### 2) -m 100 2ff 70

This second example shows that it's very easy to overwrite most of the source you're copying from using the Move command. Apparently, DEBUG stores the source bytes elsewhere before writing them; otherwise, this example would cause a problem when it started overwriting what it hadn't copied yet! This copies the 512 bytes between Offsets 100h and 2FFh (inclusive) to Offset 0070 overwriting the first 368 bytes in the process.

Name: N [pathname] [arglist] This command can be used to load files into DEBUG's Memory after you have started the program, but it's main function is to create a new file under control of the Operating System which DEBUG can WRITE data to.

### Normally, when you want to 'debug' a file, you'd start DEBUG with a command like this

```
C:\WINDOWS>debug test.com . But it's also possible to load a file into DEBUG's Memory
```

from within DEBUG itself by using the 'N' command and then the 'L' command (with no

### parameters at all ) like this

-n c:\temp\test.com -l which will load the file test.com into DEBUG's Memory starting at location CS:0100 (you cannot specify any other location). The 'N' command makes it quite easy to save data or an Assembly program you created in DEBUG to a file on your hard drive!

### For example, these commands (in BOLD; with the DEBUG reponses)

-n c:\temp\dosok.com

```
-a 100
```

cs:0100 jmp 12C cs:0102 db "It's OK to run this program under DOS!" cs:0128 db 0d,0a,24 cs:012B nop cs:012C mov dx,102 cs:012F mov ah,9 cs:0131 int 21 cs:0133 mov ax,4c01 cs:0136 int 21 cs:0138 -rcx

### CX 0000

:38 -w Writing 00038 bytes   [ 56 bytes in decimal ] -q will create a 56-byte file called DOSOK.COM in the C:\TEMP folder. Even when running DEBUG in a DOS-window, though, the file names are still limited to DOS's 8 characters plus 3 for the extension! Output: O port byte

See the comments under the Input command.

Proceed: P [=address] [number]

Proceed acts exactly the same as Debug's T (Trace) command for most types of instructions... EXCEPT: Proceed will immediately execute ALL the instructions (rather than stepping through each one) inside any Subroutine CALL, a LOOP, a REPeated string instruction or any software INTerrupts. This means that you do not have to single-step through any of the code contained in a Subroutine or INT call if you use the Proceed (P) command. This means Proceed will be the command you use most often to debug programs, and Trace will only be used to step into a Subroutine or possibly check the logic of the first few iterations of a LOOP or REP instruction.

Quit: Q Immediately quits (exits) the Debug program! No questions ever asked... should be the easiest command to remember.

Register: R [register] Entering ' r ' all by itself will display all of the 8086 register's contents and the next instruction which the IP register points to in both machine code and an unassembled (Assembly Language) form. For example, if you start DEBUG in a Windows 95B DOS-box

### with the command line

>debug c:\windows\command\choice.com

```asm
and then enter an ' r ' at the first DEBUG prompt, DEBUG will display someting similar to
this:
```

```
AX=0000 BX=0000        CX=1437 DX=0000 SP=FFFE            BP=0000 SI=0000 DI=0000
DS=0ED8 ES=0ED8        SS=0ED8 CS=0ED8 IP=0100             NV UP EI PL NZ NA PO NC
0ED8:0100 E90E01             JMP    0211
```

For an explanation of the names of the registers (AX, BX, CX, etc. and the Flag symbols: NV UP EI PL NZ NA PO NC), see the Appendix (The 8086 CPU Registers). The last line shows that the next CPU instruction (actually the first in this case) to be executed, begins at memory location 100 hex (the Offset) in Segment ED8 hex (0ED8:0100) and that the Hex bytes E90E01 represent the actual binary machine code of the CPU instruction (JMP 0211 in Assembly language) that would be executed by DEBUG if you entered a Trace (t) or Proceed (p) command.

If you enter the ' r ' followed by the abbreviation for an 8086 register, such as: ' rcx ', then DEBUG will display only the contents of that register followed by a line with a colon symbol (:) on which you can enter a hex number to change the contents of that register. If you simply

### press the ENTER key, the contents remain the same. For example

-rcx

### CX 0100

:273

means that the Register command was used to change the contents of the CX register from 0100 to 0273. The command ' rcx ' could be used again to verify that the change had indeed taken place. If you type the letter f after an r: ' rf ', this commands DEBUG to display all of the FLAG register bits with a prompt on the same line which allows you to change any or none of the individual flag bits. For example, here's how you would display the flags and

### change just the Zero Flag bit from being cleared (a 0 bit) to being set (a 1 bit)

-rf

NV UP EI PL NZ NA PO NC                    -zr -rf

### NV UP EI PL ZR NA PO NC                    -

- As you can see above the Zero Flag was changed from NZ (cleared) to ZR (set). See the Appendix The FLAGS Register below for an explanation of all the Flag abbreviations.

Search: S range list Searches within a range of addresses for a pattern of one or more byte values given in a list. The list can be comprised of numbers or character strings enclosed by matching single or

### double quote marks. Examples

-s fe00:0 ffff "BIOS"

```
FE00:0021
FE00:006F
```

```
-d fe00:0
FE00:0000 41 77 61 72 64 20 53 6F-66 74 77 61 72 65 49 42                  Award SoftwareIB
FE00:0010 4D 20 43 4F 4D 50 41 54-49 42 4C 45 20 34 38 36                  M COMPATIBLE 486
FE00:0020 20 42 49 4F 53 20 43 4F-50 59 52 49 47 48 54 20                   BIOS COPYRIGHT
FE00:0030 41 77 61 72 64 20 53 6F-66 74 77 61 72 65 20 49                  Award Software I
FE00:0040 6E 63 2E 6F 66 74 77 61-72 65 20 49 6E 63 2E 20                  nc.oftware Inc.
FE00:0050 41 77 03 0C 04 01 01 6F-66 74 77 E9 12 14 20 43                  Aw.....oftw... C
FE00:0060 1B 41 77 61 72 64 20 4D-6F 64 75 6C 61 72 20 42                  .Award Modular B
FE00:0070 49 4F 53 20 76 34 2E 35-31 50 47 00 DB 32 EC 33                  IOS v4.51PG..2.3
```

-s 0:0 dff 'A20'

```
0000:0C42
```

```
-d 0:c40
0000:0C40 0D 0A 41 32 30 20 68 61-72 64 77 61 72 65 20 65                  ..A20 hardware e
0000:0C50 72 72 6F 72 2E 20 20 43-6F 6E 74 61 63 74 20 74                  rror. Contact t
0000:0C60 65 63 68 6E 69 63 61 6C-20 73 75 70 70 6F 72 74                  echnical support
0000:0C70 20 74 6F 20 69 64 65 6E-74 69 66 79 20 74 68 65                   to identify the
0000:0C80 20 70 72 6F 62 6C 65 6D-2E 0D 0A 24 1A 00 BA F6                   problem...$....
```

-0:0 dff 43 4f 4d

```
0000:0774
0000:07C2
0000:07D4
0000:07E6
```

```
-d 0:770
0000:0770 7A 02 A6 02 43 4F 4D 31-20 20 20 20 8E 00 70 00                  z...COM1     ..p.
0000:0780 C0 A0 7A 02 91 02 4C 50-54 31 20 20 20 20 A0 00                  ..z...LPT1     ..
0000:0790 70 00 C0 A0 7A 02 98 02-4C 50 54 32 20 20 20 20                  p...z...LPT2
0000:07A0 2D 01 70 00 C0 A0 7A 02-9F 02 4C 50 54 33 20 20                  -.p...z...LPT3
0000:07B0 20 20 11 EA 27 27 3F FD-CA 00 70 00 00 80 7A 02                    ..''?...p...z.
0000:07C0 AC 02 43 4F 4D 32 20 20-20 20 DC 00 70 00 00 80                  ..COM2     ..p...
0000:07D0 7A 02 B2 02 43 4F 4D 33-20 20 20 20 00 00 6B 03                  z...COM3     ..k.
0000:07E0 00 80 7A 02 B8 02 43 4F-4D 34 20 20 20 20 E8 D2                  ..z...COM4     ..
```

Trace: T [=address] [number] The T command is used to trace (step through) CPU instructions one at a time. If you enter the T command all by itself, it will step through only ONE instruction beginning at the

location specified by your CS:IP registers, halt program execution and then display all the CPU registers plus an unassembled version of the next instruction to be executed; this is the 'default' mode of the TRACE command. Say, however, you wanted DEBUG to trace and

### execute seven instructions beginning at address CS:0205; to do so, you would enter

```
-t =205 7
```

Remember that the value for the number of instructions to execute must be given in hexadecimal just as all other values used in DEUBG. (Since the T command uses the "hardware trace mode" of the CPU, it's possible to step through instructions in a ROM - Read Only Memory - chip.)

Unassemble: U [range] Disassembles machine instructions into 8086 Assembly code. Without the optional [range], it uses Offset 100 as its starting point, disassembles about 32 bytes and then remembers the next byte it should start with if the command is used again. ( The word 'about' was used above, because it may be necessary to finish with an odd-number of bytes greater than 32, depending upon the last type of instruction DEBUG has to disassemble. )

NOTE: The user must decide whether the bytes that DEBUG disassembles are all 8086 instructions, just data or any of the newer x86 instructions (such as those for the 80286, 80386 on up to the lastest CPU from Intel; which are all beyond the ability of DEBUG to understand)!

### Example

```
-u 126 133
```

xxxx:0126 31C0                           XOR          AX,AX xxxx:0128 B409                           MOV          AH,09 xxxx:012A BA0201                         MOV          DX,0102 xxxx:012D CD21                           INT          21 xxxx:012F B84C00                         MOV          AX,004C xxxx:0132 CD21                           INT          21 -

The 8086 CPU REGISTERS

First, a quick review of how Binary and Hexadecimal numbers are related: When the ones and zeros of four Binary bits are grouped together (from 0000 to 1111; often called a nibble), they can be represented by a single Hex digit (from 0 to F); both of which are used to count from 0 to 15 in Decimal. Eight Binary bits (which allow for any Decimal value from 0 to 255) are

```asm
represented by two Hex digits; for example, the Binary number 10101010 is equal to AA in
```

Hexadecimal. Two-digit Hex numbers (or 8-bit Binary numbers) are called bytes. No matter how many digits a number has in Binary or Hexadecimal, you can switch between the two by grouping and converting every four Binary bits to one Hex digit or vice versa. The Hexadecimal equivalent of a 12-bit Binary must have 3 digits (e.g., 101010111100 = ABC hex), and the largest Decimal number that can be represented by sixteen Binary bits (65,535)

is            equivalent               to                FFFF            in           Hex.

The four main (16-bit) registers of an 8086 CPU are called: The Accumulator (AX), Base (BX), Count (CX) and Data (DX) Registers. Each of these registers has a High (H) and Low (L) 8-bit half which can store one Hexadecimal byte (1 byte = 8 binary bits). Each of these

### high and low halves can be accessed separately by program code

AX:                                                 Accumulator BX:                     AH                AL        Base Register CX:                                                 Count Register DX:                     BH                BL        Data Register

### CH                CL

### DH                DL

<-- 8 bits --> <-- 8 bits -->

< 1 byte >        < 1 byte >

### The other 16-bit ( two-byte ) registers of the 8086 CPU are

SP                Stack Pointer

BP                Base Pointer

SI                Source Index

DI                Destination Index

CS                Code Segment

DS                Data Segment

SS                Stack Segment

ES                Extra Segment

IP                Instruction Pointer

The 8086 CPU uses a method I'll call the SEGMENT: OFFSET scheme whenever it needs to access Memory locations or Jump from one 64kb Segment to another. It does this by combining two 16-bit registers together to form a 20-bit Segment:Offset value ( which means it can access over 1MB of Memory this way). For certain types of tasks, the registers are often grouped together in the same way, but the programmer must still make sure that the CPU will

### use them as expected. Here are a couple tasks which are set by the CPU itself

CS             :         IP               Next Instruction SS             :         SP               Stack Pointer

### Two other sets which are often used together in String operations are

DS             :         SI               Source Index ES             :         DI               Destination Index

The "FLAGS" REGISTER

If you really want to use MS-DEBUG (or any other debugger!) to examine the operation of Assembly programs, then I advise you to copy these abbreviations onto notecards and try to understand why certain bits (flags) do/don't change in the register for each instruction in the program you're examining. ( Make sure you study the final table below if you'll be reading textbooks which discuss the newer 16-bit Flags Register. Newer 32-bit debuggers, such as Borland's Turbo Debugger, display the same eight Flags as DEBUG, but use an abbreviation for the Name of the Flag and simply show whether it's a 0 or 1 bit.)

This is an 8-bit register that holds 1-bit of data for each

### of the eight "Flags" which are to be interpreted as follows

Textbook abbrev. for Flag Name =>            of df if sf zf af pf cf If the FLAGS were all SET (1),               -- -- -- -- -- -- -- -- they would look like this...   =>            OV DN EI NG ZR AC PE CY If the FLAGS were all CLEARed (0), they would look like this...   =>            NV UP DI PL NZ NA PO NC

FLAGS                   SET (a 1-bit)   CLEARed (a 0-bit) ---------------                 --------------- ------------------- Overflow        of    =    OV              NV [No Overflow]

Direction      df    =    DN (decrement)      UP (increment)

Interrupt      if    =    EI   (enabled)      DI (disabled)

Sign     sf    =    NG (negative)       PL (positive)

Zero     zf    =    ZR    [zero]        NZ   [ Not zero]

Auxiliary Carry        af    =    AC                  NA   [ No AC ]

Parity     pf   =      PE   (even)         PO   (odd)

Carry     cf   =      CY   [Carry]        NC   [ No Carry]

==============

### The individual abbreviations appear to have these meanings

OV = OVerflow, NV = No oVerflow.    DN = DowN,              UP (up). EI = Enable Interupt, DI = Disable Interupt.

NG = NeGative, PL = PLus; a strange mixing of terms due to the fact that 'Odd Parity' is represented by PO (rather than POsitive), but they still could have used 'MI' for MInus.

ZR = ZeRo, NZ = Not Zero. AC = Auxiliary Carry, NA = Not Auxiliary carry. PE = Parity Even, PO = Parity Odd. CY = CarrY, NC = No Carry.

To help you understand the display in MS-DEBUG compared to any Assembly texts which make references to a 16-bit FLAGS register, here's the layout of the first 12 bits

### (0 - 11) of the newer 16-bit Flags Register

Symbols used by MS-DEBUG ----------------------------------- OV DN EI    NG ZR    AC    PE    CY            ---> When bit = 1 NV UP DI    PL NZ    NA    PO    NC            ---> When bit = 0

### |xx|xx|xx|--|xx|xx| 0|xx| 0|xx| 1|xx| Newer Designations

Bits: 11 10 9 8 7 6 5 4 3 2 1 0 | | | | | | | | | | | '--- CF - Carry Flag | | | | | | | | | | '--- is always a 1 | | | | | | | | | '--- PF - Parity Flag | | | | | | | | '--- is always a 0 | | | | | | | '--- AF - Auxiliary (Carry) Flag | | | | | | '--- is always a 0 | | | | | '--- ZF - Zero Flag | | | | '--- SF - Sign Flag | | | '--- (TF Trap Flag - not shown in MS-DEBUG) | | '--- IF - Interrupt Flag | '--- DF - Direction Flag '--- OF - Overflow flag

## instructions

8086/80186/80286/80386/80486 Instruction Set Instruction                                          Usage         Modifies flags                  Operands

```asm
AAA - Ascii Adjust for Addition                      AAA           AF CF (OF,PF,SF,ZF undefined)   none
AAD - Ascii Adjust for Division                      AAD           SF ZF PF (AF,CF,OF undefined)   none
AAM - Ascii Adjust for Multiplication                AAM           PF SF ZF (AF,CF,OF undefined)   none
```

AAS - Ascii Adjust for Subtraction                   AAS           AF CF (OF,PF,SF,ZF undefined)   none ADC - Add With Carry                                 ADC d,s       AF CF OF SF PF ZF               r,r m,r r,m r,i m,i a,i

```asm
ADD - Arithmetic Addition                            ADD d,s       AF CF OF PF SF ZF               r,r m,r r,m r,i m,i a,i
AND - Logical And                                    AND d,s       CF OF PF SF ZF (AF undefined)   r,r m,r r,m r,i m,i a,i
BSF - Bit Scan Forward                               BSF d,s       ZF                              r,r r,m r32,r32 r32,m32
```

BSR - Bit Scan Reverse                               BSR d,s       ZF                              r,r r,m r32,r32 r32,m32 BSWAP - Byte Swap                                    BSWAP r32     none                            r32 BT - Bit Test                                        BT d,s        CF                              r16,i8 m16,i8 r16,r16 m16,r16 BTC - Bit Test with Compliment                       BTC d,s       CF                              r16,i8 m16,i8 r16,r16 m16,r16 BTR - Bit Test with Reset                            BTR d,s       CF                              r16,i8 m16,i8 r16,r16 m16,r16 BTS - Bit Test and Set                               BTS d,s       CF                              r16,i8 m16,i8 r16,r16 m16,r16

```asm
CALL - Procedure Call                                CALL d        None                            address
```

CBW - Convert Byte to Word                           CBW           None                            none CDQ - Convert Double to Quad                         CDQ           None                            none

```asm
CLC - Clear Carry                                    CLC           CF                              none
CLD - Clear Direction Flag                           CLD           DF                              none
CLI - Clear Interrupt Flag (disable)                 CLI           IF                              none
```

CMC - Complement Carry Flag                          CMC           CF                              none

```asm
CMP - Compare                                        CMP d,s       AF CF OF PF SF ZF               r,r m,r r,m r,i m,i a,i
```

CMPS - Compare String (B, W or Dw)                   CMPS d,s      AF CF OF PF SF ZF               ES:DI,DS:SI CMPXCHG - Compare and Exchange                       CMPXCHG d,s   AF CF OF PF SF ZF               r,r m,r CWD - Convert Word to Doubleword                     CWD           None                            none (AX -> DX:AX) CWDE - Convert Word to Ext.Dword                     CWDE          None                            none (AX->EAX)

```asm
DAA - Decimal Adjust for Addition                    DAA           AF CF PF SF ZF (OF undefined)   none (AL)
DAS - Decimal Adjust for Subtraction                 DAS           AF CF PF SF ZF (OF undefined)   none (AL)
DEC - Decrement                                      DEC d         AF OF PF SF ZF                  r8 m r16/32
DIV - Divide                                         DIV s         AF,CF,OF,PF,SF,ZF undefined     r8 r16 r32 m8 m16 m32
```

(b:AX/src->q=AL,r=AH, w:DX:AX/src->q=AX,r=DX) IDIV - Signed Integer Division                       IDIV s        AF,CF,OF,PF,SF,ZF undefined     r8 r16 r32 m8 m16 m32 IMUL - Signed Multiply                               IMUL s        CF OF (AF,PF,SF,ZF undefined)   r8 r16 r32 m8 m16 m32 (b:AL*src->AX, w:AX*src->DX:AX) IMUL d,s                                      r16,r16 r32,r32 r16,m16 r32,m32 r16,i r32,i IMUL d,s,i8                                   r16,r16,i r32,r32,i r16,m16,i r32,m32,i

```asm
IN - Input Byte or Word From Port                    IN a,port     None                            a,i8 a,DX
INC - Increment                                      INC d         AF OF PF SF ZF                  r8 r16 r32 m
```

INS - Input String from Port                         INS d,port    None                            ES:DI,DX

```asm
INT - Interrupt                                      INT num       TF IF                           i8
```

INTO - Interrupt on Overflow                         INTO          IF TF                           none IRET/IRETD - Interrupt Return                        IRET          AF CF DF IF PF SF TF ZF         none

```asm
JA Jump if Above                                                   CF=0 and ZF=0
JAE Jump if Above or Equal                                         CF=0
JB Jump if Below                                                   CF=1
JBE Jump if Below or Equal                                         CF=1 or ZF=1
JC Jump if Carry                                                   CF=1
JCXZ Jump if                                                       CX Zero CX=0
JE Jump if Equal                                                   ZF=1
JG Jump if Greater (signed)                                        ZF=0 and SF=OF
JGE Jump if Greater or Equal (signed)                              SF=OF
JL Jump if Less (signed)                                           SF != OF
JLE Jump if Less or Equal (signed)                                 ZF=1 or SF != OF
JMP Unconditional Jump                                             unconditional
JNA Jump if Not Above                                              CF=1 or ZF=1
JNAE Jump if Not Above or Equal                                    CF=1
JNB Jump if Not Below                                              CF=0
JNBE Jump if Not Below or Equal                                    CF=0 and ZF=0
JNC Jump if Not Carry                                              CF=0
JNE Jump if Not Equal                                              ZF=0
JNG Jump if Not Greater (signed)                                   ZF=1 or SF != OF
JNGE Jump if Not Greater or Equal (signed)                         SF != OF
JNL Jump if Not Less (signed)                                      SF=OF
JNLE Jump if Not Less or Equal (signed)                            ZF=0 and SF=OF
JNO Jump if Not Overflow (signed)                                  OF=0
JNP Jump if No Parity                                              PF=0
JNS Jump if Not Signed (signed)                                    SF=0
JNZ Jump if Not Zero                                               ZF=0
JO Jump if Overflow (signed)                                       OF=1
JP Jump if Parity                                                  PF=1
JPE Jump if Parity Even                                            PF=1
JPO Jump if Parity Odd                                             PF=0
JS Jump if Signed (signed)                                         SF=1
JZ Jump if Zero                                                    ZF=1
JCXZ/JECXZ - Jump if CX is Zero                      JCXZ label    None                            addr
JMP - Unconditional Jump                             JMP target    None                            addr
```

LAHF - Load Rister AH From Flags                     LAHF          None                            none

1/2

8086/80186/80286/80386/80486 Instruction Set LDS - Load Pointer Using DS                                  LDS d,s            None                            r16,m32 r,m

```asm
LEA - Load Effective Address                                 LEA d,s            None                            r,m
```

LES - Load Pointer Using ES                                  LES d,s            None LFS - Load Pointer Using FS LGS - Load Pointer Using GS

```asm
LODS - Load String (Byte, Word or Double)                    LODS s             None                            DS:SI->accumulator
LOOP - Decrement CX and Loop if CX Not Zero                  LOOP label         None
LOOPE - Loop While Equal                                     LOOPE label        None
LOOPZ - Loop While Zero                                      LOOPZ label        None
LOOPNZ - Loop While Not Zero                                 LOOPNZ label       None
LOOPNE - Loop While Not Equal                                LOOPNE label       None
```

LSS - Load Pointer Using SS

```asm
MOV - Move Byte or Word                                      MOV d,s            None
MOVS - Move String (Byte or Word)                            MOVS d,s           None                            DS:SI->ES:DI
MOVSX - Move with Sign Extend                                MOVSX d,s          None
MOVZX - Move with Zero Extend                                MOVZX d,s
MUL - Unsigned Multiply                                      MUL s              CF OF (AF,PF,SF,ZF undefined)
```

NEG - Two's Complement Negation                              NEG d              AF CF OF PF SF ZF

```asm
NOP - No Operation (90h)                                     NOP                None
NOT - One's Compliment Negation (Logical NOT)                NOT d              None
OR - Inclusive Logical OR                                    OR d,s             CF OF PF SF ZF (AF undefined)
OUT - Output Data to Port                                    OUT port,a         None
```

OUTS - Output String to Port                                 OUTS port,s        None

```asm
POP - Pop Word off Stack                                     POP d              None
```

POPA/POPAD - Pop All Risters onto Stack                      POPA               None POPF/POPFD - Pop Flags off Stack                             POPF POPFD                                                        all flags

```asm
PUSH - Push Word onto Stack                                  PUSH s
```

PUSHA/PUSHAD - Push All Risters onto Stack                   PUSHA PUSHAD                                                       None PUSHF/PUSHFD - Push Flags onto Stack                         PUSHF PUSHFD                                                       None

```asm
RCL - Rotate Through Carry Left                              RCL d,count        CF OF
RCR - Rotate Through Carry Right                             RCR d,count        CF OF
REP - Repeat String Operation                                REP                None
REPE/REPZ - Repeat Equal / Repeat Zero                       REPE               None
REPNE/REPNZ - Repeat Not Equal / Repeat Not Zero             REPNE              None
RET/RETF - Return From Procedure                             RET nBytes
ROL - Rotate Left                                            ROL d,count        CF OF
ROR - Rotate Right                                           ROR d,count        CF OF
```

SAHF - Store AH Rister into FLAGS                            SAHF               AF CF PF SF ZF

```asm
SAL/SHL - Shift Arithmetic Left / Shift Logical Left         SAL d,count        CF OF PF SF ZF (AF undefined)
SHL d,count        CF OF PF SF ZF (AF undefined)
SAR - Shift Arithmetic Right                                 SAR d,count        CF OF PF SF ZF (AF undefined)
```

SBB - Subtract with Borrow/Carry                             SBB d,s            AF CF OF PF SF ZF

```asm
SCAS - Scan String (Byte, Word or Doubleword)                SCAS string        AF CF OF PF SF ZF
```

SETAE/SETNB - Set if Above or Equal / Set if Not Below       SETAE d            none                            r8 m8 SETB/SETNAE - Set if Below / Set if Not Above or Equal SETBE/SETNA - Set if Below or Equal / Set if Not Above SETE/SETZ - Set if Equal / Set if Zero SETNE/SETNZ - Set if Not Equal / Set if Not Zero SETL/SETNGE - Set if Less / Set if Not Greater or Equal SETGE/SETNL - Set if Greater or Equal / Set if Not Less SETLE/SETNG - Set if Less or Equal/Set if Not greater or Equal SETG/SETNLE - Set if Greater / Set if Not Less or Equal SETS - Set if Signed SETNS - Set if Not Signed SETC - Set if Carry SETNC - Set if Not Carry SETO - Set if Overflow SETNO - Set if Not Overflow SETP/SETPE - Set if Parity / Set if Parity Even SETNP/SETPO - Set if No Parity / Set if Parity Odd

```asm
SHL - Shift Logical Left See: SAL
SHR - Shift Logical Right                                      SHR d,count      CF OF PF SF ZF (AF undefined)
```

SHLD/SHRD - Double Precision Shift                             SHLD d,s,count   CF PF SF ZF (OF,AF undefined) SHRD d,s,count   CF PF SF ZF (OF,AF undefined) STC - Set Carry                                                STC              CF                              none STD - Set Direction Flag                                       STD              DF                              none STI - Set Interrupt Flag                                       STI              IF                              none

```asm
STOS - Store String (B,W,Dword)                                STOS d           None                            accumulator->ES:DI
SUB - Subtract                                                 SUB d,s          AF CF OF PF SF ZF               r,r m,r r,i m,i a,i
TEST - Test For Bit Pattern                                    TEST d,s         CF OF PF SF ZF (AF undefined)   r,r r,m m,r r,i m,i a,i
XCHG - Exchange                                                XCHG d,s         None                            r,r m,r r,m a,r r,a
```

XLAT/XLATB - Translate                                         XLAT X-table     None                            [BX+AL]->AL

```asm
XOR - Exclusive OR                                             XOR d,s          CF OF PF SF ZF (AF undefined)   r,r m,r r,m r,i m,i a,i
```

2/2
