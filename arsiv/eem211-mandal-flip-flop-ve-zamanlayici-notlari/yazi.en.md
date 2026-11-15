---
baslik: EEM211 Digital Logic Design: D Latch, JK Flip-Flop, State Table and Timer Exercise
ozet: From photographed student notes: the D latch, edge triggering, the JK characteristic equation, a four-state machine, and a timer question that counts sheets of paper.
---

Study sheets for EEM211 Digital Logic Design prepared by a friend were transcribed to text from photographed pages. Three of the note photographs are dated 28 December 2012; the additional timer question carries no date. Student names have been removed. The photographs themselves and the download file are not published.

## D Latch

The note states that the D latch avoids the indeterminate state of the SR latch. The D and D' signals are passed through NAND gates together with the En (enable) input and applied to a cross-coupled NAND latch.

| En | D | Next Q |
|---|---|---|
| 0 | X | No change |
| 1 | 0 | 0: reset |
| 1 | 1 | 1: set |

The block symbols of the NOR-based SR latch, the NAND-based active-low SR latch, and the D latch are also compared.

## Edge Triggering with Two D Latches

Two D latches are connected in series; CLK is applied to the enable of the first and inverted CLK to the enable of the second. Below this are the symbols for positive-edge-triggered and negative-edge-triggered D flip-flops. The operations listed in the note are: setting the output to 1, setting it to 0, and complementing (toggling) it.

## JK Flip-Flop

The table for the two-input JK flip-flop:

| Q | J | K | Q(t+1) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

From the Karnaugh map, **Q(t+1) = Q'J + K'Q**. When J = K = 0 the state is held; 01 resets, 10 sets, and 11 complements (toggles).

## Four-State Machine Example

In the table and diagram in the photograph, the input is x, the output is y, and the state bits are A and B. The previous page of the circuit is not in this photograph.

| Present AB | Next AB, x=0 | Next AB, x=1 | y, x=0 | y, x=1 |
|---|---|---|---|---|
| 00 | 00 | 01 | 0 | 0 |
| 01 | 00 | 11 | 1 | 0 |
| 10 | 00 | 10 | 1 | 0 |
| 11 | 00 | 10 | 1 | 0 |

In the state diagram each arrow is labeled x/y: state 00 has a 0/0 self-loop; 00→01 is labeled 1/0; 01→11 is 1/0; 11→10 is 1/0; and 10 has a 1/0 self-loop. States 01, 10, and 11 return to 00 with 0/1.

## Timer Question for an ECG Device

The question on the paper: A self-running ECG device collects data for ten minutes and produces one printout at the end of every ten minutes. Given that there are six sheets of paper, design the circuit that will control the first data acquisition; any type of flip-flop may be used.

In the solution drawing there is **CLK = 1/60 Hz**, a counter made of four D flip-flops, and a second counter made of three JK flip-flops. The codes **1010** are noted next to the first counter and **101** and **111** next to the second; feedback and clear connections are drawn. The final output is shown as a "light bulb".

*Note: A 1/60 Hz clock produces one pulse per minute; ten pulses correspond to ten minutes. Six printouts require a total of 60 minutes. The connections of the second counter in the photograph and the differing final-state markings are not clear enough to confirm this behavior with certainty; the drawing is not presented as a completed and verified design.*
