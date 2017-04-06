# -*- coding: utf-8 -*-
# slice()
###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
# 利用切片从一段字符串中提取某一段时
# 使用命名切片可以避免大量无法理解的硬编码下标,使代码更清晰可读
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

# 内置的slice函数创建了一个切片对象,可以被用在任何切片允许使用的地方
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])  # [2, 3]
items[a] = [10, 11]
print(items)  # [0, 1, 10, 11, 4, 5, 6]
del items[a]
print(items)  # [0, 1, 4, 5, 6]

# 切片对象有start,stop,step属性
a = slice(5, 50, 2)
print(a.start, a.stop, a.step)  # 5 50 2

# 可以通过调用切片的indices(size)方法将它映射到一个确定大小的序列上,
# 这个方法返回一个三元组(start,stop,step),且所有值都会被合适的缩小以到边界限制
# 从而避免IndexError
s = "HelloWorld"
print(a.indices(len(s)))  # (5, 10, 2)
