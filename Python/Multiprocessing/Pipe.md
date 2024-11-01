Channels to send and receive data between processes
`Literally Go...`
```python
from multiprocessing import Pipe

def send_data(conn):
    conn.send("hello world")
    conn.send()

if __name__ == "__main__":
    output_c, input_c = Pipe()
    p = multiprocessing.Process(target=send_data, args=(input_c,))
    p.start()
    p.join()
    print("data: ", output_c.recv())
```