import math
from functions import f3

### simpson 积分公式近似：[f(a)+ 2sum(f(x_2j))+ 4sum(f(x_2j-1))+ f(b)]
def Simpson(a,b,n):     # 输入：端点a, b；正偶数n
                        # 输出：积分后的近似值result   
    h = abs(a-b)/n      # 关于x增加的步长h

    # for even:
    x1 = 0
    for i in range(2,n,2):
        x1 += f3(a+i*h)
    # for odd:
    x2 = 0
    for i in range(1,n,2):
        x2 += f3(a+i*h)
    
    result = (f3(a)+ 2*x2+ 4*x1+ f3(b))*h/3.0
    return result

def test():
    n = 10000000
    a = 0
    b = 2

    result = Simpson(a,b,n)
    print(f'Simpson({a},{b},{n}):{result}.')

test()