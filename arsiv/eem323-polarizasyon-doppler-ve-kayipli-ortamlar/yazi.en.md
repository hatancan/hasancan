---
baslik: EEM323 Electromagnetics II: Polarization, Doppler Effect, Low-Loss Dielectrics and Good Conductors (Prof. S. Gökhun Tanyer)
ozet: A text summary of the notes from Prof. Dr. S. Gökhun Tanyer's EEM323 course on the polarization of electromagnetic waves (linear, circular, elliptical), the Doppler effect, plane waves in lossy media, group velocity, and the Poynting vector.
---

This is the text content of three sets of notes that Prof. Dr. S. Gökhun Tanyer covered in his **EEM 323 Electromagnetics II** course (Fall 2013–2014, November 2013): polarization, the Doppler effect, and plane waves in lossy media. The figures and the equations taken from the textbook have not been reproduced.

## 1. Polarization of an electromagnetic wave

The polarization of an EM wave is defined as the **polarization of the electric field**. Depending on the direction of propagation, the wave can be observed from different directions; unless otherwise specified, the viewing direction is looking from the direction in which the wave is propagating toward the wave (i.e., looking at the wave as it approaches the observer). Types of polarization:

- **Linear**,
- **Circular**: clockwise (left-hand polarization, LHP, in the instructor's notation) or counterclockwise (right-hand polarization, RHP),
- **Elliptical**: again clockwise or counterclockwise; for elliptical polarization, the axis tilt is defined.

The slides follow the notation of Balanis (*Antenna Theory*) and Collin (*Antennas and Radiowave Propagation*): the electric field of a wave propagating in the −z direction is written in Cartesian coordinates in the far field, and the linear, circular, and general elliptical cases are distinguished according to the amplitude and phase difference of the x and y components.

**Difference in notation between textbooks (the instructor's emphasis).** The aim of the course is to give students the ability to do research without being bothered by differences in formulation and notation between different books. Example: **Cheng**, used in EEM 224/EEM 323, examines a wave propagating in the +z direction, whereas **Balanis**, used in EEM 423, examines a linearly polarized plane wave propagating in the −z direction. When the phases of the waves propagating in both directions are examined and the two are combined, it can be seen that the arrows indicating the right-hand direction are opposite to each other in the two directions. Important example: for a wave propagating in the +z direction, if the phase difference is positive, the polarization is clockwise (CW), that is, opposite to the right-hand direction. According to the instructor's note, the polarization of a wave propagating in an arbitrary direction is within the scope of EEM 423; in the slides, examples of determining polarization are solved for a wave propagating in the +z direction and, in the far field, in the r direction.

**Assignments and questions:**

- Internet research: investigate the operating principle of 3D TVs and cinemas that require polarized glasses.
- Using MATLAB, plot the electric field vector over time and observe how the polarization changes; show the vector on the polarization diagram at different time values.

## 2. Doppler effect

The effect named after Christian Doppler (1803–1853) is described by the instructor as follows: **as the source approaches the observer**, each successive wave crest is emitted from a position closer than the previous one; thus each wave reaches the observer in slightly less time, the time between the arrivals of successive crests decreases, and the **frequency increases**. During travel, the spacing between successive wavefronts decreases and the waves "bunch up". If the source is **receding**, each wave is emitted from a position farther away than the previous one, so the arrival times lengthen, the frequency decreases, and the spacing between wavefronts widens.

**Question (the instructor's question):** Draw the wavefronts of a wave emitted from a point source: (a) the source is stationary; the source moves to the right at a speed equal to (b) 3/4 of the wave speed, (c) the wave speed, (d) 4/3 of the wave speed.

The notes also show the following applications: the **redshift** of waves from distant galaxies (the shift of lines in the optical spectrum of a galaxy cluster relative to those of the Sun), **ultrasound** Doppler imaging (colored flow in the carotid artery), Doppler weather radar, and police radar. A question the instructor poses for thought: does the Doppler effect also apply to ultrasonic sound waves?

## 3. Plane waves in lossy media (low-loss dielectrics and good conductors)

- **Good dielectrics** are low-loss media, and **good conductors** are high-loss media (σ/ωε is very small or very large). In both extreme cases, simpler solutions are obtained by approximating Maxwell's equations; in media that are neither good conductors nor good dielectrics, **there is no approximation** and the general solution is used.
- **Group velocity** is the velocity of the envelope of a wave packet; **phase velocity** is the velocity of the phase of the waveform, defined in a particular direction. A wave of angular frequency ω along the z axis has the form cos(ωt − βz); the group velocity is calculated from the envelope function of this waveform.
- **Electromagnetic power and the Poynting vector**; wave number and the wave propagation vector; relationships for transverse electromagnetic (TEM) waves.
- At the end of the notes, polarization examples are solved (with complete equation images).

## Source note

This post is a summarized and written-up version of **the instructor's own text content** (headings, explanations, questions, assignments) from the lecture presentations that Prof. Dr. S. Gökhun Tanyer prepared for the EEM 323 Electromagnetics II course (Fall 2013–2014) at Başkent University (OGR-EEM323-DN-2G-Polarisation, 2H-DopplerEffect, 2I-LowLossGoodCond). According to the presentations themselves, the figures, tables, and equation images in them are taken from D. K. Cheng's textbooks (*Fundamentals of Engineering Electromagnetics*, *Field and Wave Electromagnetics*); therefore they are **not reproduced here**, and the original presentation file has not been made available for download. For the figures and detailed derivations, Cheng's book should be consulted.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*
