def main():
    while True:
        x = input('Please input')
        try:
            x = int(x)
            print('You have input {0}'.format(x))
            break
        except Exception as e:
            print('Error')

main()
