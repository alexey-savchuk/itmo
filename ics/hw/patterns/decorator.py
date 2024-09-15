from time import time, sleep
from random import randint
from numpy import mean

metrics_storage = {}


def measure_execution_time(f):
    def inner(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()

        if f.__name__ not in metrics_storage:
            metrics_storage[f.__name__] = []
        metrics_storage[f.__name__].append(end - start)

        return result

    inner.__name__ = f.__name__

    return inner


def some_function():
    sleep(randint(0, 1))


some_function = measure_execution_time(some_function)

for _ in range(10):
    some_function()

metrics = metrics_storage[some_function.__name__]

print(metrics)
print(mean(metrics))
