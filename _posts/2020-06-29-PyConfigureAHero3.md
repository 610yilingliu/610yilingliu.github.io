---
layout:     post
title:      First Python Project - Configure A Hero - Part C
subtitle:   Tutorial for newbies to programming
date:       2020-06-29
author:     Yiling
header-img: img/python/pylogo.png
catalog: true
tags:
    - Python
    - Beginner
    - ExampleProject
---
Related links for this tutorial could be found **[HERE](https://610yilingliu.github.io/2020/06/23/PyForBeginners/)**

# Use Data inside a List 

Now you already got a Python function in the previous tutorial
```python
def HeroEquipChoose(ori_atk, ori_edm):
    use_eq_a = (ori_atk + 200) * (1 + ori_edm + 0.1)
    use_eq_b = (ori_atk + 100) * (1 + ori_edm + 0.2)
    if use_eq_a > use_eq_b:
        print('choose a')
    elif use_eq_a < use_eq_b:
        print('choose b')
    else:
        print('two equipments are the same')
```
but you still have to type `HeroEquipChoose(input1, input2)` for 25 times to finish analyzing process.

Is there anyway that allows you to type `HeroEquipChoose(input1, input2)` just once and tell the result?

There is a data structure called `List`

You can find the academic concepts of `List` on wiki but today I just want to tell you how it works in this project in an interesting way.

Imagine you need to tell a truck to move n containers from the current city to city A. If you put the containers everywhere without a specific location, you need to point to the container to the bus driver and tell him:

"Hey David, would you please move this container to city A?"

"Hey David, would you please move that container to city A?"

...... for n times.

But it you put all the containers on a square then you just need to tell him:

"Hey David, would you please move those containers on the square to city A?"

In this project, a `List` plays the role of the square. You put things inside it, tell function to call the elements inside the list, and wait for result.

In python, a list could be defined as:
```python
ls = [element1, element2, element3....]
```

elements could be different objects, it could be a single element like `int`, `string`, `float` or even data structures like `list`, `tuple`.....

In this example, if you have 3 heros

Hero1
```
ori_atk = 1000
ori_edn = 0.2
```
Hero2
```
ori_atk = 1200
ori_edn = 0.1
```
Hero3
```
ori_atk = 500
ori_edn = 0.5
```

You can defind the input list as
```
heroes = [[1000, 0.2], [1200, 0.1], [500, 0.5]]
```
You can also use `Tuple` as the element inside heroes like `heroes = [(1000, 0.2), (1200, 0.1), (500, 0.5)]` but this is a long story to talk although it ise much efficient than put lists inside `heroes`, and I will not teach you about this in the tutorial face to newbies.

`heroes` is a list of list, which means every element in heroes is a list.

`heroes[0] == [1000, 0.2]`, the first element in this list represents the attack of hero1, and the second element reperesnts the extra damage multiplier. `heroes[1] = [1200, 0.1]` and `heroes[2] = [500, 0.5]` working on similar way, which represent the data of hero2 and hero3 (Notice the number inside computer start from 0, instead of 1 in real life)

There are two ways to go through list `heroes`

Method 1:
Go through every element in `heroes` straightly
```python
for hero in heroes:
    HeroEquipChoose(hero[0], hero[1])
```

Method 2:
Gothrough elements in `heroes` by its index
```python
for index in range(len(heroes)):
    # heroes[0] == [1000, 0.2], heroes[1] == [1200, 0.1]...
    HeroEquipChoose(heroes[index][0], heroes[index][1])
```
variable `index` could be replaced by anything you want, programmers always use `i` for convenience.

![Running Result](\img\python\hero9.png)