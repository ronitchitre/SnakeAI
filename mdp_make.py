from pygame.math import Vector2
import classes
import pygame
# food_pos is food position
# snake_pos is array of blocks that the snake occupies
# make a state object [b1,b2,b3,b4,b5,a] and index are attributes. then make a 3d array with x as state index y as actin index and z as value
# to convert to index we can just convert the binary to decimal also a can be split to bottom/top and left/right
# action 0,1,2 corresponds to left nothing right
# death is 1 live is 0
# right is 1 
# up is 1

up = Vector2(0, -1)
down = Vector2(0, 1)
right = Vector2(1, 0)
left = Vector2(-1, 0)
num_states = 128
alpha = 0.5
e = 0.1

class State:
	def __init__(self,argstate):
		self.left = argstate[0]
		self.topleft = argstate[1]
		self.front = argstate[2]
		self.topright = argstate[3]
		self.right = argstate[4]
		self.foodx = argstate[5]
		self.foody = argstate[6]
		self.index = binary_to_decimal(argstate)

	def __init__(self, snakepos, foodpos, snakedir):
		headpos = snakepos[0]
		leftpos = headpos + left
		topleft = headpos + left + top
		front = headpos + up
		topright = headpos + right + top
		right = headpos + right
		self.left = check_death()
		self.topleft = argstate[1]
		self.front = argstate[2]
		self.topright = argstate[3]
		self.right = argstate[4]
		self.foodx = argstate[5]
		self.foody = argstate[6]


def binary_to_decimal(binary):
	i = 0
	decimal = 0
	for b in binary:
		decimal += (2**(i))*b
		i += 1 
	return decimal

def decimal_to_binary(decimal):
	binary = []
	if decimal == 0:
		return [0, 0, 0, 0, 0, 0, 0]
	while decimal > 0:
		binary.append(decimal % 2)
		decimal = int(decimal / 2)
	while len(binary) < 7:
		binary.append(0)
	return binary

# def move_snake(action, snakepos):
# 	body_copy = snakepos[:-1]
# 	body_copy.insert(0, body_copy[0] + action)
# 	return body_copy

# def check_death(snakepos, snakedir):
# 	if snakepos[0].x > 19 or snakepos[0].x < 0 or snakepos[0].y > 19 or snakepos[0].y < 0:
# 		return 1
# 	elif snakepos[0] in snakepos[1:] and snakedir != Vector2(0, 0):
# 		return 1
# 	else:
# 		return 0
		

def check_state(food, snake, state):
    state.left = snake.move_snake_backend("left").check_death()
    state.topleft = snake.move_snake_backend("topleft").check_death()
    state.front = snake.move_snake_backend("front").check_death()
    state.topright = snake.move_snake_backend("topright").check_death()
    state.right = snake.move_snake_backend("right").check_death()
    if food.pos.x >= snake.body[0].x:
    	state.foodx = 1
    else:
    	state.foodx = 0
    if food.pos.y <= snake.body[0].y:
    	state.foody = 1
    else:
    	state.foody = 0
    return state



def make_state_set():
	state_set = {}
	for state_index in range(num_states):
		state_index_binary = decimal_to_binary(state_index)
		state = State(state_index_binary)
		state_set[state.index] = state
	return state_set

state_set = make_state_set()
state_action_matrix = np.zeros([num_states, 3])





