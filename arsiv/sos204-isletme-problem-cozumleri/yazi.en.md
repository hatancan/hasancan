---
baslik: SOS204 Business Administration: Numerical Problems and Solutions (Depreciation, Center of Gravity, Economic Order Quantity, NPV and Internal Rate of Return)
ozet: Handwritten numerical problem solutions for the SOS204 Business Administration course: depreciation methods, center of gravity and weighted scoring for facility location, unit holding cost and economic order quantity, capacity calculation, payback period, net present value and internal rate of return.
---

This is a text transcription of an 8-page **handwritten problem-solution** note prepared for the SOS204 Business Administration course (the pages are dated "December 23"; the author is not stated). The pages were photographed/scanned from paper and transcribed into text; the images are not published. Because most of the solutions are low-resolution, numbers that could not be read are either indicated or omitted.

## 1. Depreciation methods

- Question: a machine used in a business has a book value of 450 TL at the end of its 2nd year of use and 337.5 TL at the end of the 3rd year; given that the 4th-year depreciation will be less than 100 TL, which method was used? The depreciation between the 2nd and 3rd years is 450 − 337.5 = 112.5 TL; since depreciation decreases each year and will fall below 100 TL in the 4th year, the method is **declining-balance depreciation**.
- For a machine with cost C = 1024 TL, salvage value S = 243 TL, and life n = 5 years:
  - **Straight-line:** A = (C − S)/n = (1024 − 243)/5 = **156.20 TL** per year.
  - **Declining-balance:** rate a = 1 − ⁿ√(S/C) = 1 − ⁵√(243/1024) = **0.25**. Annual depreciation = remaining value × 0.25: year 1 is 256, year 2 is 192, year 3 is 144, year 4 is 108, year 5 is 81 TL (remaining value 1024 → 768 → 576 → 432 → 324 → 243).
  - **Sum-of-the-years'-digits (increasing amount):** sum of year numbers 1 + 2 + 3 + 4 + 5 = 15; depreciation = (C − S) × (remaining years)/15 = 781 × 5/15, 781 × 4/15, … 781 × 1/15.
- Note: when calculating the first year's depreciation and when subtracting the salvage value in the last year, attention must be paid to the characteristics of the method (notes on the page: first-year depreciation is found directly from the cost, later years from the remaining value).

## 2. Cost concepts (total, average, and marginal cost)

A table of total cost TC is given for production quantity q; average cost AC = TC/q and **marginal cost** MC = ΔTC/Δq are calculated (example: when TC rises from 2800 to 3300 with Δq = 1, MC = 500, and so on; the values in the page's table could not be fully read).

## 3. Facility location selection: center of gravity method

C_x = Σ(d_ix · V_i)/ΣV_i and C_y = Σ(d_iy · V_i)/ΣV_i; here C_x, C_y are the coordinates of the center of gravity, d_ix, d_iy are the coordinates of the i-th demand point, and V_i is the quantity of product shipped to that point. Example: the demands of demand points A, B, C, D, E, F are 400, 300, 200, 100, 300, 100 units; the coordinates (as read in the solution) are A(60, 85), B(80, 75), C(30, 120), D(90, 110), E(127, 30), F(65, 40). The calculation gives a **center of approximately (76.3, 38.3)** (the result for x on the page is not legible). This method gives a central location; when choosing the actual site, the manager prefers a nearby area.

## 4. Weighted scoring method

Factor weights: total transportation (30%), labor (10%), transportation quality (30%), living conditions (10%), proximity to suppliers (10%). For each alternative location (A, B, C), the factors are given letter grades (M: excellent, VA: below average, V: average, I: good, Z: poor), converted to numerical scores, and the sum Σ w_i · F_i is taken; in the example, for A, 0.30·5 + 0.20·3 + 0.30·3 + 0.1·2 + 0.1·4 = **3.6** was found. Among the alternatives, the location with the highest score is chosen.

## 5. Unit holding cost and economic order quantity

**Question 1.** A firm incurs 5 TL of transportation, 3 TL of storage, and 2 TL of insurance costs for each of the products it purchases at 50 TL. Given that the holding cost rate of inventories is 20% and the firm holds an average of 3000 units in stock, calculate the holding cost: unit holding cost = transportation 5 + storage 3 + insurance 2 = 10 TL, plus the holding (financing) cost of the purchased goods 50 × 20% = 10 TL, giving **20 TL**; total holding cost = average inventory × unit holding cost = 3000 × 20 = **60,000 TL**.

**Question 2.** A store sells 1500 men's suits in 1 year; the holding cost per suit is 3 million (old TL), and the ordering cost per order is 2 million; what is the store's economic order quantity? If the holding cost increases by 10% and the ordering cost by 5%, what will the new economic order quantity be? The formula is Q* = √(2·D·S/H); the old Q = √(2·1500·2,000,000/3,000,000) and the new value Q_n = √(2·1500·2,100,000/3,300,000) ≈ **44** units (44.1 on the page).

## 6. Capacity and payback period

**Capacity.** A garment workshop will sew 250,000 units (pockets) per year; the processing time on one machine is 1.5 minutes per pocket; 10% of machine time is lost to unexpected breakdowns and 3% to time (unusable in the assembly-line workshop); 250 days per year are worked. In the calculation, the efficiency factor is 90%, practical capacity = 250 × 8 hours = 2000 hours/machine/year, required total time = 250,000 × 1.5 / 0.87 / 0.90 ≈ 429,553 minutes ≈ 7159 hours; number of machines = 7159/2000 ≈ **3.58 → 4 machines** should be purchased (with 3, the capacity of three machines is insufficient; with 4, utilization drops).

**Payback period.** The investment amounts are A: 15,000, B: 12,000, C: 20,000, D: 10,000; the annual net cash inflows are given in a table. The calculated periods: PP_A = 3 + (15,000 − 13,000)/3000 = **3 2/3 years**; PP_B = 3 + (12,000 − 11,000)/2000 = **3.5 years**; PP_C = 2 + 5/6 years; PP_D = 2 + 1/3 years (the numbers in the solution are written as far as they could be read). The project with the shortest period is chosen.

## 7. Net present value

**Question.** Net present values of projects A and B (both with an investment of 300,000 TL) at a 40% discount rate: cash inflows A: 100,000, 200,000, 150,000, 250,000, 400,000; B: 200,000, 150,000, 100,000, 250,000, 300,000. NPV = Σ CF_t/(1 + i)^t − investment. Result: **NPV_A ≈ 67,585 TL** and **NPV_B ≈ 76,668 TL**; the one with the higher NPV is chosen (according to the paper, B is higher than A).

**Question.** A vehicle will yield 200 TL of income at the end of the 1st, 2nd, and 3rd years; it will be sold for 1000 TL at the end of the 3rd year; with an annual discount rate of 25%, is it acceptable to buy the vehicle for 950 TL? NPV = 200/1.25 + 200/1.25² + 1200/1.25³ = **≈ 902.4 TL** < 950 TL; since the present value is lower than the purchase price, the vehicle should not be bought.

## 8. Internal rate of return and working capital

The internal rate of return is the discount rate that makes the project's net present value zero. If the NPVs for two discount rates (20% and 22%) are found to be +11.57 and −124.65, then by linear interpolation **IRR = r_p + NPV_p/(NPV_p + |NPV_n|) · (r_n − r_p) = 0.20 + 11.57/(11.57 + 124.65) · (0.22 − 0.20) ≈ 20.17%** (0.2017 on the page).

**Working capital requirement.** For a business with a cost of goods sold of 1400, the components of the operating cycle are given as raw material inventory 20 days, manufacturing 5 days, finished goods inventory 20 days, credit term 20 days (and sales 5 days); the operating cycle duration is 20 + 5 + 20 + … days, the operating cycle turnover coefficient = 365/duration ≈ 4.56, and the **working capital requirement = cost of goods sold / operating cycle turnover coefficient = 1400/4.56 ≈ 307** (the page shows 3.06 ≈ 306.x; the handwriting is not clearly legible).
