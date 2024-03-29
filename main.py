import pygame
from utils import *
from snake import Snake


class Game:
    def __init__(self):
        # Pygame stuff
        pygame.init()
        pygame.display.set_caption("Snake Game")

        # Snake
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.snake = Snake([2, 0])

        # Clock
        self.clock = pygame.time.Clock()

        # Food
        x_pos, y_pos = get_random_food_pos()
        # Create the rect for the food
        self.food = pygame.Rect(x_pos * CELL_SIZE, y_pos * CELL_SIZE, CELL_SIZE, CELL_SIZE)

        # Score
        self.high_score = get_high_score()
        self.score = 0
        self.score_font = get_font(64)

        self.game_over_surface = self.score_font.render("GAME OVER! Press 'R' to restart.", True, "white")
        self.game_over = False

    def draw_grid(self):
        # Draw vertical lines
        for i in range(CELL_SIZE, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, "#7c7d7c", (i, 0), (i, SCREEN_HEIGHT))

        # Draw horizontal lines
        for i in range(CELL_SIZE, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, "#7c7d7c", (0, i), (SCREEN_WIDTH, i))

    def manage_eating(self):
        # Check if snake is in the same cell as the food
        if self.snake.parts[0][0] == self.food.left // CELL_SIZE and self.snake.parts[0][1] == self.food.top // CELL_SIZE:
            # Make the snake grow
            self.snake.grow()

            # Increase score
            self.score += 1
            if self.score > self.high_score:
                set_high_score(self.score)

            # Spawn the food at next random position
            x_pos, y_pos = get_random_food_pos()
            self.food.left = x_pos * CELL_SIZE
            self.food.top = y_pos * CELL_SIZE

    def restart_game(self):
        self.snake.parts.clear()
        self.snake.parts.append([0, 0])
        x_pos, y_pos = get_random_food_pos()
        self.food.left = x_pos * CELL_SIZE
        self.food.top = y_pos * CELL_SIZE
        self.game_over = False
        self.score = 0

        # Set the game over bool back to false
        self.game_over = False


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.move(0, -1)
                    if event.key == pygame.K_DOWN:
                        self.snake.move(0, 1)
                    if event.key == pygame.K_LEFT:
                        self.snake.move(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        self.snake.move(1, 0)
                    if self.game_over:
                        if event.key == pygame.K_r:
                            self.restart_game()

            self.clock.tick(FPS)
            self.screen.fill("#212121")
            score_surface = self.score_font.render(f"{self.score}", True, "white")
            self.screen.blit(score_surface, (SCREEN_WIDTH // 2, CELL_SIZE))

            # Snake
            self.snake.draw(self.screen)
            self.game_over = self.snake.is_game_over()
            if self.game_over:
                self.screen.blit(self.game_over_surface, (100, (SCREEN_HEIGHT // 2) - 128))
            else:
                self.draw_grid()
                self.snake.update()

            # Manage the eating mechanism of the snake
            self.manage_eating()

            # Draw the food
            pygame.draw.rect(self.screen, FOOD_COLOR, self.food)
            pygame.display.update()


if __name__ == "__main__":
    Game().run()
