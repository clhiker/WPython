class File:
    filename = ""
    def __init__(self,value):
        File.__filename = value

    def openFile(self):
        f1 = open(self.filename,'r')
        f1.close()

def main():
    f = input("input filename:\n")
    file = File(f)

main()
