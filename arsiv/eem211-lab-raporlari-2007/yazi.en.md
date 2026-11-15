---
baslik: EEM211 Digital Logic Design: 2006–2007 Laboratory Reports and Verilog Code (Experiments 4–9, Seven-Segment Display Driver)
ozet: Experiment 4–9 reports and Verilog code prepared by classmates for the EEM211 laboratory: behavioral and structural 4-bit adders, a full adder with gate delays and carry-lookahead, finding a faulty wire, design with MUXes and decoders, D flip-flops and JK counters, a four-digit seven-segment display driver (SSdriver) with 0–9 and 0–99 counters.
---

This post brings together the reports and Verilog source code prepared by classmates for the laboratory experiments of the EEM211 Digital Logic Design course, collected in the course folder under the name "ferhat_notlari" (Ferhat's notes), from the **fall semesters of 2006 and 2007**. Student names and numbers in the reports have been masked, and the numbers have been removed from file names (the reports are marked with the letters A, B, C, D as belonging to four different people). The Xilinx intermediate files in the folder (compilation outputs, simulation databases) were not included. The masked reports and Verilog files can be downloaded as a ZIP at the end of the post.

## Experiment 4: 4-bit adder (Verilog)

Report A contains two solutions. In the second question, the full adder is written behaviorally, using minterms:

```verilog
module fadder(s,co,c,a,b);
output s,co;
input c,a,b;
assign co = (~c & a & b) | (c & ~a & b) | (c & a & ~b) | (a & b & c);
assign s = (~c & ~a & b) | (~c & a & ~b) | (c & ~a & ~b) | (c & a & b);
endmodule
```

In the third question, the AND, OR, and complement (inverter) gates are defined as separate modules (`andgate`, `orgate`, `invgate`), and the full adder (`fadderStr`) is rebuilt structurally from these gates; in both solutions, four full adders are chained to form `fourbitadder1` and `fourbitadder2`.

## Experiment 6: Adders with gate delays

In Report B, the full adder is defined with gate delays (XOR 17, AND 14, OR 15 units):

```verilog
module tamtoplayici(s,cout,a,b,cin);
input a,b,cin;
output s,cout;
wire w1,w2,w3;
xor #(17)
  x1(w1,a,b),
  x2(s,cin,w1);
and #(14)
  a1(w2,a,b),
  a2(w3,w1,cin);
or #(15) (cout,w3,w2);
endmodule
```

With this, a 4-bit ripple-carry adder was built, along with a 4-bit **carry-lookahead** adder (`fourbitscarrylookahead`) using the `PGgen` and `carrygen` modules.

## Experiment 7: Faulty circuit, MUX, and decoder

Two reports (B and C) answer the same questions:

1. When the incorrect function F of the given circuit is simplified on a Karnaugh map, the **c'd** term of the correct F turns out to be missing; that is, the wire carrying d' to the AND gate that produces the c'd term is faulty (not making contact).
1. The function F was written in canonical form, and the four-input, single-output circuit was designed using at most three 2-input MUXes.
1. Using a 2x4 decoder and a 4x1 MUX, a circuit that outputs 1 if the two-bit numbers ab and cd are equal: F = a'b'c'd' + a'bc'd + ab'cd' + abcd. It is written in canonical form and placed on a Karnaugh map to perform the equality check.

## Experiment 8: D flip-flop and JK counters

The same questions are answered in three explanation documents:

1. The FD block is a D flip-flop triggered on the rising edge; because of the inverter in front of the output, the output is the complement of the input and changes at every clock pulse (the frequency is halved).
1. The circuit with four JK flip-flops is an asynchronous **down counter**, with the output of each flip-flop connected to the clock input of the next: it decrements from 1111 to 0000.
1. When inverters are placed on all the clock inputs, the flip-flops trigger on the falling edge and the circuit **counts up** from 0000.
1. Since the first flip-flop of the counter in Figure 3 passes the complement of its input to the output, the operation in Figure 1 can also be performed with this circuit (by taking the least significant bit).

*Note: In one of the explanations, the second state of the down counter is written as "0111, decimal equivalent 14"; the bits were read from Q0 to Q3 (in reverse order). In the order Q3Q2Q1Q0, this state is 1110 = 14.*

## Experiment 9: Latches, flip-flops, and the seven-segment display driver

This experiment uses a four-digit seven-segment display driver (`SSdriver`). According to Report D (19 December 2006), the module's task is to transfer the four 4-bit pieces of input data (S1–S4) to the four displays in sequence: first the equivalent of S1 is given to the SS output and the common anode (AN) of the first display is driven, then the same is done for S2, S3, and S4. Since this scan is repeated hundreds of times per second, the eye does not notice the flicker and steady digits are seen on the displays.

```verilog
module clkdiv(clk,mclk);
output clk;
input mclk;
reg [15:0] cnt;
assign clk=cnt[15];
initial cnt=0; // Don't forget!! Otherwise simulator does generate X only
always @(posedge mclk)
begin
cnt = cnt+1;
end
endmodule

module SSdriver(SS,AN,mclk,S1,S2,S3,S4);
input mclk;
input [3:0] S1,S2,S3,S4;
output reg [7:0] SS;
output reg [3:0] AN;
wire [7:0] w1,w2,w3,w4;
wire clk;
wire [3:0] w5;
reg [1:0] cnt;
clkdiv cdiv(clk,mclk);
decoder d1(w1,S1);
decoder d2(w2,S2);
decoder d3(w3,S3);
decoder d4(w4,S4);
anode_decoder d5(w5,cnt);
initial cnt=0;
always @(posedge clk)
begin
cnt=cnt+1;
end
always @(cnt)
begin
AN<=w5;
case (cnt)
2'b00 : SS<=w1;
2'b01 : SS<=w2;
2'b10 : SS<=w3;
2'b11 : SS<=w4;
endcase
end
endmodule
```

The `decoder` module converts the digits 0–9 into an 8-bit segment code (e.g., 0 → 10000001, 1 → 10011111; active low), while `anode_decoder` sets one of the four anodes to 0 according to the 2-bit counter (1110, 1101, 1011, 0111). `clkdiv` generates the scan clock by dividing the board's clock by 2¹⁶.

The reports describe the counters built with this driver:

- **0–9 counter:** An AND gate connected to the output of an 8-bit binary counter sets the clr input to 1 when the output is 1010 (10) and resets the counter; thus the counter counts only up to 9, and the output is passed to the display.
- If the clr input is tied permanently to 1, the outputs are reset and the display always shows 0.
- **0–99 counter:** Each digit is counted by a separate counter; the output of the AND gate that resets the first counter at 10 is connected to the clock input of the second counter. Thus each time the ones digit rolls over from 9 to 0, the tens digit increments by one, and the circuit counts up to 99.
