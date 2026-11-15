---
baslik: EEM335 Computer Organization: Final Exam (January 14, 2011)
ozet: EEM335 Computer Organization final exam questions from 14.01.2011: TLB, disk access times, 32-bit floating-point number, tri-state circuits, cache mapping methods, virtual address, DMA signals, and page table calculation.
---

The final exam of the **EEM335 Computer Organization** course at Başkent University, dated **14 January 2011** (duration 100 minutes; the course is taught by Prof. Dr. Emin Akata). The exam paper is a single page; the original can be downloaded at the end of the post. The calculations in the *Note* lines below the questions have been added for the archive; the paper itself contains no solutions.

## Question 1 (30 points)

Answer the following:

1. What is a TLB (Translation Lookaside Buffer)? What is it used for?
2. Explain the concepts of *seek time*, *rotational delay*, *access time*, and *transfer time* in disk usage.
3. What is the decimal equivalent of the number whose 32-bit floating-point representation is `1 01111111 10100010000000000000000`? Answer with an explanation.
4. What is the importance of tri-state circuit elements in bus usage?
5. What are the basic characteristics of DRAM, SRAM, SDRAM, and DDR SDRAM chips?
6. The output signals of a memory module do not include an interrupt signal, whereas the output of an I/O module does. Explain why.

*Note: In part 3, the sign bit is 1 (negative), the exponent 01111111 = 127 (since the IEEE 754 bias is 127, the exponent = 0), and the mantissa is 1.1010001₂ = 1 + 1/2 + 1/8 + 1/128 = 1.6328125; the number is −1.6328125.*

## Question 2 (7 + 5 + 8 points)

In a memory system that uses 32-bit addresses, is byte-addressable, and has a cache line size of 128 bytes:

1. In a **direct mapped** cache with a 16-bit tag, specify the address format; find the number of addressable units, the number of blocks in main memory, and the number of lines in the cache.
2. In a **fully associative** cache, specify the address format; find the number of addressable units, the number of blocks in main memory, the number of lines in the cache, and the tag size.
3. Find the cache size and, for a **2-way set associative** cache, specify the address format; find the number of addressable units, the number of blocks in main memory, the number of lines per set, and the number of sets in the cache.

*Note: Since a line is 128 = 2⁷ bytes, the word field is 7 bits. (a) 32 − 16 − 7 = 9 bits for the line field: 512 lines, 2³² addressable bytes, 2²⁵ blocks. (b) Tag = 32 − 7 = 25 bits. (c) If the cache is taken to be the same as in part (a), it is 512 × 128 B = 64 KB; in the 2-way organization there are 2 lines per set and 256 sets, and the format is 17-bit tag + 8-bit set + 7-bit word.*

## Question 3 (15 points)

Explain the concepts of "logical address", "virtual address", and "demand paging".

## Question 4 (20 points)

Draw a connection diagram containing the CPU, Disk Controller, Main Memory, and DMA Controller, and explain how a DMA operation is carried out using the HRQ, HLDA, DREQ, and DACK signals.

## Question 5 (4 + 4 + 7 points)

In a memory organization with a 4 GByte virtual address space, this space is divided into a total of 2M pages. The size of the page table is calculated as 8 MBytes.

1. Find the frame (page) size.
2. Find the length of each entry in the page table.
3. Explain, with a drawing, what address structure would be set up for a 2-level paging scheme that uses a root table the size of 1 page.

*Note: The page size is 4 GB / 2M = 2 KB; the entry length is 8 MB / 2M = 4 bytes. If the root table is 1 page (2 KB), it contains 512 entries (9 bits); the remaining 12 bits of the 21-bit page number are for the second level (second-level tables of 4096 entries, 16 KB = 8 pages each); the offset within a page is 11 bits (9 + 12 + 11 = 32 bits in total).*
