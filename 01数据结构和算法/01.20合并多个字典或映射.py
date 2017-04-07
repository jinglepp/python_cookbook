# -*- coding: utf-8 -*-
# 合并多个字典或映射

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 如果要在两个字典中执行查找
# 最简单的方法是collections模块中的ChaiMap类
from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

# 一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。 然后，这些字典并不是真的合并在一起了，
#  ChainMap 类只是在内部创建了一个容纳这些字典的列表
# 并重新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的，比如：
print(len(c))  # 3
print(list(c.keys()))  # ['x', 'y', 'z']
print(list(c.values()))  # [1, 2, 3]

# 如果出现重复键,那么第一次出现的映射值会被返回
# 对字典的更新或删除总是影响的是列表中第一个字典。

c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']  # KeyError: "Key not found in the first mapping: 'y'"

# ChainMap 对于编程语言中的作用范围变量(比如 globals , locals 等)是非常有用的。 事实上，有一些方法可以使它变得简单：

values = ChainMap()
values['x'] = 1
# 增加一个新的映射
values = values.new_child()
values['x'] = 2
# 增加一个新的映射
values = values.new_child()
values['x'] = 3
print(values)
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])  # 3
# 丢弃最后一个映射
values = values.parents
print(values['x'])  # 2
# 丢弃最后一个映射
values = values.parents
print(values['x'])  # 1
print(values)  # ChainMap({'x': 1})

# 作为 ChainMap 的替代，你可能会考虑使用 update() 方法将两个字典合并。如:
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'], merged['y'], merged['z'])
# 这样也能行得通，但是它需要你创建一个完全不同的字典对象(或者是破坏现有字典结构)。
# 同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去。比如：
a['x'] = 13
print(merged['x'])  # 1
# ChainMap 使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说的结果，比如：
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])  # 1
a['x'] = 42
print(a['x'])  # 42
