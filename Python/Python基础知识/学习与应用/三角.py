n=int(input("shuru shu ju:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('@',end=" ")
    print("\n")
m=int(input("shuru new shu ju:"))
for i in range(m+1,1,-1):
    for j in range(i,1,-1):
        print('#',end=" ")
    print("\n")
p=int(input("shuru new shu ju:"))
for i in range(p+1,1,-1):
    for j in range(1,p+2-i):
        print(' ' ,end=" ")
    for m in range(i,1,-1):
        print('$',end=" ")
    print("\n")
