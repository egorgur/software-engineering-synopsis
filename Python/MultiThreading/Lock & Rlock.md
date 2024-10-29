Threading synchronization methodics

**Lock**
---
```python
value = 0
locker = threading.Lock()

def some_func():
	global value
	while True:
		locker.acquire()
		value += 1
		locker.release()

for _ in range(n):
	threading.Thread(target=some_func).start()
```

**RLock**
---
```python
locker = threading.RLock()

def some_func():
	print("Thread is locked")
	locker.acquire()
	print("Thread is unlocked")

threading.Thread(target=some_func).start()
```
Without **RLock**
---
```bash
ipython -i main.py
# Ipython data...
In [1]: locker.release()
# An attempt to unlock from main thread
Thread is unlocked
# Bad behaviour: 
# a thread should not have an ability to unlock any other thread's locks
```
With RLock
---
```bash
ipython -i main.py
# Ipython data...
In [1]: locker.release()
# An attempt to unlock from main thread
----------------------------------------------------------------
RuntimeError
#....
RuntimeError: cannot release un-acquired lock
# Obviously how it should work 
```

