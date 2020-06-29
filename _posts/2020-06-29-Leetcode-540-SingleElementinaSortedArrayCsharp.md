---
layout:     post
title:      Leetcode 540. Single Element in a Sorted Array Csharp(C#) Solution
subtitle:   Leetcode With Csharp series tutorial
date:       2020-06-29
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

Problem could be found on Leetcode [Here](https://leetcode.com/problems/single-element-in-a-sorted-array/)

# Problem Description

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:
```

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```
Example 2:

```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```

Constraints:

1 <= nums.length <= 10^5

0 <= nums[i] <= 10^5

# My Solution


## Solution 1. Bit Manipulation

**Time Complexity: O(n)**

### Code

```c#
public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        for(int i = 0; i < nums.Length; i += 2){
            try{
                if((nums[i] ^ nums[i + 1]) != 0) return nums[i];
            }
            catch{
                return nums[nums.Length - 1];
            }
        }
        return -1;
    }
}
```
If you don't know what bit manupulation is, come to [THIS PAGE](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/) to study about it, or Google by yourself.

In bit manupulation, if a == b, then a ^ b = 0. So we can group the numbers in the list two by two

In case:
```
nums = [1,1,2,2,3,4,4]
```
We can split it into 4 groups:
```
[1, 1]
[2, 2]
[3, 4]
[4]
```
1 ^ 1 = 0, 2 ^ 2 = 0, 3 ^ 4 != 0 so we can return 3 and break the searching loop.

That is what `if((nums[i] ^ nums[i + 1]) != 0) return nums[i];` in my code does

But what if the single number occurs at the end of the list?

From the problem we know that the length of list is always an odd number, so the last pair must be a single number. It will cause error in `nums[i] ^ nums[i + 1]`(i + 1 is out of range), so simply return the last element if there is an error.

`return -1` is not really useful in this problem, just meet the requirement of C#: every path should return something.
