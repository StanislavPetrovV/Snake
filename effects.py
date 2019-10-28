import pygame
from random import randint, choice

class Effect:
    RANGE = 30
    NUMBER = 15
    color = 255
    list_effects = []
    directions = []
    sizes = []

    def __init__(self, surf):
        self.surf = surf

    def run(self, trigger, x, y):
        if trigger:
            self.color = 255
            self.list_effects = [(randint(x - self.RANGE + 12, x + self.RANGE + 12),
                                  randint(y - self.RANGE + 12, y + self.RANGE - 12))
                                  for i in range(self.NUMBER)]
            self.directions = [(randint(-1, 1), randint(-1, 1)) for i in range(self.NUMBER)]
            self.sizes = [(randint(1, 7), randint(1, 7)) for i in range(self.NUMBER)]

        for i, xy in enumerate(self.list_effects):
            pygame.draw.rect(self.surf, (max(self.color, 120), 0, 0), (*xy, *self.sizes[i]))

        self.list_effects = [(xy[0] - d[0], xy[1] - d[1]) for xy, d in zip(self.list_effects, self.directions)]

        self.color -= 3
