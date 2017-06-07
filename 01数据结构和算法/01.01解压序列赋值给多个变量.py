# -*- coding: utf-8 -*-
# 现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？
# 解决方案
# 任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。 唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
#
# 代码示例：
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
