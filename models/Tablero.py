from .Peon import Peon


class Tablero():
    def __init__(self):
        # Inicialización del tablero
        self.tablero = [[None for i in range(8)] for j in range(8)]
        # Carga de peones
        for i in range(8):
            # Peones blancos
            peon_blanco = Peon(color='B', x=i, y=6)
            self.tablero[i][6] = peon_blanco
            # Peones negros
            peon_negro = Peon(color='N', x=i, y=1)
            self.tablero[i][1] = peon_negro

    def get_posicion(self, x, y):
        return self.tablero[x][y]

    def mover_pieza(self, x1, y1, x2, y2):
        pieza = self.tablero[x1][y1]
        if pieza.puede_mover(self, x2, y2):
            self.tablero[x1][y1] = None
            self.tablero[x2][y2] = pieza
            # Actualiza las coordenadas de la pieza.
            pieza.x = x2
            pieza.y = y2
            print("Pieza movida correctamente.")
        else:
            print("La pieza NO se pudo mover.")
