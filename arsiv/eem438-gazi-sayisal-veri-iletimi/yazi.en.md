---
baslik: EEM438 Data Communications: Digital Data Transmission: Line Coding and PCM (Gazi University, Suat Özdemir)
ozet: Data Communications lecture slides by Suat Özdemir of Gazi University: line coding techniques (NRZ, Manchester, AMI, 4B/5B, B8ZS, HDB3), sampling with PCM, parallel and serial transmission.
---

These are the Chapter 4 (Digital data transmission) slides that Suat Özdemir of the Department of Computer Engineering at Gazi University prepared for the "Veri İletişimi / Data Communications" course (slide date 5 March 2011; the footer reads BM 403 Data Communications). They are kept in the EEM438 folder as the course material of a second instructor. The slide text is transcribed below; figures and tables taken from the textbook are not published, and slides without text are marked. The original PDF can be downloaded at the end of the post.

Scope: line coding techniques (NRZ, Manchester, AMI, 4B/5B, B8ZS, HDB3), sampling with PCM, parallel and serial transmission.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*

## Digital-to-digital conversion

- For information to be transmitted between two points, it must be converted into an analog or digital signal.
- In digital-to-digital conversion, digital data is converted into a digital signal.
- In analog-to-digital conversion, analog data is converted into a digital signal.
- The signal obtained from the conversion is transmitted between two points in parallel or serial form.

## Digital-to-digital conversion (2)

- Line coding is the process of converting digital data into a digital signal.
- In data communications, the goal is to transmit pieces of data. The smallest piece is called a bit.
- In the figure, r denotes the number of data pieces carried by one signal piece.

## Digital-to-digital conversion (3)

- Data rate denotes the number of bits transmitted in one second (bps, bit/s).
- Signal rate denotes the number of signals transmitted in one second (baud).
- Data rate is usually expressed as bit rate.
- Signal rate is expressed as baud rate, pulse rate, or modulation rate.
- The goal is to increase the bit rate while reducing the baud rate.
- Bandwidth denotes the frequency bandwidth required to carry the signal.
- Increasing the number of changes in the signal requires a wider frequency band.

## Problems in signal transmission

- In signal encoding, long runs of 1s and 0s are difficult to decode correctly at the receiver. Precautions must be taken.
- If a digital signal stays constant for a certain period, a DC component arises, which is a problem for systems that do not pass low frequencies. (A telephone line does not pass frequencies below 200 Hz.)
- The bit interval must be the same in both systems (receiver and transmitter).
- A self-synchronizing digital signal is one that carries its own timing information.

## Digital signal line coding techniques

- They fall into 5 basic groups.

## Unipolar (non-return-to-zero)

- Bit 1 is represented by a positive voltage and bit 0 by a negative voltage or 0 V.
- It is called non-return-to-zero because the signal does not return to 0 in the middle of the bit.

## Polar (non-return-to-zero)

- A two-level signal is used. There are two types: NRZ-Level and NRZ-Invert.
- In NRZ-L coding, bit 0 is represented by a positive voltage and bit 1 by a negative voltage.
- In NRZ-I, a change in voltage level represents bit 1 and no change represents bit 0.
- Long runs of 1s and 0s are difficult to detect (more so in NRZ-L).
- Both have a synchronization problem (more so NRZ-L).

## Polar (return-to-zero)

- The problem with NRZ coding is the lack of receiver–transmitter synchronization.
- Return-to-zero uses positive, zero, and negative voltage levels.
- In RZ, the signal returns to the 0 level in the middle of the bit.
- More transitions are needed per bit (more bandwidth).
- There is no DC component problem.

## Polar (Biphase: Manchester and Differential Manchester)
- In Manchester, the signal has specific transitions for bit 1 and bit 0.
- In Differential Manchester, there is a transition at the start of the bit for bit 0 and no transition for bit 1.
- In both, the level is changed in the middle of the bit (synchronization is provided).

## Polar (Biphase: Manchester and Differential Manchester) (2)
- There is no DC component in Manchester and Differential Manchester coding. Each bit has both a positive and a negative voltage.
- The signal rate is twice that of NRZ coding. (The bandwidth is doubled.)

## Bipolar (AMI – Alternate Mark Inversion and Pseudoternary)
- In AMI coding, the level for bit 0 is 0, and for bit 1 it alternates continuously between positive and negative.
- In pseudoternary coding, the level for bit 1 is 0, and for bit 0 it alternates continuously between positive and negative.
- There is no DC component in bipolar coding. The level continuously alternates between positive and negative.

## Multilevel (2B1Q, 8B6T, 4D-PAM5)

- The main goal of coding is to increase the data rate and reduce the bandwidth.
- Let m denote the number of data pieces and n the number of signal pieces.
- Since binary data is 1 and 0, m data bits can be represented by 2^m different signals.
- If each signal has L levels, L^n different signals are obtained.

## Multilevel (2B1Q, 8B6T, 4D-PAM5) (2)

- If 2^m = L^n, one signal can be used for each data pattern.
- If 2^m < L^n, all data patterns can be represented by a subset of the signals.
- If 2^m > L^n, not all data patterns can be represented by the available signals.
- This type of coding is called mBnL.
- Here, m is the length of the binary data, B denotes binary data, n is the length of the signal, and L is the number of signal levels.
- B (binary) is used for L=2, T (ternary) for L=3, and Q (quaternary) for L=4.
- The first two characters (mB) denote the data, and the last two (nL) denote the signal.

## Multilevel (2B1Q)

- In 2B1Q (two-binary, one-quaternary) coding, the data size encoded by one signal is 2 bits and the total number of levels in the signal is 4.
- 2B1Q is used in DSL (digital subscriber line) technology.

## Multilevel (8B6T)

- In 8B6T (eight-binary, six-ternary) coding, 8 bits of data are represented by a three-level signal.
- 2⁸ = 256 different data patterns and 3⁶ = 729 different signals are used.
- Some of the signals are used for synchronization and error detection.
- The signal group used for each bit group is fixed.
- 8B6T is used in 10Base-4T networks.

## Multilevel (4D-PAM5)

- In 4D-PAM5 (four-dimensional five-level pulse-amplitude modulation) coding, "4D" indicates that the data is transmitted over 4 wires.
- 5 different signal levels (-2, -1, 0, 1, 2) are used.
- 8 bits are sent with one signal element.
- The signal is represented by 4 parts, each transmitted over one wire.
- 4D-PAM5 coding is used in Gigabit LAN networks.

## Multiline Transmission (MLT-3)

- NRZ-I and Differential Manchester apply two transition rules when encoding data.
- MLT-3 (Multiline Transmission, Three Level) coding is used for data with more than two levels; MLT-3 uses a three-level (+V 0 -V) transition rule.
- Because there are fewer transitions, the bandwidth is ¼ of the bit rate. (BW = ¼ bit rate)
- If the next bit is 0, there is no transition.
- If the next bit is 1 and the current level is not 0, the next level is 0.
- If the next bit is 1 and the current level is 0, the next level is the opposite of the last nonzero level.

## Multiline Transmission (MLT-3) (2)

*This slide contains only a figure/table; the image is in the original PDF.*


## Summary of line coding methods

*This slide contains only a figure/table; the image is in the original PDF.*


## Block coding

- Extra bits are needed for better synchronization and for error detection.

## Block coding (2)

- Block coding converts m bits into n bits (mB/nB), where n > m.
- The "/" sign distinguishes block coding from multilevel coding (8B6T).
- An m-bit group is replaced by an n-bit group.
- In 4B/5B, the original bits are divided into 4-bit groups and each 4-bit group is replaced by 5 bits.

## Block coding (4B/5B)

- 4B/5B (four binary/five binary) coding is used together with NRZ-I. NRZ-I coding has a synchronization problem with long runs of 0s. A modification is needed before NRZ-I coding so that there are no long runs of 0s. The receiver first recovers the bits with NRZ-I and then discards the redundant extra bit. 4B/5B does not contain more than two consecutive 0s. No group contains more than three 0s.
- The added 1 bit requires 20% more traffic. The DC component is still present.

## Block coding (4B/5B) (2)

- Example: We want to send data at 1 Mbps. What is the minimum bandwidth required when using 4B/5B with NRZ-I, and when using Manchester? 4B/5B increases the bit rate to 1.25 Mbps. Since NRZ-I coding requires a bandwidth of N/2, 625 kHz is needed. Manchester coding requires a bandwidth of 1 MHz. NRZ-I has a DC component; Manchester does not.

## Block coding (8B/10B)

- 8B/10B (eight binary/ten binary) coding uses 10 bits instead of 8 bits.
- It consists of one 5B/6B (for the left 5 bits) and one 3B/4B (for the right 3 bits).
- A disparity controller performs error detection. 2¹⁰ – 2⁸ = 768 extra groups are produced.

## Scrambling

- The biphase method is suitable between two stations over a short distance (within a LAN), but it is not suitable for long distances because it requires a wide bandwidth.
- Using block coding together with NRZ is also not suitable for long distances because of the DC component.
- Bipolar AMI coding requires a narrow bandwidth and has no DC component. However, there is no synchronization during long runs of 0s.
- A series of a certain number of 0s is replaced with a different sequence.

## Scrambling (B8ZS – Bipolar with 8-zero substitution)
- In place of 8 consecutive zero-voltage levels, 000VB0VB is inserted.
- V denotes a violation, i.e., the same voltage level as the previous one in AMI coding.
- B denotes bipolar, i.e., the opposite of the previous voltage level.

## Scrambling (HDB3 – High-density bipolar 3-zero)
- 4 consecutive zero-voltage levels are replaced with 000V or B00V.
- If the number of nonzero pulses since the last substitution is odd, the 000V pattern is used. This makes the number of nonzero pulses even.
- If the number of nonzero pulses since the last substitution is even, the B00V pattern is used. This makes the number of nonzero pulses even.

## Analog-to-digital conversion

- In some applications there is an analog signal (produced by a microphone or camera).
- The analog signal is converted into digital data and then converted into a digital signal.
- Pulse code modulation (PCM) is the most commonly used method for converting an analog signal into digital data.

## Analog-to-digital conversion (2)

- Analog-to-digital conversion has 3 stages:
  - Sampling
  - Quantization
  - Reconstructing the original signal

## Sampling

- The analog signal is sampled at every interval Ts (sampling rate, sampling frequency).
- Three different kinds of sampling are used. Sample and hold (flat-top) is the most common.

## Sampling rate

- According to the Nyquist theorem, the sampling rate must be at least twice the highest frequency.

## Sampling rate (2)

- If the sampling frequency is low, a wheel appears to rotate backwards.
- In a film, 24 frames pass per second. Sampling at fewer than 12 is undersampling.

## Quantization

- The sampled values are analog. The range between the minimum and maximum is divided into L levels. The difference between two levels is Δ = (Vmax–Vmin)/L.
- In the example, Vmax = +20 V, Vmin = -20 V, L = 8.

## Reconstructing the original signal

- The bit sequence is used to recreate the analog signal.

## Delta modulation

- Delta modulation is simpler than PCM.
- If the sampled value is greater than the previous one, an increase is made; if it is smaller, a decrease is made.

## Communication modes

- Communication is either parallel or serial.

## Parallel communication

- n bits are sent at the same time.
- It is costly and fast. It is used over short distances.

## Serial communication

- 1 bit is sent at a time.
- It is low-cost and slow. It is used over long distances.

## Serial communication – asynchronous

- Information is sent in groups. A group usually consists of 8 bits.
- The start bit tells the receiver that a group is arriving, and the stop bit tells it that the group has ended.
- It is asynchronous at the byte level, but synchronization is still required at the bit level.
- A keyboard and a mouse are examples.

## Serial communication – synchronous

- Bits are sent one after another without start and stop bits.
- Dividing the bits into groups and the timing are handled by the receiver.
- It is faster than asynchronous communication.

## Isochronous communication
- In real-time video and audio applications, delays between frames are not acceptable.
- Isochronous communication provides data transmission at a constant rate.

*Note: Superscripts and subscripts in the slides appeared as plain digits in the PDF text (2^m, L^n, 2⁸, 3⁶, 2¹⁰), so they were corrected.*
