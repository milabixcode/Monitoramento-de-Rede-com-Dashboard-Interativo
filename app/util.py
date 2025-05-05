from contextlib import contextmanager
import time

@contextmanager
def measure(name: str):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end - start} seconds")