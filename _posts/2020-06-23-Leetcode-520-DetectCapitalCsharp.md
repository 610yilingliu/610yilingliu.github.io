---
layout:     post
title:      Leetcode 520. Detect Capital Csharp(C#) Solution
subtitle:   Leetcode With Csharp series tutorial
date:       2020-06-23
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

Problem could be found on Leetcode [Here](https://leetcode.com/problems/detect-capital/)

# Problem Description

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".

All letters in this word are not capitals, like "leetcode".

Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:
```
Input: "USA"
Output: True
```

Example 2:
```
Input: "FlaG"
Output: False
```

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

# My Solution

## Code

```
public class Solution {
    public bool DetectCapitalUse(string word) {
        if(word == null) return false;
        int ucount = 0;
        bool l = false;
        for(int i = 0; i < word.Length; i ++){
            if(i > 0 && l){
                if(Char.IsUpper(word[i])) return false;
            }
            if(ucount > 1 && Char.IsLower(word[i])) return false;
            if(Char.IsUpper(word[i])){
                ucount ++;
            }
            else{
                l = true;
            }
        }
        return true;
    }
}
```

## Explain

**Time Complexity: O(n)** - n is the length of the string.

All cases for us to pause the loop and return false could be inffered from the problem

1. Any lowercases followed by uppercase (case: aA)

2. If there are more than one uppercase letter inside the string, no lowercase should be found in the rest of the string


So I set a bool ```l``` to detect if there already existed lowercase letter in the string and a int ```ucount``` to count the number of uppercase letter in the string.


## Failure Case Study

```word = aBBBB```

loop 1:

l = true, ncount = 0; Go to the next loop

loop 2:

l = true, B is an uppercase letter, matches failure case 1, return false

```word = BBaa```

loop 1:

l = false, ncount = 1; Go to the next loop

loop 2:

l = false, ncount = 2; Go to the next loop

loop 3:

ncount = 2; a is a lowercase letter, matches failure case 2, return false