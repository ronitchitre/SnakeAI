import random
import pygame
import colors
from pygame.math import Vector2
import numpy as np
import classes
from backend import State, check_state,e_greedy_policy
print("imports done")

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

    def get_matrix(self, address):
        state_action_matrix = []
        file = open(address, "r")
        while True:
            row_str = file.readline()
            if row_str == "":
                break
            else:
                row_str = list(row_str.split())
                row = list(map(float, row_str))
                state_action_matrix.append(row)
        self.state_action_matrix = np.array(state_action_matrix)

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
main_game.get_matrix(r"solutions\50000.txt")

while not game_quite:
    state_action_matrix = main_game.state_action_matrix
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quite = True
        if event.type == SCREEN_UPDATE:
            main_game.update()
            # game_over = main_game.snake.check_death()
            # game_over == main_game.snake.check_death() is 1
            if main_game.snake.check_death() == 1:
                main_game = Main()
                main_game.get_matrix(r"solutions\50000.txt")
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

    if main_game.game_start:
        cur_state = check_state(main_game.food, main_game.snake)
        cur_state_index = cur_state.index
        check_array = state_action_matrix[cur_state_index]
        print(check_array)
        optimal_action = e_greedy_policy(state_action_matrix, cur_state_index)[0]
        print(optimal_action)
        if optimal_action == 0:
            main_game.snake.direction = main_game.snake.direction.rotate(-90)
        elif optimal_action == 2:
            main_game.snake.direction = main_game.snake.direction.rotate(90) 
        # elif optimal_action == 1:
            # main_game.snake.move_snake()

    main_game.update()
    main_game.draw_stuff()


    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
# x = get_matrix(r"solutions\10.txt")
# print(x)