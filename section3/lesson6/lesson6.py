"""
TUPLAS

A diferença da tupla para a Lista é que a gente não pode editar os elementos da Tupla|| não pode adicionar, remover ou alterar os valores
"""

t1 = (1, 2, 3, 'Davi', True)
print(t1, type(t1))
print(t1[3])

print('')
print('Mais exemplos')

# iteração em uma Tupla
# for v in t1:
#     print(v)

print('')
print('Mais exemplos')

# fatiando
print(t1[2:])  # do segundo índice até o final
print(t1[::2])  # percorrendo a tupla toda de 2 em 2

print('')
print('Mais exemplos')

# criando uma Tupla sem os parenteses
t2 = 4, 5, 6, 'Santos', False
print(t2, type(t2))
# t3 = 1 <- ASSIM EU CRIEI UM INTEIRO
# t3 = 1, <- ASSIM EU CRIEI UMA TUPLA

print('')
print('Mais exemplos')

# concatenando Tuplas
t3 = t1 + t2
print(t3, type(t3))
# desempacotando isso tudo
n1, n2, n3, n4, *_ = t3
print(n4)

print('')
print('Mais exemplos')

# t3 = (t1 + t2) * 10 vai repetir esse valor 10x na variável

# CAST DE TUPLE PARA LIST
t3 = list(t3)
# agora podemos manipular os valores livremente. Adicionar, deletar e alterar
print(t3, type(t3))
