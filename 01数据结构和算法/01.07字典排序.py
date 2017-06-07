# -*- coding: utf-8 -*-
# 问题
# 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
#
# 解决方案
# 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。
# 在迭代操作的时候它会保持元素被插入时的顺序，示例如下：
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

# python 3.6之后dict会保持插入顺序了,OrderedDict内存也改为pypy的实现方式了
