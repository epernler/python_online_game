import pygame
from settings import *

vec = pygame.math.Vector2

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(PURPLE)  # the color
        self.rect = self.image.get_rect()
        self.rect.center = (30, size[1] - 30)
        #self.pos = vec(30, size[1] - 30)
        self.holding = False ## Holding food or not

    #def update(self):
        #self.pos.x = pygame.mouse.get_pos()[0]
        #self.pos.y = pygame.mouse.get_pos()[1]
        #self.rect.center = self.pos
    def set_color(self):
        self.image.fill(LIGHT_PINK)

    def get_y_position(self):
        return self.rect.y

    def get_x_position(self):
        return self.rect.x

    def set_y_pos(self, position):
        self.rect.y = position

    def set_x_pos(self, position):
        self.rect.x = position

    def get_holding(self):
        return self.holding

    def set_holding(self, bool):
        self.holding = bool
        if bool == True:
            self.image.fill(PINK)
        else:
            self.image.fill(PURPLE)

    def move(self, dx, dy, walls, other_player):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, walls, other_player)
        if dy != 0:
            self.move_single_axis(0, dy, walls, other_player)

    def move_single_axis(self, dx, dy, walls, other_player):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            self.collision_check(dx, dy, wall)

        # Check for collision with other player
        self.collision_check(dx, dy, other_player)

    def collision_check(self, dx, dy, obj):
        if self.rect.colliderect(obj.rect):
            if dx > 0:  # Moving right; Hit the left side of the wall
                self.rect.right = obj.rect.left
            if dx < 0:  # Moving left; Hit the right side of the wall
                self.rect.left = obj.rect.right
            if dy > 0:  # Moving down; Hit the top side of the wall
                self.rect.bottom = obj.rect.top
            if dy < 0:  # Moving up; Hit the bottom side of the wall
                self.rect.top = obj.rect.bottom