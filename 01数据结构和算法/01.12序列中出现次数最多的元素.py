# -*- coding: utf-8 -*-
# 问题
# 怎样找出一个序列中出现次数最多的元素呢？
# 解决方案
# collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案。
# 为了演示，先假设你有一个单词列表并且想找出哪个单词出现频率最高。你可以这样做：
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_counts = Counter(words)
# 出现频率最高的3个单词
# most_common(3)
print(word_counts.most_common())
# [('eyes', 8), ('the', 5), ('look', 4), ..., ("you're", 1), ('under', 1)]
top_tree = word_counts.most_common(3)
print(top_tree)  # [('eyes', 8), ('the', 5), ('look', 4)]

# 讨论
# 作为输入,Counter对象可以接受任意的hashable元素序列对象
# 在底层实现上,一个Counter对象就是一个字典,将元素映射到它出现我次数上.
print(word_counts['not'])  # 1
print(word_counts['eyes'])  # 8

# 如果你想手动增加计数，可以简单的用加法：
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts)

# 或者使用update()方法
word_counts.update(morewords)

# Counter实例一个鲜为人知的特性是它可以很容易跟数学运算结合
a = Counter(words)
b = Counter(morewords)
print(a)
# Counter({'eyes': 8, 'the': 5, 'look': 4, ...
print(b)
# Counter({'why': 1, 'are': 1, 'you': 1, 'not'...
print(a + b)
# Counter({'eyes': 9, 'the': 5, 'look': 4, ...
print(a - b)
# Counter({'eyes': 7, 'the': 5, 'look': 4, ...

# 毫无疑问， Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。
# 在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。
