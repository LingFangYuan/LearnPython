import numpy as np
from 偏导数 import func_2
import matplotlib.pyplot as plt


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val

    return grad


def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append(x.copy())
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)


if __name__ == '__main__':
    # print(numerical_gradient(func_2, np.array([2.4-0.48-0.384-0.3072, 3.2-0.64-0.512-0.4096])))
    # print(numerical_gradient(func_2, np.array([0.0, 2.0])))
    # print(numerical_gradient(func_2, np.array([1.0, 0.0])))

    init_x = np.array([-3.0, 4.0])
    x, x_history = gradient_descent(
        func_2, init_x=init_x, lr=0.1, step_num=100)
    plt.plot(x_history[:, 0], x_history[:, 1], 'o')
    plt.plot([-5, 5], [0, 0], '--b')
    plt.plot([0, 0], [-5, 5], '--b')
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.show()
