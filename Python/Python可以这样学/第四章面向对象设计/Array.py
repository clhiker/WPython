from fractions import Fraction

def main():
    for i in range(100):
        print('hello world!')
def fushu():
    x = 1+2j
    y = 2+5j
    print(x+y)
def fenshu():
    x = Fraction(3, 5)
    y = Fraction(3, 7)
    print(x+y)
def dizhi():
    x = 18802
    print(id(x))
fushu()
fenshu()
dizhi()