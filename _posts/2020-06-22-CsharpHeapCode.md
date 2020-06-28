---
layout:     post
title:      Inplement Priority Queue(heap) in C#
subtitle:   Data structure
date:       2020-06-22
author:     Yiling
header-img: img/csharp/csharpintro.png
catalog: true
tags:
    - DataStructure
    - C#
    - CodeStorage
---

I will continue update this code during study C#, now it may looks not elegant enough.

Please tell me if anyone needs a Python3 version, I am good at Python.

```c#
public class heapq{
    List<int> h = new List<int>();
    public int lastidx = -1;
    public void heappush(int num){
        h.Add(num);
        lastidx ++;
        int parent = lastidx / 2;
        int curidx = lastidx;
        while(num > h[parent]){
        // switch if parent is smaller
            h[curidx] = h[parent];
            h[parent] = num;
            curidx = parent;
            parent = parent / 2;
        }
    }
    public int heappop(){
        int to_return = h[0];
        h[0] = h[lastidx];
        // O(1) according to MSDN https://docs.microsoft.com/en-us/dotnet/api/system.collections.generic.list-1.removeat?view=netcore-3.1
        h.RemoveAt(lastidx);
        lastidx --;
        if(lastidx < 1){
            return to_return;
        }
        if(lastidx == 1){
            h.Sort((x, y) => -x.CompareTo(y));
            return to_return;
        }
        // if len(list) > 2
        shift_down(0);
        return to_return;
    }
    public void shift_down(int parent){
        int left_child = 2 * parent + 1;
        int right_child = 2 * parent + 2;
        int curlargest = h[parent];
        if(right_child <= lastidx){
            if(h[left_child] > curlargest && h[left_child] > h[right_child]){
                h[parent] = h[left_child];
                h[left_child] = curlargest;
                shift_down(left_child);
            }
            else if(h[right_child] > curlargest && h[right_child] >= h[left_child]){
                h[parent] = h[right_child];
                h[right_child] = curlargest;
                shift_down(right_child);
            }
        }
        else if(left_child == lastidx){
            if(h[left_child] > curlargest){
                h[parent] = h[left_child];
                h[left_child] = curlargest;
            }
        }
    }
}
```