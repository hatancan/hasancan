---
baslik: EEM332 Microprocessors: 2007 Midterm Questions and Solution Checks
ozet: Loops, stack, arithmetic flags, ASCII conversion and indirect addressing in the 13 April 2007 midterm.
---

This content from the Başkent University EEM332 Microprocessors course archive was transcribed to text from photographed pages. The 13 April 2007 midterm covered loops, the stack, arithmetic flags, ASCII conversion and indirect addressing. Student names and numbers have been removed. The photographs are kept in a private archive. A two-page PDF version of the clean scanner copy can be downloaded as a ZIP at the end of the post.

## BX at the End of the Loop

```asm
MOV BX,0005H
MOV CX,30H
L1: CMP CX,0010H
    JA L2
    INC BX
L2: LOOP L1
```

BX is incremented when CX is 10H or less. After sixteen increments, BX = 0015H.

## PUSH and the Stack Layout

The initial values are given as SP=1236H, AX=24B6H, DI=85C2H and DX=5F93H.

```asm
PUSH AX
PUSH DI
PUSH DX
```

| Address | Byte |
| --- | --- |
| SS:1230 | 93H |
| SS:1231 | 5FH |
| SS:1232 | C2H |
| SS:1233 | 85H |
| SS:1234 | B6H |
| SS:1235 | 24H |

The final SP=1230H; SS:1236 is not modified by these instructions. The low-order byte is written to the lower address.

## Signed Addition and Extension

```asm
DATA1 DB +80
DATA2 DB +85
SONUC DW ?
MOV AL,DATA1
MOV BL,DATA2
ADD AL,BL
JNO HIGH
MOV AL,DATA2
CBW
MOV BX,AX
MOV AL,DATA1
CBW
ADD AX,BX
HIGH: MOV SONUC,AX
```

After the first ADD, AL=A5H, OF=1, CF=0 and SF=1. JNO does not jump; the two positive numbers are sign-extended separately. After the second ADD, AX=00A5H, OF=0, CF=0 and SF=0.

## Forming Two ASCII Digits

Source program for AL=29H:

```asm
MOV AH,AL
AND AX,F00FH
MOV CL,4
SHR AH,CL
OR AX,3030H
XCHG AH,AL
```

The result is AX=3932H. AL holds the ASCII "2" and AH holds the ASCII "9".

## Equation with Registers

```asm
PUSH DX
MOV AX,4
MUL BX
PUSH AX
MOV AX,CX
MOV CX,7
AND DX,00
DIV CX
POP BX
ADD AX,BX
POP BX
XOR DX,DX
DIV BX
```

Assuming no overflow occurs and the initial DX is nonzero, if the initial registers are called B, C and D, the result is of the form floor((floor(C/7)+4B)/D). DIV is unsigned integer division; the remainders are also written to DX.

## LOOPNZ

```asm
MOV CX,17
TOP: SUB CX,2
     CMP CX,12
     LOOPNZ TOP
```

In the first pass, CX becomes 15 and then 14. In the second pass, SUB brings it down to 12; as a result of CMP, ZF=1. LOOPNZ still decrements CX, making it 11, and then exits without jumping. The final CX=11.

## Flags

The 8-bit result of the sum F5H+0BH is 00H: CF=1, SF=0, PF=1, AF=1 and ZF=1.

## Completing the Subtraction Program

In the source, MOV DH,4CH; SUB DH,6EH; JNC Next is followed by two blank lines, and then Next: MOV BL,DH. The solution in the photograph writes NOT DH and INC DH in these lines; this yields the absolute value of the negative difference.

```asm
MOV DH,4CH
SUB DH,6EH
JNC Next
NOT DH
INC DH
Next: MOV BL,DH
```

The final BL=22H. The CF=1 produced by SUB is not changed by NOT and INC.

## Sum of Five Bytes with Register Indirect Addressing

The source asks for the instructions that add the values [0200], [0201], [0202], [0203] and [0204] to AL in turn to be written as a loop. The text equivalent of the method in the photograph:

```asm
MOV AL,0
MOV BX,0200H
MOV CX,5
NEXT: ADD AL,[BX]
      INC BX
      LOOP NEXT
```

*Note: The numerical results were verified instruction by instruction. The memory addresses in the last two questions are interpreted as hexadecimal; in the source, the H suffix is missing from some constants.*
