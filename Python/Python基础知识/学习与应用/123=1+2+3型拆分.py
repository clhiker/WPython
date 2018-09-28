def chaifen(n):
  list1 = []
  counter = 0
  while n > 0:
    num = n % 10
    n = int(n / 10)
    counter +=1
    list1.append(num)
  print(list1[0:3:-1])
print("input a number")
n = int(input())
chaifen(n)

  
