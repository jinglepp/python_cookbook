# -*- coding: utf-8 -*-
# 通过下标访问元素使代码难以阅读,通过名称要清晰一些

# collections.namedtuple()函数使用一个普通的元组来解决这个问题
# 这个函数实际上是一个返回Python标准元组类型子类的一个工厂方法.
# 传递一个类型名和需要的字段给它,就会返回一个类,可以初始化这个类,为定义的字段传递值
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jinglepp@qq.com', '2017-04-07')
print(sub)  # Subscriber(addr='jinglepp@qq.com', joined='2017-04-07')
print(sub.addr)
print(sub.joined)

# 尽管namedtuple实例看起来像一个普通的类实例
# 但是它跟元组类型是可交换的,支持所有的普通元组操作,如索引和解压
print(len(sub))
addr, joined = sub
print(addr, joined)


# 命名元组的一个主要用途是将代码从下标操作中解脱出来.
# 因此,如果从数据库调用中返回了一个很大的元组列表,通过下标去操作元素时
# 如果在表中添加了新的列,代码就出错了,但是使用命名元组不会有这样的问题

# 如:
# 使用普通元组
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# 普通元组会让代码表意不清晰,并且非常依赖记录的结构.
# 使用命名元组的版本:

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost_namedtuple(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# 命名元组的另一个用途是作为字典的替代,因为字典存储需要更多的内存空间.如果需要构建一个非常大的包含字典的数据结构
# 使用命名元组更加高效
# 需要注意的是,不像字典那样,一个命名元组是不可更改的.
s = Stock('ACME', 100, 123.45)
print(s)  # Stock(name='ACME', shares=100, price=123.45)
print(s.shares)
# s.shares = 75  # AttributeError: can't set attribute

# 如果真的需要改变属性的值
# 可以使用命名元组实例的_replace()方法,它会创建一个全新的命名元组并将对应的字段用新的值取代
s = s._replace(shares=75)
print(s)  # Stock(name='ACME', shares=75, price=123.45)

# _replace()方法还有一个很有用的特性是当命名元组拥有可选或者缺失字段时,它是一个非常方便的填充数据的方法
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# 创建一个原型实例
stock_prototype = Stock('', 0, 0.0, None, None)


# 转换字典到Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


# 使用方法:
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
# Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))
# Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)

# 最后,如果目标是定义一个需要更新很多实例属性的高效数据结构,那么命名元组并不是最佳选择
# 这时候应该考虑定义一个包含__slots__方法的类
