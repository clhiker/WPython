import random
from functools import reduce

#增
def addElement():
    x = list(range(5))
    random.shuffle(x)
    print(x)
    x.append(5)
    print(x)
    x.insert(0, 10)
    print(x)
    x.extend([2, 32, 23])
    print(x)

    x += [0, 0, 0]
    print(x)
    x *= 2
    print(x)

#删
def delElement():
    x = list(range(10))
    random.shuffle(x)
    print(x)
    x.pop()
    print(x)
    x.pop(0)
    print(x)
    x.remove(4)
    print(x)
    del x[3]
    print(x)
    x.clear()
    print(x)

#统计
def Count():
    x = list(range(10))
    random.shuffle(x)
    print(x)
    print(x.count(3))   #统计某元素出现的个数
    print(x.index(3))   #某元素首次出现的索引,没有则抛出异常
    print(10 in x)
    print(2 in x)

#排序
def Sort():
    #原地排序
    x = list(range(10))
    random.shuffle(x)
    print(x)
    x.sort()    #默认为非递减
    print(x)
    x.reverse()
    print(x)
    x.sort(key=str)
    print(x)
    x.sort(key=int)
    print(x)
    x.sort(key=lambda item: len(str(item)), reverse=True)
    print(x)

    #异地排序
    x = list(range(5))
    random.shuffle(x)
    y = sorted(x)
    z = reversed(x)     #返回的是逆序的迭代对象
    print(x)
    print(y)
    print(z)
    z = list(reversed(x))
    print(z)

def add5(e):
    return e+5
def add(x, y):
    return x+y
#外置算法
def outOperator():
    x = list(range(10))
    random.shuffle(x)
    print(x)
    print(max(x, key=int))
    print(min(x, key=str))
    print(sum(x))
    print(len(x))

    #更高级的外置函数
    #组合函数
    y = list(zip(x, [1]*11))
    print(y)
    z = list(zip(range(1, 4), "hhda"))
    print(z)

    #枚举函数
    a = list(enumerate(x))      #前一项为序号从0开始，后一项为值
    print(a)

    #映射
    b = list(map(str, range(6)))
    print(b)
    b = list(map(add5, range(7)))
    print(b)
    b = list(map(lambda x,y:x+y, range(5), range(4, 9)))
    print(b)

    #累积作用函数
    c = list(range(10))
    random.shuffle(c)
    print(reduce(add, c))
    print(reduce(lambda x,y:x+y, c))

def main():
    #addElement()
    #delElement()
    #Count()
    #Sort()
    outOperator()
main()