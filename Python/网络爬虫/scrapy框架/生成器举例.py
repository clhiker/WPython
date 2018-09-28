import time
def gen(n):
    for i in range(n):
        yield i**2

def quickSquare(n):
    ls = (i**2 for i in range(n))
    return ls

def square(n):
    ls = [i**2 for i in range(n)]
    return ls

def main():
    begin = time.time()
    for i in square(100000000):
        pass
    print('花费了'+ str(time.time() - begin))

    start = time.time()
    for i in gen(100000000):
        pass
    print('花费了' + str(time.time() - start))

    begin = time.time()
    for i in quickSquare(100000000):
        pass
    print('花费了' + str(time.time() - begin))



if __name__ == '__main__':
    main()