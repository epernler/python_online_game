# Kodskelett från: https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
# Import the pygame library and initialise the game engine
import pygame
from player import *
from foods import *

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

number = 0

# Sprites (paddles & ball)
all_sprites = pygame.sprite.Group()

player_one = player()

food_one = foods()

all_sprites.add(player_one)
all_sprites.add(food_one)

# -------- Functions ----------
def check_carry(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if 230 > player_one.get_y_position() or player_one.get_y_position() > 410 and 230 > player_one.get_x_position() or player_one.get_y_position() > 410:
                if player_one.get_x_position() - 15 < food_one.get_x_position() < player_one.get_x_position() + 15 and player_one.get_y_position() - 15 < food_one.get_y_position() < player_one.get_y_position() + 15:
                    player_one.set_holding(True)
                    # food_one.change_color()
                    all_sprites.remove(food_one)

def check_drop(event):
    if player_one.get_holding():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                all_sprites.add(food_one)
                food_one.set_y_pos(player_one.get_y_position())
                food_one.set_x_pos(player_one.get_x_position())
                player_one.set_holding(False)
                if 230 < player_one.get_y_position() < 410 and 230 < player_one.get_x_position() < 410:
                    return 1
    return 0

# -------- Main Program Loop ----------

while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        number = number + check_drop(event)
        check_carry(event)

    # --- Game logic should go here

    all_sprites.update()

    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLUE)

    # Draw the net
    pygame.draw.circle(screen, LAVENDER, [350, 350], 100)

    # Count
    myFont = pygame.font.SysFont("Open Sans", 70)
    randNumLabel = myFont.render(str(number), 0, BLACK)
    screen.blit(randNumLabel, (335, 330))

    # Sprites
    all_sprites.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()