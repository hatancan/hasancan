---
baslik: EEM311 Electronics II: 2005 Laboratory Handouts and Differences from the 2010 Version
ozet: Differences between the EEM311 Electronics II laboratory handouts of the 2005 fall semester and the 2010 version: corrected formula and value errors (V_T, C_E, I_D formula), changed input amplitudes, measurement resistor, added notes, and rearranged experiment steps.
---

This post covers the **2005 fall semester** experiment handouts of the **EEM311 Electronics II** laboratory in the Electrical-Electronics Engineering Department at Başkent University. The handouts continued to be used in later years with minor corrections; the detailed posts in the archive (Experiments 1–2, 3–4, 5–6, 7–8, and the laboratory information booklet) are based on the **2010** version. For this reason, the 2005 handouts are not reproduced here from scratch; only the differences between the two versions are collected. The 2005 handouts were prepared between October and December 2005; the files were password-protected, and copies with the password removed can be downloaded as a ZIP at the end of this post.

## General differences

- At the bottom of the pages, the 2005 handouts show the course's web address as *www.baskent.edu.tr/~kocaturk*, while the 2010 handouts show *www.baskent.edu.tr/~ozparlak*.
- The experiment topics, circuit values, and result forms are largely the same in both versions. The 2010 version is somewhat better organized (sub-items are separated as a/b/c, lines have been added to the result forms), and the µ symbols have been corrected.
- The two versions of Experiment 2 (single-stage BJT amplifier design) are identical, apart from the web address.
- The laboratory rules booklet used in 2008 (*EEM311_LabKurallari.pdf*) already appears in the archive in the post *Laboratory Information Booklet*; the copy in Dropbox is the same file.

## Experiment 1: Single Stage BJT Amplifier

- In the 2005 handout, the thermal voltage at room temperature was mistakenly written as **V_T ≈ 0.0025 mV**; in the 2010 handout it is corrected to **25 mV**.
- In the 2010 version, the words "undistorted" and "unclipped" are placed in quotation marks; the theory and steps are the same.

## Experiment 3: Single Stage MOSFET Amplifier

- In the input and output impedance measurement (Figures 6 and 7), the series measurement resistor in the 2005 handout is a fixed **R_x = 1 kΩ** resistor; in the 2010 handout it is a **50 kΩ potentiometer**. In 2010, a 50 kΩ pot and a 10 µF capacitor were also added to the parts list.
- Two notes were added to the 2010 handout: the wires connecting the transistor terminals should be kept as short as possible; and the DC supply should be turned on before, and turned off after, the AC signal.
- The signal generator setting is written as "approximately 50 mV" in 2005 and "50 mVp-p" in 2010; in the measurement steps, the source voltage is named *v_x*.
- Step 2 of the experimental work was divided into sub-items a/b/c in 2010, and the sentence "Rebuild the amplifier in Figure 1" was added to step 3 (to restore the circuit after the step in which C_S was removed).

## Experiment 4: Two Stage Amplifier Circuit

- In the 2005 handout, step 3 was split into two parts: a) the largest undistorted peak-to-peak output; b) setting the signal generator to a **triangular wave** and measuring the largest output swing at which clipping begins. In the 2010 handout, part b was removed, and only the swing at which distortion begins is measured. The "v_out,undistorted(unclipped) max" row in the result form was also removed.

## Experiment 5: MOSFET Current Mirror

- In the 2005 handout, the expressions for I_D1 and I_D2 are **missing the ½ coefficient**: I_D = µ_n·C_ox·(W/L)·(V_GS − V_t)²·(1 + λV_DS). In the 2010 handout, the correct form is given as I_D = ½·µ_n·C_ox·(W/L)·(V_GS − V_t)²·(1 + λV_DS).
- In the result form, 2005 had a separate "Part 2/Part 3" layout for R_O, whereas in 2010 the R_O row was moved to the M1 column; the word "lab" became "experiment".

## Experiment 6: CMOS Common-Source Amplifier with an Active Load

The PDF of the 2005 handout could not be opened with the password in the folder (the password of the other handouts); therefore it could not be compared and was not included in the ZIP. The file size is almost the same as that of the 2010 handout (167,109 and 167,191 bytes), so the content is most likely the same as well.

## Experiment 7: BJT Differential Pair Amplifier

- In the theory section, for the DC analysis the 2005 handout says "I_C1 = I_C2 = I_EE"; in the 2010 handout the correct form is given as **I_C1 = I_C2 ≈ I_EE/2**.
- The common-mode input resistance expression was mistakenly named **R_id** = v_icm/(2i_b) in 2005; in 2010 it is **R_icm**.
- In the common-mode simulation in the preliminary work, the amplitude of the sinusoid applied to the two bases is **2 V** in 2005 and **4 V** in 2010.
- In step 5 of the experimental work, the common-mode input is **4.0 Vp-p** in 2005 and **8.0 Vp-p** in 2010.
- In step 3, the 2005 handout asks for the 100 mVp-p input to be obtained with the voltage divider in Figure 7 and says "connect it to v_in2, ground v_in1". In the 2010 handout, the divider sentence was removed and the sentence was left incorrectly as "connect it to v_in2 and ground v_in2" (this was corrected as a note in the 2010 post); the wording in the 2005 handout is the correct one.
- In the result form, the bias rows for Q_B and Q2 were moved to the end of the table in 2010.

## Experiment 8: Frequency Response of Common Emitter Amplifier

- In the preliminary work table, the emitter bypass capacitor is given as **C_E = 10 µF** in the 2005 handout, whereas the parts list has 100 µF. In the 2010 handout, the table was also corrected to **100 µF**. (For this reason, in some student work from 2008, the simulation was done with C_E = 10 µF.)
- The condition under which the effect of r_x can be neglected is posed in 2005 as "I_BQ ≫ ?" and in 2010 as "**I_BQ ≪ ?**".
- In the 2005 handout, the source is named *v_s* (through R_s), and in the 2010 handout *v_in*; the source drawing in Figure 2 changed accordingly, and two oscilloscope grids were added for the input/output waveforms.
- **500 Hz, 1 kHz, and 10 kHz** were added to the frequency sweep list in 2010; the table header became "v_out" instead of "v_out (peak)".
- In 2010, step 3 was divided into a (measuring the cutoff frequencies) and b (the frequency response curve).
- Step 4 (removing C_E) was a single paragraph in 2005; in 2010 it was divided into three sub-steps: a) adjusting the input for an undistorted output at 1 kHz, measuring the midband gain, and **comparing it with the PSpice result**, b) measuring f_H and f_L, c) commenting on the changes.

## Other files in the folder

The PSpice library files distributed with the 2005 handouts (*jfet.lib*, *jfet.ind*, *cd4007.ind*), the 2N4860 datasheet, the standard resistor values table, and the "how to add an include file" guide were not included in this post.
