---
baslik: EEM211 Digital Logic Design: D Flip-Flop Finite State Machine Quiz and Answer Key (December 2012)
ozet: Analysis of a finite state machine (FSM) with two D flip-flops: the equations DA = X'·QB, DB = X and Z = QA·X, the state table, and a four-state Mealy state diagram. Başkent University BME 231 Quiz V (21.12.2012) and the BİL 275 2010–2011 fall Quiz-4 answer key.
---

This post was transcribed to text from two photographs shared by phone on 28 December 2012 for EEM211 Digital Logic Design final exam preparation. Both photographs contain the same question: the Başkent University Department of Biomedical Engineering **BME 231 Digital Logic Design Quiz V** paper (21.12.2012; the student information area was already covered in the photograph) and the handwritten worked "answer key" sheet for the Computer Engineering **BİL 275 Digital Logic Design 2010–2011 Fall Quiz-4** question. The text was transcribed from the photographed pages; the photographs themselves have not been published.

## Question

The circuit has two D flip-flops (A and B), a common clock (Clock), and an input X. X passes through an inverter and then, together with the output QB of flip-flop B, enters an AND gate; the output of this AND drives the D input of flip-flop A (DA). X is connected directly to the D input of flip-flop B (DB). The output Z is the AND of QA and X.

> Using the finite state machine (FSM) circuit given above, answer the following questions.
> a. Write the equations of the two flip-flop circuits and of Z. (30 points)
> b. Construct the state table. (40 points)
> c. Draw the state diagram. (30 points)

The D flip-flop table is also given on the paper: for D = 0, Q(t+1) = 0; for D = 1, Q(t+1) = 1.

## Answer key

**a) Equations:**

- DA = X'·QB
- DB = X
- Z = QA·X

**b) State table:**

| QA | QB | Next QA QB (X = 0) | Next QA QB (X = 1) | Z (X = 0) | Z (X = 1) |
|---|---|---|---|---|---|
| 0 | 0 | 00 | 01 | 0 | 0 |
| 0 | 1 | 10 | 01 | 0 | 0 |
| 1 | 0 | 00 | 01 | 0 | 1 |
| 1 | 1 | 10 | 01 | 0 | 1 |

*Note: The table was checked against the equations; for example, for QA QB = 01 and X = 0, DA = 1·1 = 1, DB = 0, so the next state is 10; for QA = 1 and X = 1, Z = 1.*

**c) State diagram** (labeled X/Z; since the output depends on the input, this is a Mealy machine):

- 00: X = 0 → 00 (0/0), X = 1 → 01 (1/0)
- 01: X = 0 → 10 (0/0), X = 1 → 01 (1/0)
- 10: X = 0 → 00 (0/0), X = 1 → 01 (1/1)
- 11: X = 0 → 10 (0/0), X = 1 → 01 (1/1)

When X = 1 arrives, the machine goes to 01 from every state; when X = 0 arrives, the value of QB is shifted into QA. Thus QB holds the previous input, and QA holds the information "the input two steps ago was 1 and the previous input was 0". For Z = 1, the last three inputs must be **1, 0, 1**; that is, the circuit detects the **sequence 101** (allowing overlaps).

*Note: The sequence interpretation in the last paragraph is not in the answer key; it was derived from the state table.*
