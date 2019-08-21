#!/usr/bin/env python
# -*- coding:utf-8 -*-

#  list 和 duple
# list的使用----------------------
students=[2,3,4,5,6,7]

print 'students = ',students

print 'students[-1] = ',students[-1]

s = raw_input('add a new value at last:')
students.append(s)
print 'students = ',students

t = len(students) - 1
i = raw_input("select the index \(form 0 to %d \):"%t)
s1 = raw_input("insert a number :")
students.insert(int(i),s1)
print 'students = ',students

print '\nDelete one index from students:\n'
t = len(students) - 1
index1 = raw_input('input the index\(from 0 to %d\):'%t)
if int(index1) <= t:
	students.pop(int(index1))
else:
	print "the index is error ! t = %d index1 = %d"%(t,index1)
print 'students = ',students
