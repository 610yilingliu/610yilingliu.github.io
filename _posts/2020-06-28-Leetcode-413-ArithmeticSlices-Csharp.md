---
layout:     post
title:      Leetcode 413. Arithmetic Slices Csharp(C#) Solution
subtitle:   Leetcode With Csharp series tutorial
date:       2020-06-28
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

Problem could be found on Leetcode [Here](https://leetcode.com/problems/arithmetic-slices/)

# Problem Description

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```

The following sequence is not arithmetic.

```
1, 1, 2, 5, 7
```

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

```
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
```

# My Solution

## Code

Version 1: Easier to Understand
```c#
public class Solution {
    public int NumberOfArithmeticSlices(int[] A) {
        if(A is null || A.Length < 3) return 0;
        int ans = 0;
        int pregap = A[1] - A[0];
        int counter = 2;
        for(int i = 1; i <A.Length - 1; i ++){
            if(A[i + 1] - A[i] == pregap) counter ++;
            else{
                if(counter >= 3){
                    for(int c = 3; c <= counter; c++){
                        ans += counter - c + 1;
                    }
                }
                counter = 2;
                pregap = A[i + 1] - A[i];
            }
        }
        if(counter >= 3){
            for(int c = 3; c <= counter; c++){
                ans += counter - c + 1;
            }
        }
        return ans;
    }
}
```

Version 2: Shorter
```c#
public class Solution {
    public int NumberOfArithmeticSlices(int[] A) {
        if(A is null || A.Length < 3) return 0;
        int ans = 0;
        int pregap = A[1] - A[0];
        int counter = 2;
        for(int i = 1; i <A.Length - 1; i ++){
            int curgap = A[i + 1] - A[i];
            if(curgap == pregap){
                counter ++;
                if(counter > 2){
                    // remember 3 - 2, 4 - 2, 5 - 2 equal to 5 - 4, 5 - 3, 5 - 2 so we can use this instead.
                    ans += counter - 2;
                }
            }
            else{
                counter = 2;
                pregap = curgap;
            }
        }
        return ans;
    }
}
```
## Explain
**Time Complexity: O(n)** - n is the length of `A`

**Core concept**

Remenber the number of continuous subarray with length `sub_l` in array with length `l` equal to `l - sub_l + 1`, like the following example:

![Continous Subarray with Length = 3 in [1,2,3,4,5,6]](\img\csharp\leetcode413-1.png)

So the number of subarray with length = 4, 5, 6... (Use sub_l<sub>n</sub> to represent subarray with length n)in the example shown above is 3, 2, 1. That means, the number of subarrays that length >= 3 equal to:

sub_l<sub>3</sub> + sub_l<sub>4</sub> + sub_l<sub>5</sub> + sub_l<sub>6</sub> = 4 + 3 + 2 + 1

**Analyze via an example**

Use version 1 to explain(I afraid that not everyone can understand the comment in Version 2)
In case:
```
A = [1, 2, 3, 4, 6, -2, -3, -4]
```
While the code is running

Initialize `pregap` = A[1] - A[0] = 2 - 1 = 1; `counter` = 2; `ans` = 0

Start for loop:

for `i` == 1:

`curgap` = A[1 + 1] - A[1] = 1, equal to pregap

Update counter, current `counter` = 3;

for `i` == 2:

almost the same to case i == 1, simply update `counter` = 4;

for `i` == 3:

`curgap` = A[3 + 1] - A[3] = 6 - 4 = 2, not equal to pregap

Now we need to settle the previous arithmetic slice. The length of previous arithmetic slice were counted by `counter`, which is 4 (Slice `[1, 2, 3, 4]`), it has two kinds of subarrays that are arithmetic slices, sub_l<sub>3</sub>  and sub_l<sub>4</sub>. According to the Core concept I already explained, sub_l<sub>3</sub> = length([1,2,3,4]) - 3 + 1 = 2, sub_l<sub>4</sub> = length([1,2,3,4]) - 4 + 1 = 1, so ans = 0 + 2 + 1;

Reset `counter` to 2, `pregap` = `curgap` = 2

for `i` = 4;

`curgap` = A[4 + 1] - A[4] = -8 , not equal to pregap;

Now variable `counter` = 2, smaller than 3, so do nothing with counter, simply set `pregap` = `curgap` = -8

for `i` = 5:

Almost the same with `i` = 4;

set `pregap` = `curgap` = -1

for `i` = 6:
`curgap` = A[6 + 1] - A[6] = -1 == `pregap`;

Update `counter` to 3.

Now we reach to the end of the array, but we still need to settle the arithmetic slice `[-2, -3, -4]` that had not been settled yet. add sub_l<sub>3</sub> of slice `[-2, -3, -4]` to ans, then the ans is the final answer we want.