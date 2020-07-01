---
layout:     post
title:      Debug C project with OpenMP in VScode
subtitle:   What I found while learing HPC
date:       2020-06-17
author:     Yiling
header-img: img/hpc/1.png
catalog: true
tags:
    - C
    - VScode
    - HPC
---

# Problem We Have

While using VScode to debug code with openMP, there will be errors if you use gcc filename.c directly.

```c
#include<stdio.h>
#include <omp.h>
int main()
{
    #pragma omp parallel
    {
        printf("The parallel region is executed by thread%d\n",omp_get_thread_num());
    }
}
```
Assume the fileneame of the code above is `test.c`

If you type `gcc test.c` in terminal and there will be an error like this:
![](\img\hpc\err1.png)

And if you press **F5** in VScode, similar error will happend:

![](\img\hpc\err2.png)

This problem troubled me for a few minutes, editing launch.json seems not helpful.

# Solution

Remember if we want to compile C code with OpenMP successfully in the command line, you have to input

```shell
gcc -fopenmp -o exe_name_withoutexe cfilename.c
```
But how to apply this command while debugging in VScode?

First, press `Ctrl + Shift + P` and type "tasks"

You will see some options like this:

![](\img\hpc\tasks.png)

Select `Configure Default Test Task`

Then click `gcc.exe: build active file`

![](\img\hpc\gcc.png)

VScode will create a default tasks.json automatically.
![](\img\hpc\tasksjson.png)

You need to change the contenets in the red box.

Replace them by
```json
"-fopenmp",
"-o",
"${fileDirname}\\${fileBasenameNoExtension}.exe",
"${file}"
```
After that your tasks.json will looks like this:

![](\img\hpc\tasks2.png)

Save it and return to test.c, press F5, it works!

![](\img\hpc\output.png)

