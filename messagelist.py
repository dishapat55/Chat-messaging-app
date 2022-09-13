from multiprocessing.connection import _ConnectionBase
import socket

PORT = 80
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATUTF = "utf-8"
Disconnect_message = "...disconnected!"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def start():  # a different start fx since its a different file-works
    connection = connect()

    while True:
        msg = connection.recv(1024).decode(FORMATUTF)
        print(msg)


start()
