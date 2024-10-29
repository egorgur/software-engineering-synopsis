*Daemon* is a thread that stops it's execution if a main thread has stopped it's own

```python
thr = threading.Thread(target=some_func,args=(,),daemon=True)
```