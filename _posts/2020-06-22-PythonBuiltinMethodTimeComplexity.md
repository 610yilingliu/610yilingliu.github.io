---
layout:     post
title:      Time Complexity of Python3 Built-in Methods
subtitle:   Data structure
date:       2020-06-22
author:     Yiling
header-img: img\python\pylogo.png
catalog: true
tags:
    - DataStructure
    - Python
    - Documentation
---

## Note:

[1] = These operations rely on the “Amortized” part of “Amortized Worst Case”. Individual actions may take surprisingly long, depending on the history of the container.

[2] = For these operations, the worst case n is the maximum size the container ever achieved, rather than just the current size. For example, if N objects are added to a dictionary, then N-1 are deleted, the dictionary will still be sized for N objects (at least) until another insertion is made.

# List

**n: Number of Elements inside list**

**k: How many elements to operate**

|  Operation   | Average Case  | Amortized Worst Case |
|  ----  | ----  | ----  |
|Copy	|O(n)	|O(n)|
|Append[1]|	O(1)|	O(1)|
|Insert|	O(n)|	O(n)|
|Get Item|	O(1)|	O(1)|
|Set Item|	O(1)|	O(1)|
|Delete Item|	O(n)|	O(n)|
|Iteration|	O(n)|	O(n)|
|Get Slice|	O(k)|	O(k)|
|Del Slice|	O(n)|	O(n)|
|Set Slice|	O(k+n)|	O(k+n)|
|Extend[1]|	O(k)|	O(k)|
|Sort	|O(n log n)|	O(n log n)|
|Multiply	|O(nk)	|O(nk)|
|x in s	|O(n)	||
|min(s), max(s)|	O(n)||	
|Get Length|	O(1)|	|O(1)|

# Collections.deque

**n: Number of Elements inside queue**

**k: How many elements to operate**

|  Operation   | Average Case  | Amortized Worst Case |
|  ----  | ----  | ----  |
Copy	|O(n)|	O(n)
append	|O(1)|	O(1)
appendleft	|O(1)|	O(1)
pop	|O(1)|	O(1)
popleft	|O(1)|	O(1)
extend	|O(k)|	O(k)
extendleft	|O(k)|	O(k)
rotate	|O(k)|	O(k)
remove	|O(n)|	O(n)

# Dictionary

**n: Number of Elements inside dictionary**

|Operation|	Average Case|	Amortized Worst Case|
|  ----  | ----  | ----  |
|Copy[2]|	O(n)|	O(n)|
|Get Item|	O(1)|	O(n)|
|Set Item[1]|	O(1)|	O(n)|
|Delete Item|	O(1)|	O(n)|
|x in s	O(1)|	O(n)|
|Iteration[2]|	O(n)|	O(n)

# Set

**n: Number of Elements inside set**

|Operation|	Average Case|	Amortized Worst Case|
|  ----  | ----  | ----  |
x in s|	O(1)|	O(n)|
Union s\|t|	O(len(s)+len(t))
Intersection s&t	|O(min(len(s), len(t))	|O(len(s) * len(t))
Multiple intersection s1&s2&..&sn|		(n-1)*O(l) where l is max(len(s1),..,len(sn))
Difference s-t	|O(len(s))	
s.difference_update(t) |	O(len(t))	
Symmetric Difference s^t|	O(len(s))|	O(len(s) * len(t))
s.symmetric_difference_update(t)|	O(len(t))|	O(len(t) * len(s))

# Math Operations

|Operation|	Input|Time Complexity|
|  ----  | ---- | ---- |
|Multiplication| Two n-digit numbers | O(n<sup>2</sup>), and O(n<sup>1.585</sup>) for large numbers|
|Division|Two n-digit numbers|O(n<sup>2</sup>)|

# Tricks

num >> 1 is faster than num // 2

num * num is faster than num ** 2