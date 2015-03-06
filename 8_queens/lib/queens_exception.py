"""
@created_at 2014-05-10
@author Exequiel Fuentes <efulet@gmail.com>
"""

class QueensException(Exception):
    """QueensException maneja las excepciones para la clase Queens
    
    Como usar esta clase:
      raise QueensException("Testing QueensException")
    """

    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)
