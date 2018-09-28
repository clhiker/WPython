
#同时对多个变量进行赋值
def assignmentSomeElement():
    x, y, z = 1, 2, 3
    print(x, y, z)
    v_tuple = (False, 3.5, 'exp')
    (x, y, z) = v_tuple
    print(x, y, z)
    x, y, z = map(str, range(3))
    print(x, y, z)

#列表与字典的序列解包操作
def sequenceUnpacking():
    a = [1, 2, 3]
    b, c, d = a
    print(b)
    x, y, z = sorted([1, 2, 3])
    print(x)
    s = {'a':1, 'b':2, 'c':3}
    b, c, d = s.items()
    print(b)
    b,c,d = s.values()
    print(c)

#同时遍历多个序列
def visitSomeSequence():
    keys = ['a','b','c','d']
    values = [1,2,3,4]
    for k,v in zip(keys,values):
        print(k,v)

#序列解包对枚举操作
def visitEnum():
    x = ['a','b','c']
    for i,v in enumerate(x):
        print('The value on position {0} is {1}'.format(i,v))

#序列解包对字典操作
def visitDict():
    s = {'a':1,'b':2,'c':3}
    for k,v in s.items():
        print(k,v)


def main():
    #assignmentSomeElement()
    #sequenceUnpacking()
    #visitSomeSequence()
    #visitEnum()
    visitDict()

main()