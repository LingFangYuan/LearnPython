import numpy as np
import matplotlib.pyplot as plt


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def f(x):
    return 0.01 * x ** 2 + 0.1 * x


def f1(x):
    return 0.02 * x + 0.1


def tangent_line(f, x):
    d = numerical_diff(f, x)
    y = f(x) - d*x
    print('b', y)
    return lambda t: d*t + y


if __name__ == '__main__':
    print(numerical_diff(f, 5), f1(5))
    print(numerical_diff(f, 10), f1(10))
    x = np.arange(0, 20, 0.1)
    tf1 = tangent_line(f, 5)
    tf2 = tangent_line(f, 10)
    y1 = f(x)
    y2 = tf1(x)
    y3 = tf2(x)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.show()
