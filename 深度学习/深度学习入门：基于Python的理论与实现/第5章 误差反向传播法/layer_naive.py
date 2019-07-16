

class MulLayer(object):
    '''
    乘法层
    '''

    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        '''
        前向传播
        '''
        self.x = x
        self.y = y
        out = self.x * self.y

        return out

    def backward(self, dout):
        '''
        反向传播
        '''
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy


class AddLayer(object):

    def __init__(self):
        pass

    def forward(self, x, y):
        out = x + y
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy


if __name__ == '__main__':
    # apple = 100
    # apple_num = 2
    # tax = 1.1

    # # mul_layer
    # mul_apple_layer = MulLayer()
    # mul_tax_layer = MulLayer()

    # # forward
    # apple_price = mul_apple_layer.forward(apple, apple_num)
    # price = mul_tax_layer.forward(apple_price, tax)

    # print(price)

    # # backward
    # dprice = 1
    # dapple_price, dtax = mul_tax_layer.backward(dprice)
    # dapple, dapple_num = mul_apple_layer.backward(dapple_price)

    # print(dapple, dapple_num, dtax)

    # buy_apple_orange

    apple_price = 100
    orange_price = 150
    apple_qty = 2
    orange_qty = 3
    tax = 1.1

    # layer
    mul_apple_layer = MulLayer()
    mul_orange_layer = MulLayer()
    add_sum_layer = AddLayer()
    mul_tax_layer = MulLayer()

    # forward
    apple_amt = mul_apple_layer.forward(apple_price, apple_qty)
    orange_amt = mul_orange_layer.forward(orange_price, orange_qty)
    sum_amt = add_sum_layer.forward(apple_amt, orange_amt)
    price = mul_tax_layer.forward(sum_amt, tax)

    print(price)

    # backward
    dprice = 1
    dsum, dtax = mul_tax_layer.backward(dprice)
    dapple_amt, dorange_amt = add_sum_layer.backward(dsum)
    dapple_price, dapple_qty = mul_apple_layer.backward(dapple_amt)
    dorange_price, dorange_qty = mul_orange_layer.backward(dorange_amt)

    print(dapple_price, dapple_qty)
    print(dorange_price, dorange_qty)
    print(dtax)
    print()
    print(dsum, dapple_amt, dorange_amt)
