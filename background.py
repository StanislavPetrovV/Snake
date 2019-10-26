import pygame
from random import  randint, randrange

class BG:
    def __init__(self, surface):
        self.surf = surface
        self.max_obj = 250
        self.width = surface.get_width()
        self.height = surface.get_height()
        self.x = [randrange(-self.width, 2 * self.width) for i in range(self.max_obj)]
        self.y = [randrange(-self.height, 2 * self.height) for i in range(self.max_obj)]
        self.radius = [randint(2, 4) for i in range(self.max_obj)]
        self.speed = [randint(1, 4) for i in range(self.max_obj)]
        self.color = [(randrange(255), randrange(255), randrange(255)) for i in range(self.max_obj)]

    def draw(self, directon):
        if directon == 'l':
            self.x = [x + r for x,r in zip(self.x, self.speed)]
        elif directon == 'r':
            self.x = [x - r for x, r in zip(self.x, self.speed)]
        elif directon == 'u':
            self.y = [y + r for y, r in zip(self.y, self.speed)]
        elif directon == 'd':
            self.y = [y - r for y, r in zip(self.y, self.speed)]
        [pygame.draw.circle(self.surf, self.color[i], (self.x[i], self.y[i]), self.radius[i]) if i % 5
         else  pygame.draw.circle(self.surf, (randrange(255), randrange(255), randrange(255)), (self.x[i], self.y[i]), self.radius[i])
         for i in range(self.max_obj)]



