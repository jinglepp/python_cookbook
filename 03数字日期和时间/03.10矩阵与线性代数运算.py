# -*- coding: utf-8 -*-
# 执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等等。
# 解决方案
# NumPy 库有一个矩阵对象可以用来解决这个问题。

# 矩阵类似于3.9小节中数组对象，但是遵循线性代数的计算规则。
# 下面的一个例子展示了矩阵的一些基本特性：
import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
# 转置
print(m.T)
# 求逆
print(m.I)
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)
# 可以在 numpy.linalg 子包中找到更多的操作函数，比如：
import numpy.linalg

# 行列式
print(numpy.linalg.det(m))

# Eigenvalues特征值
print(numpy.linalg.eigvals(m))
# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
print(x)
print(m * x)
print(v)

# 讨论
# 很显然线性代数是个非常大的主题，已经超出了本书能讨论的范围。
# 但是，如果你需要操作数组和向量的话， NumPy 是一个不错的入口点。
# 可以访问 NumPy 官网 http://www.numpy.org 获取更多信息。
