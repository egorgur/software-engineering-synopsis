Process waits for an event to be set to true
```python
import time
from multiprocessing import Process, Event
  
event = Event()
  
def test():
    print("Test func if running")
    while True:
        event.wait()
        print("test")
        time.sleep(1)
  
if __name__ == "__main__":
    Process(target=test).start()
```