"""
Funções - def em Python pt 1
Na func foi atribuído um valor padrão ao argumento, pra quando o usuário esquercer de fornecer essa informação o código já ter uma solução padrão para o problema.
"""


def func(vasco = 'Vasco da grana'): 
    return f'{vasco}'


func()
func('VASCO DA GAMA')
func(vasco = 'Time do povo')


def func2(arg=input('Insira seu nome! '), age=input('Informa a sua idade! ')):
    return f'Olá, {arg}! Você aprendeu a usar o input nos argumentos da função! E sua idade é{age}'


msg = func2()
print(msg)
