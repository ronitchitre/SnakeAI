import pygame
from pygame.math import Vector2


class food:
    def __init(self):
        self.x = 5
        self.y = 9
        self.pos = Vector2(self.x, self.y)


class Snake:
    def __init__(self):
        self.pos = [450, 300]
        self.side = 30
        self.vel_dir = [0, 0]
        self.vel_mag = 5
        self.turn = "0"
        self.body = [[self.pos[0], self.pos[1], self.side, self.side, self.vel_dir, self.turn]]
        self.length = 10
        self.len_increment = 500
        self.headpic = pygame.image.load("snakehead_up.png").convert_alpha()
        self.body_hor = pygame.image.load("snake_bod_hor.png").convert_alpha()
        self.body_ver = pygame.image.load("snake_bod_ver.png").convert_alpha()
        self.body_corner4 = pygame.image.load("snake_corner_4.png").convert_alpha()
        self.body_corner3 = pygame.image.load("snake_corner_3.png").convert_alpha()
        self.body_corner2 = pygame.image.load("snake_corner_2.png").convert_alpha()
        self.body_corner1 = pygame.image.load("snake_corner_1.png").convert_alpha()
