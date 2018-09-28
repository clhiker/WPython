def f():
    a, b = 1, 1
    while True:
        yield a     #使用yield创建可迭代的生成器对象
        a, b = b, a+b

def main():
    a = f()
    for i in range(10):
        print(a.__next__(), end=" ")

main()
