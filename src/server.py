# To get started with sockets, threads and time, this guide was used https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim

import socket
import time
import threading

CLIENTS = 2
PORT = 8080
FORMAT = "utf-8"
HEADER = 8                                                 # header that tells us how big the following message is
HOST = socket.gethostbyname(socket.gethostname())           # set the host of server to own local IP, should be changed to public IP when 2 players
ADDRESS = (HOST, PORT)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket object, IPv4 and TCP
D_MSG = "Client disconnected"

SERVER.bind(ADDRESS)

def connect_client(c, a):
    connection = True
    print(f"[New connection] {a} connected")                # c is a connection object we use to communicate with each connection
    while connection:
        msg_len = c.recv(HEADER).decode(FORMAT)
        if msg_len:                                         # avoid error since theres a connection message that cant convert to int
            msg_len = int(msg_len)
            msg = c.recv(msg_len).decode(FORMAT)
            print(f"[{a}] {msg}")
            if msg == D_MSG:
                connection = False
            c.send("Message recieved".encode(FORMAT))
    c.close()


def init_server():
    SERVER.listen(CLIENTS)
    while True:
        print("Server waiting for connection...")
        c, a = SERVER.accept() # waits for a new connection, stores address and object that allows us to communicate back to client
        thread = threading.Thread(target=connect_client, args=(c, a))
        thread.start()
        print(f"[Active connections] {threading.active_count() - 1}")

print("Server is starting...")
init_server()