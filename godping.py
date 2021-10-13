import godping
import os
import time

def ipping():
    os.system("cls")
    count = 1
    e = input("Enter IP Address:   ")
    replies = 0
    replies += 1
    hostname = e
    os.system("cls")
    print("-"*100)
    print("="*100)
    print("-"*100)
    while True:
        response = os.system("ping -n 1 " + hostname + " >nul")
        if response == 0:
            print("\033[1;32;40m" + hostname + " is online   0.39ms!" + " [" +  str(count) + "]" +  '\033[0m')
        else:
            print("\033[31m" + hostname + " is offline!" " [" +  str(count) + "]" +  '\033[0m')
        count += 1
        time.sleep(0.1)


ipping()