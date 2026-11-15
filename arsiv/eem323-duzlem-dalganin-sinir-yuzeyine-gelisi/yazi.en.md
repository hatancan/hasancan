---
baslik: EEM323 Electromagnetics II: Normal and Oblique Incidence of a Plane Wave on a Boundary (Prof. S. Gökhun Tanyer)
ozet: Normal and oblique incidence of a plane wave on dielectric-conductor and dielectric-dielectric boundaries in Prof. Dr. S. Gökhun Tanyer's EEM323 course: standing waves, reflection and transmission coefficients, Snell's law; the instructor's questions and homework.
---

The text content of three sets of notes that Prof. Dr. S. Gökhun Tanyer covered in the **EEM 323 Electromagnetics II** course (Fall 2013–2014, December 3, 2013): incidence of a plane wave on a planar boundary. Since most of the solutions in these notes are equation images, this post presents the flow of topics, the instructor's questions and homework, and the key results.

## 1. Topic outline

The basic problems the instructor outlined:

- **Normal incidence:** dielectric–perfect conductor boundary and dielectric–dielectric boundary. Problem: given the incident E field, compute all other fields.
- **Oblique incidence:** dielectric–conductor and dielectric–dielectric boundaries; parallel and perpendicular polarization in each case.
- Other concepts: definitions of parallel and perpendicular polarization, the Huygens/Snell **law of reflection**, Snell's **law of refraction**, the Brewster angle (no reflection).
- If time permits, the next topic: transmission lines.

## 2. Normal incidence

**Dielectric–perfect conductor boundary.** The incident E field is given; the reflected field and the total field are computed, resulting in a **standing wave** solution. The instructor's homework: compute the standing wave solution for the **magnetic field** as well. Questions: what would the standing wave function be if the reflection coefficient were +1? What if it were −1?

**Dielectric–conductor boundary.** Question: given only the incident electric field, what are the fields in the two regions, and how many equations are needed?

**Multiple dielectric interfaces (three media).** The instructor's questions: How would you approach the problem? How many unknowns and how many equations are there? If there are enough equations, how do you solve them? Two suggested methods:

1. Compute all the recursive (successive) reflections and transmissions one by one. Questions: In how many steps can it be solved? If there are infinitely many, can a method be defined for convergence; what are the constraints on the stopping time?
2. Write the total E and H fields and apply the boundary conditions (the instructor's solution follows this method). The fields are numbered 1, 2 and 3 according to the medium number; the question asked: define the known and unknown variables.

## 3. Oblique incidence

**Dielectric–conductor boundary, perpendicular polarization.** The E field is perpendicular to the plane formed by the incident and reflected rays. The instructor's homework: by examining your solution, show that: (1) there is a **standing wave pattern** in the direction normal to the boundary; (2) this pattern comes from the sin(β_z z) and cos(β_z z) terms, where β_z = β cos θ; (3) the average power propagates in the direction parallel to the boundary. Also: compute the distance of the nulls from the z = 0 plane.

**Dielectric–dielectric boundary, parallel polarization.** The E field is parallel to the plane of incidence. Given the incident field, the magnetic field is computed; the reflected and transmitted fields are written similarly. The instructor's question: how many unknowns are there, how many equations are needed, and what are these boundary conditions?

Boundary conditions:

- B.C.(1): continuity of tangential E,
- B.C.(2): continuity of tangential H,
- B.C.(3): continuity of all fields (phase terms) at the z = 0 plane; conditions (1) and (2) must be satisfied for all values of x along the boundary.

The following results follow from B.C.(3):

> θᵢ = θᵣ (law of reflection), sin θᵢ / sin θₜ = k₂/k₁ = u₁/u₂ (**Snell's law of refraction**)

Applying B.C.(1) and (2) yields the **reflection and transmission coefficients** for perpendicular polarization. The last slide of the notes says "Lecture notes will be added after this section."; that is, the notes were left unfinished.

*Note: Among the files there was a copy of 3A with "(1)" appended; it differs only in minor details of its titles ("…AT PLANAR BOUNDARY" / "…BASIC PROBLEMS TO BE SOLVED IN THIS LECTURE"), and the content is identical.*

## Source note

This post is a summarized and written-up version of the **instructor's own text content** (headings, explanations, questions, homework) from the lecture slides prepared by Prof. Dr. S. Gökhun Tanyer for the Başkent University EEM 323 Electromagnetics II course (Fall 2013–2014) (OGR-EEM323-DN-3A-PlaneIncidence, 3B-NormalIncidence, 3C-ObliqueIncidence). According to the slides' own statement, the figures, tables, and equation images in the slides were taken from D. K. Cheng's textbooks (*Fundamentals of Engineering Electromagnetics*, *Field and Wave Electromagnetics*); therefore they are **not reproduced here**, and the original slide file has not been made available for download. For figures and detailed derivations, refer to Cheng's books.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution. It will be removed at the request of the rights holder.*
