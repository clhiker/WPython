def main():
  import time
  for i in range(29):
    print('-',end = '')
  print('-')
  while True:
    for i in range(10):
      print(chr(15),end ='')
      time.sleep(0.2)
      print(chr(222),end='')
      time.sleep(0.2)
    print("\r")

main()
