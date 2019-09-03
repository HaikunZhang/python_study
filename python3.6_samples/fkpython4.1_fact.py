#!/usr/bin/env python
# -*- coding:utf-8 -*-


def fact(n):
    if n < 1:
        return 1
    else:
        print(n, "*", end=" ") if n != 1 else print(n, "=", end=" ")
        return n * fact(n-1)


s = int(input("请输入需要计算阶乘的数："))
print(fact(s))


