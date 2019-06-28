import numpy as np
import os
import sys
sys.path.append(os.pardir)
from dataset.mnist import load_mnist


def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


def cross_entropy_error(y, t):
    '''
    on_hot_lable:True
    '''
    delta = 1e-7
    if y.ndim == 1:
        t == t.reshape(1, t.size)
        y == y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + delta)) / batch_size


def cross_entropy_error1(y, t):
    '''
    one_hot_label:False
    '''
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


if __name__ == '__main__':
    # t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ])
    # y = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
    # print(mean_squared_error(y, t), cross_entropy_error(y, t))
    # y = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])
    # print(mean_squared_error(y, t), cross_entropy_error(y, t))
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize=True, one_hot_label=True)
    print(x_train.shape)
    print(t_train.shape)
    print(t_train[0])
    train_size = x_train.shape[0]
    batch_size = 10
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    print(batch_mask)
    print(x_batch)
    print(t_batch)
