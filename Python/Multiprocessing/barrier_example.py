import time
import random
import multiprocessing

def f1(bar):
    name = multiprocessing.current_process().name
    sl = random.randint(2,10)
    print(f"wait for {sl} seconds")
    time.sleep(sl)
    bar.wait()
    print(f"[{name}] - run")

b = multiprocessing.Barrier(5)

if __name__ == "__main__":
    for i in range(5):
        multiprocessing.Process(target=f1, args=(b,)).start()
