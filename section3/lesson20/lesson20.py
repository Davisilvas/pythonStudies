"""
REDUCE
Essa função vai fazer a acumulação de valores.
"""

from functools import reduce
from dado import *

# A cada volta nesse loop a função vai guardar o valor da soma no AC
soma = reduce(lambda ac, i: i + ac, lista, 0)
print(soma)

print()
print('Mais exemplos')
print()

# fazendo com dict || somar o total dos produtos.

somaPrecos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(somaPrecos / len(produtos))
