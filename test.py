#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
print 'hello world!'
print '你好，世界！'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
print p.__score

# for x in range(1, 10):
#     for y in range(0, 10):
#         if x < y:
#             print x * 10 + y;

def average(*args):
    count = 0
    sum = 0.0
    for temp in args:
        sum += temp
        count +1
    if 0==count:
        return 0
    else:
        return sum/count

# print range(1,10)