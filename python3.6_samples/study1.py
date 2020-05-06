#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 1. 请利用print()输出1024 * 768 = xxx
print("1024 * 768 =", 1024 * 768)


# 2. 多行输出
print('''这是第一行
这是第二行...
这是第三行''')

# 3. 不转义输出
print(r"\n\\\\-->加r表示不转义")


print(str(1234) + str(5678))

print(repr(1234) + repr(5678))




b1 = b'abc'
print(b1)
b2='我爱你'.encode()
print(b2)
b3=bytes("我爱你","UTF-8")
print(b3)
b4 = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0'
print(b4.decode('UTF-8'))


a, b , c =range(5)