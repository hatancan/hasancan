---
baslik: EEM442 Communications II Laboratory: Experiment 1 Quantization-PCM, Experiment 2 µ-Law Companding, Experiment 3 Delta Modulation (MATLAB)
ozet: EEM442/444 Communications II laboratory, May 2017: uniform quantization and PCM, theoretical and measured SQNR values, voice signal with µ-law companding, linear and adaptive delta modulation; experiment reports and MATLAB code.
---

Three experiment reports and MATLAB functions prepared for **EEM 442/444 Communications II – Laboratory** (May 2017) at Başkent University. I prepared Experiments 1 and 2; Experiment 3 is a friend's report (name and number removed). The reports and code, with student numbers masked, can be downloaded as a ZIP at the end of the post. A second copy of a friend's identical Experiment 1 report found in the folder, and the `.wav` audio files, have not been published.

## Experiment 1: Quantization – PCM

**Objective:** to implement PCM, one of the baseband digital communication modulations, and the quantization process; to measure quantization noise and SNR values.

**Theory.** Analog-to-digital conversion has two steps: discretization in the time domain (sampling) and discretization in the amplitude domain (**quantization**). In this experiment, a uniform quantizer is examined in MATLAB. If the message is the single tone m(t) = A·cos(2πf_m·t) and the quantization error is assumed to have a uniform probability density, then the message power is ⟨x²⟩ = A²/2, the error power is ⟨e²⟩ = a²/12 (a = 2A/2ⁿ is the step size), and

SQNR_dB = 10·log10((3/2)·2^{2n}) = 1.76 + 6.02·n

(n: number of bits per sample).

**Procedure.** The function `u_pcm.m` is used with a single-tone message: a) the quantized signal is plotted for different numbers of quantization levels; as the number of quantization levels increases, precision and closeness to the original increase (with 8-level quantization the same bit value appears at two different times, whereas with 16 levels different values appear); b) the PCM code is generated for different levels:

```matlab
t = [0:0.01:10];
a = sin(t);
[sqnr8,  aquan8,  code8 ] = u_pcm(a, 8);
[sqnr16, aquan16, code16] = u_pcm(a, 16);
[sqnr32, aquan32, code32] = u_pcm(a, 32);
[sqnr64, aquan64, code64] = u_pcm(a, 64);
subplot(5,1,1), plot(t,a), title('sampled signal');
subplot(5,1,2), plot(t,aquan8),  title('8-level quantized signal');
subplot(5,1,3), plot(t,aquan16), title('16-level quantized signal');
subplot(5,1,4), plot(t,aquan32), title('32-level quantized signal');
subplot(5,1,5), plot(t,aquan64), title('64-level quantized signal');
```

c) The SQNR values are compared with the calculated values:

| Quantization level (Q) | SQNR (calculated) | SQNR (measured) |
|---|---|---|
| 8 | 19.280 | 18.9023 |
| 16 | 25.84 | 25.1272 |
| 32 | 31.86 | 31.3002 |
| 64 | 37.88 | 37.4202 |

*Note: For Q = 8 (n = 3), 1.76 + 6.02·3 = 19.82 dB; the table lists 19.280, which is a typo. The measured values are slightly below the theoretical values.*

**Conclusion.** The result closest to the original sampled signal was obtained with 64-level quantization.

## Experiment 2: µ-Law companding

**Objective:** to implement PCM and quantization with the µ-law companding technique; to measure quantization noise and SNR.

**Theory.** Non-uniform PCM can be realized with uniform quantization by means of compressor and expander structures: compressor → uniform quantizer → expander. For a normalized input with |x| ≤ 1, the µ-law compression function is

y = [ln(1 + µ|x|) / ln(1 + µ)]·sgn(x),

and its inverse (expansion) is

x = [((1 + µ)^{|y|} − 1) / µ]·sgn(y).

**Procedure.** The function `mulaw_pcm.m` is used with a voice signal (µ = 255; Q = 8, 16, 32, 64):

```matlab
x = audioread('history.wav');
x = x(1:50000);
[sqnrmu8,  aquanmu8,  codemu8 ] = mulaw_pcm(x, 8,  255);
[sqnrmu16, aquanmu16, codemu16] = mulaw_pcm(x, 16, 255);
[sqnrmu32, aquanmu32, codemu32] = mulaw_pcm(x, 32, 255);
[sqnrmu64, aquanmu64, codemu64] = mulaw_pcm(x, 64, 255);
```

Measured SQNR (dB): Q = 8 → 8.2776; Q = 16 → 13.4264; Q = 32 → 19.8473; Q = 64 → 25.9201.

**Conclusion.** The result closest to the original voice was obtained at Q = 64 (the original voice is almost audible); as the quantization level decreases, the voice becomes distorted. As the level was increased, precision increased and a result closer to the original voice signal was obtained.

## Experiment 3: Delta modulation (DM)

**Objective:** to implement PCM by means of delta modulation and adaptive delta modulation; to measure quantization noise and SNR.

**Theory.** In PCM each sample is sent with multiple bits, which consumes a lot of power and energy; instead, the *changes* in the signal can be sent: encoding is done according to whether the difference between two samples is positive or negative (delta modulation), so the number of bits per sample is greatly reduced. A **linear DM** transmitter consists of a hard limiter (comparator), a sampler, and an integrator in the feedback path; the receiver has an integrator and a low-pass filter (LPF). Bit pulses are generated according to the sign of the difference between the input and the approximate signal produced by the feedback; the limiter output is sampled at an f_s much higher than the Nyquist frequency. The LPF smooths the discontinuities; the output differs from x(t) because of quantization errors.

Three undesirable effects can occur in DM:
1. At the beginning, x̂(t) needs several steps to catch up with x(t) (**start-up period**).
2. When x(t) stays constant, x̂(t) tracks it with alternating plus and minus steps (**idling noise**).
3. If x(t) changes quickly, x̂(t) cannot follow it because it can only change by ±Δ (**slope overload**).

**Adaptive DM** was developed for these problems: the step size is adapted at every sampling instant. The quantized difference sequence gives information about the slope of the waveform: if successive signs alternate, the slope is small; if they have the same sign, the slope is steep. According to Jayant's simple rule, Δ(n) = Δ(n − 1)·K^{ε(n)·ε(n−1)} (K: a constant that minimizes local distortion, K > 1).

**Procedure.** The files `delta_mod.m` and `adpt_delta_mod.m` are used with a voice signal; linear DM is tried for Δ = 1, 0.1, 0.01, and 0.001. **Conclusion:** SQNR increased as Δ became smaller, but at the last value SQNR dropped again because of slope overload.

## MATLAB code (the `kod/` folder in the ZIP)

The functions are `u_pcm.m` (uniform PCM), `mulaw.m`, `invmulaw.m`, `mulaw_pcm.m`, `delta_mod.m`, `adpt_delta_mod.m`, and example scripts. The two core functions:

```matlab
function [ sqnr, a_quan, code ] = u_pcm( a, n )
% uniform PCM encoding of a sequence; n = number of quantization levels
amax = max(abs(a));
a_quan = a/amax;
b_quan = a_quan;
d = 2/n;
q = d.*[0:n-1];
q = q-((n-1)/2)*d;
for i=1:n
    a_quan(find((q(i)-d/2<=a_quan) & (a_quan<=q(i)+d/2)))= q(i).*ones(1,length(find((q(i)-d/2<=a_quan) & (a_quan<=q(i)+d/2))));
    b_quan(find( a_quan== q(i) )) = (i-1).*ones(1,length(find( a_quan== q(i) )));
end
a_quan = a_quan*amax;
nu = ceil(log2(n));
code = zeros(length(a),nu);
for i = 1:length(a)
    for j=nu:-1:0
        if ( fix(b_quan(i)/2^j) == 1)
            code(i,(nu-j)) = 1;
            b_quan(i) = b_quan(i) - 2^j;
        end
    end
end
sqnr = 20*log10(norm(a)/norm(a-a_quan));
end
```

```matlab
function [X_quan, sqnr]=delta_mod(X,delta)
l = size(X,2);
Y_quan = zeros(1,l);
X_quan = zeros(1,l);
if X(1) >= 0, epsi = 1; else epsi = -1; end
Y_quan(1) = epsi * delta;
X_quan(1) = Y_quan(1);
for n = 2:l
    if X(n) >= X_quan(n-1), epsi = 1; else epsi = -1; end
    Y_quan(n) = epsi * delta;
    X_quan(n) = X_quan(n-1) + Y_quan(n);
end
sqnr = 20*log10(norm(X)/norm(X-X_quan));
```
