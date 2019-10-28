import pygame
from random import randint

class Food:
    COLOR = (255, 0, 0)
    SIDE = 25

    def __init__(self, surface):
        self.surface = surface
        self.x = self.SIDE
        self.y = self.SIDE
        self.set_x = set()
        self.set_y = set()

    def add_food(self):
        pygame.draw.rect(self.surface, self.COLOR, (self.x, self.y, self.SIDE, self.SIDE))
        self.set_x = set(range(self.x, self.x + self.SIDE + 1))
        self.set_y = set(range(self.y, self.y + self.SIDE))

    def new_foodxy(self, snake_side):
        self.x = randint(snake_side, self.surface.get_width() - snake_side)
        self.y = randint(snake_side, self.surface.get_height() - snake_side)

    def is_eaten(self, snake_x, snake_y, snake_side):
        if set(range(snake_x, snake_x + snake_side + 1)) & self.set_x and set(range(snake_y, snake_y + snake_side + 1)) & self.set_y:
            return True
        return False
