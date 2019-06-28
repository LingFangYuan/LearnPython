import numpy as np
from 激活函数 import softmax


a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)
sum_exp_a = np.sum(exp_a)
print(sum_exp_a)
y = exp_a / sum_exp_a
print(y)

y1 = softmax(a)
print(y1, np.sum(y1))
