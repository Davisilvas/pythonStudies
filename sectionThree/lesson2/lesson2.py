"""
    funções pt2.

    se a função não tiver nenhum return definido, ela vai retornar none.(não valor.)

    depois do return nada mais é executado na função. Logo o return deve estar por último.
"""


def divisao(n1=input('Informe o primeiro número: '), n2=input('Informe o segundo número: ')):
    if n1.isnumeric() and n2.isnumeric():
        nn1 = int(n1)
        nn2 = int(n2)
    else:
        print('Por favor insira apenas números inteiros e positivos.')
    r = nn1 / nn2
    return r


var = divisao()

if var % 2 == 0:
    print(
        f'{var} é um número PAR')
else:
    print(
        f'{var} é um número IMPAR')

def random():
    return 'Alétório', 'demais'
    #isso aqui retorna uma tupla!

var2 = random()
print(var2, type(var2))