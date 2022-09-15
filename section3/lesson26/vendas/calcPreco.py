import imp
from vendas.formata import preco


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor*porcentagem)/100
    if formata:
        return f'O produto, com aumento, passou a custar {preco.real(r)}!'


def desconto(valor, porcentagem, formata=False):
    r = valor - (valor*porcentagem)/100
    if formata:
        return f'O produto, com desconto, passou a custar {preco.real(r)}!'
    else:
        return r
