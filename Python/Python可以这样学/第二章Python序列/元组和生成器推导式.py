#元组 == 常量列表
import random

#元组是限制式容器
#元组是不可变序列，一旦创建没有任何方法修改元组中的值
#故此无法增添和删除
def buildTuple():
    x = (1,2,3)
    print(x)
    print(type(x))
    x1 = (3)
    x2 = (3,)
    x3 = ()
    x4 = tuple()
    x5 = tuple(range(10))
    print(x5)

#元组的切片仅限于访问
def Visit():
    x = ([1, 2], 3)
    x[0][0] = 10        #元组中的列表支持修改
    print(x)
    x[0].append(3)
    print(x)

#生成器推导式
#注意生成的是生成器对象
def generatorDerivation():
    gd = ((i+2)**2 for i in range(10))
    print(gd)
    tg = tuple(gd)
    lg = list(gd)       #对象使用过后无元素了
    print(tg)
    print(lg)

    gd2 = ((i+2)**2 for i in range(10))
    print(gd2.__next__())
    print(gd2.__next__())
    print(next(gd2))
    print(list(gd2))        #能形成列表的也只是剩下的了

    gd3 = ((i+2)**2 for i in range(10))
    for i in gd3:
        print(i, end=" ")

def main():
    #buildTuple()
    #Visit()
    generatorDerivation()

main()