---
layout:     post
title:      Enable MPI in Visual Studio
subtitle:   High Performance Computing
date:       2020-07-21
author:     Yiling
header-img: img/hpc/MPI.png
catalog: true
tags:
    - C
    - HPC
    - MPI
---

# Download MPI for Windows(Microsoft MPI)

[https://www.microsoft.com/en-us/download/details.aspx?id=57467](https://www.microsoft.com/en-us/download/details.aspx?id=57467)

Run both .exe and .msi file, they will install Microsoft MPI under `C:\Program Files\Microsoft MPI` by default.(But if you have changed the register manually, the path might be changed)

# Configure MPI in Visual Studio 2019

Open `Project` -> `Project_name Properties` 

![](\img\hpc\mpi_setting1.png)



### Under `VC++ Directories`

Add `C:\Program Files (x86)\Microsoft SDKs\MPI\Include` in `Include Directories`

Add `C:\Program Files (x86)\Microsoft SDKs\MPI\Lib\x86` in `Library Directories`

![](\img\hpc\mpi_setting3.png)

### In `C/C++` -> `Preprocessor` -> `Preprocessor Definitions`

Add `MPICH_SKIP_MPICXX`

![](\img\hpc\mpi_setting2.png)

### In `C/C++` -> `Code Generation`

Change `Runtime Library` to MTd

![](\img\hpc\mpi_setting4.png)

### In `Linker` -> `Input` -> `Additional Dependencies`

Add `msmpi.lib` and `msmpifec.lib`

![](\img\hpc\mpi_setting5.png)

# Testing

```c
#include<stdio.h>
#include<mpi.h>
#include<stdlib.h>

int main(int argc, char* argv[])
{
	int myid, numprocs, namelen;
	char processor_name[MPI_MAX_PROCESSOR_NAME];

	MPI_Init(&argc, &argv);        // starts MPI
	MPI_Comm_rank(MPI_COMM_WORLD, &myid);  // get current process id
	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);      // get number of processeser
	MPI_Get_processor_name(processor_name, &namelen);

	if (myid == 0) printf("number of processes: %d\n...", numprocs);
	printf("%s: Hello world from process %d \n", processor_name, myid);

	MPI_Finalize();

	return 0;
}
```
Click `Build` -> `Build Solution`

And your terminal will looks like the following screenshot. Please make sure you can build .exe file successfully without error.

You can see the .exe file path inside the terminal, for me, it is `E:\TestingPrograms\omp_test\x64\Debug\omp_test.exe`
![](\img\hpc\mpi_setting6.png)

Open file explorer, `E:\TestingPrograms\omp_test\x64\Debug\` folder (Your path will be different!)

Do right-click while pressing `Shift` button

Enter `mpiexec -n 5 omp_test.exe` in powershell or command-line window(depend on your Windows version, for Win10 you will see powershell, but for early version you will see command-line)

You can replace `5` with number of process you want, `omp_test.exe` must be replaced by the name of your builded .exe file

The result will be:
![](\img\hpc\mpi_setting7.png)

Done!