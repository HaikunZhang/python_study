#!/usr/bin/env python
# -*- coding:utf-8 -*-

##################################################################
# 练习3. 列表去重
##################################################################

import random
import itertools


# 方法1.新列表搜集法---------------------------------------------

# 使用列表推导式创建一个包含重复元素的列表：
scr_list1 = [random.randint(20, 25) for i in range(15)]
print('scr_list1 =', scr_list1)
target_list1 = []
for ele in scr_list1:
    if ele not in target_list1:
        target_list1.append(ele)
print('去重后：', target_list1)


# 方法2.使用set集合去重-----------------------------------------------

# 注意： set集合去重后会自动排序
scr_list2 = [random.randint(20, 30) for i in range(15)]
print('scr_list2 =', scr_list2)
target_list2 = list(set(scr_list2))
print('去重后：', target_list2)


# 方法3.使用itertools模块的groupBy函数去重-----------------------------

# group函数用于分组，相同的就分为同一组， 所以使用这种方式去重需要先对列表进行排序
scr_list3 = [random.randint(20, 30) for i in range(15)]
print('scr_list3 =', scr_list3)
scr_list3.sort()
it = itertools.groupby(scr_list3)
for k, g in it:
    print(k, end=" ")  # end表示以" "分隔





