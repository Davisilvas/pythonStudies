"""
Módulos padrão do Python
Módulos são arquivos .py e servem para expandir as funcionalidades padrão da linguagem.
módulos padrão do python na doc da linguagem.
https://docs.python.org/3/py-modindex.html
"""
# import sys  # -> Dessa forma nós estamos importando o módulo inteiro de uma vez.
# from sys import platform # -> Dessa forma nós estamos importando apenas algo específico do módulo, no caso o platform. Aí para usar o que importamos nõs não devemos mais colocar o nome inteiro (sys.platform) e sim usar apenas a palavra platform

# from sys import platform  as pl

import sys
import pymysql
import random

print(sys.platform)

for i in range(10):
    print(random.randint(0, 199))
