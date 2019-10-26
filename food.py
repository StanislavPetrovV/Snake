import pygame
from random import randint


class Food:
    COLOR = (255, 0, 0)
    SIDE = 25

    def __init__(self, surface):
        self.surface = surface
        self.x = self.SIDE
        self.y = self.SIDE

    def add_food(self):
        pygame.draw.rect(self.surface, self.COLOR, (self.x, self.y, self.SIDE, self.SIDE))

    def new_foodxy(self):
        self.x = randint(self.SIDE, self.surface.get_width() - self.SIDE)
        self.y = randint(self.SIDE, self.surface.get_height() - self.SIDE)

    def is_eaten(self, snake_x, snake_y):
        if abs(snake_x - self.x) < Food.SIDE - 2 and abs(snake_y - self.y) < Food.SIDE - 2:
            return True
        return False