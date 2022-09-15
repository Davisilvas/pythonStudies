"""
Funções em Python parte 3
após argumentos com valores padrões só podemos adicionar argumentos assim. Ou seja, após o argumento nome abaixo, não podemos colocar argumentos normais.

PASSANDO ARGUMENTOS INDEFINIDOS, E TAMBÉM DESEMPACOTADOS

"""


def func(a1, a2, a3, a4, a5, nome=None):
    print(a1, a2, a3, a4, a5, nome)


func(1, 2, 'a', 3, 4, nome='Davi')

print('')
print('Mais um')
# daqui pra baixo função com número ilimitado de argumentos

# quando colocamos os argumentos dessa forma o python cria uma tupla com eles, pra manipular livremente temos que fazer um cast e transformar em array


def x(*args):  # é como se fosse um empacotamento
    args = list(args)
    args[1] = 'Um'
    print(args)
    print(len(args))
    print(args[0])
    print(args[-1])

# arr = [1,2,3,4,5]
# print(*arr, sep='-') uma forma de desempacotar rápido || sep coloca um separador


x(1, 2, 3, 4, 5)

###########################
print('')
print('Mais um exemplo')


def funcao(*args, **kwargs):
    print(args)
    print(kwargs['nome'],kwargs['sobrenome'])
    nome = kwargs.get('nome')
    print(nome)
    #essa segunda forma acima é a melhor forma de se pegar os kwargs, pois se for algo que não exite, vai retornar none e não um erro. Permite criar condicionais.

#aqui, para a gente não ter uma lista no índice 0 da tupla e uma sequência de dados normais na tupla a gente desempacotou a lista no momento em que a gente passou ela como argumento.
# **kwargs = key word args || argumentos com palavras chave. argumentos nomeados
lista = [1, 2, 3]
lista2 = [10, 20, 30]
funcao(*lista, *lista2, nome='Davi', sobrenome='Santos')
# no terminal vamos ter {'nome': 'Davi', 'sobrenome': 'Santos'} que são as chaves e valores.
