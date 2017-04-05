# -*- coding: utf-8 -*-

# dict是一个键对应一个单值的映射
# 如果需要一个键对应多个值,需要将这多个值放到另外的容器中
# 如:
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}
# 使用列表还是集合取决于实际需求
# 如果想保持元素的插入顺序就应该使用列表
# 如果想去掉重复元素就使用集合

# collections模块中的defaultdict会自动初始化每个key刚开始对应的值

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)
d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['a'].add(4)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2, 4]})
print(d2)  # defaultdict(<class 'set'>, {'a': {1, 2, 4}})

# defaultdict会自动为要访问的key创建映射实体
# 如果要禁用这样的特性,可以在一个普通dict上使用setdefault()来代替
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)  # {'a': [1, 2], 'b': [4]}

# # 自己实现
# d = {}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)

# # 使用defaultdict更简洁
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)
