---
baslik: EEM441 Communications I: MATLAB and Simulink AM Study
ozet: A MATLAB script for AM modulation of a square wave and a Simulink model that builds the message–carrier product.
---

The Simulink model dated 21 November 2011 and the MATLAB script from the same AM preparation folder were archived together. The source files, with computer/user metadata removed, can be downloaded as a ZIP. The code was not run.

## MATLAB script

```matlab
Fs = 1e7; % Sampling rate is 8e6 samples per second.
Fc = 1000000; % Carrier frequency in Hz
t = [0:.1*Fs]'/Fs; % Sampling times for .1 second
t = [-10:0.2:10];
duty = 50;
x = square(t,duty); % Representation of the signal
plot(x)
y = ammod(x,Fc,Fs); % Modulate x to produce y.
figure;
subplot(2,1,1); plot(t,x); % Plot x on top.
subplot(2,1,2); plot(t,y)% Plot y below.
```

*Note: In the source, the sampling rate is 10 million, while the comment says 8 million samples/second. The numbers were only converted to scientific notation; this discrepancy is preserved. The first time vector is overwritten by the subsequent `t` assignment. The argument of `square(t,duty)` is in radians; the step of this vector and the Fs given to `ammod` do not describe the same sampling arrangement. Therefore, the plot axis and the time base of the modulation should not be assumed to be consistent.*

## Simulink model

The model is named `eem441`, version 7.0, with start time 0 and stop time 10. The message generator's frequency field is 167, the carrier generator's frequency field is 100, and the constant block value is 0. The message and the constant are summed and then multiplied by the carrier. The message, the carrier, and the output each go to separate Scope blocks. The sample time of the Product block was saved as 0.001.

Text representation of the connections:

```
Message ──┬── Message Scope
          └── Sum ── Product ── Scope
Constant ────┘         │
carrier ──┬────────────┘
          └── Carrier Scope
```

The constant being zero indicates that no DC carrier component is added on top of the message. The frequency fields written in the file are transcribed here as they are; without seeing the unit setting, they have not been assumed to be in Hz.
