# -*- coding: utf-8 -*-
# 问题
# 你想测试一个文件或目录是否存在。

# 解决方案
# 使用 os.path 模块来测试一个文件或目录是否存在。比如：

import os

test_path = r'D:\testdata\test.txt'
print(os.path.exists(test_path))

# 你还能进一步测试这个文件时什么类型的。 在下面这些测试中，如果测试的文件不存在的时候，结果都会返回False：
print(os.path.isfile(test_path))
print(os.path.isdir(test_path))
print(os.path.islink(test_path))
print(os.path.realpath(test_path))

# 如果你还想获取元数据(比如文件大小或者是修改日期)，也可以使用 os.path 模块来解决：
print(os.path.getsize(test_path))
print(os.path.getmtime(test_path))
import time

print(time.ctime(os.path.getmtime(test_path)))

# 讨论
# 使用 os.path 来进行文件测试是很简单的。
# 在写这些脚本时，可能唯一需要注意的就是你需要考虑文件权限的问题，特别是在获取元数据时候。
# 比如：
# print(os.path.getsize("/User/guido/Desktop/foo.txt"))
# PermissionError
