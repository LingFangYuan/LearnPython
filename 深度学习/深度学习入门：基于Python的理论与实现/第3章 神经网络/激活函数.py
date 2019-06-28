import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np


def set_func(x):
    '''
    阶跃函数
    '''
    return np.array(x > 0, dtype=np.int)


def set_f(s):
    if s > 0:
        return 1
    else:
        return 0


def sigmoid(x):
    '''
    sigmoid函数
    '''
    return 1 / (1 + np.exp(-x))


def relu(x):
    '''
    ReLU函数
    '''
    return np.maximum(0, x)


def identity_func(x):
    '''
    恒等函数
    '''
    return x


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc')

if __name__ == '__main__':
    set_func1 = np.frompyfunc(set_f, 1, 1)
    x = np.arange(-5.0, 5.0, 0.1)
    y1 = set_func1(x)
    # y1 = set_func(x)
    y2 = sigmoid(x)
    y3 = relu(x)
    plt.plot(x, y1, label='阶跃函数')
    plt.plot(x, y2, label='sigmoid函数', linestyle='--')
    plt.plot(x, y3, label='ReLU函数', linestyle='-.')
    # plt.ylim(-0.1, 1.1)
    plt.xlabel('X', fontproperties=font)
    plt.ylabel('Y', fontproperties=font)
    plt.title('激活函数', fontproperties=font)
    plt.legend(prop=font)
    plt.show()
