list1 = []
print("input number:")
for i in range(10):
  num = int(input())
  list1.append(num)
average = sum(list1)/10
counter = 0
for i in range(10):
  if list1[i] > average:
    counter += 1
print("there",end=' ')
print(counter,end=' ')
print("number bigger than average")

