# -*- coding: utf-8 -*-
def findMinAndMax1(L):
    min = None
    max = None
    for i in L:
        if min == None or max == None:
            min = i
            max = i
        elif min > i:
            min = i
        elif max < i:
            max = i
        else:
            pass
    return min, max
    
def findMinAndMax(L):
    mi = None if len(L)==0 else min(L)
    ma = None if len(L)==0 else max(L)
    return mi, ma

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')