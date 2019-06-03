import math
import numpy as np


def sigmoid(z):
    ' 激活函数'
    return 1 / (1 + math.e**(-z))


def s1(x, w, b):
    ' 运算'
    z = np.inner(np.append(x, 1), np.append(w, b))
    return sigmoid(z)


def s2(x):
    ' 输入层运算'
    return x


class Node(object):
    ' 神经元的数据节点'

    def __init__(self, data=np.NaN):
        self.data = data


class neure(object):
    ' 神经单元'

    def __init__(self, b, ntype):
        self.w = {}
        self.b = b
        self.ntype = ntype
        self.input = {}
        self.output = Node()

    def operation(self):
        ' 运算'

        w, i = self.dict2np()
        if self.ntype == 'input':
            self.output.data = s2(i)
        else:
            self.output.data = s1(i, w, self.b)

    def set_w(self, idx, n):
        self.w[idx - 1] = n

    def dict2np(self):
        if isinstance(self.input, dict):
            if len(self.input) != len(self.w):
                raise ValueError("输入数据的个数与权重的个数不同！")
        w_t = np.array([])
        input_t = np.array([])
        for i in range(len(self.input)):
            w_t = np.append(w_t, self.w[i + 1])
            input_t = np.append(input_t, self.input[
                                i + 1] if not isinstance(self.input[i + 1], Node) else self.input[i + 1].data)
        return w_t, input_t


class neural_network(object):
    ' 神经网络'

    def __init__(self, inp, mid, out):
        ' 建立所有的神经单元'
        self.inp_l = {}
        self.mid_l = {}
        self.out_l = {}
        for i in range(inp):
            self.inp_l[i + 1] = neure(1, ntype='input')
        for i in range(mid):
            self.mid_l[i + 1] = neure(1, ntype='middle')
        for i in range(out):
            self.out_l[i + 1] = neure(1, ntype='output')
        self.organize()

    def organize(self):
        ' 组织网络'
        for k_i, v_i in self.inp_l.items():
            v_i.w[k_i] = 1
            v_i.input[k_i] = np.NaN
            for k_m, v_m in self.mid_l.items():
                v_m.w[k_i] = 1
                v_m.input[k_i] = v_i.output
        for k_m, v_m in self.mid_l.items():
            for k_o, v_o in self.out_l.items():
                v_o.w[k_m] = 1
                v_o.input[k_m] = v_m.output

    def run(self, x):
        ' 运行网络'
        x = x.flatten()
        for k, v in self.inp_l.items():
            v.input[1] = x[k - 1]
            v.operation()
        for v in self.mid_l.values():
            v.operation()
        rs = {}
        for k, v in self.out_l.items():
            v.operation()
            rs[k] = v.output.data
        self.clear()
        return rs

    def clear(self):
        ' 清理神经单元的输出'

        for v in self.inp_l.values():
            v.data = np.NaN
        for v in self.mid_l.values():
            v.data = np.NaN
        for v in self.out_l.values():
            v.data = np.NaN


class neural_network_01(neural_network):
    ' 识别通过4x3像素的图像读取的手写数字0和1。其中像素是单色二值。'

    def __init__(self, inp, mid, out):
        ' 建立所有的神经单元'
        self.inp_l = {}
        self.mid_l = {}
        self.out_l = {}
        for i in range(inp):
            self.inp_l[i + 1] = neure(1, ntype='input')
        for i in range(mid):
            self.mid_l[i + 1] = neure(-10, ntype='middle')
        for i in range(out):
            self.out_l[i + 1] = neure(-4, ntype='output')
        self.organize()

    def organize(self):
        ' 组织网络, 设置权重。'
        for k_i, v_i in self.inp_l.items():
            v_i.w[1] = 1
            v_i.input[1] = np.NaN
            for k_m, v_m in self.mid_l.items():
                if (k_i, k_m) in [(4, 1), (7, 1), (5, 2), (8, 2), (6, 3), (9, 3)]:
                    v_m.w[k_i] = 5
                else:
                    v_m.w[k_i] = 1
                v_m.input[k_i] = v_i.output
        for k_m, v_m in self.mid_l.items():
            for k_o, v_o in self.out_l.items():
                if (k_m, k_o) in [(1, 1), (3, 1), (2, 2)]:
                    v_o.w[k_m] = 5
                else:
                    v_o.w[k_m] = 1

                v_o.input[k_m] = v_m.output

    def run(self, x):
        ' 运行网络'
        x = x.flatten()
        for k, v in self.inp_l.items():
            v.input[1] = x[k - 1]
            v.operation()
        for v in self.mid_l.values():
            v.operation()
        rs = {}
        for k, v in self.out_l.items():
            v.operation()
            rs[k] = v.output.data
        self.clear()
        return "识别为：0" if rs[1] > rs[2] else "识别为：1"


if __name__ == '__main__':
    x0 = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [1, 0, 1],
                   [0, 1, 0]])

    x1 = np.array([[0, 1, 0],
                   [0, 1, 0],
                   [0, 1, 0],
                   [0, 1, 0]])

    n1 = neural_network_01(12, 3, 2)
    print(n1.run(x0))
    print(n1.run(x1))
