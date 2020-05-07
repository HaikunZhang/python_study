#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 1.请利用print()输出1024 * 768 = xxx
print("1024 * 768 =", 1024 * 768)


# 2.多行输出
print('''这是第一行
这是第二行...
这是第三行''')


# 3.不转义输出
print(r"\n\\\\-->加r表示不转义")


# 4.str() 和 repr() 的区别：
print(str('str and repr'))
print(repr('str and repr'))


# 5.字符编码:
b1 = b'abc'
print(b1)
b2 = '我爱你'.encode()
print(b2)
b3 = bytes("我爱你", "UTF-8")
print(b3)
b4 = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'
print(b4.decode('UTF-8'))


# 6.序列自动解包:
a, *b, c = range(5)
print(a, b, c)


# 7. if 的使用：
score = int(input('please input score: (0-100)'))
if score > 99:
    print('A')
elif score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")

