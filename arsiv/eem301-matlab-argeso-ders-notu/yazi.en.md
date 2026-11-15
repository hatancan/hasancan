---
baslik: EEM301 Signals and Systems I: Introduction to MATLAB Lecture Notes (A. Hakan Argeşo)
ozet: 2004 MATLAB 6 lecture notes: command window, arithmetic, workspace, files, help, save/load and diary examples.
---

The EEM301 archive contains a 19-page lecture note titled **A. Hakan Argeşo, MATLAB: Lecture Notes**, dated March 8, 2004, according to the PDF creation date. It describes the working environment and basic usage of MATLAB 6. The explanations and examples from the English-language note are given below; the PDF can be downloaded at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request by the rights holder.*

## Introduction

MATLAB, short for Matrix Laboratory, is an interactive language for technical and scientific computing. The notes introduce mathematical computation, graphics, algorithm development, modeling, simulation and data analysis. Arrays are its basic data elements, and the examples use double-precision numeric values.

The document describes MATLAB version 6 for Windows, released in 2000. Its menus and interface descriptions belong to that historical version.

## Desktop tools

The desktop includes Command Window, Command History, Current Directory Browser, Workspace Browser, Launch Pad, Help Browser, Array Editor and Editor/Debugger. Windows can be docked within the desktop or undocked. The View menu controls visibility and predefined desktop layouts.

The Command Window accepts expressions after the `>>` prompt. Command History retains entered lines, which can be copied or executed again. The Workspace Browser shows variables, their sizes and their classes.

## Arithmetic and assignment

```matlab
2*6
3+ans
x=5+2*7
x=38/x
```

The successive numeric results are 12, 15, 19 and 2. Variable names are case sensitive: `xsum` and `Xsum` are different names.

*Note: The source shows the output of both assignments to x under the heading "ans". In MATLAB, the result of an assignment is displayed under the variable's name, x; the results of unnamed calculations are stored in the variable ans.*

| Operation | MATLAB notation |
|---|---|
| Exponentiation | a^b |
| Multiplication | a*b |
| Right division | a/b |
| Left division | a\b |
| Addition | a+b |
| Subtraction | a-b |

Parentheses control grouping; exponentiation precedes multiplication and division, which precede addition and subtraction. The worked examples are:

```matlab
5*6/2 + 17
8^2*7 - (3*11 + 7)/(6 - 1)
27^(1/3)*2 - 81^0.5 + 3*(17+18+19)
0.5*((2^3+1)^2 + 15)^2/8
```

The results are 32, 440, 159 and 576.

The assignment operator places the value of the right-hand expression into the variable on the left. `12=x` and `x+12=x` are invalid assignments. `x=x+12` is valid when x has already been assigned.

## Example: area of a trapezoid

```matlab
a=3;
b=2;
h=5;
A=h*(a+b)/2
```

The result is A=12.5. Semicolons suppress display; commas separate statements while allowing their values to be displayed. The same calculation can be written on one line.

*Note: The source calls h the "base length"; in the formula A=h(a+b)/2, h is the height, and a and b are the lengths of the parallel sides.*

## Managing a session

| Command | Purpose |
|---|---|
| who | List current variables |
| whos | List variables with sizes and classes |
| clear | Remove workspace variables |
| clear a | Remove only a |
| clc | Clear the Command Window display |
| pwd | Display current directory |
| dir | List directory entries |
| cd dirname | Change current directory |

For the trapezoid example, `who` lists A, a, b and h. `whos` reports four 1×1 double arrays. After `clear a`, the remaining names are A, b and h.

MATLAB searches the current directory and its search path for files. The Current Directory Browser allows navigation and file operations.

## Getting help

```matlab
help cos
lookfor tangent
```

`help` gives concise command documentation. `lookfor` searches descriptions using a keyword; the example lists inverse tangent, tangent and related functions. The Help Browser provides Contents, Index, Search and Favorites tabs.

The note also shows `doc cosine` and then explains why `help cosine` reports that cosine.m cannot be found.

*Note: In the document, the names cos and cosine are mixed up within the same help example. Since the function name is cos, doc cos should be used to open the function's documentation directly.*

## Menus

File contains commands for new files, opening files, importing data, saving workspaces, configuring the path and printing. Edit contains undo, redo, clipboard actions and commands for clearing windows or variables. View manages desktop tools and layouts. Web opens MathWorks resources; Window selects open windows; Help opens documentation.

## Saving and loading variables

```matlab
save Mywork
load Mywork
```

`save` without a filename uses matlab.mat; an explicit name creates the corresponding MAT file. `load` restores saved variables into the workspace. The document also describes Save Workspace As and opening MAT files from the directory browser.

## Recording a session with diary

```matlab
diary on
a=1
b=2
c=a+b
diary off
get(0,'diary')
get(0,'diaryfile')
```

The example computes c=3. `diary on` starts recording commands and textual output, `diary off` stops it, and `diary filename` chooses another file. Graphs are not included. The ASCII diary can be opened in the Editor/Debugger for viewing and editing.
