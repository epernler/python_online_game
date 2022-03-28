import pygame
from settings import *

vec = pygame.math.Vector2

class paddles_ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 30))
        self.image.fill((153, 153, 255))  # the color
        self.rect = self.image.get_rect()
        self.rect.center = (size[0] / 2, size[1] - 30)
        self.pos = vec(30, size[1] - 30)

    def update(self):
        self.pos.y = pygame.mouse.get_pos()[1]
        self.rect.center = self.pos

    def get_y_position(self):
        return self.rect.y

    def set_y_pos(self, position):
        self.pos.y = position

    def set_x_pos(self, position):
        self.pos.y = position
