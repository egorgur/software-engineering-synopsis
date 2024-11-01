The communication between processes
```python
import multiprocessing
import multiprocessing.synchronize
import random
import time

lock = multiprocessing.Lock()
arr = multiprocessing.Array("i", range(10))
process = []

def add_value(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f"array[{index}] = {num}, time = {vtime}")
        time.sleep(num)

if __name__ == "__main__":
    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(lock,arr,i))
        process.append(pr)
        pr.start()

    for i in process:
        i.join()
    
    print(list(arr))
```
```shell
array[0] = 5, time = Fri Nov  1 21:49:17 2024
array[1] = 18, time = Fri Nov  1 21:49:22 2024
array[2] = 10, time = Fri Nov  1 21:49:40 2024
array[3] = 6, time = Fri Nov  1 21:49:50 2024
array[4] = 9, time = Fri Nov  1 21:49:56 2024
array[5] = 5, time = Fri Nov  1 21:50:05 2024
array[6] = 3, time = Fri Nov  1 21:50:10 2024
array[7] = 10, time = Fri Nov  1 21:50:13 2024
array[8] = 18, time = Fri Nov  1 21:50:23 2024
array[9] = 1, time = Fri Nov  1 21:50:41 2024
[5, 18, 10, 6, 9, 5, 3, 10, 18, 1]
```