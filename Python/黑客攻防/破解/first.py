import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('direction', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if (cryptWord == cryptPass):
            print("[+] Found PassWord: " + word + "\n")
            return
        print("[-] PassWord Not Found.\n")
        return

def main():
    passFile = open('PassWrds.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[1].strip(' ')
            print("[*] Cracking password for: "+user)
            testPass(cryptWord)

if __name__ == '__main__':
    main()
