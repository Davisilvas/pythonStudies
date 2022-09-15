"""
Uso de try except como condicional
"""


def conversaoNumero(valor):
    # Neste try aninhado eu tratei dois erros, pra converter em int e depois pra converter em float. E no if eu tratei pra caso o valor venha como uma letra.
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = conversaoNumero(input('Digite um número: '))

if numero is None:
    print('Isso não é número')
else:
    print(numero * 5)
