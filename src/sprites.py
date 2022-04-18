from player import *
from foods import *
from walls import *

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

D_MSG = "DISCONNECT"