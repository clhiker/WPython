list1 = [1,3,5,7,9,0]
list2 = [2,6,10] 
for i in range(3):
  counter = -1
  
  for j in range(8):
    counter += 1

    if list2[i] < list1[j]:
      break

  print(counter)
  list1.insert(counter,list2[i])
    
print(list1)
