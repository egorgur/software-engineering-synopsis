Theading package
```python
import threading
```

create a thread
```python
thr = threading.Thread(target=some_func, args=(some_arg1,some_arg2,etc,),name="thread", daemon=false)

thr.start()
```

join
```python
thr_list = []
"""A list with all threads"""

for i in range(n):
	thr = threading.Thread(target=some_func, args=(,), name="some-thread")
	thr_list.append(thr)
	"""Add to list before start"""
	thr.start()

for i in thr_list:
	i.join()
```







