"""
Formatando valores com modificadores


:s - texto - strings
:d - inteiros - int
:f - números de ponto flutuante - float
:.(NÚMERO)f - quantidade de casas decimais - float
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - direita
< - esquerda
^ - centro
"""

v1 = 10
v2 = 3
r = v1/v2
nome = 'Davi Silva santos'

print('{:.2f}'.format(r)) #Formatando a quantidade de casas decimais que o número vai mostrar
print(f'{nome}')
print(f'{v1:0^5}')

print('###')
nome_formatado = '{:@>18}'.format(nome)
nome_formatado1 = '{n:@>18} {n:@>19} {n:@>20}'.format(n=nome)
print(f'{nome_formatado}')
print(f'{nome_formatado1}')

print('###')
print(nome.lower())
print(nome.upper())
print(nome.title())
