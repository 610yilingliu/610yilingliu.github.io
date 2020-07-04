---
layout:     post
title:      Leetcode 98. Range Addition II C & Csharp(C#) Solution
subtitle:   Leetcode With Csharp series tutorial
date:       2020-07-04
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
    - C
---

Problem could be found on Leetcode [Here](https://leetcode.com/problems/range-addition-ii/)

I am previewing HPC unit at school but it requires C knowledge, I almost forget it. So I will attached C code together with C# for review.

# Problem Description

Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
```
Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation: 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
```

Note:

The range of m and n is [1,40000].

The range of a is [1,m], and the range of b is [1,n].

The range of operations size won't exceed 10,000

# My Solution

## Code(C#)

```c#
public class Solution {
    public int MaxCount(int m, int n, int[][] ops) {
        int res_l = m;
        int res_h = n;
        for(int i = 0; i < ops.Length; i ++){
            res_l = Math.Min(res_l, ops[i][0]);
            res_h = Math.Min(res_h, ops[i][1]);
        }
        return res_l * res_h;
    }
}
```
## Code(C)

```c
int maxCount(int m, int n, int** ops, int opsSize, int* opsColSize){
    int res_l = m;
    int res_h = n;
    for(int i = 0; i < opsSize; i ++){
        if(ops[i][0] < res_l) res_l = ops[i][0];
        if(ops[i][1] < res_h) res_h = ops[i][1];
    }
    return res_l * res_h;
}
```
## Explain

The result matrix is always on the top-left of the origional matrix, so what we need to do is to find the intersection of matrixs in the list.

That means, we just need to continue updating the minimun value of operators[i][1] and operators[i][0] to find the down-right corner(point P) of the result matrix

![](\img\csharp\leetcode598.png)