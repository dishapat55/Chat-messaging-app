from multiprocessing.connection import _ConnectionBase
import socket
import time
from xmlrpc import client

from numpy import True_

PORT = 80
SERVER = socket.gethostbyname(socket.gethostname())
# ip address of machine running our socket, either
# either localhost or socket.gethostbyname(socket.gethostname()) or print it
ADDR = (SERVER, PORT)
FORMATUTF = "utf-8"
Disconnect_message = "...disconnected!"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, msg):
    message = msg.encode(FORMATUTF)
    client.send(message)


def start():
    answer = input("Would you like to connect? yes/no ")
    if answer.lower() != "yes":
        return

    connection = connect()
    username = input("Press q to quit anytime\nEnter username: ")
    while True:
        msg = input(username.upper() + ": ")

        if msg == 'q':
            break

        send(connection, username.upper() + ": " + msg)

    send(connection, Disconnect_message)
    time.sleep(1)  # pause for 1 second
    print("Disconnected!")


start()
