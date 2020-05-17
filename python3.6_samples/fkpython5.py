#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 8.定义类：
class User:
    def __init__(self, name='init'):
        self.name = name  # self 代表该构造器正在构造的对象

    def info(self):
        print(self)
        print(self.name)


u1 = User()  # 此时User中的self 代表u1
print(u1.name)

u2 = User(' this is u2\'s name')  # 此时User中的self 代表u2
print(u2.name)
print("u2:", u2)
u2.info()  # 通过u2调用info，那么info中的self 则代表u2
u1.info()  # 通过u1调用info，那么info中的self 则代表u1
