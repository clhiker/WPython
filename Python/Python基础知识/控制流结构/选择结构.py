print(1,end=' ')
for i in range(1,10):
    print(i,end=' \t')
print("\n")
for i in range(1,10):
    print(i,end=' ')
    for j in range(1,i+1):
        print(i*j,end=' \t')
    print("\n")    
