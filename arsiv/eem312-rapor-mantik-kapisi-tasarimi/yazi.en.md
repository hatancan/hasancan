---
baslik: EEM312 Digital Electronics: Logic Gate Design Reports, Pass Transistor XOR and CMOS NAND/NOR (2005–2017)
ozet: Student reports from 2005–2017 for the logic gate design experiment of the EEM312 Digital Electronics software laboratory: source/drain connections that swap depending on the input in a six-transistor pass transistor XOR gate, two- and three-input CMOS NAND/NOR with the minimum number of transistors, truth tables, and a delay comparison.
---

This post collects the reports written for the **logic gate design** experiment of the **EEM312 Digital Electronics** software laboratory at Başkent University. The experiment was run as **Y8** in 2005–2006, as **Y6** in the 2011 handouts, and as "Experiment 10" in 2014. The reports are: two from 2005 (A, B), two from 2006 (C, D), two prelab-and-report sets from 2011 (E, F), and one prelab-and-report set from 2014 (G); these are the work of friends, with **personal information removed**. The ZIP also contains the XOR simulations prepared by **Hasan Can Öztürk** in 2017 (student number redacted). The handouts are in the post [EEM312 software laboratory handouts Y4–Y8](/arsiv/eem312-yazilim-deneyleri-y4-y8/) (Y6 and Y8 sections). The PDFs of the reports, the cleaned-up SPICE netlists, and the 2017 screenshots are in the ZIP at the end of the post.

## 1. Pass transistor XOR gate

The XOR gate in the handout has six transistors: a CMOS inverter produces the complement of A (−A), an inverter-like structure is connected to input B, and a transmission gate driven by B passes either A or −A to the output. The common observation in the reports: **depending on the value of input B, the source and drain terminals of the transistors in the transmission gate (P2/N2 or M3/M6, depending on the report) swap roles**; since the bulk is written as tied to the source in SPICE, a separate netlist was prepared for each input combination (A, B = 00, 01, 10, 11). Example (from report E for A = 0, B = 0; node 2 = A, 3 = −A, 4 = B, 5 = output, model lines omitted):

```
*  D G S B
M1 3 2 0 0 MOSN W=1.8u L=1.2u
M2 3 4 5 5 MOSN W=1.8u L=1.2u
M3 5 3 4 4 MOSN W=1.8u L=1.2u
M4 3 2 1 1 MOSP W=3.6u L=1.2u
M5 2 4 5 5 MOSP W=3.6u L=1.2u
M6 4 2 5 5 MOSP W=3.6u L=1.2u
vdd 1 0 5V
v2 2 0 0v
v4 4 0 0v
.control
tran 0.05n 500n
plot v(2) v(4) v(5)
.endc
.end
```

The prelab of report G explains the A = B = 0 case step by step: since A is low, the inverter's PMOS conducts and produces −A = 1; since B is low, the PMOS connected to B is conducting, the NMOS is cut off, and the value of A at its source (0) is passed to the output. The 2014 report, on the other hand, showed the four cases in succession in a single netlist using two pulse sources (A: 100 ns, B: 200 ns half-period).

| A | B | A ⊕ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

All simulations satisfy the truth table. Report E notes that the small values seen in the plot where the output should be 0 are on the order of nanovolts, and that 0.1 V was added to the signals to separate the overlapping waveforms. Report A found the rise delay of the XOR output to be 0.27 ns and the fall delay to be 0.268 ns.

## 2–3. NAND and NOR with the minimum number of transistors

The task is a CMOS NAND and NOR gate with the minimum number of transistors: an N-input gate uses N NMOS and N PMOS transistors (4 transistors for 2 inputs, 6 for 3 inputs). In the NAND, the NMOS transistors are in series and the PMOS transistors in parallel; in the NOR, the reverse.

- **2005 (A, B):** three-input NAND and NOR (1 fF load at the output). The NAND gives 0 only when all three inputs are 1, and the NOR gives 1 only when all three inputs are 0.
- **2006 and later (C–G):** two-input NAND and NOR; the simulation results agree with the truth tables. The prelab of F shows that the two-input NAND can also be built with two pass transistors and an inverter, and that there is an alternative structure for the NOR as well.

## 4–5. Delay comparison

| Report | Gate | Low to high | High to low |
|---|---|---|---|
| A (2005) | XOR (2 inputs) | 0.27 ns | 0.268 ns |
| A (2005) | NAND (3 inputs) | 1.03 ns | 2.35 ns |
| A (2005) | NOR (3 inputs) | 1.95 ns | 3.15 ns |
| D (2006) | NAND (2 inputs), worst case | 1.135 ns | |
| D (2006) | NOR (2 inputs), worst case | 1.623 ns | |

Report A points out that the XOR has two inputs while the others have three, and that the real comparison should be made between the NAND and the NOR; in both reports (A, D) the NOR is slower than the NAND. Reports C, E, and F, however, concluded that "the gate with the smallest worst-case delay is the NOR." Report F also writes that in designs close to a differential structure, the change at the output is seen earlier.

*Note: In the NOR gate the PMOS transistors are connected in series, and the carrier mobility of the PMOS (KP = 2.7E−5 in the model) is about three times smaller than that of the NMOS (8.0E−5); for this reason, with the same sizes, the rise delay of the NOR comes out larger than that of the NAND. The numerical results of reports A and D agree with this. The explanation in report A that "the delay is large because the transistors are connected in parallel in the NOR" is incomplete: what increases the delay is the series PMOS chain that pulls the output up. The "NOR is fastest" conclusion in C, E, and F also contradicts this expectation; the reports do not give the worst-case delays numerically.*

*Note: The column heading of the NOR truth table in report A mistakenly says "NAND"; the table values belong to the NOR and are correct. The title of F's prelab also gives the course code as "EEM332".*

## Other files in the folder

The folder also contained netlist folders from other students for the same experiment (separate files for each input combination, three-input gate attempts) and two more report copies: one is an identical copy of report A without a title, and the other has almost the same text as report C. These were not included separately. The ZIP contains the netlists of report E (`2011_…`) as well as the XOR netlists and WinSPICE screenshots from the 2017 work.
