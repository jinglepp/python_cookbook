# -*- coding: utf-8 -*-

p = (4, 5)
x, y = p
print(x, y)
data = ['ACME', 50, 91.1, (2017, 3, 31)]
# name, shares, price, date = data
# print(name, shares, price, data)
# name, shares, price, (year, mon, day) = data
# print(name, shares, price, year, '/', mon, '/', day)

# 个数不匹配会产生一个异常：
# ValueError: not enough values to unpack
# x, y, z = p
# print(x, y, z)

# 也可以用在迭代对象上
s = "Hello"
# a, b, c, d, e = s
# print(a, b, c, d, e)
# 如果只想解压一部分，丢弃其他的值，使用占位符
# _, shares, price, _ = data
