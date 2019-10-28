import pygame

class Snake:
    COLOR = [0, 170, 0]
    SIDE = 15
    lenght = 2
    vel = 10

    def __init__(self, surface):
        self.surface = surface
        self.x = surface.get_width() // 2
        self.y = surface.get_height() // 4
        self.XY = [(self.x, self.y)]
        self.direction = 'd'

    def add_lenght(self):
        self.lenght += 1
        self.SIDE += 1
        self.COLOR[1] += 1
        self.COLOR[1] = min(self.COLOR[1], 255)

    def get_snake(self):
        self.XY += [(self.x, self.y)]
        self.XY = self.XY[-self.lenght:]
        for kx, ky in self.XY:
            pygame.draw.rect(self.surface, self.COLOR, (kx, ky, self.SIDE, self.SIDE))

    def move_snake(self, key):
        if key == 'l':
            self.x -= self.vel
            self.get_snake()
        if key == 'r':
            self.x += self.vel
            self.get_snake()
        if key == 'u':
            self.y -= self.vel
            self.get_snake()
        if key == 'd':
            self.y += self.vel
            self.get_snake()