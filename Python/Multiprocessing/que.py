import random
import multiprocessing

def get_text(q):
    val = random.randint(0,10)
    q.put(str(val))



if __name__ == "__main__":
    queue = multiprocessing.Queue()
    pr_list = []

    for _ in range(10):
        prc = multiprocessing.Process(target=get_text, args=(queue,))
        pr_list.append(prc)
        prc.start()

    for i in pr_list:
        i.join()
    

    for elem in iter(queue.get, None):
        print(elem)