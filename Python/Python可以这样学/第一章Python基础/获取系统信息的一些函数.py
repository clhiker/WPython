import platform
import sys

#获取版本及版本信息
def getVerson():
    a = platform.python_version()
    print(a)
    b = sys.version
    c = sys.winver
    d = sys.version_info
    e = sys.executable
    print(b)
    print(c)
    print(d)
    print(e)

#查看操作系统
def System():
    f = platform.win32_ver()
    g = platform.version()
    h = platform.machine()
    i = platform.python_compiler()
    print(f)
    print(g)
    print(h)
    print(i)

def main():
    print("版本信息")
    getVerson()
    print("操作系统")
    System()

main()
