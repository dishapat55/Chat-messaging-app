import threading
import socket

from numpy import True_

PORT = 80
SERVER = socket.gethostbyname(socket.gethostname())
# ip address of machine running our socket, either
# either localhost or socket.gethostbyname(socket.gethostname()) or print it
ADDR = (SERVER, PORT)
FORMATUTF = "utf-8"
Disconnect_message = "...disconnected!"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()  # lock is built in fx


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMATUTF)
            if not msg:
                break

            if msg == Disconnect_message:
                connected = False

            print(f"[{addr}{msg}]")
            with clients_lock:
                for c in clients:
                    c.sendall(f"[{addr}]{msg}".encode(FORMATUTF))

    finally:  # removes client,to close the connection
        with clients_lock:
            clients.remove(conn)

        conn.close()


def start():
    print("[SERVER STARTED]")
    server.listen()
    while True:
        conn, addr = server.accept()  # waits for incoming conn from clients
        with clients_lock:
            clients.add(conn)
        # thread allows multiple clients to interact with server without blocking each other
        # the target= needs to be a function
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
