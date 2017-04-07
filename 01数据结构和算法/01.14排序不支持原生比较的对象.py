# -*- coding: utf-8 -*-

# 排序不支持原生比较的对象
# 内置的sorted()函数有一个关键字参数key,可以传递一个callable对象给它
# 这个对象对每个传入的对象返回一个值,sorted用这个返回值来排序对象

# 如,利用应用程序中User实例的user_id属性进行排序

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


sort_notcompare()
# 使用operator.attrgetter()来代替lambda函数
from operator import attrgetter

users = [User(23), User(3), User(99)]
print(sorted(users, key=attrgetter('user_id')))

# 使用lambda和attrgetter()取决于个人喜好,但attrgetter()函数通常会运行的快点,并能同时允许多个字段进行比较
# 这和operator.itemgetter()函数作用于字典类型很类似

# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
# 这些对min(),max()同样适用
print(min(users, key=attrgetter('user_id')))  # User(3)
print(max(users, key=attrgetter('user_id')))  # User(99)
