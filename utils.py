import random
import pygame.font

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_SIZE = 30
FPS = 15

FOOD_COLOR = "red"


def get_font(size: int=36):
    return pygame.font.SysFont(None, size)


def get_random_food_pos() -> tuple:
    x_pos = random.randint(0, (SCREEN_WIDTH - (CELL_SIZE * 2)) // CELL_SIZE)
    y_pos = random.randint(0, (SCREEN_HEIGHT - (CELL_SIZE * 2)) // CELL_SIZE)
    return x_pos, y_pos

def get_high_score() -> int:
    with open("highscore.txt") as f:
        return int(f.read())

def set_high_score(score: int):
    with open("highscore.txt", "w") as f:
        return f.write(str(score))
    
