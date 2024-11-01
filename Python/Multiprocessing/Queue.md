Queue is a multiprocessing communication technique
Used as channels in Go
```python
import random
import multiprocessing

def get_text(q):
    val = random.randint(0,10)
    q.put(str(val))



if __name__ == "__main__":
    queue = multiprocessing.Queue()
    pr_list = []

    for _ in range(10):
        prc = multiprocessing.Process(target=get_text, args=(queue,))
        pr_list.append(prc)
        prc.start()

    for i in pr_list:
        i.join()
    

    for elem in iter(queue.get, None):
        print(elem)
```
```shell
[<Process name='Process-1' pid=22208 parent=2484 stopped exitcode=0>, <Process name='Process-4' pid=21328 parent=2484 stopped exitcode=0>, <Process name='Process-5' pid=9124 pa
parent=2484 stopped exitcode=0>, <Process name='Process-8' pid=15716 parent=2484 stoppeded exitcode=0>]
7
8
3
0
1
8
6
```