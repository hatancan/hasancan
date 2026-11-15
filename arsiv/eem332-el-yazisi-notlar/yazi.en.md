---
baslik: EEM332 Microprocessors: 8086 Hardware and Assembly Handwritten Notes
ozet: Addressing, stack, flags, loops, and memory connections from the 2011 course pages archived in 2014.
---

This content from the Başkent University EEM332 Microprocessors course archive was transcribed from photographed pages. It covers addressing, stack, flags, loops, and memory connections from the 2011 course pages archived in 2014. Student names and numbers have been removed. The photographs are kept in a private archive; this post has no download file.

## A Software and Hardware View of the Microprocessor

The notes dated April 6, 2011 treat the processor from two perspectives: on the software side, the registers and instruction set; on the hardware side, the pins, data bus, and control signals. A 40-pin package is shown for the 8086 and 8088, with 16-bit and 8-bit external data buses respectively. Minimum mode is described for single-processor connections, and maximum mode for larger system connections.

*Note: The statement in the source that "the only difference between the 8086 and the 8088 is the data bus" is a simplification; the instruction queue and some pin functions also differ.*

## Control Signals and Clock

RD and WR determine the read/write direction, and the memory/port selection determines the relevant control signal. ALE causes the address on the multiplexed address/data lines to be held in a latch; data can then be carried over the same pins. NMI is shown as the non-maskable interrupt; it is not blocked by IF. Reset puts the processor into its initial execution state.

Clock pulses determine the timing of operations. In the notes, a memory read/write cycle is shown as taking four clock pulses; a single instruction may require more than one cycle.

*Note: The four-clock depiction is the basic bus cycle without added wait states. For dynamic RAM, the word "reset" in the note describes the refresh operation. When an NMI arrives, all data is not saved automatically; the necessary saving is done by the interrupt routine.*

## Memory Capacity and Address Decoding

For k address lines and an N-bit data width, the capacity is 2ᵏ×N bits. A 32 KiB×8-bit organization requires 15 address lines, and a 2 KiB memory requires 11 address lines. The upper address bits are connected to the decoder, and the lower bits to the memory's own address inputs. The 16 KiB block with A19–A14=111100 is the range F0000H–F3FFFH.

## Segment and Physical Address

Physical address = segment×10H + offset. A segment start lies on a 16-byte boundary; the 16-bit offset addresses a 64 KiB area within a segment. CS:IP is used for instructions, DS for data, and SS:SP for the stack. LEA loads the effective address, not the data in memory.

In the example with CS=3489H and IP=2500H, the last digits of the addition result in the note are garbled.

*Note: The calculation should be 34890H+2500H=36D90H. The offsets 0000H–FFFFH of this segment correspond to the range 34890H–4488FH.*

## MOV and Addressing Examples

```asm
MOV AL,BL
MOV AL,0005H
MOV [1234H],AL
MOV CX,DX
MOV AX,857AH
```

In the notes, direct memory-to-memory MOV and MOV AL,CX with mismatched widths are crossed out as invalid. A register must be used as an intermediate step. The basic addressing modes are immediate, register, direct memory, register indirect, indexed, and base+index+displacement.

In the MOV AX,[BX+4] example, with DS=0100H and BX=0600H, the physical address is 01604H. If this address holds B0H and the next address holds C0H, then AX=C0B0H. In the MOV [BP][SI],AH example, the default segment is SS; for SS=2000H, BP=4000H, SI=0800H, the address is 24800H. AH=07H is written to this address.

## Registers and DEBUG Flags

AX/BX/CX/DX can be split into high and low bytes such as AH/AL. SP is the stack pointer, BP is the base pointer, and SI and DI are the index registers. The laboratory photograph shows DEBUG's flag abbreviations:

| Flag | 1 | 0 |
| --- | --- | --- |
| OF | OV | NV |
| DF | DN | UP |
| IF | EI | DI |
| SF | NG | PL |
| ZF | ZR | NZ |
| AF | AC | NA |
| PF | PE | PO |
| CF | CY | NC |

CF denotes unsigned carry/borrow, OF signed overflow, ZF zero, SF sign, and PF even parity of the low byte. In BCD operations, each decimal digit is represented by four bits; appropriate BCD adjust instructions are needed after arithmetic.

## Stack

On the 8086, a word PUSH decrements SP by 2; POP increments it by 2. SS does not change. For SS=0000H, SP=2000H, and AX=1234H, after PUSH AX, SP=1FFEH; [1FFE]=34H and [1FFF]=12H.

```asm
PUSH AX
PUSH BX
POP AX
POP BX
```

This sequence swaps the contents of the two registers. In subroutines used with CALL/RET, the necessary registers can be preserved with PUSH/POP.

## Counting Zero Bits

Source example for NUM=F0E0H:

```asm
MOV CX,16
SUB BX,BX
MOV AX,NUM
Back: SHR AX,1
      JC SON
      INC BX
SON: LOOP Back
MOV Count,BX
```

F0E0H contains seven 1s and nine 0s; Count=9. The bit shifted out by SHR goes into CF. JC skips the increment when the bit is 1.

## Adding Five Bytes

```asm
SUB AL,AL
MOV CX,5
MOV BX,200H
NEXT: ADD AL,[BX]
      INC BX
      LOOP NEXT
```

The bytes at DS:0200H–0204H are summed in AL. Since the result is eight bits, overflow must be tracked separately.

## Adding Five to Every Element of an Array

For the 16 bytes in the range DS:1000H–100FH, the note contains CX=16, a start of DI=1000H, and a loop of ADD [DI],5, INC DI, and LOOP.

*Note: The source does not specify the width of the memory operand; for the assembler to determine it, the form ADD BYTE PTR [DI],5 is needed. The handwritten statement that the LOOP instruction sets ZF to 1 because CX=0 is incorrect: LOOP does not modify the flags.*

## Signed Sum

For DATA1=+80 and DATA2=+85, the eight-bit sum is A5H; OF=1, CF=0, SF=1. If each operand is separately extended to a word with CBW and then added, the result is 00A5H, that is, +165.

## Comparison and Conditional Jumps

CMP sets the flags without storing the result of the subtraction. JE/JZ tests equality, JNE/JNZ tests inequality, JNC tests for no carry, and JS tests for a negative sign. JA/JAE are for unsigned magnitude comparison. AND AL,04H is an example of testing by masking bit 2.

```asm
MOV CL,03H
SHR AL,CL
JC BIT2_ONE
```

After three right shifts, the original bit 2 is in CF. Another counter loop in the notes uses DEC CL and JNZ.

## Flag Transfer and Control

LAHF transfers some of the status flags to AH, and SAHF transfers from AH to those flags. CLC clears the carry flag and STC sets it; CLI and STI control maskable interrupts. CLD sets DF=0 so that string operations proceed toward increasing addresses.

## String Instructions and Nested Loops

MOVSB moves one byte from DS:SI to ES:DI; MOVSW moves one word. LODS transfers the source value to AL/AX, and STOS transfers AL/AX to the destination. SCAS compares AL/AX with the value at ES:DI. The REP counter is CX. In the STOS example in the notes, the value AL=42 is written to consecutive destination locations. LODS and STOS do not perform comparisons and do not change the arithmetic status flags.

LOOPE requires CX to be nonzero and ZF=1; LOOPNE requires CX to be nonzero and ZF=0. In nested loops, the stack can be used to preserve the outer CX value. HLT halts processor execution until an appropriate interrupt or reset condition.
