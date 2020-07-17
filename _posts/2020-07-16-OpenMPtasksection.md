---
layout:     post
title:      OpenMP - Task and Sections
subtitle:   High Performance Computing
date:       2020-07-17
author:     Yiling
header-img: img/hpc/1.png
catalog: true
tags:
    - C
    - HPC
    - OpenMP
---
# Sections

`omp sections` is quite similar with `omp for` but much flexible for small number of tasks without iteration relation.

It could be seen as a special kind of `omp for`.

Example:
```c
#include <stdio.h>
#include <omp.h>
void t1() {
	printf("Task 1 is on thread %d \n", omp_get_thread_num());
}
void t2() {
	printf("Task 2 is on thread %d \n", omp_get_thread_num());
}
void t3() {
	printf("Task 3 is on thread %d \n", omp_get_thread_num());
}

int main()
{
#pragma omp parallel sections
	{
#pragma omp section
		{
			t1();
		}
#pragma omp section
		{
			t2();
		}
#pragma omp section
		{
			t3();
		}
	}
	return 0;
}
```

Result:
```
Task 2 is on thread 1
Task 1 is on thread 3
Task 3 is on thread 6
```

If we use `#pragma omp sections` instead of `#pragma omp parallel sections` tasks will run on the same thread in order

```
Task 1 is on thread 0
Task 2 is on thread 0
Task 3 is on thread 0
```

# Task

Task is a new feature after OpenMP 3.0
It works like `sections` but much efficient, you can see the explain about difference between `task` and `sections` on [StackOverflow](https://stackoverflow.com/questions/13788638/difference-between-section-and-task-openmp)

For fibonacci sequence

if we use `section`

```c
int fib(int n)
{
	int i, j;
	if (n < 2)
		return n;
	else
	{
#pragma omp parallel sections
		{
#pragma omp section
			{
				i = fib(n - 1);
			}
#pragma omp section
			{
				j = fib(n - 2);
			}
		}
		printf("Current int %d is on thread %d \n", i + j, omp_get_thread_num());
		return i + j;
	}
}

int main()
{
	int n = 10;

#pragma omp parallel shared(n)
	{
#pragma omp single
		{
			printf("%d\n", omp_get_num_threads());
			printf("fib(%d) = %d\n", n, fib(n));
		}
	}
}
```

if we use `task` (**Notice: The following code is NOT available on Visual Studio, you can use command `gcc -fopenmp -o test Source.c` to compile and `./test.exe` to run it**)

```c
#include <stdio.h>
#include <omp.h>
int fib(int n)
{
  int i, j;
  if (n<2)
    return n;
  else
    {
       #pragma omp task shared(i) firstprivate(n)
       i=fib(n-1);

       #pragma omp task shared(j) firstprivate(n)
       j=fib(n-2);

       #pragma omp taskwait
	printf("Current int %d is on thread %d \n", i + j, omp_get_thread_num());
       return i+j;
    }
}

int main()
{
  int n = 10;

  #pragma omp parallel shared(n)
  {
    #pragma omp single
    {
	    printf("%d\n", omp_get_num_threads());
    	printf ("fib(%d) = %d\n", n, fib(n));
    }
  }
}
```

For `section` one, what you will see on console is:
```
12
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 8 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 13 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 8 is on thread 0
Current int 21 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 8 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 13 is on thread 0
Current int 34 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 8 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 13 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 5 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 1 is on thread 0
Current int 3 is on thread 0
Current int 8 is on thread 0
Current int 21 is on thread 0
Current int 55 is on thread 4
fib(10) = 55
```

For `task` one, the result is:
```
12
Current int 1 is on thread 3
Current int 2 is on thread 3
Current int 1 is on thread 8
Current int 2 is on thread 8
Current int 1 is on thread 8
Current int 1 is on thread 4
Current int 1 is on thread 11
Current int 1 is on thread 11
Current int 2 is on thread 11
Current int 3 is on thread 11
Current int 1 is on thread 11
Current int 2 is on thread 11
Current int 1 is on thread 11
Current int 1 is on thread 11
Current int 2 is on thread 11
Current int 3 is on thread 11
Current int 1 is on thread 11
Current int 2 is on thread 11
Current int 1 is on thread 11
Current int 1 is on thread 11
Current int 2 is on thread 11
Current int 3 is on thread 11
Current int 5 is on thread 11
Current int 8 is on thread 11
Current int 1 is on thread 8
Current int 2 is on thread 8
Current int 3 is on thread 8
Current int 5 is on thread 8
Current int 13 is on thread 8
Current int 1 is on thread 7
Current int 2 is on thread 7
Current int 1 is on thread 7
Current int 1 is on thread 7
Current int 1 is on thread 0
Current int 1 is on thread 0
Current int 2 is on thread 0
Current int 3 is on thread 0
Current int 1 is on thread 1
Current int 1 is on thread 6
Current int 2 is on thread 6
Current int 1 is on thread 9
Current int 2 is on thread 9
Current int 1 is on thread 2
Current int 2 is on thread 7
Current int 3 is on thread 7
Current int 5 is on thread 7
Current int 2 is on thread 5
Current int 5 is on thread 5
Current int 1 is on thread 5
Current int 2 is on thread 5
Current int 1 is on thread 5
Current int 1 is on thread 5
Current int 2 is on thread 5
Current int 3 is on thread 5
Current int 1 is on thread 5
Current int 2 is on thread 5
Current int 1 is on thread 5
Current int 1 is on thread 5
Current int 2 is on thread 5
Current int 3 is on thread 5
Current int 5 is on thread 5
Current int 1 is on thread 5
Current int 2 is on thread 5
Current int 1 is on thread 11
Current int 2 is on thread 11
Current int 1 is on thread 8
Current int 2 is on thread 8
Current int 5 is on thread 8
Current int 3 is on thread 1
Current int 8 is on thread 1
Current int 21 is on thread 1
Current int 1 is on thread 10
Current int 3 is on thread 10
Current int 8 is on thread 0
Current int 1 is on thread 4
Current int 3 is on thread 4
Current int 1 is on thread 9
Current int 3 is on thread 9
Current int 8 is on thread 9
Current int 3 is on thread 2
Current int 5 is on thread 3
Current int 13 is on thread 3
Current int 5 is on thread 6
Current int 13 is on thread 7
Current int 8 is on thread 10
Current int 21 is on thread 10
Current int 34 is on thread 3
Current int 55 is on thread 1
fib(10) = 55
```

You can see that most of the iters in `sections` run on thread 0 while iters in `task` distribute evenly among threads. That means `tasks` is much "wiser" than `sections` in computing-resource allocation.


# Reference

[OpenMP Tutorials - Task](https://computing.llnl.gov/tutorials/openMP/#Task)

[OpenMP Tutorials - Sections](https://computing.llnl.gov/tutorials/openMP/#SECTIONS)

[OpenMP3.0的新特性Task指令基础](https://blog.csdn.net/gengshenghong/article/details/7004594) (Not exact enough, just for reference)

[Difference between section and task openmp](https://stackoverflow.com/questions/13788638/difference-between-section-and-task-openmp)






