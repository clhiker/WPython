def main():
  list2 =[]
  add = 0
  for num in range(100,10000):
   list2=chaifen(num,weishu(num))
   for i in range(weishu(num)):
      add = int(list2[i]**weishu(num))
   if num ==add:
      print(num)
  
def weishu(num):
  counter = 0
  for i in range(10):
    num = int (num/10)
    counter +=1
    if num == 0:
      break
  return counter

def chaifen(num,wei):
  list1 = []
  for i in range(wei):
    coup = int(num%10)
    num = int(num/10)
    list1.append(coup)
  return list1
  
main()
    
