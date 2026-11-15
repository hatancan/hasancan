---
baslik: EEM226 Electromagnetic Wave Theory I: Homework 1, Orthogonal Coordinate Systems (Handwritten)
ozet: Handwritten solution to Homework 1 of the electromagnetics course: Cartesian, cylindrical, and spherical coordinate systems, unit vectors, scalar and vector products, differential length and volume, coordinate transformations.
---

This post is the three-page handwritten solution to Homework 1 of the Electromagnetics course; the pages were photographed on October 3, 2010. The heading of the first page reads "Electromagnetics 2 – Homework 1"; the topic is **orthogonal coordinate systems**, the foundation of vector analysis: Cartesian, cylindrical, and spherical coordinates. Below, the headings, formulas, and results of each page are given as text; the photographs themselves are kept in the archive and are not published.

## Page 1: Cartesian coordinates

**Orthogonal coordinate systems — a) Cartesian coordinates**

- The planes x = x₁, y = y₁, and z = z₁ intersect at only one point. If we define this point as point P, we can denote it as P(x₁, y₁, z₁).
- The mutually perpendicular unit vectors **a**ₓ, **a**ᵧ, and **a**_z in these three coordinate directions are called base vectors. The right-hand rule holds in this system:

```
ax × ay = az
ay × az = ax
az × ax = ay
```

- **a**ₓ · **a**ᵧ = **a**ᵧ · **a**_z = **a**ₓ · **a**_z = 0, because the axes are perpendicular to each other (**A** · **B** = |A| |B| cos θ, which is 0 for θ = 90°).
- **a**ₓ · **a**ₓ = **a**ᵧ · **a**ᵧ = **a**_z · **a**_z = 1

The position vector of point P(x₁, y₁, z₁) is the vector drawn from the origin O to point P. Its components in the **a**ₓ, **a**ᵧ, and **a**_z directions are x₁, y₁, and z₁, respectively. Thus:

- **OP** = **a**ₓ x₁ + **a**ᵧ y₁ + **a**_z z₁
- A vector in Cartesian coordinates: **A** = **a**ₓ Aₓ + **a**ᵧ Aᵧ + **a**_z A_z
- A differential length: d**l** = **a**ₓ dx + **a**ᵧ dy + **a**_z dz
- A differential volume: dv = dx dy dz

## Page 2: Scalar and vector products, cylindrical coordinates

In the Cartesian coordinate system, let **A** = **a**ₓ Aₓ + **a**ᵧ Aᵧ + **a**_z A_z and **B** = **a**ₓ Bₓ + **a**ᵧ Bᵧ + **a**_z B_z be defined.

**Scalar product:**

**A** · **B** = (**a**ₓ Aₓ + **a**ᵧ Aᵧ + **a**_z A_z) · (**a**ₓ Bₓ + **a**ᵧ Bᵧ + **a**_z B_z) = Aₓ Bₓ + Aᵧ Bᵧ + A_z B_z

**Vector product:**

```
        | ax  ay  az |
A × B = | Ax  Ay  Az |
        | Bx  By  Bz |
```

**A** × **B** = **a**ₓ (Aᵧ B_z − A_z Bᵧ) + **a**ᵧ (A_z Bₓ − Aₓ B_z) + **a**_z (Aₓ Bᵧ − Aᵧ Bₓ)

*Note: In the handwriting, the **a**ᵧ component is written as (Aₓ B_z − A_z Bₓ); in the determinant expansion the sign of this term is reversed, and the correct form is (A_z Bₓ − Aₓ B_z). Also, the page writes the components of B as "bₓ Bₓ + …"; the unit vectors should be **a**ₓ, **a**ᵧ, **a**_z. The corrected versions are given above.*

**b) Cylindrical coordinates**

In this system, we consider point P on the surface of an imaginary cylinder with components r₁, φ₁, and z: P(r₁, φ₁, z).

- r: radial distance
- φ: angle measured from the positive x axis

The right-hand rule holds:

```
ar × aφ = az
aφ × az = ar
az × ar = aφ
```

- Vector differential length in cylindrical coordinates: d**l** = **a**_r dr + **a**_φ r dφ + **a**_z dz
- Differential volume: dv = r dr dφ dz

## Page 3: Spherical coordinates and transformations

**Spherical coordinates (Question 3)**

In spherical coordinates, a point P is defined as the intersection of three surfaces: P(R₁, θ₁, φ₁).

- R = R₁: the surface of a sphere of radius R₁ centered at the origin
- θ = θ₁: a right circular cone with its vertex at the origin, its axis coinciding with the z axis, and half-angle θ₁
- φ = φ₁: the angle measured from the xz plane (a half-plane)

The right-hand rule holds:

```
aR × aθ = aφ
aθ × aφ = aR
aφ × aR = aθ
```

- Differential volume in spherical coordinates: dv = R² sin θ dR dθ dφ
- Differential length in spherical coordinates: d**l** = **a**_R dR + **a**_θ R dθ + **a**_φ R sin θ dφ

Converting the position of a point in spherical coordinates to Cartesian coordinates:

- x = R sin θ cos φ
- y = R sin θ sin φ
- z = R cos θ

**Question 2: Relations among (x, y, z), (r, φ, z), and (R, θ, φ)**

In the drawing, point P is shown with distance R from the origin and angle θ with the z axis; its projection onto the xy plane has length r and makes angle φ with the x axis:

- r = R sin θ
- x = r cos φ
- y = r sin φ
- z = R cos θ
