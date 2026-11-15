---
baslik: EEM441 Communications I: AM and FM Laboratory Preliminary Work
ozet: Preparations for AM, DSB-SC, VCO, and the superheterodyne receiver; examples of generating FM signals with MATLAB.
---

These preliminary works for the EEM441 laboratory cover AM and FM signals, the superheterodyne receiver, VCO types, and MATLAB plots. Works dated 30 December 2010, 22 November 2011, and 6 December 2011, together with undated supplementary pages, have been brought together. PDF copies with student information removed can be downloaded at the end of the post.

## AM and DSB-SC Preparation

The 22 November 2011 exercise modulates the square-wave message from the lab handout onto a 1 MHz carrier. In the first part, the message, the carrier, and the double-sideband output with carrier are plotted; in the second part, the double-sideband suppressed-carrier output of the same message is plotted.

For full AM, the signal is s(t) = Ac[1 + ka m(t)] cos(2πfc t). In the DSB-SC example, the message is multiplied by the carrier; where the message changes sign, the phase of the carrier is reversed.

The modulation index pages define m = Vm/Vc and the modulation percentage as 100m. From the maximum and minimum values of the envelope on the oscilloscope, m = (Vmax − Vmin)/(Vmax + Vmin) is found. m = 1 corresponds to 100% modulation; m > 1 corresponds to distortion in envelope detection. For single-tone double-sideband AM, BW = 2fm.

## Superheterodyne, Costas, and Synchronous Receivers

The superheterodyne receiver mixes the signal that has passed through the antenna and the RF filter with a local oscillator to shift it to a fixed intermediate frequency. Amplification and filtering are performed at the intermediate frequency, followed by demodulation. In this way, the same intermediate-frequency stage can be used while selecting different broadcasts.

The supplementary page also mentions the Costas receiver and the synchronous detector. The DSB-SC signal is multiplied by a suitable carrier and passed through a low-pass filter to recover the message. For AM, radio and two-way radio (walkie-talkie) uses are given.

## VCO Types and AM–FM Comparison

A VCO is an oscillator whose oscillation frequency changes with a control voltage. For high-frequency applications, examples include a varactor connected to an LC tank; for low frequency, a current source that changes the charging rate of a capacitor. Series and parallel Colpitts, Clapp, and Hartley oscillators are listed. Colpitts and Clapp are described with capacitive feedback, and Hartley with inductive feedback. Where a small frequency adjustment is required, the VCXO is mentioned.

In AM, the message varies the carrier amplitude; in FM, it varies the instantaneous frequency. The ideal FM envelope is constant. Whereas AM has two sidebands, single-tone FM has many sidebands. In FM, the bandwidth depends on the frequency deviation and the message bandwidth.

## FM with Numerical Integration

The MATLAB code of the undated preliminary work is as follows:

```matlab
Ac = 1;
Am = 5;
fm = 10;
fc = 100;
kf = 100;
t = 0:0.00001:0.2;
m_t = Am*cos(2*pi*fm*t);
integral_m_t = cumtrapz(t,m_t);
s_t = Ac*cos(2*pi*fc*t + kf*integral_m_t);
figure(1); plot(t,m_t); title('Mesaj Sinyali');
figure(2); plot(t,integral_m_t); title('Mesaj Sinyalinin Integrali');
figure(3); plot(t,Ac*cos(2*pi*fc*t)); title('Tasiyici Sinyal');
figure(4); plot(t,s_t); title('Moduleli Sinyal');
```

The plots cover the interval 0–0.2 seconds. The amplitude of the message is 5 and the amplitude of the carrier is 1; the peak value of the integral plot is approximately 0.08. In the 6 December 2011 version, Ac = 10 and Am = 20 were chosen; the same `integral_m_t` variable is used, but the line that computes this variable is missing from the document.

*Note: Although the document gives Hz for kf, this code, which adds kf∫m(t)dt directly to the phase, uses kf as an angular-frequency sensitivity. If a Hz/unit sensitivity is intended, a factor of 2π is needed in the phase term. The source code has been transcribed without modification; it has not been run.*

## fmmod Example

The second approach in the 30 December 2010 work:

```matlab
Fs = 300;
Fc = 100;
t = [0:Fs]'/Fs;
x = sin(2*pi*300*t);
dev = 50;
y = fmmod(x,Fc,Fs,dev);
figure();
xlabel('fc = 100Hz');
ylabel('fs = 300Hz');
plot(t,y);
```

*Note: The cover page says EEM401; it has been kept here because the file is in the EEM441 archive. Sampling a 300 Hz sinusoid again at 300 Hz makes all samples zero in ideal arithmetic; this code is not an example of correctly sampling the message. The generalizations in the source, such as "FM always requires less power," "the AM index is always 1," and that AM zero crossings carry the message, are also not unconditionally valid.*
