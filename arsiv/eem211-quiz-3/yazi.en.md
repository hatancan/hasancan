---
baslik: EEM211 Digital Logic Design: Quiz 3 Answer Key (2006)
ozet: Answer key for the 2006 Quiz 3 of EEM211 Digital Logic Design (Groups A and B): truth table, canonical sum of products (Σ minterm) and product of sums (Π maxterm) forms, and simplification with a four-variable Karnaugh map.
---

This post is the answer key for **Quiz 3** of the Başkent University course **EEM 211 Digital Logic Design**, given in October 2006 (according to the file information, prepared by Evren Ferhat Emekdaş). The topic of this two-question quiz is **canonical forms and the Karnaugh map**. Groups A and B are the same questions asked with different functions. The questions are printed and the solutions are handwritten; the original Word file can be downloaded at the end of the post.

## Quiz 3 (A)

### Question 1

> Given the Boolean function F=xy+x'z: a. Obtain the truth table for F. b. Write F in canonical sum of products form. c. Write F in canonical product of sums form.

a) Truth table:

| x | y | z | F |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

- b) F(x, y, z) = Σ(1, 3, 6, 7) = m1 + m3 + m6 + m7
- c) F(x, y, z) = Π(0, 2, 4, 5) = M0 · M2 · M4 · M5

### Question 2

> Express F(A,B,C,D)=Σ(1,3,4,6,9,11,12,14) in standard product of sums form by using Karnaugh map.

Karnaugh map (rows AB, columns CD):

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 0 | 1 | 1 | 0 |
| 01 | 1 | 0 | 0 | 1 |
| 11 | 1 | 0 | 0 | 1 |
| 10 | 0 | 1 | 1 | 0 |

F' is found by grouping the zeros: the four corners give B'D', and the central group of four gives BD.

- F' = BD + B'D'
- F = [(BD) + (B'D')]'
- F = (BD)' · (B'D')'
- **F = (B' + D')(B + D)**

![Quiz 3 Group A answer key: truth table, canonical forms, and Karnaugh map](s-01.jpg "Quiz 3 (A), Answer Key")

## Quiz 3 (B)

### Question 1

> Given the Boolean function F=x'y+xz: a. Obtain the truth table for F. b. Write F in canonical sum of products form. c. Write F in canonical product of sums form.

a) Truth table:

| x | y | z | F |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

- b) F(x, y, z) = Σ(2, 3, 5, 7) = m2 + m3 + m5 + m7
- c) F(x, y, z) = Π(0, 1, 4, 6) = M0 · M1 · M4 · M6

### Question 2

> Express F(A,B,C,D)=Π(1,3,4,6,9,11,12,14) in standard sum of products form by using Karnaugh map.

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 00 | 1 | 0 | 0 | 1 |
| 01 | 0 | 1 | 1 | 0 |
| 11 | 0 | 1 | 1 | 0 |
| 10 | 1 | 0 | 0 | 1 |

The ones are grouped: the four corners give B'D', and the central group of four gives BD.

**F = B'D' + BD**

![Quiz 3 Group B answer key: truth table, canonical forms, and Karnaugh map](s-02.jpg "Quiz 3 (B), Answer Key")
