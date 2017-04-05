# -*- coding: utf-8 -*-

from collections import deque


# 发现有匹配时输出当前匹配行和最后检查过的N行
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern.lower() in li.lower():
            yield li, previous_lines
        previous_lines.append(li)


if __name__ == '__main__':
    with open('test.txt', encoding='utf-8') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


# from collections import deque
#
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q)  # deque([1, 2, 3])
# q.appendleft(4)
# print(q)  # deque([4, 1, 2, 3])
# q.pop()
# print(q)  # deque([4, 1, 2])
#
# # 在deque两端插入或删除元素时间复杂度都是O(1)
# # 在list的开头插入或删除元素时的时间复杂度是O(N)
