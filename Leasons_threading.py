import threading
import time
from concurrent.futures import ThreadPoolExecutor


def treat():
    for _ in range(10):
        time.sleep(3.1)
        print("hello there")

def number(n):
    for _ in range(3):
        time.sleep(3)
        print(n)


if __name__ == "__main__":
    x = threading.Thread(target=treat, args=())
    y = threading.Thread(target=number, args=(1,))
    x.start()
    y.start()
    x.join()
    y.join()

