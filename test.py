from pygame.math import Vector2
import numpy as np
from random import random, choice
file = open('high_score.txt', 'r')
hs = file.read()
print(hs)
file.close()
file = open('high_score.txt', '+w')
file.write('3')
file.close()

