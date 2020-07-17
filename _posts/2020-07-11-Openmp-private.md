---
layout:     post
title:      OpenMP Private Variable - Understand Why you got error while using it
subtitle:   High Performance Computing
date:       2020-07-11
author:     Yiling
header-img: img/hpc/1.png
catalog: true
tags:
    - C
    - HPC
    - OpenMP
---

For beginners, the following code seems good.
```c
int main()
{
	omp_set_num_threads(4);
	int A = 100;
#pragma omp parallel for private(A)
	for (int i = 0; i < 10; i++)
	{
		int num = omp_get_thread_num();
		printf("Thread %i got %d\n", num, i + A);
	}

	return 0;
}
```

But there will be an error if you run it.
![](\img\hpc\err3.png)

What causes this error?

It is important to know that in OpenMP, **Private variables are undefined on entry** that means, this code is the same to 

```c
int main()
{
	omp_set_num_threads(4);
// remove A
#pragma omp parallel for private(A)
	for (int i = 0; i < 10; i++)
	{
		int num = omp_get_thread_num();
		printf("Thread %i got %d\n", num, i + A);
	}

	return 0;
}
```

Of course there will be an error!

The way to fix this problem is to define `A` inside and outside the loop.

```c
int main()
{
	// you have to declare A outside, too. Otherwise there will be an error with #pragma omp parallel for private(A)
	int A;
	omp_set_num_threads(4);
#pragma omp parallel for private(A)
	for (int i = 0; i < 10; i++)
	{
		int A = 100;
		int num = omp_get_thread_num();
		printf("Thread %i got %d\n", num, i + A);
	}

	return 0;
}
```

If you want to see what A is outside for loop, you need to initialize A with a number(I use 0 as example)

```c
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
Result:
![](\img\hpc\res1.png)

A will be the value we defined **before** for loop if we print it outside.