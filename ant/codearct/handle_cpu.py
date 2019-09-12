import time
import threading



time.sleep(1)
print 1

global flag
flag = False
i = 1

def received_alarm(n):
    global flag
    time.sleep(n)
    flag = True


while True:
    global flag
    while True:
        if flag:
            flag = False
            break
        i += 1