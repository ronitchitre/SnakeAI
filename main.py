import random
import pygame
import colors

# initialize pygame
pygame.init()

# game variables
cell_size = 40
cell_number = 20
gameWindow = pygame.display.set_mode((cell_size*cell_number, cell_size*cell_number))

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)


# function to print text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# main game loop
def game_loop():
    # loop variables
    game_quite = False
    game_over = False
    score = 0
    score_color = colors.red

    food_x = random.randint(50, 400)  # x and y coordinates of food
    food_y = random.randint(50, 250)
    food_size = 25  # size of food
    food_col = colors.green  # this represents green color
    accuracy = 10  # how close the snake must be to eat the food

    fps = 100

    while not game_quite:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quite = True
                pygame.quit()
                quit()
        gameWindow.fill(colors.white)
        pygame.display.update()
        clock.tick(fps)


game_loop()
