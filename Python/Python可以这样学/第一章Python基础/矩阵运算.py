import numpy

def main():
    x = numpy.ones(3)
    m = numpy.eye(3)    #单位矩阵
    m *= 3              #矩阵数乘
    print(x)
    print(m)
    m = m @ x           #矩阵乘法
    print(m)

main()