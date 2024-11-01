import multiprocessing
import multiprocessing.managers

multiprocessing.managers.BaseManager.register("time")
manager = multiprocessing.managers.BaseManager(address=("127.0.0.1", 4444), authkey=b"abc")
print("client connected")
manager.connect()

res = manager.time()
print(f"result: {res}")