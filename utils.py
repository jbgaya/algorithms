import time
import typing as tp

def measure_time(func: tp.Callable, *args, **kwargs) -> float:
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time