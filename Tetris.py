import pygame

# The playfield is a 10 by 22 grid of blocks
GRID_HEIGHT = 22
GRID_WIDTH = 10

# A tetromino is composed of blocks, each block is 10px by 10 px
BLOCK_WIDTH = 30
BLOCK_HEIGHT = BLOCK_WIDTH

# Pygame window sizes
SCREEN_HEIGHT = BLOCK_HEIGHT * GRID_HEIGHT
SCREEN_WIDTH = BLOCK_WIDTH * GRID_WIDTH

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.grid[0][0] = 1
        self.grid[0][2] = 1
        self.grid[0][4] = 1
        self.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
    
    def draw(self):
        # Draw tetrominos
        for r, row in enumerate(self.grid):
            for c, block in enumerate(row):
                # Background block
                pygame.draw.rect(self.screen, BLACK, (c * BLOCK_WIDTH, r * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT))
                if block:
                    # Tetromino block
                    pygame.draw.rect(self.screen, ORANGE, (c * BLOCK_WIDTH, r * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT))
        # Draw falling tetromino

        # Update screen
        pygame.display.flip()

    def print_grid(self):
        """For debugging only"""
        print("{")
        for row in self.grid:
            print(" { ", end="")
            for c in row:
                print(f"{c}", end=" ")
            print("}")
        print("}")