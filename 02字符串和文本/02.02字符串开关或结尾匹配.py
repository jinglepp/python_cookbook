# -*- coding: utf-8 -*-

# 通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等。

# 解决方案
# 检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法。比如：
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，
#  然后传给 startswith() 或者 endswith() 方法：
import os

filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.py', '.pyc'))])
print(any(name.endswith('.py') for name in filenames))

# 下面是另一个例子
from urllib.request import urlopen


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# 奇怪的是，这个方法中必须要输入一个元组作为参数。
# 如果你恰巧有一个 list 或者 set 类型的选择项，
# 要确保传递参数前先调用 tuple() 将其转换为元组类型。比如：
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices)) # TypeError: startswith first arg must be str or a tuple of str, not list
print(url.startswith(tuple(choices)))

# 讨论
# startswith() 和 endswith() 方法提供了一个非常方便的方式去做字符串开头和结尾的检查。
# 类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅。比如：
filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')
# 你可以能还想使用正则表达式去实现，比如：
import re

url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))
# 这种方式也行得通，但是对于简单的匹配实在是有点小材大用了，本节中的方法更加简单并且运行会更快些。

# 最后提一下，当和其他操作比如普通数据聚合相结合的时候 startswith() 和 endswith() 方法是很不错的。
# 比如，下面这个语句检查某个文件夹中是否存在指定的文件类型：
if any(name.endswith(('.py', '.pyc')) for name in os.listdir('.')):
    print('当前目录下有.py文件')
