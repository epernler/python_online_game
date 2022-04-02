import socket
import time
import threading

CLIENTS = 2
PORT = 1337
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname())           #
ADDRESS = (HOST, PORT)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #
SERVER.bind(ADDRESS)                                        #

def connect_client():
    connection = True
    while connection:


def init_server()
    SERVER.listen(CLIENTS)
    while True:
        c, a = SERVER.accept()
        thread