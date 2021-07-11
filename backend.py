from pygame.math import Vector2
import classes
import numpy as np
from random import random
from random import randint
print("hi")

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
gamma = 0.9

class State:
	def __init__(self,argstate):
		self.left = argstate[0]
		self.front = argstate[1]
		self.right = argstate[2]
		self.foodup = argstate[3]
		self.fooddown = argstate[4]
		self.foodright = argstate[5]
		self.foodleft = argstate[6]
		self.index = binary_to_decimal(argstate)

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
		

def check_state(food, snake):
	left = snake.move_snake_backend("left").check_death()
	front = snake.move_snake_backend("front").check_death()
	right = snake.move_snake_backend("right").check_death()
	relative_pos = food.pos - snake.body[0]
	rel_angle = snake.direction.angle_to(relative_pos)
	rel_angle2 = rel_angle + 360
	if food.pos == snake.body[0]:
		foodup = 0
		fooddown = 0
		foodleft = 0
		foodright = 0
	if rel_angle == 0 or rel_angle == 360 or rel_angle2 == 0:
		foodup = 1
		fooddown = 0
		foodleft = 0
		foodright = 0
	elif rel_angle == 180 or rel_angle2 == 180:
		foodup = 0
		fooddown = 1
		foodleft = 0
		foodright = 0
	elif rel_angle == 90 or rel_angle2 == 90:
		foodup = 0
		fooddown = 0
		foodleft = 0
		foodright = 1
	elif rel_angle == 270 or rel_angle2 == 270:
		foodup = 0
		fooddown = 0
		foodleft = 1
		foodright = 0
	elif (rel_angle > 0 and rel_angle < 90) or (rel_angle2 > 0 and rel_angle2 < 90):
		foodup = 1
		fooddown = 0
		foodleft = 0
		foodright = 1
	elif (rel_angle > 270 and rel_angle < 360) or (rel_angle2 > 270 and rel_angle2 < 360):
		foodup = 1
		fooddown = 0
		foodleft = 1
		foodright = 0
	elif (rel_angle > 90 and rel_angle < 180) or (rel_angle2 > 90 and rel_angle2 < 180):
		foodup = 0
		fooddown = 1
		foodleft = 0
		foodright = 1
	elif (rel_angle > 180 and rel_angle < 270) or (rel_angle2 > 180 and rel_angle2 < 270):
		foodup = 0
		fooddown = 1
		foodleft = 1
		foodright = 0




	return State([left, front, right, foodup, fooddown, foodleft, foodright])



# def make_state_set():
# 	state_set = {}
# 	for state_index in range(num_states):
# 		state_index_binary = decimal_to_binary(state_index)
# 		state = State(state_index_binary)
# 		state_set[state.index] = state
# 	return state_set

def e_greedy_policy(state_action_matrix, state_index, e = 0):
	if random() <= e:
		explore = randint(0, 2)
		return [explore, state_action_matrix[state_index][explore]]
	else:
		check_array = state_action_matrix[state_index]
		return [np.random.choice(np.flatnonzero(np.isclose(check_array, check_array.max()))), np.argmax(check_array)]


# state_set = make_state_set()
# state_action_matrix = np.zeros([num_states, 3])

def qlearning(max_iter, e):
	# state_set = make_state_set()
	state_action_matrix = np.zeros([num_states, 3])
	i = 0
	j = 0
	snake = classes.Snake(False)
	snake.direction = up
	for _ in range(max_iter):
		i+=1
		print(i)
		food = classes.Food(False)
		cur_state = check_state(food, snake)
		while True:
			# action_index = e_greedy_policy(state_action_matrix, cur_state.index,)
			# print(cur_state.index)
			action_value = e_greedy_policy(state_action_matrix, cur_state.index, e)
			action_index = action_value[0]
			if action_index == 0:
				snake.direction = snake.direction.rotate(-90)
				snake.move_snake()
				nxt_state = check_state(food, snake)
			elif action_index == 1:
				snake.move_snake()
				nxt_state = check_state(food, snake)
			elif action_index == 2:
				snake.direction = snake.direction.rotate(90)
				snake.move_snake()
				nxt_state = check_state(food, snake)
			reward = 0
			if abs(snake.body[0].x - food.pos.x) == 1 and abs(snake.body[0].y - food.pos.y) == 1:
				reward = 5
			elif snake.body[0] == food.pos:
				reward = 500
				# snake.add_block()
				# break
				# food = classes.Food(False)
			if snake.check_death() == 1:
				reward = -500
				food = classes.Food(False)
				snake = classes.Snake(False)
				j+=1
			nxt_greedy_state_value = e_greedy_policy(state_action_matrix, nxt_state.index, 0)[1]
			state_action_matrix[cur_state.index][action_index] += alpha*(reward + gamma*nxt_greedy_state_value - state_action_matrix[cur_state.index][action_index])
			# print(cur_state.left, cur_state.topleft, cur_state.front, cur_state.topright, cur_state.right)
			if reward == 500:
				snake.add_block()
				break
			cur_state = nxt_state
			# print(snake.body, snake.direction,food.pos,reward)
			# print(len(snake.body))
	print(j)
	return state_action_matrix

def write_file(state_action_matrix, max_iter):
	address = r"solutions\{}.txt".format(max_iter)
	file = open(address, "+w")
	for state_action in state_action_matrix:
		for action in state_action:
			to_write = str(float(action))
			file.write(f"{to_write} ")
		file.write("\n")
	file.close()

if __name__ == "__main__":
	x = qlearning(50000, 0.1)
	write_file(x, 50000)

# print(decimal_to_binary(8))
