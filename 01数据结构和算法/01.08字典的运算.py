# -*- coding: utf-8 -*-

# 字典的常用计算操作(最大值,最小值,排序):
# 股票名称和价格映射字典
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 为了对字典值执行计算操作,通常需要使用zip()函数先将键和值反转过来.如
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)  # (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)  # (612.78, 'AAPL')

# 类似的,可以使用zip()和sorted()函数来排列字典数据
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

# # 这里需要注意的是zip()函数创建的是一个*只能访问一次*的迭代器.
# # 下面这样连续访问会出错.
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

# 在字典上执行普通的数学运算
min(prices)  # 'AAPL'
max(prices)  # 'IBM'
# 值可以使用values()
min(prices.values())  # 10.75
max(prices.values())  # 612.78

# 可以在min()和max()函数中提供key参数来获取最大值或最小值对应的键信息
print(min(prices, key=lambda k: prices[k]))  # FB
print(max(prices, key=lambda k: prices[k]))  # AAPL
# 但是如果还想要得到最小值,需要再执行一次查找
min_value = prices[min(prices, key=lambda k: prices[k])]

# zip()反转字典为值键元组后,比较时值会先进行比较,然后才是键
# 这样一条简单的语句就可以轻松的实现在字典上的求最值和排序操作了
# 需要注意的是,反转后,如果最大值或最小值有重复,那么拥有最小或最大键的实体会返回
prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))  # (45.23, 'AAA')
print(max(zip(prices.values(), prices.keys())))  # (45.23, 'ZZZ')
