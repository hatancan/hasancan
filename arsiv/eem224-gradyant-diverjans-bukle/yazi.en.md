---
baslik: EEM224 Electromagnetics I: The Field Concept, Gradient, Divergence, Curl, and the Stokes and Divergence Theorems (Handwritten Lecture Notes)
ozet: EEM224 Electromagnetics I handwritten lecture notes: scalar and vector fields, the nabla operator and its unit, gradient, divergence and curl, solenoidal and irrotational fields, the divergence theorem, Stokes' theorem, the two zero identities, and Helmholtz's theorem.
---

This post brings together two sections of handwritten lecture notes for **EEM224 Electromagnetics I** at Başkent University: **"The Field Concept – Gradient – Divergence – Curl"** (3 pages) and **"Classification of Fields – Stokes' and Divergence Theorems"** (3 pages). The notes do not state the author's name or the date. The content of the notes has been transcribed into text; the scanned original PDFs can be downloaded as a ZIP at the end of the post.

## The concept of a field

**Field:** a spatial distribution; in other words, a function that depends on "space coordinates".

- g = f(x, y, z) is a scalar value at the point x = x₀, y = y₀, z = z₀; **f is a scalar field**. An example is the temperature function in a volume.
- Ḡ = F̄(x, y, z) is a vector value at the same point; **F̄ is a vector field**. An example is the wind function in a volume.

A field can be static or time dependent: f(x, y, z; t) is a time-dependent scalar field, and F̄(x, y, z; t) is a time-dependent vector field.

**Static field:** it may vary with position, but it does not vary with time.

The magnitude of each component of a vector field is a scalar field:

F̄(x, y, z) = â_x f_x(x, y, z) + â_y f_y(x, y, z) + â_z f_z(x, y, z)

Here f_x, f_y, f_z are the magnitudes of the components in the x, y and z directions, respectively (scalar fields).

**Important note:** The component in the x direction does not have to be a function of x only. As in this example, it can be a function of x, y and z.

## The del, delta or nabla operator

The nabla operator (denoted by ∇) is a vector operator that is expressed in Cartesian coordinates as follows:

∇ = â_x ∂/∂x + â_y ∂/∂y + â_z ∂/∂z

**Question: What is the unit of ∇?** Looking at the definition, the ∇ operator contains derivative terms with respect to x, y and z. Since x, y, z are length variables, their unit can be expressed as "meters". Therefore, taking the derivative with respect to x, y, z is in effect dividing by "meters". For this reason, the unit of the ∇ operator is **1/meter**. (In general: taking the derivative with respect to a variable means dividing by the unit of that variable.)

## The gradient of a scalar field

The gradient is a vector field in the direction of change of a scalar field.

As an example, consider the temperature function in a region: T(x, y, z). Suppose the temperature is constant at a fixed height, but increases as the height (z) increases. In this case, the gradient of the temperature function will be a vector field in the â_z direction.

Mathematically (in Cartesian coordinates), the gradient of a scalar field is:

∇f(x, y, z) = â_x ∂f/∂x + â_y ∂f/∂y + â_z ∂f/∂z

The result is a vector. No symbol is placed between ∇ (vector) and f (scalar), just as in the product of a vector and a scalar.

## The divergence of a vector field

The divergence of a vector field is a measure of whether each component of the vector field varies in its own direction. Let Ā(x, y, z) = â_x A_x(x, y, z) + â_y A_y(x, y, z) + â_z A_z(x, y, z):

∇ · Ā = (â_x ∂/∂x + â_y ∂/∂y + â_z ∂/∂z) · (â_x A_x + â_y A_y + â_z A_z) = ∂A_x/∂x + ∂A_y/∂y + ∂A_z/∂z

The terms are, respectively, the variation of the x-directed component in the x direction, the variation of the y-directed component in the y direction, and the variation of the z-directed component in the z direction. There is a dot product between ∇ (vector) and Ā (vector); **the result is a scalar**.

## The curl of a vector field

The curl of a vector field is a measure of whether the vector field in question has a rotational variation. In Cartesian coordinates:

∇ × Ā = (â_x ∂/∂x + â_y ∂/∂y + â_z ∂/∂z) × (â_x A_x + â_y A_y + â_z A_z)

```
        | â_x    â_y    â_z  |
∇ × Ā = | ∂/∂x   ∂/∂y   ∂/∂z |
        | A_x    A_y    A_z  |
```

There is a cross product between ∇ (vector) and Ā (vector); **the result is a vector**.

## Classification of vector fields by their divergence and curl

- A vector field whose divergence is equal to 0 is called **"solenoidal"**: if ∇ · Ā(x, y, z) = 0, then Ā(x, y, z) is a solenoidal field.
- A vector field whose curl is equal to 0 is called **"irrotational"** or **"conservative"**: if ∇ × Ā(x, y, z) = 0, then Ā(x, y, z) is an irrotational or conservative field.

Note: In some sources the curl (∇×) operator is also called "rotational". For this reason, fields whose curl is 0 are called "irrotational", that is, "without rotation".

## The divergence theorem

Let v be a volume and S be the closed surface enclosing the volume v. For any vector field Ā(x, y, z):

∫_v (∇ · Ā) dv = ∮_S Ā · ds̄

That is, the total flux of Ā(x, y, z) through the closed surface S can be found from the volume integral of ∇ · Ā(x, y, z) over v.

An easy way to remember this: on the left side, ∇ · Ā is a scalar field and dv is a scalar; the operands in a volume integral must be scalars. On the right side, Ā is a vector field and ds̄ is a vector, and there is a dot product between them; the operands in a surface integral must be vectors.

**In terms of units** (let the unit of Ā be "Kappa"): on the left side, the unit of ∇ · Ā is Kappa/m and the unit of dv is m³, giving a total of Kappa·m². On the right side, Ā is Kappa and ds̄ is m², again giving a total of Kappa·m². The term on the left has an extra derivative because of ∇, but there is a triple integral; the term on the right has a double integral.

## Stokes' theorem

Let S be a surface and C be the closed contour enclosing the surface S. For any vector field Ā(x, y, z):

∫_S (∇ × Ā) · ds̄ = ∮_C Ā · dl̄

That is, the total work done against Ā(x, y, z) in traversing a closed contour C is equal to the flux of ∇ × Ā(x, y, z) through S.

An easy way to remember this (let the unit of Ā be Kappa): on the left side, ∇ × Ā is Kappa/m and ds̄ is m², giving a total of Kappa·m; on the right side, Ā is Kappa and dl̄ is m, giving a total of Kappa·m. The left term has an extra derivative because of ∇, but there is a double integral; the right term has a single integral.

## The two "0" identities

**1. The curl of the gradient of a scalar field is 0.** Let f(x, y, z) be a scalar field:

∇ × (∇f(x, y, z)) = 0

Therefore, a vector field whose curl is 0 can be expressed as the gradient of a scalar field. That is, if ∇ × Ā(x, y, z) = 0, then there is a scalar field f(x, y, z) satisfying Ā(x, y, z) = ∇f(x, y, z).

**2. The divergence of the curl of a vector field is 0.** Let Ā(x, y, z) be a vector field:

∇ · (∇ × Ā(x, y, z)) = 0

Therefore, a vector field whose divergence is 0 can be expressed as the curl of another vector field. That is, if ∇ · B̄(x, y, z) = 0, then there is a vector field Ā(x, y, z) satisfying B̄(x, y, z) = ∇ × Ā(x, y, z).

## Helmholtz's theorem

If (i) ∇ × Ā(x, y, z) and (ii) ∇ · Ā(x, y, z) are known everywhere, then Ā(x, y, z) can also be calculated everywhere.

In other words, specifying the curl and divergence of a vector field everywhere in space is equivalent to specifying the vector field itself.
