import time
import multiprocessing


def test():
    for _ in range(4):
        print(f"{multiprocessing.current_process().name} - {time.time()}")
        time.sleep(1)

prc: list[multiprocessing.Process] = []

if __name__ == "__main__":        
    for _ in range(3):
        pr = multiprocessing.Process(target=test)
        prc.append(pr)
        pr.start()
    
    for i in prc:
        i.join()
    
    print("all processes are done")
        