import zipfile
zFile = zipfile.ZipFile("1.zip")
passFile = open('dictionary.txt')
for line in passFile.readline():
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print("[+] password = " + password + "\n")
    except:
        pass

print("Didn't find")