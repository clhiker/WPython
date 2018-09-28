import math
from fractions import Fraction

def main():
    print(3/2)
    print(3//2)     #整除

    #分数
    x = Fraction(3, 5)
    y = Fraction(4, 3)
    print(x + y)
    print(x.numerator)      #分子
    print(x.denominator)        #分母

    #复数
    a = 3+4j
    b = 4+5j
    print(a+b)
    print(abs(a))       #复数的模
    print(a.imag)
    print(a.real)
    print(a.conjugate())    #共轭复数

    #精确度和舍入问题
    print(0.2+0.3)
    print(0.4-0.3)
    print(0.4-0.3 == 0.1)
    print(0.9-0.5)
    print(0.9-0.7)

    print("测试一下")
    x = 0.9
    y = 0.1
    for i in range(20):
        print(x-y)
        y += 0.1

    #差值低过0.4就会产生偏差！！！！
    #差值为负则普遍存在偏差
    print(abs(0.5-0.4-0.1) < 1e-6)

main()