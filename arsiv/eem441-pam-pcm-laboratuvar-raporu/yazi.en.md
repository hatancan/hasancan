---
baslik: EEM441 Communications I: PAM and PCM Laboratory Report (EEM442 Document)
ozet: An anonymized laboratory report on sampling, quantization, coding, and time-division multiplexing.
---

The cover of this peer-submitted work, found in the EEM441 folder, reads EEM442. The report, which describes the PAM and PCM experiment, has been archived with personal information removed. The source file's date was used for this undated document; the report and the anonymized cover page can be downloaded at the end of the post.

## PCM: Sampling, Quantization, and Coding

Pulse code modulation is explained in three stages: sampling the analog signal, quantizing the samples to a finite number of levels, and converting the levels into binary code words. One sample is drawn for Q = 8 levels, n = 3 bits, and a = 1.

In the experiment, the word length and bit rate are adjustable. The oscilloscope's first channel is connected to the demodulator output and the second channel to the trigger signal. A staircase waveform is observed at the output; it is noted that the step height remains constant when the input amplitude is changed.

The rightward shift of the output waveform when the bit rate is reduced is explained by the delay of the demodulator, which must wait to receive all the bits of a word. The report also states explicitly that not all of the expected results could be obtained because of a problem with the PCM demodulator.

## PAM and Time-Division Multiplexing

In PAM, the pulse amplitudes follow the sample values of the message. The report uses flat-top sampling. Placing samples from different channels into the gaps between short pulses is described as TDM, that is, time-division multiplexing.

The distributor switches at the transmitter and the receiver must be synchronized. At each rotation of the transmitter switch, one sample is taken from the corresponding signal; the receiver switch simultaneously routes this sample to the correct output channel.

## Sampling Condition

The message bandwidth is denoted fm, the sampling period Ts, and the sampling frequency fs = 1/Ts. The condition fs > 2fm is used to recover a band-limited message. The samples are passed through an ideal low-pass filter. Since practical filters are not ideal, it is noted that a margin above the Nyquist limit must be left.

*Note: The report's statement that "digital signals are not affected by noise" is not true in an absolute sense; exceeding the decision thresholds produces bit errors. Not all forms of PAM use flat-top sampling. The historical claim that PCM emerged only in the 1970s is the source's own assertion and should not be taken as a verified date.*

## Sources Cited in the Report

The report lists the MEGEP Analog and Digital Communications course notes, KTÜ telecommunications lab sheets, Hasan Balık's communications laboratory page, and the GYTE experiment sheet.
