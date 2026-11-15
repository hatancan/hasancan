---
baslik: EEM424 Microwave Theory: Electromagnetic Wave Propagation - Dispersion Effect Project Report (Square and Triangular Wave, MATLAB)
ozet: The 2015 project report for EEM424 Microwave Theory by two friends: the distortion that square and triangular signals undergo in dispersive propagation; concept and operation, work breakdown structure, work schedule, interim research results and MATLAB code. Personal information has been removed.
---

This post describes the project report that two of my friends prepared in the **EEM 424 Microwave Theory** course (Prof. Dr. S. Gökhun Tanyer), titled "Electromagnetic Wave Propagation – Dispersion Effect" (April 17, 2015), together with the additional documents in the project folder. Student names and numbers have been removed, and the report pages have been masked. The masked report and the MATLAB files can be downloaded as a ZIP at the end of the post.

## Concept and Operation

1. The effects of the **amplitude distortions that square and triangular input signals may undergo during EM wave propagation** on the wave will be examined.
2. The following topics are researched through open-source review: Fourier series/transform, fast Fourier transform, discrete Fourier transform, distortion, dispersion, channel modeling, channel equalization.
3. A square wave and a triangular wave are given as inputs; the wave parameters and attenuation functions are determined.
4. Outputs: the time-domain representation of the input waveforms, the frequency spectrum, the waveforms at a specified distance (on a single plot), and the frequency spectrum of the waveforms at that distance (on a single plot).
5. **Version 1:** all inputs are entered manually into the program text and run. **Version 2:** inputs are entered through a graphical interface.
6. The project report is prepared.

## Work Breakdown Structure and Work Schedule

Tree: 1.0 EM wave propagation – dispersion effect → 1.1 preparatory work (open-source research) → 1.2 Version 1 work (manual entry of inputs into the software) → 1.3 Version 2 work (entry of inputs through a graphical interface) → 1.4 compilation → 1.5 tests → 1.6 preparation of documents.

Schedule: Week 7: concept and operation, work breakdown structure; Week 9: preparatory work, completion of Version 1; Week 10: preparation of the inputs in MATLAB; Week 11: obtaining the outputs in MATLAB; Week 12: completion of Version 2 and report in article format; Week 13: project submission.

## Interim Research Results

- **Fourier series / transform:** expands a periodic function into an infinite series of sines and cosines; Fourier first used it for the heat equation in a metal rod or plate. The transform converts a time-domain signal into the frequency domain. Another study summarizes converting the Fourier series to exponential form via Euler's expansion and using the transform to represent non-periodic signals in phasor space.
- **FFT:** an algorithm used in the discrete Fourier transform to convert time-domain signals to the frequency domain (Cooley–Tukey is the most common, and its logic is based on Gauss's work); the data must be sampled at equal intervals.
- **Discrete Fourier transform:** equal to samples of the Fourier transform at equally spaced frequencies; it provides evaluation for a finite number of points.
- **Distortion:** a deformation in signal amplitude; harmonics that are not present at the input appear in the output signal, and their ratio to the signal is expressed in dB. It has types such as amplitude, frequency, phase, harmonic, and group velocity distortion; it is frequently used in music (electric guitar), whereas in communications it is an effect that one tries to prevent.
- **Nyquist rate:** the minimum sampling rate required to avoid aliasing in band-limited signals (twice fmax).
- **Dispersion:** the distortion in the waveform caused by the components of different wavelengths that make up a signal traveling at different phase velocities; it is observed in acoustic, optical, communication, seismic, and ocean waves.
- **Channel modeling:** modeling the environmental conditions of a channel sufficiently well before the coding and processing stage (saving performance, cost, and time). **Channel equalization:** used to reverse the distortions that occur in a signal transmitted through a channel.
- **Radar pulse duty factor:** the ratio of pulse duration to the gap duration.

## MATLAB Code

Triangular and square wave inputs (`ucgen-dalga.m` and `kare-dalga.m` in the ZIP):

```matlab
fs = 1000;
t = 0:1/fs:1;
x1 = sawtooth(2*pi*50*t);
plot(211),plot(t,x1), axis([0 0.2 -1.2 1.2])
xlabel('Zaman (san)');
ylabel('Genlik');
title('Ucgen Dalga');
```

```matlab
fs = 10000;
t = 0:1/fs:1.5;
x1 = square(2*pi*50*t);
subplot(211)
plot(t,x1)
axis([0 0.2 -1.2 1.2]);
xlabel('Zaman');
ylabel('Genlik');
title('Kare Dalga');
```

A 50 Hz square wave and triangular (sawtooth) wave are generated and the first 0.2 seconds are plotted; the generated figures are also included in the ZIP as PNG files. The code in the folder only generates the input waves; the dispersive propagation calculation (the waveform at a given distance) is left to Version 2, which is not in the folder, and the report contains only the concept, schedule, and interim research results.

*Note: The names and numbers on the report cover have been removed. The folder also contained project files for a different course (BME 314), a three-phase circuit assignment titled "ÖDEV 3" (Homework 3), and a course slide deck; these are not included in this post.*
