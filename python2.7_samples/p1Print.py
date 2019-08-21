#!/usr/bin/env python
# -*- coding:utf-8 -*-

#6.格式输出：

print '%2d-%2d'%(3,1)

print  '%2d - %2d'%(3,1)

#5.中文输出：

print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

u'中文'.encode('utf-8')

#4.转义输出： (r 表示内部字符不转义）

print r"\\\n\\"

print "\\\n\\"

print ''' line1
...line2
...line3
\\\n\\......line4'''

print r''' line1
...line2
...line3
\\\n\\line4'''


#3.输入学习：

name=raw_input("Please enter your name:")

if name == "zhk":
    print "\nHello,",name
else:
    print u"输入错误"

#2.输出计算结果：

print "\n100 + 200 =",100+200

#1.带换行、带引号输出：

print "\nHello World !"

print "\nI'd much rather you 'not'.\n"

print 'I said "do not touch this" .\n'

