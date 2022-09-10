"""
List comprehension
são usadas para otimização - perfomance
escrever menos linhas. 
"""

l1 = [1, 2, 3, 4, 5]
l2 = [v for v in l1]
l3 = [value * 2 for value in l1]
# l4 = [value print(value * 2 f'Linha {value}') for value in l1]
l5 = [(v, v2) for v in l1 for v2 in range(3)]

print(l2, 'ESSE É O L2')
print()
print(l1, 'ESSE É O L1')
print()
print(l3, 'ESSE É O L3')
print()
# print(l4, 'ESSE É O L4')
print(l5, 'ESSE É O L5')
print()

lStr = ['Davi', 'Maria', 'Doly']
lStr2 = [v.replace('a', '@').upper() for v in lStr]
print(lStr2, 'Esse é o lStr2')
print()

##########################################################

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

tupla2 = [(y, x) for x, y in tupla]  # inverteu os valores da TUPLA
print(tupla2, 'Essa é a tupla2')
tupla2 = dict(tupla2)
print(tupla2, 'Essa é a tupla2 CONVERTIDA pra DICT')
print()
##########################################################

lista3 = list(range(16))
# Para mostrat somente os divisíveis por 3
ex1 = [v for v in lista3 if v % 3 == 0]
print(ex1, 'Esse é o ex1')
print()
# Para pegar todos os números que são divisíveis por 2 E por 3
ex2 = [v for v in lista3 if v % 3 == 0 if v % 2 == 0]
print(ex2, 'Esse é o ex2')
print()
# Para usar o ELSE || A gente passa o if com o else antes do FOR
ex3 = [v if v % 2 == 0 else f'{v} não é divisível por 2' for v in lista3]
print(ex3, 'Esse é o ex3')
print()
#Adicionando mais uma condição 
ex4 = [v if v % 2 == 0 and v % 3 == 0 else f'{v} não é divisível por 2' for v in lista3]
print(ex4, 'Esse é o ex4')
print()
