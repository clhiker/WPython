
def chooseStruct():
    if 3:
        print(5)

def Join(ch_list, sep=None):
    return (sep or ',').join(ch_list)
def Test():
    ch_test = ['1', '2', '3', '4']
    a = Join(ch_test)
    print(a)
    b = Join(ch_test, " ")
    print(b)

def main():
    Test()

main()

