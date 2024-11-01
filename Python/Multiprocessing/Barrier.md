wait untill all processes have reached the barrier
```python
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
```
```shell
wait for 7 seconds
wait for 5 seconds
wait for 7 seconds
wait for 3 seconds
wait for 4 seconds
[Process-3] - run
[Process-2] - run
[Process-4] - run
[Process-5] - run
[Process-1] - run
```