---
layout:     post
title:      First Python Project - Configure A Hero - Part B
subtitle:   Tutorial for newbies to programming
date:       2020-06-25
author:     Yiling
header-img: img/python/pylogo.png
catalog: true
tags:
    - Python
    - Beginner
    - ExampleProject
---
Related links for this tutorial could be found **[HERE](https://610yilingliu.github.io/2020/06/23/PyForBeginners/)**

# Make Your Calculator Works Like a Program

Now you already get the result for your own character, but you friend says: "Hey, brother. My team want to explore the new dungeon this week and we have 25 characters. Would you please help us decide the equipment for each team member to wear? 

You tried to rewrite the function 25 times in Part A but drove crazy when the third time you type the same thing again.

'God! I need a function to help me treat with those data in batch!' You cried out.

Well, that is why people use function in programs. In python, a function is represented as ```def function_name(variable1, variable2...)```

**variables** are the things that waits you to input yourself. It could be empty, like this:
```python
def printhelloworld():
    print('hello World')
```

If you execute `printhelloworld()` the function will print 'hello World' on the screen.

The function with input variables looks like this:
```python
def printhellosb(name):
    print('hello ' + name)
```
The function will print 'hello John' if you execute `printhellosb('John')` and 'hello Allen' for `printhellosb('Allen')`.

There will be an error if executing `printhellosb(John)`, because now John is an unknown variable, instead of a string. The thing you input should be a known variable. In case `printhellosb(John)`, computer confused about 'Who is John' unless you tell it John = 'John'. The following command will run successfully:
```python
John = 'John'
printhellosb(John)
```

Ofcourse you can write a function which receives multiple variables:

```python
def printhelloguys(name1, name2):
    print('hello' + name1 + ' and ' + name2)
```
`printhelloguys('John', 'Allen')` shows 'hello John and Allen' on your screen.

Now back to our calculator.

The code we got from the last tutorial is:
```python
use_eq_a = (800 + 200) * (1 + 0.05 + 0.1)
print('DMG if use a ' + str(use_eq_a))

use_eq_b = (800 + 100) * (1 + 0.05 + 0.2)
print('DMG if use using b ' + str(use_eq_b))

if use_eq_a > use_eq_b:
    print('choose a')
elif use_eq_a < use_eq_b:
    print('choose b')
else:
    print('two equipments are the same')
```
Now try to pack everything up into a function, analyze the previous code

![Previous Code](\img\python\hero5.png)

From the given condition in Part A which says:

Assume your hero already have:
```
Atk: 800
EDM: 5%
```
And the code we written, We can conclude that:

1. `800` in the red box represents the origional attack(before wearing equipments) of your character
2. `0.05` in the blue box represents the origional Extra Damage Multiplier

So your function could be
```python
def HeroEquipChoose(ori_atk, ori_edm):
    logics...
```python
`HeroEquipChoose`, `ori_atk`, `ori_edm` could be any name you want, it just works like a sign. You can also set your function as:
```python
def doggy(a, b):
    logics...
```
If it not confuse you and others who will read your code.

Simply replace `800` and `0.05` by variable names you want, and that is the function:
```python
def HeroEquipChoose(ori_atk, ori_edm):
    use_eq_a = (ori_atk + 200) * (1 + ori_edm + 0.1)
    print('DMG if use a ' + str(use_eq_a))

    use_eq_b = (ori_atk + 100) * (1 + ori_edm + 0.2)
    print('DMG if use using b ' + str(use_eq_b))

    if use_eq_a > use_eq_b:
        print('choose a')
    elif use_eq_a < use_eq_b:
        print('choose b')
    else:
        print('two equipments are the same')
```

You may get confused about how to use it. In VSCode, simply use
```python
if __name__ == '__main__':
    functionname(input1, input2...)
```
and methods we mentioned in Part A to run
or you can even get rid of `if __name__ == '__main__':` , use `functionname(input1, input2...)` straightly, just like this:

![How to execute a function](\img\python\hero6.png)

Now you can do the analyze in a more easier way, the following picture shows the result of anayzing 4 characters in your friend's team.

![Treat data in function](\img\python\hero7.png)

You can get rid of lines that you don't want by adding `#` ahead of the line, and that line will not execute while running.

![If we don't want extra output](\img\python\hero8.png)

The line `print('DMG if use a ' + str(use_eq_a))` and line `print('DMG if use using b ' + str(use_eq_b))` will not run, your terminal just print the clean result without extra messages.

Now you almost finished 2/3 work of batch-data processing, in the next tutorial, you will learn how to put data in a list and print it one-by-one or export them to a file.