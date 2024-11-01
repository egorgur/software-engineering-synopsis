import time
from multiprocessing import Process, Condition

cond = Condition()

def f1(cond):
    while True:
        with cond:
            cond.wait()
            print("received condition")


def f2(cond):
    for i in range(100):
        if i % 10 == 0:    
            with cond:
                cond.notify()
        else:
            print(f"f2: {i}")
        time.sleep(1)

if __name__ == "__main__":
    Process(target=f1, args=(cond,)).start()
    Process(target=f2, args=(cond,)).start()
