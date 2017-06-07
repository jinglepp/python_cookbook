# -*- coding: utf-8 -*-
# 实现一个按优先级排序的队列？ 并且在这个队列上面每次pop操作总是返回优先级最高的那个元素

# 使用heapq模块实现一个简单的优先级队列
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 下面是它的使用方式：

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())  # Item('bar')
print(q.pop())  # Item('spam')
print(q.pop())  # Item('foo')
print(q.pop())  # Item('grok')

# pop()返回优先级最高的元素.如果两个有相同优先级的元素,pop按照它们的插入顺序返回

# 讨论
# 这一小节我们主要关注 heapq 模块的使用。
# 函数 heapq.heappush() 和 heapq.heappop() 分别在队列 _queue 上插入和删除第一个元素，
# 并且队列_queue保证第一个元素拥有最高优先级(1.4节已经讨论过这个问题)。
# heappop() 函数总是返回”最小的”的元素，这就是保证队列pop操作返回正确元素的关键。
# 另外，由于push和pop操作时间复杂度为O(log N)，其中N是堆的大小，因此就算是N很大的时候它们运行速度也依旧很快。

# 在上面代码中，队列包含了一个 (-priority, index, item) 的元组。
# 优先级为负数的目的是使得元素按照优先级从高到低排序。 这个跟普通的按优先级从低到高排序的堆排序恰巧相反。

# index 变量的作用是保证同等优先级元素的正确排序。
# 通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。
# 而且， index 变量也在相同优先级元素比较的时候起到重要作用。

# 为了阐明这些，先假定Item实例是不支持排序的：
a = Item('foo')
b = Item('bar')
# print(a < b)
# TypeError: '<' not supported between instances of 'Item' and 'Item'
# 如果你使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。
# 但是如果两个元素优先级一样的话，那么比较操作就会跟之前一样出错：
a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)
c = (1, Item('grok'))
# print(a < c)
# TypeError: '<' not supported between instances of 'Item' and 'Item'
# 通过另外引入index组成(priority,index,item)可以避免上面的错误
# 因为不可能有两个元素有相同的 index 值。
# Python在做元组比较时候，如果前面的比较已经可以确定结果了， 后面的比较操作就不会发生了：
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b, a < c)
# 如果想在多个线程中使用同一个队列,需要增加适应的锁和信号量机制,具体见12.3的例子
