import random
import time
from multiprocessing import Process, Event

event = Event()

def test():
    print("Test func if running")
    while True:
        event.wait()
        time.sleep(1)
        print("test")


if __name__ == "__main__":
    Process(target=test, daemon=True).start()
    time.sleep(2)
    event.set()
    print(event)
    time.sleep(3)
    event.clear()
    print(event)
