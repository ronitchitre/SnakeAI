import random
import pygame
import colors
import classes
from pygame.math import Vector2
# from backend import mdp_make

# initialize pygame
pygame.mixer.init()
pygame.mixer.music.load("Sound/star-wars-theme-song.mp3")
pygame.mixer.music.play()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# game variables
cell_size = 40
cell_number = 20
gameWindow = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)


class Main:
    def __init__(self):
        self.snake = classes.Snake()
        self.food = classes.Food()
        self.score = 0
        bg_img = pygame.image.load("snakebg.jpg")
        self.bg_img = pygame.transform.scale(bg_img, (cell_number*cell_size, cell_number*cell_size))
        self.game_start = False

    def update(self):
        if self.game_start:
            self.snake.move_snake()
            self.check_collision()

    def draw_stuff(self):
        gameWindow.blit(self.bg_img, (0,0))
        self.snake.draw_snake(gameWindow)
        self.food.draw_food(gameWindow)
        text_screen(f"Score {self.score}", colors.red, 300, 80)

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food = classes.Food()
            self.snake.add_block()
            self.score += 1
            self.snake.crunch_sound.play()
            for block in self.snake.body[1:]:
                if block == self.food.pos:
                    self.food = classes.Food()


# function to print text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# main game loop

# loop variables
game_quite = False
game_over = False
score = 0
score_color = colors.red
fps = 60
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while not game_quite:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quite = True
        if event.type == SCREEN_UPDATE:
            main_game.update()
            # game_over = main_game.snake.check_death()
            game_over = main_game.snake.check_death() is 1
            if game_over:
                main_game = Main()
        if event.type == pygame.KEYDOWN:
            main_game.game_start = True
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y == 0:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y == 0:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x == 0:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x == 0:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_SPACE:
                game_quite = True

    main_game.draw_stuff()

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
