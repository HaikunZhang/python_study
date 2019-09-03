#!/usr/bin/env python
# -*- coding:utf-8 -*-

##################################################################
# 练习2. 生成N个随机的大写字符存入列表
##################################################################

import random
import numpy


# 输入随机数并转为整数型
Num = int(input("请输入随机数个数N："))


# 方法一：传统方法---------------------------------------------------
result1 = []
for i in range(Num):
    # 生成65~91（不包括）的随机数
    n = random.randint(65, 90)
    # 将生成的随机数转化成大写字符
    result1.append(chr(n))
print('result1 =', result1)


# 方法二：列表推导式---------------------------------------------------
result2 = [chr(random.randint(65, 90)) for i in range(Num)]
print('result2 = ', result2)


# 方法三：使用numpy 模块一次生成N个随机数-------------------------------
# numpy.random.randint 可生成一个随机数的矩阵。
result3 = [chr(a) for a in numpy.random.randint(65, 91, [Num, 1])]
print('result3 =', result3)




