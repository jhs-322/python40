import threading
import time

def t1():
    while True:
        print("쓰레드 1 동작")
        time.sleep(1)

thr1 = threading.Thread(target=t1)
thr1.daemon = True
thr1.start()

while True:
    print("메인 동작")
    time.sleep(2)
