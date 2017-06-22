# coding:utf-8

# 问题
# 你需要处理一个很大的数据集并需要计算数据总和或其他统计量。

# 解决方案
# 对于任何涉及到统计、时间序列以及其他相关技术的数据分析问题，都可以考虑使用 Pandas库 。

# https://data.cityofchicago.org/Service-Requests/311-Service-Requests-Rodent-Baiting/97t6-zrhs
# 为了让你先体验下，下面是一个使用Pandas来分析芝加哥城市的老鼠和啮齿类动物数据库的例子。
# 在我写这篇文章的时候，这个数据库是一个拥有大概74,000行数据的CSV文件。

import pandas

rats = pandas.read_csv('rats.csv', skipfooter=1, engine='python')
# print(rats)
# print(rats['Current Activity'].unique)
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
# print(len(crew_dispatched))
# print(crew_dispatched['ZIP Code'].value_counts()[0:10])
print(crew_dispatched['ZIP Code'].value_counts().values[:10])
# [13635 12919 10100  9735  8640  7759  7218  7096  6868  6589]

dates = crew_dispatched.groupby('Completion Date')
print(len(dates))
#
date_counts = dates.size()
print(date_counts[0:10])
#
# # date_counts.sort()  # AttributeError: 'Series' object has no attribute 'sort'
date_counts.values.sort()
print(date_counts[-10:])
# 12/29/2016    378
# 12/30/2011    384
# 12/30/2013    384
# 12/30/2014    391
# 12/30/2015    401
# 12/30/2016    412
# 12/31/2012    457
# 12/31/2013    461
# 12/31/2014    488
# 12/31/2015    492
# 嗯，看样子2015年12月31日对老鼠们来说是个很忙碌的日子啊！^_^

# 讨论
# Pandas是一个拥有很多特性的大型函数库，我在这里不可能介绍完。
# 但是只要你需要去分析大型数据集合、对数据分组、计算各种统计量或其他类似任务的话，这个函数库真的值得你去看一看。
