# -*- coding: utf-8 -*-

from collections import OrderedDict

# OrderedDict保持传递顺序
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])  # foo 1 bar 2 spam 3 grok 4

# 在需要序列化或转成其他格式时OrderedDict经常用到
# 如精确控制以JSON编码后字段的顺序:
import json

json.dumps(d)
print(d)  # OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])

# OrderedDict内部维护着一个根据键插入顺序排序的双向链表
# 每次一个新的元素插入进来时,它会被放到链表的尾部
# 对一个已经存在的键的重复赋值不会改变键的顺序

# 需要注意的是,一个OrderedDict的大小是一个普通字典的两倍,因为它内部维护着另外一个链表.
# 所以数据量很大的时候要权衡一下
