import pygame
from utils import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class Snake:
    def __init__(self, start_pos: list):
        self.parts = [start_pos, [1, 0], [0, 0]]
        self.direction_x = 1
        self.direction_y = 0

    def is_game_over(self) -> bool:
        head_x = self.parts[0][0]
        head_y = self.parts[0][1]
        return head_x * CELL_SIZE >= SCREEN_WIDTH or head_y * CELL_SIZE >= SCREEN_HEIGHT or head_x * CELL_SIZE < 0 or head_y * CELL_SIZE < 0

    def grow(self):
        pass

    def draw(self, surface: pygame.Surface):
        for i in range(len(self.parts)):
            part = self.parts[i]
            x_pos = part[0]
            y_pos = part[1]
            color = "blue"
            if i == 0:
                color = "yellow"
            pygame.draw.rect(surface, color, pygame.Rect(x_pos * CELL_SIZE, y_pos * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def update(self):
        if self.is_game_over():
            print("Game over")
            return

        initial_head_x = self.parts[0][0]
        initial_head_y = self.parts[0][1]

        self.parts[0][0] += self.direction_x
        self.parts[0][1] += self.direction_y

        if len(self.parts) > 1:
            temp = self.parts[1]
            self.parts[1] = [initial_head_x, initial_head_y]

            for i in range(2, len(self.parts)):
                a = self.parts[i]
                self.parts[i] = temp
                temp = a

    def move(self, direction_x, direction_y):
        if len(self.parts) > 1:
            if direction_x == -self.direction_x:
                return
            if direction_y == -self.direction_y:
                return
        self.direction_y = direction_y
        self.direction_x = direction_x
