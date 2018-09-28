def main():
    test = "p|q&f|~d"
    pos = test.find("m")
    print(pos)
    pro_var = {""}
    standard_oper = "|&~"
    for i in range(0, len(test)):
        if (standard_oper.find(test[i]) == -1):
            pro_var.add(test[i])
    l = list(pro_var)
    for i in range(len(l)):
        print(l[i])
    pattern = test.split("|")
    for i in range(len(pattern)):
        print(pattern[i],end=" ")

def test():
    test = "p|q&f|~d"
    for i in range(len(test)):
        if(test[i] != '~'):
            print("fdsa")

test()