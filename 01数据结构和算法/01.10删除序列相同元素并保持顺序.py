# -*- coding: utf-8 -*-
# 在一个序列上面保持元素顺序的同时消除重复的值

# # 如果序列上的值都是hashable的
# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#         seen.add(item)
#
#
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# print(list(dedupe(a)))


# 如果想消除元素不可哈希(如dict),上面会TypeError: unhashable type: 'dict'
# 这时可以把代码改成这样:

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))
# 这种方案同样适用于基于单个字段属性或者某个更大的数据结构来消除重复元素

# 如果仅仅想消除重复元素,可以直接构造一个set
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))
# 这种方法不能保持元素的顺序,生成的结果中的元素位置被打乱.而上面的方法可以避免这种情况

# ps:上面用到生成器函数可以使函数更加通常,不仅仅是局限于列表处理.
# 比如想读取文件,消除重复行:
somefile = "test.txt"
with open(somefile, 'r') as f:
    for line in dedupe(f):
        pass
