import time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        wrapper.time_elapsed += round(elapsed_time, 4)  # Accumulate time for all calls
        return result
    wrapper.call_count = 0
    wrapper.time_elapsed = 0.
    return wrapper