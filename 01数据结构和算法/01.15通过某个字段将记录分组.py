# -*- coding: utf-8 -*-
# itertools.groupby()函数用来数据分组非常实用
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 按date分组
# 需要先按指定字段(date)排序,再调用itertools.groupby()函数

from operator import itemgetter
from itertools import groupby

# 排序
rows.sort(key=itemgetter('date'))
# 分组
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# groupby()函数扫描整个序列并查找连续相同值(或者根据指定key函数返回值相同)的元素序列
# 在每次迭代时,它会返回一个值和一个迭代器对象,这个迭代器对象可以生成元素值全部等于上面那个值的组中所有对象

# 需要注意的是要根据指定字段将数据排序.因为groupby()仅仅检查连续的元素
# 如果事先并没有排序完成的话,分组函数将得不到想要的结果

# 如果仅仅只是想根据date字段将数据分组到一个大的数据结构中去,并允许随机访问,
# 那么最好使用defaultdict()来构建一个多值字典
# 如
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)
for r in rows_by_date['07/01/2012']:
    print(r)

# 这种方式不需要先将记录排序
# 如果不是很在意内存占用,这种方式会比先排序再通过groupby()快一些
