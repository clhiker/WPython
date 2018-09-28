
from Stack import*

class Caculate:
    def __init__(self):
        self.str = ""
        self.inop = {""}
        self.outop = {""}

    def get_str(self):
        #self.str = input("请输入算式")
        self.str += "#"

    def define_op(self):
        self.inop = {"#": 0, "(": 1, "+": 3, "-": 3, "*": 5, "/": 5, ")": 8}
        self.outop = {"#": 0, "(": 8, "+": 2, "-": 2, "*": 4, "/": 4, ")": 1}

    def result(self):
        print(self.str)
        self.get_str()
        self.define_op()
        print(self.inop[self.str])

def main():
    '''c = Caculate()
    c.result()'''
    test = "1.2"
    hhda = test[0:3]
    print(float(hhda))

main()
