Allows to run a thread after a certain period

```python
def some_func():
	while True:
		print("The Thread answers")
		time.sleep(1)

threading.Timer(10, some_func).start()

while True:
	print("The Main thread speaks")
	time.sleep(2)
```
```bash
# The result
The Main thread speaks
The Main thread speaks
The Main thread speaks
The Main thread speaks
# ... afted 10 seconds
The Thread answers
The Thread answers
The Main thread speaks
```

Thread cancel
```python
def some_func():
	...

thr = threading.Timer(10, some_func)
thr.start()

for _ in range(3):
	print("The Main thread speaks")
	time.sleep(2)
	
thr.cancel()
# Cancel a thread before it starts
```