import numpy as np

def Sigmoid(x):
    return 1.0/(1+np.exp(-x))

def main():
    x = int(input("请输入x\n"))
    print(Sigmoid(x))

main()