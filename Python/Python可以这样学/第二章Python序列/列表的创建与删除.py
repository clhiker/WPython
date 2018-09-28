import random
def Create():
    x = list(range(1, 10, 3))
    print(x)
    y = list("lihuizhizhang!")
    print(y)

    #字典与列表的转换
    a = {1:'a', 2:'b', 3:'c'}
    print(list(a))
    print(list(a.items()))

def Visit():
    #逆序访问
    n = list(range(10))
    random.shuffle(n)
    print(n)
    for i in range(1, 11):
        print(n[-i],end=" ")

def Delete():
    x = list(range(5))
    print(x)
    del x[3]
    print(x)

def main():
    Delete()
main()
