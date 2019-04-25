def power(x, n=2):
    return x ** n
 
def calc(*n):
    sum = 0
    for i in n:
        sum = sum + i * i
    return sum
    
def product(*args, **kw):
    if len(args) == 0 and len(kw) == 0:
        raise TypeError
    pro = 1
    for i in args:
        if not isinstance(i, (int,float)):
            raise TypeError("出现非数字！")
        pro = pro * i
    for i in kw:
        if not isinstance(i, (int,float)):
            raise TypeError("出现非数字！")
        pro = pro * kw[i]
    return pro

if __name__ == "__main__":
    number = None
    while not isinstance(number, (int, float)):
        try:
            number = float(input("请输入一个数字："))
            break
        except ValueError:
            print("不能输入一个非数字！")
            
    number = float(number)
    rs = power(number)
    print("%f 的 %d 次方是: %f" % (number, 2, rs))
    print("calc(1,2,3):",calc(1, 2, 3))


    # 测试
    print('product(5) =', product(5))
    print('product(5, 6) =', product(5, 6))
    print('product(5, 6, 7) =', product(5, 6, 7))
    print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
    if product(5) != 5:
        print('测试失败!')
    elif product(5, 6) != 30:
        print('测试失败!')
    elif product(5, 6, 7) != 210:
        print('测试失败!')
    elif product(5, 6, 7, 9) != 1890:
        print('测试失败!')
    else:
        try:
            product('a')
            print('测试失败!')
        except TypeError as e:
            print('测试成功!', e)
        finally:
            print("--------------------")