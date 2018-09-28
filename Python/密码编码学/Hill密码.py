"""

1.密钥固定了
2.空格被处理掉了
3.不足的长度空间用a补充了
4.只写了加密过程，解密过程还没写
"""

import numpy

plaintext = input("请输入明文")
# 密码矩阵必须可逆，随机生成
password = numpy.array([(17,17,5),(21,18,21),(2,2,19)])
print(password)

# 密码长度
password_length = len(plaintext) // 3

# 补零操作
remainder = len(plaintext) % 3
if remainder != 0:
    for i in range(3-remainder):
        plaintext += 'a'
    password_length += 1

# 生成字母映射表,反向字母映射表
dir = {}
redir = {}
for i in range(26):
    dir[chr(i + 97)] = i

for i in range(26):
    redir[i] = chr(i + 97)

# 明文转换为密文
ciphertext = ""

part_list = [0,0,0]
for i in range(len(plaintext)):
    if (i+1) % 3 != 0:
        part_list[i%3] = (dir[plaintext[i]])
    else:
        part_list[i%3] = (dir[plaintext[i]])
        arr = numpy.array(part_list)
        result = numpy.dot(password, arr)
        temp_num = ""
        for j in range(len(result)):
            temp_num += redir[result[j] % 26]
        ciphertext += temp_num
if remainder != 0:
    ciphertext = ciphertext[:-(3-remainder)]
print(ciphertext)