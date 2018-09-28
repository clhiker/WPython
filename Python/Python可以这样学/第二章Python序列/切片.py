import random
#双切片
def doubleSection():
    a_list = [3,4,5,6,7,9,11,13,15,17]
    a = a_list[::]
    print(a)
    b = a_list[::-1]
    print(b)
    c = a_list[::2]
    print(c)
    d = a_list[1::2]
    print(d)

#单切片
def singleSection():
    a_list = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
    a = a_list[3:6]
    print(a)
    b = a_list[:100]
    print(b)

#增删改查
def Operator():
    #增改
    a_list = [3, 5, 7]
    a = a_list[len(a_list):]
    print(a)
    a_list[len(a_list):] = [9]
    print(a_list)
    a_list[:3] = [1, 2, 3]
    print(a_list)
    a_list[:3] = []
    print(a_list)

    c = list(range(10))
    print(c)
    c[::2] = [0] * (len(c)//2)
    print(c)

    #删
    del c[::3]
    print(c)

#切片返回的是列表元素的浅复制
def Copy():
    a = [3, 5, 7]
    b = a
    b[1] = 1        #修改b的同时修改了a
    print(a)
    print(b)
    print(a is b)
    c = a[::]
    print(c)
    print(a == c)
    print(a is c)
    print(id(a), "\t" ,id(b) ,"\t", id(c))
    c[1] = 10
    print(c)

    x = [[1], [2], [3]]
    y = x[:]
    print(x)
    print(y)
    y[0] = 4
    print(x)
    print(y)
    z = x[::]
    print(z)
    z[1].append(10)
    print(x)
    print(z)

def main():
    #doubleSection()
    #singleSection()
    #Operator()
    Copy()

main()