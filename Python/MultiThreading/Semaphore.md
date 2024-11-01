```python
from threading import Thread, BoundedSemaphore

max_connections = 5
pool = BoundedSemaphore(value=max_connections)

def test():
	while True:
		with pool:
			print(currentThread().name)
			time.sleep(6)

for i in range(10):
	Thread(target=test, name=f"thr-{i}").start()
```
```bash
thr-0
thr-1
thr-2
thr-3
thr-4
# 6 seconds later...
thr-5
thr-6
thr-7
thr-8
thr-9
```
