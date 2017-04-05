# -*- coding: utf-8 -*-

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

# heapq.heappush()和heapq.heappop()分别在队列_queue上插入和删除第一个元素
# 并且_queue保证第1个元素拥有最高优先级.
# heappop()函数总是返回最小的元素,这保证了队列pop操作返回正确元素
# push和pop的时间复杂度为O(logN)
# 上面代码中,队列包含了一个(-priority,index,item)的元组.
# 优先级为负数便元素按照优先级从高到低排序.这跟普通的按优先级从低到高排序的堆排序相反
# index变量的作用是保证同等优先级元素的正常排序

a = Item('foo')
b = Item('bar')
# print(a < b)
# TypeError: '<' not supported between instances of 'Item' and 'Item'

a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)
c = (1, Item('grok'))
# print(a < c)
# TypeError: '<' not supported between instances of 'Item' and 'Item'
# 通过另外引入index组成(priority,index,item)可以避免上面的错误

# 如果想在多个线程中使用同一个队列,需要增加适应的锁和信号量机制,具体见12.3的例子
