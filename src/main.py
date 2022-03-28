# Kodskelett från: https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
# Import the pygame library and initialise the game engine
import pygame
from paddles_ball import*

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Sprites (paddles & ball)
all_sprites = pygame.sprite.Group()

paddle_one = paddles_ball()
all_sprites.add(paddle_one)

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop

    # --- Game logic should go here
    all_sprites.update()

    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLUE)

    # Sprites
    all_sprites.draw(screen)

    # Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()