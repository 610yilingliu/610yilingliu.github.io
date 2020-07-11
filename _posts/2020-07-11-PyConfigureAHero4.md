---
layout:     post
title:      First Python Project - Configure A Hero - Part D
subtitle:   Tutorial for newbies to programming
date:       2020-07-11
author:     Yiling
header-img: img/python/pylogo.png
catalog: true
tags:
    - Python
    - Beginner
    - ExampleProject
---

Related links for this tutorial could be found **[HERE](https://610yilingliu.github.io/2020/06/23/PyForBeginners/)**

# Import Data From a File

Now you are much lazier than before. You asks your friend to provide msgs in the form of:

```
1000, 0.2
1200, 0.1
500, 0.5
```

You copy and paste those data to a text file, planning to import it to the list to analyze. Assume the file name is `data.txt`, in the same folder with your `hero.py`, like this:
![](\img\python\path1.png)

You can use `f = open('data.txt', 'r')` to open this file as a file stream(It is not equal to a string, list or some thing, you can imagine it is a special, continuous byte sequence. You can find some explain on [Microsoft Documentation](https://docs.microsoft.com/en-us/windows/win32/fileio/file-streams)), if any error shown in your console, You can also use the absolute path like `E:/folder/code_example/data.txt` instead of the relative path 'data.txt'

**REMENBER: Use '/' instead of '\\' because '\\' is a default escape character in Python**

Then put those content in a list-of-list through `content = f.readlines()`. If you print content, the result will be:
![](\img\python\hero10.png)

'\\n' means `ENTER`

You already load the data into a list, but how to delete those annoying '\\n' and split string 'ATK, EDM'?

Let's use a for loop to travel through the list

The following content will be a bit of hard to understand.

```python
f = open("E:/GitStorage/610yilingliu.github.io/code_example/data.txt", 'r')
content = f.readlines()
f.close()
for line in content:
    # after this step, you got a string like '1000, 0.2'
    deleted_enter = line.strip('\n')
    # after this step, you will get ['1000', '0.2']
    list_inside_list = deleted_enter.split(',')
    # contert `1000` to 1000.0, '0.2' to 0.2, and call function HeroEquipChoose()
    HeroEquipChoose(float(list_inside_list[0]), float(list_inside_list[1]))
```

You can also use `int(list_inside_list[0], float(list_inside_list[1])` to convert the string into numbers, but you cannot use `int(list_inside_list[0], int(list_inside_list[1])` because numbers 0.2 is not an integer.

To explain in a picture:
![](\img\python\hero11.png)

Hero.py for you to test

```python
def HeroEquipChoose(ori_atk, ori_edm):
    use_eq_a = (ori_atk + 200) * (1 + ori_edm + 0.1)
    # print('DMG if use a ' + str(use_eq_a))

    use_eq_b = (ori_atk + 100) * (1 + ori_edm + 0.2)
    # print('DMG if use using b ' + str(use_eq_b))

    if use_eq_a > use_eq_b:
        print('choose a')
    elif use_eq_a < use_eq_b:
        print('choose b')
    else:
        print('two equipments are the same')


# replace with your local path!!!
f = open("E:/GitStorage/610yilingliu.github.io/code_example/data.txt", 'r')
content = f.readlines()
f.close()
for line in content:
    # after this step, you got a string like '1000, 0.2'
    deleted_enter = line.strip('\n')
    # after this step, you will get ['1000', '0.2']
    list_inside_list = deleted_enter.split(',')
    # contert `1000` to 1000.0, '0.2' to 0.2, and call function HeroEquipChoose()
    HeroEquipChoose(float(list_inside_list[0]), float(list_inside_list[1]))
```

That's all, thanks for reading my tutorial.