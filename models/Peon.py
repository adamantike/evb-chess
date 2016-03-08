# coding=utf-8

from .Pieza import Pieza


class Peon(Pieza):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def __repr__(self):
        return 'Peon (%s) <%d,%d>' % (self.color, self.x, self.y)

    def puede_mover(self, tablero, x, y):
        resultado = False

        # Determina la dirección del movimiento.
        # Si el color del peón es blanco, su movimiento sobre el eje Y es
        # negativo (avanza cuando se reduce el valor de y).
        # Si el color del peón es negro, su movimiento sobre el eje Y es
        # positivo.
        direccion_y = -1 if self.color == 'B' else 1

        # Lógica para los diferentes movimientos posibles del peón.
        # Movimiento frontal
        if self.x == x and self.y + direccion_y == y:
            resultado = not tablero.get_posicion(x, y)
        # Movimiento para comer
        elif x in [self.x - 1, self.x + 1]and self.y + direccion_y == y:
            destino = tablero.get_posicion(x, y)
            resultado = destino and destino.color != 'B'
        # Movimiento frontal doble
        elif (self.x == x
                and self.y + 2 * direccion_y == y
                and ((self.color == 'N' and self.y == 1)
                       or (self.color == 'B' and self.y == 6))):
            resultado = not tablero.get_posicion(x, y)

        return resultado
