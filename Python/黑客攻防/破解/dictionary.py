import itertools as its
import time
def main():
    a = time.time()
    word = "abcdefghijklmnopqrstuvwxyz"
    r = its.product(word, repeat=6)
    dic = open("dictionary.txt", "a")
    for i in r:
        dic.write("".join(i))
    b = time.time()
    print(b-a)
    dic.close()

main()