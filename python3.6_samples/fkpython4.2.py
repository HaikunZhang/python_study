#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = 'javascript'


def foo():
    name = 'python'
    print('foo函数声明的name:', name)  # python

    def bar():
        nonlocal name  # 表示name 不是新声明的局部变量
        print('bar函数处理前的name:', name)  # python
        name = 'java'  # 默认情况下， name是bar函数新声明的一个局部变量
        print('bar函数处理后的name:', name)  # java
    bar()
    print('最终的name:', name)  # java


foo()
