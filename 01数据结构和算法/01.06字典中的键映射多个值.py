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
# 如果想去掉重复元素就使用集合（并且不关心元素的顺序问题）

# 你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
# defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。
# 比如：

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

# 需要注意的是， defaultdict 会自动为将要访问的键(就算目前字典中并不存在这样的键)创建映射实体。
# 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。比如：
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)  # {'a': [1, 2], 'b': [4]}

# 但是很多程序员觉得 setdefault() 用起来有点别扭。
# 因为每次调用都得创建一个新的初始值的实例(例子程序中的空列表 [] )。


# 讨论
# 一般来讲，创建一个多值映射字典是很简单的。
# 但是，如果你选择自己实现的话，那么对于值的初始化可能会有点麻烦， 你可能会像下面这样来实现：
# d = {}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)

# # 使用defaultdict更简洁
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)

# 这一小节所讨论的问题跟数据处理中的记录归类问题有大的关联。可以参考1.15小节的例子。
