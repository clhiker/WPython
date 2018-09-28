from Stack import *

class Caculate:
    def __init__(self):
        self.str = ""
        self.inop = {""}
        self.outop = {""}

    def get_str(self):
        self.str = input("请输入算式\n")
        self.str += "#"

    def define_op(self):
        self.inop  = {"#" : 0, "(" : 1, "+" : 3, "-" : 3, "*" : 5, "/" : 5, ")" : 8}
        self.outop = {"#" : 0, "(" : 8, "+" : 2, "-" : 2, "*" : 4, "/" : 4, ")" : 1}

    def get_result(self):
        self.get_str()
        self.define_op()
        num = Stack()
        oper = Stack()
        oper.push("#")
        length = len(self.str)
        i=0
        while i < length:
            if(self.str[i].isdigit()):
                temp = i
                while (self.str[i] in self.inop) == False:
                    i += 1
                temp_num = self.str[temp:i]
                num.push(float(temp_num))
            else:
                temp1 = int(self.inop[oper.top()])
                temp2 = int(self.outop[self.str[i]])
                if(temp1 < temp2):
                    oper.push(self.str[i])
                elif(temp1 > temp2):
                    while temp1 > temp2:
                        op = oper.top()
                        oper.pop()
                        right = num.top()
                        num.pop()
                        left = num.top()
                        num.pop()
                        com = Compute(left, right, op)
                        num.push(com.compute())
                        temp1 = int(self.inop[oper.top()])
                        if(temp1 == temp2):
                            oper.pop()
                    oper.push(self.str[i])
                elif(temp1 == temp2):
                    oper.pop()
                i += 1
            if(oper.empty()):
                break
        print(num.top())

class Compute:
    def __init__(self, left=0, right=0, op=""):
        self.left = left
        self.right = right
        self.op = op

    def compute(self):
        if(self.op == "+"):
            return self.left+self.right
        elif(self.op == "-"):
            return self.left-self.right
        elif (self.op == "*"):
            return self.left * self.right
        elif (self.op == "/"):
            if(self.right != 0):
                return self.left / self.right
            else:
                return False

def main():
    caculater = Caculate()
    caculater.get_result()

main()