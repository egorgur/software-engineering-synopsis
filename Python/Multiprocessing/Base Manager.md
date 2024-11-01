Allows to share classes instances between processes using machine's OS ports

>*Behold the micro-microservice architecture . . .*

server
```python
import multiprocessing
import multiprocessing.managers
import time


def get_time():
    return time.time()

multiprocessing.managers.BaseManager.register("time", callable=get_time)
manager = multiprocessing.managers.BaseManager(address=("", 4444), authkey=b"abc")
server = manager.get_server()
print("manager server start")
server.serve_forever()
```
client
```python
import multiprocessing
import multiprocessing.managers

multiprocessing.managers.BaseManager.register("time")
manager = multiprocessing.managers.BaseManager(address=("127.0.0.1", 4444), authkey=b"abc")
print("client connected")
manager.connect()

res = manager.time()
print(f"result: {res}")
```
when the server runs:
```console
manager server start
```
when the client runs:
```console
client connected
result: 1730481940.8905141
```