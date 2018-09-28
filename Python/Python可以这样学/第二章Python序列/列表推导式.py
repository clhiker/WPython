import random
import os
import math

#初始测试
def Test():
    x = [random.randint(1, 100)for i in range(10)]
    print(x)
    x = [e**e for e in range(10)]
    print(x)

#列表内嵌套循环
def Clear():
    a = [[1, 2, 3], [4, 5], [6]]
    a = [sec for fir in a for sec in fir]
    print(a)

#过滤不符合条件的元素
def Filter():
    #同一文件夹下的快速查找形成的列表
    b = [filename for filename in os.listdir('.')if filename.endswith('.py')]
    print(b)

    #使用多个循环
    b = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(b)

#矩阵转置
def Matrix():
    c = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    #列表推导式法
    c = [[row[i] for row in c]for i in range(4)]
    print(c)

    #解析列表推导式
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    result = []
    for i in range(len(matrix)):
        temp = []
        for row in matrix:
            temp.append(row[i])
        result.append(temp)
    print(result)

    #zip&list 法
    c = list(map(list, zip(*c)))
    print(c)

#推导式中使用函数或者复杂表达式
def f(v):
    if v%2 == 0:
        v = v**2
    else:
        v += 1
    return v
def useFun():
    #使用函数
    print([f(v) for v in [2,3,4,-1] if v>0 ])
    #使用复杂表达式
    print([v**2 if v%2==0 else v+1 for v in [2,3,4,-1] if v>0])

#迭代文件对象
def iterateFiles():
    fp = open('C:\cl.txt', 'r')
    print(line for line in fp)
    fp.close()

#举例
def Example():
    f = [p for p in range(2, 100)if 0 not in [p%d for d in range(2, int(pow(p,1/2))+1)]]
    print(f)
def main():
    #Test()
    #Clear()
    #Filter()
    #Matrix()
    #useFun()
    #iterateFiles()
    Example()

main()
