---
baslik: EEM332 Microprocessors: Laboratory 1–2: DEBUG and Segment Registers
ozet: Getting started with DEBUG, the CS/DS/SS/ES and IP registers, memory addresses; handouts and student solutions with personal information removed.
---

This post brings together the related notes and exercises from the Başkent University **EEM332 Microprocessors** course archive (2006–2015). It covers getting started with DEBUG, the CS/DS/SS/ES and IP registers, and memory addresses; handouts and student solutions with personal information removed. Work prepared by a friend and course documents are presented together; student names, numbers, and group information have been removed. PDF archive copies of the documents and, where available, the source code can be downloaded as a ZIP at the end of the post.

## eem332_lab01

EEM 332 - Microprocessors

Experiment Number: 1 Experiment Title: Introduction to Debug, x86 Registers, and Machine Instructions

Preliminary Work: Research the 8086 registers and DEBUG commands and prepare a summary of at most four pages. Be sure to include the names of the sources you used.

Experimental Work

Read the following exercises and apply the given commands. State the answers to the questions in your report.

### To run the DEBUG program, open a DOS window and enter the following command

```
C:\> debug <enter>
```

DEBUG responds with a hyphen "-" prompt. The hyphen prompt indicates that the DEBUG program is ready to accept commands interactively. One of the most important commands is the "?" command, which gives a summary of all valid commands. A list of all valid DEBUG commands is given on page 118 of the textbook.

Now run DEBUG and display the list of all commands;

```
C:\> debug              <enter>
```

-?                      <enter>

When these commands are applied, a list of valid DEBUG commands is displayed on the screen. All commands consist of a single letter. Some commands require additional arguments.

### Arithmetic Operations in DEBUG

The "h" command shows the sum and difference of the two arguments given in DEBUG. DEBUG works only in the hexadecimal number system!

### Enter the following command at the DEBUG prompt

-h 3 2 <enter>

### After the command is executed, the following line will be displayed on the screen

0005 0001

Here, the results of the addition and subtraction operations are shown, respectively: 3+2=5 and 3-2=1.

### Now try the following command

-h 2 3 <enter>

In this case the negative result, 2-3= -1, is given as the two's complement. To identify a number as negative, one checks whether its most significant bit is 1. On the other hand, the most significant bit of a positive number resulting from an addition can also be 1. Interpreting the result correctly

### is up to the PROGRAMMER. As an example, run the following commands

-h E1F6 1E09 <enter>

### The positive result of the addition appears as FFFF! Now run the following command

-h 5C3F0 4BC6 <enter>

The error message you see is caused by DEBUG operating on a WORD basis. In the x86 architecture, a word is 16 bits long.

### Registers and Memory

x86 processors (at least the 8086 version) contain 14 basic registers. To view the contents of the registers

### enter the following command

```
-r <enter>
```

Note the two-letter abbreviations at the end of the second line. These abbreviations show the values of the special-purpose bits in the FLAGS register. The "r" command, with the name of a register as an argument, can be used to examine and modify the contents of that register. For example, enter the following commands:

```
-r ax <enter>
```

ax    0000 :3A7 <enter>

Now examine all the registers again using the r command. You will see that the AX register now holds the number 03A7.

Using the r command, load the value 92A into the BX register. Then observe that the AX and BX registers hold the numbers 3A7 and 92A, respectively.

Now, instead of using DEBUG commands, we will have the x86 microprocessor perform the operation 3A7+92A in its memory using machine instructions. Here DEBUG will be used only as a tool for loading the instructions into the processor. The "e" command is used to examine and modify the contents of memory.

### Apply the commands given below

```
-e 100                          <enter>
3756:0100       E4.01           <enter>
-e 101                          <enter>
3756:0101       85.D8           <enter>
```

When entering the commands above, you will most likely see values different from 3756, E4, and 85. These numbers depend on the state of memory before DEBUG was run, and they are unimportant at this stage. You need to enter the values 01 and D8 at the relative locations (offsets) 0100 and 0101. By entering the e 100 command, we instruct DEBUG to load a byte of data at relative location (offset) 0100 in the current code segment. In the example above, the existing byte E4 at address 3756:0100 has been replaced with the byte 01 entered by the user. In the same example, the address of the code segment is 3756. This value may be different on your computers, but that is unimportant for now.

If you multiply the code segment address by 10 in hexadecimal and add the offset value to the result, you obtain the physical address. X86 systems generally specify memory addresses in segmented form.

### Addition Using x86

### Examine the register contents

```
-r <enter>
```

### The screen display will be similar to the following

```
AX=03A7 BX=092A CX=0000 DX=0000 SP=#### BP=#### SI=#### DI=####
DS=#### ES=#### SS=#### CS=#### IP=0100 NV UP DI PL NZ NA PO NC
```

### #### : 0100 01D8 ADD AX, BX

Here # represents one hexadecimal digit. The last line of the display indicates that the value 01D8 is stored in memory. This is in fact the machine language equivalent of the ADD AX, BX instruction; when this instruction is executed, the contents of the specified registers are added and the result is written to the AX register. Since the x86 architecture is byte-addressable, the information is arranged as follows

### as follows

3756 : 0100             01

### 3756 : 0101             D8

Although the instruction is in memory in x86, the location of the instruction must be specified for it to be executed. The method used in x86 systems employs two special registers: CS and IP. These registers hold the segmented address of the next instruction to be executed. In this way, the location in memory of the instruction to be executed is effectively indicated by the code segment value (held in the CS register) and the offset value (held in the IP register). When necessary, the correct offset value is loaded into the IP register using the r command (0100 in the example).

DEBUG has a trace command, "t", which allows machine language instructions to be executed one at a time. Let us apply the trace command

### to DEBUG with the current memory and register contents

```
-t <enter>
```

The contents of the AX register is now 0CD1, the sum of the numbers 03A7 and 092A. The contents of the AX register is seen to have changed to the sum obtained as the result of the operation. At the same time, the contents of the IP register changes to 0102. x86 systems automatically change the contents of the IP register according to the address of the next instruction to be executed.

Now, using your systems, add the value 092A (in the BX register) to the value 0CD1 (in the AX register). Do not forget to set the IP register to the appropriate value using DEBUG's r command!

To perform the subtraction operation, the machine language instruction required must be added to the code segment. Add the instruction encoded in machine language as 29D8 to the current code segment using the e command, with the offset value set to 0100. Using the r command, observe that the SUB AX, BX instruction has been placed in memory, and then have this operation carried out using the trace command.

### Using DOS Functions in Assembler Language Programs

```asm
The INT instruction allows access to special programs that are copied into memory from the hard
```

disk via DOS during the computer's boot process in x86 systems. For now, the INT instruction can be thought of as a "function caller."

Using DEBUG, let us load the value 0200 into the AX register and the value 0041 into the DX register. The machine language equivalent of the INT 21 instruction is CD21 (details of the INT instruction and the values assigned to registers can be found at the link given on the web page). Using the offset value 0102, enter CD in the current code segment in memory and 21 at the location indicated by the next offset value. Set the IP register to 0102 and check that the memory and register contents are correct. Then run the instruction by applying the following

### operation

```
-g 104 <enter>
```

The g command is DEBUG's "go until" command. By applying this line, we cause the x86 to execute all instructions from the current IP value up to the specified IP value. No change occurs in the code segment here (only IP changes in the CS:IP structure). Had we used the trace (t) command, we would have had to use the same command many times, once for each instruction, in order to execute all the instructions within the INT 21 function, and in some cases this would mean running quite long pieces of code line by line. By using the g command, all the necessary instructions are executed until the value CS:0104 is reached.

At the end of the operation above, we see the character A printed on the screen. The INT function we use here is number 21 among all INT functions. By using this function, access to other DOS functions can be obtained. The value 02 in the AH register (AH is the most significant byte of AX) indicates to DOS that a character will be written to the screen. The character to be printed is specified by the value 41 that we wrote into the DL register (DL is the least significant byte of DX). 41 is the equivalent of the character A in ASCII code.

### Terminating Programs

When assembler or machine language programs finish their work, the x86 system must become controllable by the operating system. One way to accomplish this is to call the INT 20 function. In programs written in high-level programming languages (such as C/C++), the compiler adds this line automatically. In the low-level assembler language we are using, adding the INT 20 line at the end of the program depends on the programmer and their needs.

### Now let us write the following 2-line program

```asm
INT 20
INT 21
```

### To do this, we need to perform the following operations

### 1. Using DEBUG's r command, store the values 0200 and 0043 in the AX and DX registers,

respectively

### 2. Load the following into memory in order

### CD

### CD

### 3. Load into the IP and CS registers the memory addresses that indicate the location of the INT 21 instruction

### 4. Specify a valid ending offset value and run these instructions using DEBUG's g command

Congratulations! You have written and run your first machine language program. Show the program running to the laboratory instructor.

QUESTION 1: What did you see on the screen when you ran the 2-line program? Explain the reason.

### Assemble/Disassemble

Many programs are longer than two lines. To see the mnemonics, which are the human-readable form of the code you wrote, set the value of the IP register to point to the starting location of your 2-line program and enter DEBUG's unassemble command

### as follows

```
-u <enter>
```

You will see that your program is written in mnemonics, and next to each mnemonic there is a hexadecimal machine code stored in memory. What we have done so far involved machine language code. Writing a program using mnemonics is easier in terms of writing and understanding. For this reason, DEBUG includes an assemble command, "a". As an example, consider the 2-line program. Starting from offset value 0100 in the current code segment, let us write the same

### program as mnemonics

```
-a 100          <enter>
```

```asm
int 21          <enter>
int 20          <enter>
```

<enter>

With the commands above, you can express the same program as mnemonics instead of hexadecimal machine code.

### DEBUG Scripts

Assembler language programs can be written using DEBUG alone. In this case there are some limitations. Detailed information will be given when these limitations in DEBUG are encountered. Assembler language programming can be done in DEBUG in two different ways. In the first method, the code is typed and run in the DEBUG window. In the second method, a file containing the assembler language code can be created and run by DEBUG. Do the following exercise, which demonstrates the second method:

### 1. Using any word processor or text editor on your computer (e.g., Notepad),

create a file named TEMP.DBG. The required contents of this file are given below. You may use any word processor or text editor you wish, but you must save the file as a TEXT or ASCII file!

a 100

```asm
mov ah, 02
mov dl, 2a
```

```asm
int 21
int 20
```

n temp.com r bx r cx w q

You must also leave the blank line between the lines above when writing the commands. This line indicates to DEBUG that the assembler code has ended and that the use of DEBUG commands is beginning.

### 2. Open the DOS command prompt and type the following command:

```
C:\> DEBUG < TEMP.DBG               <enter>
```

After this operation, an executable file named TEMP.COM will be created on your hard disk.

QUESTION 2: Run the file named TEMP.COM. What does this file do?

QUESTION 3: Using the information in this document and DEBUG's help menu (the ? command), state what functions the lines in the TEMP.DBG file perform.

QUESTION 4: Briefly summarize what you learned from this experiment.

## eem332_lab02

EEM 332 - Microprocessors Experiment Number: 2 Experiment Title: Basic Debug and Assembly Commands

Preliminary Work: Read the "Introduction to Debug" document.

### 1.        Explain how the segment registers (CS, SS, DS, ES) and the instruction pointer (IP) are used.

### 2.        Explain the DEBUG commands written in CAPITAL letters that you see in the experimental work section.

Experimental Work: Perform the operations given below. State the required command lines and the results you observe in your report.

### 1. Using the REGISTER command:

a. display the current contents of the registers, b. change the contents of the IP register to 100₁₆, c. change the contents of the DS register to 1500₁₆, d. change the contents of the CS register to 1600₁₆, e. change the state of the overflow flag to "no overflow" and the state of the parity flag to "even parity".

### 2. According to the new register states resulting from the changes above, calculate

the effective address for the following a. DS:BX b. CS:IP c. SS:BP

### 3. Using the FILL command, replace the current values of 16 storage locations,

starting from address DS:10, with the value 23₁₆.

### 4. Observe the contents of the first 64 bytes of the current data segment using the DUMP

command.

### 5. Using the MOVE command, copy 20 storage locations starting from address DS:15

to the storage locations starting from address CS:100, and observe the changes with the DUMP command.

### 6. Using the SEARCH command, determine the locations where the values 86₁₆ and

FF₁₆ are found in the range DS:00 to DS:100.

### 7. Using the COMPARE command, perform the following operations

a. Compare the contents of 20 locations starting from address DS:15 with the contents of the locations starting from address CS:100,

b. Repeat step (a) for 32 storage locations.

### 8. Using the ASSEMBLE command, enter the commands given below and verify the

machine language codes they produce with the UNASSEMBLE command. How many bytes does each instruction occupy?

```asm
MOV AX,00
MOV BX,AX
MOV CX,12
MOV DX,0101
OR CX,AX
OR AX,CX
ADD BX,AX
SUB AX,BX
ROL DX,1
ROR DX,1
ROR DX,1
NOT DX
```

### 9. Using the TRACE command, run the program above step by step

and observe the changes in the register contents.

```asm
Note: Numbers in base 16 are indicated with the subscript "16". Since all other
```

numbers are given in base 10, you may need to convert them to base 16.

EEM 332 – Microprocessors Experiment 2 Worksheet

### Name

1       Translate the following mnemonic instructions into machine language codes. a) MOV AX,BX                              Answer___________ b) MOV AX,0AAAAH                          Answer ___________ c) MOV AX,[BX]                            Answer ___________ d) MOV AX,[0004]                          Answer ___________ e) MOV AX,[BX+SI]                         Answer ___________ f) MOV AX,[SI]+[0004]                     Answer ___________ g) MOV AX,[BX][SI]+[0004]                 Answer ___________

2       State the number of bytes occupied by each of the codes above. a) Answer ___________ b) Answer ___________ c) Answer ___________ d) Answer ___________ e) Answer ___________ f) Answer ___________ g) Answer ___________

3       Perform the following operations and observe the results. State the commands you wrote to carry out each operation. Address condition for all operations: DS=200, CS=100.

a. Load the values ED at address DS:1234, BE at address DS:1235, CD at address DS:1236, and AB at address DS:1237. b. Load the value 1236 into the SI register. c. Display the state of the registers after these changes.

### d. Assemble the following instructions starting from address CS:0000

```asm
MOV AX, 1234
MOV BX,[1234]
MOV CX,[SI]
```

e. Set the CS and IP register values required to trace the instructions you wrote. f. Trace the program and observe the results. Explain the changes in the AX, BX, and CX registers and the reasons for them.

## calisma-623

1.)

a)

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=13FA ES=13FA SS=13FA CS=13FA IP=0100 NV UP EI PL NZ NA PO NC
```

```
13FA:0100 0000      ADD     [BX+SI],AL      DS:0000=CD
```

b)

```
-r ip
```

### IP 0100

### 

c)

```
-r ds
```

### DS 13FA

:1800

d)

```
-r cs
```

### CS 13FA

:2400

e)

```
-r f
```

NV UP EI PL NZ NA PO NC -pl

```
-r f
```

NV UP EI PL NZ NA PO NC -ov

```
-r f
```

### OV UP EI PL NZ NA PO NC -

f)

```
-r
```

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0100 OV UP EI PL NZ NA PO NC
```

```
2400:0100 0000        ADD    [BX+SI],AL               DS:0000=00
```

2.)

```
-f 20 3d 42
```

3.)

```
-d 20 3d
```

```
1800:0020 42 42 42 42 42 42 42 42-42 42 42 42 42 42 42 42 BBBBBBBBBBBBBBBB
```

```
1800:0030 42 42 42 42 42 42 42 42-42 42 42 42 42 42         BBBBBBBBBBBBBB
```

4.)

-m ds:20 33 cs:100

```
-d cs:100 133
```

```
2400:0100 42 42 42 42 42 42 42 42-42 42 42 42 42 42 42 42 BBBBBBBBBBBBBBBB
```

```
2400:0110 42 42 42 42 00 00 00 00-00 00 00 00 00 00 00 00 BBBB............
```

```
2400:0120 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

```
2400:0130 00 00 00 00                         ....
```

```
-d ds:20 33
```

```
1800:0020 42 42 42 42 42 42 42 42-42 42 42 42 42 42 42 42 BBBBBBBBBBBBBBBB
```

```
1800:0030 42 42 42 42                         BBBB
```

5.)

a)

-c ds:20 33 cs:100

b)

-c ds:20 47 cs:100

```
1800:0034 42 00 2400:0114
```

```
1800:0035 42 00 2400:0115
```

```
1800:0036 42 00 2400:0116
```

```
1800:0037 42 00 2400:0117
```

```
1800:0038 42 00 2400:0118
```

```
1800:0039 42 00 2400:0119
```

```
1800:003A 42 00 2400:011A
```

```
1800:003B 42 00 2400:011B
```

```
1800:003C 42 00 2400:011C
```

```
1800:003D 42 00 2400:011D
```

6.)

-s ds:00 30 42

```
1800:0020
```

```
1800:0021
```

```
1800:0022
```

```
1800:0023
```

```
1800:0024
```

```
1800:0025
```

```
1800:0026
```

```
1800:0027
```

```
1800:0028
```

```
1800:0029
```

```
1800:002A
```

```
1800:002B
```

```
1800:002C
```

```
1800:002D
```

```
1800:002E
```

```
1800:002F
```

```
1800:0030
```

7.)

```
-a 100
```

```
2400:0100 mov ax,55
```

```
2400:0103 mov bx,ax
```

```
2400:0105 mov cx,20
```

```
2400:0108 mov dx,0110
```

```
2400:010B or cx,ax
```

```
2400:010D or ax,cx
```

```
2400:010F add bx,ax
```

```
2400:0111 sub ax,bx
```

```
2400:0113 rol dx,1
```

```
2400:0115 ror dx,1
```

```
2400:0117 ror dx,1
```

```
2400:0119 not dx
```

```
2400:011B
```

```
-u 100
```

```
2400:0100 B85500       MOV     AX,0055
```

```
2400:0103 89C3        MOV     BX,AX
```

```
2400:0105 B92000       MOV     CX,0020
```

```
2400:0108 BA1001       MOV     DX,0110
```

```
2400:010B 09C1        OR    CX,AX
```

```
2400:010D 09C8        OR     AX,CX
```

```
2400:010F 01C3        ADD    BX,AX
```

```
2400:0111 29D8        SUB    AX,BX
```

```
2400:0113 D1C2        ROL    DX,1
```

```
2400:0115 D1CA        ROR    DX,1
```

```
2400:0117 D1CA        ROR    DX,1
```

```
2400:0119 F7D2        NOT    DX
```

```
2400:011B 0000        ADD    [BX+SI],AL
```

```
2400:011D 0000     ADD    [BX+SI],AL
```

```
2400:011F 0000     ADD    [BX+SI],AL
```

8.)

```
-r ip
```

### IP 0100

:100

```
-t 3
```

```
AX=0055 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0103 OV UP EI PL NZ NA PO NC
```

```
2400:0103 89C3     MOV    BX,AX
```

```
AX=0055 BX=0055 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0105 OV UP EI PL NZ NA PO NC
```

```
2400:0105 B92000    MOV     CX,0020
```

```
AX=0055 BX=0055 CX=0020 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0108 OV UP EI PL NZ NA PO NC
```

```
2400:0108 BA1001    MOV     DX,0110
```

```
-t 3
```

```
AX=0055 BX=0055 CX=0020 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=010B OV UP EI PL NZ NA PO NC
```

```
2400:010B 09C1     OR    CX,AX
```

```
AX=0055 BX=0055 CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=010D NV UP EI PL NZ NA PO NC
```

```
2400:010D 09C8    OR    AX,CX
```

```
AX=0075 BX=0055 CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=010F NV UP EI PL NZ NA PO NC
```

```
2400:010F 01C3    ADD   BX,AX
```

```
-t 3
```

```
AX=0075 BX=00CA CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0111 NV UP EI PL NZ NA PE NC
```

```
2400:0111 29D8    SUB   AX,BX
```

```
AX=FFAB BX=00CA CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0113 NV UP EI NG NZ AC PO CY
```

```
2400:0113 D1C2    ROL   DX,1
```

```
AX=FFAB BX=00CA CX=0075 DX=0220 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0115 NV UP EI NG NZ AC PO NC
```

```
2400:0115 D1CA    ROR    DX,1
```

```
-t 3
```

```
AX=FFAB BX=00CA CX=0075 DX=0110 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0117 NV UP EI NG NZ AC PO NC
```

```
2400:0117 D1CA    ROR    DX,1
```

```
AX=FFAB BX=00CA CX=0075 DX=0088 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=0119 NV UP EI NG NZ AC PO NC
```

```
2400:0119 F7D2    NOT   DX
```

```
AX=FFAB BX=00CA CX=0075 DX=FF77 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1800 ES=13FA SS=13FA CS=2400 IP=011B NV UP EI NG NZ AC PO NC
```

```
2400:011B 0000    ADD   [BX+SI],AL          DS:00CA=00
```

## D2 preliminary work

### 1)

a) Code Segment

```asm
The code segment register, CS, indicates the starting address of the segment containing the program being executed. In other words, machine language instructions reside within the segment addressed by CS. The stack segment register, SS, contains the starting address of the current stack segment. The stack segment is a block of memory in which various data are temporarily stored.
```

b) Data Segment

```asm
The data segment register, DS, is the starting address of the current data segment. This segment is generally used by program variables. In other words, the data subjected to data processing operations reside at locations within the data segment.
```

c) Extra Segment

```asm
The extra segment register, ES, contains the starting address of the current extra segment. The extra segment is generally used for string operations. In systems with sufficient memory, these 4 segments are different parts of memory. In systems without large memory, these segments may overlap.
```

d) Stack Segment

```asm
The stack segment register, SS, contains the starting address of the current stack segment. The stack segment is a block of memory in which various data are temporarily stored.
```

e) IP: It is used as an address pointer to access data in various memory regions. Two separate address values are used to indicate the address of a location in memory. The first value is the address of the segment containing the indicated location; the segment registers are used at this point. The second address value, which indicates the location's position within the segment, is known as the offset address. Pointer and index registers are used to specify offset addresses.

### 2)

- R (Register) : This command is used to determine the current register values and the state of the flags.

### Ex

```
-R
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2AF2 ES=2AF2 SS=2AF2 CS=2AF2 IP=0100 NV UP EI PL NZ NA PO NC
2AF2:0100 8B24   MOV   SP,[SI]           DS:0000=20CD
```

-

With the help of this command, desired values (provided they are hexadecimal) can be given to the registers.

### Ex

```
-R AX
```

### AX 0000

- F (Fill) : It is used to fill an area whose memory start and end addresses are specified with a specified number.

### Ex

-

```
-F DS:100,120,AB
```

Using the F command, the portion of DS between 100H and 120H will be filled with the value ABH. If we then examine from address DS:100H with the D command, we verify that the operation was carried out correctly.

- D (Dump / Display): With this command we can view the information from a desired offset of a desired segment of memory. If we wish, we can also limit the area we want to see.

### Ex

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

Here, the portion of the data segment starting from offset 0000H is shown. If no range is given, it shows 128 bytes. After giving the memory dump in hexadecimal, the corresponding displayable ASCII characters are also shown alongside.

### Ex

```
-D DS:100,115
2AF2:0100 8B 24 17 5A 18 BA 4A 29-A2 4F F6 C9 07 AE 07 09 .$.Z..J).O......
2AF2:0110 20 8C 07 BA 4F 80                    ...O.
```

-

- M (Move) : It is used to move a block of information from one place to another

### Ex

### - M DS:100,110,CS:500

With this command, the information between DS:100H and DS:110H will be placed starting from address CS:500H.

- C (Compare) : It is a command used to compare the information in specified ranges.

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
```

```
2AF2:0110 AB FF 2AF2:0020
```

This command compares the information at addresses 100H-110H with the information starting at address 10H and lists those that differ.

### -C 100,110,100

-

It compares the contents at 100H-110H with the contents at 100H again. Since no difference is found, no information appears on the screen.

S (Search) : Searches for a given value in the desired address range of the memory region. If it finds a result, it is displayed on the screen as an address.

### Ex

### -S CS:100,110,65

It searches for the value 65 between offsets 0100 and 0110.

## calisma-704

### CS:BX 15000

### CS:IP 16000

### SS:BP 15470

```
-r
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0100 OV DN DI NG NZ NA PO CY
1600:0100 0000      ADD [BX+SI],AL                     DS:0000=00
-f DS:10 1f 23
-d DS:10
1500:0010 23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23 ################
1500:0020 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0030 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0040 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0050 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0060 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0070 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0080 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-m 15 29 cs:100

```
-d cs:100
1600:0100 23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00 ###########.....
1600:0110 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0120 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0130 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0140 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0150 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0160 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0170 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-1500:0010 23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23 ################

```
1500:0020 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0030 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0040 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0050 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0060 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0070 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1500:0080 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-m 15 29 cs:100

```
-d cs:100
1600:0100 23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00 ###########.....
1600:0110 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0120 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0130 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0140 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0150 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0160 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
1600:0170 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
```

-s ds:0000 0100 86 -s ds:0000 0100 ff

```
1500:00F9
```

-c ds:15 29 cs:100 -c ds:15 34 cs:0100 -c ds:0015 0034 cs:0100 --a 100

```
1600:0100 MOV AX,00
1600:0103 MOV BX,AX
1600:0105 MOV CX,12
1600:0108 MOV DX,0101
1600:010B OR CX,AX
1600:010D OR AX,CX
1600:010F ADD BX,AX
1600:0111 SUB AX,BX
1600:0113 ROL DX,1
1600:0115 ROR DX,1
1600:0117 ROR DX,1
1600:0119 NOT DX
1600:011B
```

```
-u
1600:0100 B80000    MOV AX,0000
1600:0103 89C3     MOV BX,AX
1600:0105 B91200    MOV CX,0012
1600:0108 BA0101    MOV DX,0101
1600:010B 09C1     OR  CX,AX
1600:010D 09C8     OR  AX,CX
1600:010F 01C3     ADD BX,AX
1600:0111 29D8     SUB AX,BX
1600:0113 D1C2     ROL DX,1
1600:0115 D1CA      ROR DX,1
1600:0117 D1CA      ROR DX,1
1600:0119 F7D2     NOT DX
1600:011B 0000     ADD [BX+SI],AL
1600:011D 0000     ADD [BX+SI],AL
1600:011F 0000     ADD [BX+SI],AL
```

-

```
1600:0117 ROR DX,1
1600:0119 NOT DX
1600:011B
-t
```

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0103 OV DN DI NG NZ NA PO CY
1600:0103 89C3   MOV BX,AX
```

-

```
-t
```

```
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0105 OV DN DI NG NZ NA PO CY
1600:0105 B91200  MOV CX,0012
```

```
-t
```

```
AX=0000 BX=0000 CX=0012 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0108 OV DN DI NG NZ NA PO CY
1600:0108 BA0101  MOV DX,0101
-t
```

```
AX=0000 BX=0000 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=010B OV DN DI NG NZ NA PO CY
1600:010B 09C1   OR    CX,AX
-t
```

```
AX=0000 BX=0000 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=010D NV DN DI PL NZ NA PE NC
1600:010D 09C8    OR   AX,CX
```

--t

```
AX=0012 BX=0000 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=010F NV DN DI PL NZ NA PE NC
1600:010F 01C3   ADD BX,AX
-t
```

```
AX=0012 BX=0012 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0111 NV DN DI PL NZ NA PE NC
1600:0111 29D8   SUB AX,BX
-t
```

```
AX=0000 BX=0012 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0113 NV DN DI PL ZR NA PE NC
1600:0113 D1C2    ROL DX,1
-t
```

```
AX=0000 BX=0012 CX=0012 DX=0202 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0115 NV DN DI PL ZR NA PE NC
1600:0115 D1CA    ROR DX,1
```

--t

```
AX=0000 BX=0012 CX=0012 DX=0101 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0117 NV DN DI PL ZR NA PE NC
1600:0117 D1CA    ROR DX,1
-t
```

```
AX=0000 BX=0012 CX=0012 DX=8080 SP=FFEE BP=0000 SI=0000 DI=0000
DS=1500 ES=1547 SS=1547 CS=1600 IP=0119 OV DN DI PL ZR NA PE CY
1600:0119 F7D2   NOT DX
```

## lab1_report(1)

### QUESTION 1 

### - When we ran the 2-line program, the screen showed

```
AX=0200 BX=0000 CX=0000 DX=0043 SP=FFEE BP=0000 SI=0000 DI=0000
DS=152D ES=152D SS=152D CS=152D IP=0100 NV UP EI PL NZ NA PO NC
152D:0100 CD21   INT 21
```

### - I entered the g 104 command

### “C:\>

### C

Program terminated normally

```
C:\>“
```

Here, int 21 is the command for printing text, and int 20 is the command for terminating the program. Thanks to the int 21 command, we see that the value 43 we loaded into the DX register corresponds to the ASCII code of the letter C.

### QUESTION 2 

When I ran the TEMP.COM file, the screen showed

```
C:\>temp.com
```

*

```
C:\>
```

As can be understood from this, this file prints * to the screen.

### QUESTION 3 

a 100

```
152D:0100 mov ah,02      (AX->AH 02)
152D:0102 mov dl,2a      (DX ->DL2a)
152D:0104 int 21
152D:0106 int 20
```

n temp.com (Parameter list) r bx         (bx ?)

### BX 0000

:0 r cx              (cx ?)

### CX 0000

:08 w     (write command) 00008 bytes are written q     (exit the program)

### QUESTION 4 

We learned about the 8086 registers and the Debug commands, and we learned how to run the Debug program and perform operations in it. Using Debug commands, we learned how to change the contents of the registers whose locations are shown on the screen and how to perform operations with their help, and we learned how to obtain, in the DOS environment, the output of a Debug program that we wrote in WordPad.

## lab1_report

### QUESTION 1 

### - Screen output when we ran the 2-line program

```
AX=0200 BX=0000 CX=0000 DX=0043 SP=FFEE BP=0000 SI=0000 DI=0000
DS=0C81 ES=0C81 SS=0C81 CS=0C81 IP=0100 NV UP EI PL NZ NA PO NC
0C81:0100 CD21   INT 21
```

### - When we used the g 104 command, the screen showed

### “C

Program terminated normally “ Here, int 21 is the command for printing text, and int 20 is the command for terminating the program. Thanks to the int 21 command, we see that the value 43 we loaded into the DX register corresponds to the ASCII code of the letter C.

### QUESTION 2 

The TEMP.COM file displayed the * character on the screen as its output.

### QUESTION 3 

a 100

```asm
mov ah,02    (write 02 into the high part of the AX register)
mov dl,2a    (write 2a into the low part of the DX register)
int 21
int 20
```

n temp.com (Parameter list) r bx         (change the contents of the bx register) r cx          (change the contents of the cx register) w     (write command) q     (exit the program)

### QUESTION 4 

We learned about the 8086 registers and learned the Debug commands. We learned how to perform arithmetic operations in Debug, how to view and change the functions of the registers, and how to carry out the operations we want on them.

## lab2_prelab

### R Register Command

The command is used to view or change the values of the CPU registers. The usage of the R command is given below. - R Register Name The command performs 3 different tasks related to the use of registers. R: If the command is used alone, all the current values of the CPU registers are shown. Besides the registers, the command also shows the values of the Flag register symbolically. At the end of the command, the instruction pointed to by CS:IP is also displayed on the screen. After using the R command, a display similar to the following is obtained.

```
-R
AX=0000 BX=0000 CX=0000 DX=0000 SP=FFEE BP=0000 SI=0000 DI=0000
DS=2054 ES=2054 SS=2054 CS=2054 IP =0100 NV UP EI PL NZ NA PO NC
2054:0100 IE PUSH DS
```

If the letter F is used as a parameter after the R command, the program displays the current flags so that they can be changed and waits for you to change the flags you want. In this case, you can set or reset any flag you want.

### -RF

### NV UP EI PL NZ NA PO NC - ZRUP

- In the example above, the Zero flag is SET and the direction flag is RESET. With the R command, not only the flags but the values of all registers can be changed. To do this, the name of the register to be changed must be typed after the R command. When this is done, the current value of the register is printed on the screen, and the new value of the register is asked for by placing a colon ( : ). The value must be given next to this mark as 4 hexadecimal digits. If no value is given and the Enter key is pressed, the contents of the register will not be changed.

### T Trace Command 

The Trace command is used to execute the lines of a program in memory one by one or a certain portion of them. The usage of the command is given below. - T=Address Value The parameters of the command are optional. The first parameter is the Address parameter; if this parameter is to be used, the = sign must be used after the command. The Address parameter is taken as the address of the first instruction to be executed. The Value parameter indicates how many instructions will be executed consecutively. If it is not used, this value is taken as 1. If no parameter is used, 1 instruction is executed starting from the location addressed by CS:IP, and after the instruction is executed, the register values and the instruction to be executed next are displayed on the screen.

### U Unassemble Command 

The U command is used to list the machine language and assembly equivalents of the program in memory on the screen. The usage of the command is given below. - U Address1 Address2 The Address1 parameter given indicates the start address of the program to be listed. This

```asm
address can be given as segment and offset. When giving this address, care must be taken not to split any instruction
```

in the middle. Otherwise, the list displayed on the screen will be a meaningless list. The second parameter given determines the end of the listing. The address given here must be an offset. The segment will be taken as the segment address specified in Address1.

### A Assemble Command 

The A command is used to write assembly programs. The usage of this command is: -- A [segment:offset]. The address, which is the parameter of the command, indicates where in memory the program to be written will be placed. The parameter is optional. If it is not given, the current values of CS and IP are assumed as the parameter of the command. After the command, you may give no parameter at all, or you may give only the offset address. If only a single number is given after the command, the given value is taken as the offset, and by assigning this value to the IP register, the program is written at the default segment and the specified offset. When the command is executed, the default or specified segment and offset address is written at the start of a new line, and the command waits for instruction input next to this address. Each time an instruction is entered and the Enter key is pressed, debug first interprets the entered instruction, and if the entered instruction is correct, the segment and offset addresses are increased by the length of the entered instruction and it waits for a new instruction. If the entered instruction is incorrect, the location of the error is shown and it waits at the same segment and offset addresses for the instruction to be entered again. If Enter is pressed on a line without entering an instruction, debug returns to the command line.

- D (Dump / Display): With this command we can view the information of the memory from any offset of any segment we want. If we wish, we can also limit the area we want to see. If the address of the range to be displayed is given next to the D command, only the values in the specified address range will be displayed on the screen.

F (Fill): It is used to fill an area of memory whose start and end addresses are specified with a specified number. -

```
-F DS:100,120,AB
```

Using the F command, the part of DS between 100H and 120H will be filled with the value ABH. If we then examine from address DS:100H with the D command, we verify that the operation was performed as intended.

- C (Compare): It is a command used to compare the information in the specified ranges.

```asm
Information in different segments can also be compared.
```

- M (Move): It is used to move a block of information in one place to another place

### - M DS:100,110,CS:500

With this command, the information between DS:100H and DS:110H will be placed starting from address CS:500H.

### Debug: s (search)

Searches an address range for a pattern of one or more byte values. Syntax

s Range List, Parameters Range Required. Specifies the start and end addresses of the range you want to search. List Required. Specifies the pattern of one or more byte values, or a string, that you want to search for.

```asm
Code segment:
```

The part of memory that stores the operators (instructions) is called the code segment, and the start address of this region of memory is held in the CS register. It identifies the beginning of the program instructions. The actual memory address of the next byte to be executed is found by placing the paragraph whose address is specified into the code segment register and adding this value to the instruction pointer (IP).

```asm
Data segment:
```

Likewise, the part where the operands are stored is called the data segment. The start address of this memory region is held in the DS register. It identifies the beginning of the data section of the program. When the compiler encounters a data declaration, it allocates space within the data segment depending on the size of that data. If the data has a specific type, its initial value is placed in memory. Otherwise, its value consists of the content that was there before the start of the program.

### -DS:BX- -DS:SI-

```asm
Extra segment:
```

The memory region used for various purposes (for example, string operations) is called the extra segment, and its address is held in the ES register

### -ES:DI-

```asm
Stack segment:
```

It refers to the region in which stack segments are temporarily held in memory; the SS register indicates the start address of this region

### -SS:SP-

### -SS:BP-

### IP: (Instruction pointer)

It contains the address of the next instruction to be executed. The reason for this is that changing the register would adversely affect the program. The instruction pointer cannot be accessed directly or changed.

## calisma-840

Başkent University, Department of Electrical and Electronics Engineering

EEM 332 – Microprocessors Laboratory

Pre-lab/Report

Experiment No: # 2 Experiment Title: Basic Debug and Assembler (Assembly) Commands Experiment Date: 10/03/2006

### 2)

### DS: 15000

### CS: 16100

### SS: 13A50

### 8)

Number of Bytes

```asm
MOV AX,00       B80000     3
MOV AX,BX       89C3       2
MOV CX,12       B91200     3
MOV DX,0101     BA0101     3
OR CX,AX        09C1       2
OR AX,CX        09C8       2
ADD BX,AX       01C3       2
SUB AX,BX       29D8       2
ROL DX,1         D1C2       2
ROR DX,1         D1CA       2
ROR DX,1         D1CA       2
NOT DX           F7D2      2
```

### 9)

```asm
MOV AX,00:AX=0000 BX=0000 CX=0000 DX=0000
```

```asm
MOV AX,BX: AX=0000 BX=0000 CX=0000 DX=0000
```

```asm
MOV CX ,12: AX=0000 BX=0000 CX=0012 DX=0000
```

```asm
MOV DX,0101: AX=0000 BX=0000 CX=0012 DX=0101
```

```asm
OR CX,AX:AX=0000 BX=0000 CX=0012 DX=0101
```

```asm
OR AX,CX:AX=0012 BX=0000 CX=0012 DX=0101
```

```asm
ADD BX,AX: AX=0012 BX=0012 CX=0012 DX=0101
```

```asm
SUB AX,BX:AX=0000 BX=0012 CX=0012 DX=0101
```

```asm
ROL DX,1: AX=0000 BX=0012 CX=0012 DX=0202
```

```asm
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=0101
```

```asm
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=8080
```

```asm
NOT DX: AX=0000 BX=0012 CX=0012 DX=7F7F
```

## report_2

### 2)

### DS:BX 15000

### CS:IP 16100

### SS:BP 15050

### 8)

```asm
MOV AX,00       B80000   3
MOV AX,BX       89C3     2
MOV CX,12       B91200   3
MOV DX,0101     BA0101   3
OR CX,AX        09C1     2
OR AX,CX        09C8     2
ADD BX,AX       01C3     2
SUB AX,BX       29D8     2
ROL DX,1         D1C2     2
ROR DX,1         D1CA     2
ROR DX,1         D1CA     2
NOT DX           F7D2    2
```

### 9)

```asm
MOV AX,00:AX=0000 BX=0000 CX=0000 DX=0000
MOV AX,BX: AX=0000 BX=0000 CX=0000 DX=0000
MOV CX ,12: AX=0000 BX=0000 CX=0012 DX=0000
MOV DX,0101: AX=0000 BX=0000 CX=0012 DX=0101
OR CX,AX:AX=0000 BX=0000 CX=0012 DX=0101
OR AX,CX:AX=0012 BX=0000 CX=0012 DX=0101
ADD BX,AX: AX=0012 BX=0012 CX=0012 DX=0101
SUB AX,BX:AX=0000 BX=0012 CX=0012 DX=0101
ROL DX,1: AX=0000 BX=0012 CX=0012 DX=0202
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=0101
ROR DX,1: AX=0000 BX=0012 CX=0012 DX=8080
NOT DX: AX=0000 BX=0012 CX=0012 DX=7F7F
```

## calisma-1259

### EEM332-MICROPROCESSORS

Experiment Number: 2 Experiment Title: Basic DEBUG and Assembler (Assembly) Commands

### PRE-LAB

1-) Explain how the segment registers and the Instruction Pointer (IP) are used. Although the 8086 processor has 20 address pins, its largest register is 16 bits. With the value in a single register, it can address only a 64 KB area. In this case, the segmented memory access structure was devised in order to make use of the 1 MB of memory that can be addressed with 20 address pins. In the 8086 family, main memory is divided into 64 KB areas, each starting from an even address. Basically there are 4 types of segments. Accessing any segment is possible only by using the segment register of that area. These basic segment registers are called CS, SS, DS and ES. The data within a segment is reached with intra-segment pointers (IP). Intra-segment pointers are values called relative positions (offsets), which determine the distance from the start of the segment.

2-) Explain the DEBUG commands written in CAPITAL letters that you saw in the experimental work section.

a-) REGISTER Command: This command is used to determine the current register values and the state of the flags. With the help of this command, the desired values (provided they are hexadecimal) can be given to the registers.

b-) FILL Command : It is used to fill an area of memory whose start and end addresses are specified with a specified number.

c-) DUMP Command : With this command we can view the information of the memory from any offset of any segment we want. If we wish, we can also limit the area we want to see. If the address of the range to be displayed is given next to the D command, only the values in the specified address range will be displayed on the screen.

d-) MOVE Command : It is used to move a block of information in one place to another place

### e-) SEARCH Command 

f-) COMPARE Command : It is a command used to compare the information in the specified ranges. Information in different segments can also be compared.

g-) ASSEMBLE Command : This command makes it possible to write simple programs with the help of Debug. Programs written inside Debug start from offset address 100H, as in programs with the COM extension. For this reason, when the program is to be run, the value of the IP register must be set to 100H with the R command.

h-) UNASSEMBLE Command : It is a command used to translate the machine code written in CS into mnemonics in a form the user can understand. Each time it is called, it shows the user the mnemonics of 32 bytes of machine code.

ı-) TRACE Command : The written assembly instructions are executed one by one, and the values taken by the registers and flags are displayed on the screen at the end of the operation. The T command starts running from the point indicated by IP and stops after each instruction is executed. If the user wishes, a number can also be given next to the T command. In this case, the given number of instruction lines are executed back to back, and the register and flag values are written to the screen each time.

## ucs-eem332 lab prelab 2

### 1) The segment registers are all 16 bits and are used to address the part of memory called a segment.

```asm
Code Segment Register (CS) : In the MS-DOS operating system, the codes that make up programs
are loaded into the Code Segment. That is, the instructions are stored in the Code Segment registers. These codes
```

are found with the help of the Instruction Pointer (IP). IP stores the address information of the instruction to be executed. Thus, when IP points to the CS to be processed, the instructions there are executed.

```asm
Stack Segment Register (SS) : Programs use a memory area called the Stack Segment (SS)
```

as a temporary storage area. For example, when a branch or an interrupt occurs, the

```asm
information at that moment is saved to SS. These stacks work with the "Last In First Out" technique. The Stack
```

Pointer (SP) holds the address of SS. After the program performs the required interrupt, the files in SS are popped off with the help of SP. The program continues from where it left off.

```asm
Data Segment Register (DS) : The data to be used in a program of the .exe type is kept in the Data
```

Segment. The start address of the data section of the program is kept in DS.

```asm
Extra Segment Register (ES) : The memory area used in various string operations is called the Extra
```

Segment. This memory address is kept in DI and ES.

Instruction Pointer (IP) : It holds the offset address of the instruction following the one currently being executed. It is incremented by 1 by the microprocessor after each code operation, and the process continues in this way. It is possible to change the value of this register indirectly, with the information on the stack.

### 2)

REGISTER : This command is used to view and change the registers used by the CPU. If all registers are to be displayed, a result like the following is obtained;

```
-R
```

```
AX=0000 BX=0000 CX=0000 DP=0000 SP=FFEE BP=0000 SI=0000 DI=0000
```

```
DS=1787      ES=1787     SS=1787    CS=1787     IP=0100     NV UP EI PL NZ NA PO NC
```

```
1787:01000 0000                      ADD [BX+SI], AL
```

If it is for a register to be changed;

```
-R AX
```

### AX 0000

: 0200         it goes like this.

FILL : The F command is used to fill a memory region we specify with data we enter. Its usage is as follows;

```
-F DS:100,110,AB       When this is done, the DS addresses 100 – 110 are filled with AB.
```

DUMP : It is used to show the desired portion of a memory region.

```
-When the D command is entered, the 128 bytes following the last displayed memory region are displayed.
```

To narrow this area;

```
-D (offset) is entered. Thus the start address is taken as the offset and the following 128 bytes are
```

displayed.

```
-When the D (start) (end) command is entered, only the region between the specified points is displayed.
```

MOVE : With the help of this command, we can move a certain region to another place in memory. The command can be used as follows;

- M DS:100,110,CS:500            With this command, the region of DS between 100-110 is moved to CS:500.

SEARCH : It searches for the desired data in a memory region. The following code fragment can be used for this;

-S (start) (end) (list)

COMPARE : It is used to compare the data within two specified ranges.

-C 100,110,10 When this is entered, the data at addresses 100-110 are compared with the information starting from address 10 and the differing ones are listed. If the data are the same, nothing is written to the screen.

ASSEMBLE : With this code, code can be written in Assembly language.

- A [segment:offset] Code can be written in Assembly language in this form.

UNASSEMBLE : With this code, code written in Assembly language is translated into machine language. Thus programs can be written in machine language without using a separate compiler

### Its usage is as follows

```
-U (start) (end)
```

These start and end addresses can be given as segment or offset. The point to note here is that, when selecting the start and end points, a piece of code must be taken without being split.

TRACE : It is used to run a desired portion of the instructions in memory. We can do this one by one or as a whole. That is;

```
-T (number of steps) When this code is entered, the number of instructions entered are executed.
```

```
-T (start) (number of steps) When this code is entered, the number of steps after the start address
```

of instructions are executed.

## calisma-834

```asm
		.MODEL SMALL
		.STACK 64
		.DATA
		ORG 0010H			
		SIGN_DATA DB 69,87,96,45,75		;place data definitions here
		;
		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX		;assign value to DS
		;
		MOV CX,5;place code here	
		MOV BX,OFFSET SIGN_DATA	
		SUB AL,AL
AGAIN:		CMP AL,[BX]
		JA NEXT 
		MOV AL,[BX]
NEXT:		INC BX
		LOOP AGAIN
		MOV BX,10H
		MOV AH,02H
		MOV DL,[BX]
		INT 21H	
		;		
		MOV	AH,4CH	;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END	MAIN		;this is the program exit point
```

## calisma-1231

```
Umut [personal information removed] Sağdıçoğlu
[personal information removed]
Experiment 2
21.03.2011


Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\calisma>debug
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1524  ES=1524  SS=1524  CS=1524  IP=0100   NV UP EI PL NZ NA PO NC
1524:0100 0000          ADD     [BX+SI],AL                         DS:0000=CD
-r ip
IP 0100
:
-r ds
DS 1524
:1500
-r cs
CS 1524
:1600
-r f
NV UP EI PL NZ NA PO NC  -nv pe
-f ds:10,1f,23
-d ds:00,3f
1500:0000  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0010  23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23   ################
1500:0020  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0030  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
-m ds:15,22,cs:100
-d cs:100
1600:0100  23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00   ###########.....
1600:0110  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0120  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0130  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0140  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0150  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0160  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1600:0170  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
-s ds:00,100,86
-s ds:00,100,ff
-c ds:15,22,cs:100
-c ds:15,2e,cs:100
-a cs:200
1600:0200 MOV AX,00
1600:0203 MOV BX,AX
1600:0205 MOV CX,12
1600:0208 MOV DX,0101
1600:020B OR CX,AX
1600:020D OR AX,CX
1600:020F ADD BX,AX
1600:0211 SUB AX,BX
1600:0213 ROL DX,1
1600:0215 ROR DX,1
1600:0217 ROR DX,1
1600:0219 NOT DX
1600:021B
-u cs:200
1600:0200 B80000        MOV     AX,0000
1600:0203 89C3          MOV     BX,AX
1600:0205 B91200        MOV     CX,0012
1600:0208 BA0101        MOV     DX,0101
1600:020B 09C1          OR      CX,AX
1600:020D 09C8          OR      AX,CX
1600:020F 01C3          ADD     BX,AX
1600:0211 29D8          SUB     AX,BX
1600:0213 D1C2          ROL     DX,1
1600:0215 D1CA          ROR     DX,1
1600:0217 D1CA          ROR     DX,1
1600:0219 F7D2          NOT     DX
1600:021B 0000          ADD     [BX+SI],AL
1600:021D 0000          ADD     [BX+SI],AL
1600:021F 0000          ADD     [BX+SI],AL
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0100   NV UP EI PL NZ NA PE NC
1600:0100 2323          AND     SP,[BP+DI]                         SS:0000=20CD
-r ip
IP 0100
:200
-t

AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0203   NV UP EI PL NZ NA PE NC
1600:0203 89C3          MOV     BX,AX
-t

AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0205   NV UP EI PL NZ NA PE NC
1600:0205 B91200        MOV     CX,0012
-t

AX=0000  BX=0000  CX=0012  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0208   NV UP EI PL NZ NA PE NC
1600:0208 BA0101        MOV     DX,0101
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=020B   NV UP EI PL NZ NA PE NC
1600:020B 09C1          OR      CX,AX
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=020D   NV UP EI PL NZ NA PE NC
1600:020D 09C8          OR      AX,CX
-t

AX=0012  BX=0000  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=020F   NV UP EI PL NZ NA PE NC
1600:020F 01C3          ADD     BX,AX
-t

AX=0012  BX=0012  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0211   NV UP EI PL NZ NA PE NC
1600:0211 29D8          SUB     AX,BX
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0213   NV UP EI PL ZR NA PE NC
1600:0213 D1C2          ROL     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0202  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0215   NV UP EI PL ZR NA PE NC
1600:0215 D1CA          ROR     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0217   NV UP EI PL ZR NA PE NC
1600:0217 D1CA          ROR     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=8080  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=0219   OV UP EI PL ZR NA PE CY
1600:0219 F7D2          NOT     DX
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=1524  SS=1524  CS=1600  IP=021B   OV UP EI PL ZR NA PE CY
1600:021B 0000          ADD     [BX+SI],AL                         DS:0012=23


-u 200
1600:0200 B80000        MOV     AX,0000      3 byte
1600:0203 89C3          MOV     BX,AX	     2 byte	
1600:0205 B91200        MOV     CX,0012	     3 byte
1600:0208 BA0101        MOV     DX,0101	     3 byte
1600:020B 09C1          OR      CX,AX        2 byte
1600:020D 09C8          OR      AX,CX        2 byte
1600:020F 01C3          ADD     BX,AX        2 byte
1600:0211 29D8          SUB     AX,BX        2 byte
1600:0213 D1C2          ROL     DX,1         2 byte
1600:0215 D1CA          ROR     DX,1         2 byte
1600:0217 D1CA          ROR     DX,1         2 byte
1600:0219 F7D2          NOT     DX           2 byte
1600:021B 0000          ADD     [BX+SI],AL   
1600:021D 0000          ADD     [BX+SI],AL
1600:021F 0000          ADD     [BX+SI],AL


///EXPERIMENT 2 WORKSHEET\\\

Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\calisma>debug
-a
1524:0100 MOV AX,BX
1524:0102 MOV AX,AAAA
1524:0105 MOV AX,[BX]
1524:0107 MOV AX,[0004]
1524:010A MOV AX,[BX+SI]
1524:010C MOV AX,[SI]+[0004]
1524:010F MOV AX,[BX][SI]+[0004]
1524:0112
-u 100
1524:0100 89D8          MOV     AX,BX
1524:0102 B8AAAA        MOV     AX,AAAA
1524:0105 8B07          MOV     AX,[BX]
1524:0107 A10400        MOV     AX,[0004]
1524:010A 8B00          MOV     AX,[BX+SI]
1524:010C 8B4404        MOV     AX,[SI+04]
1524:010F 8B4004        MOV     AX,[BX+SI+04]
1524:0112 0000          ADD     [BX+SI],AL
1524:0114 0000          ADD     [BX+SI],AL
1524:0116 0000          ADD     [BX+SI],AL
1524:0118 0000          ADD     [BX+SI],AL
1524:011A 0000          ADD     [BX+SI],AL
1524:011C 3400          XOR     AL,00
1524:011E 1315          ADC     DX,[DI]

-r ds
DS 1524
:200
-r cs
CS 1524
:100
-f ds:1234,1234,ED
-f ds:1235,1235,BE
-f ds:1236,1236,CD
-f ds:1237,1237,AB
-r SI
SI 0000
:1236
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0100   NV UP EI PL NZ NA PO NC
0100:0100 0000          ADD     [BX+SI],AL                         DS:1236=CD
-a 00
0100:0000 MOV AX,1234
0100:0003 MOV BX,[1234]
0100:0007 MOV CX,[SI]
0100:0009
-r ip
IP 0100
:0000
-t

AX=1234  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0003   NV UP EI PL NZ NA PO NC
0100:0003 8B1E3412      MOV     BX,[1234]                          DS:1234=BEED
-t

AX=1234  BX=BEED  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0007   NV UP EI PL NZ NA PO NC
0100:0007 8B0C          MOV     CX,[SI]                            DS:1236=ABCD
-t

AX=1234  BX=BEED  CX=ABCD  DX=0000  SP=FFEE  BP=0000  SI=1236  DI=0000
DS=0200  ES=1524  SS=1524  CS=0100  IP=0009   NV UP EI PL NZ NA PO NC
0100:0009 0000          ADD     [BX+SI],AL                         DS:D123=85
```

## fig2-2

```asm
;THE FORM OF AN ASSEMBLY LANGUAGE PROGRAM
 USING SIMPLIFIED SEGMENT DEFINITION
		.MODEL SMALL
		.STACK 64
		.DATA
		;
		;place data definitions here
		;
		.CODE
MAIN		PROC	FAR		;this is the program entry point
		MOV	AX,@DATA	;load the data segment address
		MOV	DS,AX		;assign value to DS
		;
		;place code here	
		;	
		MOV	AH,4CH	;set up to
		INT	21H		;return to DOS
MAIN		ENDP			
		END	MAIN		;this is the program exit point
```

## 2010 laboratory 2 experimental work template

The DEBUG session in the template demonstrates register setting, physical address, fill, move, search and compare operations.

```
Parts A, b, c, d, e

-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=13B6  ES=13B6  SS=13B6  CS=13B6  IP=0100   NV UP EI PL NZ NA PO NC
13B6:0100 0000          ADD     [BX+SI],AL                         DS:0000=CD

-r ip
IP 0100
:100
-r ds
DS 13B6
:1500
-r cs
CS 13B6
:1600
-r f
NV UP EI PL NZ NA PO NC  -nv pe
-r
AX=0000  BX=0000  CX=0000  DX=0000  SP=FFEE  BP=0000  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=1600  IP=0100   NV UP EI PL NZ NA PE NC
1600:0100 0000          ADD     [BX+SI],AL                         DS:0000=00


 To write the effective address, we shift the first register left by 4 bits and add the second one. Accordingly;

DS:BX = 15000
CS:IP = 16100
SS:BP = 13B60

3)

-f ds:10,1f,23

4)
-d ds:00,3f
1500:0000  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0010  23 23 23 23 23 23 23 23-23 23 23 23 23 23 23 23   ################
1500:0020  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0030  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................

5)
-m ds:15,28,cs:100
-d ds:100
1500:0100  23 23 23 23 23 23 23 23-23 23 23 00 00 00 00 00   ................
1500:0110  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0120  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0130  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0140  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0150  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
1500:0160  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00   ................
6) 
-s ds:0000 0100 86
-s ds:0000 0100 ff
With the commands above, I searched for 86 and ff in the addresses between 00 and 100.
Since it found no match, nothing was displayed on the screen.

7)

I carried out parts a and b by entering the following commands.
-c 15,28,100
-c 15,34,100

However, since I had previously moved the data starting at ds:15 to the storage locations starting at cs:100, and since everything outside the relevant storage regions contains “00”, it could not find any differing value and displayed no result.

If I had used the compare command as follows, it would have produced a result.

-c 30,36,100
1500:0030  00  23  1500:0100
1500:0031  00  23  1500:0101
1500:0032  00  23  1500:0102
1500:0033  00  23  1500:0103
1500:0034  00  23  1500:0104
1500:0035  00  23  1500:0105
1500:0036  00  23  1500:0106

Here, since the address starting at c:30 holds 00 and the address starting at c:100 holds 23, it displayed the difference on the screen.


8)

-a
13B6:0100 mov ax,00
13B6:0103 mov bx,ax
13B6:0105 mov cx,12
13B6:0108 mov dx,0101
13B6:010B or cx,ax
13B6:010D or ax,cx
13B6:010F add bx,ax
13B6:0111 sub ax,bx
13B6:0113 rol dx,1
13B6:0115 ror dx,1
13B6:0117 ror dx,1
13B6:0119 not dx
13B6:011B

-u 13b6:0100
13B6:0100 B80000        MOV     AX,0000
13B6:0103 89C3          MOV     BX,AX
13B6:0105 B91200        MOV     CX,0012
13B6:0108 BA0101        MOV     DX,0101
13B6:010B 09C1          OR      CX,AX
13B6:010D 09C8          OR      AX,CX
13B6:010F 01C3          ADD     BX,AX
13B6:0111 29D8          SUB     AX,BX
13B6:0113 D1C2          ROL     DX,1
13B6:0115 D1CA          ROR     DX,1
13B6:0117 D1CA          ROR     DX,1
13B6:0119 F7D2          NOT     DX
13B6:011B 0034          ADD     [SI],DH
13B6:011D 00A51300      ADD     [DI+0013],AH


9) Since I entered the a command in the previous question without giving an address, it started writing from address cs:13b6:0100. For this reason, I changed the CS value, which was 1600, with

-r cs
CS 1600
:13B6 
and then ran the code.

AX=0000  BX=0000  CX=0000  DX=0000  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0103   NV UP EI PL ZR NA PE NC
13B6:0103 89C3          MOV     BX,AX
-t

AX=0000  BX=0000  CX=0000  DX=0000  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0105   NV UP EI PL ZR NA PE NC
13B6:0105 B91200        MOV     CX,0012
-t

AX=0000  BX=0000  CX=0012  DX=0000  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0108   NV UP EI PL ZR NA PE NC
13B6:0108 BA0101        MOV     DX,0101
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=010B   NV UP EI PL ZR NA PE NC
13B6:010B 09C1          OR      CX,AX
-t

AX=0000  BX=0000  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=010D   NV UP EI PL NZ NA PE NC
13B6:010D 09C8          OR      AX,CX


AX=0012  BX=0000  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=010F   NV UP EI PL NZ NA PE NC
13B6:010F 01C3          ADD     BX,AX
-t

AX=0012  BX=0012  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0111   NV UP EI PL NZ NA PE NC
13B6:0111 29D8          SUB     AX,BX
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0113   NV UP EI PL ZR NA PE NC
13B6:0113 D1C2          ROL     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0202  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0115   NV UP EI PL ZR NA PE NC
13B6:0115 D1CA          ROR     DX,1
-t

AX=0000  BX=0012  CX=0012  DX=0101  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0117   NV UP EI PL ZR NA PE NC
13B6:0117 D1CA          ROR     DX,1
-

AX=0000  BX=0012  CX=0012  DX=8080  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0119   OV UP EI PL ZR NA PE CY
13B6:0119 F7D2          NOT     DX
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=011B   OV UP EI PL ZR NA PE CY
13B6:011B 0034          ADD     [SI],DH                            DS:0000=00
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=011D   NV UP EI PL NZ NA PO NC
13B6:011D 00A51300      ADD     [DI+0013],AH                       DS:0013=23
-t

AX=0000  BX=0012  CX=0012  DX=7F7F  SP=5DB7  BP=20CA  SI=0000  DI=0000
DS=1500  ES=13B6  SS=13B6  CS=13B6  IP=0121   NV UP EI PL NZ NA PO NC
13B6:0121 0000          ADD     [BX+SI],AL                         DS:0012=23
```

*Note: Since no prepared PDF version of the .dot file was available, the text was extracted from the text table of the original Word file. A metadata-free TXT dump was included in the download package. The expression "effective address" in the source describes the physical address in the calculations given.*
