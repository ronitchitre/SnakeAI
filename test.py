from pygame.math import Vector2
import numpy as np
from random import random, choice
v1 = Vector2(1, 1)
v2 = Vector2(0, -1)
angle_v1_v2_degree = v2.angle_to(v1)
print(angle_v1_v2_degree)

