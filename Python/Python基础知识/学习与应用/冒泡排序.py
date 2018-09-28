inf = []
n = int(input("enter the number:"))
print("input the information")

for i in range(0,n):
  num=int( input())
  inf.append (num)
print("the former:")
print(inf[:])

for i in range(0,n-1):
  for j in range(0,n-i-1):
    if inf[j] > inf[j+1]:
      temp = inf[j]
      inf[j] = inf[j+1]
      inf[j+1] = temp
print("the later:")      
print(inf)
