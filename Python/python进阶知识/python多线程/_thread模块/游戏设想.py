import _thread
import time

def player():
    print('I\'m player')

def NPC():
    print('I\'m NPC')

def main():
    while True:
        try:
            _thread.start_new_thread(player,())
            _thread.start_new_thread(NPC,())
        except:
            print('Error create thread')
        time.sleep(1)

main()