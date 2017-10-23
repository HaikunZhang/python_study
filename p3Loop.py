# -*- coding:utf-8 -*-


# 判断和循环
x = 20
if x < 2:
	print "asdf"
	print "asdaasdfa"
elif x < 10:
	print "OK!"
else:
	print "x = ",x

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print "name = ",name

sum = 0	
for x in range(101):
	sum = sum + x
print "sum = ",sum

n = 0
sum = 0
while n < 100:
	n = n + 1
	sum = sum + n

print "sum = ",sum

print u'中文'

#while 1:
#	print "Hello \n"

