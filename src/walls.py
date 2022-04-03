import pygame
import random
from settings import *

vec = pygame.math.Vector2

class walls(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((250, 10))
        self.image.fill(LIGHT_BLUE)  # the color
        self.rect = self.image.get_rect()
        self.rect.center = (30, size[1] - 30)
        self.pos = vec(random.randint(10, 500), random.randint(10, 100))

    def update(self):
        self.rect.center = self.pos

    def get_y_position(self):
        return self.rect.y

    def get_x_position(self):
        return self.rect.x

    def set_y_pos(self, position):
        self.pos.y = position

    def set_x_pos(self, position):
        self.pos.x = position