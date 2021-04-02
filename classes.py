import pygame
import colors
from pygame.math import Vector2
from random import randint

cell_size = 20
cell_number = 30


class Food:
    def __init__(self):
        self.x = randint(0, cell_number - 1)
        self.y = randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.pic = pygame.image.load("food.png", ).convert_alpha()

    def draw_food(self, gameWindow):
        food_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        gameWindow.blit(self.pic, food_rect)


class Snake:
    def __init__(self):
        self.body = [Vector2(15, 15), Vector2(15, 16), Vector2(15, 17)]
        self.direction = Vector2(0, 0)
        self.head_up = pygame.image.load("snakehead_up.png").convert_alpha()
        self.head_down = pygame.image.load("snakehead_down.png").convert_alpha()
        self.head_left = pygame.image.load("snakehead_left.png").convert_alpha()
        self.head_right = pygame.image.load("snakehead_right.png").convert_alpha()

        self.bod_ver = pygame.image.load("snake_bod_ver.png").convert_alpha()
        self.bod_hor = pygame.image.load("snake_bod_hor.png").convert_alpha()

        self.tail_up = pygame.image.load("snake_tail_-y.png").convert_alpha()
        self.tail_down = pygame.image.load("snake_tail_+y.png").convert_alpha()
        self.tail_left = pygame.image.load("snake_tail_-x.png").convert_alpha()
        self.tail_right = pygame.image.load("snake_tail_+x.png").convert_alpha()

        self.snake_corner1 = pygame.image.load("snake_corner_1.png").convert_alpha()
        self.snake_corner2 = pygame.image.load("snake_corner_2.png").convert_alpha()
        self.snake_corner3 = pygame.image.load("snake_corner_3.png").convert_alpha()
        self.snake_corner4 = pygame.image.load("snake_corner_4.png").convert_alpha()

        self.head = pygame.image.load("snakehead_up.png").convert_alpha()
        self.tail = pygame.image.load("snake_tail_-y.png").convert_alpha()

    def draw_snake(self, gameWindow):
        self.update_head()
        self.update_tail()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                gameWindow.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                gameWindow.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    gameWindow.blit(self.bod_ver, block_rect)
                elif previous_block.y == next_block.y:
                    gameWindow.blit(self.bod_hor, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        gameWindow.blit(self.snake_corner4, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        gameWindow.blit(self.snake_corner3, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        gameWindow.blit(self.snake_corner1, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        gameWindow.blit(self.snake_corner2, block_rect)


    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

    def add_block(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

    def check_death(self):
        if self.body[0].x > 38 or self.body[0].x < 1 or self.body[0].y > 38 or self.body[0].y < 1:
            return True
        elif self.body[0] in self.body[1:] and self.direction != Vector2(0, 0):
            return True
        else:
            return False

    def update_head(self):
        if self.direction == Vector2(1, 0):
            self.head = self.head_right
        elif self.direction == Vector2(-1, 0):
            self.head = self.head_left
        elif self.direction == Vector2(0, 1):
            self.head = self.head_down
        elif self.direction == Vector2(0, -1):
            self.head = self.head_up

    def update_tail(self):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
