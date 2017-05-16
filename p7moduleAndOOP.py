#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '\n----------------------------------------------'
#  1. 模块

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, this is a test model !'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

	if __name__=='__main__':   #导入时不调用test()
		test()

test()
		
print '\n----------------------------------------------'		
#	2.面向对象编程

#创建一个类		
class Student(object):
        def __init__(self,name,score):
            self.__name = name
            self.__score = score
			
		#封装的方法
        def print_score(self):
            print "Name: %s,Grade: %s"%(self.__name,self.__score)
        def get_grade(self):
            if self.__score >= 90:
                return 'A'
            elif self.__score >= 60:
                return 'B'
            else:
                return 'C'

bart = Student('zhk',99)

bart.print_score()

print "The Grade is %s."%(bart.get_grade())