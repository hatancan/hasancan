---
baslik: EEM438 Data Communications: Data and Signals (Gazi University, Suat Özdemir)
ozet: Data Communications lecture slides by Suat Özdemir of Gazi University: analog and digital signals, frequency and bandwidth, attenuation, Nyquist and Shannon limits, performance metrics.
---

These are the slides for Chapter 3 (Data and Signals) of the "Data Communications" course prepared by Suat Özdemir of the Computer Engineering Department at Gazi University (slide date 5 March 2011; the footer reads BM 403 Data Communications). They were kept in the EEM438 folder as course material from a second instructor. The slide text is transcribed below; figures and tables taken from the textbook are not published, and slides without text are indicated. The original PDF can be downloaded at the end of the post.

Scope: analog and digital signals, frequency and bandwidth, attenuation, Nyquist and Shannon limits, performance metrics.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*

## Analog and digital signals

- One of the important functions of the physical layer is to carry data over the transmission medium as signals.
- Analog data represents continuous information; digital data represents information with discrete states.
- An analog signal has an infinite number of values in a given time interval (continuous).
- A digital signal has a limited number of values. It generally represents the values 0 and 1 (discrete).

## Analog and digital signals (2)

- A periodic signal continuously repeats the same pattern over a given time interval.
- In a periodic signal, the time interval for one pattern is called the period, and the repeated pattern is called a cycle. Frequency is the number of repetitions in 1 second.
- An aperiodic signal contains no repeating pattern.
- In aperiodic signals, the period is infinite and the frequency is zero.

## Periodic analog signals

- Periodic analog signals fall into two groups: simple and composite.
- A simple analog signal, the sine wave, cannot be decomposed into simpler signals.
- Composite analog signals can be built from simple sine waves.
- A sine wave is described by its amplitude, frequency, and phase.

## Periodic analog signals (2)

- The period is the time a signal takes to complete one cycle, and the frequency is the number of periods in 1 second. f=1/T,T=1/f
- Period is expressed in seconds (s) and frequency in hertz (Hz).
- A signal that never changes has a frequency of 0 and an infinite period.
- A signal that changes instantaneously has a period of 0 and an infinite frequency.

## Periodic analog signals (3)

- Phase describes the position of the signal at time t=0.
- Signals with phase angles of 0º, 90º, and 180º are shown alongside.

## Periodic analog signals (4)

- Wavelength is the distance a signal travels in one period. Its unit is the meter. λ = c/f = c·T (c = 3×10⁸ m/s)

## Periodic analog signals (5)

- The time-domain plot shows the variation of the signal with time.
- The frequency-domain plot shows the relationship between frequency and amplitude.

## Periodic analog signals (6)

- The figure shows two sine waves and a DC signal in the frequency domain.
- The DC signal in the figure has a frequency of 0 and an amplitude of 15.

## Periodic analog signals (7)

- A composite signal is formed by combining many sine waves.
- In the 1900s, Jean-Baptiste Fourier showed that any composite signal is a combination of simple sine waves with different amplitudes, frequencies, and phases.
- f is the fundamental frequency or 1st harmonic, 3f is the 3rd harmonic, and 9f is the 9th harmonic.

## Periodic analog signals (8)

- The figure shows the frequency-domain representation of an aperiodic signal.

## Periodic analog signals (9)

- The frequency range of the signals that make up a composite signal is called the bandwidth.

## Periodic analog signals (10)

- Example: Draw the frequency-domain plot of a periodic signal composed of 5 sine waves of 10 V amplitude at frequencies of 100, 300, 500, 700, and 900 Hz.

## Periodic analog signals (11)

- Example: The bandwidth of a periodic signal is 20 Hz. If the highest frequency is 60 Hz, what is the lowest frequency? Draw the spectrum, given that all components of the signal have the same amplitude.

## Digital signals

- Information can be represented by a digital signal as well as by an analog signal.
- A 1 can be represented by a positive voltage and a 0 by zero amplitude.
- A digital signal can have more than two amplitude levels. For a signal with L levels, each level represents log₂L bits.

## Digital signals (2)

- Most digital signals are nonperiodic.
- Bit rate is the number of bits sent per second (bps).
- Bit length is the distance one bit occupies on the transmission medium. bit length = propagation speed * bit duration
- Example: A file of 100 pages, with 24 lines and 80 columns on each page, is downloaded in 1 second. Given that each character is 8 bits, what is the bit rate? Bit rate = 100*24*80*8 = 1,536,000 bps = 1.536 Mbps
- Example: What is the bit rate for HDTV? An HDTV screen has a 16:9 aspect ratio. The screen has 1920*1080 pixels. Each pixel is represented by 24 bits, and the screen is refreshed 30 times per second. Bit rate = 1920*1080*30*24 = 1,492,992,000 bps = 1.5 Gbps

## Digital signals (3)

- A digital signal is an analog composite signal with infinite bandwidth.
- The figure shows the bandwidth of periodic and aperiodic digital signals.

## Digital signals (4)

- Digital signals can be transmitted as baseband or broadband (using modulation).
- In baseband communication, the digital signal is sent as is (without converting it to an analog signal).
- Baseband communication uses a low-pass channel. The transmission medium forms only one channel.

## Digital signals (5)

- Baseband communication can be carried out over a low-pass channel with limited bandwidth or wide bandwidth.

## Digital signals (6)

- Two devices can communicate very well over a transmission medium with wide bandwidth.
- In the figure, f1 is close to zero and f2 is a very high frequency.
- In baseband transmission of a digital signal, the original shape is preserved. The low-pass channel must have a bandwidth from 0 up to a high frequency.
- In LANs, a single channel is formed and the entire bandwidth is dedicated to communication between two devices.

## Digital signals (7)

- In communication over a transmission medium with limited bandwidth, the digital signal is approximated by an analog signal.
- How closely the resulting signal resembles the original digital signal depends on the bandwidth.
- In the figure, N denotes the bit rate. The maximum frequency of the analog signal is N/2 for the worst case, 1010 or 0101. For the others it is N/4.
- Bandwidth = N/2 – 0 = N/2

## Digital signals (8)

- To make the analog signal resemble the original digital signal more closely, more harmonics must be used. (The bandwidth must be increased.)
- In baseband communication, the required bandwidth depends on the bit rate.
- In baseband communication, the bandwidth must be increased to send data faster.

## Digital signals (9)

- The table gives the bandwidths (B) required to send data at different rates (N).
- In baseband communication, the required bandwidth depends on the bit rate.

## Digital signals (10)

- Example: What bandwidth is required to send data at 1 Mbps using baseband communication? For a low-pass channel, minimum BW = N / 2 = 1 Mbps / 2 = 500 kHz (1st harmonic only). A better BW = 3 * 500 kHz = 1.5 MHz (1st and 3rd harmonics). If the 5th harmonic is used, BW = 5 * 500 kHz = 2.5 MHz (1st, 3rd, and 5th harmonics)
- Example: What is the maximum bit rate over a low-pass channel with a bandwidth of 100 kHz? The maximum bit rate is obtained using the 1st harmonic. BW = N/2, N (bit rate) = 100 kHz * 2 = 200 kbps

## Digital signals (11)

- In broadband communication, the digital signal is modulated and converted to an analog signal.
- Modulation makes it possible to create a bandpass channel.
- Telephone lines are designed for voice signals with a bandwidth of 0–4 kHz.
- With baseband communication, the maximum bit rate would be 8 kbps.

## Digital signals (12)

- In broadband communication, the digital signal must be converted to an analog signal. A modem (modulator/demodulator) is used for this.

## Transmission impairments

- A signal weakens in the transmission medium and does not remain the same as the one sent.
- Signal impairment has three causes: attenuation, distortion, and noise.
- Attenuation is the loss of signal energy due to the resistance of the medium.
- Signal attenuation and gain are expressed in decibels (dB). dB = 10log₁₀ (P2/P1)

## Transmission impairments (2)

- Example: If P2 = ½ P1, what is the attenuation? 10 log₁₀(P2/P1) = 10.log₁₀(0.5 P1/P1) = 10 . (-0.3) = -3 dB
- Example: If P2 = 10P1, what is the attenuation? 10 log₁₀(P2/P1) = 10.log₁₀(10) = 10 . (1) = 10 dB

## Transmission impairments (3)

- Distortion is a change in the shape of the signal.
- The components of a signal all travel at different speeds. They arrive at the destination at different times, and the received signal has a different shape from the original.

## Transmission impairments (4)

- Noise refers to effects that corrupt the signal. Thermal noise, induced noise, crosstalk, and impulse noise can corrupt the signal.
- Thermal noise is caused by the movement of electrons in the wire.
- Induced noise can come from motors or other devices.
- Crosstalk occurs when one cable affects another.
- Impulse noise consists of unpredictable, sudden effects (lightning, etc.).

## Categories of Noise

*This slide contains only figures/tables; the image is in the original PDF.*


## Categories of Noise (2)

- Crosstalk: Impulse Noise:
  - caused by external electromagnetic interferences
  - noncontinuous, consisting of irregular pulses or spikes
  - short duration and high amplitude
  - minor annoyance for analog signals but a major source of error in digital data
  - a signal from one line is picked up by another
  - can occur by electrical coupling between nearby twisted pairs or when microwave antennas pick up unwanted signals

## Transmission impairments (5)

- Signal-to-noise ratio (SNR) is the ratio of signal power to noise power. The figure shows examples of high and low SNR.
- SNRdB is expressed as SNRdB = 10 log 10 SNR.
- Example: If the signal power is 10 mW and the noise power is 1 μW, what are the SNR and SNRdB? SNR = 10,000 μW/1 μW = 10,000, SNRdB = 10log₁₀SNR = 10log₁₀10,000 = 40 dB

## Data rate limits

- The data rate depends on three factors:
  - The bandwidth used
  - The number of levels in the signal used
  - The quality of the channel (the noise level)
- Nyquist determined the data rate for a noiseless channel and Shannon for a noisy channel. Nyquist Bit Rate = 2*BW*log₂L bps BW = Bandwidth, L = Number of signal levels
- As L increases, the reliability of the system decreases.

## Data rate limits (2)

- Example: In a system with BW = 3000 Hz, what is the maximum bit rate if L=2? Bit rate = 2 * BW * log₂L = 6000 * log₂ 2 = 6000 bps. If the number of signal levels is 4, Bit rate = 2 * BW * log₂4 = 6000 * 2 = 12000 bps
- Example: For a bit rate of 265 kbps in a noiseless channel with BW=20 kHz, how many signal levels should be used? 265000 = 2*20000*log₂L → 265000/40000 = log₂L → L = 98.7 levels are required.

## Data rate limits (3)

- In 1944, Claude Shannon determined the theoretical highest bit rate for a noisy channel. Capacity = BW*log₂(1+SNR) bps
- Capacity characterizes a channel, not the communication method!
- Capacity indicates the maximum bit rate regardless of how many levels are used.

## Data rate limits (4)

- Example: What is the capacity of a very noisy channel whose SNR is approximately 0? C = BW*log₂(1+SNR) = BW*log₂1 = 0.
- Example: In telephone lines, BW=3000 Hz (3300–300 Hz). The SNR is usually 3162. What is the channel capacity? C =BW*log₂(1+SNR) = 3000*log₂(1+3162) = 3000*11.62 = 34,860 bps
- Example: What is the theoretical channel capacity of a channel with SNRdB = 36 and BW = 2 MHz? SNRdB = 10log₁₀SNR → SNR = 3981 C = BW * log₂(1+SNR) = 2×10⁶ × log₂(3982) ≈ 24 Mbps

## Performance

- Bandwidth is one of the metrics that determine network performance.
- Bandwidth indicates either a frequency band in Hz or a rate in bps.
- Throughput is the actual bps value of a connection.
- Latency (delay) is the time from when the first bit leaves the source until the entire message arrives at the destination.
- Latency = PT+TT+QT+PD, PT=Propagation time, TT=Transmission time, QT=Queuing time, PD=Processing delay
- Propagation time is the ratio of distance to propagation speed.
- PT = D/PS, D = distance, PS = Propagation speed
- Transmission time is the ratio of message size to bandwidth.
- TT = MS/BW, MS= Message size

## Performance (2)

- Example: For a 2.5 kbyte e-mail on a network with 1 Gbps bandwidth, what are PT and TT? The distance between sender and receiver is 12000 km and the propagation speed is 2.4×10⁸ m/s. PT = (12000×10³)/(2.4×10⁸) = 50 ms, TT = (2500×8)/10⁹ = 0.02 ms

## Performance (3)

- The bandwidth-delay product indicates the number of bits present on the link at the same time.
- Jitter is the variation in delay among different packets.

## Performance (4)

*This slide contains only figures/tables; the image is in the original PDF.*

*Note: In the slide's expression "2*BW*log₂1 = 0", the leading factor 2 does not belong in Shannon's formula; since the result is 0 it does not change, and the text is written as C = BW·log₂(1+SNR). The exponents in the wavelength and calculations (10⁸, 10⁶, 10³, 10⁹) appeared as plain digits in the PDF text and were corrected to superscripts.*
