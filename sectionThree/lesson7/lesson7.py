"""
Dicionários em python
são similares às listas. Possuem índice e valor.
A diferença é que nas listas os Index são gerados automaticamente. E no dicionário você que controla o index(chave).
Dicionário = estrutura de dados que suporta um par de chave e valor.
# Chaves DEVEM ser únicas em dicionários
PODEMOS TER UM DICIONÁRIO COM OUTROS ANiNHADOS



Uma KEY pode RECEBER um DICIONÁRIO
"""

import copy

d1 = {
    'k1': 'Valor 1',
    'k2': 'Valor 2',
    'arr' : [1,2,3,4]
}

# Pra chamar um valor do dicionário temos que passar o nome da chave entre parênteses.
print(d1['k2'])

print('')
print('Mais exemplos')

# Adicionando itens no dicionário após sua inicialização
d1['k3'] = 'Valor 3'
print(d1)

print('')
print('Mais exemplos')

# Outra forma de fazer um dicionário

# Essa função dict vai criar um dicionário, para ela passamos as chaves e seus valores
d2 = dict(key1=1, key2=2, key3=3)
print(d2)
print(d2['key3'])

print('')
print('Mais exemplos')

# O que fazer quando não temos certeza de que a chave existe no dicionário podemos chamar ela assim:

if 'naoExiste' in d2:
    # caso a gente tente usar essa chave que a gente não tem certeza que existe direto, ela vai dar erro e travar o código
    print(d2['naoExiste'])

# Dessa forma a gente está vendo se ela existe porém sem travar o código
# if d2.get('naoExiste') is not None:
#     print(d2.get('naoExiste'))

print(d2.get('naoExiste'))
print(d2['key3'] ** d2['key2'], '|| Exponenciei uma chave pela outra!!!')

print('')
print('Mais exemplos')

# func update
# a func recebe o nome da chave e o valor desejado entre chaves
d2.update({'key4': 4})
print(d2)

print('')
print('Mais exemplos')

# exclusão de chaves e valores
print(d2, 'ANTES do del')
del d2['key4']
print(d2, 'Após o del')

print('')
print('Mais exemplos')

# Tudo isso vai retornar True, pois as condições dentro do print são verdadeiras
print('key2' in d2)
print(2 in d2.values())  # Checando pelo valor
print('key2' in d2.keys())  # Checando pela chave

print('')
print('Mais exemplos')

# Descovrir quantos pares temos num dicionário
print(len(d2), '|| len de d2')

print('')
print('Mais exemplos')

# iterando sobre o dicionário
for k in d2:  # Acessando somente as CHAVES
    print(k)

for v in d2.values():  # Acessando somente os VALORES
    print(v)

for k in d2.items():  # acessando CHAVE E VALOR em Tuplas
    print(k)

for k in d2.items():
    # imprimindo fora de tuplas, o index 0 é a chave e o 1 o Valor
    print(k[0], k[1])

for k, v in d2.items():  # Desempacotando
    print(k, ':', v)

print('')
print('Mais exemplos')

clientes = {
    'c1': {
        'nome': 'Davi',
        'sobrenome': 'Santos'
    },
    'c2': {
        'nome': 'Maria',
        'sobrenome': 'Xavier'
    },
    'c3': {
        'nome': 'Doly',
        'sobrenome': 'Pancada Seca'
    },
    'c4': {
        'nome': 'Thor',
        'sobrenome': 'Medroso'
    }
}

# Primeiro ta iterando sobre os "pais" e depois sobre os "filhos"
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

print('')
print('Mais exemplos')

v = d1
v['k1'] = 'modificado'
print(d1, 'd1')
print(v)
# Nos dicionários quando a gente usa o sinal de igual a gente não ta cirando um novo obj, então d1 e v são identicos. se alterar um o outro também será

print('')
print('Mais exemplos')
# CRIANDO A CóPIA DE UM DICIONÁrio

v = d1.copy()  # shallowCopy
v['k1'] = 'VASCO'
print(d1, 'd1')
print(v)
# Porem se a gente acessar alguma chave individualmente e fazer alguma alteração nela, a alteração vai contra pros dois

print('')
print('Mais exemplos')

#PARA FAZER UMA DEEPCOPY PRECISAMOS IMPORTAR O MÓDULO COPY E FAZER DA SEGUINTE FORMA. DA FORMA ABAIXO CRIAREMOS DUAS COISAS DIFERENTES NA MEMÓRIA, E NÃO UMA REFERÊNCIA COMO É NA SHALLOW COPY

v = copy.deepcopy(d1) 
v['arr'][0] = 'VASCUDO'
print(d1['arr'][0], 'ESSE É O D1')
print(v['arr'][0], 'ESSE É O v') # Dessa forma um não altera o outro 

print('')
print('Mais exemplos')

#cast de dicionário || dict
print(type(v))

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]
#SE FOREM ARRYAS ASSIM, SEMELHANTES A UM DICT VAI DAR BOM
d3 = dict(lista)
print(d3)

print('')
print('Mais exemplos')

#d2 = dict(key1=1, key2=2, key3=3)
d2.pop('key2') #vai eliminar essa chave
d2.popitem() #vai eliminar o último item independente de qual seja
print(d2)