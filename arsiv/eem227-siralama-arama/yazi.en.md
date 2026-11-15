---
baslik: EEM227 Data Structures: Sorting and Searching Algorithms (Week 4)
ozet: Week 4 lecture notes and programs for EEM227 Data Structures (Lecturer Oğul Göçmen, October 2007): bubble sort, selection sort, quick sort, shell sort, sequential search, binary search, and merge algorithms; with C and vector-template C++ code.
---

This post is the **week 4 lecture note** of the Fall 2007 **EEM227 Data Structures** course at Başkent University: sorting and searching algorithms. Prepared by **Lecturer Oğul Göçmen**, dated 21 October 2007. The text of the note and the example programs are below; at the end there are also additional programs written with the STL (vector) from the same week's folder. The PDF of the lecture note and all source files can be downloaded as a ZIP at the end of the post.

## Sorting and searching algorithms

Various sorting algorithms have been developed to sort the elements of an unordered array from smallest to largest or from largest to smallest, that is, to put them in order. Search operations are also easier on sorted data. The most commonly used sorting algorithms are the following:

1. Bubble sort
1. Shell sort (sorting by repeated halving)
1. Selection sort
1. Quick sort

## Bubble sort algorithm

Each element in the array is compared in turn with the element that follows it, and they are swapped if necessary. The sorting process continues as long as swaps occur. When analyzing the efficiency of any sorting method, one looks at how many comparisons and swaps (exchanges) are made. In bubble sort the number of comparisons is always the same. Even if the given array is already sorted, the two for loops used repeat the stated number of times. This means that the method makes (n² – n)/2 comparisons. Here n is the number of elements to be sorted. This formula is obtained by considering that the outer loop runs n-1 times and the inner loop runs n/2 times on average.

Bubble sort is said to be an n² algorithm, because its running time is proportional to the square of the number of elements it sorts. Therefore, it is an algorithm whose processing time grows large when the number of array elements is large. For a completely disordered data structure, that is, for the worst case, the Big-O notation of this algorithm is O(n²).

(n-1) + (n-2) + … + 2 + 1 = n·(n-1)/2 = O(n²)

*Note: In the lecture note this sum is written as n·(n-2)/2; the correct form is n·(n-1)/2 (the same as (n² – n)/2 above).*

As a special case, if a certain portion of the data is already sorted, and c of the n data items are not sorted, the complexity of the algorithm is O(cn).

### Example 1.1: sorting an array of random elements with bubble sort

```cpp
#include <iostream>

using namespace std;

//--------------------------- bubbleSort -----------------------------
//
// Purpose  : To sort the given values from smallest to largest
//
// Input parameter : The vector in which the values are stored
//
// Return value : void
//
// In this function, the sorting is implemented with the Bubble Sort
// algorithm.
//
//-----------------------------------------------------------------------

void bubbleSort ( int dizi[],int size)
{
      int temp;
// In each iteration, the for loop starts from the first of the unsorted
// elements and compares each element with its right neighbor. If it has
// a value greater than its neighbor, it is swapped with it.
      for (int i = size; i > 2; i --)
      {
// Here i indicates the number of unsorted elements, that is,
// the elements up to the (i-1)th term are not yet sorted.
// Each of the unsorted elements is compared with its right neighbor.
// If its value is greater than its neighbor's, it is swapped with it.
// Since the largest unsorted element is swapped with all elements up
// to the (i-1)th term, it reaches the beginning of the sorted elements.
// Since each of the elements that were already sorted has a greater
// value than this element, this element is now sorted as well.
            for (int j = 0; j < i - 1; j ++)
            {
            // Swaps with its neighbor. (swap)
                  if (dizi[j] > dizi[j + 1])
                  {
                        temp = dizi[j + 1];
                        dizi[j + 1] = dizi[j];
                        dizi[j] = temp;
                  }
            }
      }
}

//------------------------------ main -----------------------------------

int main ()
{
     int d[20];

// A random array of 20 elements is created.
     for (int i = 0; i < 20; i ++)
     d[i]=(rand () % 1000);
     bubbleSort (d,20);

     for (int i = 0; i < 20; i ++)
     cout<<d[i]<<" ";
     cout<<endl;
     system("pause");
     return 0;
}
```

*Note: Because the outer loop condition is `i > 2`, the last pass (the i = 2 step, which compares only `dizi[0]` and `dizi[1]`) is never performed; the first two elements may remain in reverse order. For example, the array {3, 2, 1} remains {2, 1, 3}. The condition should be `i > 1`. The same error is also present in Example 1.2 and in BubbleSortSTL.cpp in the folder.*

### Example 1.2: bubble sort (with the vector template)

```cpp
#include <iostream>
#include <vector>
using namespace std;

template <class T>
void bubbleSort (vector<T>& dizi)
{     for (int i = dizi.size (); i > 2; i --)
      { for (int j = 0; j < i - 1; j ++)
            { if (dizi[j] > dizi[j + 1])
                  {     T temp = dizi[j + 1];
                        dizi[j + 1] = dizi[j];
                        dizi[j] = temp;
                  }
            }
      }
}

//------------------------------ main -----------------------------------

int main ()
{
      vector<int> D;

// A random array of 20 elements is created.
      for (int i = 0; i < 20; i ++) D.push_back (rand () % 10);
      bubbleSort (D);
      return 0;
}
```

## Selection sort algorithm

In selection sort, if the array is to be sorted from smallest to largest, the first element is taken and the smallest-valued element among the rest is searched for; if one is found, it is swapped with the first element. Then the smallest of the remaining n-1 elements is found and swapped with the second element. The process continues in this way. This method also requires (n² – n)/2 comparisons. Even though the number of comparisons is the same as in bubble sort, the average number of swaps is lower.

T(n) = 2·(n-1) + 2·(n-2) + 2·(n-3) + … + 2·(n-(n-2)) + 2·(n-(n-1))
= 2·((n-1) + (n-2) + (n-3) + … + 2 + 1) (twice the sum of the first n-1 integers)
= 2·((n-1)·n/2) = n² – n

Therefore, the complexity of this algorithm is O(n²).

### Example 2.1: sorting from smallest to largest with selection sort (C)

```c
#include<stdio.h>
/* selection sort ile diziyi kucukten buyuye dogru siralar */
int main(void)
{
int d[10];
int i,j,n,min,yer;
printf(" dizinin eleman sayisini < 10 giriniz \n");
scanf("%d",&n);
printf(" dizi elemanlarini giriniz \n");
for (i=0;i<n;i++)
   scanf("%d",&d[i]);
for(i=0;i<n-1;i++)
{
   yer=i;
   min=d[i];
     for(j=i+1;j<n;j++)
         if(d[j]<min)
         {
              yer=j;
              min=d[j];
          }
       d[yer]=d[i];
       d[i]=min;
     }
  printf(" sirali dizi \n\n");

for(i=0;i<n;i++)
printf("%4d",d[i]);

return 0;
 }
```

### Example 2.2: selection sort (with the vector template)

```cpp
#include <iostream>
#include <vector>
using namespace std;

//--------------------------- selectionSort -----------------------------
//
// Purpose  : To sort the given values from smallest to largest
//
// Input parameter : The vector in which the values are stored
//
// Return value : void
//
// In this function, the sorting is implemented with the Selection Sort
// algorithm.
//
//-----------------------------------------------------------------------
template <class T>
void selectionSort (vector<T>& dizi)
{
      int minIndex;

       // In each iteration, the for loop finds the smallest among the
       // unsorted elements and stores the position of this value in the
       // vector in the variable named minIndex.
       for (int i = 0; i < dizi.size () - 1; i ++)
       {
             minIndex = i;

              // In the unsorted part of the vector (from i+1 onward),
              // the smallest-valued element is found. First, the first
              // element of the unsorted part is assumed to be the
              // smallest. Starting from this element, the other elements
              // are examined. If a smaller value is encountered, the
              // position of this element is now assigned to the variable
              // minIndex. Thus the smallest element in the unsorted part
              // is found.
              for (int j = i + 1; j < dizi.size (); j ++)
                    if (dizi [minIndex] > dizi [j]) minIndex = j;

              // swap operation
              // This newly found element is swapped with the first
              // unsorted element. If both are already the same element,
              // this exchange is not needed.
              if (minIndex != i)
              {
                    T temp = dizi[i];
                    dizi[i] = dizi[minIndex];
                    dizi[minIndex] = temp;
              }
       }
}

//------------------------------ main -----------------------------------

int main ()
{
      vector<int> D;

       // A random array of 20 elements is created.
       for (int i = 0; i < 20; i ++) D.push_back (rand () % 10);

       selectionSort (D);

       return 0;
}
```

## Quick sort algorithm

This is known as the best of the improved sorting algorithms. In its general operation, a value called the comparand is chosen and then the array is divided into two. Elements greater than or equal to the comparand are placed on one side, and smaller ones on the other side. This process is repeated on each remaining partition. The comparand is either chosen at random or computed as the average of the values of a small number of elements in the array.

For the quick sort algorithm, the average number of comparisons can be given as n log n and the average number of swaps as n/6 log n. The point to watch in this method is choosing the comparand well. If the value compared against is the largest value in each partition, the method will slow down. Choosing a sorting algorithm suited to the structure of the data will be the right approach. Although quick sort is the most efficient algorithm, it may not be efficient on arrays with few elements because of its repeated calls. For such arrays (100 elements or fewer), bubble sort or selection sort will give better results.

### Example 3.1: sorting strings with quick sort

```c
#include<iomanip>
/*karakter dizisini quick sort ile siralar */
#include<stdio.h>
#include<string.h>
void quick_str(char dizi[][10],int say);
void qs_string(char dizi[][10],int sol,int sag);
char str[][10]={"tulay","pelin","aysu","can","beril","ogul"};
int main(void)
{

int i;
quick_str(str,sizeof(str));
printf("siralanmis dizi\n");
for (i=0;i<sizeof(str);i++)
printf("%s\n",str[i]);
system("pause");
return 0;

}

void quick_str(char dizi[][10],int say)
{
qs_string(dizi,0,say-1);
}

void qs_string(char dizi[][10],int sol,int sag)
{
int i,j;
char *x;
char yedek[10];
i=sol;j=sag;
x=dizi[(sol+sag)/2];
do {
  while((strcmp(dizi[i],x)< 0) && (i< sag))i++;
  while((strcmp(dizi[j],x)> 0) && (j > sol))j--;
      if(i <= j)
        {
       strcpy( yedek,dizi[i]);
       strcpy( dizi[i],dizi[j]);
       strcpy( dizi[j],yedek);
          i++; j--;
        }
     }while(i <= j);
     if(sol < j) qs_string(dizi,sol,j);
     if(i < sag) qs_string(dizi,i,sag);
}
```

Expected sorted output: aysu, beril, can, ogul, pelin, tulay.

*Note: `sizeof(str)` gives the size of the array in bytes, not the number of elements (6 × 10 = 60). Both in the `quick_str` call and in the printing loop, `sizeof(str)/sizeof(str[0])` (that is, 6) should be used as the element count; otherwise the array bounds are exceeded. Also, the pivot `x` is not a copy but a pointer to a row in the array; since the contents of that row can change during swaps, it is safer to first copy the pivot into a separate array such as `yedek`.*

### Example 3.2: quick sort (with the vector template)

```cpp
#include <iostream>
#include <vector>
using namespace std;

//---------------------------- quickSort --------------------------------
//
// Purpose  : To sort the given values from smallest to largest
//
// Input parameter : The vector in which the values are stored
//
//-----------------------------------------------------------------------

template <class T>
void quickSort (vector<T>& dizi)
{
      quickSort (dizi, 0, dizi.size () - 1);
}

//---------------------------- quickSort --------------------------------
//
// Input parameters : The vector in which the values are stored. Two
//                    variables named sol and sag that indicate which
//                    range of this vector we are interested in. A pivot
//                    will be chosen from within this range, and this
//                    range will be divided into two parts.
//
//-----------------------------------------------------------------------

template <class T>
void quickSort (vector<T>& dizi, int sol, int sag)
{
      int x = sol;
      int y = sag;
      T pivot = dizi[x]; // The first element of the given range is chosen as the pivot

       // Elements greater than the pivot are moved to the right side,
       // and elements smaller than the pivot are moved to the left side.
       // At the end, the pivot is placed in the middle of the two new
       // groups formed.
       while (x < y)
       {
             // Find the first element on the right smaller than the pivot
             while ((dizi[y] >= pivot) && (x < y)) y --;

              // Move this element to the left
              if (x != y)
              {
                    dizi[x] = dizi[y];
                    x ++;
              }

              // Find the first element on the left greater than the pivot
              while ((dizi[x] <= pivot) && (x < y)) x ++;

              // move this element to the right
              if (x != y)
              {
                    dizi[y] = dizi[x];
                    y --;
              }
       }

       dizi[x] = pivot; // the pivot has been moved here

       int pivotIndis = x; // the new position of the pivot

       // Elements smaller than the pivot are now in the range [sol,pivotIndis-1].
       // Elements greater than the pivot are now in the range [pivotIndis+1,sag].
       // For each of these two ranges, if the length of the range is greater
       // than one, the quickSort function is called again recursively

       if (sol + 1 < pivotIndis)
             quickSort (dizi, sol, pivotIndis - 1); // left side of the pivot

       if (sag - 1 > pivotIndis)
             quickSort (dizi, pivotIndis+1, sag); // right side of the pivot
}

//------------------------------ main -----------------------------------

int main()
{
      vector<int> D;

       // A random array of 100 elements is created.
       for (unsigned int i = 0; i < 100 ; i ++) D.push_back (rand ()%10);

       quickSort (D);

       return 0;
}
```

## Shell sort algorithm

Although this sort takes its name from D. L. Shell, who developed the algorithm, it is referred to by this name because its way of working resembles seashells (shell) stacked on top of one another. To sort n elements, the running time of the method can be said to be proportional to n^1.2. In this case, shell sort is seen to be an improved algorithm compared with n-squared algorithms.

There is no code for shell sort in the lecture note; `ShellSort.cpp` in the folder sorts the array from largest to smallest. The gap (`orta`) is first taken as (n-1)/2 and is halved in each round; for each gap, elements that far apart are compared and swapped if necessary.

```c
#include <stdio.h>
/* shell sort algoritmasi ile buyukten kucuge siralama yapar */
int main (void)
{
int a[10],i,j,n,orta,k,yedek;
printf(" dizinin eleman sayisini < 10 giriniz \n");
scanf("%d",&n);
printf("Diziyi  giriniz\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
orta=(n-1)/2;
     while(orta >0){
	  for(i=orta+1;i<n;i++){
              j=i-orta;
	      while(j>0){
                k=(j-1)+orta;
	        if(a[j-1]>=a[k]) j=0;
	        else {
		yedek=a[j-1];
		a[j-1]=a[k];
                a[k]=yedek;
                j=j-orta;
	       }
	    }
	 }
    orta=orta/2;
    }
printf("Siralanmis Dizi\n");
for(i=0;i<n;i++)
printf("%3d",a[i]);
scanf("%d",&n);
return 0;
}
```

*Note: Since the initial gap is `(n-1)/2`, for n = 2 the gap is 0 and the loop never runs; a two-element array is not sorted. The initial gap should be `n/2`.*

## Searching algorithms

Searching for information in an unsorted array is possible in two ways: a sequential search is performed that either ends when an equal element is found, starting from the first element, or ends the search when the end of the array is reached. If a sorted array is used, results can be obtained in a shorter time with the binary search algorithm.

### Sequential search

This is a simple algorithm that searches an array with a known number of elements until the desired information is found.

```c
# include <stdio.h>
# include <stdlib.h>
/* sirali arama yapar */
int sirali_ara (int a[],int n)
{
int sonuc,x,j;
printf("aranacak sayiyi Giriniz:\n");
scanf("%d",&x);
for(j=0;j<n;j++){
if(a[j]==x){
sonuc=j;
break;
}
else sonuc=-1;
}
return(sonuc);
}
int main (void)
{
int n,i,dizi[10],x,bul;
printf("dizinin eleman sayisini giriniz < 10:\n");
scanf("%d",&n);
printf("dizi elemanlarini Giriniz:\n");
for (i=0;i<n;i++)
scanf("%d",&dizi[i]);
bul=sirali_ara(dizi,n);
if(bul==-1)printf(" aranan sayi dizide yer almiyor\n");
else
printf(" aranan sayi dizinin %d . elemanidir",bul);
return 0;
}
```

*Note: In the lecture note, two comparisons are written as `= =` (with a space in between); this does not compile in C and should be `==` (the corrected version is shown above).*

### Binary search

In this method, the element exactly in the middle of the sorted array is taken first and compared with the number being searched for. If the searched number is greater than the middle element, the middle element of the second half is found and compared again. The process continues until the searched number is found. In binary search, the number of comparisons in the worst case is log₂n.

```c
#include <stdio.h>
/* binary search algoritmasi ile sirali dizide arama yapar */
int main (void)
{
int a[10],i,bas,son,x,orta,bul,n;
printf(" dizinin eleman sayisini < 10 giriniz \n");
scanf("%d",&n);
printf("Diziyi sirali olarak giriniz\n");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
printf("\n aranacak sayıyı giriniz\n");
scanf("%d",&x);
     bas=0;son=n;
     bul=0;
     while(bas <= son && bul==0){
        orta=(bas+son)/2;
        if(x==a[orta]) bul=1 ;
        else
        if(x>a[orta]) bas=orta+1;
        else
          son=orta-1;
        }
     if(x==a[orta]) printf("aranan sayı%3d dizideki indisi:%3d",x,orta);
     else printf("bulunamadı");
scanf("%d",&x); // ekranı durdurma
return 0;
}
```

*Note: The last index should be `son=n-1`, not `son=n`; if the searched number is greater than the largest element in the array, the program reads the element `a[n]`, which is outside the array.*

## Merge algorithm

This is an algorithm that merges two sorted input arrays.

```c
# include <stdio.h>
/* merge algoritmasi ile iki sirali diziyi birlestirir */
// Not Her iki girilen dizide kendi içinde sıralı olmalıdır...

int main (void)
{
int a[10],b[10],d[20];
int n,m,i,j,l;
printf("ilk dizinin boyutu < 10 ?\n");
scanf("%d",&n);
printf("ikinci dizinin boyutu <10 ?\n");
scanf("%d",&m);
printf(" birinci dizinin elemanlari\n ");
for(i=0;i<n;i++)
scanf("%d",&a[i]);
printf(" ikinci dizinin elemanlari\n ");
for(i=0;i<m;i++)
scanf("%d",&b[i]);
a[n]=b[m-1];
b[m]=a[n-1];
i=0;
j=0;
for(l=0;l<n+m;l++)
   if(a[i]<=b[j]){
      d[l]=a[i];
      i++;
      }
      else
      { d[l]=b[j];
         j++;
      }
printf(" birlestirilmis dizi \n\n" );
for(i=0;i<n+m;i++)
printf("%5d",d[i]);
scanf("%d",&n); // ekranı durdurmak için
return 0; }
```

The program places the last (largest) element of the other array at the end of each array as a "sentinel" value; thus, when one of the arrays is exhausted, reading continues from the other without a separate bounds check.

*Note: If, when the first array is exhausted, values equal to the sentinel remain in the second array, the sentinel may still be selected and `i` may advance beyond the array; also, if 10 is entered as the size, `a[10]`/`b[10]` overflows. In a safe version, the loop is written with the conditions `i<n` and `j<m`.*

## Additional programs in the folder (with STL vector)

In the same week's folder, besides the .cpp files of the programs in the lecture note, there are a few additional programs that use the STL vector.

### STL and vector

The comment at the beginning of the `STL.cpp` file:

> STL (Standard Template Library) is a general set of routines used to process data. Vector, deque, and list are container classes.

> Vectors can be thought of as smart arrays. When adding or removing data, vectors perform memory allocation on your behalf by expanding and shrinking the vector size. You can use vectors very much like arrays by accessing vector elements with the [] operator. Such random accesses are very fast with vectors. Adding new elements to the end (back) of a vector is also fast. In such a case, the vector size is automatically increased to hold the new data item.

> To define the vector D, the vector's default constructor (without arguments) is used. As in all STL containers, the template form is used to specify the variable type the container will hold (the int type in this example). The size of the container is not stated explicitly; therefore the container starts from 0.

> The push_back() member function adds the parameter it takes to the end of the vector. The back (end) of the vector is where the element with the highest index number is located. The front of the vector is where the index number is 0, and it is not used to add new elements.

> As soon as the vector starts to contain data, this data becomes accessible for reading and writing by means of the overloaded [] operator, just as if it were in an array. The size() member function returns the number of elements currently in the container.

```cpp
#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void foo(vector<T>& dizi)
{
  for(int i=0;i<dizi.size();i++)
    cout<<dizi[i]<<" ";
}

int main()
{
    vector<int> v;
    v.push_back(10);
    v.push_back(112);
    v.push_back(15);
    v.push_back(56);
    v.push_back(17);
    v.push_back(19);
    v.push_back(33);

    foo(v);

    system("pause");
    return 0;
}
```

```
10 112 15 56 17 19 33
```

### Sequential search (with the vector template)

`seqSearch` returns the index of the searched value if it finds it in the range [first, last), and returns `son` (the last value) if it does not.

```cpp
// Sequential Search...
//-----------------------
#include <iostream>
#include <iomanip> // for the setw function
#include <vector>

using namespace std;

template <class T>
int seqSearch (vector<T>& dizi,int ilk, int son, int aranan)
{
	int i=ilk;
	while(i != son && dizi[i] != aranan)
	i++;

	return i;
}

//------------------------------ main -----------------------------------

int main ()
{
    vector<int> D;
    int x;

    // A random array of 20 elements is created.
	for (int i = 0; i < 10; i ++)
     D.push_back (rand () % 150);

	for(int i=0;i<D.size();i++)
	cout<<setw(4)<<'['<<i<<']'<<setw(5)<<D[i]<<"\n";
	cout<<"Aranacak Deger ? ";
	cin>>x;
	cout<<"Indis No : "<< seqSearch(D,0,D.size(),x)<<endl;
    system("pause");
	return 0;
}
```

Sample run from the file (10 random values; if not found, it prints "Indis No : 10"):

```
   [0]   41
   [1]   17
   [2]   34
   [3]  100
   [4]  119
   [5]  124
   [6]   78
   [7]  108
   [8]  112
   [9]   14
Aranacak Deger ? 119
Indis No : 4
Press any key to continue . . .
```

### Binary search (with the vector template)

```cpp
// Binary  Search...
// Code for finding the searched value in a sorted array
#include <iostream>
#include <iomanip> // for the setw function
#include <vector>

using namespace std;

template <class T>
int binSearch (vector<T>& dizi,int ilk, int son, int aranan)
{
	int orta; // index of the midpoint
	T ortadeger; // value to be assigned to dizi[orta]
	int origSon=son; // save the original value of son

	while(ilk < son)
	{
    orta=(ilk+son)/2;
	ortadeger=dizi[orta];

	if(aranan==ortadeger)
	   return orta;
    else if ( aranan < ortadeger)
       {
       son=orta; // search in the lower sublist
       binSearch (dizi,ilk,son,aranan);
       }
    if ( aranan > ortadeger)
       {
       ilk=orta+1; // search in the upper sublist
       binSearch (dizi,ilk,son,aranan);
       }
    }
    return origSon; // the searched value was not found...
}

//------------------------------ main -----------------------------------

int main ()
{
    vector<int> D;
    int x;

    // A sorted array of 20 elements is created.
	for (int i = 0; i < 20; i ++)
     D.push_back (i*10-3);

	for(int i=0;i<D.size();i++)
	cout<<setw(4)<<'['<<i<<']'<<setw(6)<<D[i]<<"\n";
	cout<<"Aranacak Deger ? ";
	cin>>x;
	cout<<"Indis No : "<< binSearch(D,0,D.size(),x)<<endl;
    system("pause");
	return 0;
}
```

Sample run from the file (if not found, it prints "Indis No : 20"):

```
   [0]    -3
   [1]     7
   [2]    17
   [3]    27
   [4]    37
   [5]    47
   [6]    57
   [7]    67
   [8]    77
   [9]    87
   [10]    97
   [11]   107
   [12]   117
   [13]   127
   [14]   137
   [15]   147
   [16]   157
   [17]   167
   [18]   177
   [19]   187
Aranacak Deger ? 127
Indis No : 13
Press any key to continue . . .
```

*Note: The return values of the recursive `binSearch(...)` calls inside the function are not used; what actually finds the result is the `while` loop itself, since `ilk` and `son` are updated. These calls needlessly repeat the same search.*

### Other files

- `BubbleSortSTL.cpp`: the vector version of bubble sort; it prints the first 10 elements before and after sorting.
- `STLSelectionSort.cpp`: the vector version of selection sort; while sorting an array decreasing from 10 to 1, it prints the array at the end of each pass.
- `QuickSortTemplate.cpp`: the non-template version of the quick sort in Example 3.2, written with an int array; it sorts 20 random numbers and prints them.

*Note: In `BubbleSortSTL.cpp`, the `for(int i=10;i>0;i++)` loop that fills the vector never terminates (it should be `i--`). In this file and in `STLSelectionSort.cpp`, the functions are declared to return `T` but have no `return` (they should be `void`). In `QuickSortTemplate.cpp`, the call `quickSort(d,0,20)` passes 20 as the last index; for a 20-element array the last index is 19.*
