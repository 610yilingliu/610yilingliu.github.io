---
layout:     post
title:      Frequently Used C Built-in Functions in File Processing
subtitle:   C basic
date:       2020-07-10
author:     Yiling
header-img: img/hpc/ccode.png
catalog: true
tags:
    - C
    - Documentation
---
# Methods

## fopen
```c
FILE *fopen(const char *filepath, const char *mode)
```
*filepath should be a relative path or path of target file.

Mode include:

Mode|Description
  ----  | ----  
"r"|Opens a file for reading. The file must exist.
"w"|Creates an empty file for writing. If a file with the same name already exists, its content is erased and the file is considered as a new empty file.
"a"|Appends to a file. Writing operations, append data at the end of the file. The file is created if it does not exist.
"r+"|Opens a file to update both reading and writing. The file must exist.
"w+"|Creates an empty file for both reading and writing.
"a+"|Opens a file for reading and appending.

Example:
```c
FILE * fp;
fp = fopen ("file.txt", "r");
```

## fgets

```
char *fgets(char *str, int n, FILE *stream)
```

`str` points to an array where we will store the content we read

`n` is the maximum length to store the content, n <= length(str)

`stream` is the object returned from `fopen`

Notice: it wil stop while meats '\n'

Example:
```c
char str[60];
// fp is the content returned from fopen
if( fgets (str, 60, fp)!=NULL ) {
    /* writing content to stdout */
    puts(str);
}
```
## fscanf

```c
int fscanf(FILE *stream, const char *format, ...)
```

Similar with `fgets` but stops if meets any `\s`

`stream` is the object returned from `fopen`

`format` is the C string that contains one or more of the following items − Whitespace character, Non-whitespace character and Format specifiers. A format specifier will be as [=%[*][width][modifiers]type=], which is explained below

Sr.No.|Argument|Description
 ---- | ----  | ----  
 1 | * | This is an optional starting asterisk indicates that the data is to be read from the stream but ignored, i.e. it is not stored in the corresponding argument.
2 | width | This specifies the maximum number of characters to be read in the current reading operation.
3 | modifiers| Specifies a size different from int (in the case of d, i and n), unsigned int (in the case of o, u and x) or float (in the case of e, f and g) for the data pointed by the corresponding additional argument: h : short int (for d, i and n), or unsigned short int (for o, u and x) l : long int (for d, i and n), or unsigned long int (for o, u and x), or double (for e, f and g) L : long double (for e, f and g)
4 | type| A character specifying the type of data to be read and how it is expected to be read. See next table.

type specifiers
type | Qualifying Input | Type of argument
----  | ----  | ----  
c | Single character: Reads the next character. If a width different from 1 is specified, the function reads width characters and stores them in the successive locations of the array passed as argument. No null character is appended at the end. | char *
d | Decimal integer: Number optionally preceded with a + or - sign | int *
e, E, f, g, G | Floating point: Decimal number containing a decimal point, optionally preceded by a + or - sign and optionally followed by the e or E character and a decimal number. Two examples of valid entries are -732.103 and 7.12e4 | float *
o | Octal Integer |int *
s | String of characters. This will read subsequent characters until a whitespace is found (whitespace characters are considered to be blank, newline and tab). | char *
u | Unsigned decimal integer. | unsigned int *
x, X | Hexadecimal Integer | int *

Additional arguments Depending on the format string, the function may expect a sequence of additional arguments, each containing one value to be inserted instead of each %-tag specified in the format parameter (if any). There should be the same number of these arguments as the number of %-tags that expect a value.

Example:
```c
int main () {
   char str1[10], str2[10], str3[10];
   int year;
   FILE * fp;

   fp = fopen ("file.txt", "w+");
   fputs("We are in 2012", fp);
   
   rewind(fp);
   fscanf(fp, "%s %s %s %d", str1, str2, str3, &year);
   
   printf("Read String1 |%s|\n", str1 );
   printf("Read String2 |%s|\n", str2 );
   printf("Read String3 |%s|\n", str3 );
   printf("Read Integer |%d|\n", year );

   fclose(fp);
   
   return(0);
}
```
Console will show:
```
Read String1 |We|
Read String2 |are|
Read String3 |in|
Read Integer |2012|
```

## strcmp

```c
int strcmp(const char *str1, const char *str2)
```

This function return values that are as follows

if Return value < 0 then it indicates str1 is less than str2.

if Return value > 0 then it indicates str2 is less than str1.

if Return value = 0 then it indicates str1 is equal to str2.


So if `str1 == str2`, it will return `0`

# Reference

[Tutorials Point](https://www.tutorialspoint.com/c_standard_library/)