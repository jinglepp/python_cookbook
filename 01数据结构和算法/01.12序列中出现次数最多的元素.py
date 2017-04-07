# -*- coding: utf-8 -*-
# collections.Counter类是专门为这类问题而设计的
# most_common()
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_counts = Counter(words)
# 出现频率最高的3个单词
print(word_counts.most_common())
# [('eyes', 8), ('the', 5), ('look', 4), ..., ("you're", 1), ('under', 1)]
top_tree = word_counts.most_common(3)
print(top_tree)  # [('eyes', 8), ('the', 5), ('look', 4)]

# 作为输入,Counter对象可以接受任意的hashable元素序列对象
# 在底层实现上,一个Counter对象就是一个字典,将元素映射到它出现我次数上.
print(word_counts['not'])  # 1
print(word_counts['eyes'])  # 8

# 可以手动增加计数
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
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1,
# 'under': 1})
print(b)
# Counter({'why': 1, 'are': 1, 'you': 1, 'not': 1, 'looking': 1, 'in': 1, 'my': 1, 'eyes': 1})
print(a + b)
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2, 'around': 2, "don't": 1, "you're": 1,
# 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking': 1, 'in': 1})
print(a - b)
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2, "don't": 1, "you're": 1, 'under': 1})

# Counter对象在制表或计数数据的场合经常用到
