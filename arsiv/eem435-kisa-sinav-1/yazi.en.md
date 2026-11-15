---
baslik: EEM435 Computer-Aided Design: Quiz I (27.10.2016), Generating an Amplitude Modulation Signal with MATLAB
ozet: Quiz I question from Dr. Alparslan Çağrı Yapıcı's EEM435 Computer-Aided Design course: generating and plotting an amplitude modulation signal with a single-tone message and a carrier (modulation index 0.8).
---

The paper for **Quiz I** of the **EEM 435 Computer-Aided Design** course (**Dr. Alparslan Çağrı Yapıcı**) at Başkent University, dated **27 October 2016**. The folder was named only "Ders" (Course); the course name can be inferred from the quiz paper. The name and number fields on the paper are blank. The PDF of the quiz can be downloaded at the end of the post.

## Question

Let the **amplitude modulation (AM)** signal for a single-tone message signal be defined as

s(t) = A_c·[1 + μ·cos(2π·f_m·t)]·cos(2π·f_c·t)

Using MATLAB:

- **a)** Generate the message signal m(t) = A_m·cos(2π·f_m·t) for f_m = 1 kHz and A_m = 1 V, over a time span of at least three periods.
- **b)** Generate the carrier signal c(t) = A_c·cos(2π·f_c·t) for f_c = 20 kHz and A_c = 1 V, over the time interval used in part a.
- **c)** Generate the AM signal s(t) for the message and carrier of the first two parts, with μ = 0.8, over the same time interval.
- **d)** Plot the generated message, carrier, and AM signals as separate plots on the same figure. Show the title and axis labels of each plot on the figure.

*Note: The answer to the question is not on the paper. The message period is 1 ms, so three periods amount to 3 ms; since the carrier is 20 kHz, the sampling frequency must be chosen to be at least 40 kHz (in practice much higher, such as 200 kHz); the envelope of the AM signal is A_c·[1 + 0.8·cos(2π·1000·t)], which varies between 0.2 and 1.8 V.*
