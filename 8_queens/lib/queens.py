"""
@created_at 2014-05-10
@author Exequiel Fuentes <efulet@gmail.com>
"""

import numpy
from collections import deque
import copy

from queens_exception import QueensException

class Queen:
    """La clase Queen representa a una reina"""
    
    def __init__(self):
        """Crea una instancia de la clase Queen."""
        self.row = -1
        self.column = -1
    
    def is_valid(self):
        """Verifica si la reina tiene asignada una posicion"""
        if self.row != -1 and self.column != -1:
            return True
        else:
            return False
    
    def is_attacking(self, queen):
        """Determina si la actual reina esta atacando a la reina pasada
        
        :param queen: La reina a comparar con la actual reina
        """
        if self.row == queen.row or self.column == queen.column: return True
        if abs(self.row-queen.row) == abs(self.column-queen.column): return True
        return False

class Board:
    """La clase Board representa al tablero"""
    def __init__(self, board_size):
        """Crea una instancia de Board.
        
        :param board_size: Tamano del tablero
        """
        self.board_size = board_size
        self.queens = []
        self.depth_index = 0 # indica la profundidad en el arbol
    
    def get_depth(self):
        return self.depth_index
    
    def increment_depth(self):
         self.depth_index += 1
    
    def set_queen(self, row, column):
        """Asigna una posicion a la reina si no ataca a otra
        
        :param row: Fila en el tablero
        :param column: Columns en el tablero
        """
        tmp_queen = Queen()
        tmp_queen.row = row
        tmp_queen.column = column
        
        for queen in self.queens:
            if queen.is_valid() and tmp_queen.is_attacking(queen): return False
        
        self.queens.append(tmp_queen)
        
        return True
        
    
    def is_valid(self):
        """Verifica si el tablero es valido"""
        if len(self.queens) == self.board_size: return True
        return False
    
    def board_to_str(self):
        """Retorna una representacion del tablero"""
        board_str = "  "
        for i in xrange(self.board_size):
            board_str += `i+1` + ' '
        board_str += "\n"
        for i in xrange(self.board_size):
            cols_str = []
            queen = self.queens[i]
            for j in xrange(self.board_size):
                if queen.row == i and queen.column == j:
                    cols_str.append('Q')
                else:
                    cols_str.append('#')
            board_str += `i+1` + ' ' + ' '.join(cols_str) + "\n"
        
        return board_str

# States: Any arrangement of 0 to 8 queens on the board is a state.
# Initial state: No queens on the board.
# Transition model: Returns the board with a queen added to the specified 
# square.
# Goal test: 8 queens are on the board, none attacked.
class Queens:
    """La clase Queens define varios metodos para resolver el problem de las 8 reinas.
    Esta solucion comienza con un tablero vacio, en cada action se agrega una 
    reina al tablero si esta no ataca a las otras reinas.
    """
    
    def __init__(self, options):
        """Crea una instancia de la clase Queens
        
        :param options: Valores opcionales para inicializar las variables de clase
        """
        self.board_size = 8
        self.options = options
    
    def __create_board(self):
        """Create un tablero vacio"""
        return Board(self.board_size)
    
    def __print_board(self, solutions):
       """Imprime las soluciones
       
       :param solutions: La lista de soluciones para imprimir
       """
       chess_number = 1
       for board in solutions:
           print "Tablero: ", chess_number
           print board.board_to_str()
           chess_number += 1
    
    def __get_successors(self, current_board):
        """Retorna los siguientes sucesores
        
        :param current_board: Es el actual tablero
        """
        new_board_successors = []
        
        for col in xrange(self.board_size):
            board_successor = copy.deepcopy(current_board)
            if board_successor.set_queen(board_successor.get_depth(), col):
                board_successor.increment_depth()
                new_board_successors.append(board_successor)
        
        return new_board_successors
    
    # DFS is based on stack data structure.
    def depth_first_search(self):
        """Encuentra todas las posibles soluciones usando el algoritmo Depth-First."""
        initial_state = self.__create_board()
        open_states = []
        open_states.append(initial_state)
        valid_boards = []
        
        while open_states:
            current_board = open_states.pop()
            if current_board.is_valid():
                valid_boards.append(current_board)
            else:
                # Genera proximos estados
                new_boards = self.__get_successors(current_board)
                for new_board in new_boards:
                    open_states.append(new_board)
        
        # Imprime las soluciones
        print "Fueron encontradas:", len(valid_boards), "soluciones"
        if self.options.show: self.__print_board(valid_boards)
    
    def __ids_helper(self, max_depth):
        """Basicamente es el mismo algoritmo DFS pero con un limite
        
        :param max_depth: Indica la profundidad maxima
        """
        initial_state = self.__create_board()
        open_states = []
        open_states.append(initial_state)
        valid_boards = []
        
        current_depth = 0
        while open_states:
            current_board = open_states.pop()
            if current_board.is_valid():
                print "Solucion encontrada en la profundidad:", current_depth
                valid_boards.append(current_board)
            else:
                # Genera proximos estados pero con limite
                if current_depth < max_depth:
                    new_boards = self.__get_successors(current_board)
                    for new_board in new_boards:
                        open_states.append(new_board)
                    current_depth += 1
        
        
        return valid_boards
    
    # IDS operates like a DFS (stack data structure), except slightly more 
    # constrained --there is a maximum depth which defines how many levels 
    # deep the algorithm can look for solutions.
    def iterative_deepening_search(self):
        """Encuentra todas las posibles soluciones usando el algoritmo Iterative Deepening."""
        valid_boards = []
        
        # La profundidad maxima sera el tamano del tablero
        for i in xrange(self.board_size):
            temp_boards = self.__ids_helper(i)
            if temp_boards: valid_boards.append(temp_boards)
        
        # Imprime las soluciones
        print "Fueron encontradas:", len(valid_boards), "soluciones"
        if self.options.show: self.__print_board(valid_boards)
    
    # BFS is based on queue data structure.
    def breadth_first_search(self):
        """Encuentra todas las posibles soluciones usando el algoritmo Breadth-First."""
        initial_state = self.__create_board()
        open_states = []
        open_states = deque([])
        open_states.append(initial_state)
        valid_boards = []
        
        while open_states:
            current_board = open_states.popleft()
            if current_board.is_valid():
                valid_boards.append(current_board)
            else:
                # Genera proximos estados
                new_boards = self.__get_successors(current_board)
                for new_board in new_boards:
                    open_states.append(new_board)
        
        # Imprime las soluciones
        print "Fueron encontradas:", len(valid_boards), "soluciones"
        if self.options.show: self.__print_board(valid_boards)
