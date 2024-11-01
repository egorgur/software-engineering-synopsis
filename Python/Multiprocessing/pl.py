import random
import multiprocessing

# map_async version
# def end_func(response):
#     print("The work is done")
#     print(response)

# def get_value(value):
#     name = multiprocessing.current_process().name
#     print(f"[{name}] value: {random.randint(0,10)}")
#     return value

# if __name__ == "__main__":
#     with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
#         p.map_async(get_value, list(range(100)), callback=end_func)
#         p.close()
#         p.join()


# def end_func(response):
#     print("response: ", response)


# def out(x):
#     print(f"value: {x}")
#     return x


# if __name__ == "__main__":
#     with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
#         for i in range(10):
#             p.apply_async(out, args=(i,), callback=end_func)
#         p.close()
#         p.join()

# Starmap
# def out(x, y, z):
#     print(f"value: {x} {y} {z}")


# if __name__ == "__main__":
#     with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
#         p.starmap(out, [(1, 2, 3), (4, 5, 6)])
#         p.close()
#         p.join()

def out(x, y, z):
    print(f"value: {x} {y} {z}")
    return x,y,z

def end_func(response):
	print("end_func: ", response)

if __name__ == "__main__":
     with multiprocessing.Pool(multiprocessing.cpu_count() * 3) as p:
          p.starmap_async(out, [(1, 2, 3), (4, 5, 6)], callback=end_func)
          p.close()
          p.join()