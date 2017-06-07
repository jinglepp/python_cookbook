# -*- coding: utf-8 -*-
# 你想在迭代一个序列的同时跟踪正在被处理的元素索引。
# 解决方案
# 内置的 enumerate() 函数可以很好的解决这个问题：

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 为了按传统行号输出(行号从1开始)，你可以传递一个开始参数：
for idx, val in enumerate(my_list, 1):
    print(idx, val)


# 这种情况在你遍历文件时想在错误消息中使用行号定位时候非常有用：
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, line))


# enumerate() 对于跟踪某些值在列表中出现的位置是很有用的。
# 所以，如果你想将一个文件中出现的单词映射到它出现的行号上去，可以很容易的利用 enumerate() 来完成：
from collections import defaultdict

word_summary = defaultdict(list)
with open('somefile.txt', 'r') as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)
