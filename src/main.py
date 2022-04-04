# Kodskelett från: https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
# Import the pygame library and initialise the game engine
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

# -------- Functions ----------
def check_carry(player, event, food):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if player.get_holding() == False:
                if player.get_x_position() - 15 < food.get_x_position() < player.get_x_position() + 15 and player.get_y_position() - 15 < food.get_y_position() < player.get_y_position() + 15:
                    player.set_holding(True)
                    all_sprites.remove(food)


def check_drop(player, event):
    if player.get_holding():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if 290 < player.get_y_position() < 410 and 290 < player.get_x_position() < 410:
                    player.set_holding(False)
                    all_sprites.remove(player)
                    return 1
    return 0

# -------- Main Program Loop ----------

while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_one.move(15, 0, walls, player_two)
            if event.key == pygame.K_LEFT:
                player_one.move(-15, 0, walls, player_two)
            if event.key == pygame.K_UP:
                player_one.move(0, -15, walls, player_two)
            if event.key == pygame.K_DOWN:
                player_one.move(0, 15, walls, player_two)

        number = number + check_drop(player_one, event)
        number = number + check_drop(player_two, event)

        check_carry(player_one, event, food_one)
        check_carry(player_one, event, food_two)

        check_carry(player_two, event, food_one)
        check_carry(player_two, event, food_two)

    # --- Game logic should go here
    # --- Collision detection
    #for wall in walls:

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