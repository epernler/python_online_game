import socket
import time
import threading
import pygame

from player import *
from foods import *
from walls import *

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crazy Game")
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Sprites
all_sprites = pygame.sprite.Group()

player_one = player()
player_two = player()

food_one = foods()
food_two = foods()

# Walls
wall_one = walls()
wall_two = walls()
wall_three = walls()
wall_four = walls()

walls = [wall_one, wall_two, wall_three, wall_four]

all_sprites.add(player_one)
all_sprites.add(player_two)
all_sprites.add(food_one)
all_sprites.add(food_two)
all_sprites.add(wall_one)
all_sprites.add(wall_two)
all_sprites.add(wall_three)
all_sprites.add(wall_four)

#--------- Set up map -------
wall_one.set_x_pos(200)
wall_one.set_y_pos(200)

wall_two.set_x_pos(150)
wall_two.set_y_pos(400)

wall_three.set_x_pos(550)
wall_three.set_y_pos(300)

wall_four.set_x_pos(500)
wall_four.set_y_pos(100)

food_one.set_x_pos(20)
food_one.set_y_pos(20)

food_two.set_x_pos(680)
food_two.set_y_pos(20)

player_one.set_x_pos(300)
player_one.set_y_pos(350)

player_two.set_x_pos(350)
player_two.set_y_pos(350)
player_two.set_color()

number = 0

# Socket configuration
PORT = 8080
HEADER = 8
FORMAT = "utf-8"
D_MSG = "Client disconnected"
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT.connect(ADDRESS)

def send_msg(msg):
    m = msg.encode(FORMAT)                      # encode message string into a byte object
    m_len = len(m)
    s_len = str(m_len).encode(FORMAT)           # length of message in string
    s_len += b' ' * (HEADER - len(s_len))       #
    SERVER.send(s_len)
    SERVER.send(m)
    print(SERVER.recv(2048).decode(FORMAT))

while in_game:

    # keyevents här, för varje så skickas iväg ett specifikt meddelande som definieras i server

    for event in pygame.event.get():  # User did something
        # skicka input till servern och sedan få game state från
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #input från servern player_one
                # send to server player_one.getx 1 / 5
                player_one.move(15, 0, walls, player_two)
            if event.key == pygame.K_LEFT:
                # 2 / 6
                player_one.move(-15, 0, walls, player_two)
            if event.key == pygame.K_UP:
                # 3 / 7
                player_one.move(0, -15, walls, player_two)
            if event.key == pygame.K_DOWN:
                # 4 /8
                player_one.move(0, 15, walls, player_two)
            if event.key == pygame.K_SPACE:
                number = number + check_drop(player_one)
                number = number + check_drop(player_two)

                check_carry(player_one, food_one)
                check_carry(player_one, food_two)

                check_carry(player_two, food_one)
                check_carry(player_two, food_two)

    all_sprites.update()

    if number != 2:
        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(BLUE)

        # Draw the net
        pygame.draw.circle(screen, BLACK, [350, 350], 60)

        # Count
        myFont = pygame.font.SysFont("Open Sans", 70)
        randNumLabel = myFont.render(str(number) + "/2", 0, LAVENDER)
        screen.blit(randNumLabel, (320, 330))

        # Sprites
        all_sprites.draw(screen)
    else:
        # Game win screen
        screen.fill(PINK)
        myFont = pygame.font.SysFont("Open Sans", 100)
        randNumLabel = myFont.render("Win!", 0, WHITE)
        screen.blit(randNumLabel, (300, 250))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

send_msg("Hello bitch")
send_msg(D_MSG)