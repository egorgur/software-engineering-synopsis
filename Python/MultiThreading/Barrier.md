Like a waitgroup in Golang + a Semaphore
```python
import time
import random
import threading
from threading import currentThread

def test(barrier):
	slp = random.randint(3,7)
	print(f"Thread [{currentThread().name}] is run in ({time.ctime()})")
	time.sleep(slp)
	
	barrier.wait()
	print(f"Thread [{currentThread().name}] got through the barrier in ({time.ctime()})")

bar = threading.Barrier(5)
for i in range(5):
	threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()
```
```bash
Thread [thr-0] is run in (Wed Oct 30 22:47:25 2024)
Thread [thr-2] is run in (Wed Oct 30 22:47:26 2024)
Thread [thr-3] is run in (Wed Oct 30 22:47:27 2024)
Thread [thr-4] is run in (Wed Oct 30 22:47:28 2024)
Thread [thr-1] is run in (Wed Oct 30 22:47:29 2024)
Thread [thr-1] got through the barrier in (Wed Oct 30 22:47:29 2024)
Thread [thr-0] got through the barrier in (Wed Oct 30 22:47:29 2024)
Thread [thr-2] got through the barrier in (Wed Oct 30 22:47:29 2024)
Thread [thr-3] got through the barrier in (Wed Oct 30 22:47:29 2024)
Thread [thr-4] got through the barrier in (Wed Oct 30 22:47:29 2024)
```