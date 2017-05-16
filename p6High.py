#!/usr/bin/env python
#-*- coding:utf-8 -*-

'a practised module'

__author__ = 'haikun'

print '\n----------------------------------------------'
#   切片

print 'range(100)[::5] =',range(100)[::5],'\n'

S = 'QWERTYUIOPASDFGHJKLXZCVBNMN'
print 'S =',S
print 'S[0::2] =',S[0::2]

print '\n----------------------------------------------'
# 生成器

print u'10以内的斐波拉奇数列：'
def  fib(max):
    a,b,n=0,1,0
    while n < max :
        yield b		# 返回后继续执行
        a,b = b , a+b
        n = n + 1		
for x in fib(10):
	print x

print '\n----------------------------------------------'	
# 高阶函数：map/reduce


# task:将List 中的元素首字母换成大写,其他全小写
L = ['admin','LISA','barT']
print u'L[\'admin\',\'LISA\',\'barT\']首字母大写：',map(lambda x:x.title(),L)

#  sum()函数可以对list求和，编写函数prod(),利用reduce()求list的积
L = range(10)
def prod(x,y):
	if x >0:
		return x*y
	else:
		return 1	
print u'L[1,2,3,4,5,6,7,8,9,10]的乘积：',reduce(prod,L)

print '\n----------------------------------------------'
# filter

#task:用filter()删除1~100的素数
def isNotPrime(x):
	if x == 1:
		return True
	i = 2
	while i < x:
		if x%i ==0:
			return True
		i = i+ 1
	return False
notPrime = filter(isNotPrime,range(1,101))
print u'100以内的非素数共%d个，分别是：%s'%(len(notPrime),notPrime)

print '\n----------------------------------------------'
# 返回函数/闭包			匿名函数： lambda x:x*y

def t_sum(*args):
    def sum():
        s = 0
        for x in args :
            s = s + x
        return s
    return sum
t = t_sum(1,2,3,4,5)
print '1+2+3+4+5=',t()

print '\n----------------------------------------------'
# 生成器：dacorator

import functools


def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s():'%func.__name__
		return func(*args,**kw)
	return wrapper
@log
def now():
	print "11-17-2016\n\n"
now()

# 编写一个decorator，在调用函数前后分别打出begin call和end call

def deco1(func):
	def AA(*args,**kw):
		print "begin call:"
		ccc = func(*args,**kw)			
		print "end call ."	
		return ccc	
	return AA
	
@deco1
def fuA():
	print "This is a function which is waiting to call."

fuA()


fuC()	
print '\n----------------------------------------------'
# 偏函数：Partial function

import functools
int2 = functools.partial(int,base=2)
print "",int2('1000')
