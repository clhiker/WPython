import numpy
def main():
    x = numpy.ones(3)
    m = numpy.eye(3)*3
    print(x)
    print(m)
    print(x@m)
main()