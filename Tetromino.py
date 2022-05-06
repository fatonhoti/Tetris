class Tetromino:
    def __init__(self, x, y, type_):
        self.x = x
        self.y = y
        self.type = type_
        self.offsets = []
        self.offset = 0
        self.rotations = []
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.rotations)

    def drop(self):
        pass


class I(Tetromino):
    def __init__(self):
        super().__init__(3, 0, "I")
        self.offsets = [(0, -1), (-1, 0), (0, 0), (-2, 0)]
        self.rotations = [[4, 5, 6, 7], [1, 5, 9, 13], [0, 1, 2, 3], [2, 6, 10, 14]]
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
        super().__init__(4, 0, "O")
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
        super().__init__(4, 0, "T")
        self.offsets = [(0, -1), (-1, -1), (0, -2), (0, -1)]
        self.rotations = [[8, 9, 10, 5], [5, 9, 13, 10], [8, 9, 10, 13], [5, 9, 13, 8]]
        self.rotations = [
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
                [0, 0, 0, 0],
                [1, 1, 1, 0],
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
        super().__init__(4, 0, "S")
        self.offsets = [(0, -1), (0, 0)]
        self.rotations = [[8, 9, 5, 6], [0, 4, 5, 9]]
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
        super().__init__(4, 0, "Z")
        self.offsets = [(0, -1), (0, 0)]
        self.rotations = [[4, 5, 9, 10], [4, 8, 1, 5]]
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
        super().__init__(4, 0, "J")
        self.offsets = [(0, 0), (0, 0), (-1, 0), (0, -1)]
        self.rotations = [[1, 5, 9, 8], [0, 4, 5, 6], [1, 2, 5, 9], [4, 5, 6, 10]]
        self.rotations = [
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
            [
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
            ],
        ]


class L(Tetromino):
    def __init__(self):
        super().__init__(4, 0, "L")
        self.offsets = [(-1, 0), (0, -1), (0, 0), (0, 0)]
        self.rotations = [[1, 5, 9, 10], [4, 5, 6, 8], [0, 1, 5, 9], [2, 4, 5, 6]]
        self.rotations = [
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [1, 0, 0, 0],
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
