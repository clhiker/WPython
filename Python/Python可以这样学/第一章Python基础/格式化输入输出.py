import sys
import pprint

def comonIO():
    print(1, 3, 5, 7, sep='\t')
    print(2, 4, 6, 8, end="\n")

    #Python有很方便的文件操作
    #example
    fp = open("C:\\cl.txt", 'a+')
    print("lihuizhizhang", file=fp)
    fp.close()

def stadIO():
    x = sys.stdin.read(5)
    print(x)
    y = sys.stdin.readline()
    print(y)
    z = sys.stdin.readline(4)
    print(z)

def prettyPrinter():
    a = "sdfaaaaaafdsaaaaaaahreaghergds"
    b = ['wer', 'ewrq', 'dfsg']
    pprint.pprint(a, width=10)
    pprint.pprint(b, width=67)

def main():
    #comonIO()
    #stadIO()
    prettyPrinter()

main()