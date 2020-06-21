---
layout:     post
title:      Leetcode 7. Reverse Integer
subtitle:   Leetcode With Csharp serious tutorial
date:       2020-06-19
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

Problem could be found on Leetcode [Here](https://leetcode.com/problems/reverse-integer/)

# Problem Description

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
```
Input: 123
Output: 321
```
Example 2:
```
Input: -123
Output: -321
```
Example 3:
```
Input: 120
Output: 21
```
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2<sup>31</sup>,  2<sup>31 − 1</sup>]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# My Solution

## Code
```
public class Solution {
    public int Reverse(int x) {
        if(x == 0 || x == int.MinValue) return 0;
        int ans = 0;
        int pre_overflow = int.MaxValue / 10;
        int suf_overflow = int.MaxValue % 10;
        bool neg_tag = false;
        if(x < 0){
            neg_tag = true;
        }
        // return directly if x == 0
        x = Math.Abs(x);
        while(x > 0){
            int res = x % 10;
            // if the current answer > int.MaxValue % 10, in the following step, ans = ans * 10, it will cause overflow
            if(ans > pre_overflow) return 0;
            // if answer == int.MaxValue // 10, check the comming digit.
            if(ans == pre_overflow && res > suf_overflow) return 0;
            ans = ans * 10 + res;
            x = x / 10;
        }
        if(neg_tag == true){
            return -ans;
        }
        else return ans;
    }
}
```

## Explain

**Time Complexity: O(n)** - n is the length of (string)x

This problem have multiple solutions.

### String

Convert the input int into string, check if it has '-' at the beginning of the string or not. If yes, set variable ```neg_tag``` as true and remove str[0].

Then reverse the string by ```reversed_s = new string(s.Reverse().ToCharArray())```, if ```neg_tag``` is true, do ```reversed_s.Insert(0, "-")```

At the end convert string to int and return

### Long
Set variable ```ans``` as long type, let ``x % 10`` become current digit, return 0 if x < −2<sup>31</sup> or x > 2<sup>31 − 1</sup>, else return x

Remenber you cannot set ```ans``` as int type without check, otherwise it might cause error if ans > 2<sup>31 − 1</sup>

### Try/catch

Quite similar with "Long" solution but set ```ans``` as int type, if error(overflow), return -1 in catch.

### Int Only Solution

It is what my code does. Explained in the comment.