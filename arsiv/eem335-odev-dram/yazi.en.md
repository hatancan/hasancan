---
baslik: EEM335 Computer Organization: DRAM Technology Assignments (Structure, Error Correction, History, DRAM Types)
ozet: DRAM assignments for EEM335 Computer Organization: DRAM cell and row-column organization, refresh, advantages and disadvantages, an error-correction example using Hamming code, the history of DRAM and its types such as FPM, EDO, and SDRAM.
---

Four student submissions (assignments by friends; personal information removed, cover pages not included) for the **DRAM technology** assignment given in the Başkent University **EEM335 Computer Organization** course. Two of the assignments follow the headings of the same assignment guideline: **1. DRAM technology** (a. structure and operating principle, b. error occurrence and correction, c. advantages and disadvantages) and **2. History and current state of DRAM technology** (a. history, b. DRAM types from past to present). The text is largely compiled from internet sources. The original (masked) PDFs can be downloaded at the end of the post.

## What is DRAM and how does it work?

**Dynamic Random Access Memory (DRAM)** is a random access memory that stores each bit of data in a separate **capacitor** within an integrated circuit ("random access": the processor can access any location in memory directly). Since it requires only one transistor and one capacitor per cell, it occupies less area than SRAM and is cheaper. A charged capacitor represents 1 and an empty one represents 0. Because capacitors lose charge over time, the data must be **refreshed**; this refresh is performed at intervals of about 2–4 ms, and the data is lost when power is removed (volatile). The cells form a matrix (DRAM array) at the intersections of rows and columns; the address is selected in two stages with the **RAS (row address strobe)** and **CAS (column address strobe)** signals. Example chip: 41256 (256K × 1 bit = 256 Kbit); modules are produced in sizes such as 16 MB (2M×64), 32 MB (4M×64), and 64 MB (8M×64). Refresh is performed either with read/write cycles or with a dedicated refresh cycle (hidden/transparent refresh, cycle stealing).

**Comparison with SRAM:** DRAM is slower but cheaper and denser; SRAM is faster, consumes more power, and is larger and more expensive, which is why it is used in cache.

## Error occurrence and Hamming code

One of the assignments gives an example of using **Hamming code** to correct errors in DRAM: the data bits are placed in the appropriate positions, and the parity bits are calculated so as to give even parity; in the example, the new data word (with parity bits) is 10001100101. If the last bit is erroneously flipped from 1 to 0 (10001100100), re-evaluating the parity bits yields the number **11**, which indicates the error position; flipping the 11th bit restores the original word.

## History and types

The history of DRAM technology is described through the transition from magnetic core memory to semiconductor memory, the first DRAM chips, and the rapid decline in cost per bit. The types covered include asynchronous DRAM types (FPM, EDO), **SDRAM** (clock-synchronous), **DDR SDRAM**, and its successor generations. Details and figures are in the assignments in the ZIP.
