from multiprocessing import Pool
import time

def func(num):
    for _ in range(num):
        pass
        

if __name__ == "__main__":
    p = Pool()
    st = time.time()
    result = p.map(func,range(10000))
    p.close()
    p.join()
    print(f"Pool took : {time.time() - st}")

    t2 = time.time()
    reslult  = []
    for x in range(10000):
        reslult.append(func(x))
    print(f"Single proceess took : {time.time() -  t2}")