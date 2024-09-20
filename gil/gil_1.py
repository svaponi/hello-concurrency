import time
from threading import Thread


def countdown(n):
    while n > 0:
        n -= 1


COUNT = 100_000_000


def run(n_of_threads=4):
    _start = time.perf_counter()
    if n_of_threads == 1:
        countdown(COUNT)
    else:
        t = [Thread(name=f"t-{j}", target=countdown, args=(COUNT // n_of_threads,)) for j in range(n_of_threads)]
        [t_.start() for t_ in t]
        [t_.join() for t_ in t]
    elapsed = time.perf_counter() - _start
    print(f"exec time {n_of_threads=}:", elapsed)


if __name__ == '__main__':
    # with with_profiling():
    for i in range(0, 5):
        run(2 ** i)
