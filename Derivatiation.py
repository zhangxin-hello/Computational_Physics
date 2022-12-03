import numpy as np
from functions import f1,f2

### for 一阶导数：三点公式（2种）；五点公式（2种）

# 三点公式：
#  1.f'(x0) = [-3f(x0)+4f(x0+h)-f(x0+2h)]/(2h)近似；当x0为左端点时，取h>0,右端点时取h<0.
#  2.f'(x0) = [f(x0+h)-f(x0-h)]/(2h)近似；此时x0为中间点

def tri_1(x0,h):    #第一种三点公式：
    result = (-3*f1(x0)+4*f1(x0+h)-f1(x0+2*h))/(2*h)
    return result
def tri_2(x0,h):    #第二种三点公式：
    result = (f1(x0+h)-f1(x0-h))/(2*h)
    return result

# 五点公式类似三点公式：
# 1.f'(x0) = [-25(fx0)+48f(x0+h)-36f(x0+2h)+16f(x0+3h)-3f(x0+4h)]/(12h)  近似：当x0为左端点时，取h>0;x0为右端点时，取x0<0; 
# 2.f'(x0) = [f(x0-2h)-8f(x0-h)+8f(x0+h)-f(x0+2h)]/(12h) 近似：x0为中间点

def fif_1(x0,h):    #第一种五点公式：
    result = (-25*f1(x0)+48*f1(x0+h)-36*f1(x0+2*h)+16*f1(x0+3*h)-3*f1(x0+4*h))/(12*h)
    return result
def fif_2(x0,h):
    result = (f1(x0-2*h)-8*f1(x0-h)+8*f1(x0+h)-f1(x0+2*h))/(12*h)
    return result

### for 二阶导数：
# 1.f''(x0) = [f(x0-h)-2f(x0)+f(x0+h)]/(h**2)
def second_derivative(x0,h):
    result = (f2(x0-h)-2*f2(x0)+f2(x0+h))/(h**2)
    return result

def test():                 #使用方法如下：
    # result = tri_1(1.8,0.000001)
    # print(f'tri_1(1.8,0.000001):{result}.')
    # result = tri_2(1.8,0.000001)
    # print(f'tri_2(1.8,0.000001):{result}.')
    # result = fif_1(1.8,0.000001)
    # print(f'fif_1(1.8,0.000001):{result}.')
    # result = fif_1(1.8,0.000001)
    # print(f'fif_1(1.8,0.000001):{result}.')

    # result = second_derivative(2.0,0.1)
    # print(f'second_derivative(2.0.1):{result}.')

    print('it end.')

test()