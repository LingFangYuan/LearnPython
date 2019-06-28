import numpy as np
from 手写数字识别2 import get_data, init_network, predict


x, t = get_data()
network = init_network()
# W1, W2, W3 = network['W1'], network['W2'], network['W3']
# print(x.shape, x[0].shape)
# print(W1.shape, W2.shape, W3.shape)

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print('Accuracy:' + str(float(accuracy_cnt) / len(x)))
