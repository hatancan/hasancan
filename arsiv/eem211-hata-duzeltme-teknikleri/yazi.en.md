---
baslik: EEM211 Digital Logic Design: Error Correction Techniques – Parity, CRC, ARQ and Hamming Code (Trakya University Project Assignment, 2009)
ozet: A "Error Correction Techniques" project assignment and presentation prepared in 2009 for the Trakya University BİLM 637 course: parity checking, two-dimensional parity, VRC/LRC, CRC-16, stop-and-wait and sliding window protocols, ARQ, (11,7) and (7,4) Hamming codes, error correction with the G and H matrices, Reed-Solomon and Raptor codes.
---

This post is a **project assignment** and presentation that is included in the EEM211 Digital Logic Design course folder as a supplementary resource on Hamming codes. The assignment was prepared by a graduate student for the **BİLM 637 Mobile and Wireless Computing** course (Assoc. Prof. Dr. Hasan Hüseyin Balık) at the **Trakya University Institute of Science, Department of Computer Engineering** (Edirne, December 2009). The student's name and number on the cover have been removed. The 36-page report consists of two parts: the fundamentals of digital communication and error detection/correction techniques. Below, the parts of the report most relevant to a digital logic course (parity, CRC, Hamming code) are presented in detail and the other parts in summary. A PDF of the redacted report and the 37-slide presentation can be downloaded as a ZIP at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon the request of the rights holder.*

## Introduction

Packets travelling through a network are subject to certain error risks; in particular, if the network conditions are poor, packets may be lost or corrupted. However, such errors can be corrected. This study focuses on error correction techniques, with emphasis on the most widely used Hamming coding algorithm and ARQ techniques, and also briefly covers the Reed-Solomon and Raptor forward error correction codes.

## Part I: Fundamentals of digital communication (summary)

The first part of the report reviews the underlying background of the subject:

- **Digital communication:** the transfer of binary (0/1) coded data between systems. Transmission rate is given in bit/s; for example, a 2400 bit/s line using 8-bit codes carries 2400 / 8 = 300 characters per second.
- **Data transmission characteristics:** information is carried by varying the amplitude, frequency and phase of an oscillating signal; **baud** is the rate at which the signal on the line changes. If two bits are sent with each signal change, the bit rate is twice the baud rate.
- **Bandwidth and Shannon's law:** the maximum information rate a channel can carry is given by C = W·log₂(1 + S/N) (W is the bandwidth, S/N is the signal-to-noise ratio). The report gives the maximum capacity of a voice channel with an S/N ratio of 1000 to 1 as 25,900 bit/s.
- **Period and wavelength:** T = 1/F; for example, the period of a 2400 Hz signal is 1/2400 ≈ 0.000416 s. Wavelength WL = S / F (S: propagation speed of the signal).
- **Coding:** with n bits, 2ⁿ symbols can be encoded; ASCII is a 7-bit code (128 characters) and EBCDIC is an 8-bit code. An 8th bit (parity) can be added to ASCII to detect errors.
- **Parallel and serial transmission:** in parallel transmission each bit travels on a separate path (with data-ready / request signals); serial transmission is divided into three types: asynchronous (start and stop bits for each character), synchronous (clock travels with the data, special codes at the beginning and end of a block) and isochronous (periodic, guaranteed capacity; audio-video).
- **Line types:** simplex (one-way, TV broadcasting), half duplex (two-way in turns, walkie-talkie), full duplex (two-way simultaneously, telephone).

## Part II: Error detection and correction techniques

During data transmission, the possibility that some bits become corrupted, however small, cannot be ignored; even a single corrupted bit can render the whole data meaningless. **Error detection** techniques are used to determine whether corruption has occurred, and **error correction** techniques are used to fix it if it has; if the error cannot be corrected, the data packet is retransmitted. These functions belong to the **data link layer** of the OSI model: the layer divides the data into frames and appends a **Frame Check Sequence (FCS)** to the end of each frame; the receiver performs the same calculation and compares the result with the FCS.

### Protocols (summary)

- **Stop-and-wait (Idle RQ):** an ACK is awaited after each frame. If the frame or the ACK is corrupted, the frame is retransmitted after a timeout; if the receiver sends a NAK for a corrupted frame, retransmission takes place without waiting for the timeout.
- **Continuous RQ:** the sender transmits frames back to back without waiting for an ACK and keeps copies of them in a retransmission list.
- **Selective repeat:** only the corrupted frame is retransmitted.
- **Go-back-N:** when an out-of-sequence frame is received, all frames following the last acknowledged frame are requested again.
- **Sliding window:** the number of frames that can be sent without waiting for acknowledgment is limited to K (when K = 1 it behaves like stop-and-wait).

Two types of errors are seen in data transmission: in a **burst** error, meaningless information arrives at the receiver for a period of time and all the bits during that period may be corrupted; in a **random** error, individual bits are corrupted by noise in the medium. Errors have two causes: **bit errors** (electromagnetic effects, etc.) and **packet losses** (network congestion, excessive delay).

### Error correction methods

1. **Symbol substitution:** if a human evaluates the data at the receiver, an unused symbol is substituted for a character that was received incorrectly; if the operator cannot make sense of it, retransmission is requested.
1. **Retransmission (ARQ, Automatic Repeat Request):** a message received in error is automatically requested again. It is the most reliable method, but not always the most efficient; the statistically ideal message block is stated to be 256–512 characters.
1. **Forward error correction (FEC):** extra bits are added to the message before transmission, and errors are detected and corrected at the receiver without retransmission. The most common example is the **Hamming code**, developed by R. W. Hamming at Bell Laboratories.

| Algorithms used for FEC | Algorithms used for ARQ |
|---|---|
| Convolutional codes | CRC codes |
| BCH codes | Serial parity |
| Hamming codes | Block parity |
| Reed-Solomon codes | Modular sum |
| Raptor codes | |

## Error detection techniques

Error detection techniques do not say which bit is erroneous; they only determine that an error exists.

- **Redundancy:** each character is sent twice; if the two copies are not identical, there is an error.
- **Exact count coding:** all characters have the same number of 1s (e.g., three 1s in every character); errors are detected by counting the 1s.
- **Echoplex:** the operation performed at the terminal is reported to the host, the host echoes it back, and the user checks its correctness on the screen.

### Parity check

This is the most frequently used error detection method. In **even parity**, the number of 1s including the parity bit is even; in **odd parity**, it is odd. The even parity bit is found by XORing the data bits; the odd parity bit is found with XNOR. For example, for the data 0110 the even parity bit is 0 and the odd parity bit is 1.

| Data | Number of 1s | Even parity | Odd parity |
|---|---|---|---|
| 1101 | 3 (odd) | 1 → 11011 | 0 → 11010 |
| 1100 | 2 (even) | 0 → 11000 | 1 → 11001 |

*Note: In the odd parity example, the report states that the bit to be appended for 1100 is "0"; the correct value is 1 (the resulting 11001 given as the outcome is correct).*

### Two-dimensional parity, VRC and LRC

In two-dimensional parity, in addition to each character's own parity bit, parity bits are also generated by bit position (column); thus, for a single-bit error, the position of the erroneous bit can also be found.

- **VRC (vertical redundancy check, character parity):** a parity bit is appended to each character before transmission.
- **LRC (longitudinal redundancy check, message parity):** for each bit position, the parity of all characters in the message is calculated and appended to the end of the message like a final character; only even parity is used in LRC.

Example: for the ASCII message "THE CAT", odd parity for VRC and even parity for LRC:

| Character | T | H | E | space | C | A | T | LRC |
|---|---|---|---|---|---|---|---|---|
| Hexadecimal | 54 | 48 | 45 | 20 | 43 | 41 | 54 | 2F |
| b0 (LSB) | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| b1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| b2 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| b3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| b4 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| b5 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| b6 (MSB) | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 |
| b7 (VRC) | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |

LRC detects 95–98% of all transmission errors, but it cannot detect an error if an even number of characters are corrupted in the same bit position. When VRC and LRC are used together, the position of a single-bit error can be located. The **checksum**, which uses the mod 256 sum of the bytes in the message, also belongs to this family.

### CRC (cyclic redundancy check)

CRC is the most reliable and most widely used error detection technique; it detects approximately 99.95% of transmission errors. The data bits are treated as the coefficients of a polynomial. The data polynomial P(x) is multiplied by xᵖ (p zeros are appended to the right of the data) and divided mod 2 (using XOR) by the **generator polynomial G(x)** of degree p:

xᵖ·P(x) = Q(x)·G(x) + R(x)

The quotient is discarded, and the **remainder R(x)** is appended to the end of the data and transmitted. The receiver divides the received sequence by the same G(x); if the remainder is zero, the data has arrived without error. The most common code in the USA is **CRC-16**; its generator polynomial is:

G(x) = x¹⁶ + x¹² + x⁵ + 1

The number of bits in the CRC code equals the highest power of the generator polynomial (16 here).

### ARQ methods

Three methods are used in ARQ: **positive acknowledgment** (the receiver sends an acknowledgment for every frame it receives without error), **retransmission after timeout**, and **retransmission with negative acknowledgment** (the receiver sends a NAK for a corrupted frame). There are two types of ARQ: stop-and-wait ARQ (idle RQ) and continuous RQ (go-back-N, selective repeat).

## Hamming coding system

The Hamming code is a linear error control and correction method used in telecommunications: it **detects and corrects single-bit errors**, and can detect but not correct two-bit errors. In the 1940s, Richard Hamming was working at Bell Laboratories on the Bell Model V relay computer, which ran on punched cards; tired of his jobs being aborted by errors on weekends when no operator was present, after years of work he published the method bearing his name in 1950.

Hamming defined codes using the (n, k) notation: n is the total number of bits and k is the number of data bits. For example, adding one parity bit to 7-bit ASCII is an (8,7) code, and repeating three times is a (3,1) code; the **code rate** is k/n (1/3 for repetition). The number of bits by which two codewords differ from each other was called the **Hamming distance**: the distance of the parity method is 2, and the distance of the (3,1) repetition code is 3. The goal is to increase the distance while keeping the code rate high.

The algorithm:

1. All bit positions that are powers of 2 (1, 2, 4, 8, 16, …) are reserved for parity bits.
1. The other positions (3, 5, 6, 7, 9, 10, 11, …) are reserved for data bits.
1. The parity bit at position n checks n bits, skips n bits, checks n bits, skips n bits, and so on, starting at its own position. That is, the 1st parity bit checks positions 1, 3, 5, 7, 9, 11…; the 2nd parity bit checks 2, 3, 6, 7, 10, 11…; the 4th parity bit checks 4–7, 12–15…; the 8th parity bit checks 8–15, 24–31….

### (11,7) Hamming code example

Let the 7-bit data be "0110001". The data bits d1…d7 are placed at positions 3, 5, 6, 7, 9, 10, 11 and the parity bits (even parity) are calculated:

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bit | p1 | p2 | d1 | p3 | d2 | d3 | d4 | p4 | d5 | d6 | d7 |
| Data without parity | | | 0 | | 1 | 1 | 0 | | 0 | 0 | 1 |
| Data with parity | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |

The transmitted codeword is **00001101001**. Suppose the 3rd bit from the left is corrupted during transmission, and the receiver receives **00101101001**. The receiver rechecks each parity bit; it writes 0 if correct and 1 if wrong:

| Parity bit | Positions checked | Result | Parity check bit |
|---|---|---|---|
| p1 | 1, 3, 5, 7, 9, 11 | Wrong | 1 |
| p2 | 2, 3, 6, 7, 10, 11 | Wrong | 1 |
| p3 | 4, 5, 6, 7 | Correct | 0 |
| p4 | 8, 9, 10, 11 | Correct | 0 |

Writing these bits in the order p4 p3 p2 p1 gives **0011** = 2 + 1 = **3**: the erroneous bit is at position 3. By flipping the 3rd bit, the data is restored to its original form, 00001101001.

*Note: The codeword and the syndrome were checked; the (11,7) Hamming code of the data 0110001 is indeed 00001101001.*

### (7,4) Hamming code and Hamming matrices

The first thing that comes to mind today when one says Hamming code is the **(7,4)** code announced in 1950: 3 check bits are added to every 4 data bits; it can correct every single-bit error, or detect all single- and two-bit errors. This code works with two matrices: the **generator matrix G** (7×4) and the **parity-check matrix H** (3×7). In this example the data bits are in the first 4 positions and the parity bits are in the last 3 positions.

```
G =  1 0 0 0        H =  0 1 1 1 1 0 0
     0 1 0 0             1 0 1 1 0 1 0
     0 0 1 0             1 1 0 1 0 0 1
     0 0 0 1
     0 1 1 1
     1 0 1 1
     1 1 0 1
```

The first 4 rows of G form the 4×4 identity matrix (it passes the data through as is), and its last 3 rows show from which data bits the parity bits are calculated. The last 3 columns of H form the 3×3 identity matrix, and its first 4 columns are the same parity relationships.

**Channel coding:** let the data to be sent be "1001", p = (1, 0, 0, 1)ᵀ. The encoded data is obtained by mod 2 multiplication as x = G·p = (1, 0, 0, 1, 1, 0, 0)ᵀ.

**Parity check:** if there is no error, the received r = x and z = H·r = (0, 0, 0)ᵀ.

**Error correction:** if there is a single-bit error, r = x + eᵢ (eᵢ is the zero vector with a 1 at position i) and

H·r = H·(x + eᵢ) = H·x + H·eᵢ = 0 + H·eᵢ = H·eᵢ

that is, z equals the i-th column of H and indicates the position of the erroneous bit. For example, if the 3rd bit is corrupted, r = (1, 0, 1, 1, 1, 0, 0)ᵀ and z = H·r = (1, 1, 0)ᵀ; this is the 3rd column of H. When the 3rd bit is flipped, the original data is recovered.

## Reed-Solomon and Raptor codes (summary)

- **Reed-Solomon** codes are powerful linear error correction codes; they operate over Galois fields (each symbol is 8 bits), and an R-S(n, k) code can correct (n−k)/2 symbol errors. The decoder is complex and has some limitations for packet-level losses; the required processing power increases rapidly with block length.
- In **Raptor** codes, the receiver reconstructs the k source symbols by receiving k' > k symbols; the receiver overhead R = (k' − k)/k is below 1%. They place no limit on data size, and the required processing power increases linearly.

## Conclusion

When comparing different error correction techniques, the packet loss rate, the required network resources (bandwidth), the processor load at the sender and receiver, and the complexity of the algorithm should be taken into account.

## Presentation

The 37-slide presentation prepared with the assignment summarizes the same topics: digital communication and data transmission, parallel/asynchronous/synchronous serial transmission, transmission line types, real-time and non-real-time communication, the data link layer and FCS, stop-and-wait, continuous RQ, selective repeat, go-back-N and sliding window protocols, error types, error detection techniques (redundancy, exact count, echoplex, two-dimensional parity, LRC, CRC), the three error correction methods, FEC and ARQ algorithms, the Hamming code algorithm, the (11,7) example, the (7,4) code and matrices, and Reed-Solomon and Raptor codes.
