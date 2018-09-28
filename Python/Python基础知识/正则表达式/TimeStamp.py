import time

def main():
    t1 = time.time()
    for i in range(10000):
        for j in range(10000):
            pass
    t2 = time.time()
    print(t2-t1)

main()
