# 数值积分.py 所需要的函数

import math
def f1(x): #定义函数f(x) = x**2;用来测试一阶导数
    f = math.log(x)
    return f

def f2(x):  #定义函数f1(x) = xe**x;用来测量二阶导数
    f = x* math.e**x
    return f

def f3(x):
    f = x**2
    return f