
nome = input('Qual o seu nome? ')

# checando se o primeiro lado é True, se for False executa a próxima expressão. Ele para na primeira expressão verdadeira que achar.
print(nome or None or False or 0 or 'Você não digitou nada :(' or '123')

# if nome:
#     print(nome)
# else:
#     print('vc n digitou nada')

a = 0
b = None
c = False
d = []
e = {}
f = 21
g = 'Davi'

var = a or b or c or d or e or f or g
print(var)