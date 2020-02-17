import threading
import time

def treat():
    for _ in range(10):
        time.sleep(5)
        print("hello there")

def number(n):
    for _ in range(3):
        print(n)


if __name__ == "__main__":
    x = threading.Thread(target=number, args=(1,))
    y = threading.Thread(target=treat, args=())
    y.start()
    x.start()
    x.join()
    y.join()
