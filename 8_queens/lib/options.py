"""
@created_at 2014-05-10
@author Exequiel Fuentes <efulet@gmail.com>
"""

from argparse import ArgumentParser

class Options:
    """Esta clase ayuda a manejar algunos argumentos que pueden ser pasados por
    la line a de comando
    
    Por ejemplo, escriba:
    $> ./bin/8_queens.sh --help
    """
    def __init__(self):
        self._init_parser()
    
    def _init_parser(self):
        self.parser = ArgumentParser(usage='main.py [--show]')
        self.parser.add_argument('-s', '--show',
                                 help='show the solutions as a board representation',
                                 action='store_true')
    
    def parse(self, args=None):
        return self.parser.parse_args(args)
