import time
import random
#无序不重复可变序列

#建立字典
def buildSet():
    a_set = {}
    b = {1, 2, 3}
    c = set(range(10))
    d = set([1, 2, 3])
    print(d)

#效率测试
def Test():
    x = list(range(10000))
    y = set(range(10000))
    z = dict(zip(range(10000),range(10000)))
    r = random.randint(0, 9999)
    start = time.time()
    for i in range(99999):
        r in x
    print('list, time used:', time.time()-start)

    start = time.time()
    for i in range(99999):
        r in y
    print('set, time used:', time.time() - start)

    start = time.time()
    for i in range(99999):
        r in z
    print('dict, time used:', time.time() - start)
    #由此可见，随着序列的增长，元组，字典的效率要远高于列表

#增删改查
def Operator():
    #增
    s = set(range(5))
    print(s)
    s.add(33)
    print(s)
    s.update({2, 23})       #合并集合
    print(s)

    #删
    s.discard(5)    #删除指定元素，没有则不操作
    print(s)
    s.remove(3)     #删除指定元素，没有则抛出异常
    print(s)
    s.pop()         #弹出集合首部元素
    print(s)
    s.clear()
    print(s)

#集合运算
def setOperation():
    a = set([8,9,10,11,12,13])
    b = {0,1,2,3,7,8}
    #并集
    print(a | b)
    print(a.union(b))
    #交集
    print(a & b)
    print(a.intersection(b))
    #差集
    print(a.difference(b))
    print(a - b)
    #对称差集
    print(a.symmetric_difference(b))
    print(a ^ b)
    #测试子集
    print(a.issubset(b))
    print(b.issubset(a))
    #集合比较  包含关系
    print(a>b)
    print(a<b)
    print(a == b)

#集合不重复性
def noRepeat():
    #自写函数验证
    list_random = [random.choice(range(1000)) for i in range(100)]
    no_repeat = []
    for i in list_random:
        if i not in no_repeat:
            no_repeat.append(i)

    print(len(list_random))
    print(len(no_repeat))

    #集合自带函数
    new_set = set(list_random)
    print(len(new_set))

#random模块自带的不重复元素函数
def getNoRepeat():
    s = random.sample(range(1000), 20)
    print(s)

#集合推导式
def setDeduction():
    x = {i.strip() for i in ('he', 'she', 'I')}
    print(x)
    y = {random.randint(1, 500) for i in range(10)}
    print(y)
    z = {str(i) for i in range(10)}
    print(z)


def main():
    #buildSet()
    #Test()
    #Operator()
    #setOperation()
    #noRepeat()
    #getNoRepeat()
    setDeduction()

main()
