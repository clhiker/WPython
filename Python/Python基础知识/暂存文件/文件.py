def main():
  file = "zhi.txt"
  infile = open(file,'r')
  for line in infile:
    print(line,end = '')
  without(file)
  infile.close()

def without(file):
  infile = open(file,'r')
  list1 = [line.retrip() for line in infile]
  print(list1)

main()

