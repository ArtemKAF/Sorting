import time
from datetime import timedelta


def time_use(func):
    def wrapper(*args, **kwargs):
        s_time = time.monotonic()
        result = func(*args, **kwargs)
        e_time = time.monotonic()
        print(f"Время сортировки массива: {timedelta(e_time - s_time)}")
        return result
    return wrapper
