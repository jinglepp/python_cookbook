# -*- coding: utf-8 -*-
# 构造一个字典,它是另一个字典的子集。
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 价格>200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)  # {'AAPL': 612.78, 'IBM': 205.55}
tech_names = {'AAPL', 'IBM', 'HPQ', "MSFT"}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

# 通常一个字典推导能做到的,通过创建一个元组序列然后把它传给dict()函数也能实现
pp = dict((key, value) for key, value in prices.items() if value > 200)
print(pp)
# 但是字典推导方式更清晰,并且实际上更快一些

# 有时候完成同一件事会有多种方式
p2_other_way = {key: prices[key] for key in prices.keys() & tech_names}
print(p2_other_way)
# 书中说这一种方式比字典推导慢1.6倍,
1