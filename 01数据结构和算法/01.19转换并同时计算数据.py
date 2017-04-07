# -*- coding: utf-8 -*-
#  在数据序列上执行聚焦函数(sum(),min(),max()),但是首先需要先转换或过滤数据

# 使用生成器表达式参数
# 计算平方和
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# 更多的例子
import os

# 判断当前目录下是否有.py文件
files = os.listdir(os.getcwd())
if any(name.endswith('.py') for name in files):
    print("当前目录下有python文件.")
else:
    print("当前目录下没有python文件.")
# 以csv格式输出元组
s = ("ACME", 50, 123.45)
print(','.join(str(x) for x in s))
# 通过数据结构中的字段简化数据
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

# 使用生成器表达式作为一个单独参数传递给函数时并不需要多加一个括号
# 下面语句等价
s = sum((x * x) for x in nums)
s = sum(x * x for x in nums)

# 使用生成器表达式作为参数会比先创建一个临时列表更加高效和优雅
# 如果不使用生成器表达式
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
# 这种方式同样可以达到效果,但会多一个步骤,先创建一个额外的列表
# 对小型列表没关系,但如果元素数量非常大的时候,它会创建一个巨大的仅仅被使用一次就被丢弃的临时数据
# 而生成器方案会以迭代方式转换数据,更省内存

# 在使用一些聚焦函数时使用生成器版本更方便
# 它们接受一个key关键字参数,所以也可以这样写:
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)  # 20
min_shares = min(portfolio, key=lambda s: s['shares'])
print(min_shares)  # {'name': 'AOL', 'shares': 20}
