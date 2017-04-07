# -*- coding: utf-8 -*-

# 过滤数据

# 最简单的方式是列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 列表推导的缺点是数据量非常大的时候会产生一个非常大的结果集,占用大量内存
# 如对内存占用比较敏感,可以使用生成器迭代产生过滤元素
pos = (n for n in mylist if n > 0)
print(pos)  # <generator object <genexpr> at 0x0000021D5F294EB8>
for x in pos:
    print(x)

# 如果过滤规则比较复杂,不能简单的在列表推导或生成器表达式中表达出来
# 可以写下个过滤函数,然后使用filter()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# filter创建了一个迭代器,需要使用list转换成列表

# 列表推导和生成器表达式也能在过滤时转换数据
import math

print([math.sqrt(n) for n in mylist if n > 0])

# 数据过滤的一个变种是将不符合条件的值用新值代替,而不是丢弃它们
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)  # [1, 4, 0, 10, 0, 2, 3, 0]
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)  # [0, 0, -5, 0, -7, 0, 0, -1]

# 另一个值得关注的过滤工具是itertools.compress()
# 它以一个iterable对象和一个相对应的Boolean选择器序列作为输入参数
# 然后输出iterable对象中对应选择器为true的元素
# 当需要用另外一个相关联的序列来过滤某个序列的时候,这个函数是非常有用的
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

# 将count大于5的地址全部输出
from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)  # [False, False, True, False, False, True, True, False]

print(list(compress(addresses, more5)))
# ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
