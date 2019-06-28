import numpy as np


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
print(c)
print('------------')
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])
c = np.dot(a, b)
print(a.shape, b.shape)
print(c)
print('------------')

x = np.array([1, 2])
w = np.array([[1, 3, 5], [2, 4, 6]])
y = np.dot(x, w)
print(x.shape, w.shape)
print(y)
