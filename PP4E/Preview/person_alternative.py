#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
person类的替代实现，包含数据、行为和运算符重载（未用于对象的持久储存）
'''

class Person(object):
    '''
    一般person:数据+逻辑
    '''

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.apge = age
        self.pay = pay
        self.job =job
    
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return ('<%s => %s: %s, %s>' %
                (self.__class__.__name__, self.name, self.job, self.pay))

class Manager(Person):
    '''
    带有自定义加薪的person
    继承了通用的 lastname, str
    '''

    def __init__(self, name, age, pay):
        super().__init__(name, age, pay, job='manager')

    def giveRaise(self, percent, bonus=0.1):
        super().giveRaise(percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jones', 47, 40000, 'hardware')
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        obj.giveRaise(.1)
        print(obj)
