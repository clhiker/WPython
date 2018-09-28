fn1 = 1
fn2 = 0
print("{0:<8d}".format(fn2,fn1),end = ' ')
i = 1
counter = 1
while i < 20:
  fn = fn1 + fn2
  fn2 = fn1
  fn1 = fn
  i +=1
  counter +=1
  print("{0:<8d}".format(fn),end = ' ' )
  if counter == 8:
    print('\n')
    counter = 0
