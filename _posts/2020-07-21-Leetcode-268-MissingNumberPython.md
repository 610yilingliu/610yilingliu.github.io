---
layout:     post
title:      Leetcode 268. Missing Number (Python) - Four ways to solve it
subtitle:   Leetcode Python Solution
date:       2020-07-21
author:     Yiling
header-img: img/python/pylogo.png
catalog: true
tags:
    - Python
    - Leetcode
---


**This tutorial is from my [Medium blog](https://medium.com/@yilingliu1994/4-different-ways-to-solve-leetcode-268-missing-number-e449981af8d6), I will no longer to use it because it is not as flexible as markdown format.**

Problem could be found on Leetcode [Here](https://leetcode.com/problems/missing-number/)

# Problem Description

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
```
Input: [3,0,1]
Output: 2
```
Example 2:
```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```
Note:

Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# My Solution

## Solution 1: List


Sort the list, and inspect elements inside this sorted list. If the value of the next element minus the current element is larger than one, than the missing number will be the value of the current element + 1

### Code (Python)
```py
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                return nums[i] + 1
        return nums[-1] + 1
```

**Time Complexity: O(nlogn) + O(n)**

O(nlogn) to sort the list, and O(n) to go through it

 The note in problem description requires you to use algorithms with linear complexity, so I suggest you not to use it although it is easy to understand.

## Solution 2: Dictionary

Create a set with all elements inside it, and remove the elements from that set which could be found in given list

### Code (Python)

```py
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        whole = set([item for item in range(0, n)])
        for item in nums:
            whole.remove(item)
        for rest in whole:
            ans = rest
        return ans
```

**Time Complexity: O(n)**

O(n) to create the new list, O(n) to convert list to set, and O(n) to go through the given list, O(n) to remove all elements(except missing number) from the set. The total time complexity is still O(n)

## Solution 3: Bit-Manipulation

Remember if `num1 == num2`, than `num1^num2 = 0`.

So we can create a list include missing number, and merge this list with nuns together using `^` operator

### Code (Python)

```py
class Solution:
    def missingNumber(self, nums):
        largest = len(nums)
        s1 = 0
        s2 = 0
        for item in range(largest + 1):
            s1 ^= item
        for num in nums:
            s2 ^= num
        return s1 ^ s2
```

Spends O(n) to go through the new list, and O(n) to go through the given one.

You should know how the bitwise operators work before using this method. Bitwise method is quite efficient in some cases, for example, you can use `a & 1 == 0` instead of `a//2 == 0` while you want to know if `a` is an even number or not.

## Solution 4: Math Trick

Simply use the sum of arithmetic progression minus the sum of the provided array.
You can also use `number >> 1` instead of `int(number/2)` to speed up the process

```py
class Solution:
    def missingNumber(self, nums):
        largest = len(nums)
        # n = (0 + largest)/1 + 1
        n = largest + 1
        # arithmetic_sum = int((0 + largest) * n / 2)
        arithmetic_sum = int(largest * n / 2)
        return arithmetic_sum - sum(nums)
```

