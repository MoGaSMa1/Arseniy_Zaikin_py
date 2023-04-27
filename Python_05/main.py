import time
import os
import datetime
import UTFNumbers
from colorama import init, Fore, Style
import random
from threading import Thread



def time_to_numbers(sdel, ch):
    t = time_now()
    stroka = ''
    for i in t:
        if i != ':':
            stroka = stroka + ' ' + UTFNumbers.rectangle_num(int(i), sdel)
        else:
            stroka = stroka + UTFNumbers.rectangle_dot(ch, sdel)
    return stroka
            
def time_now():
    t = datetime.datetime.now()
    t = t.time()
    t = datetime.time.strftime(t, "%H:%M:%S")
    return t

def rundom_color():
    while True:
        time.sleep(2)
        ch = random.randint(0, 4)
        match ch:
            case 1:
                print(Fore.GREEN)
            case 2:
                print(Fore.YELLOW)
            case 3:
                print(Fore.MAGENTA)
            case 4:
                print(Fore.RED)

def main():
    tr = True
    ch = 0

    while True:
        if tr == True:
            ch += 1
            if ch == 4:
                tr = False
        else:
            ch -= 1
            if ch == 1:
                tr = True
        time.sleep(0.2)
        os.system('cls')
        for i in range(5):
            print(time_to_numbers(i, ch))

thread1 = Thread(target=main)
thread2 = Thread(target=rundom_color)

thread1.start()
thread2.start()

