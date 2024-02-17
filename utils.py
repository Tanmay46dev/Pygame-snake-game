import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_SIZE = 30
FPS = 15

FOOD_COLOR = "red"


def get_random_food_pos():
    x_pos = random.randint(0, SCREEN_WIDTH // CELL_SIZE)
    y_pos = random.randint(0, SCREEN_HEIGHT // CELL_SIZE)
    return x_pos, y_pos
