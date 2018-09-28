def main():
  list1 = ["lihui","huangjunhui","zhoujingyao","chenle"]
  list1.sort(key = len)
  print(list1)
  list1.sort(key = vowels , reverse = True)
  print(list1)

def vowels(list1):
  vowels = ["a","e","i","o","u"]
  total = 0
  for i in vowels:
    total += list1.count(i)
  return total
  
main()
