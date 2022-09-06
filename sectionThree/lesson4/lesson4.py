"""
ESCOPO
Manipular uma variável de dentro de uma função através do global não é uma boa prática. Devemos passar como argumento para aí então receber essa variável e RETORNAR ela manipulada.
"""

variavel = 'valor' # Escopo global

def func(arg=None):
    arg = arg.replace('v', 'c')
    return arg

def func2():
    #variavel = 'Outro Valor' ESCOPO local. acessível apenas para essa função.
    global variavel
    variavel = 'Outro Valor'
    print(variavel)
    #COMO A VARIÁVEL FOI EDITADA DENTRO DE UMA FUNÇÃO, ESSE ESCOPO DELA NÃO FOI GLOBAL. Logo ela só vai ter esse valor diferente aqui dentro
    #PARA CONSEGUIR ALTERAR ela no escopo global, temos que colocar um global na frente do nome da variável.

alterado = func(variavel)
print(variavel)
print(alterado)
#desta forma manipulamos o valor da variável e atribuímos o retorno desta função a outra variável sem mexer no valor original da variável original
func2()
