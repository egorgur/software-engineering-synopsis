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
