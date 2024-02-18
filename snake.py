import pygame
from utils import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class Snake:
    def __init__(self, start_pos: list):
        self.parts = [start_pos]
        self.direction_x = 1
        self.direction_y = 0

    def is_game_over(self) -> bool:
        head_x = self.parts[0][0]
        head_y = self.parts[0][1]
        return head_x * CELL_SIZE >= SCREEN_WIDTH or head_y * CELL_SIZE >= SCREEN_HEIGHT or head_x * CELL_SIZE < 0 or head_y * CELL_SIZE < 0

    def grow(self, food_pos=None):
        last_part = self.parts[-1]
        if len(self.parts) > 1:
            second_last_part = self.parts[-2]
            if last_part[0] == second_last_part[0]:
                new_x_pos = last_part[0]
                new_y_pos = -second_last_part[1]
                self.parts.append([new_x_pos, new_y_pos])
            elif last_part[1] == second_last_part[1]:
                new_x_pos = -second_last_part[0]
                new_y_pos = last_part[1]
                self.parts.append([new_x_pos, new_y_pos])
        else:
            if self.direction_x == 0:
                x_pos = self.parts[0][0]
                y_pos = -self.parts[0][1]
                self.parts.append([x_pos, y_pos])
            if self.direction_y == 0:
                x_pos = -self.parts[0][0]
                y_pos = self.parts[0][1]
                self.parts.append([x_pos, y_pos])


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
