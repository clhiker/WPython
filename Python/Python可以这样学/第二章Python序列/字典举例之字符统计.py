import random
import string
from collections import defaultdict
from collections import Counter

def keyWay():
    x = string.ascii_letters + string.digits + string.punctuation   #字符+数字+标点
    print(x)
    y = [random.choice(x) for i in range(1000)]
    print(y)
    z = ''.join(y)
    print(z)
    d = dict()
    for ch in z:
        d[ch] = d.get(ch, 0)+1
    print(d)

def defaulidictWay():
    x = string.ascii_letters + string.digits + string.punctuation  # 字符+数字+标点
    y = [random.choice(x) for i in range(1000)]
    z = ''.join(y)
    fq = defaultdict(int)       #生成默认字典
    print(fq)
    for i in z:
        fq[i] += 1
    print(fq)

def countWay():
    x = string.ascii_letters + string.digits + string.punctuation  # 字符+数字+标点
    y = [random.choice(x) for i in range(1000)]
    z = ''.join(y)
    fq = Counter(z)
    print(fq.items())
    print(fq.most_common(1))    #出现次数最多的字符
    print(fq.most_common(3))    #出现次数最多的前三个字符

def main():
    #defaulidictWay()
    countWay()
main()

