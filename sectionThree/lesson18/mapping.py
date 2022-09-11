"""
A função map vai aplicar uma função pra cada item da lista de itens
"""

from lesson18 import produtos, pessoas, lista
#from lesson18 import *

new_list = map(lambda x: x * 2, lista)
listaa = [x*2 for x in lista]
print(lista)
print(listaa, 'list comprehension')
print(list(new_list))

print()
print('Mais exemplos')
print()

def juros(p):
    conta = p['preco'] * 1.05
    p['preco'] = round(conta, 2)
    return p

precos = map(juros , produtos)
for i in precos:
    print(i)

print()
print('Mais exemplos')
print()

nomes = map(lambda x:x['nome'], pessoas)
# for i in nomes:
#     print(i)
nomes = list(nomes)
print(nomes)