import threading
import time

sofa = 4
chair = 3
seat = 13       #等候室

def Baber(persons):
    for i in range(persons):
        print()

def Costumes(persons):

#
# class Control:
#     def __init__(self):
#         self.name = ''
#
# class Baber:
#     def __init__(self):
#         self.name = ''
#
#     def cutHair(self):
#
#
# class Cosumer:
#     def __init__(self):
#         self.name = ''

thread1 = threading.Thread(target=Baber,args=())