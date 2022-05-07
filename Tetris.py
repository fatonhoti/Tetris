from random import choice

import pygame

from settings import *
from Tetromino import *

STEP = pygame.USEREVENT


class Tetris:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("monospace", 40)
        pygame.time.set_timer(STEP, 500)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + 300, SCREEN_HEIGHT))
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
        self.score = 0

    def display_score(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (SCREEN_WIDTH, 0, 300, SCREEN_HEIGHT))
        text = self.font.render(f"Score:", True, (255, 255, 255))
        self.screen.blit(text, (SCREEN_WIDTH + 20, 10))
        scr = self.font.render(f"{self.score}", True, (255, 255, 255))
        self.screen.blit(scr, (SCREEN_WIDTH + 200, 12))

    def run(self):

        self.spawn_tetromino()

        # GAME LOOP
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit(0)
                elif event.type == pygame.KEYDOWN:
                    if self.tetromino:
                        if event.key == pygame.K_UP:
                            self.tetromino.rotate()
                            if self.collision():
                                self.tetromino.rotate(True)
                        elif event.key == pygame.K_DOWN:
                            self.tetromino.y += 1
                            if self.collision():
                                self.tetromino.y -= 1
                                self.place_tetromino()
                                self.tetromino = None
                                self.break_lines()
                        elif event.key == pygame.K_LEFT:
                            self.tetromino.x -= 1
                            if self.collision():
                                self.tetromino.x += 1
                        elif event.key == pygame.K_RIGHT:
                            self.tetromino.x += 1
                            if self.collision():
                                self.tetromino.x -= 1
                        elif event.key == pygame.K_SPACE:
                            while not self.collision():
                                self.tetromino.y += 1
                            self.tetromino.y -= 1
                            self.place_tetromino()
                            self.tetromino = None
                            self.break_lines()
                        elif event.key == pygame.K_c:
                            self.spawn_tetromino()
                elif event.type == STEP:
                    if not self.tetromino:
                        self.spawn_tetromino()
                    else:
                        self.tetromino.y += 1
                        if self.collision():
                            self.tetromino.y -= 1
                            self.place_tetromino()
                            self.tetromino = None
                            self.break_lines()

            # Draw playfield
            self.draw_playfield()

            # Draw falling tetromino
            if self.tetromino:
                self.draw_falling()

            self.display_score()

            # Update screen
            pygame.display.flip()

    def collision(self):
        t = self.tetromino
        shape = t.rotations[t.rotation]
        offset_x, offset_y = t.offsets[t.offset]
        y = t.y + offset_y
        x = t.x + offset_x
        for r, row in enumerate(shape):
            for c, block in enumerate(row):
                if block:
                    # Collision with other tetromino
                    if (y + r < GRID_HEIGHT and x + c < GRID_WIDTH) and self.grid[
                        y + r
                    ][x + c] != 0:
                        return True
                    # OOB left OR right
                    if x + c < 0 or x + c >= GRID_WIDTH:
                        return True
                    # OOB floor
                    if y + r >= GRID_HEIGHT:
                        return True
        return False

    def place_tetromino(self):
        t = self.tetromino
        offset_x, offset_y = t.offsets[t.offset]
        shape = t.rotations[t.rotation]
        y = t.y + offset_y
        x = t.x + offset_x
        for r, row in enumerate(shape):
            for c, block in enumerate(row):
                if block:
                    self.grid[y + r][x + c] = t.type

    def break_lines(self):
        lines_cleared = sum(1 for row in self.grid[::-1] if 0 not in row)
        if lines_cleared:
            self.score += {1: 100, 2: 300, 3: 500, 4: 800}[lines_cleared]
            self.grid = [[0] * GRID_WIDTH for _ in range(lines_cleared)] + self.grid[
                : GRID_HEIGHT - lines_cleared
            ]

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

    def spawn_tetromino(self):
        self.tetromino = choice([I(), O(), T(), S(), Z(), J(), L()])
        self.draw_falling()
        pygame.display.flip()
        if self.collision():
            self.tetromino = None
            self.game_over()
            pygame.time.wait(500)
            exit(0)

    def game_over(self):
        # Do something
        pass

    def print_grid(self):
        """For debugging only"""
        print("{")
        for row in self.grid:
            print(" { ", end="")
            for c in row:
                print(f"{c}", end=" ")
            print("}")
        print("}")
