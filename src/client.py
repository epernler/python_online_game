import socket
import time
import threading

PORT = 8080
HEADER = 8
FORMAT = "utf-8"
D_MSG = "Client disconnected"
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)
CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT.connect(ADDRESS)

def send_msg(msg):
    m = msg.encode(FORMAT)                      # encode message string into a byte object
    m_len = len(m)
    s_len = str(m_len).encode(FORMAT)           # length of message in string
    s_len += b' ' * (HEADER - len(s_len))       #
    CLIENT.send(s_len)
    CLIENT.send(m)
    print(client.recv(2048).decode(FORMAT))

send_msg("Hello bitch")
send_msg(D_MSG)