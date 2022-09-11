"""
A função filter serve pra filtrar as coisas. E essa função retorna um iterator.

A função filter retorna true ou false pra função que lhe é passada como parâmetro. No exemplo abaixo, tudo que for true pra expressão x>5 vai ser atribuido à nova lista.

a necessidade de fazer algo mais complexo a ponto de necessitar de uma função separada pra passar no filter é rara
"""

from data import *


newList = filter(lambda x: x > 5, lista)
# nn = [x for x in lista if x > 5]
# print(nn) Forma com List Comprehension

for i in newList:
    print(i)

print()
print('Mais exemplos')
print()

# def maiorQue10(p):
#     if p['preco'] > 40:
#         return p


def maiorQue10(p):
    if p['preco'] > 40:
        p['e_caro'] = True
    return True


caros = filter(maiorQue10, produtos)
# caros = filter(lambda p: p['preco'] > 40, produtos)
for p in caros:
    print(p)
