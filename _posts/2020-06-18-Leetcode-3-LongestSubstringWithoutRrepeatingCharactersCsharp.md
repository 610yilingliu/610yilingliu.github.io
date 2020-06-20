---
layout:     post
title:      Leetcode 3. Longest Substring Without Repeating Characters
subtitle:   Leetcode With Csharp serious tutorial
date:       2020-06-18
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

Problem could be found on Leetcode [Here](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

# Problem Description

Given a string, find the length of the longest substring without repeating characters.

Example 1:

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```
Example 2:
```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Example 3:
```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

# My Solution

## Code
```
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<object> notdup = new HashSet<object>();
        Queue anslist = new Queue();
        int maxlen = 0;
        for(int i = 0;i < s.Length;i++){
            if(notdup.Contains(s[i])){
                while(anslist.Count > 0 && notdup.Contains(s[i])){
                    var curele = anslist.Dequeue();
                    notdup.Remove(curele);
                }
            }
            notdup.Add(s[i]);
            anslist.Enqueue(s[i]);
            int curlen = anslist.Count;
            maxlen = curlen > maxlen ? curlen : maxlen;
        }
        return maxlen;
    }
}
```

## Explain

**Time Complexity: O(n)** - n is the length of string s

**Key Points: Set, Queue**

Maintain a Queue ```anslist``` with unduplicated numbers, and a hashset ```notdup``` to verify if the next char of string s inside the current queue in O(1) time. Time complexity for computer to find an element inside a list is O(m) - m is the current length of list, but only takes O(1) to find it in a set.

If the next char could be found in ```notdp``` , record the current length of queue and pop the left-most element from the queue until the char that is the same with the next char canceled from ```notdp```

![Fig 3-1: initial status](\img\csharp\leetcode3-1.png)