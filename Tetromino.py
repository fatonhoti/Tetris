START_Y = 0


class Tetromino:
    def __init__(self, x, y, type_):
        self.x = x
        self.y = y
        self.type = type_
        self.offsets = []
        self.offset = 0
        self.rotations = []
        self.rotation = 0

    def rotate(self, reverse=False):
        if reverse:
            self.rotation = (self.rotation - 1) % len(self.rotations)
        else:
            self.rotation = (self.rotation + 1) % len(self.rotations)


class I(Tetromino):
    def __init__(self):
        super().__init__(3, START_Y, "I")
        self.offsets = [(0, -1), (-1, 0), (0, 0), (-2, 0)]
        self.rotations = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
            ],
            [
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
            ],
        ]


class O(Tetromino):
    def __init__(self):
        super().__init__(4, START_Y, "O")
        self.offsets = [(-1, -1)]
        self.rotations = [
            [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ]
        ]


class T(Tetromino):
    def __init__(self):
        super().__init__(4, START_Y, "T")
        self.offsets = [(0, -2), (0, -1), (-1, -1), (0, -1)]
        self.rotations = [
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
            ],
            [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
            ],
            [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
            ],
        ]


class S(Tetromino):
    def __init__(self):
        super().__init__(4, START_Y, "S")
        self.offsets = [(0, -1), (0, 0)]
        self.rotations = [
            [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [1, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
            ],
        ]


class Z(Tetromino):
    def __init__(self):
        super().__init__(4, START_Y, "Z")
        self.offsets = [(0, -1), (0, 0)]
        self.rotations = [
            [
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 1, 0, 0],
                [1, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 0],
            ],
        ]


class J(Tetromino):
    def __init__(self):
        super().__init__(4, START_Y, "J")
        self.offsets = [(0, -1), (0, 0), (0, 0), (-1, 0)]
        self.rotations = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [1, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
            ],
        ]


class L(Tetromino):
    def __init__(self):
        super().__init__(4, START_Y, "L")
        self.offsets = [(0, -1), (-1, 0), (0, 0), (0, 0)]
        self.rotations = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ],
            [
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
        ]
