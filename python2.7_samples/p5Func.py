# -*- coding:utf-8 -*-


#  函数 - 1.必选参数

print u"\n 函数介绍：\n\n1. 必选参数：\n"

PI = 3.14
r = 2
def area_of_circle(PI,r):
  s = PI * r * r
  return s
s = area_of_circle(PI,r)
print "Q:PI = 3.14,r = 2. \nA:s = ",s

#  2.默认参数

print u"\n2. 默认参数：\n"

def a(a,b,c = 3,d = 4):
	print "a =",a
	print "b =",b
	print "c =",c
	print "d =",d	
print "Q:a(a,b,c = 3,d = 4). \nA:dd:"
dd = a(1,2,7)

# 3.可变参数：即传入的参数个数可变

print u"\n3. 可变参数：\n"

def calc(*numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum
	
print "calc(1,2,3) = ",calc(1,2,3)

nums = [1,2,3,4]
print "nums[1,2,3,4] = ",calc(*nums)

#  4.关键字参数: 用 ** 定义

print u"\n4. 关键字参数：\n"

kaw = {'department':'CMS','sex':'female'}

def groupPartner(name,age = 28,**kw):
	print 'Name:',name,'Age:',age,'Other:',kw
print "Q:kaw = {'department':'CMS','sex':'female'}. \n ddd:"
ddd = groupPartner('lqy',**kaw)

#  5. 参数组合

print u"\n5. 参数组合：\n"

def paramterMix(num,b=2,*args,**kw):
	if len(args) == 0 and len(kw) == 0:
		print 'num = ',num,'; b = ',b
	elif len(args) == 0:
		print 'num = ',num,'; b = ',b,'; kw =',kw
	elif len(kw) == 0:
		print 'num = ',num,'; b = ',b,'; args =',args
	else:
		print 'num = ',num,'; b = ',b,'; args =',args,'; kw =',kw

print "paramterMix(1):",paramterMix(1)
 
print "paramterMix(2,'a'):",paramterMix(2,'a')

print "paramterMix(3,'b',*('q','w','e','r')):",paramterMix(3,'b',*('q','w','e','r'))

print "paramterMix(4,'c',*('a','s','d','f'),s = 5,t = 6,g = 7):",paramterMix(4,'c',*('a','s','d','f'),s = 5,t = 6,g = 7)

print "paramterMix(5,*('z','x','c','v'),**{'ss':55,'tt':66}):",paramterMix(5,*('z','x','c','v'),**{'ss':55,'tt':66})

print "paramterMix(6,**{'ss':99,'tt':88}):",paramterMix(6,**{'ss':99,'tt':88})


#  6. 函数递归

print u"\n6. 函数递归：\n"

def arit(n):
	if n > 1 :
		return  n + arit(n - 1)
	else:
		return n
		
print u"1至100的等差数列之和：",arit(100)

def fact(n):
    return fact_x(n,1)
def fact_x(x,y):
	if x == 1:
		return y
	return  fact_x(x - 1, x*y)
print "The product from 1 to 5:",fact(5)