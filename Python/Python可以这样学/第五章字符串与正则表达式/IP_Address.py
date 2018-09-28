import re
def main():
    ipv4 = input("input IP address:")
    # result = re.findall(ipv4,'\d')
    # result = re.match(ipv4, '\w[3]')    #match函数只能从头开始匹配
    # print(result)
    # result = re.search(r'\d[3]', ipv4)   #不是从头也可以
    # print(result)
    test = re.compile(r'3')
    print(test.findall(ipv4))

if __name__ == '__main__':
    main()
