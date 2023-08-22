import time
import multiprocessing

def count_num(name):
    cnt = 0
    for _ in range(1000000):
        cnt += 1
    print(f"{name} Done")

def func1():
    start = time.time()

    with multiprocessing.Pool(processes=3) as pool:
        pool.map(count_num, range(3))

    end = time.time()
    delta = end-start
    print(f"총 시간: {delta:.3f} sec")
    
if __name__ == "__main__":
    func1()