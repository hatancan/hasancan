---
baslik: END355 Project Management: CPM and PERT Network Models Lecture Notes (Critical Path, Crashing with LP, Beta Distribution)
ozet: CPM and PERT project network methods: network diagram rules, earliest/latest times via forward and backward passes, critical path and slack, LP model, time-cost (crashing) analysis, PERT three-time estimates and project completion probability; with worked examples.
---

Two lecture notes from the END355 Project Management folder have been combined: the 14-page **"CPM and PERT – Network Models"** presentation and the 12-page **"Project Management"** (network diagram and critical path method) presentation. The notes do not name an author or institution; judging from the content, they belong to civil engineering and operations research courses. The original PDFs can be downloaded at the end of the post.

*This content belongs to a third-party source (the author and institution are not stated in the document); it is shared for archival and nostalgic purposes. It will be removed at the request of the rights holder.*

## What are CPM and PERT?

Questions sought across a project: How long will the project take? When can an activity start? Does a delay in an activity affect the whole project, and by how much? Which activities should be accelerated to finish the project earlier?

- **CPM (Critical Path Method):** Developed by DuPont de Nemours in the 1950s; activity durations are deterministic and are obtained from experience with similar projects.
- **PERT (Program Evaluation Review Technique):** Developed by the U.S. Navy in 1958; activity durations are probabilistic (stochastic).
- Both show the activities and their dependencies on a network; the main difference is PERT's statistical approach to duration estimation.

## Network diagram rules

Arrows represent activities, and nodes represent **events** (the start or finish of one or more activities).

1. There is one start node and one finish node.
2. Each activity is shown once by a single arrow.
3. Two activities cannot share the same start and end event; in this case a **dummy** activity with zero duration is used.
4. Precedence relations are determined by these questions: Which activities must be completed before this activity can start? Which activities follow it? Which can be done concurrently with it?

## CPM terminology

- **Critical activity:** an activity whose delay delays the completion of the whole project; **critical path:** the longest-duration path in the project, on which every activity has zero slack.
- **ES (earliest start)**, **EF (earliest finish)**, **LS (latest start)**, **LF (latest finish)**.
- **Slack (TS):** the difference between the latest and earliest start (or finish) times; slack = LF − ES − activity duration.
- Earliest times are computed from start to finish (forward pass), and latest times from finish to start (backward pass). If more than one activity ends at a node, the largest EF is the earliest start of the following activity; in the backward pass, the smallest LS among the activities leaving the node is taken.

## CPM with LP

Let t_i be the occurrence time of the event at the i-th node. To minimize the project duration:

- Min Z = t_n − t_1
- Constraints: t_j − t_i ≥ T_ij (for each activity (i,j)), t_i ≥ 0.

## Example 1: CPM with LP (8 activities)

| Activity | Predecessor | Duration (days) |
|---|---|---|
| A | – | 10 |
| B | – | 12 |
| C | A, B | 15 |
| D | B | 18 |
| E | B | 16 |
| F | C | 11 |
| G | D, E | 10 |
| H | F, G | 8 |

In the LP solution in the notes, with the constraints t₂−t₁ ≥ 12, t₃−t₂ ≥ 0, t₃−t₁ ≥ 10, t₅−t₂ ≥ 16, t₆−t₂ ≥ 18, t₇−t₆ ≥ 10, t₈−t₇ ≥ 8, the event times are found to be 12, 30, 40, and 48 days. **The critical path is B–D–G–H, and the project duration is 48 days** (the path B→C→F→H takes 46 days, and the path B→E→G→H takes 46 days).

## Example 2: Design and production of a new electronic device

| Code | Activity | Predecessor | Duration (days) |
|---|---|---|---|
| A | Determining product specifications | – | 30 |
| B | Budget and feasibility studies | A | 8 |
| C | Prototype production | B | 8 |
| D | Raw material procurement and production preparations | B | 5 |
| E | Preparing the final design | H | 2 |
| F | Production | D, E | 25 |
| G | Personnel training | A | 10 |
| H | Personnel feedback on the prototype | C, G | 3 |
| I | Sales training and preparing the user manual | E | 5 |
| J | Determining the marketing mix | A | 5 |
| K | Promotion campaign | I, J | 15 |
| L | Project closure | F, K | 2 |

*Note: When computed, the critical path is A–B–C–H–E–F–L with a duration of 30 + 8 + 8 + 3 + 2 + 25 + 2 = 78 days; the path A–B–C–H–E–I–K–L takes 73 days.*

## Example 3: Park landscaping project (ES/EF, LS/LF table)

Converting a wooded site into a park: A grading excavation (4 days), B cut the trees (A; 4), C collect and utilize the trees (B; 5), D open the road and lay stabilized surface (A; 3), E lay stabilized surface for the parking lot (D; 3), F water and electrical installation (D; 4), G build the building and shelters (C, E; 5), H planting flowers and greenery (C, E; 8), I complete the installation and clean up (F, G; 2).

| Activity (nodes) | Earliest start | Earliest finish | Latest start | Latest finish | Slack |
|---|---|---|---|---|---|
| 1-2 (A) | 0 | 4 | 0 | 4 | 0 |
| 2-3 (B) | 4 | 8 | 4 | 8 | 0 |
| 2-4 (D) | 4 | 7 | 7 | 10 | 3 |
| 3-5 (C) | 8 | 13 | 8 | 13 | 0 |
| 4-5 (E) | 7 | 10 | 10 | 13 | 3 |
| 4-6 (F) | 7 | 11 | 15 | 19 | 8 |
| 5-6 (G) | 13 | 18 | 14 | 19 | 1 |
| 5-7 (H) | 13 | 21 | 13 | 21 | 0 |
| 6-7 (I) | 18 | 20 | 19 | 21 | 1 |

**Critical path: A, B, C, H (1-2-3-5-7); project duration 21 days.**

## Time–cost analysis (crashing) and acceleration with LP

In basic CPM, the goal is to find the minimum duration; CPM, however, assumes that activity durations can be shortened by a certain amount with additional investment (labor, equipment, materials). The additional expenditure for shortening duration is called the **crash cost**; the additional cost is offset by the benefit gained from shortening the total duration. If the shortening cost is assumed to be linear, with K_ij the unit crash cost of activity (i,j), the LP that minimizes the additional investment for completing the project within T_max is:

- Min Z = Σ K_ij · (NT_ij − T_ij)
- Constraints: t_j − t_i ≥ T_ij; CT_ij ≤ T_ij ≤ NT_ij (shortest ≤ duration ≤ normal duration); t_n − t_1 ≤ T_max; t_i ≥ 0.

It can also be written with the variable D_ij = NT_ij − T_ij (the amount of shortening). If there is an additional budget limit NEWB, then Σ K_ij·D_ij ≤ NEWB; if there is an indirect unit cost I that depends on total duration, Min Z = Σ K_ij·D_ij + I·(t_n − t_1); if the unit reward for finishing the project earlier than T_set is B (e.g., build-operate-transfer projects), Min Z = Σ K_ij·D_ij − B·(T_set − t_n).

## PERT

When there is no experience with an activity, duration uncertainty is taken into account: three duration estimates are made for each activity: **optimistic (a)**, **most likely (m)**, and **pessimistic (b)**. Durations are assumed to be independent and Beta-distributed; the expected duration is t_e = (a + 4m + b)/6 and the variance is σ² = ((b − a)/6)². The expected project duration is the sum of the expected durations on the critical path, and its variance is the sum of the variances on the critical path; the project completion time is approximately Normally distributed with this mean and variance.

**Example:** For a project with E(T) = 29 days and σ = √6 days, the probabilities of finishing (a) 3 days before the expected duration (within 26 days) and (b) at most 2 days after the expected duration (within 31 days) are required.

*Note: From the standard normal distribution, P(T ≤ 26) = Φ(−3/√6) = Φ(−1.22) ≈ 0.11 and P(T ≤ 31) = Φ(2/√6) = Φ(0.82) ≈ 0.79. Since the beta formula in the notes appears in a slide image, the t_e and σ² expressions were written as the standard PERT formulas.*

## Source: summary of the network method (second note)

The second presentation summarizes the same topics as follows: in CPM, activity times are deterministic, while in PERT they are probabilistic. The network diagram can be drawn in two ways (activity on arrow / activity on node); the first method (activity = arrow, event = node) is more convenient. The critical path is found by computing the earliest/latest start and finish times; activities with zero slack are critical.
