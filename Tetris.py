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


class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.print_grid()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

    def print_grid(self):
        """For debugging only"""
        print("{")
        for row in self.grid:
            print(" { ", end="")
            for c in row:
                print(f"{c}", end=" ")
            print("}")
        print("}")