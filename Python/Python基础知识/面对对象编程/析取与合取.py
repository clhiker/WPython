
class Expression:
    def __init__(self, exp="", pro_var={""}):
        self._exp = exp
        self._pro_var = pro_var

    # 得到命题变元
    def get_pro_var(self):
        standard_oper = "|&~"
        for i in range(0, len(self._exp)):
            if (standard_oper.find(self._exp[i]) == -1):
                self._pro_var.add(self._exp[i])
        l = list(self._pro_var)
        return l

    def get_map(self):
        l = self.get_pro_var()
        for i in range(len(l)):
            Pv[l[i]] = i
        return Pv

    def spiltExp(self):
        pattern = self._exp.split("|")
        return pattern

    def get_result(self):
        PV = self.get_map()
        pattern =self.spiltExp()
        for i in range(len(pattern)):
            temp = pattern[i]
            for j in range(len(temp)):
                if(temp[j] != '~'):
                    if(temp[j] in PV):
                        num += pow(2,PV[temp[j]])
                else:



    def __str__(self):
        l = self.get_pro_var()
        for i in range(len(l)):
            print(l[i])
        return "表达式为:" + self._exp

def main():
    name = input("请输入表达式\n")
    exp = Expression(name)
    print(exp)

main()