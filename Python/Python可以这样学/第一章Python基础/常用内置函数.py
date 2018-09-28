
def Type():
    x = 3
    print(type(x))      #获取类型
    print(isinstance(x, int))    #确定类型

def Name():
    print('3ag'.isidentifier()) #判断是否为可用变量名
    print('--e'.isidentifier())

def numberTypeChange():
    x = 12
    print(bin(x))   #二进制
    print(hex(x))   #十六进制
    print(oct(x))   #八进制
    print(int(x))   #整数且转换为十进制
    print(bool(x))
    print(chr(x))
    print(ord("3"))     #“ ”!!!!!
    print(str(x))

    y = "3+4"
    print(eval(y))      #对字符串求值函数

    print(pow(2, 3) == 2**3)

    print(round(4.23))      #四舍五入

def Important():
    print("三个重要的内置函数")
    zip()
    reduce()
    map()

def main():
    Type()
    Name()
    numberTypeChange()
    print(help('math'))

main()

