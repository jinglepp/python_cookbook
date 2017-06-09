# -*- coding: utf-8 -*-
# 问题
# 你想使用操作类文件对象的程序来操作文本或二进制字符串。

# 解决方案
# 使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据。比如：
import io

s = io.StringIO()
print(s.write("Hello World\n"))
print("This is a test", file=s)
print(repr(s.getvalue()))
s = io.StringIO("Hello\nWorld\n")
print(s.read(4))
print(s.read())
# io.StringIO 只能用于文本。如果你要操作二进制数据，要使用 io.BytesIO 类来代替。比如：
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())

# 讨论
# 当你想模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。
# 比如，在单元测试中，你可以使用 StringIO 来创建一个包含测试数据的类文件对象，
# 这个对象可以被传给某个参数为普通文件对象的函数。

# 需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。
# 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。
