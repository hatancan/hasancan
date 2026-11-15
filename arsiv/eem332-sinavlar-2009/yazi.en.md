---
baslik: EEM332 Microprocessors: 2009 Midterm and Final Exam Questions
ozet: 8086 instructions, flags, address decoding, 8255, ADC, and PIC questions from 2009 exam photographs.
---

This content from the Başkent University EEM332 Microprocessors course archive was transcribed from photographed pages. It covers 8086 instructions, flags, address decoding, 8255, ADC, and PIC questions from the 2009 exam photographs. Student names and numbers have been removed. The photographs are kept in a private archive; this post has no download file.

## Midterm: Clearing AX

Four different methods are requested:

```asm
MOV AX,00H
AND AX,00H
SUB AX,AX
XOR AX,AX
```

## ADD DL,CH and Flags

| Initial DL | CH | Final DL | OF | SF | CF |
| --- | --- | --- | --- | --- | --- |
| 80H | FEH | 7EH | 1 | 0 | 1 |
| FEH | FBH | F9H | 0 | 1 | 1 |

*Note: The printed answer CF=0 in the second row has been corrected to 1 in red pen in the photograph. Since FEH+FBH=1F9H, there is a carry.*

## Logical Operations

```asm
MOV BH,0A8H
AND BH,3DH
OR BH,0C0H
XOR BH,05H
```

The intermediate values are 28H, E8H, and EDH; the final BH=EDH.

## Assembly Equivalent of a C Loop

The variables in the question are a=16, b=2, c=0; the condition is c<300. In each iteration, a=a*b and c=c+1 are applied. The answer from the source:

```asm
MOV AX,16
MOV BL,2
MOV CX,0
DONGU: MUL BL
       INC CX
       CMP CX,300
       JL DONGU
```

*Note: MUL BL multiplies only AL by BL and writes the result to AX. This code does not represent the computation of 16×2³⁰⁰ with unlimited precision; register width and overflow must be taken into account.*

## Polynomial Question for AL=k

```asm
MOV DL,AL
MUL DL
MOV CX,5
MUL CX
XCHG DX,AX
MOV AL,3
MUL DL
SUB DX,AX
XCHG DX,AX
SUB AX,CX
```

The answer key gives 5k²−3k−5.

*Note: In the source code, MUL CX modifies the DX:AX pair; the subsequent XCHG also swaps DX and AX. Therefore, the assumption that DL preserves the initial value k is not valid. The polynomial in the key cannot be verified as the general result of the listed instructions.*

## DEC and Flag Table

Starting from AL=02H, DEC AL is applied three times:

| Step | AL | ZF | PF | SF |
| --- | --- | --- | --- | --- |
| First | 01H | 0 | 0 | 0 |
| Second | 00H | 1 | 1 | 0 |
| Third | FFH | 0 | 1 | 1 |

## Subtracting Five from a Memory Array

The question asks for 5 to be subtracted from each of the bytes in the range DS:2000–DS:2008. The answer from the source:

```asm
MOV CX,8
MOV DI,2000H
TOP: SUB [DI],5
     INC DI
     LOOP TOP
```

*Note: The range 2000H–2008H, including both endpoints, is nine bytes; CX=8 processes only the first eight bytes. The width of the memory operand must also be specified with BYTE PTR for the assembler.*

## Address Decoding

The address bits A14, A15, and A16 are connected to the 74LS138 decoder. The A0–A13 pins of the ROM select 2¹⁴=16384 bytes, that is, 16 KiB of capacity. In the solution in the photograph, the ranges F0000H–F3FFFH are given for Y4 and F8000H–FBFFFH for Y6. The upper address bits determine the enable inputs.

## Cumulative Sum of an Array

```asm
DELTA DB 1,2,4,2,6
MOV AX,0
MOV SI,OFFSET DELTA
MOV CX,5
DONGU: ADD AX,[SI]
       MOV [SI],AX
       INC SI
       LOOP DONGU
MOV BX,AX
MOV CX,5
DIV CL
INT 03
```

The handwritten key gives the array as 1,3,7,9,15; AX as 3, BX as 15, and DX as 0.

*Note: DELTA is a byte array, but ADD AX,[SI] and MOV [SI],AX operate at word width. Advancing by one byte at a time creates overlapping word accesses. The dividend of DIV CL is AX, and its results are AL and AH; it does not clear DX. The key describes the intended byte-wise summation, not the actual execution of the listed code.*

## CMP Results

Initially AX=8001H, SI=0200H, DI=0300H; DS:0100=F0H, DS:0200=F0H, DS:0201=01H, DS:0300=34H, and DS:0301=12H are given.

| Instruction | ZF | SF | CF | AF | OF | PF |
| --- | --- | --- | --- | --- | --- | --- |
| CMP [0100],AL | 0 | 1 | 0 | 1 | 0 | 0 |
| CMP AX,[SI] | 0 | 0 | 0 | 1 | 1 | 1 |
| CMP WORD PTR [DI],1234H | 1 | 0 | 0 | 0 | 0 | 1 |

## Final: ADC and Transfer Rate

The example in the photograph uses a 10 V full scale and 16-bit conversion. 10/2¹⁶≈0.0001526 V, that is, approximately 152.6 µV/step is found. For 4 V, the ideal proportional code is approximately 26214. In the separate transfer question, when one byte is sent each time at a rate of 1 kHz, 3,600,000 bytes are transferred in one hour.

*Note: The duration statement in the continuation of the ADC question could not be read with certainty in the photograph, so it has not been transcribed. Depending on the endpoint definition, the use of 2ⁿ or 2ⁿ−1 in the resolution calculation may vary; here the 2¹⁶ assumption on the paper has been retained.*

## CALL, INT, RET, and IRET

CALL stores the return address on the stack. In a near call, IP is stored; in a far call, CS and IP are stored. INT transfers to the interrupt routine by storing FLAGS, CS, and IP. RET is used for returning from a procedure, and IRET is used to restore IP, CS, and FLAGS.

## Bit Counting and Clearing

For DL=E0H there are three 1 bits; in the source, this count was added to the initial value to obtain the result E3H. Another loop starts at DS:2000 and clears eight bytes with CX=8; the value read into AL is cleared with XOR AL,AL and written back.

## Port Transfer with the 8255

Port A is selected as input, port B as output, the upper half of C as input, and the lower half of C as output. The port addresses are A=7CH, B=7DH, C=7EH, and control=7FH; the mode 0 control word is 98H. The data read from A is transferred to B, and the upper four bits of C are rotated right by four positions and transferred to the lower four outputs.

```asm
MOV AL,98H
OUT 7FH,AL
TEKRAR: IN AL,7CH
        OUT 7DH,AL
        IN AL,7EH
        MOV CL,4
        AND AL,0F0H
        ROR AL,CL
        OUT 7EH,AL
        JMP TEKRAR
```

*Note: The final LOOP instruction in the source was changed to JMP in red pen; the corrected reading is shown here.*

## The 1,2 Pattern in an Array

The data array is 5,7,9,1,2,6,5,0,1,2,1,1,1,2. The consecutive 1,2 pair occurs in three places. The solution compares two adjacent elements and increments the counter.

*Note: In the draft in the photograph, DX is used as a memory addresser. In the 8086's 16-bit addressing modes, [DX] is not valid; the limitation of the source draft has been retained and noted.*

## Reading Five Bytes from a Port

```asm
MOV SI,0
MOV CX,0005H
KAL: IN AL,80H
     MOV [SI+2000H],AL
     INC SI
     LOOP KAL
```

## PIC LED Application

PORTB is set as output and PORTA as input. 01H is written to PORTB and the carry is cleared. After the delay subroutine, the lit LED is shifted left with RLF. When a carry occurs, the program waits for the button on bit 1 of PORTA; the movement is repeated in the reverse direction with RRF. LIST specifies the target processor, INCLUDE specifies the register definitions; the TRIS registers determine the port directions.

*Note: Returning to the same label with GOTO does not terminate the program; it creates an infinite loop. The "end of program" comment in the source should be read in this sense.*
