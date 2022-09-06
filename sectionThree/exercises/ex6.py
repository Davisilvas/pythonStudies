# def mestre(arg1, arg2):
#     return arg1(), arg2()

# def func1(saudacao):
#     return saudacao

# def func2(nome, idade):
#     return nome, idade

# x = mestre(func1('Boa Tarde'), func2('Davi', '21'))
# print(x)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(saudar, nome):
    return f'{saudar}, {nome}'


exec2 = mestre(fala_oi, 'Davi')
executar = mestre(saudacao, 'Boa Tarde', 'Davi')
print(exec2)
print(executar)
