import time
from socket import *


def fib_client(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)
    print("Connected", sock.getsockname())
    num = 1
    while True:
        start = time.time()
        sock.send(f"{num}".encode("ascii"))
        resp = sock.recv(100)
        end = time.time()
        elapsed = end - start
        print(f"fib({num}): {resp} {elapsed=}")
        if elapsed < 1:
            num += 1
        elif elapsed > 2:
            num -= 1


if __name__ == '__main__':
    fib_client(("", 25000))
