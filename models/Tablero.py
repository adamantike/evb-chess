from .Peon import Peon


class Tablero():
    def __init__(self):
        # Inicialización del tablero
        self.tablero = [[None for i in range(8)] for j in range(8)]
        # Carga de peones blancos
        for i in range(8):
            peon = Peon(color='B', x=i, y=6)
            self.tablero[i][6] = peon
        # Carga de peones negros
        for i in range(8):
            peon = Peon(color='N', x=i, y=1)
            self.tablero[i][1] = peon

    def get_posicion(self, x, y):
        return self.tablero[x][y]

    def mover_pieza(self, x1, y1, x2, y2):
        pieza = self.tablero[x1][y1]
        if pieza.puede_mover(self, x2, y2):
            self.tablero[x1][y1] = None
            self.tablero[x2][y2] = pieza
            print("Pieza movida correctamente.")
        else:
            print("La pieza NO se pudo mover.")