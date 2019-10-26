import pygame
import sys
from pygame.locals import *
import tkinter as tk
import os
from snake import *
from food import *
from background import *


class Game:
    SIZE = WIDTH, HEIGHT = (600, 600)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    fps = 15
    score = 0

    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = f'{(tk.Tk().winfo_screenwidth() - self.WIDTH) // 2},' \
                                             f'{(tk.Tk().winfo_screenheight() - self.HEIGHT) // 2}'
        pygame.init()
        self.surf = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.bg = BG(self.surf)
        self.snake = Snake(self.surf)
        self.food = Food(self.surf)
        self.font_score = pygame.font.Font(None, 22)
        self.font_end = pygame.font.Font(None, 48)
        self.play()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[K_LEFT] or keys[K_a]:
                if self.snake.direction != 'r':
                    self.snake.direction = 'l'
            elif keys[K_RIGHT] or keys[K_d]:
                if self.snake.direction != 'l':
                    self.snake.direction = 'r'
            elif keys[K_UP] or keys[K_w]:
                if self.snake.direction != 'd':
                    self.snake.direction = 'u'
            elif keys[K_DOWN] or keys[K_s]:
                if self.snake.direction != 'u':
                    self.snake.direction = 'd'

            if self.food.is_eaten(self.snake.x, self.snake.y):
                self.snake.add_lenght()
                self.food.new_foodxy()
                self.score += 1
                self.fps += 1

            if len(self.snake.XY) != len(set(self.snake.XY)):
                break

            if (self.snake.x < 0 or self.snake.y < 0 or self.snake.x + self.snake.SIDE > self.WIDTH
                    or self.snake.y + self.snake.SIDE > self.HEIGHT):
                break

            self.draw()
        self.game_over()

    def draw(self):
        self.surf.fill(self.BLACK)
        self.surf.blit(self.font_score.render(f'SCORE: {self.score}', 1, (255, 165, 0)), (self.WIDTH - 80, 5))

        self.bg.draw(self.snake.direction)
        self.food.add_food()
        self.snake.move_snake(self.snake.direction)

        pygame.display.update()
        self.clock.tick(self.fps)

    def game_over(self):
        while True:
            self.surf.blit(self.font_end.render(f'YOUR SCORE: {self.score}', 1, (255, 165, 0)),
                           (self.WIDTH // 2 - 130, self.HEIGHT // 3))
            self.clock.tick(self.fps)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == '__main__':
    Game()
