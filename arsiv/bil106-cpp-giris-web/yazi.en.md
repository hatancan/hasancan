---
baslik: BIL106 Introduction to Programming: Introduction to Computers and Programming with C++ (Bilgisayar Dersleri site)
ozet: "Bilgisayar Dersleri" (bilgisayardersleri.wordpress.com) site's introductory C++ post: the units of a computer, generations of programming languages, history of C and C++, first C++ programs, cout/cin, arithmetic, relational and equality operators.
---

This post is a printout of a web page kept in the BIL106 Introduction to Programming course archive folder: the post titled *"Introduction to Programming with C++"* from the site named **"Bilgisayar Dersleri"** (**bilgisayardersleri.wordpress.com**). The document does not mention an author; the printout was made in August 2016. The text occasionally contains page references such as *"Diagram: p. 15 (Deitel)"*; so it appears to be lecture notes based on the introductory chapter of Deitel & Deitel's *C++ How to Program*. A 15-page PDF printout of the page can be downloaded at the end of the post.

*This content belongs to a third-party source; it is shared for archival and nostalgic purposes with attribution to the source. It will be removed at the request of the rights holder.*

## Introduction to computers and programming with C++

### What is a computer?

A computer is a device that performs calculations millions or even billions of times faster than a human can and/or makes logical decisions. Supercomputers can perform hundreds of billions of additions per second, which is the amount of work a person could do in tens of years with a simple calculator.

Computers process data under the control of sets of instructions called computer programs. The computer programs that run on a computer are called **software**. The people who develop and write them are called **computer programmers**.

A computer consists of 6 logical units:

1. Input unit
1. Output unit
1. Memory
1. Arithmetic logic unit (central processing unit)
1. Control unit (central processing unit)
1. Secondary storage

### Evolution of operating systems

The first computers could do only one job at a time. Programs written on punched cards were fed to the computer through a card reader and run one after another (one job at a time). In this environment, where one job runs at a time, the computer's resources are not used efficiently: while the CPU is working, the input and output units sit idle. For more efficient use of resources, operating systems that allow **"multiprogramming"** were gradually developed. In these environments several jobs run at once, but users still enter their programs into the computer by punching them onto cards.

In the 1960s, **"timesharing"** operating systems were developed. In a timesharing environment, users access the computer through terminals (a screen and a keyboard). In this way, tens or even hundreds of people can access and use a single computer at the same time.

### Personal, distributed, and client/server computing

In 1977, Apple popularized personal computers. Starting as a hobbyist pursuit, personal computer use became very widespread not only in homes but also in business, when IBM introduced the Personal Computer in 1981.

However, these computers were stand-alone units. To share the data on a computer, it had to be carried to another computer on removable disks. **Distributed processing** began when stand-alone, independent computers were connected to one another through LANs or larger networks. Today, large amounts of data can be used by client computers through computers on the network called file servers, which store the programs and data to be shared (the **client/server environment**).

C and C++ are today widely used languages for writing these environments (computer networks, distributed client/server environments, and the operating systems that support them).

### Programming languages

In terms of the evolution of programming, we can speak of 4 classes:

1. **Machine languages (1st generation):** languages made up of numbers, understood only by a particular machine, and highly prone to errors.
1. **Assembly languages (2nd generation):** languages made up of English-like commands. A program written in assembly language is converted into machine language by a translator and then run. Although it looks fairly understandable, a large number of instructions must be written even for a very simple task.
1. **High-level languages (3rd generation), "procedural" languages:** languages in which we specify in detail "HOW" something is to be done. They resemble English and use the symbols we use in arithmetic operations; programs are written faster and more easily. C and C++ belong to this group.
1. **Very high-level languages (4th generation):** languages in which we state "WHAT" is to be done: LISP, SNOBOL, FORTH, SQL…

Many languages were developed in the 3rd generation. Those that gained wide acceptance:

| Language | Developed by | Year | Note |
|---|---|---|---|
| Fortran | IBM | 1954 | Still widely used in engineering applications. |
| Cobol | | 1959 | Half of today's commercial applications are written in Cobol. |
| Pascal | Niklaus Wirth | 1971 | For academic use |

### History of C and C++

| Language | Year | Developed by | Institution |
|---|---|---|---|
| BCPL | 1967 | Martin Richards | |
| B | 1970 | Ken Thompson | Bell Laboratories |
| C | 1972 | Dennis Ritchie | Bell Laboratories |
| C++ | 1980 | Bjarne Stroustrup | AT&T |

C was used to write the UNIX operating system; it is a machine-independent language. Between 1983 and 1989, ANSI produced the standard definition of C; the standard was published in 1990: ANSI/ISO 9899:1990.

C++ brought **object-oriented programming** capabilities, along with a number of additional features, to C. Objects are reusable software components; they make software development much easier (more productive). Other object-oriented languages:

- **Smalltalk:** Xerox Palo Alto Research Center
- **Java:** Sun Microsystems, James Gosling, 1995 (1993, the popularization of the WWW)

*Note: The source reads "James Goslin 995"; it should be James Gosling and 1995.*

### The C++ standard library

C++ programs consist of classes and functions. These are program pieces. Some of them are written by the programmer, and some are readily available in the standard library.

### Structured programming

Until the 1960s, programming was very complex, difficult, and costly. **Structured programming** began to emerge in the 1960s. Structured programming is an approach to writing programs that are clearer, more understandable, and easier to read, follow, and test.

Three basic structures are used: **sequence**, **repetition structure**, and **decision structure**. Goto is not used, or is used as little as possible. One of the first languages suited to this (and we could say the most popular) is Pascal (Niklaus Wirth, 1971). It was developed to teach structured programming in academic settings and was widely used in many schools. However, the fact that it lacked many of the features needed in commercial applications and in applications suited to every kind of business environment prevented it from gaining wide acceptance outside universities.

Ada: 1970s – early 1980s, US Department of Defense.

### Key software trend: object technology

Advances and progress in software technology began with structured programming, structured design, and structured analysis. However, greater progress was achieved with object-oriented analysis, design, and programming. With the object-oriented approach, we model all the objects around us (car, student, course, person, airplane, classroom, etc.). Not only can we reuse these modeled software pieces repeatedly, but software written in this way is also better organized and more understandable, so it is much easier to maintain, saving the programmer a great deal of time and cost (80% of software cost belongs not to the effort at the start of programming and writing, but to the continuous maintenance done afterwards).

Although C++ is referred to as an object-oriented language, it is a **hybrid** language; that is, it makes it possible to write both structured and object-oriented programs.

Until the topic of "Classes and Data Abstraction," we will cover "procedural" programming concepts with C++: control structures, functions, data types, input/output, arrays, pointers, and strings. These chapters will cover the C part of C++ and the procedural enhancements C++ makes to C.

### Stages of executing a C++ program

Executing a C++ program in a Unix environment goes through 6 stages:

1. **Edit:** writing the source program with an editor program. The extension is .cpp, .cxx, or .c
1. **Preprocess:** some operations before compilation
1. **Compile:** the output of compilation is the object program
1. **Link:** bringing together (linking) the functions found in the standard library or special libraries that we have specified we will use in our program with the object program
1. **Load:** taking the program and any necessary modules (from shared libraries) from disk and loading them into memory
1. **Execute**

Diagram: p. 15 (Deitel).

### Portability

Although it is possible to write portable programs, some problems arise between different systems and different compilers. Issues related to portability are covered in the ANSI standard document: www.ansi.org. Document title: *Information Technology – Programming languages – C++*. Document number: ISO/IEC 14882-1998. Older draft version (free): www.cygnus.com/misc/wp/

### Good programming practices

- Write your C++ programs in a simple and straightforward manner: KIS ("Keep It Simple").
- The manual of the C++ version you are using should be at hand.
- The best teacher is your computer. You can learn and gain experience by running the topics and examples covered in books or lectures on the computer, reading the error messages that appear, and trying again.

## Introduction to programming with C++

### A simple program: printing a line of text

```cpp
// C++ ile ilk programım
#include <iostream>

int main()
{
    std::cout << "Herkese Merhaba!\n";

    return 0;   // program sonu
}
```

```
Herkese Merhaba!
```

- `//` is placed at the beginning of a comment line in C++. The compiler does nothing for these lines; they are comment lines that appear as-is in the program listing and are needed for the readability and understandability of the program. A good programmer puts the necessary comments in the necessary places. In C, comments are placed between `/*  */`.
- Lines that begin with `#` are for the preprocessor. In our example program, the line beginning with `#` tells the preprocessor to include the `iostream` header file, which is related to input/output, in the program.
- `int main()` must be present in every C++ program. Every C++ program consists of one or several functions. The `()` indicates that main is a function, and the word "main" indicates that it is the main function.
- `int` means integer. The meaning of `int main()` is: the value this main function returns after it runs is an integer (the zero returned by `return 0`).
- The body of a function begins with the left brace `{` and ends with the right brace `}`.
- `std::cout` is used for output to the screen; we will see it in more detail in later chapters. `std::cin` is for reading what is entered from the keyboard.
- `<<` is the "stream insertion operator."
- Note that the `\n` characters do not appear in the output! `\` is the "escape" character; `n` tells the cursor to move to the next line.

| Escape sequence | Meaning |
|---|---|
| `\n` | new line |
| `\t` | move forward one "tab" |
| `\r` | the cursor moves to the beginning of the line being written ("carriage return") |
| `\a` | alert sound |

*Note: The source calls curly braces "square brackets"; `{ }` are braces (curly brackets). Also, the code on the page was typed with curly quotes (“ ”); straight quotes (") are used here so that it can compile.*

How else could we have printed the sentence "Herkese Merhaba!"?

```cpp
std::cout << "Herkese ";
std::cout << "Merhaba!\n";
```

What would the output be if I wrote it as follows?

```cpp
std::cout << "Herkes\ne\nMerhaba!\n";
```

```
Herkes
e
Merhaba!
```

### Another simple program: adding two integers

```cpp
// İKİ TAMSAYIYI TOPLAYAN PROGRAM
#include <iostream>

int main()
{
    int tamsayi1, tamsayi2, toplam;   // tanımlamalar

    std::cout << "Birinci tamsayıyı giriniz\n";
    std::cin >> tamsayi1;   // klavyeden girilen sayıyı oku
    std::cout << "İkinci tamsayıyı giriniz\n";
    std::cin >> tamsayi2;   // klavyeden girilen sayıyı oku
    toplam = tamsayi1 + tamsayi2;
    std::cout << "Toplam = " << toplam << std::endl;

    return 0;   // programın başarıyla bittiğini gösterir
}
```

`std::endl`: endl means "end line." What it does is flush the output buffers after writing the newline (sending it to the screen). As is known, data to be sent to the output is accumulated in output buffers before being sent. We use endl to empty/flush the buffers after the output operation.

**Important notes:**

- C++ is a case-sensitive language.
- Statements end with `;` (semicolon).

**Good programming practices:**

1. Lines written inside the body of a function are indented by 3 spaces ("indentation").
1. Leave a blank line between declarations and executable statements.
1. Use meaningful variable names.
1. Leave one space on each side of binary operators.

### Arithmetic operators

| C++ operation | Arithmetic operator | Algebraic expression | C++ expression |
|---|---|---|---|
| Addition | `+` | f + 7 | `f + 7` |
| Subtraction | `-` | p − c | `p - c` |
| Multiplication | `*` | bm | `b * m` |
| Division | `/` | x/y | `x / y` |
| Modulus | `%` | r mod s | `r % s` |

Rules of operator precedence in arithmetic operations in C++:

1. Expressions inside parentheses are evaluated first.
1. Next, multiplication, division, and modulus operations are performed. If an arithmetic expression contains more than one multiplication, division, or modulus operation, the operators in these operations are applied from **left to right**. Multiplication, division, and modulus operators have the same precedence.
1. Addition and subtraction operations are performed last. If an expression contains more than one addition and subtraction operation, their operators are applied from **left to right**.

Examples: pp. 31–33 (Deitel).

**Good programming practice:** As in algebra, unnecessary parentheses may be omitted. However, especially in long expressions, it is good to increase understandability by enclosing subexpressions in parentheses.

### Relational operators and equality operators

| Algebraic operator | C++ equivalent | C++ example | Meaning |
|---|---|---|---|
| > | `>` | `x > y` | x is greater than y |
| < | `<` | `x < y` | x is less than y |
| ≥ | `>=` | `x >= y` | x is greater than or equal to y |
| ≤ | `<=` | `x <= y` | x is less than or equal to y |
| = | `==` | `x == y` | x is equal to y (equality operator) |
| ≠ | `!=` | `x != y` | x is not equal to y (equality operator) |

*Note: The symbols ≥, ≤, and ≠ do not appear in the page printout (they were left blank); they were added to the table.*

**Common errors:**

- When writing the operators `==`, `>=`, `<=`, `!=`, no space should be left between the two characters, and the order of the two characters should not be swapped.
- Do not confuse the equality operator `==` with `=`, which is used for assignment.

### A sample program using equality and relational operators

```cpp
// if cümlesi ile eşitlik ve ilişki/bağıntı operatörlerini kullanan bir program
#include <iostream>

using std::cout;   // program cout kullanır
using std::cin;    // program cin kullanır
using std::endl;   // program endl kullanır

int main()
{
    int sayi1, sayi2;

    cout << "İki tamsayi giriniz.\n"
         << "Ben aralarındaki ilişkiyi söyleyeceğim: ";
    cin >> sayi1 >> sayi2;

    if (sayi1 == sayi2)
        cout << sayi1 << sayi2 << "'ye eşittir." << endl;
    if (sayi1 != sayi2)
        cout << sayi1 << sayi2 << "'ye eşit değildir." << endl;
    if (sayi1 < sayi2)
        cout << sayi1 << ", " << sayi2 << "'den küçüktür." << endl;
    if (sayi1 > sayi2)
        cout << sayi1 << ", " << sayi2 << "'den büyüktür." << endl;
    if (sayi1 <= sayi2)
        cout << sayi1 << ", " << sayi2 << "'den küçük veya eşittir." << endl;
    if (sayi1 >= sayi2)
        cout << sayi1 << ", " << sayi2 << "'den büyük veya eşittir." << endl;

    return 0;
}
```

Sample runs:

```
İki tamsayı giriniz.
Ben size aralarındaki ilişkiyi söyleyeceğim: 3 7
3, 7'ye eşit değildir.
3, 7'den küçüktür.
3, 7'den küçük veya eşittir.
```

```
İki tamsayı giriniz.
Ben size aralarındaki ilişkiyi söyleyeceğim: 22 12
22, 12'ye eşit değildir.
22, 12'den büyüktür.
22, 12'den büyük veya eşittir.
```

```
İki tamsayı giriniz.
Ben size aralarındaki ilişkiyi söyleyeceğim: 7 7
7, 7'ye eşittir.
7, 7'den küçük veya eşittir.
7, 7'den büyük veya eşittir.
```

*Note: Because `", "` is not printed between the two numbers in the first two `if` lines of the program, this program would actually print "37'ye eşit değildir."; to obtain the output shown, those lines would also need to be of the form `cout << sayi1 << ", " << sayi2 << ...`. The phrase "Ben size aralarındaki…" in the sample outputs also differs slightly from the text in the code.*

**Using statements:** They eliminate the need for `std::` before `cout` and `cin`. As you will recall, we used `std::cout` in our first simple example. When a lot of input/output will be done, writing `std::` before every `cout` and `cin` would not be very practical. For this reason, it is worthwhile to use `using`.

**Good programming practices:**

1. To increase the readability of the program, indent the statements inside an `if` structure by 3 spaces.
1. There should not be more than one statement on a line.
1. If a statement does not fit on one line and continues on the next line, take care to break the statement at a meaningful place.

*Page tags: c++, c++ lessons, c++ files, what is c++, c++ programming, history of c++, introduction to programming with C++, programming languages.*
