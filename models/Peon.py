from .Pieza import Pieza


class Peon(Pieza):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __repr__(self):
        return 'Peon (%s) <%d,%d>' % (self.color, self.x, self.y)

    def puede_mover(self, tablero, x, y):
        resultado = False
        if self.color == 'B':
            # Movimiento frontal
            if self.x == x and self.y - 1 == y:
                resultado = not tablero.get_posicion(x, y)
            # Movimiento para comer
            elif x in [self.x - 1, self.x + 1] and self.y - 1 == y:
                destino = tablero.get_posicion(x, y)
                resultado = destino and destino.color != 'B'
            # Movimiento frontal doble
            elif self.x == x and self.y - 2 == y == 4:
                resultado = not tablero.get_posicion(x, y)

        return resultado
