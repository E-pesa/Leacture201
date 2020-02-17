from concurrent.futures import ThreadPoolExecutor
import threading
import time


def iterates():
    list = []
    for next in range(5):
        list_url = f"https://wwww.facebook.com/{next}"
        list.append(list_url)
    return list

def use():
    p = iterates()
    for i in p:
        print(i) 
    print(f"Time it's took to execute is {end - start}")

if __name__ == "__main__":
     start = time.time() * 1000
     with ThreadPoolExecutor(max_workers=1) as executor:
         x = executor.submit(use)
     end = time.time() * 1000 
     print(end - start)

        