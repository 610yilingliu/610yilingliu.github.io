---
layout:     post
title:      Leetcode 1. Two Sum Csharp(C#) Solution
subtitle:   Leetcode With Csharp series tutorial
date:       2020-06-17
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

Problem could be found on Leetcode [HERE](https://leetcode.com/problems/two-sum/)

# Problem Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```


# My Solution

## Code
```
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int len = nums.Length;
        Dictionary<int, int> walked = new Dictionary<int, int>();
        for(int i = 0; i < len; i ++){
            var rest = target - nums[i];
            if(walked.ContainsKey(rest))
                return new int[]{walked[rest], i};
            else
                if(!walked.ContainsKey(nums[i]))
                    walked.Add(nums[i], i);
        }
        return new int[0];
    }
}
```

## Explain

**Time Complexity: O(n)** - n is the length of nums.

**Key Point: Dictionary**


Get the diff between ```target``` and number we 'walked' and put them inside a ditionary like: 
```
dict = {
    rest1: target - walked1;
    rest2: target - walked2;
    .....
}
```

If you can find any ```rest``` in the following elements inside ```nums```, directly return this rest and its value. You just need to find one pair of the answer according to the problem.

You can also solve this problem through two for loops, like:
```
for(int i = 0; i < nums.Length - 1; i ++){
    for(int j = i + 1; j < nums.Length; j ++){
        if(nums[i] + nums[j] == target){
            return new int {nums[i], nums[j]}
        }
    }
}
```

But the time complexity of this solution is O(n<sup>2</sup>), it is not a good way to solve it in the job interview.