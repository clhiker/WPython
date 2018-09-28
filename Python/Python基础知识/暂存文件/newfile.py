# # Display presidents with a specified first name.
firstName = input("enter a first name:")
foundFlag = False
infile = open("USPres.txt" ,'r')
for line in infile:
    if line.startswith(firstName + ' '):
        print(line.rstrip())
        foundFlag = True
if not foundFlag:
    print("No president had the first name",firstName + '.')
