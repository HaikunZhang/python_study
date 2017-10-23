# -*- coding:utf-8 -*-


#  dict 和 set

d = { 0:"a",1:"b",2:"c"}
print "d = ",d

d[3]="d"
print "d = ",d

print "judge the key is exist:"
3 in d
d.get(4)
d.get(5,-1)

print "delete one key:"
d.pop(3)
print "d = ",d



d = set([1,2,3])
print "d = ",d

d.add(4)
d.add(5)
print "d = ",d

d.remove(4)
print "d = ",d


a = raw_input("pause !")