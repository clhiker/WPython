from enum import Enum

class Color(Enum):
    red = 1
    blue = 2
    green = 3

def main():
    print(Color.red)
    print(type(Color.red))
    x = dict()
    x[Color.red] = 'red'
    print(x)
    print(Color(2))
    print(Color['red'])
    r = Color.red
    print(r.name)
    print(r.value)
    print(list(Color))

main()
