---
baslik: EEM211 Digital Logic Design: Additional Verilog Sources for the Adder and the Display
ozet: Ten source files covering dataflow and structural modeling, gate delays, and a four-digit display driver.
---

Additional Verilog examples prepared by classmates during the 2005–2006 laboratory work. Personal information has been removed from the comments. Files with the same name but different content were placed in separate example folders inside the ZIP; personal folder paths were not used. The code can be downloaded at the end of the post.

The examples were transferred into the text as they were found in the archive; they were not run or compiled. Some module names are repeated across files; these are separate works. Errors noticed during code review are noted under the relevant example.

## 1. decoder.v

A four-digit display driver: decoder, anode_decoder, clkdiv and SSdriver. This version uses bit cnt[2] in the clock divider. *Note: The last always block is sensitive only to changes in cnt; no separate sensitivity has been written for changes on the data inputs. The source behavior has been preserved.*

```verilog
`timescale 1ns / 1ps
module decoder(SS,S);
output reg [7:0] SS;
input [3:0] S;
always @(S)
case (S)
	0				:SS=8'b10000001;
	1				:SS=8'b10101111;
	2				:SS=8'b01001001;
	3				:SS=8'b00001101;
	4				:SS=8'b00010111;
	5				:SS=8'b00100101;
	6				:SS=8'b00100001;
	7				:SS=8'b10001111;
	8				:SS=8'b00000001;
	9				:SS=8'b00000101;
	10				:SS=8'b11111110;
	default		:SS=8'b11111111;
	endcase
	endmodule
	
module anode_decoder(AN,cnt);
output reg [3:0] AN;
input	[1:0] cnt;
always @(cnt)
case (cnt)
	0				:AN=4'b1110;
	1				:AN=4'b1101;	
	2				:AN=4'b1011;
	3				:AN=4'b0111;
	default		:AN=4'b1111;
	endcase
	endmodule

module clkdiv(clk,mclk);
output clk;
input mclk;
reg [15:0] cnt;
assign clk=cnt[2];
initial cnt=0;

	always @(posedge mclk)
	begin
			cnt=cnt+1;						
	end
endmodule

module SSdriver(SS,AN,mclk,S1,S2,S3,S4);
input mclk;
input[3:0] S1,S2,S3,S4;
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
		2'b01	: SS<=w2;
		2'b10	: SS<=w3;
		2'b11 : SS<=w4;	 

	endcase
	end
	endmodule
```

## 2. fourbitadder1.v

A four-bit connection that builds the full adder from sum-of-products expressions.

```verilog
`timescale 1ns / 1ps
module fadder (s,co,c,a,b);
	output s,co;
	input c,a,b;
	assign co=(~c & a & b)|(c & ~a & b)|(c & a & ~b)|(a & b & c);
	assign s=(~c & ~a & b)|(~c & a & ~b)|(c & ~a & ~b)|(c & a & b);
endmodule

module fourbitadder1 (LD0,LD1,LD2,LD3,LD4,SW0,SW1,SW2,SW3,SW4,SW5,SW6,SW7,BTN0);
	 output LD0,LD1,LD2,LD3,LD4;
	 input  SW0,SW1,SW2,SW3,SW4,SW5,SW6,SW7,BTN0;
	 wire W1,W2,W3;
	 fadder a1(LD0,W1,BTN0,SW0,SW4);
	 fadder a2(LD1,W2,W1,SW1,SW5);
	 fadder a3(LD2,W3,W2,SW2,SW6);
	 fadder a4(LD3,LD4,W3,SW3,SW7);
endmodule
```

## 3. fourbitadder2.v

A gate-level structural full adder and a four-stage connection. *Note: The inputs of gate g18 include both c and ~c; this term is always 0. One term of the expected sum function is therefore missing. The source was not modified.*

```verilog
`timescale 1ns / 1ps
module andgate (y,a,b,c);
	output y;
	input a,b,c;
	assign  y=a & b & c;
endmodule

module orgate (y,a,b,c);
	output y;
	input a,b,c;
	assign y=a | b | c;
endmodule

module invgate (y,a);
	output y;
	input a;
	assign y=~a;
endmodule

module fadderStr(s,co,a,b,c);
output s,co; 
input a,b,c;
wire w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17;
not g1(w1,c);
not g2(w2,a);
not g3(w3,b);
and g4(w4,a,b,w1);
and g5(w5,w2,b,c);
and g6(w6,a,w3,c);
and g7(w7,a,b,c);
or g8(co,w4,w5,w6,w7);
not g9(w8,a);
not g10(w9,c);
not g11(w10,b);
not g12(w11,c);
not g13(w12,a);
not g14(w13,b);
and g16(w14,w8,b,w9);
and g17(w15,a,w10,w11);
and g18(w16,w12,w13,c);
and g15(w17,a,b,c);
or g19(s,w14,w15,w16,w17);
endmodule 

module fourbitadder2 (LD0,LD1,LD2,LD3,LD4,SW0,SW1,SW2,SW3,SW4,SW5,SW6,SW7,BTN0);
	 output LD0,LD1,LD2,LD3,LD4;
	 input  SW0,SW1,SW2,SW3,SW4,SW5,SW6,SW7,BTN0;
	 wire W1,W2,W3,W4,W5,W6,W7,W8,W9;
	 fadderStr a1(LD0,W1,BTN0,SW0,SW4);
	 fadderStr a2(LD1,W2,W1,SW1,SW5);
	 fadderStr a3(LD2,W3,W2,SW2,SW6);
	 fadderStr a4(LD3,LD4,W3,SW3,SW7);
endmodule
```

## 4. tamtoplayici.v

A single-bit full adder with 17 ns XOR, 14 ns AND and 15 ns OR delays.

```verilog
`timescale 1ns / 1ps
module tamtoplayici(LD0,LD1,SW0,SW1,BTN0);
input SW0,SW1,BTN0;
output LD0,LD1;
wire w1,w2,w3;
xor #(17) xor1(w1,SW0,SW1);
and #(14) and1(w2,SW0,SW1);
xor #(17) xor2(LD0,w1,BTN0);
and #(14) and2(w3,BTN0,w1);
or #(15) or1(LD1,w2,w3);


endmodule
```

## 5. fourbitadder4.v

A four-stage version of the full adder with delays; the sum and carry are connected to the LD outputs.

```verilog
`timescale 1ns / 1ps
module tamtoplayici(s,cout,a,b,cin);
input a,b,cin;
output s,cout;
wire w1,w2,w3;
xor #(17) xor1(w1,a,b);
and #(14) and1(w2,a,b);
xor #(17) xor2(s,w1,cin);
and #(14) and2(w3,cin,w1);
or #(15) or1(cout,w2,w3);


endmodule

module tamtoplayici4(LD,SW,BTN0);
input [7:0] SW;
input BTN0;
output [4:0] LD;
wire W1,W2,W3;
tamtoplayici a1(LD[0],W1,SW[4],SW[0],BTN0 );
tamtoplayici a2(LD[1],W2,SW[5],SW[1],W1);
tamtoplayici a3(LD[2],W3,SW[6],SW[2],W2);
tamtoplayici a4(LD[3],LD[4],SW[7],SW[3],W3);

endmodule
```

## 6. fourbitscarryahead.v

A version built with the PCgen and carrygen modules. *Note: Although carrylookahead appears in its name, the c1→c2→c3 carry chain proceeds sequentially; a full parallel carry-lookahead network has not been written.*

```verilog
`timescale 1ns / 1ps
module PCgen(s,c,x,y);
input x,y;
output s,c;
xor #(17) (s,x,y);
and #(14) (c,x,y);
endmodule

module carrygen(s,c,x,y,z);
input x,y,z;
output s,c;
wire w1,w2,w3;
PCgen pc1(w1,w2,x,y);
PCgen pc2(s,w3,w1,z);
or #(15) g1(c,w2,w3);
endmodule

module fourbitscarrylookahead(LD,BTN0,SW);
input [0:7] SW;
input BTN0;
output [0:4] LD;
wire c1,c2,c3,s0,s1,s2,s3,p0,p1,p2,p3;

carrygen ca1(s0,c1,SW[4],SW[0],BTN0);
carrygen ca2(s1,c2,SW[5],SW[1],c1);
carrygen ca3(s2,c3,SW[6],SW[2],c2);
carrygen ca4(s3,LD[4],SW[7],SW[3],c3);
xor #(17) x1(p0,SW[4],SW[0]);
xor #(17) x2(p1,SW[5],SW[1]);
xor #(17) x3(p2,SW[6],SW[2]);
xor #(17) x4(p3,SW[7],SW[3]);
xor #(17) x5(LD[3],c3,p3);
xor #(17) x6(LD[2],c2,p2);
xor #(17) x7(LD[1],c1,p1);
xor #(17) x8(LD[0],BTN0,p0);
endmodule
```

## 7. forbitadder1.v

A four-bit dataflow version with a different port order.

```verilog
module fadder(s,co,c,a,b);
	input c,a,b;
	output s,co;
	assign co=(~c&a&b)|(c&~a&b)|(c&a&~b)|(a&b&c);
	assign s=(~c&~a&b)|(~c&a&~b)|(c&~a&~b)|(c&a&b);
endmodule




module fourbitadder1(ld0,ld1,ld2,ld3,ld4,btn0,sw0,sw4,sw1,sw5,sw2,sw6,sw3,sw7);
	input btn0,sw0,sw4,sw1,sw5,sw2,sw6,sw3,sw7;
	output ld0,ld1,ld2,ld3,ld4;
	wire w1,w2,w3;
	fadder f0(ld0,w1,sw0,sw4,btn0);
	fadder f1(ld1,w2,sw1,sw5,w1);
	fadder f2(ld2,w3,sw2,sw6,w2);
	fadder f3(ld3,ld4,sw3,sw7,w3);
endmodule
```

## 8. fourbitadder2.v

A structural version built with the andgate, orgate and invgate submodules.

```verilog
`timescale 1ns / 1ps
module andgate(y,a,b,c);
	input c,b,a ;
	output y ;
	assign y=(a&b&c);
endmodule

 module orgate(y,a,b,c,d);
	input a,b,c,d;
	output y ;
	assign y=(a|b|c|d);
endmodule

 module invgate(y,a);
	input a;
	output y;
	assign y=(~a);
endmodule


 module fadderstr(s,co,a,b,c);
	input a,b,c;
	output s,co;
	wire w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11;
	invgate i1(w1,a);
	invgate i2(w2,b);
	invgate i3(w3,c);
	andgate a0(w4,w3,a,b);
	andgate a1(w5,c,w1,b);
	andgate a2(w6,c,a,w2);
	andgate a3(w7,a,b,c);
	orgate o0(co,w4,w5,w6,w7);
	andgate a7(w8,w3,w1,b);
	andgate a4(w9,w3,a,w2);
	andgate a5(w10,c,w1,w2);
	andgate a6(w11,c,a,b);
	orgate o2(s,w8,w9,w10,w11);
endmodule

module fourbitadder2(ld0,ld1,ld2,ld3,ld4,btn0,sw0,sw4,sw1,sw5,sw2,sw6,sw3,sw7);
	input btn0,sw0,sw4,sw1,sw5,sw2,sw6,sw3,sw7;
	output ld0,ld1,ld2,ld3,ld4;
	wire w1,w2,w3;
	fadderstr f0(ld0,w1,sw0,sw4,btn0);
	fadderstr f1(ld1,w2,sw1,sw5,w1);
	fadderstr f2(ld2,w3,sw2,sw6,w2);
	fadderstr f3(ld3,ld4,sw3,sw7,w3);



endmodule
```

## 9. fourbitadder.v

Building a full adder from two half adders, and a four-bit circuit from four full adders.

```verilog
`timescale 1ns / 1ps
module halfadder (S,C,a,b);
	input a,b;
	output S,C;
	xor #(17)(S,a,b);
	and #(14)(C,a,b);
endmodule

module tamtoplayici(S,C,a,b,cin);
	input a,b,cin;
	output S,C;
	wire S1,D1,D2;
	halfadder HA1 (S1,D1,a,b),
				 HA2 (S,D2,S1,cin);
	or #(15) g1(C,D2,D1);
endmodule

module fourbitadder (S,C,A,B,cin);
	input [3:0] A,B;
	input cin;
	output [3:0] S;
	output C;
	wire C1,C2,C3;
	tamtoplayici FA0(S[0],C1,A[0],B[0],cin),
				    FA1(S[1],C2,A[1],B[1],C1),
				    FA2(S[2],C3,A[2],B[2],C2),
				    FA3(S[3],C,A[3],B[3],C3);
endmodule
```

## 10. fourbitscarrylookahead.v

A version that computes the propagate Pi=A⊕B and generate Gi=AB signals in separate modules. *Note: The carry stages are connected in series; although the file name says carrylookahead, the carry dependency forms a chain.*

```verilog
`timescale 1ns / 1ps
module PGgen(Pi,Gi,A,B);

output Pi,Gi;
input A,B;
xor #(17)(Pi,A,B);
and #(14) (Gi,A,B);

endmodule

module carrygen (S,ea,Pi,Gi,cout);

output S,ea;
input Pi,Gi,cout;
wire w;

xor # (17) (S,Pi,cout);
and # (14) (w,Pi,cout);
or  # (15) (ea,Gi,w);

endmodule


module fourbitscarrylookahead (S,cout,A,B,cin);

output [3:0] S;
output cout;
input [3:0] A,B;
input cin;

wire P0,P1,P2,P3,G0,G1,G2,G3,C0,C1,C2,C3;

PGgen pg1 (P0,G0,A[0],B[0]);
PGgen pg2 (P1,G1,A[1],B[1]);
PGgen pg3 (P2,G2,A[2],B[2]);
PGgen pg4 (P3,G3,A[3],B[3]);

carrygen C6 (S[0],C1,P0,G0,cin);
carrygen C7 (S[1],C2,P1,G1,C1);
carrygen C8 (S[2],C3,P2,G2,C2);
carrygen C9 (S[3],cout,P3,G3,C3);

endmodule
```
