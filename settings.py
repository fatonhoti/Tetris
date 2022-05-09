# The playfield is a 10 by 22 grid of blocks
from pygame import USEREVENT, font, image, mixer

# Event triggers every 500 ms
STEP = USEREVENT

# Font
font.init()
FONT_MAIN = font.Font("./assets/fonts/Blockletter.otf", 30)
TETRIS_TEXT = FONT_MAIN.render("TETRIS", True, (255, 255, 255))
CONTROLS_UP = FONT_MAIN.render("UP:   ROTATE", True, (255, 255, 255))
CONTROLS_LEFT = FONT_MAIN.render("LEFT:   MOVE LEFT", True, (255, 255, 255))
CONTROLS_RIGHT = FONT_MAIN.render("RIGHT:   MOVE RIGHT", True, (255, 255, 255))
CONTROLS_SPACE = FONT_MAIN.render("SPACE:   DROP", True, (255, 255, 255))
CONTROLS_C = FONT_MAIN.render("C:   New Tetromino", True, (255, 255, 255))

# Sound effects
mixer.init()
SOUND_TETRIS_THEME = mixer.Sound("assets/sounds/tetris_theme.ogg")
SOUND_ROTATE = mixer.Sound("./assets/sounds/block_rotate.mp3")
SOUND_BLOCK_DROP = mixer.Sound("./assets/sounds/block_drop.mp3")
SOUND_LINE_REMOVE = mixer.Sound("./assets/sounds/line_remove.wav")
SOUND_LINE_REMOVE5 = mixer.Sound("./assets/sounds/line_remove5.wav")
SOUND_WHOOSH = mixer.Sound("./assets/sounds/whoosh.mp3")
SOUND_BLOCK_SWAP = mixer.Sound("./assets/sounds/block_swap.wav")

# Block images
BLOCKS = {
    "I": image.load("./assets/tiles/tile_red.png"),
    "O": image.load("./assets/tiles/tile_green.png"),
    "T": image.load("./assets/tiles/tile_blue.png"),
    "S": image.load("./assets/tiles/tile_purple.png"),
    "Z": image.load("./assets/tiles/tile_orange.png"),
    "J": image.load("./assets/tiles/tile_turquoise.png"),
    "L": image.load("./assets/tiles/tile_yellow.png"),
    "GHOST": image.load("./assets/tiles/tile_ghost.png"),
    0: image.load("./assets/tiles/tile_empty.png"),
}

SHAPES = {
    "I": image.load("./assets/shapes/shape_i.png"),
    "O": image.load("./assets/shapes/shape_o.png"),
    "T": image.load("./assets/shapes/shape_t.png"),
    "S": image.load("./assets/shapes/shape_s.png"),
    "Z": image.load("./assets/shapes/shape_z.png"),
    "J": image.load("./assets/shapes/shape_j.png"),
    "L": image.load("./assets/shapes/shape_l.png"),
}


GRID_HEIGHT = 22
GRID_WIDTH = 10

# A tetromino is composed of blocks, each block is 10px by 10 px
BLOCK_WIDTH = 30
BLOCK_HEIGHT = BLOCK_WIDTH

# Pygame window sizes
SCREEN_HEIGHT = BLOCK_HEIGHT * GRID_HEIGHT
SCREEN_WIDTH = BLOCK_WIDTH * GRID_WIDTH

# COLORS
RED = "RED"
GREEN = "GREEN"
BLUE = "BLUE"
PURPLE = "PURPLE"
ORANGE = "ORANGE"
TURQUOISE = "TURQUOISE"
YELLOW = "YELLOW"
