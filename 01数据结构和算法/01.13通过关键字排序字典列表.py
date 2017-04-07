# -*- coding: utf-8 -*-

# 根据字典列表中的某个或某几个字典字段来排序这个列表

# 使用operator模块的itemgetter函数

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# itemgetter()函数支持多个keys
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

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
