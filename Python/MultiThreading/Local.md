```python
data = threading.local()

def get():
	"""
	local data could be accessed through a func
	if it is being called from a thread func
	"""
	print(data.value)

def t1():
	data.value = 111 # Local attribute value set
	print("t1:", data.value)
	#get()

def t2():
	data.value = 222 # Local attribute value set
	data.test = ["eeee", "teeee"]
	print("t2:", data.value)
	print("t2:", data.test)
	#get()

threading.Thread(target=t1).start()
threading.Thread(target=t2).start()
```
```bash
222
["eeee", "teeee"]
111
```