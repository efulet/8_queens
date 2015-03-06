"""
@created_at 2014-05-10
@author Exequiel Fuentes <efulet@gmail.com>
"""

class QueensRosetta:
    """Queens define varios metodos para resolver el problema de 8 reinas.
    Para mas informacion, ver: http://en.wikipedia.org/wiki/Eight_queens_puzzle
    Esta clase esta basada en http://rosettacode.org/wiki/N-Queens#Python
    """
    
    def __init__(self, options):
        """Crea una instancia de QueensRosetta.
        
        :param options: Valores opcionales para inicializar las variables de clase
        """
        self.board_size = 8 # quizas esto podria ser asignado por una opcion
        self.options = options
    
    def __under_attack(self, col, queens):
        """Determina si la actual reina ataca alguna pieza en la misma file o 
        columna o diagonal.
        
        :param col: Posicion a evaluar
        :param queens: Las posiciones de las otras reinas
        """
        return col in queens or \
               any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))
    
    def __solve(self):
        """Encuenta todas las posibles soluciones dado el tamano del tablero. 
        Esta solucion esta desarrollada por formulacion incremental. Estos es,
        comienza con un estado vacio y cada iteracion agrega una reina al estado.
        """
        solutions = [[]]
        for row in range(self.board_size):
            solutions = (solution+[i+1]
                           for solution in solutions # la primera clausula es evaluada inmediatamente,
                                                     # entonces "solutions" esta correctamente capturada
                           for i in range(self.board_size)
                           if not self.__under_attack(i+1, solution))
        return solutions
    
    def __board_to_str(self, solutions):
        """Returna una representacion del tablero
        
        :param solutions: Las soluciones
        """
        return " " + "=" * 22 + "\n" + \
            ("\n".join(' # ' * (i-1) + ' Q ' + ' # ' * (self.board_size-i) for i in solutions) + \
            "\n" + " " + "=" * 22 + "\n")
    
    def find_and_print(self):
        """Encuenta e imprime todas las posibles soluciones para el problema de las 8 reinas"""
        chess_number = 1
        for answer in self.__solve():
            print "Tablero: ", chess_number
            print self.__board_to_str(answer)
            chess_number += 1
