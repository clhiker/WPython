PI = 4
def add(a,b):
    return a+b

def future(p,r,m,t):
    return float(p*(1+r/m)**(m*r))

a=int(input())
b=int(input())
c=add(a,b)
print(c)
print(future(2,3,4,5))
print(PI)
