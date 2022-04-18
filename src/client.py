from typing import Any

import socket
import time
import threading
import pygame

from sprites import *

space = False
number = 0
win_message = ""

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crazy Game")
clock = pygame.time.Clock()
in_game = True

# Socket configuration
PORT = 8080
HEADER = 2048
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish three way handshake
SERVER.connect(ADDRESS)

def send_msg(msg):
    try:
        SERVER.send(str.encode(msg))                # Vi skickar meddelandet till servern
        return SERVER.recv(HEADER).decode()         # ... och returnerar serverns svar
    except socket.error as e:
        print(e)


# -------- Functions ----------

def set_otherplayer_position(tuple):
    other_player.set_x_pos(tuple[0])
    other_player.set_y_pos(tuple[1])

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def check_carry(player, food):
    if not player.get_holding():                                           # om player inte håller i rektangel
        if player.get_x_pos() - 15 < food.get_x_pos() < player.get_x_pos() + 15 and player.get_y_pos() - 15 < food.get_y_pos() < player.get_y_pos() + 15:
            player.set_holding(True)                                            # och är på rektangeln så håller playern nu maten, den försvinner
            all_sprites.remove(food)

def check_drop(player):
    if player.get_holding():                                                    # if you carry rectangle
        if 290 < player.get_y_pos() < 410 and 290 < player.get_x_pos() < 410:   # if your pos is middle circle
            player.set_holding(False)                                           # you're not holding no more
            all_sprites.remove(player)                                          # you are removed from game
            return 1
        else:
            return 0
    else:
        return 0

def event_handler():
    global number
    global win_message
    global space
    global in_game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                this_player.move(15, 0, walls, other_player)
            if event.key == pygame.K_LEFT:
                this_player.move(-15, 0, walls, other_player)
            if event.key == pygame.K_UP:
                this_player.move(0, -15, walls, other_player)
            if event.key == pygame.K_DOWN:
                this_player.move(0, 15, walls, other_player)
            if event.key == pygame.K_SPACE:
                number += check_drop(this_player)  # check if returned block to middle for both players
                if number == 1:
                    win_message = "WIN!"
                check_carry(this_player, food_one)  # check if on food and in that case eat it
                check_carry(this_player, food_two)
                space = True

# Vi tar emot första meddelandet från servern som säger oss vilken spelare vi är
msg = SERVER.recv(HEADER).decode(FORMAT)
if msg == "ASSIGNED_PLAYER_1":
    this_player = player_one
    other_player = player_two
    print("Assigned player one!")
elif msg == "ASSIGNED_PLAYER_2":
    this_player = player_two
    other_player = player_one
    print("Assigned player two!")

# Main game-loop
while in_game:
    if space == True:            # Om vi space:at skickar vi det till servern, tar emot svaret från servern och
        # återställer sedan space variabeln
        reply = send_msg("SPACE")
        space = False
    else:                        # Annars skickar vi vår klients position
        pos = make_pos((this_player.get_x_pos(), this_player.get_y_pos()))
        reply = send_msg(pos)
    try:                         # Vi använder serverns svar för att uppdatera den andra klientens position eller
        # klicka space åt den
        if reply == "SPACE":
            number = number + check_drop(other_player)  # check if returned block to middle for both players
            if number == 1:
                win_message = "LOSE"
            check_carry(other_player, food_one)  # check if on food and in that case eat it
            check_carry(other_player, food_two)
        else:
            set_otherplayer_position(read_pos(reply))
    except:
        pass

    all_sprites.update()

    if number != 1:                     # Så länge ingen vunnit ...
        event_handler()
        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(BLUE)

        # Draw the net
        pygame.draw.circle(screen, BLACK, [350, 350], 60)

        # Count
        myFont = pygame.font.SysFont("Open Sans", 70)
        randNumLabel = myFont.render("GO", 0, LAVENDER)
        screen.blit(randNumLabel, (320, 330))

        # Sprites
        all_sprites.draw(screen)
    else:                               # Annars om vunnit så visar vi slutskärm
        # Game win screen
        screen.fill(PINK)
        myFont = pygame.font.SysFont("Open Sans", 100)
        randNumLabel = myFont.render(win_message, 0, WHITE)
        screen.blit(randNumLabel, (300, 250))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
send_msg(D_MSG)
