
def main():
    x = 3
    print(id(x))
    y = x
    print(id(y))
    #结果二者指向同一处地址

    x += 6
    print(id(x))
    print(id(y))    #结果y的地址并未发生变化
    #即Python中修改变量值的操作并非是修改值而是修改应用

    #Python采用的是基于值的内存管理方式
    #即多个变量指向同一块内存地址
    print("\n典例")

    a = [1, 1, 1]
    for i in range(3):
        print(id(a[i]))

main()