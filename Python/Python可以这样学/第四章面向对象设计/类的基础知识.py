#第一个类
class Car():
    def infor(self):
        print("This is a car")

#类内注释
class Tree:
    '''This is a tree'''
    pass

#私有共有成员
class A:
    def __init__(self, value1=0, value2=0):
        self._value1 = value1
        self.__value2 = value2

    def setValue(self,value1,value2):
        self._value1 = value1
        self.__value2 = value2

    def show(self):
        print(self._value1)
        print(self.__value2)


#动态增加数据成员
class MyCar:
    price = 100000              #属于类的数据成员
    def __init__(self, c):
        self.color = c          #属于对象的数据成员

def Test():
    car1 = MyCar("red")
    car2 = MyCar("blue")
    print(car1.color, MyCar.price)

    MyCar.price = 11000     #修改类的数据成员
    MyCar.name = 'QQ'       #增加类的属性
    car1.color = 'yellow'

    print(car1.price, car1.color, MyCar.name)
    print(car2.price, car2.color, MyCar.name)

def main():
    car = Car()
    car.infor()
    print(isinstance(car, Car))
    print(Tree.__doc__)         #输出注释
    a = A()
    print(a._value1)
    print(a._A__value2)         #私有成员的调用方法
    Test()

main()