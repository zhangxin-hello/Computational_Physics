import math
from functions import f3

### T_2n = T_n /2.0 + sum_0^{n-1}(f(x_(j+h/2)))

#输入：积分前后点：a，b；误差：c。
#输出：积分近似结果。
def main(a,b,c):
    h = abs(b-a)
    t1 = (f3(a)+f3(b))*h/2.0

    while(1):
        s = 0
        x = a + h/2.0
        while(1):
            s = s + f3(x)
            x = x + h
            if x > b or x == b:
                break
        t2 = t1 /2.0 + s *h /2.0
        if abs(t2-t1)<c:
            return t2
            break
        # 将此时的t2作为新的t1；h对半，进行新的一次运算 
        h = h/2.0
        t1 =t2

def test():
    a = 0
    b = 2
    c = 0.000001

    result = main(a,b,c)
    print(f'main({a},{b},{c}):{result}.')

test()