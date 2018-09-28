import sys
import chardet

def getCode(path):
    f = open(path, 'rb')
    data = f.read()
    print(chardet.detect(data))

print(sys.getdefaultencoding())
path1 = "D:/test/1.java"
path2 = "D:/test/2.java"
print()
getCode(path1)
getCode(path2)