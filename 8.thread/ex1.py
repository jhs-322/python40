import threading
import time

def th1():
    while True:
        print("스레드1 작업")
        time.sleep(1)

def th2():
    while True:
        print("스레드2 작업")
        time.sleep(3)

t1 = threading.Thread(target=th1)
t1.start()
t2 = threading.Thread(target=th2)
t2.start()

while True:
    print("메인 동작")
    time.sleep(3)
