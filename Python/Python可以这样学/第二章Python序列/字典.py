#字典是无序可变序列
#键具有不可变不重复性
#当对字典进行迭代时，默认遍历的是“键”！！

def buildDic():
    #zip法建立
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    dic = dict(zip(keys, values))
    print(dic)

    #dict法建立
    d = dict(name = 'lihui', age = 20)
    print(d)

    #修改值
    adict = dict.fromkeys(['lihui', 'zhoujy', 'huangjh'])
    print(adict)
    adict['lihui'] = "zhizhang"
    print(adict)

def Operator():
    #update法添加键值
    adict = dict.fromkeys(['lihui', 'zhoujy', 'huangjh'])
    print(adict.items())
    adict.update({'cl':123})
    print(adict)

    #删除键
    del adict['huangjh']
    print(adict)
    adict.popitem()
    print(adict)
    adict.pop('zhoujy')     #弹出必须要有相对的键
    print(adict)
    adict.clear()
    print(adict)

def commonVisit():
    keys = ['lihui', 'zhoujy', 'huangjh', 'cl']
    values = [1, 2, 3, 4]
    adict = dict(zip(keys, values))

    #1键值对
    for i in adict.items():
        print(i, end=" ")
    print()

    #键
    for i in adict.keys():
        print(i, end=" ")
    print()

    #值
    for i in adict.values():
        print(i, end=" ")
    print()


#安全访问字典
def safeVisit():
    adict = dict.fromkeys(['lihui', 'zhoujy', 'huangjh'])

    #法一错误抛出法
    try:
        print(adict['cl'])
    except:
        print('no exit!')

    #法二get法
    print(adict.get('lihui', 'no exit'))
    print(adict.get('cl', 'no exit'))

    #法三setdefault法
    print(adict.setdefault('lihui', 'zhizhang'))
    print(adict.setdefault('cl', 'hhda'))
    print(adict)

def main():
    #buildDic()
    #Operator()
    commonVisit()
    #safeVisit()

main()
