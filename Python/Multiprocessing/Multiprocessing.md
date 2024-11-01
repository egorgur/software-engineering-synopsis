```python
import time
import multiprocessing

def test():
	while True:
		print(f"{multiprocessing.current_process()}",time.time())
		time.sleep(1)

multiprocessing.Process(target=test, name="prc-1").start()
```

some methods and attributes:
`is_alive()` - is alive
`pid` - unique process id
`terminate()` - save process termination
