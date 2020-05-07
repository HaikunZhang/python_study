#!/usr/bin/env python
# -*- coding:utf-8 -*-

##################################################################
# 练习6. 定义计算N的阶乘的函数
# 要求：
# 1. 使用循环计算阶乘
# 2. 使用递归计算阶乘
# 3. 调用reduce 函数计算阶乘
##################################################################

import functools

# 1. 使用循环计算阶乘:


def fact1(n1):
    sum_fact = 1
    if n1 < 1:
        print("N不能小于1")
        return
    for x in range(1, n1 + 1):
        sum_fact *= x
    return sum_fact

# 2.使用递归计算阶乘：


def fact2(n2):
    if n2 < 1:
        print("n不能小于1")
        return
    elif n2 == 1:
        return 1
    else:
        return n2 * fact2(n2 - 1)

# 3. 调用reduce 函数计算阶乘


def fact3(n3):
    if n3 < 1:
        print("n不能小于1")
        return
    else:
        return functools.reduce(lambda x, y: x * y, range(1, n3+1))


n = int(input("请输入需要计算阶乘的数N = "))

print("1. 使用循环计算阶乘，结果：", fact1(n))
print("2. 使用递归计算阶乘，结果：", fact2(n))
print("3. 使用递归计算阶乘，结果：", fact3(n))


