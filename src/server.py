# To get started with sockets, threads and time, these guides were used to help:
# https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim and https://www.youtube.com/watch?v=McoDjOCb2Zo&ab_channel=freeCodeCamp.org

import socket
import time
import threading

from server_cmd_dict import *

CLIENTS = 2
PORT = 8080
FORMAT = "utf-8"
HEADER = 2048                                               # header that tells us how big the following message is
HOST = socket.gethostbyname(socket.gethostname())           # set the host of server to own local IP, should be changed to public IP when 2 players
ADDRESS = (HOST, PORT)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket object, IPv4 and TCP

SERVER.bind(ADDRESS)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

#def set_game_state(data):

#    return

pos = [(300, 350), (350, 350)]


def connect_client(c, a, p):
    print(f"[New connection] {a} connected")                # c is a connection object we use to communicate with each connection
    c.send(str.encode(f"ASSIGNED_PLAYER_{p}"))
    while True:
        try:
            print("receiving message...")
            data = read_pos(c.recv(HEADER).decode(FORMAT))       # stuck
            #for x in [1, 2, 4, 5, 6]:
            #    if switch(x) == data:
            #        reply = set_game_state(data)
            print("recieved message" + make_pos(data) + "p: " + f"{p}" + f"{data}")
            pos[p - 1] = data                              # uppdatera position
            print("updated position" + f"{pos[p-1]}")
            if not data:                                         # avoid error since theres a connection message that cant convert to int
                print("Disconnected client")
                break
            else:
                if data == D_MSG:
                    print(D_MSG)
                    break
                if p == 1:      # if we are player two we send ones position and vice versa
                    reply = pos[1]
                    print("reply to: " + f"{p+1} position: " + make_pos(reply))
                else:
                    reply = pos[0]
                    print("reply to: " + f"{p-1} position: " + make_pos(reply))
                print("Recieved: ", data)
                print("Sending: ", reply)
            print("reply:" + f"{str.encode(make_pos(reply))}")
            c.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Lost connection")
    c.close()

print("Server is starting...")
SERVER.listen(CLIENTS)

curr_player = 0
while True:
    print("Server waiting for connection...")
    conn, addr = SERVER.accept() # waits for a new connection, stores address and object that allows us to communicate back to client
    curr_player += 1
    thread = threading.Thread(target=connect_client, args=(conn, addr, curr_player))
    thread.start()
    #conn.send(str.encode(f"ASSIGNED_PLAYER_{threading.active_count() - 1}"))
    print(f"[Active connections] {threading.active_count() - 1}")