Works the same way as in threads

```python
import multiprocessing

lock = multiprocessing.RLock()
# lock = multiprocessing.Lock()
# If Lock instead of RLock, then any process could release the lock

def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f"Process [{pr_name}] has been started")

if __name__ == "__main__":
	multiprocessing.Process(target=get_value, args=(lock,)).start()
	lock.release() # AssertionError: attempt to release recursive lock not owned by thread
```
```shell
...
AssertionError: attempt to release recursive lock not owned by thread
Process [Process-1] has been started
...
```