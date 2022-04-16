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

# Våra klienters position och space - variabler
pos = [(300, 350), (350, 350)]
space = [False, False]

def connect_client(c, a, p):                            # Vi kör denna metod i en thread för varje klient
    other_p = 2 if p == 1 else 1
    print(f"[New connection] {a} connected")
    c.send(str.encode(f"ASSIGNED_PLAYER_{p}"))          # Vi låter klienten veta vilken spelare de är
    reply = ""
    while True:
        try:                                        # Try undviker att allt kraschar ifall ett meddelande inte går att ta emot / skickas
            data = c.recv(HEADER).decode(FORMAT)    # Vi tar emot meddelande från klienten
            if space[other_p - 1]:                  # Ifall den andra spelaren har klickat space...
                c.sendall(str.encode("SPACE"))      # Så skickar vi "SPACE" till denna klient, istället för andra spelarens position
                space[other_p - 1] = False          # Återställer andra spelarens space-variabel
            else:                                   # Annars skickar vi andra spelarens position
                if not data:
                    print("Disconnected client")
                    break
                else:
                    if data == D_MSG:
                        print("Client disconnected")
                        break
                    if data == "SPACE":                     # Ifall klienten klickat space
                        space[p - 1] = True                 # ... så ser vi till att den andra klienten kan läsa det nästa loop
                    else:
                        data = read_pos(data)               # Annars, om klienten inte klickat space så läser vi in klientens position
                        pos[p - 1] = data                   # ... och uppdaterar den
                    reply = pos[1] if p == 1 else pos[0]
                    c.sendall(str.encode(make_pos(reply)))  # vi skickar som den andra klientens position som svar
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
    print(f"[Active connections] {threading.active_count() - 1}")