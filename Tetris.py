from random import choice
from unittest import case

import pygame

from settings import *
from Tetromino import *

STEP = pygame.USEREVENT


class Tetris:
    def __init__(self):
        pygame.init()
        pygame.time.set_timer(STEP, 500)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.BLOCKS = {
            "I": pygame.image.load("./assets/tiles/tile_red.png"),
            "O": pygame.image.load("./assets/tiles/tile_green.png"),
            "T": pygame.image.load("./assets/tiles/tile_blue.png"),
            "S": pygame.image.load("./assets/tiles/tile_purple.png"),
            "Z": pygame.image.load("./assets/tiles/tile_orange.png"),
            "J": pygame.image.load("./assets/tiles/tile_turquoise.png"),
            "L": pygame.image.load("./assets/tiles/tile_yellow.png"),
            0: pygame.image.load("./assets/tiles/tile_empty.png"),
        }
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.tetrominos = [I(), O(), T(), S(), Z(), J(), L()]
        self.tetromino = choice(self.tetrominos)

    def run(self):


        # GAME LOOP
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.tetromino.rotate()
                    elif event.key == pygame.K_DOWN:
                        self.tetromino.y += 1
                    elif event.key == pygame.K_LEFT:
                        self.tetromino.x -= 1
                    elif event.key == pygame.K_RIGHT:
                        self.tetromino.x += 1
                    elif event.key == pygame.K_SPACE:
                        self.tetromino.drop()
                    else:
                        pass
                elif event.type == STEP:
                    if not self.tetromino:
                        # Generate a new tetromino
                        self.tetromino = choice(self.tetrominos)
                        self.tetromino = J()
                    else:
                        # Move the tetromino down
                        self.tetromino.y += 1

                # Draw playfield
                self.draw_playfield()

                # Draw falling tetromino
                self.draw_falling()

                # Update screen
                pygame.display.flip()

    def draw_playfield(self):
        # Background
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (0, 0, BLOCK_WIDTH * GRID_WIDTH, BLOCK_HEIGHT * GRID_HEIGHT),
        )
        # Draw tetrominos
        for r, row in enumerate(self.grid):
            for c, block in enumerate(row):
                block = self.BLOCKS[self.grid[r][c]]
                self.draw_block(block, (c * BLOCK_WIDTH, r * BLOCK_HEIGHT))

    def draw_falling(self):
        t = self.tetromino
        shape = t.rotations[t.rotation]
        type_ = t.type
        offset_x, offset_y = t.offsets[t.offset]
        for r, row in enumerate(shape):
            for c, block in enumerate(row):
                if block:
                    self.draw_block(
                        self.BLOCKS[type_],
                        (
                            (t.x + c + offset_x) * BLOCK_WIDTH,
                            (t.y + r + offset_y) * BLOCK_HEIGHT,
                        ),
                    )

    def draw_block(self, block, position):
        self.screen.blit(block, position)

    def print_grid(self):
        """For debugging only"""
        print("{")
        for row in self.grid:
            print(" { ", end="")
            for c in row:
                print(f"{c}", end=" ")
            print("}")
        print("}")
