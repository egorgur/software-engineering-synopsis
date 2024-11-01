process pool
```python
import random

import multiprocessing

  

# map_async version
def end_func(response):
    print("The work is done")
    print(response)

def get_value(value):
    name multiprocessing.current_process().name
    print(f"[{name}] value {random.randint(0,10)}")
    return value

if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.map_async(get_value, list(range(100)), callback=end_func)
        p.close()
        p.join()
```
```shell
[SpawnPoolWorker-2] value: 9
[SpawnPoolWorker-3] value: 7
[SpawnPoolWorker-1] value: 9
[SpawnPoolWorker-5] value: 6
[SpawnPoolWorker-4] value: 5
# ... all workers print their value
[SpawnPoolWorker-1] value: 3
[SpawnPoolWorker-8] value: 1
[SpawnPoolWorker-27] value: 7
[SpawnPoolWorker-15] value: 2
The work is done
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```
apply async
```python
# apply_async version
def end_func(response):
    print("response: ",response) 

def out(x):
    print(f"value: {x}")
    return x
    
if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        for i in range(10):
            p.apply_async(out, args=(i,), callback=end_func)
        p.close()
        p.join()
```
```shell
value: 0
value: 1
value: 2
response:  0
value: 6
value: 7
value: 9
value: 3
value: 4
value: 8
value: 5
response:  6
response:  7
response:  3
response:  8
response:  1
response:  2
response:  9
response:  4
response:  5
```
starmap
```python
def out(x, y, z):
    print(f"value: {x} {y} {z}")

if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap(out, [(1, 2, 3), (4, 5, 6)])
        p.close()
        p.join()
```
```shell
value: 1 2 3
value: 4 5 6
```
starmap_async
```python
def out(x, y, z):
    print(f"value: {x} {y} {z}")
    return x,y,z

def end_func(response):
	print("end_func: ", response)

if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
        p.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=end_func)
        p.close()
        p.join()
```
```shell
value: 1 2 3
value: 4 5 6
end_func:  [(1, 2, 3), (4, 5, 6)]
```