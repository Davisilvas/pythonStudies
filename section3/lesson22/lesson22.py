"""
Levantamento de exceções (raise)
"""

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(erro, '|| Informe um divisor diferente de 0.0')
        raise

try:
    divide(15,0)
except ZeroDivisionError as error:
    print(error)

########## MAIS EXEMPLOS ##########

def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1 / n2

try:
    print(divide2(3,0))
except ValueError as error:
    print(error)