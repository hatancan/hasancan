---
baslik: MAT340 Probability: Practice Problems (2003) and Midterm Exam Questions (21 November 2002), with Worked Notes
ozet: Başkent University probability course practice problems (10 problems: tree diagram, counting, Bayes, independence, relay systems) and the 21.11.2002 midterm exam (relay chain, hypergeometric distribution); with computed solutions for some of the problems.
---

Two documents from the probability courses of Lecturer Pelin Toktaş at Başkent University: **"Practice Problems 1"** (5 March 2003, Computer Engineering, 2002-2003 spring, MAT 250 Probability and Statistics) and the **MAT 240 Probability Midterm Exam** (21 November 2002, Electrical and Electronics Engineering, 2002-2003 fall). The documents contain no solutions; verified short results have been added next to the problems below. The original PDFs can be downloaded as a ZIP at the end of the post. (The folder also contained other scanned practice problems/answers; these were not included in this post.)

## Practice Problems 1 (5 March 2003)

1. A die is rolled once. If the result is even, a coin is tossed once more; if it is odd, the coin is tossed twice. List all elements of the sample space using a tree diagram.
2. In a three-component system, component 1 is connected in series with the parallel 2-3 subsystem (for the system to work, component 1 and the 2-3 subsystem must both be functioning). (a) A: exactly two components are working; (b) B: at least two components are working; (c) the event that the system works: which outcomes belong to these events? (w: working, f: failed)
3. Using the digits 0, 1, 2, 3, 4, 5, 6: (a) how many three-digit numbers can be written? (b) If each digit is used only once, how many three-digit numbers? (c) …how many even numbers? (d) …how many odd numbers? (e) …how many even numbers have an odd digit in the middle position?
4. In a light bulb factory, 100 of 1000 60 W bulbs and 150 of 2000 100 W bulbs are defective. What is the probability that a randomly selected defective bulb is a 60 W bulb? *(Bayes: (100/3000)/((100+150)/3000) = 100/250 = 0.4.)*
5. A signal is transmitted from point a to point b through relays R1, R2, R3 (assuming R2 and R3 are in a parallel branch and R1 is in series): the failure probability of R1 is 0.005, and that of R2 and R3 is 0.001; the relays are independent. What is the probability that the signal fails to reach b?
6. (a) If a fair coin is tossed 10 times, what is the probability that the first five tosses show the same face? (b) Given that the sum of two fair dice is greater than 10, what is the probability that the sum is 12? *(1/3)* (c) A 3-person committee is chosen from 4 married couples: (i) how many different committees are there? *(C(8,3) = 56)* (ii) How many contain 2 women and 1 man? *(C(4,2)·4 = 24)* (iii) How many have no two members who are married to each other? *(C(4,3)·2³ = 32)*
7. Two balls are drawn from a box containing 4 balls numbered 1, 2, 3, 4. A: the number on the first ball is 1; B: the number on the second ball is 1. (a) Are A and B independent when drawing without replacement? *(No: P(A)P(B) = 1/16, P(A∩B) = 0.)* (b) With replacement? *(Yes: 1/4 · 1/4 = 1/16.)*
8. Urn 1 contains 2 white and 1 black ball; urn 2 contains 1 white and 5 black balls. A ball is drawn at random from urn 1 and placed in urn 2; then a ball is drawn from urn 2 and it is white. What is the probability that the transferred ball was white? *(Bayes: (2/3 · 2/7)/(2/3 · 2/7 + 1/3 · 1/7) = (4/21)/(5/21) = 4/5.)*
9. In a toy company, 40% of previous toys have been successful; 80% of successful toys and 30% of unsuccessful ones received a favorable report in market research. (a) What is the probability that a new toy that receives a favorable report will be successful? *(0.32/(0.32+0.18) = 0.64)* (b) Given a favorable report, what is the probability that it is unsuccessful? *(0.36)*
10. There are 3 people in an elevator and 3 floor options; each person independently and with equal probability gets off at one of the floors. What is the probability that exactly 1 person gets off at each floor? *(3!/3³ = 2/9)*

## MAT 240 Probability Midterm Exam – 21 November 2002

**Question 1 (23 points).** A transmitter sends a message in binary code; before reaching the receiver, the data passes through 3 relays, and each relay makes an error with probability 0.20 (the relays are independent). (a) (5 points) If a "1" is sent from the transmitter, what is the probability that a "1" comes out of all three relays? (b) (8 points) What is the probability that a "1" is also received at the receiver (using a tree diagram)? (c) (10 points) If 70% of the transmitted data are "1", what is the probability that a "1" was sent from the transmitter given that the receiver received a "1"?

*Solution: (a) 0.8³ = 0.512; (b) even number of errors: 0.512 + 3·0.2²·0.8 = 0.608; (c) Bayes: 0.7·0.608/(0.7·0.608 + 0.3·0.392) ≈ 0.7835.*

**Question 2 (17 points; the results of this question may be left uncomputed).** On a production line, 20 workers work during the day, 15 work at night, and 10 work from midnight until morning. The quality control department selects 6 workers for a survey, without selecting the same worker twice. (a) (4 points) In how many different ways can 6 workers be selected, all from the day shift? (b) (6 points) What is the probability that all 6 workers are from the same shift? (c) (7 points) What is the probability that the 6 selected workers are from at least two different shifts?

*Solution: (a) C(20,6) = 38,760; (b) [C(20,6) + C(15,6) + C(10,6)]/C(45,6) = (38,760 + 5,005 + 210)/8,145,060 ≈ 0.0054; (c) 1 − 0.0054 ≈ 0.9946.*

**Question 3 (23 points).** A box contains 10 balls: 8 are marked $2 and 2 are marked $5. Three balls are drawn from the box without replacement; X is the number of balls marked $5 among the 3 balls drawn. (a) (8 points) What is the probability mass function of X? (b) (8 points) What is the cumulative distribution function? (c) (7 points) What are the variance and the standard deviation?

*Solution: X is hypergeometric: P(X = 0) = 7/15, P(X = 1) = 7/15, P(X = 2) = 1/15. F(x): 0 (x < 0), 7/15 (0 ≤ x < 1), 14/15 (1 ≤ x < 2), 1 (x ≥ 2). E(X) = 0.6; Var(X) = 3 · 0.2 · 0.8 · 7/9 = 28/75 ≈ 0.373; σ ≈ 0.611.*

*Note: Since the figure in practice problem 5 could not be rendered as text, the relay connection (R1 in series, R2 and R3 in parallel) was written as an assumption; consult the original PDF for the exact result. The result of 6(c)(iii) was computed by choosing 3 of the 4 couples and then choosing one of 2 genders for each (C(4,3)·2³ = 32).*
