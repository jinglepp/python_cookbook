# -*- coding: utf-8 -*-

# 问题
# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
#
# 解决方案
# 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。
# 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
# 根据字典列表中的某个或某几个字典字段来排序这个列表
# 使用operator模块的itemgetter函数
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# itemgetter()函数支持多个keys
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# 讨论
# 在上面例子中， rows 被传递给接受一个关键字参数的 sorted() 内置函数。
# 这个参数是 callable 类型，并且从 rows 中接受一个单一元素，然后返回被用来排序的值。
# itemgetter() 函数就是负责创建这个 callable 对象的。

# operator.itemgetter() 函数有一个被 rows 中的记录用来查找值的索引参数。
# 可以是一个字典键名称， 一个整形值或者任何能够传入一个对象的 __getitem__() 方法的值。
# 如果你传入多个索引参数给 itemgetter() ，它生成的 callable 对象会返回一个包含所有元素值的元组，
# 并且 sorted() 函数会根据这个元组中元素顺序去排序。
# 但你想要同时在几个字段上面进行排序(比如通过姓和名来排序，也就是例子中的那样)的时候这种方法是很有用的。

# sorted()内置函数接受一个key参数，这个参数是callable类型，它从序列中接受一个单一元素并返回用来排序的值
# operator.itemgetter()函数可以生成这个callable对象。它接受任何能被传入__getitem__方法的值
# 如果传入多个索引参数给itemgetter，它生成的callable对象会返回一个包含所有元素值的元组
# sorted()会根据这个元组排序
# itemgetter()有时候可以用lambda表达式代替
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
# 这种方案也不错，但是itemgetter()方式会稍微快点，如果对性能要求比较高的话就使用itemgetter()

# itemgetter()对min()和max()函数同样适用
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
