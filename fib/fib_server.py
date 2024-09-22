from socket import *
from threading import Thread

from fib import fib


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    print("Listening", sock.getsockname())
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        Thread(target=fib_handler, args=(client,), daemon=True).start()


def fib_handler(client):
    def send(data):
        if not isinstance(data, bytes):
            if not isinstance(data, str):
                data = str(data)
            data = data.encode("ascii")
        if not data.endswith(b"\n"):
            data = data + b"\n"
        print(b"<< " + data)
        client.send(data)

    while True:
        try:
            req = client.recv(100)
            if not req:
                break
            print(b">> " + req)
            if req == b"quit\n":
                break
            n = int(req)
            result = fib(n)
            send(result)
        except Exception as e:
            send(f"Error: {e}")
    send(f"Bye")
    client.close()


if __name__ == '__main__':
    fib_server(("", 25000))
