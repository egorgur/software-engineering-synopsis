could make a process wait until a condition is triggered
```python
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
```
```shell
received condition
f2: 1
f2: 2
f2: 3
f2: 4
f2: 5
f2: 6
f2: 7
f2: 8
f2: 9
received condition
...
```