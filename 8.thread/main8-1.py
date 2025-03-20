import threading
import time

def thread_1():
    while True:
        print("쓰레드 1 동작")
        time.sleep(1)

t1 = threading.Thread(target = thread_1)
t1.start()

while True:
    print("메인 동작")
    time.sleep(2)