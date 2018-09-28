def main():
  infile = open("lihui.txt",'r')
  listvar = [line.rstrip() for line in infile]
  print(listvar)
  file = "chenle.txt"
  for line in infile:
    print(line, end=" ")
  infile.close()
main()
