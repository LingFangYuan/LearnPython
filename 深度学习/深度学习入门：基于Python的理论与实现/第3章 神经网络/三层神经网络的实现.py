import numpy as np
from 激活函数 import sigmoid, identity_func


# x = np.array([1.0, 0.5])
# w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
# b1 = np.array([0.1, 0.2, 0.3])
# print(x.shape, w1.shape, b1.shape)

# a1 = np.dot(x, w1) + b1
# z1 = sigmoid(a1)
# print(a1)
# print(z1)

# w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
# b2 = np.array([0.1, 0.2])
# a2 = np.dot(z1, w2) + b2
# z2 = sigmoid(a2)
# print(z1.shape, w2.shape, b2.shape)
# print(a2)
# print(z2)

# w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
# b3 = np.array([0.1, 0.2])
# a3 = np.dot(z2, w3) + b3
# y = identify_func(a3)
# print(y)

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b2']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_func(a3)

    return y


if __name__ == '__main__':
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward(network, x)
    print(y)
