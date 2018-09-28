def chaifen(n):
  print(n," = ",end=' ')
  list = []
  i = 2
  j = 0
  counter = 2
  for counter in range(2,n):
    if n%counter == 0:
      n = n/counter
      break;
  while n > 2:
    if n%i == 0:
      list.append(i)
      n = n/i
      i = 2
      j += 1
    i += 1
  print(counter,end=' ')
  for i in range(0,j):
    print('*',list[i],end=' ')

print("input a number:")
n = int(input())
counter = 0
for i in range(2,n):
  if n%i == 0:
      counter+=1
if counter != 0:
  print("n is not a sushu")
  chaifen(n) 
else:
  print("n is a sushu")


