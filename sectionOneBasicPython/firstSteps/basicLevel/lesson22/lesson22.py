"""
split, join, enumarate
split - dividir uma STRING #str divide uma str gerando um array com os itens
join - juntar um array #str transforma uma lista em uma string
enumerate - enumerar elementos do array #array / objetos iteraveis

brasil.split - a gente pegou tudo o que era separado por ' '(espaço) logo pegamos todas as palavras

no join a gente coloca entre '' o que vamos usar de separador e depois da o .join

enumerate ''cria'' um índice pra cada valor do array
"""

brasil = 'O Brasil é o país do futebol. O Brasil é pentacampeão'

lista = brasil.split(' ')

for x in lista:
    print(x)
print('  ')
print('Mais exemplos')

stringBr = ' '.join(lista)

print(stringBr)

print('  ')
print('Mais exemplos')
for index, value in enumerate(lista):
    print(index, value)

print('  ')
print('Mais exemplos')

for i, n in enumerate(stringBr):
    print(i,n)

# desempacotamento - enumarate faz isso, agora segue outra forma de fazer
print('  ')
print('Mais exemplos')

arr = [
    'Davi',
    'Maria',
    'Doly'
]

n1, n2, n3 = arr

print(n3)

for v1 in enumerate(arr,78):
    valor_enumerado, minha_lista = v1 #desempacotei o resultado da func enumerate
    print(v1)

#o enumerate vai pegar um elemento que você pode percorrer um for nele e e vai enumerar esse elemento conforme você mandar ele fazer enumerate(arr, 78).
#o enumerate gera uma tupla