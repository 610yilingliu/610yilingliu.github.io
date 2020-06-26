---
layout:     post
title:      First Python Project - Configure A Hero - Part A
subtitle:   Tutorial for newbies to programming
date:       2020-06-24
author:     Yiling
header-img: img/python/pylogo.png
catalog: true
tags:
    - Python
    - Beginner
    - ExampleProject
---

Start from printing "Hellow World" is quite boring, it appears in almost every tutorial. Let's do an interesting mini-project together. If you are a hard-core game player, it might be helpful for you while you are playing games.

# Question

You are a game player controlling a hero to fight against monsters. According to the formulas in the game you playing, there are two variables that decide the damage you will made while fighting against monsters:

```
Damage = Attack * (100% + ExtraDamageMultiplier)
```

For example, if your attack is 1000, and yor EDM is 20%, the final damage you will made is ```1000 * (100% + 20%) = 1200```

Now we have two equipments but you can only pick one.

Eqip a:
```
Atk + 200
EDM + 10%
```

Eqip b:
```
Atk + 100
EDM + 20%
```

Your hero already have Atk and EDM, that means Atk and EDM may not start from 0.

# Start From a Known Hero

Assume your hero already have:
```
Atk: 800
EDM: 5%
```

Python code to calculate the final DMG after equipping these two equipments is shown below:
```
use_eq_a = (800 + 200) * (1 + 0.05 + 0.1)
print('DMG after using a ' + str(use_eq_a))

use_eq_b = (800 + 100) * (1 + 0.05 + 0.2)
print('DMG after using b ' + str(use_eq_b))
```

## Part 1. Learn to Calculate Damage After Wearing Equipments

The formula itself it exactly the same as what you need to type on a calculator.

You pass two results of using equp a and eqip b to two variables `use_eq_a` and `use_eq_b` and print them.

Things inside `print()` is what you want to see, python cannot put `string` - the description of the output(here is `'DMG after using a/b'`) and `float` - the calculating result together, so you need to convert float into string via `str()`. Things inside `''` or `""` defines a string directly, and `+` merges two string together.

Copy these code to your IDE and run it, there are multiple ways to run it in the VSCode

Put these code in a file called ```hero.py```, select the lines you want to run and right-click, you will see a menu like this:

![VSCode way 1 & 2](\img\python\hero1.png)

If you click the red part, vscode will pop out a terminal, and show the following message after running:

![Terminal after clicking the red part](\img\python\hero2.png)

If you can see the blue part(Some body may not have it, it requires jupyter notebook, an external python plug-in and library), after clicking it, you will see:

![Interactive Window](\img\python\hero3.png)

The Third way need a VSCode plug in called Coderunner, you can install it in extension store by the steps shown on the following picture:

![Install Coderunner](\img\python\hero4.png)

Than at the upper-right corner of your workspace, you can see a triangular buttom, click it to run the current file/selection

There is a strange output `1150.0000000000002`, it is not an error, it caused by binary floating point in both C and Python(Python based on C), you can find the explaination [HERE](https://www.geeksforgeeks.org/floating-point-error-in-python/). But it doesn't matter for the following comparison.


## Part 2. Compare Two Results

Continue with the code above, now you already have 2 results and need to compare them, wear the equipment that allows you to kill monsters in the shortest time.

Add the if...elif...else after the code provided above

```
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

elif means else if(infact, many other languages use else if, but python use elif). The logit is exactly the same to the plain English. But, be careful with those spaces, I suggest you to use tab instead of pressing space multiple time for indent. Sentences on the same logic level need to have the same indent in python.

If you do
```
if sth:
    execute thing 1
else:
     execute thing 2
```
Python will throw out an error because I presses one more space before execute thing 2

After executing the code provided, what you will see in terminal will be like:

```
DMG if use a 1150.0000000000002
DMG if use using b 1125.0
choose a
```