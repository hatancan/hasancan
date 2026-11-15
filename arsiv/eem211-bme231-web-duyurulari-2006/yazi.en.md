---
baslik: EEM211 Digital Logic Design: Course Announcements, Project Guidelines, and PROM–PAL–PLA Examples (Başkent, Mehmet Yüksekkaya)
ozet: Text transcription of the 2006 BME231 course topics, project criteria, and programmable logic examples.
---

This is the 2006 record of the Başkent University Mehmet Yüksekkaya course page, together with the project announcement due on Wednesday, December 27. The course code on the source page is BME231; because the documents are stored in the EEM211 folder, it appears under EEM211 in this archive. A text-only copy of the two HTML pages (without images) can be downloaded together at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*

## Course Topics

Starting September 28, 2006, the course page lists number systems, Boolean algebra and logic gates, Boolean functions and simplification, Karnaugh maps, gate-level simplification, and combinational circuits.

The November 6 announcement lists the following as study topics: binary, BCD, and the code written in the source as "Axes-3"; conversions between codes; minterm and maxterm representations; and Karnaugh map simplification in product-of-sums form by grouping the zeros.

*Note: The expression "Axes-3" in the source refers to the Excess-3 code.*

## Homework and Quiz Schedule

| Announcement | Content |
| --- | --- |
| September 28 | Computation for a word, based on the signed/unsigned number ranges given for a byte; due October 4 |
| October 5 | The second homework will not be graded; the related questions will appear on the October 11 quiz |
| October 16 | Quiz 1 solutions |
| October 26 | Third homework; due November 1 |
| November 4 | Third homework solutions |
| November 9 | Fourth homework; due November 15 |
| November 17 | Fourth homework and Quiz 2 solutions |

In the first homework, the unsigned byte range is given as 0–255 and the signed byte range as −128–127. Students are asked to write out the calculations, not only the results. The source does not separately define the word length in this announcement.

## Digital Integrated Circuit Research Project

The report is first expected to explain digital integrated circuits and their main electrical characteristics. Total maximum output, power dissipation, time delay, and noise values are given in the announcement as example parameters.

In the second part, the function and features of a selected digital integrated circuit are examined. The characteristics defined in the general section are interpreted for this specific device. The aim is to learn which features to look at when choosing a needed digital component, and how to research this information.

## Report Requirements

- It must contain sufficient explanation and source information.
- The datasheet of the selected component must be used as the primary research source.
- A few datasheet pages showing the features must be attached to the report.
- The final deadline is the class hour on Wednesday, December 27, 2006.
- The announcement states a 25% point deduction for each day of delay.

These are the historical guidelines of the assignment in the archive. The datasheets and textbook sections have not been added to this publication.


## Additional Work: PROM, PAL, and PLA

The scanned page titled "BME 231 Examples — Instructor: Mehmet Yüksekkaya" from the same BME231 collection also contains a friend's handwritten explanations. The page carries no date; it has been transcribed here as additional work associated with the 2006 course collection. The image has not been published.

### Three Functions with a PROM

The given functions are F=AB+A′BC′, G=A′B′C+C′, and H=AB′C′+ABC′+A′B′C. Three inputs select eight addresses; the memory organization required for three outputs is 8×3 bits.

| ABC | F | G | H |
| --- | --- | --- | --- |
| 000 | 0 | 1 | 0 |
| 001 | 0 | 1 | 1 |
| 010 | 1 | 1 | 0 |
| 011 | 0 | 0 | 0 |
| 100 | 0 | 1 | 1 |
| 101 | 0 | 0 | 0 |
| 110 | 1 | 1 | 1 |
| 111 | 1 | 0 | 0 |

A, as the most significant input, is connected to the S2 terminal of the 3-to-8 decoder, B to S1, and C to S0. Decoder outputs 2, 6, 7 for F; 0, 1, 2, 4, 6 for G; and 1, 4, 6 for H are routed to the corresponding OR paths. The table was checked by evaluating the functions at all eight input combinations.

### Programmable Regions

The handwritten note explains that in a PROM the decoder is fixed and the output connections are programmed. The PAL example shows a programmable AND plane with fixed OR connections; the PLA example shows both the AND and OR planes being programmable.

The PLA drawing contains three inputs, four product terms, and two outputs. The marked product rows are AB, AC, BC, and A′B′C′. The XOR control at the output is used to produce either the selected sum itself or its complement: with the control at 0 the output is direct, and with the control at 1 it is inverted.
