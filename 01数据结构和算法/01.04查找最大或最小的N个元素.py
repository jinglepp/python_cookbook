# -*- coding: utf-8 -*-

# 从一个集合中获得最大或者最小的N个元素
# 使用heapq模块

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]

# 使用关键字用于更复杂的数据结构中
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# 如果你想在一个集合中查找最小或最大的N个元素，并且N小于集合元素数量，那么这些函数提供了很好的性能。

# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素。
# 并且剩余的元素可以很容易的通过调用 heapq.heappop() 方法得到， 该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素
# (这种操作时间复杂度仅仅是O(log N)，N是堆大小)。
heapq.heapify(nums)
print(nums)  # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

# 当要查找的元素个数相对比较小的时候函数nLargest()和nsmallest()是很合适的
# 如果仅仅想查找唯一的最小或最大(N=1)的元素的话,使用min()和max()函数会更快些
# 类似的,如果N的大小和集合大小接近的时候,通常先排序这个集合然后再使用切片操作会更快点
# sorted(items)[:N]或者sorted(items)[-N:]
# 需要在正确场合使用nLargest()和nsmallest()才能发挥它们的优势.
