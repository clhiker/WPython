def main():
  str1 = []
  str2 = []
  print("input number:")
  number1 = str(input())
  number2 = str(input())
  str1.append(number1)
  str2.append(number2)
  print(number1)
  print(number2)
  str3 = str1.split()
  str4 = str2.split()
  n1 = len(str3)
  n2 = len(str4)
  print(n1,n2)

main()
