---
layout:     post
title:      Leetcode 2. Add Two Numbers Csharp(C#) Solution
subtitle:   Leetcode With Csharp serious tutorial
date:       2020-06-17
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - Leetcode
    - C#
---

Problem could be found on Leetcode [Here](https://leetcode.com/problems/add-two-numbers/)

# Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

# My Solution

## Code

```
public class Solution
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2){
            ListNode head = new ListNode();
            var pointer = head;
            int curval = 0;
            while(l1 != null || l2 != null){
                curval = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) + curval;
                pointer.next = new ListNode(curval % 10);
                pointer = pointer.next;
                // overflow decimal, like 12, we keep 1 for the next loop
                curval = curval / 10;
                // if next l1/l2 is not null, go to the next node
                l1 = l1?.next;
                l2 = l2?.next;
            }
            // if there is overflow left, add a node
            if(curval != 0){
                pointer.next = new ListNode(curval);
            }
            return head.next;
        }
    }
```

## Explain

**Time Complexity: O(m + n)** - m, n are the length of two listnodes

This problem itself is super easy if you know how listnodes work, but take care of two special cases:

**Case 1 Example**
```
// 21
l1 = (1 -> 2)
// 54321
l2 = (1 -> 2 -> 3 -> 4 -> 5)
```
If l1 reaches to the end and there are still nodes inside l2, you must assume the rest nodes of l1 is 1.

So l1 and l2 will become:
```
// 00021
l1 = (1 -> 2)
// 54321
l2 = (1 -> 2 -> 3 -> 4 -> 5)
```
Then you can solve it in the normal way

**Case 2 Example**
```
// 789
l1 = (9 -> 8 -> 7)
// 698
l2 = (8 -> 9 -> 6)
```
789 + 698 = 1487

Loop1: 9 + 8 = 17, keep 7, move 1 to the next loop

Loop2: 8 + 9 = 17, add the 1 from the previous loop, so the current digit will be 18; keep 8, move 1 to the next loop

Loop3: 7 + 6 = 13, add the 1 from the previous loop, so the current digit weill be 14, move 1 to the next digit

Now there are no rest nodes in both l1 and l2, you need to set this 1 as next node.

If you don't know how listnode works, here is a short explain:

Define a listnode a:

```a``` point to listnode ```b```, and ```b``` point to listnode ```c```

So it will be defined as (a -> b -> c)

What if you need to change the value of node c? Assume the the value of c was 'c' and you want to change it to 'cc'.

Instead of modify in ```a``` straightly, you need a pointer, just set it as variable ```p```

So the code will looks like this(This code cannot run in the following code in a real C# environment! It just shows how I think):

```
function modifyc(listnode h, target_val_to_edit){
    head = h;
    pointer = h;
    while(pointer.val == target_val_to_edit and pointer.next != null){
        pointer = pointer.next
    }
    if(pointer.val == target_val_to_edit){
        pointer.val = 'cc'
        return head
    }
    return head
}

run function(a, 'c')
```
```head``` points to ```a``` while ```pointer``` is moving from ```a``` to ```c```.
You need to modify the node that the pointer points to, instead of ```a``` itself.
