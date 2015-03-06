"""
@created_at 2014-05-10
@author Exequiel Fuentes <efulet@gmail.com>
"""

import traceback
import sys
import datetime

from lib import Options
from lib import QueensRosetta
from lib import Queens

def check_version():
    """Python v2.7 es requerida por el curso, entonces verificamos la version"""
    if sys.version_info[:2] != (2, 7):
        raise Exception("Parece que python v2.7 no esta instalada en tu sistema")

if __name__ == '__main__':
    try:
        # Verificar version de python
        check_version()
        
        options = Options()
        opts = options.parse(sys.argv[1:])
        
        # Este es una solucion de http://rosettacode.org/wiki/N-Queens#Python
        #q = QueensRosetta(opts)
        #q.find_and_print()
        
        # Solucion basada en estados
        q1 = Queens(opts)
        
        print "Ejecutando Depth-First Search..."
        start = datetime.datetime.now()
        q1.depth_first_search()
        print "La ejecucion tomo:", str(datetime.datetime.now() - start)
        
        print "Ejecutando Breadth-First Search..."
        start = datetime.datetime.now()
        q1.breadth_first_search()
        print "La ejecucion tomo:", str(datetime.datetime.now() - start)
        
        print "Ejecutando Iterative Deepening Search..."
        start = datetime.datetime.now()
        q1.iterative_deepening_search()
        print "La ejecucion tomo:", str(datetime.datetime.now() - start)
        
    except Exception, err:
        print traceback.format_exc()
