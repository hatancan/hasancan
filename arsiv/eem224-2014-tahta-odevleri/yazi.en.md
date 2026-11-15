---
baslik: EEM224 Electromagnetics I: 2014: Board and Projected Homework Questions
ozet: A text transcription of the archived question and solution pages, prepared with personal information removed.
---

This archive record, transcribed into text from photographed pages, contains the question statements together with the legible solution steps. The photographs are kept in a private archive; there are no downloadable files.

The legible educational content of the February and March 2014 class photographs has been transcribed into text. People visible in the photographs have not been published. The name of Prof. Dr. S. Gökhan Tanyer appears in the projected notes.

## Vector triple product
Homework on the 24 February page: Verify the identity A×(B×C)=B(A·C)−C(A·B) with examples.

## Potential question
3 March page: V(R)=E₀Rsinθ is given. a) E=? b) E(R=1, θ=60°, φ=30°)=? The photograph does not contain a solution.

## MATLAB visualization
The 11 March slide includes an assignment to learn the `legend` command and to produce an example for `fprintf`. The two-dimensional "diamond" example builds a matrix using `ones`, `cos`, `sin`, transpose, element-wise square and square root, and displays it with `subplot`, `contour` and `mesh`. On the board, the alternatives are listed as `contour(z)`, `mesh(z)`, `surf(z)`, `surfl(z)`.

```matlab
Rrad = pi .* (0:360) ./ 180;
lenR = length(Rrad);
x = ones(lenR,1) * cos(Rrad);
y = ones(lenR,1) * sin(Rrad);
y = y';
Baklava = sqrt(x.^2 + y.^2);
subplot(121), contour(Baklava);
subplot(122), mesh(Baklava);
```

*Note: Lines of the slide that were blurry or obscured by people were not completed. The legible example above is also found in the source file temel06.m in the folder.*
