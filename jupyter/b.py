def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
    
def fact_iter(num, product=1):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
    
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
        
def trim(s):
    if s[:1] == ' ':
        s = s[1:]
    elif s[-1:] == ' ':
        s = s[:-1]
    else:
        return s
    return trim(s)

if __name__ == "__main__":
    print("fact(10):",fact(10))
    print("fact_iter(10):", fact_iter(10))
    move(3, 'A', 'B', 'C')

    # 测试:
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
        