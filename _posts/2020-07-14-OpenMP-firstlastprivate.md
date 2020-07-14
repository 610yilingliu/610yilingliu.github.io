---
layout:     post
title:      OpenMP - First Private and Last Private
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
# Background
We already learned that variables in `private` is stateless in the previous post [OpenMP Private Variable - Understand Why you got error while using it](https://610yilingliu.github.io/2020/07/11/Openmp-private/)

Code we use in the last post:
```c
#include <stdio.h>
#include <omp.h>
int main()
{
	// you have to declare it outside, too. Otherwise there will be an error with #pragma omp parallel for private(A)
	int A = 0;
	omp_set_num_threads(4);
#pragma omp parallel for private(A)

	for (int i = 0; i < 10; i++)
	{
		int A = 100;
		int num = omp_get_thread_num();
		printf("Thread %i got %d\n", num, i + A);
	}
	printf("Here you will see previous A: %i\n", A);

	return 0;
}
```

But the problem comes:

If you do not want to redefine `A` in each loop, we want the code looks like(The following code will return with error message):
```c
int main()
{
	int A = 0;
	omp_set_num_threads(12);
#pragma omp parallel for private(A)
	for (int i = 0; i < 10; i++)
	{
		A += i;
		int num = omp_get_thread_num();
		printf("Thread %i got %d\n", num, A);
	}
	printf("At the end, A will be: %i\n", A);


```

and got a result like:
```
Thread 4 got 4
Thread 7 got 7
Thread 3 got 3
Thread 6 got 6
Thread 1 got 1
Thread 0 got 0
Thread 5 got 5
Thread 2 got 2
Thread 8 got 8
Thread 9 got 9
At the end, A will be: 9
```

What should we do?

**Notice: I am using a 6-core cpu, if your computer don't have that much core, please use omp_set_num_threads(core_number * 2) instead of omp_set_num_threads(12)**

# First Private

Let's try not to initialize A inside the loop

we can use `firstprivate` to replace `private`, so your code become:

```c
int main()
{
int main()
{
	int A = 0;
	omp_set_num_threads(12);
#pragma omp parallel for firstprivate(A)
	for (int i = 0; i < 10; i++)
	{
		A += i;
		int num = omp_get_thread_num();
		printf("Thread %i got %d\n", num, A);
	}
	printf("At the end, A will be: %i\n", A);
	return 0;
}
```

Now you can run these code without error message, and get the following result
```
Thread 0 got 0
Thread 0 got 1
Thread 0 got 2
Thread 1 got 3
Thread 1 got 4
Thread 1 got 5
Thread 3 got 8
Thread 3 got 9
Thread 2 got 6
Thread 2 got 7
At the end, A will be: 0
```
Oh what the fuck! Why A become `0` at the end we need 9?

It is because that A is still stateless after exit the `for` loop, you need something to let global `A` inherit the final `A` value in the loop.

# Lastprivate

`lastprivate` enable global `A` to inherit the final `A` in for loop

Simply add a `lastprivate(A)`, the code become:
```c
int main()
{
	int A = 0;
	omp_set_num_threads(12);
#pragma omp parallel for firstprivate(A) lastprivate(A)
	for (int i = 0; i < 10; i++)
	{
		A += i;
		int num = omp_get_thread_num();
		printf("Thread %i got %d\n", num, A);
	}
	printf("At the end, A will be: %i\n", A);
	return 0;
}

```

You cannot remove `firstprivate(A)` here because we still have to use the global `A` we defined before entering `for` loop

Result:

```
Thread 4 got 4
Thread 7 got 7
Thread 3 got 3
Thread 6 got 6
Thread 1 got 1
Thread 0 got 0
Thread 5 got 5
Thread 2 got 2
Thread 8 got 8
Thread 9 got 9
At the end, A will be: 9
```