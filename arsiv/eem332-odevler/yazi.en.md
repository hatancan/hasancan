---
baslik: EEM332 Microprocessors: 8086 Assignments and Study Questions
ozet: 2004 and 2005 assignment groups, instruction encoding, addressing, hardware, and program tracing questions.
---

This post brings together the related notes and exercises from the Başkent University **EEM332 Microprocessors** course archive (2004–2006). It covers the 2004 and 2005 assignment groups, instruction encoding, addressing, hardware, and program tracing questions. PDF archive copies of the documents and, where available, source code can be downloaded as a ZIP at the end of the post.

## EEM%20332%20odev11

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 1/Group 1

IMPORTANT INFORMATION:        -You may submit the assignments to office C302-B by 17:00 on Tuesday, 29 March 2004. -Prepare your assignments on white A4 paper, indicating your group, and submit them stapled at a corner if necessary (plastic sleeve folders will not be accepted). -Answer only the questions belonging to the group in which your name appears. You can find the group list on the web page. -If you answer questions that do not belong to your own group, your assignment grade will be evaluated as zero.

### 1) State which of the instructions given below can and cannot be coded with 8086/88 Assembly

instructions. If any cannot be coded, explain why.

a.MOV AX,27              g.MOV DS,9BF2 b.MOV AL,97F             h.MOV CX,397 c.MOV CS,3490            i.MOV AX,23FB9 d.MOV BX,CS              j.MOV AX,DL e.MOV CS,BH              k.MOV CH,AX f.MOV DS,BX              l.MOV SI,9516

### 2) The registers given below are used as offsets. Assuming that the default segments are used to reach the logical

```asm
address, state the segment register each offset
```

register is associated with.

(a) BP     (b) DI    (c) IP   (d) SI     (e) SP       (f) BX

### 3) Find the CF, PF, AF, ZF and SF states for the operations given below.

a. MOV BL,9FH        b. MOV AL,23H             c. MOV DX,10FFH

```asm
ADD BL,61H           ADD AL,97H                ADD DX,1
```

### 4) CS=1000, DS=2000, SS=3000, SI=4000, DI=5000, BX=6080, BP=7000,

```
AX=25FF, CX=8791 and DX=1299 are given. For the operations below, state
```

the physical addresses of the memory locations used and the values stored at these addresses.

(a) MOV [SI],AL (b) MOV[SI+BX+8],AH (c) MOV [BX],AX (d) MOV [DI+6],BX (e) MOV [DI][BX]+28,CX (f) MOV[BP][SI]+10,DX (g) MOV [3600],AX (h) MOV[BX]+30,DX (i) MOV [BP]+200,AX

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 1/Group 1 (j) MOV [BP+SI+100],BX (k) MOV [SI]+50,AH (l) MOV [DI+BP+100],AX

### 5) State the addressing modes for the instructions given below.

(a) MOV AX,DS (b) MOV BX,5678H (c) MOV CX,[3000] (d) MOV AL,CH (e) MOV [DI],BX (f) MOV AL,[BX] (g) MOV DX,[BP+DI+4] (h) MOV CX,DS (i) MOV [BP+6],AL (j) MOV AH,[BX+SI+50] (k) MOV BL,[SI]+10 (l) MOV [BP][SI]+12,AX

### 6) After the instructions given below are executed, show the contents of the registers named in the instructions and of

CF, ZF, PF.

a.     MOV AX,6AB3

```asm
MOV BX,98F1
ADD AL,BL
```

ADC AH,BH           ;add with carry

b.   DATA1 DB 4CH

```asm
DATA2 DB 6EH
DATA3 DB ?            ;data3 is empty and located in memory
MOV DH,DATA1          ;data1=4ch
SUB DH,DATA2          ;data2=6eh
JNC NEXT              ;JUMP if not carry
NOT DH                ;1’s complement
INC DH                ;increase one
NEXT:MOV DATA3,DH
```

### 7) Write the assembly code required to perform the operations requested in the questions below. (AL=0FH)

a.     Using the AND instruction, make the contents of AL equal to F0. What should the CF value be in this case? b.     Using the SHL instruction, make the contents of AL equal to F0. What should the CF value be in this case? c.     Using the ROR instruction, make the contents of AL equal to F0. What should the CF value be in this case? d.     Using the STC and SHR instructions, make the contents of AL equal to F0. What should the CF value be in this case?

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 1/Group 1

### 8) After the first three of the instructions given below are executed, what is the Stack Segment, and after the second three are executed, what are the values of the registers? (SP=1245, AX=1122, BX=3344, CX=5566, DX=7788)

### SS:1238

```asm
PUSH AX                SS:1239
PUSH CX                SS:1240
PUSH BX                                              AX
```

### SS:1241

### SS:1243                       BX

```asm
POP DX                 SS:1243                       CX
POP AX                 SS:1244                       DX
POP BX                                               SP
```

### SS:1245

### SP=?

## EEM%20332%20odev12

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 1/Group 2

IMPORTANT INFORMATION:       -You may submit the assignments to office C302-B by 17:00 on Tuesday, 29 March 2004. -Prepare your assignments on white A4 paper, indicating your group, and submit them stapled at a corner if necessary (plastic sleeve folders will not be accepted). -Answer only the questions belonging to the group in which your name appears. You can find the group list on the web page. -If you answer questions that do not belong to your own group, your assignment grade will be evaluated as zero.

### 1) State which of the instructions given below can and cannot be coded with 8086/88 Assembly

instructions. If any cannot be coded, explain why.

a.MOV SI,9516              g.MOV DS,9BF2 b.MOV CX,397               h.MOV AL,97F c.MOV DS,BX                i.MOV CS,3490 d.MOV CH,AX                j.MOV CS,BH e.MOV AX,DL                k.MOV BX,CS f.MOV AX,23FB9             l.MOV AX,27

### 2) The registers given below are used as offsets. Assuming that the default segments are used to reach the logical

```asm
address, state the segment register each offset
```

register is associated with.

(a) BX   (b) SI     (c) IP    (d) DI     (e) SP      (f) BP

### 3) State the addressing modes for the instructions given below.

(a) MOV AX,DS (b) MOV [DI],BX (c) MOV CX,[3000] (d) MOV [BP][SI]+12,AX (e) MOV BX,5678H (f) MOV AL,[BX] (g) MOV [BP+6],AL (h) MOV CX,DS (i) MOV DX,[BP+DI+4] (j) MOV AH,[BX+SI+50] (k) MOV BL,[SI]+10 (l) MOV AL,CH

### 4) CS=2000, DS=3000, SS=4000, SI=1000, DI=5000, BX=8060, BP=7000,

```
AX=FF25, CX=9187 and DX=9912 are given. For the operations below, state
```

the physical addresses of the memory locations used and the values stored at these addresses.

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 1/Group 2 (a) MOV [SI],AL (b) MOV[SI+BX+8],AH (c) MOV [BX],AX (d) MOV [DI+6],BX (e) MOV [DI][BX]+28,CX (f) MOV[BP][SI]+10,DX (g) MOV [3600],AX (h) MOV[BX]+30,DX (i) MOV [BP]+200,AX (j) MOV [BP+SI+100],BX (k) MOV [SI]+50,AH (l) MOV [DI+BP+100],AX

### 5) Find the CF, PF, AF, ZF and SF states for the operations given below.

a. MOV BL,9FH          b. MOV DX,10FFH           c. MOV AL,23H

```asm
ADD BL,61H             ADD DX,1                  ADD AL,97H
```

### 6) After the instructions given below are executed, show the contents of the registers named in the instructions and of

CF, ZF, PF.

a.     MOV AX,6AB3

```asm
MOV BX,F198
ADD AL,BL
```

ADC AH,BH           ;add with carry

b.   DATA1 DB 4CH

```asm
DATA2 DB 6EH
DATA3 DB ?            ;data3 is empty and located in memory
MOV DH,DATA1          ;data1=4ch
SUB DH,DATA2          ;data2=6eh
JNC NEXT              ;JUMP if not carry
NOT DH                ;1’s complement
INC DH                ;increase one
NEXT:MOV DATA3,DH
```

### 7) Write the assembly code required to perform the operations requested in the questions below. (AL=0FH) a.     Using the ROR instruction, make the contents of AL equal to F0. What should the CF value be in this case? b.     Using the STC and SHR instructions, make the contents of AL equal to F0. What should the CF value be in this case? c.     Using the AND instruction, make the contents of AL equal to F0. What should the CF value be in this case? d.     Using the SHL instruction, make the contents of AL equal to F0. What should the CF value be in this case?

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 1/Group 2

### 8) After the first three of the instructions given below are executed, what is the Stack Segment, and after the second three are executed, what are the values of the registers? (SP=1245, AX=8877, BX=6655 CX=4433, DX=2211)

### SS:1238

```asm
PUSH AX                SS:1239
PUSH CX                SS:1240
PUSH BX                                              AX
```

### SS:1241

### SS:1243                       BX

```asm
POP DX                 SS:1243                       CX
POP AX                 SS:1244                       DX
POP BX                                               SP
```

### SS:1245

### SP=?

## EEM332%20odev21

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 2/Group 1

IMPORTANT INFORMATION:       -You may submit the assignments to office C302-B by 17:00 on Friday, 13 May 2005. -Prepare your assignments on white A4 paper, indicating your group, and submit them stapled at a corner if necessary (plastic sleeve folders will not be accepted). -Answer only the questions belonging to the group in which your name appears. You can find the group list on the web page. -If you answer questions that do not belong to your own group, your assignment grade will be evaluated as zero.

### 1) Briefly summarize the ADC section of the 16F877 PIC chip.

Resolution=?, Step size=?, Conversion time=?

### 2) Compare interrupts and polling in I/O operations in terms of their advantages and disadvantages.

### 3) The 8255 and 8253 chips are used in an 8086 processor-based system. To obtain a 300 Hz square wave,

write two separate programs using the 8255 or the 8253.

### 4) In the given port circuit, write the address required for the blank in the OUT ......., AL instruction.

### 5) Rewrite the LED control program based on the temperature given in CPU10 slide 2 so that it works with the PIC

16F877. The temperature will be read digitally from Port C. The output LEDs will be connected to Port B.

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 2/Group 1

### 6) In the given port circuit, write the addresses of the ports and state which port is an input and which

is an output.

### 16) To make the address of Port A 68H, build the decoding circuit for an 8-bit address using

NAND gates in the I/O circuit used for the 8255.

### 17) Find the address of each port in the given circuit.

## EEM332%20odev22

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 2/Group 2

IMPORTANT INFORMATION:       -You may submit the assignments to office C302-B by 17:00 on Friday, 13 May 2005. -Prepare your assignments on white A4 paper, indicating your group, and submit them stapled at a corner if necessary (plastic sleeve folders will not be accepted). -Answer only the questions belonging to the group in which your name appears. You can find the group list on the web page. -If you answer questions that do not belong to your own group, your assignment grade will be evaluated as zero.

### 1) The 8255 and 8253 chips are used in an 8086 processor-based system. To obtain a 250 Hz square wave,

write two separate programs using the 8255 or the 8253.

### 2) Looking at the given port circuit, write the address and instruction required for the blanks.

### ……… AL, ……….

### 3) Rewrite the LED control program based on the temperature given in CPU10 slide 2 so that it works with the PIC

16F84. The temperature will be read digitally from Port B. The output LEDs will be connected to Port A.

### 4) To make the address of Port A 68H, build the decoding circuit for an 8-bit address using NAND

gates in the I/O circuit used for the 8255.

Başkent University Department of Electrical and Electronics Engineering EEM 332 Microprocessors Assignment 2/Group 2

### 5) In the given port circuit, write the addresses of the ports and state which port is an input and

which is an output.

### 6) Find the address of each port in the given circuit. In the figure, the data read from Port A

will be sent to Port B as is, and its complement to Port C.

### 7) Briefly summarize the ADC section of the 16F877 PIC chip.

Resolution=?, Step size=?, Conversion time=?

### 8) Compare interrupts and polling in I/O operations in terms of their advantages and disadvantages.

## q

Başkent University Department of Electrical and Electronics Engineering EEM 332 – Microprocessors

1.1) Answer the following questions.

a. What determines the speed of a microprocessor?

b. Write the difference between ADD AX,BX and ADD AX,[BX].

c. If DS=5010 and PA (physical address)=51950, what is the offset value?

1.2) Which registers do the specified segment registers use as offset registers?

Segment register              CS              DS                  ES              SS ..........      .............       ............   .............

1.3) Mark those of the following registers that can be used as High and Low.

a) CS           b) AX           c) DS           d) SS              e) BX f) DX           g) CX           h) SI              i) DI

1.4) Mark the operations given next to each statement as true (T) or false (F).

```asm
MOV BL,AX
MOV DS,3456H
MOV [3456],[5634]
MOV AX,CS
ADD AX,[BX]+[2345]
MOV CL,5643H
```

Başkent University Department of Electrical and Electronics Engineering EEM 332 – Microprocessors

2.1) After the instructions given below are executed, show the contents of the registers named in the instructions and of CF, ZF, PF.

a.     MOV AX,6AB3

```asm
MOV BX,98F1
ADD AL,BL
```

ADC AH,BH           ;add with carry

b.   DATA1 DB 4CH

```asm
DATA2 DB 6EH
DATA3 DB ?            ;data3 is empty and located in memory
MOV DH,DATA1          ;data1=4ch
SUB DH,DATA2          ;data2=6eh
JNC NEXT              ;JUMP if not carry
NOT DH                ;1’s complement
INC DH                ;increase one
NEXT:MOV DATA3,DH
```

2.2) Complete the code that adds the numbers -2 and -7 and writes the result to the CL register. Show the state of the CL register and of CF, ZF, PF, AF, SF at the end of the code's execution.

```asm
MOV AL,___
MOV CL,___
ADD ___,___
```

2.3) A section of the memory of a CPU-based system is given. According to this, what are the changes resulting from each operation? (DS=0040, SI= 0090h, BP = 0002h) address data a) MOV AX,[SI] 00490h 35 b) MOV AX,[SI+1] 00491h 78 00492h B2            c) MOV AX,[SI][BP] 00493h 9C            d) MOV [SI-BP][3],AX 00494h 0A            e) MOV [94],AX

2.4) Write the assembly code required to perform the operations requested in the questions below. (AL=0FH) a.     Using the AND instruction, make the contents of AL equal to F0. What should the CF value be in this case? b.     Using the SHL instruction, make the contents of AL equal to F0. What should the CF value be in this case? c.     Using the ROR instruction, make the contents of AL equal to F0. What should the CF value be in this case? d.     Using the STC and SHR instructions, make the contents of AL equal to F0. What should the CF value be in this case?

Başkent University Department of Electrical and Electronics Engineering EEM 332 – Microprocessors

2.5) After the first three of the instructions given below are executed, what is the Stack Segment, and after the second three are executed, what are the values of the registers? (SP=1245, AX=1122, BX=3344, CX=5566, DX=7788)

### SS:123E

```asm
PUSH AX                SS:123F                         AX
PUSH CX                SS:1240                         BX
PUSH BX                SS:1241                         CX
```

### SS:1242                         DX

```asm
POP DX                 SS:1243                         SP
POP AX                 SS:1244
POP BX                 SS:1245
```

### SP=?

## ödev1

Başkent University Department of Electrical and Electronics Engineering EEM332 Microprocessors Assignment 1 / Group 2

### 1)

a. CAN BE CODED. b. CAN BE CODED. c. CAN BE CODED. d. 16 bits cannot be transferred to 8 bits. e. 8 bits cannot be partitioned into 16 bits. f. Overflow. 20 bits cannot be transferred to 16 bits. g. A value cannot be assigned directly. h. Overflow. 12 bits cannot be transferred to 8 bits. i. A value cannot be assigned directly. j. 8 bits cannot be partitioned into 16 bits. k. CAN BE CODED. l. CAN BE CODED.

### 2)

a. BX->DS b. SI->DS,ES c. IP->CS d. DI->DS e. SP->SS f. BP->DS

### 3)

a. direct addressing b. c. d. base indexed direct addressing e. implied addressing f. g. base indexed direct addressing h. direct addressing i. base indexed direct addressing j. base indexed direct addressing k. l. direct addressing

*Note: The 2004 assignment sheet states "Tuesday, 29 March 2004"; 29 March 2004 was a Monday. The date has been left as it appears in the source.*
