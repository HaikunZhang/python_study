#!/usr/bin/env python
# -*- coding:utf-8 -*-

# yield 的使用

def test(max_val , step):
    print("开始执行：")
    cur = 0
    for i in range(max_val):
        cur +=i * step
        yield cur



gen = test(10,3)

for j in gen:
    print("gen:%d" % j)






