import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from 数值微分的例子 import numerical_diff


def func_2(x):
    return x[0]**2 + x[1]**2


def func_tmp1(x0):
    return x0 ** 2 + 4.0 ** 2


def func_tmp2(x1):
    return 3.0 ** 2 + x1 ** 2


if __name__ == '__main__':
    x0 = np.arange(-3, 3, 0.1)
    x1 = np.arange(-3, 3, 0.1)
    x0, x1 = np.meshgrid(x0, x1)
    y = func_2(np.array([x0, x1]))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x0, x1, y)
    ax.set_xlabel('x0')
    ax.set_ylabel('x1')
    ax.set_zlabel('f(x)')
    plt.show()

    # print(numerical_diff(func_tmp1, 3))
    # print(numerical_diff(func_tmp2, 4))
