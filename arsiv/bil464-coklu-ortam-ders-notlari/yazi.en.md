---
baslik: BIL464 Multimedia Systems: Digital Technology (Sampling, Quantisation, Data Storage and Communication) and Text
ozet: Notes from Mustafa Sert's (Başkent University) BIL464 Multimedia Systems course: analog-to-digital conversion, Nyquist, quantisation error and SNR, data sizes, bandwidth, bit rate and baud rate, character sets, typefaces and typographic measures.
---

**BIL464 Multimedia Systems (Multimedia Systems)** — the first two lecture notes of the course: *Lecture 01 – Digital Technology* and *Lecture 02 – Multimedia Data Types: Text*. The notes are the lecture slides of **Asst. Prof. Dr. Mustafa Sert** from the Department of Computer Engineering at Başkent University (BIL464 Multimedia Systems, 2012). The folder was named "Computer Course"; the real name of the course, Multimedia Systems, can be understood from the title of the slides. The originals of the two presentations can be downloaded as a ZIP at the end of the post. The content below is given as a summary in English.

## Lecture 1: Digital technology

### Analog and digital

Analog signals are continuous signals (flowing water, a line on a graph, a continuously turning radio dial): there are infinitely many other points between any two points. Discrete signals, on the other hand, are clearly separated from one another. A live orchestra produces analog sound waves; a standard microphone is an analog device and transmits sound as a continuous voltage wave that varies with time. In a computer, continuous signals have to be represented by a sequence of numbers: this is called **analog-to-digital conversion** and consists of two steps.

1. **Sampling**: taking samples from the continuous signal at discrete points. The number of samples per unit time or space is the **sampling rate** (resolution), whose unit is Hertz (1 Hz = one sample per second; kHz is often used). In images the sample points are equally spaced in space, and in sound they are equally spaced in time.
2. **Quantisation**: representing each sample with a fixed number of bits (the sample size, or **bit depth**). Typically 8 bits (256 levels) or 16 bits (65,536 levels) are used. The device that performs the conversion is called an **ADC (analog-digital converter)**.

When the digital signal is played back it has to be reconstructed; a common technique is **sample and hold**. Enough samples and enough levels are needed for a signal close to the original.

### Nyquist and aliasing

**Nyquist sampling theorem**: to be able to reconstruct the signal, the sampling rate must not be less than twice the highest frequency in the signal. For example, if the highest frequency is 3000 Hz, the sampling rate must be at least 6000 Hz. If it is undersampled, some frequency components are mistakenly turned into other frequencies: **aliasing**. In the example in the slides, a 637 Hz sound wave sampled at 770 Hz is reconstructed as a wave of lower frequency and sounds different.

### Quantisation error and SNR

If the number of levels is small, there is a large error in each sample: the sample is rounded to the nearest discrete level, and the difference between the true value and the rounded value is the **quantisation error**. The magnitude of the error is measured by the **signal-to-noise ratio (SNR)**; as the resolution increases the noise decreases and quality increases. The decibel definition is 10·log10(I/I0) for power and 20·log10(E/E0) for amplitude/voltage (the two are equivalent for constant R; log10(x²) = 2·log10(x)). SNR by bit depth: **about 48 dB for 8 bits, about 96 dB for 16 bits**.

### Data storage

Working with digital media requires processing a lot of data. The slides tabulate the sizes of typical image, audio and video files (three bytes per pixel for RGB colour; in video about 30 frames per second, each frame like a still image). A note on prefixes: kilo/mega/giga are used as 2^10, 2^20, 2^30 for memory sizes; and as 10^3, 10^6, 10^9 for Hertz and data rates. Manufacturers use powers of 10 to make media look larger; computers, on the other hand, express file size in powers of 2 (for example 3,686,456 bytes ≈ 3600 kB ≈ 3.52 MB). In the course, powers of 2 are assumed for memory and file sizes, and powers of 10 for data rates. The capacities of storage media are then listed.

### Data communication

Digital media files are large and are shared (CD/DVD, e-mail, web page); audio and video are **time-dependent** media: capture and transmission must keep up with the playback rate. This is why bandwidth and data rate matter. The slides give three definitions of bandwidth:

1. **The maximum rate of change in digital data communication**: in a system with bandwidth b Hz and two signal levels, the data rate is d = 2b (bit/s); in a system with k levels, **d = 2b·log2(k)**.
2. **The bandwidth of a signal in terms of frequency**: w = f_max − f_min. Example: for a signal with components of 262, 330 and 392 Hz, w = 392 − 262 = 130 Hz.
3. **The bandwidth of a communication channel**: the range of the frequency band allocated to the channel (with examples from radio and television bands).

The **data (bit) rate** is in bit/s; bandwidth, on the other hand, is in Hz. d = 2b·log2(k) is a theoretical upper limit; noise limits the actual rate. For a noisy channel, the **Shannon theorem**: **c = b·log2(1 + s/p)** (s: signal power, p: noise power). The slides tabulate the data rates of common communication links and storage devices.

**Baud rate**: in its most precise definition, the number of signal changes per second, as a property of the sending and receiving devices; it is synonymous with bandwidth, not with bit rate: the relation d = 2b·log2(k) links baud rate and bit rate. In practice, the so-called "56 kb/s baud rate" of modems is actually a bit rate.

## Lecture 2: Multimedia data types: text

Contents: what text is, character sets, typefaces and fonts, outline and bitmap fonts, use of text in multimedia.

**Text** is a vital element of multimedia presentations and is also the visual representation of language and a graphic element in its own right; the field that studies how text is displayed is called **typography** (character shapes, spacing, line and paragraph layout).

### Character sets and encoding

Abstract characters (letters, digits, punctuation) are grouped into alphabets. For representation in a computer, a mapping between characters and stored values is needed: the **character set**. A common character set is essential for systems to communicate.

- **ASCII** (American Standard Code for Information Interchange): 7 bits, at most 128 characters; 95 printable characters, with 0–31 and 127 being control characters. ISO adopted it as the ISO 646 standard.
- **ISO 8859**: 8-bit characters, many parts; the lower 128 characters of each part are the same as ASCII.
- **Unicode**: Unicode Standard 1.0 in 1991; at the time of the slides the latest version was 6.2 (2012, ISO/IEC 10646:2012 and the Turkish lira symbol). It tries to cover all the languages of the world; the number of Chinese characters is more than 27,484 (before that, GB2312-80: 6763 simplified characters, Big5: 13,053 traditional characters, CNS11643-1992: 48,027, HKSCS: adds 3049 characters to Big5).
- **Encoding**: an additional level of mapping in which a code value is converted into a byte sequence for storage and transmission.

### Typeface and font

A **typeface** is a family of graphic characters with a consistent design, often including many sizes and styles; a **font** is a set of graphic characters in a particular design, size and style (for example, the typeface "Arial", the font "Arial Narrow 24 point").

Character measures: every character has a bounding box; the origin is usually on the baseline, and the width of the character determines the origin of the next character. The distance between the origin and the left edge of the box is the **left side bearing**. The upward-extending (b, h) and downward-extending (g, p, q) parts of lowercase letters are called the **ascender** and **descender**; the height of lowercase letters without these is the **x-height**, and the height of capital letters is the **cap-height**.

Five attributes are used to specify a font: **family** (Times, Helvetica, Courier, Garamond, Univers), **shape** (upright, oblique, italic, small caps), **weight** (light … bold), **width**, and **size** (point: in print 1 inch = 72.27 points, in PostScript systems 72 points).

**Bitmap and outline fonts**: bitmap fonts are of a specific size and resolution and look very poor when scaled; outline fonts contain the outlines of the characters and scale smoothly over a wide range of sizes, but rasterisation is required to display them on screen. Today outline fonts are widespread (two kinds: PostScript and TrueType).

**Text layout**: *leading* is the distance between two baselines (14 points for 12-point text, 12 points for 10-point text); *tracking* is the spacing between characters; *kerning* is the additional adjustment between two specific characters (for example A and v).

### Recommendations for using text in multimedia

- For small text, choose the most legible font; decorative fonts are of no use.
- Use as few typefaces as possible in the same work; vary them with weight, size and italic/bold.
- Change the text size in proportion to the importance of the message.
- Apply correct kerning in large headings.
- Experiment with the effects of different colours and of placing text on different backgrounds.
