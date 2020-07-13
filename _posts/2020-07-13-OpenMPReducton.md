---
layout:     post
title:      Reduction in OpenMP
subtitle:   What I found while learning HPC
date:       2020-07-13
author:     Yiling
header-img: img/hpc/1.png
catalog: true
tags:
    - C
    - HPC
    - OpenMP
---

# About Reduction

`reduction` is a key in OpenMP to apply multi-thread technique automatically during cumulative operation.

It assign private variables to each thread with a initial value, do the operation and accumulate them. The accepted operations and the initial values are listed as follow:

operator| Private var initial value
---- | ----
 + | 0
 - | 0
 * | 1
 & |~0
 \|| 0
 ^ | 0
 && | 1(True)
 \|\| | 0(False)

Operators `max` and `min` are also accepted. `max` returns the largest representable number in the reduction list item type while `min` returns the least representable number in the reduction list item type.

# Example

```c
#include <stdio.h>
#include <omp.h>

int main() {
	omp_set_num_threads(4);
	int sum = 0;
#pragma omp parallel for reduction(+:sum)

	for (int i = 0; i < 10; i++) {
		sum += i;
		int num = omp_get_thread_num();
		printf("Current Sum: %d, Current i: %d, Current Thread: %d\n", sum, i, num);
	}
	printf("\nSum is : %d\n",sum);
}
```

How i in [0, 10) assigned to each thread:
![](\img\hpc\reduction_2.png)
Result:
![](\img\hpc\reduction_res1.png)