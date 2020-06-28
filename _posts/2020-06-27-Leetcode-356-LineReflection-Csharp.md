---
layout:     post
title:      Leetcode 356. Line Reflection Csharp(C#) Solution
subtitle:   Leetcode With Csharp series tutorial
date:       2020-06-27
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

That is a problem that requires premium. You can find it [HERE](https://leetcode.com/problems/line-reflection/) if you are a paid menber.

# Problem Description

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points symmetrically, in other words, answer whether or not if there exists a line that after reflecting all points over the given line the set of the original points is the same that the reflected ones.

Note that there can be repeated points.

Follow up:
Could you do better than O(n2) ?

 

Example 1:
![](\img\csharp\356_example_1.PNG)
```
Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.
```


Example 2:
![](\img\csharp\356_example_2.PNG)
```
Input: points = [[1,1],[-1,-1]]
Output: false
```
Explanation: We can't choose a line.

**Constraints:**

n == points.length

1 <= n <= 10^4

-10^8 <= points[i][j] <= 10^8

Another Examples:

Example 3:
```
Input: [[1, 1], [1, 1], [1, 1]]
Output: true
```
Example 4:
```
Input: [[1, 1], [-1, 1], [-1, 1]]
Output: true
```


# My Solution

## Code
```c#

public class Solution {
    public bool IsReflected(int[][] points) {
        HashSet<(int, int)> ps = new HashSet<(int, int)>();
        float add_up = 0;
        foreach(int[] point in points){
            if(ps.Contains((point[0], point[1])) is false){
                add_up += point[0];
            }
            ps.Add((point[0], point[1]));
        }
        float added = (float)add_up;
        float mid = added/(ps.Count);
        foreach(int[] point in points){
            int ref_x = (int)(mid - (point[0] - mid));
            if(ps.Contains((ref_x, point[1])) is false) return false;
        }
        return true;
    }
}
```

## Explain
**Time Complexity: O(n)** - n is the length of points

The most important thing for us to do in this problem is to find the "middle line" of those points. From the problem description we know that this line is parallel to y-axis so the expression of this line is always `x = sth`(sth is a constant). The problem turned to "How to find a middle point which equal to sth", which is a 1-D problem.

The position of "middle point" of n points on a line is always equal to sum(x<sub>n1</sub>, x<sub>2</sub> ... x<sub>n</sub>)/n. But remember one point can be reflection of more than one points in ```points``` in this problem, just like Example 4.[1, 1] could be reflection of all two [-1, 1] so you have to use set to remove duplicates first.

After finding out the "middle point", for a point in ```points```, simply find out if its reflection is inside set(points) or not. If not, return `false` directly, else come to the next point until reaches to the end of `points`. 