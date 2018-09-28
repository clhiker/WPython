
def main():
    #for line in open("D:\\1.dat", "rb"):
     #   print(line)
    infile = open("D:\\1.dat", 'rb')
    for line in infile:
        data = line.split()
        print(data)

main()