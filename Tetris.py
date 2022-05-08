from random import choice

import pygame

from settings import *
from Tetromino import *


class Tetris:
    def __init__(self):
        self.score = 0
        self.lines = 0
        self._init_pygame()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.tetromino = None
        self.next = None

    def _init_pygame(self):
        pygame.init()
        pygame.time.set_timer(STEP, 500)
        pygame.display.set_caption("TETRIS - Faton Hoti")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + 300, SCREEN_HEIGHT))

    def run(self):
        SOUND_TETRIS_THEME.play(-1).set_volume(0.1)
        self._spawn_tetromino()
        while True:
            self._handle_events()
            self._game_logic()
            self._draw()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if self.tetromino:
                    if event.key == pygame.K_UP:
                        self.tetromino.rotate()
                        SOUND_ROTATE.play()
                        if self._collision():
                            self.tetromino.rotate(reverse=True)
                    elif event.key == pygame.K_DOWN:
                        self.tetromino.y += 1
                        if self._collision():
                            self.tetromino.y -= 1
                            self._place_tetromino()
                    elif event.key == pygame.K_LEFT:
                        self.tetromino.x -= 1
                        if self._collision():
                            self.tetromino.x += 1
                    elif event.key == pygame.K_RIGHT:
                        self.tetromino.x += 1
                        if self._collision():
                            self.tetromino.x -= 1
                    elif event.key == pygame.K_SPACE:
                        while not self._collision():
                            self.tetromino.y += 1
                        self.tetromino.y -= 1
                        self._place_tetromino()
                        SOUND_BLOCK_DROP.play()
                        SOUND_WHOOSH.play()
                    elif event.key == pygame.K_c:
                        self._spawn_tetromino()
                        SOUND_BLOCK_SWAP.play().set_volume(0.2)
            elif event.type == STEP:
                # Triggers every 500ms
                if not self.tetromino:
                    self._spawn_tetromino()
                else:
                    self.tetromino.y += 1
                    if self._collision():
                        self.tetromino.y -= 1
                        self._place_tetromino()

    def _game_logic(self):
        pass

    def _draw(self):
        self._draw_side_panel()
        self._draw_playfield()
        if self.tetromino:
            self._draw_falling()
        self._draw_next()
        pygame.display.flip()

    def _collision(self):
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

    def _place_tetromino(self):
        t = self.tetromino
        offset_x, offset_y = t.offsets[t.offset]
        shape = t.rotations[t.rotation]
        y = t.y + offset_y  # Field y coordinate
        x = t.x + offset_x  # Field x coordinate
        for r, row in enumerate(shape):  # r is tetromino matrix row
            for c, block in enumerate(row):  # c is tetromino matrix column
                if block:
                    self.grid[y + r][x + c] = t.type
        self.tetromino = None
        self._break_lines()

    def _break_lines(self):
        lines_cleared = 0
        popped_rows = []
        for row in self.grid[::-1]:
            if 0 not in row:
                popped_rows.append(row)
                lines_cleared += 1
        if lines_cleared:
            if lines_cleared < 5:
                SOUND_LINE_REMOVE.play()
            else:
                SOUND_LINE_REMOVE5.play()
            for row in popped_rows:
                self.grid.remove(row)
            self.grid = [[0] * GRID_WIDTH for _ in range(lines_cleared)] + self.grid
            self.score += {1: 100, 2: 300, 3: 500, 4: 750, 5: 1000}.get(
                lines_cleared, 1000
            ) * lines_cleared
            self.lines += lines_cleared

    def _draw_side_panel(self):
        pygame.draw.rect(self.screen, (0, 0, 0), (SCREEN_WIDTH, 0, 300, SCREEN_HEIGHT))
        SCORE_TEXT = FONT_MAIN.render(f"SCORE: {self.score}", True, (255, 255, 255))
        LINES_TEXT = FONT_MAIN.render(f"LINES: {self.lines}", True, (255, 255, 255))
        self.screen.blit(SCORE_TEXT, (SCREEN_WIDTH + 10, 10))
        self.screen.blit(LINES_TEXT, (SCREEN_WIDTH + 10, 40))
        self.screen.blit(
            TETRIS_TEXT,
            (
                SCREEN_WIDTH + 150 - TETRIS_TEXT.get_width() // 2,
                SCREEN_HEIGHT - TETRIS_TEXT.get_height() - 10,
            ),
        )
        self.screen.blit(SCORE_TEXT, (SCREEN_WIDTH + 10, 10))
        self.screen.blit(LINES_TEXT, (SCREEN_WIDTH + 10, 40))
        self.screen.blit(CONTROLS_UP, (SCREEN_WIDTH + 10, 100))
        self.screen.blit(CONTROLS_LEFT, (SCREEN_WIDTH + 10, 130))
        self.screen.blit(CONTROLS_RIGHT, (SCREEN_WIDTH + 10, 160))
        self.screen.blit(CONTROLS_SPACE, (SCREEN_WIDTH + 10, 190))
        self.screen.blit(CONTROLS_C, (SCREEN_WIDTH + 10, 220))

    def _draw_playfield(self):
        # Background
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (0, 0, BLOCK_WIDTH * GRID_WIDTH, BLOCK_HEIGHT * GRID_HEIGHT),
        )
        # Draw tetrominos
        for r, row in enumerate(self.grid):
            for c, block in enumerate(row):
                block = BLOCKS[self.grid[r][c]]
                self._draw_block(block, (c * BLOCK_WIDTH, r * BLOCK_HEIGHT))

    def _draw_falling(self):
        t = self.tetromino
        shape = t.rotations[t.rotation]
        type_ = t.type
        offset_x, offset_y = t.offsets[t.offset]
        for r, row in enumerate(shape):
            for c, block in enumerate(row):
                if block:
                    self._draw_block(
                        BLOCKS[type_],
                        (
                            (t.x + c + offset_x) * BLOCK_WIDTH,
                            (t.y + r + offset_y) * BLOCK_HEIGHT,
                        ),
                    )

    def _draw_block(self, block, position):
        self.screen.blit(block, position)

    def _draw_next(self):
        NEXT_TEXT = FONT_MAIN.render(f"NEXT", True, (255, 255, 255))
        SHAPE = SHAPES[self.next.type]
        self.screen.blit(
            NEXT_TEXT,
            (
                SCREEN_WIDTH + 150 - NEXT_TEXT.get_width() // 2,
                SCREEN_HEIGHT // 2 - SHAPE.get_height() + 50,
            ),
        )
        self.screen.blit(
            SHAPE,
            (
                SCREEN_WIDTH + 150 - SHAPE.get_width() // 2,
                SCREEN_HEIGHT // 2 - SHAPE.get_height() // 2 + 60,
            ),
        )

    def _spawn_tetromino(self):
        if not self.next:
            self.next = choice([I(), O(), T(), S(), Z(), J(), L()])
        self.tetromino = self.next
        self.next = choice([I(), O(), T(), S(), Z(), J(), L()])
        self._draw_falling()
        pygame.display.flip()
        if self._collision():
            self.tetromino = None
            pygame.time.wait(500)
            # self._game_over()
            exit(0)

    def _print_grid(self):
        """For debugging only"""
        print("{")
        for row in self.grid:
            print(" { ", end="")
            for c in row:
                print(f"{c}", end=" ")
            print("}")
        print("}")
