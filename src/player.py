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
        self.pos = vec(30, size[1] - 30)
        self.holding = False ## Holding food or not

    def update(self):
        self.pos.x = pygame.mouse.get_pos()[0]
        self.pos.y = pygame.mouse.get_pos()[1]
        self.rect.center = self.pos

    def get_y_position(self):
        return self.rect.y

    def get_x_position(self):
        return self.rect.x

    def set_y_pos(self, position):
        self.pos.y = position

    def set_x_pos(self, position):
        self.pos.x = position

    def get_holding(self):
        return self.holding

    def set_holding(self, bool):
        self.holding = bool
        if bool == True:
            self.image.fill(PINK)
        else:
            self.image.fill(PURPLE)