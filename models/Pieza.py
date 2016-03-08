class Pieza():
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def puede_mover(self, tablero, x, y):
        raise NotImplementedError
